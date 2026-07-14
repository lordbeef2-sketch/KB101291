# NI DOCUMENT BUNDLE: ni-xnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-xnet-api-ref start=251 end=290 -->
<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetpduproperties_c.html language=enus -->
## TOPIC 00251: ni-xnet-api-ref/xnetpduproperties_c.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetpduproperties_c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetpduproperties_c.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET PDU Properties

XNET PDU Properties

This section includes the XNET PDU properties.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetpdupropertynode.html language=enus -->
## TOPIC 00252: ni-xnet-api-ref/xnetpdupropertynode.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetpdupropertynode.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetpdupropertynode.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET PDU Property Node

XNET PDU Property Node

#### Format

[IMAGE alt='image' src='xnetpdupropertynode.gif']

#### Description

Property node used to read/write properties for an XNET PDU I/O name.

Pull down this node to add properties. Right-click to change direction between read and write. Right-click each property name to create a constant, control, or indicator.

For help on a specific property, open the LabVIEW context help window (<Ctrl-H>) and move your cursor over the property name.

For more information about LabVIEW property nodes, open the main LabVIEW help (select **Search the LabVIEW Help...** from the **Help** menu) and look for the *Property Nodes* topic in the index.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadsignalsinglepointvi.html language=enus -->
## TOPIC 00253: ni-xnet-api-ref/xnetreadsignalsinglepointvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadsignalsinglepointvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadsignalsinglepointvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (Signal Single-Point).vi

XNET Read (Signal Single-Point).vi

#### Purpose

Reads data from a session of Signal Input Single-Point mode.

#### Format

[IMAGE alt='image' src='xnetreadsignalsinglepoint.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Signal Input Single-Point. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | data returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point. Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list. The data returns the most recent value received for each signal. If multiple frames for a signal are received since the previous call to the XNET Read (Signal Single-Point) VI (or session start), only signal data from the most recent frame is returned. If no frame is received for the corresponding signals since you started the session, the signal Default Value is returned. For an example of how this data applies to network traffic, refer to Signal Input Single-Point Mode. A trigger signal returns a value of 1.0 or 0.0, depending on whether its frame arrived since the last Read (or Start) or not. For more information about trigger signals, refer to Signal Input Single-Point Mode. |
|  | error out is the error cluster output (refer to Error Handling). |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadsignalwaveformvi.html language=enus -->
## TOPIC 00254: ni-xnet-api-ref/xnetreadsignalwaveformvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadsignalwaveformvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadsignalwaveformvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (Signal Waveform).vi

XNET Read (Signal Waveform).vi

#### Purpose

Reads data from a session of Signal Input Waveform mode.

The data represents a waveform of resampled values for each signal in the session. You can wire the data directly to a LabVIEW Waveform Graph for display.

#### Format

[IMAGE alt='image' src='xnetreadsignalwaveform.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Signal Input Waveform. |
| --- | --- |
|  | number to read is the number of samples desired. If number to read is positive (or 0), the number of samples returned (size of Y arrays) is no greater than this number. If timeout is nonzero, the number returned is exactly this number on success. If number to read is negative (typically –1), the maximum number of samples is returned. If number to read is negative, you must use a timeout of zero. This input is optional. The default value is –1. |
|  | timeout is the time to wait for number to read samples to become available. The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds. If timeout is positive, the XNET Read (Signal Waveform) VI waits for number to read samples, then returns that number. If the samples do not arrive prior to the timeout, an error is returned. If timeout is negative, the XNET Read (Signal Waveform) VI waits indefinitely for number to read samples. If timeout is zero, the XNET Read (Signal Waveform) VI does not wait and immediately returns all available samples up to the limit number to read specifies. Because time determines sample availability, typical values for this timeout are 0 (return available) or a large positive value such as 100.0 (wait for a specific number to read). This input is optional. The default value is 0.0. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | data returns a one-dimensional array of LabVIEW waveforms. Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list. The waveform elements are: t0 is the waveform start time. This is a LabVIEW absolute timestamp that specifies the time for the first sample in the Y array. dt is the waveform delta time. This is a LabVIEW relative time that specifies the time between each sample in the Y array. LabVIEW relative time is represented as 64-bit floating point in units of seconds. The waveform dt always is the inverse of the XNET Session Resample Rate property. Y is the array of resampled signal values. Each signal value is scaled, 64-bit floating point. The Y array size is the same for all waveforms returned, because it is determined based on time, and not the number of frames received. If no frame is received for the corresponding signals since you started the session, the XNET Signal Default Value is returned. For an example of how this data applies to network traffic, refer to Signal Input Waveform Mode. |
|  | t0 is the waveform start time. This is a LabVIEW absolute timestamp that specifies the time for the first sample in the Y array. |
|  | dt is the waveform delta time. This is a LabVIEW relative time that specifies the time between each sample in the Y array. LabVIEW relative time is represented as 64-bit floating point in units of seconds. The waveform dt always is the inverse of the XNET Session Resample Rate property. |
|  | Y is the array of resampled signal values. Each signal value is scaled, 64-bit floating point. The Y array size is the same for all waveforms returned, because it is determined based on time, and not the number of frames received. If no frame is received for the corresponding signals since you started the session, the XNET Signal Default Value is returned. |
|  | error out is the error cluster output (refer to Error Handling). |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadsignalxyvi.html language=enus -->
## TOPIC 00255: ni-xnet-api-ref/xnetreadsignalxyvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadsignalxyvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadsignalxyvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (Signal XY).vi

XNET Read (Signal XY).vi

#### Purpose

Reads data from a session of Signal Input XY mode.

#### Format

[IMAGE alt='image' src='xnetreadsignalxy.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Signal Input XY. |
| --- | --- |
|  | number to read is the number of values desired. If number to read is positive (or 0), the size of value arrays is no greater than this number. If number to read is negative (typically –1), the maximum number of values is returned. This input is optional. The default value is –1. If number to read values are received for any signal, the XNET Read (Signal XY) VI returns those values, even if the time limit has not occurred. Therefore, to read values up to the time limit, leave number to read unwired (–1). |
|  | time limit is the timestamp to wait for before returning signal values. If time limit is valid, the XNET Read (Signal XY) VI waits for the timestamp to occur, then returns available values (up to number to read). If you increment time limit by a fixed number of seconds for each call to the XNET Read (Signal XY) VI, you effectively obtain a moving window of signal values. If time limit is unwired (invalid), the XNET Read (Signal XY) VI returns immediately all available values up to the current time (up to number to read). This input is optional. The default value is an invalid timestamp. The timeout of other XNET Read VI instances specifies the maximum amount time to wait for a specific number to read values. The time limit of the XNET Read (Signal XY) VI does not specify a worst-case timeout value, but rather a specific absolute timestamp to wait for. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | data returns an array of LabVIEW clusters. Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list. Each cluster contains two arrays, one for timestamp and one for value. For each signal, the size of the timestamp and value arrays always is the same, such that it represents a single array of timestamp/value pairs. Each timestamp/value pair represents a value from a received frame. When signals exist in different frames, the array sizes may be different from one cluster (signal) to another. The cluster elements are: timestamp is the array of LabVIEW timestamps, one for each frame received that contains the signal. Each timestamp represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds. value is the array of signal values, one for each frame received that contains the signal. Each signal value is scaled, 64-bit floating point. The value array size is the same as the timestamp array size. For an example of how this data applies to network traffic, refer to Signal Input XY Mode. When you use this instance with a session of Signal Input Single-Point mode, time limit and number to read are ignored, and the timestamp and value arrays always contain only one element per signal. This effectively returns a single pair of timestamp and value for every signal. |
|  | timestamp is the array of LabVIEW timestamps, one for each frame received that contains the signal. Each timestamp represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds. |
|  | value is the array of signal values, one for each frame received that contains the signal. Each signal value is scaled, 64-bit floating point. The value array size is the same as the timestamp array size. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You also can use this instance to read data from a session of Signal Input Single-Point mode, although the [**XNET Read (Signal Single-Point)** VI](xnetreadsignalsinglepointvi.html) is more common for that mode.

The data represents an XY plot of timestamp/value pairs for each signal in the session. You can wire the data directly to a LabVIEW XY Graph for display.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatecancommvi.html language=enus -->
## TOPIC 00256: ni-xnet-api-ref/xnetreadstatecancommvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatecancommvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatecancommvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State CAN Comm).vi

XNET Read (State CAN Comm).vi

#### Purpose

Reads the state of CAN communication using an XNET session.

#### Format

[IMAGE alt='image' src='xnetreadstatecancomm.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | CAN comm returns a LabVIEW cluster containing the communication elements. The elements are: communication state specifies the CAN interface state with respect to error confinement (decimal value in parentheses): Error Active (0) This state reflects normal communication, with few errors detected. The CAN interface remains in this state as long as receive error counter and transmit error counter are both below 128. Error Passive (1) If either the receive error counter or transmit error counter increment above 127, the CAN interface transitions into this state. Although communication proceeds, the CAN device generally is assumed to have problems with receiving frames. When a CAN interface is in error passive state, acknowledgement errors do not increment the transmit error counter. Therefore, if the CAN interface transmits a frame with no other device (ECU) connected, it eventually enters error passive state due to retransmissions, but does not enter bus off state. Bus Off (2) If the transmit error counter increments above 255, the CAN interface transitions into this state. Communication immediately stops under the assumption that the CAN interface must be isolated from other devices. When a CAN interface transitions to the bus off state, communication stops for the interface. All NI-XNET sessions for the interface no longer receive or transmit frame values. To restart the CAN interface and all its sessions, call the XNET Start VI. Init (3) This is the CAN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the CAN interface, it transitions from the Init state to the Error Active state. When the interface stops due to a call to the XNET Stop VI, the CAN interface transitions from either Error Active or Error Passive to the Init state. When the interface stops due to the Bus Off state, it remains in that state until you restart. transceiver error? indicates whether an error condition exists on the physical transceiver. This is typically referred to as the transceiver chip NERR pin. False indicates normal operation (no error), and true indicates an error. sleep? indicates whether the transceiver and communication controller are in their sleep state. False indicates normal operation (awake), and true indicates sleep. last error specifies the status of the last attempt to receive or transmit a frame (decimal value in parentheses): None (0) The last receive or transmit was successful. Stuff (1) More than 5 equal bits have occurred in sequence, which the CAN specification does not allow. Form (2)A fixed format part of the received frame used the wrong format. Ack (3)Another node (ECU) did not acknowledge the frame transmit. If you call the XNET Write VI and do not have a cable connected, or the cable is connected to a node that is not communicating, you see this error repeatedly. The CAN communication state eventually transitions to Error Passive, and the frame transmit retries indefinitely. Bit 1 (4) During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a recessive bit (logical 1), but the monitored bus value was dominant (logical 0). Bit 0 (5) During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a dominant bit (logical 0), but the monitored bus value was recessive (logical 1). CRC (6) The CRC contained within a received frame does not match the CRC calculated for the incoming bits. The receive error counter begins at 0 when communication starts on the CAN interface. The counter increments when an error is detected for a received frame and decrements when a frame is received successfully. The counter increases more for an error than it is decreased for success. This ensures that the counter generally increases when a certain ratio of frames (roughly 1/8) encounter errors. The transmit error counter begins at 0 when communication starts on the CAN interface. The counter increments when an error is detected for a transmitted frame and decrements when a frame transmits successfully. The counter increases more for an error than it is decreased for success. This ensures that the counter generally increases when a certain ratio of frames (roughly 1/8) encounter errors. When communication state transitions to Bus Off, the transmit error counter no longer is valid. fault? indicates that a fault occurred, and its code is available as fault code. fault code returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to CAN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State CAN Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. |
|  | communication state specifies the CAN interface state with respect to error confinement (decimal value in parentheses): Error Active (0) This state reflects normal communication, with few errors detected. The CAN interface remains in this state as long as receive error counter and transmit error counter are both below 128. Error Passive (1) If either the receive error counter or transmit error counter increment above 127, the CAN interface transitions into this state. Although communication proceeds, the CAN device generally is assumed to have problems with receiving frames. When a CAN interface is in error passive state, acknowledgement errors do not increment the transmit error counter. Therefore, if the CAN interface transmits a frame with no other device (ECU) connected, it eventually enters error passive state due to retransmissions, but does not enter bus off state. Bus Off (2) If the transmit error counter increments above 255, the CAN interface transitions into this state. Communication immediately stops under the assumption that the CAN interface must be isolated from other devices. When a CAN interface transitions to the bus off state, communication stops for the interface. All NI-XNET sessions for the interface no longer receive or transmit frame values. To restart the CAN interface and all its sessions, call the XNET Start VI. Init (3) This is the CAN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the CAN interface, it transitions from the Init state to the Error Active state. When the interface stops due to a call to the XNET Stop VI, the CAN interface transitions from either Error Active or Error Passive to the Init state. When the interface stops due to the Bus Off state, it remains in that state until you restart. |
| Error Active (0) | This state reflects normal communication, with few errors detected. The CAN interface remains in this state as long as receive error counter and transmit error counter are both below 128. |
| Error Passive (1) | If either the receive error counter or transmit error counter increment above 127, the CAN interface transitions into this state. Although communication proceeds, the CAN device generally is assumed to have problems with receiving frames. When a CAN interface is in error passive state, acknowledgement errors do not increment the transmit error counter. Therefore, if the CAN interface transmits a frame with no other device (ECU) connected, it eventually enters error passive state due to retransmissions, but does not enter bus off state. |
| Bus Off (2) | If the transmit error counter increments above 255, the CAN interface transitions into this state. Communication immediately stops under the assumption that the CAN interface must be isolated from other devices. When a CAN interface transitions to the bus off state, communication stops for the interface. All NI-XNET sessions for the interface no longer receive or transmit frame values. To restart the CAN interface and all its sessions, call the XNET Start VI. |
| Init (3) | This is the CAN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the CAN interface, it transitions from the Init state to the Error Active state. When the interface stops due to a call to the XNET Stop VI, the CAN interface transitions from either Error Active or Error Passive to the Init state. When the interface stops due to the Bus Off state, it remains in that state until you restart. |
|  | transceiver error? indicates whether an error condition exists on the physical transceiver. This is typically referred to as the transceiver chip NERR pin. False indicates normal operation (no error), and true indicates an error. |
|  | sleep? indicates whether the transceiver and communication controller are in their sleep state. False indicates normal operation (awake), and true indicates sleep. |
|  | last error specifies the status of the last attempt to receive or transmit a frame (decimal value in parentheses): None (0) The last receive or transmit was successful. Stuff (1) More than 5 equal bits have occurred in sequence, which the CAN specification does not allow. Form (2)A fixed format part of the received frame used the wrong format. Ack (3)Another node (ECU) did not acknowledge the frame transmit. If you call the XNET Write VI and do not have a cable connected, or the cable is connected to a node that is not communicating, you see this error repeatedly. The CAN communication state eventually transitions to Error Passive, and the frame transmit retries indefinitely. Bit 1 (4) During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a recessive bit (logical 1), but the monitored bus value was dominant (logical 0). Bit 0 (5) During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a dominant bit (logical 0), but the monitored bus value was recessive (logical 1). CRC (6) The CRC contained within a received frame does not match the CRC calculated for the incoming bits. |
| None (0) | The last receive or transmit was successful. |
| Stuff (1) | More than 5 equal bits have occurred in sequence, which the CAN specification does not allow. |
| Form (2) | A fixed format part of the received frame used the wrong format. |
| Ack (3) | Another node (ECU) did not acknowledge the frame transmit. If you call the XNET Write VI and do not have a cable connected, or the cable is connected to a node that is not communicating, you see this error repeatedly. The CAN communication state eventually transitions to Error Passive, and the frame transmit retries indefinitely. |
| Bit 1 (4) | During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a recessive bit (logical 1), but the monitored bus value was dominant (logical 0). |
| Bit 0 (5) | During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a dominant bit (logical 0), but the monitored bus value was recessive (logical 1). |
| CRC (6) | The CRC contained within a received frame does not match the CRC calculated for the incoming bits. |
|  | The receive error counter begins at 0 when communication starts on the CAN interface. The counter increments when an error is detected for a received frame and decrements when a frame is received successfully. The counter increases more for an error than it is decreased for success. This ensures that the counter generally increases when a certain ratio of frames (roughly 1/8) encounter errors. |
|  | The transmit error counter begins at 0 when communication starts on the CAN interface. The counter increments when an error is detected for a transmitted frame and decrements when a frame transmits successfully. The counter increases more for an error than it is decreased for success. This ensures that the counter generally increases when a certain ratio of frames (roughly 1/8) encounter errors. When communication state transitions to Bus Off, the transmit error counter no longer is valid. |
|  | fault? indicates that a fault occurred, and its code is available as fault code. |
|  | fault code returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to CAN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State CAN Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Read (State CAN Comm)** VI with any XNET session mode, as long as the session interface is CAN. Because the state reflects the CAN interface, it can apply to multiple sessions.

Your application can use the **XNET Read (State CAN Comm)** VI to check for problems on the CAN network independently from other aspects of your application. For example, you intentionally may introduce noise into the CAN cables to test how your ECU behaves under these conditions. When you do this, you do not want the **error out** of NI-XNET VIs to return errors, because this may cause your application to stop. Your application can use the **XNET Read (State CAN Comm)** VI to read the CAN network state quickly as data, so that it does not introduce errors into the flow of your LabVIEW VIs.

Alternately, to log bus errors, you can set the [Interface:Bus Error Frames to Input Stream?](propertysessioninterfacebuserrorframestoinputstream.html)

property to cause CAN bus errors to be logged as a special frame (refer to Special Frames for

more information) into a Frame Stream Input queue.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstateflexraycommvi.html language=enus -->
## TOPIC 00257: ni-xnet-api-ref/xnetreadstateflexraycommvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstateflexraycommvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstateflexraycommvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State FlexRay Comm).vi

XNET Read (State FlexRay Comm).vi

#### Purpose

Reads the state of FlexRay communication using an XNET session.

#### Format

[IMAGE alt='image' src='xnetreadstateflexraycomm.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | FlexRay comm returns a LabVIEW cluster containing the communication elements. The elements are: POC state specifies the FlexRay interface state (decimal value in parentheses): Default Config (0) This is the FlexRay interface initial state on power-up. The interface is essentially off, in that it is not configured and is not attempting to communicate with other nodes (ECUs). Ready (1) When the interface starts, it first enters Config state to validate the FlexRay cluster and interface properties. Assuming the properties are valid, the interface transitions to this Ready state. In the Ready state, the FlexRay interface attempts to integrate (synchronize) with other nodes in the network cluster. This integration process can take several FlexRay cycles, up to 200 ms. If the integration succeeds, the interface transitions to Normal Active. You can use the XNET Read (State Time Start) VI to read the time when the FlexRay interface entered Ready. If integration succeeds, you can use the XNET Read (State Time Comm) VI to read the time when the FlexRay entered Normal Active. Normal Active (2) This is the normal operation state. The NI-XNET interface is adequately synchronized to the cluster to allow continued frame transmission without disrupting the transmissions of other nodes (ECUs). If synchronization problems occur, the interface can transition from this state to Normal Passive. Normal Passive (3) Frame reception is allowed, but frame transmission is disabled due to degraded synchronization with the cluster remainder. If synchronization improves, the interface can transition to Normal Active. If synchronization continues to degrade, the interface transitions to Halt. Halt (4) Communication halted due to synchronization problems. When the FlexRay interface is in Halt state, all NI-XNET sessions for the interface stop, and no frame values are received or transmitted. To restart the FlexRay interface, you must restart the NI-XNET sessions. If you clear (close) all NI-XNET sessions for the interface, it transitions from Halt to Default Config state. Config (15) This state is transitional when configuration is valid. If you detect this state after starting the interface, it typically indicates a problem with the configuration. Check the fault? output for a fault. If no fault is returned, check your FlexRay cluster and interface properties. You can check the validity of these properties using the NI-XNET Database Editor, which displays invalid configuration properties. In the FlexRay specification, this value is referred to as the Protocol Operation Control (POC) state. For more information about the FlexRay POC state, refer to Summary of the FlexRay Standard. clock correction failed returns the number of consecutive even/odd cycle pairs that have occurred without successful clock synchronization. If this count reaches the value in the XNET Cluster FlexRay:Max Without Clock Correction Passive property, the FlexRay interface POC state transitions from Normal Active to Normal Passive state. If this count reaches the value in the XNET Cluster FlexRay:Max Without Clock Correction Fatal property, the FlexRay interface POC state transitions from Normal Passive to Halt state. In the FlexRay specification, this value is referred to as vClockCorrectionFailed. passive to active count returns the number of consecutive even/odd cycle pairs that have occurred with successful clock synchronization. This count increments while the FlexRay interface is in POC state Error Passive. If the count reaches the value in the XNET Session Interface:FlexRay:Allow Passive to Active property, the interface POC state transitions to Normal Active. In the FlexRay specification, this value is referred to as vAllowPassiveToActive. fault? indicates that a fault occurred, and its code is available is fault code. fault code returns a numeric code you can use to obtain a fault description. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to FlexRay communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State FlexRay Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description fault, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. channel A sleep? indicates whether channel A currently is asleep. channel B sleep? indicates whether channel B currently is asleep. |
|  | POC state specifies the FlexRay interface state (decimal value in parentheses): Default Config (0) This is the FlexRay interface initial state on power-up. The interface is essentially off, in that it is not configured and is not attempting to communicate with other nodes (ECUs). Ready (1) When the interface starts, it first enters Config state to validate the FlexRay cluster and interface properties. Assuming the properties are valid, the interface transitions to this Ready state. In the Ready state, the FlexRay interface attempts to integrate (synchronize) with other nodes in the network cluster. This integration process can take several FlexRay cycles, up to 200 ms. If the integration succeeds, the interface transitions to Normal Active. You can use the XNET Read (State Time Start) VI to read the time when the FlexRay interface entered Ready. If integration succeeds, you can use the XNET Read (State Time Comm) VI to read the time when the FlexRay entered Normal Active. Normal Active (2) This is the normal operation state. The NI-XNET interface is adequately synchronized to the cluster to allow continued frame transmission without disrupting the transmissions of other nodes (ECUs). If synchronization problems occur, the interface can transition from this state to Normal Passive. Normal Passive (3) Frame reception is allowed, but frame transmission is disabled due to degraded synchronization with the cluster remainder. If synchronization improves, the interface can transition to Normal Active. If synchronization continues to degrade, the interface transitions to Halt. Halt (4) Communication halted due to synchronization problems. When the FlexRay interface is in Halt state, all NI-XNET sessions for the interface stop, and no frame values are received or transmitted. To restart the FlexRay interface, you must restart the NI-XNET sessions. If you clear (close) all NI-XNET sessions for the interface, it transitions from Halt to Default Config state. Config (15) This state is transitional when configuration is valid. If you detect this state after starting the interface, it typically indicates a problem with the configuration. Check the fault? output for a fault. If no fault is returned, check your FlexRay cluster and interface properties. You can check the validity of these properties using the NI-XNET Database Editor, which displays invalid configuration properties. In the FlexRay specification, this value is referred to as the Protocol Operation Control (POC) state. For more information about the FlexRay POC state, refer to Summary of the FlexRay Standard. |
| Default Config (0) | This is the FlexRay interface initial state on power-up. The interface is essentially off, in that it is not configured and is not attempting to communicate with other nodes (ECUs). |
| Ready (1) | When the interface starts, it first enters Config state to validate the FlexRay cluster and interface properties. Assuming the properties are valid, the interface transitions to this Ready state. In the Ready state, the FlexRay interface attempts to integrate (synchronize) with other nodes in the network cluster. This integration process can take several FlexRay cycles, up to 200 ms. If the integration succeeds, the interface transitions to Normal Active. You can use the XNET Read (State Time Start) VI to read the time when the FlexRay interface entered Ready. If integration succeeds, you can use the XNET Read (State Time Comm) VI to read the time when the FlexRay entered Normal Active. |
| Normal Active (2) | This is the normal operation state. The NI-XNET interface is adequately synchronized to the cluster to allow continued frame transmission without disrupting the transmissions of other nodes (ECUs). If synchronization problems occur, the interface can transition from this state to Normal Passive. |
| Normal Passive (3) | Frame reception is allowed, but frame transmission is disabled due to degraded synchronization with the cluster remainder. If synchronization improves, the interface can transition to Normal Active. If synchronization continues to degrade, the interface transitions to Halt. |
| Halt (4) | Communication halted due to synchronization problems. When the FlexRay interface is in Halt state, all NI-XNET sessions for the interface stop, and no frame values are received or transmitted. To restart the FlexRay interface, you must restart the NI-XNET sessions. If you clear (close) all NI-XNET sessions for the interface, it transitions from Halt to Default Config state. |
| Config (15) | This state is transitional when configuration is valid. If you detect this state after starting the interface, it typically indicates a problem with the configuration. Check the fault? output for a fault. If no fault is returned, check your FlexRay cluster and interface properties. You can check the validity of these properties using the NI-XNET Database Editor, which displays invalid configuration properties. |
|  | clock correction failed returns the number of consecutive even/odd cycle pairs that have occurred without successful clock synchronization. If this count reaches the value in the XNET Cluster FlexRay:Max Without Clock Correction Passive property, the FlexRay interface POC state transitions from Normal Active to Normal Passive state. If this count reaches the value in the XNET Cluster FlexRay:Max Without Clock Correction Fatal property, the FlexRay interface POC state transitions from Normal Passive to Halt state. In the FlexRay specification, this value is referred to as vClockCorrectionFailed. |
|  | passive to active count returns the number of consecutive even/odd cycle pairs that have occurred with successful clock synchronization. This count increments while the FlexRay interface is in POC state Error Passive. If the count reaches the value in the XNET Session Interface:FlexRay:Allow Passive to Active property, the interface POC state transitions to Normal Active. In the FlexRay specification, this value is referred to as vAllowPassiveToActive. |
|  | fault? indicates that a fault occurred, and its code is available is fault code. |
|  | fault code returns a numeric code you can use to obtain a fault description. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to FlexRay communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State FlexRay Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description fault, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. |
|  | channel A sleep? indicates whether channel A currently is asleep. |
|  | channel B sleep? indicates whether channel B currently is asleep. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Read (State FlexRay Comm)** VI with any XNET session mode, as long as the session interface is FlexRay. Because the state reflects the FlexRay interface, it can apply to multiple sessions.

Your application can use the **XNET Read (State FlexRay Comm)** VI to check for problems on the FlexRay network independently from the other aspects of your application. For example, you intentionally may introduce noise into the FlexRay cables to test how your ECU behaves under these conditions. When you do this, you do not want the **error out** of NI-XNET VIs to return errors, because this may cause your application to stop. Your application can use the **XNET Read (State FlexRay Comm)** VI to read the FlexRay network state quickly as data, so that it does not introduce errors into the flow of your LabVIEW VIs.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatelincommvi.html language=enus -->
## TOPIC 00258: ni-xnet-api-ref/xnetreadstatelincommvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatelincommvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatelincommvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State LIN Comm).vi

XNET Read (State LIN Comm).vi

#### Purpose

Reads the state of LIN communication using an XNET session.

#### Format

[IMAGE alt='image' src='xnetreadstatelincomm.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session must use a LIN interface. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | LIN comm returns a LabVIEW cluster containing the communication elements. The elements are: communication state specifies the LIN interface state (decimal value in parentheses): Idle (0): This is the LIN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the LIN interface, it transitions from the Idle state to the Active state. When the interface stops due to a call to XNET Stop, the LIN interface transitions from either Active or Inactive to the Idle state. Active (1): This state reflects normal communication. The LIN interface remains in this state as long as bus activity is detected (frame headers received or transmitted). Inactive (2): This state indicates that no bus activity has been detected in the past four seconds. Regardless of whether the interface acts as a master or slave, it transitions to this state after four seconds of bus inactivity. As soon as bus activity is detected (break or frame header), the interface transitions to the Active state. The LIN interface does not go to sleep automatically when it transitions to Inactive. To place the interface into sleep mode, set the XNET Session Interface:LIN:Sleep property when you detect the Inactive state. sleep? indicates whether the transceiver and communication controller are in their sleep state. False indicates normal operation (awake), and true indicates sleep. This Boolean value changes from false to true only when you set the XNET Session Interface:LIN:Sleep property to Remote Sleep or Local Sleep. This Boolean value changes from true to false when one of the following occurs: You set the XNET Session Interface:LIN:Sleep property to Remote Wake or Local Wake. The interface receives a remote wakeup pattern (break). In addition to this XNET Read VI, you can wait for a remote wakeup event using the XNET Wait (LIN Remote Wakeup) VI. transceiver ready? indicates whether the LIN transceiver is powered from the bus. True indicates the bus power exists, so it is safe to start communication on the LIN interface. If this value is false, you cannot start communication successfully. Wire power to the LIN transceiver and run your application again. last error specifies the status of the last attempt to receive or transmit a frame. It is an enumeration (ring data type). For a table of all values for last error, refer to the Description section. last received returns the value received from the network when last error occurred. last expected returns the value that the LIN interface expected to see (instead of last received). last identifier returns the frame identifier in which the last error occurred. fault? indicates that a fault occurred, and its code is available as fault code. fault code returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to LIN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State LIN Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. For more information, refer to Fault Handling. schedule index indicates the LIN schedule that the interface is currently running. This index refers to a LIN schedule that you requested using the XNET Write (State LIN Schedule Change) VI. It indexes the array of schedules that are represented in the XNET Session Interface:LIN:Schedules property. This index applies only when the LIN interface is running as a master. If the LIN interface is running as a slave only, this element should be ignored. |
|  | communication state specifies the LIN interface state (decimal value in parentheses): Idle (0): This is the LIN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the LIN interface, it transitions from the Idle state to the Active state. When the interface stops due to a call to XNET Stop, the LIN interface transitions from either Active or Inactive to the Idle state. Active (1): This state reflects normal communication. The LIN interface remains in this state as long as bus activity is detected (frame headers received or transmitted). Inactive (2): This state indicates that no bus activity has been detected in the past four seconds. Regardless of whether the interface acts as a master or slave, it transitions to this state after four seconds of bus inactivity. As soon as bus activity is detected (break or frame header), the interface transitions to the Active state. The LIN interface does not go to sleep automatically when it transitions to Inactive. To place the interface into sleep mode, set the XNET Session Interface:LIN:Sleep property when you detect the Inactive state. |
| Idle (0): | This is the LIN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the LIN interface, it transitions from the Idle state to the Active state. When the interface stops due to a call to XNET Stop, the LIN interface transitions from either Active or Inactive to the Idle state. |
| Active (1): | This state reflects normal communication. The LIN interface remains in this state as long as bus activity is detected (frame headers received or transmitted). |
| Inactive (2): | This state indicates that no bus activity has been detected in the past four seconds. Regardless of whether the interface acts as a master or slave, it transitions to this state after four seconds of bus inactivity. As soon as bus activity is detected (break or frame header), the interface transitions to the Active state. The LIN interface does not go to sleep automatically when it transitions to Inactive. To place the interface into sleep mode, set the XNET Session Interface:LIN:Sleep property when you detect the Inactive state. |
|  | sleep? indicates whether the transceiver and communication controller are in their sleep state. False indicates normal operation (awake), and true indicates sleep. This Boolean value changes from false to true only when you set the XNET Session Interface:LIN:Sleep property to Remote Sleep or Local Sleep. This Boolean value changes from true to false when one of the following occurs: You set the XNET Session Interface:LIN:Sleep property to Remote Wake or Local Wake. The interface receives a remote wakeup pattern (break). In addition to this XNET Read VI, you can wait for a remote wakeup event using the XNET Wait (LIN Remote Wakeup) VI. |
|  | transceiver ready? indicates whether the LIN transceiver is powered from the bus. True indicates the bus power exists, so it is safe to start communication on the LIN interface. If this value is false, you cannot start communication successfully. Wire power to the LIN transceiver and run your application again. |
|  | last error specifies the status of the last attempt to receive or transmit a frame. It is an enumeration (ring data type). For a table of all values for last error, refer to the Description section. |
|  | last received returns the value received from the network when last error occurred. |
|  | last expected returns the value that the LIN interface expected to see (instead of last received). |
|  | last identifier returns the frame identifier in which the last error occurred. |
|  | fault? indicates that a fault occurred, and its code is available as fault code. |
|  | fault code returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to LIN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State LIN Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. For more information, refer to Fault Handling. |
|  | schedule index indicates the LIN schedule that the interface is currently running. This index refers to a LIN schedule that you requested using the XNET Write (State LIN Schedule Change) VI. It indexes the array of schedules that are represented in the XNET Session Interface:LIN:Schedules property. This index applies only when the LIN interface is running as a master. If the LIN interface is running as a slave only, this element should be ignored. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Read (State LIN Comm)** VI with any XNET session mode, as long as the session interface is LIN. Because the state reflects the LIN interface, it can apply to multiple sessions.

Your application can use the **XNET Read (State LIN Comm)** VI to check for problems on the LIN network independently from other aspects of your application. For example, you intentionally may introduce noise into the LIN cables to test how your ECU behaves under these conditions. When you do this, you do not want the **error out** of NI-XNET VIs to return errors, because this may cause your application to stop. Your application can use the **XNET Read (State LIN Comm)** VI to read the LIN network state quickly as data, so that it does not introduce errors into the flow of your LabVIEW VIs.

The following table lists each value for **last error**, along with a description, and applicable use of **last received**, **last expected**, and **last identifier**. In the **last error** column, the decimal value is shown in parentheses after the string name.

| Last Error | Description | Last Received | Last Expected | Last Identifier |
| --- | --- | --- | --- | --- |
| None (0) | No bus error has occurred since the previous communication state read. | 0 (N/A) | 0 (N/A) | 0 (N/A) |
| Unknown ID (1) | Received a frame identifier that is not valid (0–63). | 0 (N/A) | 0 (N/A) | 0 (N/A) |
| Form (2) | The form of a received frame is incorrect. For example, the database specifies 8 bytes of payload, but you receive only 4 bytes. | 0 (N/A) | 0 (N/A) | Received frame ID |
| Framing (3) | The byte framing is incorrect (for example, a missing stop bit). | 0 (N/A) | 0 (N/A) | Received frame ID |
| Readback (4) | The interface transmitted a byte, but the value read back from the transceiver was different. This often is caused by a cabling problem, such as noise. | Value read back | Value transmitted | Received frame ID |
| Timeout (5) | Receiving the frame took longer than the LIN-specified timeout. | 0 (N/A) | 0 (N/A) | Received frame ID |
| Checksum (6) | The received checksum was different than the expected checksum. | Received checksum | Calculated checksum | Received frame ID |

If the bus error is detected at time when no frame ID is received (such as wakeup), **last identifier** uses the special value 64.

Alternately, to log bus errors, you can set the [Interface:Bus Error Frames to Input Stream?](propertysessioninterfacebuserrorframestoinputstream.html)

property to cause LIN bus errors to be logged as a special frame (refer to Special Frames for

more information) into a Frame Stream Input queue.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatesaej1939commvi.html language=enus -->
## TOPIC 00259: ni-xnet-api-ref/xnetreadstatesaej1939commvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatesaej1939commvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatesaej1939commvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State SAE J1939 Comm).vi

XNET Read (State SAE J1939 Comm).vi

#### Purpose

Reads the state of J1939 communication using an XNET session.

#### Format

[IMAGE alt='image' src='xnetreadstatesaej1939comm.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session must use a LIN interface. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | J1939 comm returns a LabVIEW cluster containing the communication elements. The elements are: PGN specifies the J1939 PGN that occurred the last error. You cannot assign a PGN to every error. src address specifies the source address that occurred the last error. You cannot assign a source address to every error. dest addr specifies the destination address that occurred the last error. You cannot assign a destination address to every error or warning. transmit error indicates a transmit-related error occurred. receive error indicates a receive-related error occurred. fault? indicates that a fault occurred, and its code is available as fault code. fault code returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to J1939 communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State SAE J1939 Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. |
|  | PGN specifies the J1939 PGN that occurred the last error. You cannot assign a PGN to every error. |
|  | src address specifies the source address that occurred the last error. You cannot assign a source address to every error. |
|  | dest addr specifies the destination address that occurred the last error. You cannot assign a destination address to every error or warning. |
|  | transmit error indicates a transmit-related error occurred. |
|  | receive error indicates a receive-related error occurred. |
|  | fault? indicates that a fault occurred, and its code is available as fault code. |
|  | fault code returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0. A fault is an error that occurs asynchronously to the NI-XNET VIs your application calls. The fault cause may be related to J1939 communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, the XNET Read (State SAE J1939 Comm) VI provides a detection method distinct from the error out of NI-XNET VIs, yet easy to use alongside the common practice of checking the communication state. To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler VI error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Read (State SAE J1939 Comm)** VI with any XNET session mode, as long as the session interface is CAN. Because the state reflects the CAN interface, it can apply to multiple sessions.

Your application can use the **XNET Read (State SAE J1939 Comm)** VI to check for problems on the J1939 network independently from other aspects of your application. For example, you intentionally may introduce noise into the CAN cables to test how your ECU behaves under these conditions. When you do this, you do not want the error out of NI-XNET VIs to return errors, because this may cause your application to stop. Your application can use the **XNET Read (State SAE J1939 Comm)** VI to read the J1939 network state quickly as data, so it does not introduce errors into the flow of your LabVIEW VIs.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatesessioninfovi.html language=enus -->
## TOPIC 00260: ni-xnet-api-ref/xnetreadstatesessioninfovi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatesessioninfovi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatesessioninfovi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State Session Info).vi

XNET Read (State Session Info).vi

#### Purpose

Returns the current state for the session provided.

#### Format

[IMAGE alt='image' src='xnetreadstatesessioninfovi.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | session info state returns the state of the provided session. Stopped (0) All frames in the session are stopped. Started (1) All frames in the session are started. Mix (2) Some frames in the session are started while other frames are stopped. |
| Stopped (0) | All frames in the session are stopped. |
| Started (1) | All frames in the session are started. |
| Mix (2) | Some frames in the session are started while other frames are stopped. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Read (State Session Info)** VI with any XNET session mode.

The **XNET Read (State Session Info)** VI returns the state of the session's objects. A mixed state may occur when using the [**XNET Start** VI](xnetstartvi.html) or [**XNET Stop** VI](xnetstopvi.html) with the Session Only option. By reading this state, your application can ensure that all frames in the session have started or stopped.

If the session is started with any option other than Session Only, the state is known, so this VI may not be useful.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatetimecurrentvi.html language=enus -->
## TOPIC 00261: ni-xnet-api-ref/xnetreadstatetimecurrentvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatetimecurrentvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatetimecurrentvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State Time Current).vi

XNET Read (State Time Current).vi

#### Purpose

Reads the current interface timestamp using an XNET session.

#### Format

[IMAGE alt='image' src='xnetreadstatetimecurrent.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | local time current returns the current interface timestamp as a LabVIEW absolute time, using the local timescale. For CAN, FlexRay, and LIN, if the interface is not started when the XNET Read (State Time Current) VI is called, local time current returns an invalid time (0). For Ethernet, you can read current time prior to starting the interface. |
|  | network time current Ethernet only. Returns the current time as a LabVIEW absolute time, using the network timescale. The network time current timestamp is captured simultaneously with the local time current timestamp. The network time current output is not applicable for CAN, FlexRay, and LIN and returns an invalid time (0). |
|  | network synced Ethernet only. Contains the value of the Synced property at the time that both timestamps are acquired, to specify whether the network time current timestamp is synchronized to the network (true) or not (false). The network synced output is not applicable for CAN, FlexRay, and LIN and returns a value of false. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the XNET Read (State Time Current) VI with any XNET session mode. Because the time is associated with the interface, it can apply to multiple sessions.

The XNET Read (State Time Current) VI returns time as a LabVIEW absolute timestamp data type. The timestamp represents absolute time that the interface timebase source drives. You use the timebase source to timestamp frames the interface receives. For a CAN interface, you use the timebase source to schedule cyclic frame transmit.

The interface timebase source is not necessarily connected to the LabVIEW CPU clock, so this timestamp can drift relative to the LabVIEW time used for internally sourced timed loops and the LabVIEW Get Date/Time in Seconds VI.

For more information about the interface timebase source, refer to the [XNET Connect Terminals VI](xnetconnectterminalsvi.html).

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatetimestartvi.html language=enus -->
## TOPIC 00262: ni-xnet-api-ref/xnetreadstatetimestartvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatetimestartvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatetimestartvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State Time Start).vi

XNET Read (State Time Start).vi

#### Purpose

Reads the time when the session interface started its integration.

#### Format

[IMAGE alt='image' src='xnetreadstatetimestart.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | local time start returns the interface start time as a LabVIEW absolute time, using the local timescale. If the interface is not started when the XNET Read (State Time Start) VI is called, local time start returns an invalid time (0). |
|  | network time start Ethernet only. Returns the interface start time as a LabVIEW absolute time, using the network timescale. The network time start timestamp is captured simultaneously with the local time start timestamp. The network time start output is not applicable for CAN, FlexRay, and LIN and returns an invalid time (0). This output is optional. |
|  | network synced Ethernet only. Contains the value of the Synced property at the time that both timestamps are acquired, to specify whether the network time current timestamp is synchronized to the network (true) or not (false). The network synced output is not applicable for CAN, FlexRay, and LIN and returns a value of false. This output is optional. |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Read (State Time Start)** VI with any XNET session mode. Because the time is associated with the interface, it can apply to multiple sessions.

The **XNET Read (State Time Start)** VI returns time as a LabVIEW absolute timestamp data type.

Your application typically starts the interface simply by calling an [**XNET Read** VI](xnetreadvi.html) or [XNET Write VI](xnetwritevi.html), because the XNET Session Auto Start? property is true by default. If you set Auto Start? to false, you start the interface using the [XNET Start VI](xnetstartvi.html). If you use the [XNET Connect Terminals VI](xnetconnectterminalsvi.html) to import a start trigger for the interface, all sessions for that interface wait for the trigger to occur before starting the interface.

Once the interface starts, this VI captures and returns the time. Unless you connect a start trigger, this time generally is known, so this VI may not be useful.

After the XNET interface starts, the communication controller begins to integrate with ECUs in the network. After this integration is complete, the time is captured and available using the [XNET Read (State Time Comm) VI](xnetreadstatetimecommvi.html). That time often is useful for FlexRay, because it indicates the time when true communication began.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadstatetimetriggervi.html language=enus -->
## TOPIC 00263: ni-xnet-api-ref/xnetreadstatetimetriggervi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadstatetimetriggervi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadstatetimetriggervi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read (State Time Trigger).vi

XNET Read (State Time Trigger).vi

#### Purpose

Reads the captured timestamp for an imported Time Trigger.

#### Format

[IMAGE alt='image' src='xnetreadtimetrigger.gif']

#### Inputs

|  | session in is the session to read. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | timeout is the time to wait for the rising edge of Time Trigger. The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds. If timeout is positive, the XNET Read (State Time Trigger) VI waits for the rising edge of Time Trigger, then returns the timestamps for that edge. If the edge does not occur prior to the timeout, an error is returned. If timeout is negative, the XNET Read (State Time Trigger) VI waits indefinitely for the rising edge of Time Trigger. If timeout is zero, the XNET Read (State Time Trigger) VI does not wait and immediately returns the timestamps, which are zero (invalid) if the rising edge of Time Trigger has not occurred. This input is optional. The default value is 10 seconds. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | local time trigger returns the timestamp of first rising edge of the imported Time Trigger since it was armed. The timestamp is a LabVIEW absolute time, using the local timescale. If Time Trigger has not encountered a rising edge since it was armed, local time trigger returns zero (an invalid timestamp). |
|  | network time trigger returns the timestamp of first rising edge of the imported Time Trigger since it was armed. The timestamp is a LabVIEW absolute time, using the network timescale. If Time Trigger has not encountered a rising edge since it was armed, network time trigger returns zero (an invalid timestamp). |
|  | network synced contains the value of the Synced? property at the time that both timestamps are acquired, to specify whether the network time trigger timestamp is synchronized to the network (true) or not (false). |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

When you use the [XNET Connect Terminals VI](xnetconnectterminalsvi.html) with destination terminal of TimeTrigger (i.e., imported), the Time Trigger captures absolute timestamps on the rising edge, and you read those timestamps using this XNET Read (State Time Trigger) VI.

The imported Time Trigger is armed when you invoke the XNET Connect Terminals VI, and Time Trigger is armed again on each subsequent invocation of the XNET Read (State Time Trigger) VI. After the Time Trigger is armed, the first rising edge after arming is captured for the subsequent XNET Read (State Time Trigger) VI.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetreadvi.html language=enus -->
## TOPIC 00264: ni-xnet-api-ref/xnetreadvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetreadvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetreadvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Read.vi

XNET Read.vi

#### Purpose

Reads data from the network using an XNET session.

#### Description

The instances of this polymorphic VI specify the type of data returned.

The **XNET Read** and [**XNET Write**](xnetwritevi.html) VIs are optimized for real-time performance. The **XNET Read** VI executes quickly and avoids access to shared resources that can induce jitter on other VI priorities.

There are three categories of **XNET Read** instance VIs:

- Signal : Use when the session mode is Signal Input. The XNET Read VI instance must match the mode exactly (for example, the Signal Waveform instance when mode is Signal Input Waveform).
- Frame : Use when the session mode is Frame Input. The XNET Read VI instance specifies the desired data type for frames and is not related to the mode. For an easy-to-use data type, use the CAN, FlexRay, or LIN instance.
- State : Use to read state, status, and time information for the session interface. You can use these instances in addition to Signal or Frame instances, and they are not related to the mode. The data these instances return is optimized for performance. Although property nodes may return similar runtime data, those properties are not necessarily optimized for real-time loops.

The **XNET Read** instance VIs are:

- **Signal Single-Point** : The session mode is Signal Single-Point.
- **Signal Waveform** : The session mode is Signal Waveform.
- **Signal XY** : The session mode is Signal Input XY.
- **Frame CAN** : The session uses a CAN interface, and the mode is Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.
- **Frame Ethernet** : Reads data from a session as an array of Ethernet frames. The session must use an Ethernet interface and a mode of Frame Input Stream.
- **Frame FlexRay** : The session uses a FlexRay interface, and the mode is Frame Input Stream, Frame Input Queued, Frame Input Single-Point, PDU Input Queued (similar to Frame Input Queued), and PDU Input Single-Point (similar to Frame Input Single-Point).
- **Frame LIN** : The session uses a LIN interface, and the mode is Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.
- **Frame Raw** : A data type for frame input that is protocol independent and more efficient than the protocol-specific instances.
- **State CAN Comm** : Returns the CAN interface's communication state.
- **State FlexRay Comm** : Returns the FlexRay interface's communication state.
- **State FlexRay Cycle Macrotick** : Returns the current global time of the session FlexRay interface, represented as cycle and macrotick.
- **State FlexRay Statistics** : Returns the communication statistics for the session FlexRay interface.
- **State LIN Comm** : Returns the LIN interface's communication state.
- **State SAE J1939 Comm** : Returns the state of J1939 communication.
- **State Time Comm** : Returns the LabVIEW timestamp at which communication began for the session interface.
- **State Time Current** : Returns the session interface current time as a LabVIEW timestamp.
- **State Time Start** : Returns the LabVIEW timestamp at which communication started for the session interface. This time always precedes the Communication time.
- **State Time Trigger** : Reads the captured timestamp for an imported Time Trigger.
- **State Session Info** : Returns the current state for the session provided.

|  | Note: If an overflow error occurs while multiple input stream sessions are open on the same interface, all input stream sessions must be either stopped or flushed before new data can be received. For more information, refer to XNET Flush.vi. |
| --- | --- |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsessionproperties_c.html language=enus -->
## TOPIC 00265: ni-xnet-api-ref/xnetsessionproperties_c.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsessionproperties_c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsessionproperties_c.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Session Properties

XNET Session Properties

This section includes the XNET Session properties.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsessionpropertynode.html language=enus -->
## TOPIC 00266: ni-xnet-api-ref/xnetsessionpropertynode.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsessionpropertynode.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsessionpropertynode.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Session Node

XNET Session Node

#### Format

[IMAGE alt='image' src='xnetsessionpropertynode.gif']

#### Description

Property node used to read/write properties for an XNET Session I/O name.

Pull down this node to add properties. Right-click to change direction between read and write. Right-click each property name to create a constant, control, or indicator.

For help on a specific property, open the LabVIEW context help window (<Ctrl-H>) and move your cursor over the property name.

For more information about LabVIEW property nodes, open the main LabVIEW help (select **LabVIEW Help...** from the **Help** menu) and look for the *Property Nodes* topic in the index.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsignalproperties_c.html language=enus -->
## TOPIC 00267: ni-xnet-api-ref/xnetsignalproperties_c.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsignalproperties_c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsignalproperties_c.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Signal Properties

XNET Signal Properties

This section includes the XNET Signal properties.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetstopvi.html language=enus -->
## TOPIC 00268: ni-xnet-api-ref/xnetstopvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetstopvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetstopvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Stop.vi

XNET Stop.vi

#### Purpose

Stops communication for the specified XNET session.

#### Format

[IMAGE alt='image' src='xnetstop.gif']

#### Inputs

|  | session in is the session to stop. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | scope describes the impact of this operation on the underlying state models for the session and its interface. Normal (0) The session is stopped. If this is the last session stopped on the interface, the interface is also stopped. If any other sessions are running on the interface, this call is treated just like the Session Only scope, to avoid disruption of communication on the other sessions. For Ethernet interfaces, this is the only value of scope that is supported. This is the default value for scope if it is unwired. Session Only (1) The session is placed in the Stopped state (refer to State Models). If the interface was in the Started or Running state before this VI is called, the interface remains in that state and communication continues, but data from this session does not transfer. This scope generally is not necessary, as the Normal scope only stops the interface if there are no other running sessions. This operation sends the command to stop the session, but does not wait for the session to be stopped. It is ideal for a real-time application where performance is critical. Interface Only (2) The underlying interface is placed in the Stopped state (refer to State Models). This prevents all communication on the bus, for all sessions. This allows you to modify certain properties that require the interface to be stopped (for example, CAN baud rate). All sessions remain in the Started state. To have multiple sessions stop at exactly the same time, first stop the interface with the Interface Only scope and then stop each session with either the Normal or Session Only scope. Session Only Blocking (3) The session is placed in the Stopped state (refer to State Models). If the interface was in the Started or Running state before this VI is called, the interface remains in that state and communication continues, but data from this session does not transfer. This scope generally is not necessary, as the Normal scope stops the interface only if there are no other running sessions. This operation waits for the session to stop before completing. |
| Normal (0) | The session is stopped. If this is the last session stopped on the interface, the interface is also stopped. If any other sessions are running on the interface, this call is treated just like the Session Only scope, to avoid disruption of communication on the other sessions. For Ethernet interfaces, this is the only value of scope that is supported. This is the default value for scope if it is unwired. |
| Session Only (1) | The session is placed in the Stopped state (refer to State Models). If the interface was in the Started or Running state before this VI is called, the interface remains in that state and communication continues, but data from this session does not transfer. This scope generally is not necessary, as the Normal scope only stops the interface if there are no other running sessions. This operation sends the command to stop the session, but does not wait for the session to be stopped. It is ideal for a real-time application where performance is critical. |
| Interface Only (2) | The underlying interface is placed in the Stopped state (refer to State Models). This prevents all communication on the bus, for all sessions. This allows you to modify certain properties that require the interface to be stopped (for example, CAN baud rate). All sessions remain in the Started state. To have multiple sessions stop at exactly the same time, first stop the interface with the Interface Only scope and then stop each session with either the Normal or Session Only scope. |
| Session Only Blocking (3) | The session is placed in the Stopped state (refer to State Models). If the interface was in the Started or Running state before this VI is called, the interface remains in that state and communication continues, but data from this session does not transfer. This scope generally is not necessary, as the Normal scope stops the interface only if there are no other running sessions. This operation waits for the session to stop before completing. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

Because the session is stopped automatically when cleared (closed), this VI is optional.

For each physical interface, the NI-XNET hardware is divided into two logical units:

- Sessions : You can create one or more sessions, each of which contains frames or signals to be transmitted (or received) on the bus.
- Interface : The interface physically connects to the bus and transmits (or receives) data for the sessions.

You can stop each logical unit separately. When a session is stopped, all contained frames or signals are placed in a state where they are no longer ready to communicate. When the interface is stopped, it no longer takes data from sessions to communicate with other nodes on the bus. For a specification of the state models for the session and interface, refer to State Models.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetstringtoionamevi.html language=enus -->
## TOPIC 00269: ni-xnet-api-ref/xnetstringtoionamevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetstringtoionamevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetstringtoionamevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET String to IO Name.vi

XNET String to IO Name.vi

#### Purpose

Converts a LabVIEW string to an XNET I/O Name.

#### Description

This VI is not required for LabVIEW 2009 or newer. It is provided only for backward compatibility of VIs written in LabVIEW versions prior to 2009. Currently supported versions of LabVIEW can now cast LabVIEW strings to XNET IO names automatically.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsubframeproperties_c.html language=enus -->
## TOPIC 00270: ni-xnet-api-ref/xnetsubframeproperties_c.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsubframeproperties_c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsubframeproperties_c.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Subframe Properties

XNET Subframe Properties

This section includes the XNET Subframe properties.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsubframepropertynode.html language=enus -->
## TOPIC 00271: ni-xnet-api-ref/xnetsubframepropertynode.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsubframepropertynode.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsubframepropertynode.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Subframe Property Node

XNET Subframe Property Node

#### Format

[IMAGE alt='image' src='xnetsubframepropertynode.gif']

#### Description

Property node used to read/write properties for an XNET Subframe I/O name.

Pull down this node to add properties. Right-click to change direction between read and write. Right-click each property name to create a constant, control, or indicator.

For help on a specific property, open the LabVIEW context help window (<Ctrl-H>) and move your cursor over the property name.

For more information about LabVIEW property nodes, open the main LabVIEW help (select **Search the LabVIEW Help...** from the **Help** menu) and look for the *Property Nodes* topic in the index.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsystemclosevi.html language=enus -->
## TOPIC 00272: ni-xnet-api-ref/xnetsystemclosevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsystemclosevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsystemclosevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET System Close.vi

XNET System Close.vi

| Note: This VI is provided for compatibility with previous versions of NI-XNET. For new VI development, it is recommended that you use System Configuration API, as it provides more features. |
| --- |

#### Purpose

Closes the XNET system to refresh XNET hardware information.

#### Format

[IMAGE alt='image' src='xnetsystemclose.gif']

#### Inputs

|  | error in is the error cluster input (refer to Error Handling). |
| --- | --- |

#### Outputs

|  | error out is the error cluster output (refer to Error Handling). |
| --- | --- |

#### Description

When your VI first uses the [XNET System property node](xnetsystempropertynode.html), NI-XNET obtains information about all available devices and interfaces in the system. While using property nodes for the devices and interfaces, the hardware information maintains consistency. For example, if you physically add a new device (for example, a plug-in a CompactDAQ chassis), the new device does not appear in the system properties.

Use the **XNET System Close** VI to close the system and associated devices and interfaces. The next time your VI uses the XNET System property node, the hardware information is refreshed.

If you previously used the [**XNET Blink** VI](xnetblinkvi.html) to blink a device's LEDs for identification, the **XNET System Close** VI disables blinking when it closes the associated device.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsystemproperties_c.html language=enus -->
## TOPIC 00273: ni-xnet-api-ref/xnetsystemproperties_c.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsystemproperties_c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsystemproperties_c.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET System Properties

XNET System Properties

#### Description

The XNET System properties provide information about all NI-XNET hardware in your system, including all devices and interfaces.

You retrieve a system handle with [nxSystemOpen](nxsystemopen.html) and release it with [nxSystemClose](nxsystemclose.html). Pass the system handle to all system property calls.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetsystempropertynode.html language=enus -->
## TOPIC 00274: ni-xnet-api-ref/xnetsystempropertynode.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetsystempropertynode.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetsystempropertynode.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET System Property Node

XNET System Property Node

| Note: This node is provided for compatibility with previous versions of NI-XNET. For new VI development, it is recommended that you use System Configuration API, as it provides more features. |
| --- |

#### Format

[IMAGE alt='image' src='xnetsystempropertynode.gif']

#### Description

The XNET System property node provides information about all NI-XNET hardware in your system, including all devices and interfaces.

Pull down this node to add properties. Right-click to change direction between read and write. Right-click each property name to create a constant, control, or indicator.

For help on a specific property, open the LabVIEW context help window (<Ctrl-H>) and move your cursor over the property name.

For more information about LabVIEW property nodes, open the main LabVIEW help (select **Search the LabVIEW Help...** from the **Help** menu) and look for the *Property Nodes* topic in the index.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnettcpsocketclosevi.html language=enus -->
## TOPIC 00275: ni-xnet-api-ref/xnettcpsocketclosevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnettcpsocketclosevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnettcpsocketclosevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET TCP Socket Close.vi

XNET TCP Socket Close.vi

#### Purpose

Closes a TCP network connection.

#### Format

[IMAGE alt='image' src='xnettcpsocketclose.gif']

#### Inputs

|  | socket is a network connection refnum that uniquely identifies the connection. |
| --- | --- |
|  | abort (F) specifies whether to abort the TCP session immediately or stay open until any remaining data is sent. When abort is false (default), after returning from XNET TCP Socket Close.vi, the TCP connection stays open in the background while any remaining data is sent, and then closes after handshake. When abort is true, the TCP connection is immediately aborted (reset) and closed (regardless of unsent data), and XNET TCP Socket Close.vi returns. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | error out is the error cluster output (refer to Error Handling). |
| --- | --- |

#### Description

When [XNET IP Stack Clear.vi](xnetipstackclearvi.html) is called to close the stack, all TCP connections must be aborted in order to free stack resources. Therefore, setting **abort** to false for XNET TCP Socket Close.vi is applicable only when you intend to leave the stack running.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnettcpsocketcreatelistenervi.html language=enus -->
## TOPIC 00276: ni-xnet-api-ref/xnettcpsocketcreatelistenervi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnettcpsocketcreatelistenervi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnettcpsocketcreatelistenervi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET TCP Socket Create Listener.vi

XNET TCP Socket Create Listener.vi

#### Purpose

Use this VI with XNET TCP Socket Wait on Listener to create and listen for connections on the server.

#### Format

[IMAGE alt='image' src='xnettcpsocketcreatelistener.gif']

#### Inputs

|  | stack is the XNET IP Stack in which the new socket is opened. |
| --- | --- |
|  | local port is the port number where you want to listen for a connection. By default (0), this VI dynamically chooses an available TCP port to listen for connections on. The following table lists valid port numbers as defined by the Internet Assigned Numbers Authority (IANA). TypeRange System/Well-Known Ports1 through 1023 User/Registered Ports1024 through 49151 Dynamic/Private Ports49152 through 65535 |
| Type | Range |
| System/Well-Known Ports | 1 through 1023 |
| User/Registered Ports | 1024 through 49151 |
| Dynamic/Private Ports | 49152 through 65535 |
|  | timeout ms (25000) specifies the time, in milliseconds, that the VI waits to complete before reporting a timeout error. The default value is 25,000 ms. Wire a 1 to this input to wait indefinitely. |
|  | error in is the error cluster input (refer to Error Handling). |
|  | local interface identifies a specific virtual interface in the IP Stack on which to bind the socket. The virtual interface is identified using one of the following (as returned from XNET IP Stack Get Info.vi): virtual interface name (recommended) string that represents the decimal value of ifIndex IP address (see Supported Features) This input is optional. If local interface is empty (default), the socket is bound to any virtual interface in the IP stack. |

#### Outputs

|  | listener socket is a network connection refnum that uniquely identifies the listener. |
| --- | --- |
|  | actual local port is the port number the VI used. If you wire 0 to the local port input, this VI dynamically chooses an available TCP port that the XNET IP stack determines is valid for use. If you wire a value other than 0 to the local port input, actual local port returns the input port number. |
|  | error out is the error cluster output (refer to Error Handling). |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnettcpsocketopenvi.html language=enus -->
## TOPIC 00277: ni-xnet-api-ref/xnettcpsocketopenvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnettcpsocketopenvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnettcpsocketopenvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET TCP Socket Open.vi

XNET TCP Socket Open.vi

#### Purpose

Opens a TCP network connection using a specified address and port. To close the connection once data transmission is complete, use [XNET TCP Socket Close](xnettcpsocketclosevi.html).

#### Format

[IMAGE alt='image' src='xnettcpsocketopen.gif']

#### Inputs

|  | stack is the XNET IP Stack in which the new socket is opened. |
| --- | --- |
|  | remote address is the IP address with which you want to establish a connection. |
|  | remote port is the port on the server with which you want to establish a connection. If you wire a value of 0 to this input, this VI returns an error. |
|  | timeout ms (60000) specifies the time, in milliseconds, that the VI waits to complete before reporting a timeout error. The default value is 60,000 ms (1 minute). Wire a 1 to this input to wait indefinitely. |
|  | error in is the error cluster input (refer to Error Handling). |
|  | local port is the local connection port. Some servers only allow connections to clients that use port numbers within a specific range that is dependent on the server. If the value is 0, the XNET IP stack selects an unused port. The default is 0. |
|  | local interface identifies a specific virtual interface in the IP Stack on which to bind the socket. The virtual interface is identified using one of the following (as returned from XNET IP Stack Get Info.vi): virtual interface name (recommended) string that represents the decimal value of ifIndex IP address (see Supported Features) This input is optional. If local interface is empty (default), the socket is bound to any virtual interface in the IP stack. |

#### Outputs

|  | socket is a network connection refnum that uniquely identifies the connection. Use this value to refer to this connection in subsequent VI calls. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetudpsocketclosevi.html language=enus -->
## TOPIC 00278: ni-xnet-api-ref/xnetudpsocketclosevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetudpsocketclosevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetudpsocketclosevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET UDP Socket Close.vi

XNET UDP Socket Close.vi

#### Purpose

Closes a UDP socket and frees system resources.

#### Format

[IMAGE alt='image' src='xnetudpsocketclose.gif']

#### Inputs

|  | socket is a network connection refnum that uniquely identifies the connection. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | error out is the error cluster output (refer to Error Handling). |
| --- | --- |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetudpsocketinvokemethodaddgroupmember.html language=enus -->
## TOPIC 00279: ni-xnet-api-ref/xnetudpsocketinvokemethodaddgroupmember.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetudpsocketinvokemethodaddgroupmember.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetudpsocketinvokemethodaddgroupmember.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

Add Group Member

Add Group Member

#### Purpose

Add a group member to a multicast group.

#### Inputs

|  | multicast address specifies the multicast address. See Supported Features. |
| --- | --- |
|  | local interface identifies a specific virtual interface in the IP Stack on which to add multicast group membership. The virtual interface is identified using one of the following (as returned from XNET IP Stack Get Info.vi): virtual interface name (recommended) string that represents the decimal value of ifIndex IP address (see Supported Features) |

#### Description

The XNET UDP Socket Multicast Open.vi adds membership to a single multicast group. Use the Add Group Membership method to add membership to additional multicast groups on a single socket.

In Berkeley sockets APIs, this property corresponds to IP_ADD_MEMBERSHIP.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetudpsocketinvokemethodremovegroupmember.html language=enus -->
## TOPIC 00280: ni-xnet-api-ref/xnetudpsocketinvokemethodremovegroupmember.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetudpsocketinvokemethodremovegroupmember.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetudpsocketinvokemethodremovegroupmember.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

Remove Group Member

Remove Group Member

#### Purpose

Remove (drop) member from a multicast group.

#### Inputs

|  | multicast address specifies the multicast address. See Supported Features. |
| --- | --- |
|  | local interface identifies a specific virtual interface in the IP Stack on which to remove multicast group membership. The virtual interface is identified using one of the following (as returned from XNET IP Stack Get Info.vi): virtual interface name (recommended) string that represents the decimal value of ifIndex IP address (see Supported Features) |

#### Description

Use this method to remove memberships that were added using the [Add Group Membership](xnetudpsocketinvokemethodaddgroupmember.html) method.

In Berkeley sockets APIs, this property corresponds to IP_DROP_MEMBERSHIP.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetudpsocketinvokenode.html language=enus -->
## TOPIC 00281: ni-xnet-api-ref/xnetudpsocketinvokenode.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetudpsocketinvokenode.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetudpsocketinvokenode.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET UDP Socket Invoke Node

Invoke Node

#### Format

[IMAGE alt='image' src='xnetudpsocketinvokenode.gif']

#### Description

Methods in this node can be used with the XNET UDP Socket VIs. The most common usage is after opening or creating a socket (e.g., XNET UDP Socket Open.vi), and prior to reading/writing data with the socket. All methods are optional.

Each method node has terminals for XNET UDP Socket input/output and error in/out.

Available invoke methods are listed below.

| Method | Description |
| --- | --- |
| Add Group Member | Add a member to join a multicast group. |
| Remove Group Member | Remove a member from a multicast group. |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetudpsocketmulticastopenreadonlyvi.html language=enus -->
## TOPIC 00282: ni-xnet-api-ref/xnetudpsocketmulticastopenreadonlyvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetudpsocketmulticastopenreadonlyvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetudpsocketmulticastopenreadonlyvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET UDP Socket Multicast Open (Read Only).vi

XNET UDP Socket Multicast Open (Read Only).vi

#### Purpose

Subscribes to a UDP multicast group with read-only access on the port you specify.

#### Format

[IMAGE alt='image' src='xnetudpsocketmulticastopenreadonly.gif']

#### Inputs

|  | stack is the XNET IP Stack in which the new socket is opened. |
| --- | --- |
|  | local port is the local port you want to use to receive UDP datagrams. By default (0), this VI dynamically chooses an available UDP port for communication. |
|  | multicast address is the IP address of the multicast group you want to join. This terminal is required and returns an error if you do not specify an address. Multicast group addresses are in the 224.0.0.0 to 239.255.255.255 range. |
|  | error in is the error cluster input (refer to Error Handling). |
|  | local interface identifies a specific virtual interface in the IP Stack on which to bind the socket. The virtual interface is identified using one of the following (as returned from XNET IP Stack Get Info.vi): virtual interface name (recommended) string that represents the decimal value of ifIndex IP address (see Supported Features) This input is optional. If local interface is empty (default), the socket is bound to any virtual interface in the IP stack. |

#### Outputs

|  | socket is a network connection refnum that uniquely identifies the connection. Use this value to refer to this connection in subsequent VI calls. |
| --- | --- |
|  | actual local port is the port number the VI used. If you wire 0 to the local port input, this VI dynamically chooses an available UDP port that the XNET IP stack determines is valid for use. If you wire a value other than 0 to the local port input, actual local port returns the input port number. |
|  | error out is the error cluster output (refer to Error Handling). |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwriteframecanvi.html language=enus -->
## TOPIC 00283: ni-xnet-api-ref/xnetwriteframecanvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwriteframecanvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwriteframecanvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (Frame CAN).vi

XNET Write (Frame CAN).vi

#### Purpose

Writes data to a session as an array of CAN frames. The session must use a CAN interface and a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

#### Format

[IMAGE alt='image' src='xnetwriteframecan.gif']

#### Inputs

|  | session in is the session to write. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. |
| --- | --- |
|  | data provides the array of LabVIEW clusters. Each array element corresponds to a frame value to transmit. For a Frame Output Single-Point session mode, the order of frames in the array corresponds to the order in the session list. The data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for write. For an example of how this data applies to network traffic, refer to Frame Output Stream Mode, Frame Output Queued Mode, or Frame Output Single-Point Mode. Additionally, the XNET Write (Frame CAN) VI can be called on any signal or frame input session if it contains one or more Event Remote frames (refer to CAN:Timing Type). In this case, it signals an event to transmit those remote frames. The data parameter is ignored in this case, and you can set it to an empty array. The elements of each cluster are specific to the CAN protocol. For more information, refer to Summary of the CAN Standard or the CAN protocol specification. The cluster elements are: identifier is the CAN frame arbitration identifier. If extended? is false, the identifier uses standard format, so 11 bits of this identifier are valid. If extended? is true, the identifier uses extended format, so 29 bits of this identifier are valid. extended? is a Boolean value that determines whether the identifier uses extended format (true) or standard format (false). echo? is not used for transmit. You must set this element to false. type is the frame type (decimal value in parentheses): CAN Data (0)The CAN data frame contains payload data. This is the most commonly used frame type for CAN. In ISO CAN FD interface mode, this transmits a frame according to the interface setting (FD or FD+BRS). ISO CAN FD mode allows transmitting CAN 2.0, CAN FD, or CAN FD+BRS frames using the frame type (refer to the types listed below). CAN 2.0 Data (8) The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN 2.0 frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). CAN FD Data (16) The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN FD (no BRS) frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). CAN FD+BRS Data (24) The CAN data frame contains payload data. In ISO CAN FD+BRS mode, this frame is transmitted as a CAN FD+BRS frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). CAN Remote (1)CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using the XNET Read VI. timestamp represents absolute time using the LabVIEW absolute timestamp type. timestamp is not used for transmit. You must set this element to the default value, invalid (0). payload is the array of data bytes for a CAN data frame. The array size indicates the payload length of the frame value to transmit. According to the CAN protocol, the payload length range is 0–8. For CAN FD, the range can be 0–8, 12, 16, 20, 24, 32, 48, or 64. When the session mode is Frame Output Single-Point or Frame Output Queued, the number of bytes in the payload array must be less than or equal to the Payload Length property of the corresponding frame. You can leave all other CAN frame cluster elements uninitialized. For more information, refer to the topic for each mode. For a transmitted remote frame (CAN Remote type), the payload length in the frame value specifies the number of payload bytes requested. Your application provides this payload length by filling payload with the requested number of bytes. This enables your application to specify the frame payload length, but the actual values in the payload bytes are ignored (not contained in the transmitted frame). |
|  | identifier is the CAN frame arbitration identifier. If extended? is false, the identifier uses standard format, so 11 bits of this identifier are valid. If extended? is true, the identifier uses extended format, so 29 bits of this identifier are valid. |
|  | extended? is a Boolean value that determines whether the identifier uses extended format (true) or standard format (false). |
|  | echo? is not used for transmit. You must set this element to false. |
|  | type is the frame type (decimal value in parentheses): CAN Data (0)The CAN data frame contains payload data. This is the most commonly used frame type for CAN. In ISO CAN FD interface mode, this transmits a frame according to the interface setting (FD or FD+BRS). ISO CAN FD mode allows transmitting CAN 2.0, CAN FD, or CAN FD+BRS frames using the frame type (refer to the types listed below). CAN 2.0 Data (8) The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN 2.0 frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). CAN FD Data (16) The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN FD (no BRS) frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). CAN FD+BRS Data (24) The CAN data frame contains payload data. In ISO CAN FD+BRS mode, this frame is transmitted as a CAN FD+BRS frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). CAN Remote (1)CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using the XNET Read VI. |
| CAN Data (0) | The CAN data frame contains payload data. This is the most commonly used frame type for CAN. In ISO CAN FD interface mode, this transmits a frame according to the interface setting (FD or FD+BRS). ISO CAN FD mode allows transmitting CAN 2.0, CAN FD, or CAN FD+BRS frames using the frame type (refer to the types listed below). |
| CAN 2.0 Data (8) | The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN 2.0 frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). |
| CAN FD Data (16) | The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN FD (no BRS) frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). |
| CAN FD+BRS Data (24) | The CAN data frame contains payload data. In ISO CAN FD+BRS mode, this frame is transmitted as a CAN FD+BRS frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). |
| CAN Remote (1) | CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using the XNET Read VI. |
|  | timestamp represents absolute time using the LabVIEW absolute timestamp type. timestamp is not used for transmit. You must set this element to the default value, invalid (0). |
|  | payload is the array of data bytes for a CAN data frame. The array size indicates the payload length of the frame value to transmit. According to the CAN protocol, the payload length range is 0–8. For CAN FD, the range can be 0–8, 12, 16, 20, 24, 32, 48, or 64. When the session mode is Frame Output Single-Point or Frame Output Queued, the number of bytes in the payload array must be less than or equal to the Payload Length property of the corresponding frame. You can leave all other CAN frame cluster elements uninitialized. For more information, refer to the topic for each mode. For a transmitted remote frame (CAN Remote type), the payload length in the frame value specifies the number of payload bytes requested. Your application provides this payload length by filling payload with the requested number of bytes. This enables your application to specify the frame payload length, but the actual values in the payload bytes are ignored (not contained in the transmitted frame). |
|  | timeout is the time to wait for the CAN frame data to be queued up for transmit. The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds. If timeout is positive, the XNET Write (Frame CAN) VI waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned. If timeout is negative, the XNET Write (Frame CAN) VI waits indefinitely for space to become available in queues. If timeout is 0, the XNET Write (Frame CAN) VI does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call the XNET Write (Frame CAN) VI again at a later time with the same data. This input is optional. The default value is 10.0 (10 seconds). If the session mode is Frame Output Single-Point, you must set timeout to 0.0. Because this mode writes the most recent value of each frame, timeout does not apply. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

The data represents an array of CAN frames. Each CAN frame uses a LabVIEW cluster with CAN-specific elements.

The CAN frames are associated to the session's list of frames as follows:

- Frame Output Stream : Array of all frame values for transmit (list ignored).
- Frame Output Queued : Array of frame values to transmit for the single frame specified in the list.
- Frame Output Single-Point : Array of single frame values, one for each frame specified in the list.
- Any signal or frame input mode: The data parameter is ignored, and you can set it to an empty array. The VI transmits an event remote frame.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwriteframeenetvi.html language=enus -->
## TOPIC 00284: ni-xnet-api-ref/xnetwriteframeenetvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwriteframeenetvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwriteframeenetvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (Frame Ethernet).vi

XNET Write (Frame Ethernet).vi

#### Purpose

Writes data to a session as an array of Ethernet frames. The session must use an Ethernet interface and a mode of Frame Output Stream.

#### Format

[IMAGE alt='image' src='xnetwriteframeethernet.gif']

#### Inputs

|  | session in is the session to write. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Frame Output Stream. |  |
| --- | --- | --- |
|  | data provides an array of LabVIEW clusters. Each array element corresponds to a frame value to transmit. The elements of each cluster are specific to the Ethernet protocol. The data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for write. type is the type of Ethernet frame. It is a ring (enumerated list) with the following values: EnumerationValueDescription Ethernet Data0Ethernet frame received or transmitted. Delay Frame225Hardware delays for the specified time. Special frame type described in Special Frames. Future Time Wait226Hardware waits until the absolute time associated with this frame occurs before processing subsequent frames. Special frame type described in Special Frames. local timestamp is a timestamp using XNET local time. The timestamp uses the LabVIEW absolute timestamp type. network timestamp is a timestamp using network time (clock of the network's time synchronization protocol, such as IEEE Std 802.1AS). The timestamp uses the LabVIEW absolute timestamp type. network synced? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). receive? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). transmit? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). error? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). frame data is an array of bytes that provides the data of the Ethernet frame. Using the terminology from IEEE Std 802.3, the frame data begins with the first byte of the destination MAC address, and ends with the last byte of the mac_service_data_unit (MSDU). For examples of two commonly used formats for frame data, refer to the Raw Frame Format. In order to obtain the payload data that is contained in the frame, your code must decode the layered headers in frame data. For example, for an IPv4 UDP packet, you decode the Ethernet header, including the EtherType, to determine that the remaining data is an IPv4 packet; then you decode the IPv4 header, including the Protocol, to determine that the remaining data is a UDP packet; and then you decode the UDP header and its payload data. The Source MAC Address Auto property specifies automatic handling of the source MAC address in frame data (i.e., offset 6 through 11). If Source Address MAC Auto is true (default), XNET automatically replaces the source MAC address bytes with its own MAC Address. If Source Address MAC Auto is false, XNET does not alter the source MAC address, so that you can specify this address in frame data. The maximum length of this array is provided in the Payload Length Maximum property. fcs is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). |  |
|  | type is the type of Ethernet frame. It is a ring (enumerated list) with the following values: EnumerationValueDescription Ethernet Data0Ethernet frame received or transmitted. Delay Frame225Hardware delays for the specified time. Special frame type described in Special Frames. Future Time Wait226Hardware waits until the absolute time associated with this frame occurs before processing subsequent frames. Special frame type described in Special Frames. |  |
| Enumeration | Value | Description |
| Ethernet Data | 0 | Ethernet frame received or transmitted. |
| Delay Frame | 225 | Hardware delays for the specified time. Special frame type described in Special Frames. |
| Future Time Wait | 226 | Hardware waits until the absolute time associated with this frame occurs before processing subsequent frames. Special frame type described in Special Frames. |
|  | local timestamp is a timestamp using XNET local time. The timestamp uses the LabVIEW absolute timestamp type. |  |
|  | network timestamp is a timestamp using network time (clock of the network's time synchronization protocol, such as IEEE Std 802.1AS). The timestamp uses the LabVIEW absolute timestamp type. |  |
|  | network synced? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). |  |
|  | receive? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). |  |
|  | transmit? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). |  |
|  | error? is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). |  |
|  | frame data is an array of bytes that provides the data of the Ethernet frame. Using the terminology from IEEE Std 802.3, the frame data begins with the first byte of the destination MAC address, and ends with the last byte of the mac_service_data_unit (MSDU). For examples of two commonly used formats for frame data, refer to the Raw Frame Format. In order to obtain the payload data that is contained in the frame, your code must decode the layered headers in frame data. For example, for an IPv4 UDP packet, you decode the Ethernet header, including the EtherType, to determine that the remaining data is an IPv4 packet; then you decode the IPv4 header, including the Protocol, to determine that the remaining data is a UDP packet; and then you decode the UDP header and its payload data. The Source MAC Address Auto property specifies automatic handling of the source MAC address in frame data (i.e., offset 6 through 11). If Source Address MAC Auto is true (default), XNET automatically replaces the source MAC address bytes with its own MAC Address. If Source Address MAC Auto is false, XNET does not alter the source MAC address, so that you can specify this address in frame data. The maximum length of this array is provided in the Payload Length Maximum property. |  |
|  | fcs is not used for XNET Write (Frame Ethernet). Refer to XNET Read (Frame Ethernet). |  |
|  | timeout is the time to wait for the Ethernet frame data to be queued up for transmit. The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds. If timeout is positive, the XNET Write (Frame Ethernet) VI waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned. If timeout is negative, the XNET Write (Frame Ethernet) VI waits indefinitely for space to become available in queues. If timeout is 0, the XNET Write (Frame Ethernet) VI does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call the XNET Write (Frame Ethernet) VI again at a later time with the same data. This input is optional. The default value is 10.0 (10 seconds). |  |
|  | error in is the error cluster input (refer to Error Handling). |  |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

The data represents an array of Ethernet frames. Each Ethernet frame uses a LabVIEW cluster with Ethernet-specific elements.

|  | Note When the Frame Output Stream session is in in Replay Exclusive or Replay Inclusive mode (see Interface:Output Stream Timing), hardware will evaluate the timestamp for each frame and output the frame at the right time, in accordance with the policy described in Handling Timestamps. The Interface:Ethernet:Output Stream Timescale property configures which timestamp parameter is used. |
| --- | --- |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwriteframelinvi.html language=enus -->
## TOPIC 00285: ni-xnet-api-ref/xnetwriteframelinvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwriteframelinvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwriteframelinvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (Frame LIN).vi

XNET Write (Frame LIN).vi

#### Purpose

Writes data to a session as an array of LIN frames. The session must use a LIN interface and a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

#### Format

[IMAGE alt='image' src='xnetwriteframelin.gif']

#### Inputs

|  | session in is the session to write. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. |
| --- | --- |
|  | data provides the array of LabVIEW clusters. Each array element corresponds to a frame value to transmit. For a Frame Output Single-Point session mode, the order of frames in the array corresponds to the order in the session list. For Frame Output Queued session mode, the data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for write. For an example of how this data applies to network traffic, refer to Frame Output Stream Mode, Frame Output Queued Mode, or Frame Output Single-Point Mode. The elements of each cluster are specific to the LIN protocol. For more information, refer to Summary of the LIN Standard or the LIN protocol specification. The cluster elements are: identifier is not used for transmit. You must set this element to 0. Each frame is identified based on the list of frames or signals provided for the session. The actual identifier to transmit is taken from the database (frame and schedule properties). Therefore, this identifier in the frame value is ignored. event slot? is not used for transmit. You must set this element to false. The currently running schedule is used to map the specific frame to a corresponding schedule entry (slot). The schedule entry itself determines whether the slot is unconditional, sporadic, or event triggered. event ID is not used for transmit. You must set this element to 0. echo? is not used for transmit. You must set this element to false. type is the frame type (decimal value in parentheses): LIN Data (64)The LIN data frame contains payload data. This is currently the only frame type for LIN. timestamp represents absolute time using the LabVIEW absolute timestamp type. timestamp is not used for transmit. You must set this element to the default value, invalid (0). payload is the array of data bytes for a LIN data frame. The array size indicates the payload length of the frame value to transmit. According to the LIN protocol, the payload length range is 0–8. The number of bytes in the payload array must match the Payload Length property of the corresponding frame. You can leave all other LIN frame cluster elements uninitialized. For more information, refer to the topic for each mode. If you use the frame payload within an event-triggered schedule entry (slot), the first byte of data on the network is the frame's payload identifier. The LIN standard requires this even if the frame transmits in an unconditional or sporadic slot. For this type of LIN frame, the actual data (for example, signal values) is limited to 7 bytes. For this type of frame, you must write the first byte (payload of 8 bytes even if only the last 7 are used), but NI-XNET ignores the value and fills in the first byte for you, using the known frame ID from the session's configuration. |
|  | identifier is not used for transmit. You must set this element to 0. Each frame is identified based on the list of frames or signals provided for the session. The actual identifier to transmit is taken from the database (frame and schedule properties). Therefore, this identifier in the frame value is ignored. |
|  | event slot? is not used for transmit. You must set this element to false. The currently running schedule is used to map the specific frame to a corresponding schedule entry (slot). The schedule entry itself determines whether the slot is unconditional, sporadic, or event triggered. |
|  | event ID is not used for transmit. You must set this element to 0. |
|  | echo? is not used for transmit. You must set this element to false. |
|  | type is the frame type (decimal value in parentheses): LIN Data (64)The LIN data frame contains payload data. This is currently the only frame type for LIN. |
| LIN Data (64) | The LIN data frame contains payload data. This is currently the only frame type for LIN. |
|  | timestamp represents absolute time using the LabVIEW absolute timestamp type. timestamp is not used for transmit. You must set this element to the default value, invalid (0). |
|  | payload is the array of data bytes for a LIN data frame. The array size indicates the payload length of the frame value to transmit. According to the LIN protocol, the payload length range is 0–8. The number of bytes in the payload array must match the Payload Length property of the corresponding frame. You can leave all other LIN frame cluster elements uninitialized. For more information, refer to the topic for each mode. If you use the frame payload within an event-triggered schedule entry (slot), the first byte of data on the network is the frame's payload identifier. The LIN standard requires this even if the frame transmits in an unconditional or sporadic slot. For this type of LIN frame, the actual data (for example, signal values) is limited to 7 bytes. For this type of frame, you must write the first byte (payload of 8 bytes even if only the last 7 are used), but NI-XNET ignores the value and fills in the first byte for you, using the known frame ID from the session's configuration. |
|  | timeout is the time to wait for the LIN frame data to be queued up for transmit. The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds. If timeout is positive, the XNET Write (Frame LIN) VI waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned. If timeout is negative, the XNET Write (Frame LIN) VI waits indefinitely for space to become available in queues. If timeout is 0, the XNET Write (Frame LIN) VI does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call the XNET Write (Frame LIN) VI again at a later time with the same data. This input is optional. The default value is 10.0 (10 seconds). If the session mode is Frame Output Single-Point, you must set timeout to 0.0. Because this mode writes the most recent value of each frame, timeout does not apply. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

The data represents an array of LIN frames. Each LIN frame uses a LabVIEW cluster with LIN-specific elements.

The LIN frames are associated to the session's list of frames as follows:

- Frame Output Stream Mode : Array of all frame values for transmit (list ignored). If the payload is an empty array, only the header part of the LIN frame is transmitted. If the payload is not an empty array, the header and response parts of the LIN frame are transmitted.
- Frame Output Queued : Array of frame values to transmit for the single frame specified in the list.
- Frame Output Single-Point : Array of single frame values, one for each frame specified in the list.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwritesignalxyvi.html language=enus -->
## TOPIC 00286: ni-xnet-api-ref/xnetwritesignalxyvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwritesignalxyvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwritesignalxyvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (Signal XY).vi

XNET Write (Signal XY).vi

#### Purpose

Writes data to a session of Signal Output XY mode. The data represents a sequence of signal values for transmit using each frame's timing as the database specifies.

#### Format

[IMAGE alt='image' src='xnetwritesignalxy.gif']

#### Inputs

|  | session in is the session to write. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session mode must be Signal Output XY. |
| --- | --- |
|  | data provides an array of LabVIEW clusters. Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list. The data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 elements if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for writing. For an example of how this data applies to network traffic, refer to Signal Output XY Mode. Each cluster contains two arrays, one for value, and one for timestamp. Each value is mapped to a frame for transmit. When signals exist in different frames, the array sizes may be different from one cluster (signal) to another. The cluster elements are: timestamp is the array of LabVIEW timestamps. The timestamp array is unused (reserved) for Signal Output XY. If you change it from its default value of empty, the XNET Write (Signal XY) VI returns an error. value is the array of signal values, one for each frame that contains the signal. Frame transmission is timed according to the frame properties in the database. Each signal value is scaled, 64-bit floating point. |
|  | timestamp is the array of LabVIEW timestamps. The timestamp array is unused (reserved) for Signal Output XY. If you change it from its default value of empty, the XNET Write (Signal XY) VI returns an error. |
|  | value is the array of signal values, one for each frame that contains the signal. Frame transmission is timed according to the frame properties in the database. Each signal value is scaled, 64-bit floating point. |
|  | timeout is the time to wait for the data to be queued for transmit. The timeout does not wait for frames to be transmitted on the network (refer to the XNET Wait (Transmit Complete) VI). The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds. If timeout is positive, the XNET Write (Signal XY) VI waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned. If timeout is negative, the XNET Write (Signal XY) VI waits indefinitely for space to become available in queues. If timeout is 0, the XNET Write (Signal XY) VI does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call the XNET Write (Signal XY) VI again at a later time with the same data. This input is optional. The default value is 10.0 (10 seconds). |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwritestateethernetwakevi.html language=enus -->
## TOPIC 00287: ni-xnet-api-ref/xnetwritestateethernetwakevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwritestateethernetwakevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwritestateethernetwakevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (State Ethernet Wake).vi

XNET Write (State Ethernet Wake).vi

#### Purpose

Writes a request for the local Ethernet interface and its remote link partner to wake up. You can use this XNET Write VI with any input or output session for Ethernet.

#### Format

[IMAGE alt='image' src='xnetwritestateethernetwakevi.gif']

#### Inputs

|  | session in is the session to use for the state change. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Write (State Ethernet Wake)** VI with any XNET session mode, as long as the session interface is Ethernet. The wake up commands apply to the Ethernet interface and therefore apply to all sessions created on that interface.

The command that is sent after calling the **XNET Write (State Ethernet Wake)** VI depends on the current PHY Power Mode of the interface. If the XNET interface is in Sleep mode, the XNET interface wakes up and transmits the Wake Up Pulse (WUP) command to the remote link partner to wake up. If the XNET interface is in Normal mode (i.e., is already awake), the XNET interface transmits the Wake Up Request (WUR) command to the remote link partner, which is intended to be sent over active links. The VI waits for the PHY Power Mode to reach the Normal state before returning; an error will be returned if the wake command is unsuccessful. If you call the **XNET Write (State Ethernet Wake)** VI multiple times, subsequent calls will transmit the WUR command if the interface is already awake.

|  | Note The sleep/wake capability is based on the OPEN Alliance TC10 Sleep/Wake 2.0 specification and is only supported on the PXIe-8523. The port must be configured for a link speed of 100 Mbps and a port mode of Direct to use the sleep/wake capability. |
| --- | --- |

|  | Note After waking the interface from sleep, there may be a slight delay before the interface is ready to send or receive data. Query the Interface:Ethernet:Operational Status property to ensure Operational Status is Up before data is sent or received. |
| --- | --- |

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwritestateflexraysymbolvi.html language=enus -->
## TOPIC 00288: ni-xnet-api-ref/xnetwritestateflexraysymbolvi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwritestateflexraysymbolvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwritestateflexraysymbolvi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (State FlexRay Symbol).vi

XNET Write (State FlexRay Symbol).vi

#### Purpose

Writes a request for the FlexRay interface to transmit a symbol on the FlexRay bus. You can use this XNET Write VI with any input or output session for FlexRay.

#### Format

[IMAGE alt='image' src='xnetwritestateflexraysymbolvi.gif']

#### Inputs

|  | session in is the session to write. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session must use a FlexRay interface. |
| --- | --- |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the **XNET Write (State FlexRay Symbol)** VI with any XNET session mode, as long as the session interface is FlexRay. Because the symbol write applies to the FlexRay interface, it can apply to multiple sessions.

After calling the **XNET Write (State FlexRay Symbol)** VI, the XNET interface transmits the symbol during the symbol window of the FlexRay cycle following the currently executing cycle. If you call the **XNET Write (State FlexRay Symbol)** VI multiple times, only the most recent symbol is transmitted.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwritestatelinschedulechangevi.html language=enus -->
## TOPIC 00289: ni-xnet-api-ref/xnetwritestatelinschedulechangevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwritestatelinschedulechangevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwritestatelinschedulechangevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write (State LIN Schedule Change).vi

XNET Write (State LIN Schedule Change).vi

#### Purpose

Writes a request for the LIN interface to change the running schedule. You can use this XNET Write VI with any input or output session for LIN.

#### Format

[IMAGE alt='image' src='xnetwritestatelinschedulechange.gif']

#### Inputs

|  | session in is the session to use for the schedule change. This session is selected from the LabVIEW project or returned from the XNET Create Session VI. The session must use a LIN interface. |
| --- | --- |
|  | data is the XNET LIN schedule. Although the data type for this input is the XNET LIN Schedule I/O Name, you also can wire a string. The data input supports the following options: XNET LIN Schedule I/O Name: You can use the complete I/O name. This provides features such as the ability to choose from LIN schedules in a selected database. String with XNET LIN short name: If you prefer to use the XNET LIN Schedule Name (Short) property, you can wire in the property as a string. String with decimal number: This is interpreted as an index into the XNET Cluster LIN:Schedules property used for this session. If you are editing your database file to add/remove LIN schedules, this index may change, in which case the name is the recommended option. |
|  | error in is the error cluster input (refer to Error Handling). |

#### Outputs

|  | session out is the same as session in, provided for use with subsequent VIs. |
| --- | --- |
|  | error out is the error cluster output (refer to Error Handling). |

#### Description

You can use the XNET Write (State LIN Schedule Change) VI with any XNET session mode, as long as the session interface is LIN. Because the schedule change applies to the LIN interface, it can apply to multiple sessions.

According to the LIN protocol, only the master executes schedules, not slaves. If the XNET Session [Interface:LIN:Master?](propertysessioninterfacelinmaster.html) property is false (slave), this write function implicitly sets that property to true (master). If the interface currently is running as a slave, this write returns an error, because it cannot change to master while running.

The XNET Write (State LIN Schedule Change) VI behavior depends on the Run Mode property of the XNET LIN schedule that you wire in as data:

- Continuous : This mode changes the single run-continuous schedule for the interface. The single run-continuous schedule executes all its entries (slots) repetitively, starting over with the first entry after running the last entry. 



The run-continuous schedule is handled as if it is lowest priority. If you write a run-once schedule in the middle of a run-continuous execution, the run-continuous schedule is interrupted after the current slot finishes. The scheduler switches to the run-once schedule, and when all run-once schedules are done, the scheduler returns to the slot in the run-continuous schedule where it left off. For example, if run-continuous schedule A has 4 slots, and it is executing slot 2 when a run-once schedule B is written, slot 2 of A finishes, then all slots of schedule B run, then the scheduler returns to slot 3 of schedule A. 



Only one run-continuous schedule exists at a time. If you change from one run-continuous schedule to another in the middle of a run, the current schedule completes all of its slots, then the scheduler changes to the new run-continuous schedule.
- Once : This mode writes a request for a run-once schedule. Multiple run-once schedules can be pending for execution. Each run-once schedule executes all its entries (slots), and then it is considered done. 



Each run-once schedule has a priority from 1 to 254. Lower values correspond to higher priority (1 is highest). The LIN interface's scheduler maintains a priority queue of run-once schedule requests. This means the highest-priority run-once schedule executes first, followed by the next run-once in priority, and when no run-once schedules are pending, the interface returns to the run-continuous schedule. 



A run-once schedule cannot interrupt another run-once schedule. For example, if run-once schedule X has 3 slots and is executing slot 0 when a run-once schedule Y with higher priority is written, slots 0, 1, and 2 of X finish, then all slots of schedule Y run.
- Null : This mode stops scheduler execution after the current slot is finished. The queue of run-once schedules is flushed (all elements discarded). 



The null schedule is considered the highest priority schedule. It overrides the single run-continuous schedule, thus acting as the default scheduling behavior. For example, if you write a null schedule, then write a run-once schedule, the run-once schedule executes all its slots, then communication stops (returns to null schedule). 



The XNET Write (State LIN Schedule Change) VI does not wait for the requested schedule to finish execution prior to return. The VI does not wait for the schedule to begin execution, because in the case of run-once schedules, that may take a long time (depending on priority). Because this VI simply writes a schedule request and returns, it is safe to use within a high-priority loop in LabVIEW Real-Time.

Node configuration is handled using the XNET Write (State LIN Schedule Change) VI instead of the [XNET Write (State LIN Diagnostic Schedule Change) VI](xnetwritestatelindiagnosticschedulechangevi.html). Wire the node configuration schedule defined for the LIN cluster into the XNET Write (State LIN Schedule Change) VI so that it is the first schedule executed for the LIN, with a run mode of once. The data for each node configuration service request entry in the node configuration schedule is automatically transmitted by the master. After the node configuration schedule has completed, use the [XNET Write (State LIN Diagnostic Schedule Change) VI](xnetwritestatelindiagnosticschedulechangevi.html) to write master request messages and query for slave response messages, or the XNET Write (State LIN Schedule Change) VI to run normal schedules.

<!--NI_TOPIC bundle=ni-xnet-api-ref path=ni-xnet-api-ref/xnetwritevi.html language=enus -->
## TOPIC 00290: ni-xnet-api-ref/xnetwritevi.html

- bundle_id: `ni-xnet-api-ref`
- source_path: `ni-xnet-api-ref/xnetwritevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-api-ref/raw/resource/enus/ni-xnet-api-ref/xnetwritevi.html
- document_id: `ni-xnet-api-ref`
- page_type: `leaf`
- content_type: ``

XNET Write.vi

XNET Write.vi

#### Purpose

Writes data to the network using an XNET session.

#### Description

The instances of this polymorphic VI specify the type of data provided.

The [XNET Read](xnetreadvi.html) and XNET Write VIs are optimized for real-time performance. The XNET Write VI executes quickly and avoids access to shared resources that can induce jitter on other VI priorities.

The XNET Write VIs are asynchronous, in that data is written to a hardware buffer, but the XNET Write VI returns before the corresponding frames are transmitted onto the network. If you need to wait for the data provided to the XNET Write VI to transmit onto the network, use the [XNET Wait (Transmit Complete) VI](xnetwaittransmitcompletevi.html).

There are two categories of XNET Write instance VIs:

- Signal : Use when the session mode is Signal Output. The XNET Write VI instance must match the mode exactly (for example, the instance is Signal Waveform when the mode is Signal Output Waveform).
- Frame : Use when the session mode is Frame Output. The XNET Write VI instance specifies the desired data type for frames and is not related to the mode. For an easy-to-use data type, use the CAN, FlexRay, or LIN instance.
- State: Use to change the session's interface state. You can use these instances in addition to Signal or Frame instances, and they are not related to the mode. These instances are optimized for performance. Although property nodes may provide write access to similar runtime data, those properties are not necessarily optimized for real-time loops.

The XNET Write instance VIs are:

- [Signal Single-Point](xnetwritesignalsinglepointvi.html) : The session mode is Signal Output Single-Point.
- **Signal Waveform** : The session mode is Signal Output Waveform.
- **Signal XY** : The session mode is Signal Output XY.
- **Frame CAN** : The session uses a CAN interface, and the mode is Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. Additionally, the XNET Write (Frame CAN) VI can be called on any signal or frame input session if it contains one or more Event Remote frames (refer to CAN:Timing Type ). In this case, it signals an event to transmit those remote frames.
- **Frame Ethernet** : Writes data to a session as an array of Ethernet frames. The session must use an Ethernet interface and a mode of Frame Output Stream.
- **Frame FlexRay** : The session uses a FlexRay interface, and the mode is Frame Output Single-Point, Frame Output Queued, PDU Output Single-Point (similar to Frame Output Single-Point), or PDU Output Queued (similar to Frame Output Queued).
- **Frame LIN** : The session uses a LIN interface, and the mode is Frame Output Stream, Frame Output Single-Point, or Frame Output Queued.
- **Frame Raw** : A data type for frame output that is protocol independent and more efficient than the CAN, FlexRay, and LIN instances.
- **State LIN Diagnostic Schedule Change** : Write a request for the LIN interface to change the diagnostic schedule.
- **State LIN Schedule Change** : Submit a request for the LIN interface to change the running schedule.
- **State Ethernet Sleep** : Writes a request for the local Ethernet interface and its remote link partner to sleep.
- **State Ethernet Wake** : Writes a request for the local Ethernet interface and its remote link partner to wake up.
- **State FlexRay Symbol** : Write a request for the FlexRay interface to transmit a symbol on the FlexRay bus.
