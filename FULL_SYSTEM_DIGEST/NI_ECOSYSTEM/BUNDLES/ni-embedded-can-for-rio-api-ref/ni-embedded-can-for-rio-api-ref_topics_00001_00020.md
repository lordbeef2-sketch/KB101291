# NI DOCUMENT BUNDLE: ni-embedded-can-for-rio-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-embedded-can-for-rio-api-ref start=1 end=20 -->
<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_create.html language=enus -->
## TOPIC 00001: CAN Create Interface VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_create.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_create.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Create Interface VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Creates a CAN interface object to read or write data on the bus. You must create a CAN interface before using all other [Embedded CAN for RIO](embcan_rio.html) VIs.

The session that you create using this VI is in Stopped mode. Use the [CAN Start](em_start.html) VI to start the session before any communication.

[IMAGE alt='image' src='../cancreateinterfacevi.gif']

|  | interface index specifies a zero-based number of the interface to create. |
| --- | --- |
|  | baud rate specifies the CAN interface baud rate. Refer to the Baud Rate property for the proper values. The default is 125,000 bps. |
|  | receive queue size specifies the number of frames to store in the receive queue. Refer to the Receive Queue Size property for the proper values. The default is 5. Use receive queue size for the Single-Board RIO hardware. Do not use this control for CompactRIO with built-in CAN port hardware, because the hardware has a built-in receive queue in size of 64. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of the interface. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_flush.html language=enus -->
## TOPIC 00002: CAN Flush VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_flush.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_flush.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Flush VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Flushes all queues for the specified CAN interface. Use this VI to discard all elements in the transmit queue or receive queue.

The CompactRIO with the built-in CAN port hardware does not support flushing the transmit buffer. A warning occurs if you flush the transmit queues for this hardware.

[Details](#details)

[IMAGE alt='image' src='../canflushvi.gif']

|  | interface object in specifies the refnum of the interface to flush. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Flush Details

Refer to the [CAN Read](em_can_read.html) VI, the [CAN Write](em_can_write.html) VI, and the [Receive Queue Size](propertyreceivequeuesize.html) property for more information about the transmit queue and the receive queue.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_read.html language=enus -->
## TOPIC 00003: CAN Read VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_read.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_read.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Read VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Reads a CAN frame on the bus.

When the [Auto Start?](propertyautostart.html) property is TRUE and a session has not been started, running this VI starts the session automatically.

This VI is optimized for real-time performance. This VI executes quickly and avoids access to shared resources that can induce jitter on other VI priorities.

[IMAGE alt='image' src='../canreadvi.gif']

|  | interface object in specifies the refnum of the interface to read. |
| --- | --- |
|  | timeout specifies the maximum time, in seconds, that the VI waits for a frame to become available. The default is 0. If timeout is negative, this VI waits indefinitely for a frame to become available. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | CAN frame returns elements that represent the received frame. identifier returns the CAN frame arbitration identifier. If extended? is TRUE, the 29 bits of identifier are valid. If extended? is FALSE, the 11 bits of identifier are valid. extended? returns whether identifier uses extended format or standard format. If extended? is TRUE, identifier uses the extended format. If extended? is FALSE, identifier uses the standard format. type returns the frame type in decimal value. 0CAN Data—The CAN data frame contains payload data. This is the most commonly used frame type for CAN.1CAN Remote—A CAN remote frame. An ECU transmits a CAN remote frame to request data for the corresponding identifier. Your application can respond by writing a CAN data frame for the identifier. payload returns the data bytes in the CAN data frame. The array size indicates the received frame value payload length. According to the CAN protocol, this payload length range is 0–8. For a received remote frame, the payload length in the frame value specifies the number of payload bytes requested. Use payload with the requested number of bytes to provide this payload length to your application. You can use the payload array size, but you must ignore the actual values in the payload bytes. |
|  | identifier returns the CAN frame arbitration identifier. If extended? is TRUE, the 29 bits of identifier are valid. If extended? is FALSE, the 11 bits of identifier are valid. |
|  | extended? returns whether identifier uses extended format or standard format. If extended? is TRUE, identifier uses the extended format. If extended? is FALSE, identifier uses the standard format. |
|  | type returns the frame type in decimal value. 0CAN Data—The CAN data frame contains payload data. This is the most commonly used frame type for CAN.1CAN Remote—A CAN remote frame. An ECU transmits a CAN remote frame to request data for the corresponding identifier. Your application can respond by writing a CAN data frame for the identifier. |
| 0 | CAN Data—The CAN data frame contains payload data. This is the most commonly used frame type for CAN. |
| 1 | CAN Remote—A CAN remote frame. An ECU transmits a CAN remote frame to request data for the corresponding identifier. Your application can respond by writing a CAN data frame for the identifier. |
|  | payload returns the data bytes in the CAN data frame. The array size indicates the received frame value payload length. According to the CAN protocol, this payload length range is 0–8. For a received remote frame, the payload length in the frame value specifies the number of payload bytes requested. Use payload with the requested number of bytes to provide this payload length to your application. You can use the payload array size, but you must ignore the actual values in the payload bytes. |
|  | timestamp returns the time depending on receive queue size of the CAN Create Interface VI. If receive queue size is greater than five, timestamp returns the time, in microseconds, that the NI-Embedded CAN for RIO software receives the frame from CAN bus. If receive queue size is five, timestamp returns the time, in microseconds, that you use the CAN Read VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_stop.html language=enus -->
## TOPIC 00004: CAN Stop VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_stop.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Stop VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Stops communication for the specified CAN interface.

Use this VI to stop receiving CAN frames from the bus.

[IMAGE alt='image' src='../canstopvi.gif']

|  | interface object in specifies the refnum of the interface to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_wait.html language=enus -->
## TOPIC 00005: CAN Wait VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_wait.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_wait.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Wait VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Waits for CAN frames or interfaces. You must manually select the polymorphic instance to use.

#### CAN Wait (Transmit Complete)

Waits for previously written frames to be transmitted to the bus. If the queue has more than one frame, use the CAN Wait (Transmit Complete) VI to wait until all frames are transmitted.

[IMAGE alt='image' src='../canwaitvi.gif']

|  | interface object in specifies the refnum of the interface to wait. |
| --- | --- |
|  | timeout specifies the maximum time, in seconds, that the VI waits for a frame to become available. The default is 0. If timeout is negative, this VI waits indefinitely for a frame to become available. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Wait (Interface Communicating)

Waits for the interface to establish communication with the bus. After the interface starts, the controller connects to the bus and starts communication. The CAN Wait (Interface Communicating) VI waits until communication with the bus has been established.

[IMAGE alt='image' src='../canwaitinterfacecommunicatingvi.gif']

|  | interface object in specifies the refnum of the interface to wait. |
| --- | --- |
|  | timeout specifies the maximum time, in seconds, that the VI waits for a frame to become available. The default is 0. If timeout is negative, this VI waits indefinitely for a frame to become available. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Wait (Remote Wakeup)

Waits for the CAN interface to wake up to react with the activity of a remote node on the bus. Use the CAN Wait (Remote Wakeup) VI to wait when you set the [Transceiver State](propertytransceiverstate.html) property to Sleep. The interface and the transceiver go into low-powered mode after you set the property to Sleep. If a remote CAN ECU transmits a frame, the transceiver detects this transmission and both the controller and transceiver wake up.

[IMAGE alt='image' src='../canwaitremotewakeupvi.gif']

|  | interface object in specifies the refnum of the interface to wait. |
| --- | --- |
|  | timeout specifies the maximum time, in seconds, that the VI waits for a frame to become available. The default is 0. If timeout is negative, this VI waits indefinitely for a frame to become available. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_write.html language=enus -->
## TOPIC 00006: CAN Write VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_write.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_can_write.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Write VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Transmits a CAN frame to the bus.

When the [Auto Start?](propertyautostart.html) property is TRUE, running this VI for the first time starts the interface automatically.

This VI is optimized for real-time performance and executes quickly to avoid access to shared resources that can induce jitter on other VI priorities.

[Details](#details)

[IMAGE alt='image' src='../canwrite.gif']

|  | interface object in specifies the refnum of the interface to write. |
| --- | --- |
|  | CAN frame specifies the elements that correspond to a frame value to transmit. identifier specifies the CAN frame arbitration identifier. If extended? is TRUE, the 29 bits of identifier are valid. If extended? is FALSE, the 11 bits of identifier are valid. extended? specifies whether identifier uses extended format or standard format. If extended? is TRUE, identifier uses the extended format. If extended? is FALSE, identifier uses the standard format. type specifies the frame type in decimal value. 0CAN Data—The CAN data frame contains payload data. This is the most commonly used frame type for CAN.1CAN Remote—CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using the CAN Read VI. payload specifies the data bytes in the CAN data frame. The array size indicates the received frame value payload length. According to the CAN protocol, the payload length range is 0–8. For a received remote frame, the payload length in the frame value specifies the number of payload bytes requested. Specify payload with the requested number of bytes to provide the payload length to your application. You can use the payload array size, but you must ignore the actual values in the payload bytes. |
|  | identifier specifies the CAN frame arbitration identifier. If extended? is TRUE, the 29 bits of identifier are valid. If extended? is FALSE, the 11 bits of identifier are valid. |
|  | extended? specifies whether identifier uses extended format or standard format. If extended? is TRUE, identifier uses the extended format. If extended? is FALSE, identifier uses the standard format. |
|  | type specifies the frame type in decimal value. 0CAN Data—The CAN data frame contains payload data. This is the most commonly used frame type for CAN.1CAN Remote—CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using the CAN Read VI. |
| 0 | CAN Data—The CAN data frame contains payload data. This is the most commonly used frame type for CAN. |
| 1 | CAN Remote—CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using the CAN Read VI. |
|  | payload specifies the data bytes in the CAN data frame. The array size indicates the received frame value payload length. According to the CAN protocol, the payload length range is 0–8. For a received remote frame, the payload length in the frame value specifies the number of payload bytes requested. Specify payload with the requested number of bytes to provide the payload length to your application. You can use the payload array size, but you must ignore the actual values in the payload bytes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Write Details

This VI is asynchronous, in that data is written to a hardware queue (transmit queue), but the CAN Write VI returns before the corresponding frames are transmitted onto the bus. If you need to wait for the data to transmit onto the bus, use the [CAN Wait (Transmit Complete)](em_can_wait.html) VI. The frame is removed from the transmit queue after the frame is transmitted successfully onto the bus.

Do not write to a full transmit queue. If a queue is already full, writing more data to the queue causes a Transmit Queue Full error.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_close_interface.html language=enus -->
## TOPIC 00007: CAN Close Interface VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_close_interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_close_interface.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Close Interface VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Closes a session you create by using the [CAN Create Interface](em_can_create.html) VI. This VI closes the session regardless of whether an error has occurred in a preceding operation or not. Use this VI to release memory before starting a new session or to discard all elements in the transmit queue or the receive queue.

[IMAGE alt='image' src='../cancloseinterfacevi.gif']

|  | interface object in specifies the refnum of the interface to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_set_fmode.html language=enus -->
## TOPIC 00008: CAN Set Filter Mode VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_set_fmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_set_fmode.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Set Filter Mode VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Sets the mode of the filter. Use this VI and the [CAN Set Filter Value](em_set_fvalue.html) VI to create Acceptance Filters. Acceptance Filters sort the incoming CAN frames for the CompactRIO with the built-in CAN port hardware and the single-board RIO hardware. Use this filter to reduce the burden of frame storage in the NI-Embedded CAN for RIO software.

CAN protocol

[Details](#details)

[IMAGE alt='image' src='../cansetfiltermode.gif']

|  | interface object in specifies the refnum of a CAN Interface Object. Use the CAN Create Interface VI to create this Interface Object. |
| --- | --- |
|  | filter mode specifies the mode of the filter to use. 0Disabled132-bit (Default)216-bit38-bit |
| 0 | Disabled |
| 1 | 32-bit (Default) |
| 2 | 16-bit |
| 3 | 8-bit |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of the CAN Interface Object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Set Filter Mode Details

In the NI-Embedded CAN for RIO software, you can define an Acceptance Filter to sort the incoming [CAN frames](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_canframes). If the incoming CAN frames meet the acceptance conditions of the filter, the software stores the frames in the received FIFO. If the incoming CAN frames do not meet the acceptance conditions, the software discards the frames.

To define a filter, you need to define the mode and [configure the frame](em_set_fvalue.html) for the filter. Complete the following steps to define a mode for a filter.

1. In this VI, right-click filter mode and select Create»Control from the shortcut menu. Select a mode for your filter according to the hardware type and your needs.

 

NI Single-Board RIO hardware supports the following modes: Disabled mode, 32-bit mode, 16-bit mode, and 8-bit mode. The CompactRIO with built-in CAN port hardware supports the Disabled mode and 32-bit mode. 

 

Select a mode according to your needs and the function of the mode. National Instruments recommends that you use the 32-bit mode to filter an incoming CAN frame with an extended identifier, because only 32-bit mode enables you to apply the filter to all of the 29 bits. To filter a frame with a standard identifier, National Instruments recommends that you use the 32-bit mode or the 16 -bit mode. Both modes enable you to apply the filter to all of the 11 bits. You can select from the following modes.
  - Disabled Mode —The software stores all incoming CAN frames.
  - 32-Bit Mode
    - Extended CAN Frames —The filter applies to all of the 29 bits and the remote transmission request (RTR).
    - Standard CAN Frames —The filter applies to all of the 11 bits and the RTR.
  - 16-Bit Mode
    - Extended CAN Frames —The filter applies to the upper 14 bits from bit 28 to bit 15.
    - Standard CAN Frames —The filter applies to all of the 11 bits and the RTR.
  - 8-Bit Mode
    - Extended CAN Frames —The filter applies to the upper eight bits from bit 28 to bit 21.
    - Standard CAN Frames —The filter applies to the upper eight bits from bit 10 to bit 3.
2. In the CAN Set Filter Value VI, right-click **filter index** and select **Create»Constant** or **Create»Control** from the shortcut menu. Set the filter number that you want to configure. 
 

NI-Embedded CAN for RIO supports different numbers of filters in different modes. The following table shows the maximum filter number for each mode. In the Disabled mode, you cannot create a filter, so the software stores all the incoming CAN frames. If the hardware supports multiple filters, the software stores the incoming CAN frames when the frames meet the acceptance conditions of any filter.

 
 Hardware Type Disabled 32-bit 16-bit 8-bit
Single-Board RIO N/A 2 4 8
CompactRIO with Built-In CAN Port N/A 4 N/A N/A

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_set_fvalue.html language=enus -->
## TOPIC 00009: CAN Set Filter Value VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_set_fvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_set_fvalue.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Set Filter Value VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Sets the filter setting for a CAN Interface Object. Use this VI and the [CAN Set Filter Mode](em_set_fmode.html) VI to [filter the incoming CAN frames](em_set_fmode.html).

[Details](#details)

[IMAGE alt='image' src='../cansetfiltervalue.gif']

|  | interface object in specifies the refnum of a CAN Interface Object. Use the CAN Create Interface VI to create this Interface Object. |
| --- | --- |
|  | filter index specifies the index of the filter. Different hardware supports different numbers of filters. The default is 0. |
|  | filter frame specifies the filter frame setting. identifier specifies the identifier that you want to use to compare with the identifier of the incoming CAN frame. identifier mask specifies the mask for identifier of this VI and the identifier of the incoming CAN frame. If identifier mask is 0xFFFFFFFF, identifier and the identifier of the incoming CAN frame are equal. If identifier mask is one, the NI-Embedded CAN for RIO software compares the corresponding bit for identifier of this VI with the identifier of the incoming CAN frame. The software stores this CAN frame when the bits are the same. Otherwise, the software discards the CAN frame. If identifier mask is zero, the software ignores the bit of the CAN frame. For example, 0x00000700 means that the software compares the upper three bits of an 11-bit standard ID. 1F000000 means to compare the upper five bits of the 29-bit extended ID. extended? specifies whether identifier uses extended format or standard format. If extended? is TRUE, identifier uses the extended format. If extended? is FALSE, identifier uses the standard format. RTR? specifies the RTR status that you want to use to compare with the RTR bit of the incoming CAN frame. RTR mask? specifies whether to compare RTR? of this VI with the RTR bit of the incoming CAN frame. If RTR mask? is TRUE, the NI-Embedded CAN for RIO software compares RTR? of this VI with the RTR bit of the incoming CAN frame. The software stores this CAN frame when the bits are the same. Otherwise, the software discards the CAN frame. If RTR mask? is FALSE, the software ignores the RTR bit of the CAN frame. |
|  | identifier specifies the identifier that you want to use to compare with the identifier of the incoming CAN frame. |
|  | identifier mask specifies the mask for identifier of this VI and the identifier of the incoming CAN frame. If identifier mask is 0xFFFFFFFF, identifier and the identifier of the incoming CAN frame are equal. If identifier mask is one, the NI-Embedded CAN for RIO software compares the corresponding bit for identifier of this VI with the identifier of the incoming CAN frame. The software stores this CAN frame when the bits are the same. Otherwise, the software discards the CAN frame. If identifier mask is zero, the software ignores the bit of the CAN frame. For example, 0x00000700 means that the software compares the upper three bits of an 11-bit standard ID. 1F000000 means to compare the upper five bits of the 29-bit extended ID. |
|  | extended? specifies whether identifier uses extended format or standard format. If extended? is TRUE, identifier uses the extended format. If extended? is FALSE, identifier uses the standard format. |
|  | RTR? specifies the RTR status that you want to use to compare with the RTR bit of the incoming CAN frame. |
|  | RTR mask? specifies whether to compare RTR? of this VI with the RTR bit of the incoming CAN frame. If RTR mask? is TRUE, the NI-Embedded CAN for RIO software compares RTR? of this VI with the RTR bit of the incoming CAN frame. The software stores this CAN frame when the bits are the same. Otherwise, the software discards the CAN frame. If RTR mask? is FALSE, the software ignores the RTR bit of the CAN frame. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of the CAN Interface Object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Set Filter Value Details

After [defining the filter mode](em_set_fmode.html), complete the following steps to configure the filter frame.

1. Right-click extended? and select Create»Constant or Create»Control from the shortcut menu. Select one of the following options to define the identifier.
  - TRUE —The filter only applies to the incoming CAN frames with an extended identifier. The NI-Embedded CAN for RIO software discards the incoming CAN frames with a standard identifier.
  - FALSE —The filter only applies to the incoming CAN frames with a standard identifier. The NI-Embedded CAN for RIO software discards the incoming CAN frames with an extended identifier.
2. Define the values of identifier and identifier mask in filter frame .
  1. Right-click identifier and select Create»Constant from the shortcut menu. Set a value to compare the value with the incoming CAN frame. 

 

For example, set the value to 0x123 (0001 0010 0011).
  2. Right-click identifier mask and select Create»Constant from the shortcut menu. Define the bits that you want to compare between identifier in filter frame and the identifier of the incoming CAN frame. 

 

For example, if you set the value of identifier mask to 0xFF8 (1111 1111 1000), this VI compares the zero-based bit 3–bit 11 between identifier and the identifier of the incoming CAN frame.

 

If the identifier of the incoming CAN frame is 0x124 (0001 0010 0100), the bit 3–bit 11 (0001 0010 0) of 0x123 and 0x124 are equal. The lower three bits of 0x123 and 0x124 are not equal, but you can set identifier mask to ignore these bits.
3. Set the status of RTR? and RTR mask? in filter frame .
  1. Right-click RTR? and select Create»Constant or Create»Control from the shortcut menu to compare the status with the RTR bit of the incoming CAN frame.
  2. Right-click RTR mask? and select Create»Constant or Create»Control from the shortcut menu. Set the status to define whether you want to compare RTR? with the RTR bit of the incoming CAN frame.
4. Run this VI. If the comparison results of both the identifier and the RTR are equal, the NI-Embedded CAN for RIO software stores the CAN frame. The software discards the CAN frame when the mask results are not equal.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_start.html language=enus -->
## TOPIC 00010: CAN Start VI

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_start.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/em_start.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

CAN Start VI

**Owning Palette:** [Embedded CAN for RIO VIs](embcan_rio.html)

Starts communication for the specified CAN interface. This VI is optional when the [Auto Start?](propertyautostart.html) property is TRUE.

After using this VI, the interface starts to receive CAN frames from the bus and stores them in the receive queue.

[Details](#details)

[IMAGE alt='image' src='../canstartvi.gif']

|  | interface object in specifies the refnum of the interface to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### CAN Start Details

You cannot set some interface properties in communication mode. Stop communication using the [CAN Stop](em_can_stop.html) VI before setting the interface properties.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/embcan_rio.html language=enus -->
## TOPIC 00011: Embedded CAN for RIO VIs

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/embcan_rio.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/embcan_rio.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Embedded CAN for RIO VIs

Use the Embedded CAN for RIO VIs to interact with the CAN embedded devices.

| Palette Object | Description |
| --- | --- |
| CAN Close Interface | Closes a session you create by using the CAN Create Interface VI. This VI closes the session regardless of whether an error has occurred in a preceding operation or not. Use this VI to release memory before starting a new session or to discard all elements in the transmit queue or the receive queue. |
| CAN Create Interface | Creates a CAN interface object to read or write data on the bus. You must create a CAN interface before using all other Embedded CAN for RIO VIs. |
| CAN Flush | Flushes all queues for the specified CAN interface. Use this VI to discard all elements in the transmit queue or receive queue. |
| CAN Read | Reads a CAN frame on the bus. |
| CAN Set Filter Mode | Sets the mode of the filter. Use this VI and the CAN Set Filter Value VI to create Acceptance Filters. Acceptance Filters sort the incoming CAN frames for the CompactRIO with the built-in CAN port hardware and the single-board RIO hardware. Use this filter to reduce the burden of frame storage in the NI-Embedded CAN for RIO software. |
| CAN Set Filter Value | Sets the filter setting for a CAN Interface Object. Use this VI and the CAN Set Filter Mode VI to filter the incoming CAN frames. |
| CAN Start | Starts communication for the specified CAN interface. This VI is optional when the Auto Start? property is TRUE. |
| CAN Stop | Stops communication for the specified CAN interface. |
| CAN Wait | Waits for CAN frames or interfaces. You must manually select the polymorphic instance to use. |
| CAN Write | Transmits a CAN frame to the bus. |

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyautostart.html language=enus -->
## TOPIC 00012: Auto Start?

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyautostart.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyautostart.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Auto Start?

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read/Write | No | True |

#### Property Class

Embedded CAN Interface

#### Short Name

Auto Start?

#### Description

If the value is TRUE, the property automatically starts the interface when you run the [CAN Read](em_can_read.html) VI or the [CAN Write](em_can_write.html) VI for the first time.

The automatic start-up is equivalent to using the [CAN Start](em_start.html) VI.

The execution time to read or write this property is sufficient for use in a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertybaudrate.html language=enus -->
## TOPIC 00013: Baud Rate

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertybaudrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertybaudrate.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Baud Rate

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read/Write | No | 125000 |

#### Property Class

Embedded CAN Interface

#### Short Name

Baud Rate

#### Description

|  | Note You can modify this property only when the interface stops. |
| --- | --- |

Specifies the CAN interface baud rate.

**Supported Standard Baud Rates:** 10000, 12500, 15625, 16000, 25000, 31250, 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, and 1000000. (The transceiver may support only a subset of these values.)

When the upper bit is set, the remaining bits provide fields for more advanced CAN communication baud rate programming. The baud rate format in advanced mode is *0x8ABCDDDD*, where *A*, *B*, *C*, and *DDDD* are defined as follows:

- A is the (Re-)Synchronization Jump Width (SJW).
  - Valid programmed values are 0–3.
  - The actual hardware interpretation of this value is one more than the programmed value.
- B is the Time Segment 2 (TSEG2), which is the time segment after the sample point.
  - Valid programmed values are 0–7.
  - This value is the Phase_Seg2 time from ISO 11898–1, 12.4.1 Bit Encoding/Decoding .
  - The actual hardware interpretation of this value is one more than the programmed value.
- C is the Time Segment 1 (TSEG1), which is the time segment before the sample point.
  - Valid programmed values are 1–0xF (1–15 decimal).
  - This value is the combination of the Prop_Seg and Phase_Seg1 time from ISO 11898–1, 12.4.1 Bit Encoding/Decoding .
  - The actual hardware interpretation of this value is one more than the programmed value.
- DDDD is the bit time quantum. Use this value to program the baud rate prescaler.
  - 
    - Single-Board RIO Hardware —Valid programmed values are 0x53–x14C0, in increments of 0x53 (83 decimal) ns.
    - CompactRIO with the Built-In CAN Port Hardware —Valid programmed values for the are 0x7D–0x7D00, in increments of 0x7D (125 decimal) ns.
  - This value is the time quantum from ISO 11898–1, 12.4.1 Bit Encoding/Decoding .

The following examples show how to break down an advanced baud rate into *A*, *B*, *C*, and *D* values for different hardware.

- Single-Board RIO Hardware —If the baud rate is 0x82270053 , you break down the rate into the following values:
 
Each time quanta is 83 ns. From IS0 11898–1, 12.4.1.2 Programming of Bit Time , the nominal time segments length is Sync_Seg(Fixed at 1) + (Prop_Seg + Phase_Seg1)(B) + Phase_Seg2(C) = 1 + 3 + 8 = 12. So, the total time for a bit in this example is 12 * 83 ns = 996 ns ≈ 1 µs. A 1 µs bit time is equivalent to a 1 MHz baud rate.
 
The real time quantum increment in hardware is 83 1/3. So, if the tq is set to be 83 * 3, the real time quantum used in the hardware is (83 1/3) * 3 = 250.
  - A = SJW = 0x2 (0x03 in hardware, due to the + 1)
  - B = TSEG2 = 0x2 (0x03 in hardware, due to the + 1)
  - C = TSEG1 = 0x7 (0x08 in hardware, due to the + 1)
  - D = tq = 0x53 (83 ns in hardware)
- CompactRIO with the Built-In CAN Port Hardware —If the baud rate is 0x811C01F4 , you break down the rate into the following values.


 
Each time quanta is 500 ns. From IS0 11898–1, 12.4.1.2 Programming of Bit Time , the nominal time segments length is Sync_Seg(Fixed at 1) + (Prop_Seg + Phase_Seg1)(B) + Phase_Seg2(C) = 1 + 2 + 13 = 16. So, the total time for a bit in this example is 16 * 500 ns = 8000 ns. The speed is equivalent to a 125 KHz baud rate.
 
The execution time to read or write this property is sufficient for use in a high-priority loop in the LabVIEW Real-Time (RT) Module.
  - A = SJW = 0x1 (0x02 in hardware, due to the + 1)
  - B = TSEG2 = 0x1 (0x02 in hardware, due to the + 1)
  - C = TSEG1 = 0xC (0x0D in hardware, due to the + 1)
  - D = tq = 0x1F4 (500 ns in hardware)

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertycommunicationstate.html language=enus -->
## TOPIC 00014: Communication State

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertycommunicationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertycommunicationstate.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Communication State

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read | No | Init (3) |

#### Property Class

Embedded CAN Interface

#### Short Name

Communication State

#### Description

Specifies the CAN interface state with respect to error confinement (decimal value in parentheses). The following table lists the accepted values.

| Enumeration | Value | Description |
| --- | --- | --- |
| Error Active | 0 | This state reflects normal communication, with few errors detected. The CAN interface remains in this state as long as Receive Error Counter and Transmit Error Counter are both below 128. |
| Error Passive | 1 | If either Receive Error Counter or Transmit Error Counter increment above 127, the CAN interface transitions into this state. Although communication proceeds, the CAN device generally is assumed to have problems with receiving frames.When a CAN interface is in error passive state, acknowledgement errors do not increment Transmit Error Counter. Therefore, if the CAN interface transmits a frame with no other device connected, it eventually enters error passive state due to retransmissions, but does not enter bus off state. |
| Bus Off | 2 | If Transmit Error Counter increments above 255, the CAN interface transitions into this state. Communication immediately stops under the assumption that the CAN interface must be isolated from other devices.When a CAN interface transitions to the bus off state, communication stops for the interface. The interface no longer receives or transmits frame values. |
| Init | 3 | This is the CAN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs).When the start trigger occurs for the CAN interface, it transitions from the Init state to the Error Active state. When the interface stops due to a call to the CAN Stop VI, the CAN interface transitions from either Error Active or Error Passive to the Init state. When the interface stops due to the Bus Off state, it remains in that state until you restart. |

The execution time to read this property is sufficient for use in a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertylistenonly.html language=enus -->
## TOPIC 00015: Listen Only?

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertylistenonly.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertylistenonly.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Listen Only?

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read/Write | No | False |

#### Property Class

Embedded CAN Interface

#### Short Name

Listen Only?

#### Description

|  | Note You can modify this property only when the interface is stopped. |
| --- | --- |

The Listen Only? property configures whether the CAN interface transmits any information to the CAN bus.

When this property is FALSE, the interface can transmit CAN frames and acknowledge received CAN frames.

When this property is TRUE, the interface can neither transmit CAN frames nor acknowledge a received CAN frame. The TRUE value enables passive monitoring of network traffic, which is useful for debugging scenarios when you do not want to interfere with a communicating network.

The execution time to read or write this property is sufficient for a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

If you use CompactRIO with the built-in CAN port hardware as the Embedded CAN interface and the interface is the only listener on the CAN bus, the Embedded CAN interface cannot receive any CAN frame on the CAN bus. Because the interface itself does not acknowledge the CAN frame transmitter, the interface gets bit errors. If you have another CAN device that can acknowledge the CAN frame transmitter, the Embedded CAN interface receives the CAN frames without bit errors.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyreceiveerrorcounter.html language=enus -->
## TOPIC 00016: Receive Error Counter

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyreceiveerrorcounter.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyreceiveerrorcounter.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Receive Error Counter

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read | No | 0 |

#### Property Class

Embedded CAN Interface

#### Short Name

Receive Error Counter

#### Description

|  | Note You can read this property only when the interface is stopped or the transceiver state is Sleep. |
| --- | --- |

The Receive Error Counter is incremented when errors are detected for received frames, and decremented when a frame is received successfully.

The execution time to read this property is sufficient for use in a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyreceivequeuesize.html language=enus -->
## TOPIC 00017: Receive Queue Size

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyreceivequeuesize.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertyreceivequeuesize.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Receive Queue Size

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read | No | 5 |

#### Property Class

Embedded CAN Interface

#### Short Name

Receive Queue Size

#### Description

|  | Note Receive Queue Size must be 5 or above. |
| --- | --- |

Specifies the number of frames that can be stored in the receive queue.

The receive queue stores data received from the network and not yet obtained using the [CAN Read](em_can_read.html) VI.

If Receive Queue Size is greater than 5, the receive interrupt is enabled and a receive queue is allocated in RAM. When a frame is received, it is pushed into the receive queue. The timestamp when it was moved also is stored and is returned when you use the [CAN Read](em_can_read.html) VI. If Receive Queue Size is 5, the receive interrupt is disabled, and a hardware receive queue is used. A frame is retrieved from the hardware receive queue each time you use the [CAN Read](em_can_read.html) VI.

The execution time to read this property is sufficient for use in a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertytransceiverstate.html language=enus -->
## TOPIC 00018: Transceiver State

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertytransceiverstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertytransceiverstate.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Transceiver State

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read/Write | No | Sleep (1) |

#### Property Class

Embedded CAN Interface

#### Short Name

Transceiver State

#### Description

|  | Note You can modify this property only when the interface is started. |
| --- | --- |

Configures the CAN transceiver and CAN controller modes. The transceiver state controls whether the transceiver is asleep or communicating. The following table lists the accepted values.

| Enumeration | Value |
| --- | --- |
| Normal | 0 |
| Sleep | 1 |

##### Normal

This state sets the transceiver to normal communication mode. If the transceiver is in the Sleep mode, this state performs a local wakeup of the transceiver and CAN controller chip.

##### Sleep

This state sets the transceiver and CAN controller chip to Sleep (or standby) mode.

Before going to sleep, all pending transmissions are discarded. An explicit call to the [CAN Wait (Transmit Complete)](em_can_wait.html) VI is necessary to make sure the pending transmissions are transmitted. Once the interface enters Sleep mode, further communication is not possible until a wakeup occurs. The transceiver and CAN controller wake from Sleep mode when either a local wakeup or remote wakeup occurs.

A local wakeup occurs when the application sets the transceiver state to Normal.

A remote wakeup occurs when a remote node transmits a CAN frame (referred to as the wakeup frame). The wakeup frame wakes up the Embedded CAN interface transceiver and CAN controller chip. The CAN controller chip does not receive or acknowledge the wakeup frame. After detecting the wakeup frame and idle bus, the CAN interface enters Normal mode.

When the local or remote wakeup occurs, frame transmissions resume from the point at which the original Sleep mode was set.

To suspend the application while waiting for the remote wakeup, use the [CAN Wait (Remote Wakeup)](em_can_wait.html) VI.

The execution time to read this property is sufficient for use in a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertytransmiterrorcounter.html language=enus -->
## TOPIC 00019: Transmit Error Counter

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertytransmiterrorcounter.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/propertytransmiterrorcounter.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Transmit Error Counter

| Data Type | Direction | Required? | Default |
| --- | --- | --- | --- |
|  | Read | No | 0 |

#### Property Class

Embedded CAN Interface

#### Short Name

Transmit Error Counter

#### Description

|  | Note For single-board RIO hardware, you can read this property only when the interface is stopped or the transceiver state is Sleep. |
| --- | --- |

The transmit error counter is incremented when errors are detected for transmitted frames, and decremented when a frame is transmitted successfully.

The execution time to read this property is sufficient for use in a [high-priority loop](ni.com/docs/csh?context=ni-embedded-can-for-rio_lvrioembeddedcanhelp_usinglabviewrealtime) in the LabVIEW Real-Time (RT) Module.

<!--NI_TOPIC bundle=ni-embedded-can-for-rio-api-ref path=ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/rioembeddedcaninterfacepropertynode.html language=enus -->
## TOPIC 00020: Embedded CAN Interface Property Node

- bundle_id: `ni-embedded-can-for-rio-api-ref`
- source_path: `ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/rioembeddedcaninterfacepropertynode.html`
- source_url: https://docs-be.ni.com/bundle/ni-embedded-can-for-rio-api-ref/raw/resource/enus/ni-embedded-can-for-rio-api-ref/lvrioembeddedcanhelp/rioembeddedcaninterfacepropertynode.html
- document_id: `ni-embedded-can-for-rio-api-ref`
- page_type: `leaf`
- content_type: ``

Embedded CAN Interface Property Node

The NI-Embedded CAN for RIO software provides the following properties.

| Property | Purpose |
| --- | --- |
| Auto Start? | If the value is TRUE, the property automatically starts the interface when you run the CAN Read VI or the CAN Write VI for the first time. |
| Baud Rate | Specifies the CAN interface baud rate. |
| Communication State | Specifies the CAN interface state with respect to error confinement (decimal value in parentheses). |
| Listen Only? | Configures whether the CAN interface transmits any information to the CAN bus. |
| Receive Error Counter | The receive error counter is incremented when errors are detected for received frames, and decremented when a frame is received successfully. |
| Receive Queue Size | Specifies the number of frames that can be stored in the receive queue. |
| Transceiver State | Configures the CAN transceiver and CAN controller modes. |
| Transmit Error Counter | The transmit error counter is incremented when errors are detected for transmitted frames, and decremented when a frame is transmitted successfully. |
