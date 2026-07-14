# NI DOCUMENT BUNDLE: ni-industrial-communications-canopen-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-industrial-communications-canopen-api-ref start=1 end=37 -->
<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=advanced-vis.html language=enus -->
## TOPIC 00001: Advanced VIs

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `advanced-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/advanced-vis.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Use Advanced VIs to interact with CANopen objects, frames, and data arrays. Palette ObjectDescriptionCANopen Baudrate ChangeChanges the baud rate of a CANopen device. This VI is not optimized for real-time performance. CANopen CAN Frame ReadReads a CAN frame on a CANopen

### Advanced VIs

**Owning Palette:** CANopen VIs

Use Advanced VIs to interact with CANopen objects, frames, and data arrays.

| Palette Object | Description |
| --- | --- |
| CANopen Baudrate Change | Changes the baud rate of a CANopen device. This VI is not optimized for real-time performance. |
| CANopen CAN Frame Read | Reads a CAN frame on a CANopen interface. You can specify the interface when you create the CAN frame read object. Use this VI to implement advanced CAN applications. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen CAN Frame Write | Sends a CAN frame on a CANopen interface. Use this VI to implement advanced CAN applications. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen Close | Closes an interface or a CANopen object that you created by using the CANopen Create VI. This VI closes the object reference regardless of whether an error occurred in a preceding operation. LabVIEW closes all objects when the application terminates, so using this VI is optional. However, you can use this VI in advanced use cases, such as freeing memory prior to starting a new session. You must manually select the polymorphic instance to use. This VI is not optimized for real-time performance. |
| CANopen Convert to Data | Converts LabVIEW-compatible data to a CANopen data array. Wire data to the data type input to determine the polymorphic instance to use or manually select the instance. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen Emergency Convert | Converts a specified emergency (EMCY) message to an error description and a cluster containing the bit states of the error register. This VI is not optimized for real-time performance. |
| CANopen Fetch from Data | Converts a specified CANopen data array to LabVIEW-compatible data. You must manually select the polymorphic instance to use. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen Node-ID Change | Changes the node-ID of a specified device and resets the device to activate the new node-ID. This VI is not optimized for real-time performance. |
| CANopen SDO Completion Code to String | Converts an SDO completion code to a description string. Use this VI to convert completion codes that the CANopen SDO Read VI, the CANopen SDO Write VI, or the CANopen SDO Batch Write VI returns. This VI is not optimized for real-time performance. |
| CANopen Start | Starts a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a node guarding object, a synchronization (SYNC) object, an emergency (EMCY) object, or a CAN frame read object. LabVIEW automatically starts an object when the application reads or writes the object for the first time. Use this VI when you want to start and stop objects manually. You must manually select the polymorphic instance to use. This VI is not optimized for real-time performance. |
| CANopen Stop | Stops a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a node guarding object, a synchronization (SYNC) object, an emergency (EMCY) object, or a CAN frame read object. LabVIEW stops all objects when you close an application. Use this VI when you want to start and stop objects manually. You must manually select the polymorphic instance to use. This VI is not optimized for real-time performance. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=batch-sdo-batch-sdo-preview-page.html language=enus -->
## TOPIC 00002: Batch SDO - Batch SDO Preview Page

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `batch-sdo-batch-sdo-preview-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/batch-sdo-batch-sdo-preview-page.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Batch SDO dialog box, select Batch SDO - Batch SDO Preview from the Category list to display this page. Use this page to preview batch SDOs. This dialog box includes the following component: Generate Batch SDO Preview—Generates a table to preview the current state of the batch SDO.

### Batch SDO - Batch SDO Preview Page

In the Batch SDO dialog box, select **Batch SDO - Batch SDO Preview** from the **Category** list to display this page.

Use this page to preview batch SDOs.

This dialog box includes the following component:

- Generate Batch SDO Preview —Generates a table to preview the current state of the batch SDO.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=batch-sdo-dialog-box.html language=enus -->
## TOPIC 00003: Batch SDO Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `batch-sdo-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/batch-sdo-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click a batch SDO and select Edit from the shortcut menu to display this dialog box. You also can display this dialog box by creating a batch SDO. This dialog box has the following pages: Object Dictionary Batch SDO Preview Online Validation

### Batch SDO Dialog Box

In the **Project Explorer** window, right-click a batch SDO and select **Edit** from the shortcut menu to display this dialog box. You also can display this dialog box by [creating a batch SDO](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_bsdo_oddb).

This dialog box has the following pages:

- Object Dictionary
- Batch SDO Preview
- Online Validation

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=batch-sdo-general-settings-dialog-box.html language=enus -->
## TOPIC 00004: Batch SDO General Settings Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `batch-sdo-general-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/batch-sdo-general-settings-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click a target and select New»CANopen Batch SDO from the shortcut menu to display this dialog box. Use this dialog box to specify general settings of a new batch service data object (SDO). This dialog box includes the following components: Name—Enters a name for

### Batch SDO General Settings Dialog Box

In the **Project Explorer** window, right-click a target and select **New»CANopen Batch SDO** from the shortcut menu to display this dialog box.

Use this dialog box to specify general settings of a new batch [service data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sdo) (SDO).

This dialog box includes the following components:

- Name —Enters a name for the new batch SDO. The name must be a string of numbers and letters without any spaces. You can use underscores in the batch SDO name.
- EDS File —Specifies the location of an electronic data sheet (EDS) file for the batch SDO. This EDS file is optional for a batch SDO.
- Location —Displays the location of the EDS file.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=batch-sdo-object-dictionary-page.html language=enus -->
## TOPIC 00005: Batch SDO - Object Dictionary Page

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `batch-sdo-object-dictionary-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/batch-sdo-object-dictionary-page.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Batch SDO dialog box, select Batch SDO - Object Dictionary from the Category list to display this page. Use this page to add objects to, or remove objects from a batch SDO. You can also edit existing batch SDO objects in this dialog box. This page includes the following components: Object Lis

### Batch SDO - Object Dictionary Page

In the Batch SDO dialog box, select **Batch SDO - Object Dictionary** from the **Category** list to display this page.

Use this page to add objects to, or remove objects from a batch SDO. You can also edit existing batch SDO objects in this dialog box.

This page includes the following components:

- Object List —Lists all objects of the object dictionary . You can select an object from this list and add this object to the batch SDO by double-clicking this object or using the Add to Batch button.
- Add to Batch —Launches the Add/Edit Object dialog box to add selected objects to the batch SDO. You can configure the properties of the selected object in the Add/Edit Object dialog box.
- Batch SDO —Lists current objects in the batch SDO. Use the buttons beside the list to configure objects in the batch SDO.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=batch-sdo-online-validation-page.html language=enus -->
## TOPIC 00006: Batch SDO - Online Validation Page

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `batch-sdo-online-validation-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/batch-sdo-online-validation-page.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Batch SDO dialog box, select Batch SDO - Online Validation from the Category list to display this page. Use this page to validate batch SDOs online. This page includes the following components: Interface Name/Location—Selects the CANopen interface of the batch SDO that you want to validate. I

### Batch SDO - Online Validation Page

In the Batch SDO dialog box, select **Batch SDO - Online Validation** from the **Category** list to display this page.

Use this page to validate batch SDOs online.

This page includes the following components:

- Interface Name/Location —Selects the CANopen interface of the batch SDO that you want to validate.
- Interface Baud Rate —Specifies the baud rate of the CANopen interface.
- Device Node-ID —Specifies the device node-ID of the batch SDO that you want to validate.
- Timeout —Specifies the timeout, in milliseconds, of the validation.
- Send Batch SDO —Sends out a set of SDOs. These SDOs belong to the current batch SDO that you want to validate.
- Status —Returns the validation result of the set of SDOs that you send. These SDOs belong to the current batch SDO.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-baudrate-change-vi.html language=enus -->
## TOPIC 00007: CANopen Baudrate Change VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-baudrate-change-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-baudrate-change-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Changes the baud rate of a CANopen device. This VI is not optimized for real-time performance. Details revision number specifies the revision information of a CANopen device. Each revision of a CANopen device has a unique revision number. The default is 0. vendor ID spec

### CANopen Baudrate Change VI

**Owning Palette:** Advanced VIs

Changes the baud rate of a CANopen device.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

Details

[IMAGE alt='image' src='images/canopen_baudrate_change.gif']

|  | revision number specifies the revision information of a CANopen device. Each revision of a CANopen device has a unique revision number. The default is 0. |
| --- | --- |
|  | vendor ID specifies the vendor information for the CANopen device. Each CANopen device vendor has a unique vendor ID. The default is 0. |
|  | interface name specifies the name of a device interface. The interface corresponds to a CAN port on a CANopen board. You can use Measurement & Automation Explorer to view the mapping relationship between each interface name and each specific piece of hardware. |
|  | current baud rate specifies the current baud rate of the device. |
|  | new baud rate specifies a new baud rate of the device. |
|  | switch delay specifies a delay period in milliseconds. The device waits a delay period before switching current baud rate to new baud rate. The delay period ensures the device receives all messages from the CANopen master before changing the baud rate. The default is 2000. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | product code specifies the product type of the device. Each type of CANopen device has a unique product code. The default is 0. |
|  | serial number specifies the serial number of the device. Each CANopen device has a unique serial number. The default is 0. |
|  | error code returns the CANopen-specific error code of the device. This error code indicates a general error type of the device. |
|  | specific error returns specific error information of the CANopen device. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Baudrate Change Details

If the target device is the only device on the CANopen bus, you can set **revision number**, **vendor ID**, **product code**, and **serial number** to the default value 0. If the CANopen bus has multiple devices, you must specify these parameters of the target device.

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-can-frame-read-vi.html language=enus -->
## TOPIC 00008: CANopen CAN Frame Read VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-can-frame-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-can-frame-read-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Reads a CAN frame on a CANopen interface. You can specify the interface when you create the CAN frame read object. Use this VI to implement advanced CAN applications. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shar

### CANopen CAN Frame Read VI

**Owning Palette:** Advanced VIs

Reads a CAN frame on a CANopen interface. You can specify the interface when you create the CAN frame read object. Use this VI to implement advanced CAN applications.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/canopen_readfanfrm_read.gif']

|  | timeout specifies the time, in seconds, that this VI waits for a new CAN frame in the buffer of the CAN frame read object. The buffer is a first-in-first-out (FIFO) buffer. The default is 0. You can enter decimal values such as 0.05. If timeout is 0, this VI returns a warning if the object has not received any frames since the object instance is started. If timeout is greater than 0, this VI returns an error if the object has not received any frames since the object instance is started. |
| --- | --- |
|  | CAN frame read object in specifies the reference number of the CAN frame read object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RTR? indicates whether this CAN frame is a remote transmission request. |
|  | CAN frame read object out returns the reference number of CAN frame read object in. |
|  | CAN message data returns the data of the CAN frame that this VI reads from the CAN frame read object. If the buffer of the CAN frame read object receives a new frame within timeout, CAN message data returns the data of the new frame. If the buffer receives no frames within timeout, CAN message data returns different values in the following cases: If the buffer size is greater than 0 and the FIFO buffer contains frames, CAN message data returns the data of the next new frame in the FIFO buffer. If the buffer size is greater than 0 and all data in the FIFO buffer has been read, CAN message data returns the data of the latest frame and new data? returns FALSE. If the buffer size is 0, CAN message data returns the data of the latest data from object. |
|  | COB-ID returns the COB-ID of the CAN frame that the VI reads. |
|  | new data? indicates whether the CAN frame is an unread CAN frame. If new data? is TRUE, no device or VI reads this CAN frame before this VI does. |
|  | timestamp returns the device firmware time when the CAN frame arrives at the object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-can-frame-write-vi.html language=enus -->
## TOPIC 00009: CANopen CAN Frame Write VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-can-frame-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-can-frame-write-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Sends a CAN frame on a CANopen interface. Use this VI to implement advanced CAN applications. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. interface object in specifies the re

### CANopen CAN Frame Write VI

**Owning Palette:** Advanced VIs

Sends a CAN frame on a CANopen interface. Use this VI to implement advanced CAN applications.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/canopen_send_can_frame.gif']

|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
| --- | --- |
|  | CAN message data specifies the data of the CAN frame. |
|  | RTR? specifies whether this frame is a remote transmission request (RTR). The default is FALSE. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | COB-ID specifies the COB-ID of the CAN frame that you want to send. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-close-vi.html language=enus -->
## TOPIC 00010: CANopen Close VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-close-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Closes an interface or a CANopen object that you created by using the CANopen Create VI. This VI closes the object reference regardless of whether an error occurred in a preceding operation. LabVIEW closes all objects when the application terminates, so using this VI is

### CANopen Close VI

**Owning Palette:** Advanced VIs

Closes an interface or a CANopen object that you created by using the CANopen Create VI. This VI closes the object reference regardless of whether an error occurred in a preceding operation.

LabVIEW closes all objects when the application terminates, so using this VI is optional. However, you can use this VI in advanced use cases, such as freeing memory prior to starting a new session. You must manually select the polymorphic instance to use.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

CANopen Interface Close

[IMAGE alt='image' src='images/CANopen_Close.gif']

|  | interface object in specifies the reference number of the CANopen interface that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Close

[IMAGE alt='image' src='images/CANopen_SDO_Close.gif']

|  | SDO object in specifies the reference number of the SDO object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen RPDO Close

[IMAGE alt='image' src='images/CANopen_RPDO_Close.gif']

|  | RPDO object in specifies the reference number of the RPDO object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen TPDO Close

[IMAGE alt='image' src='images/CANopen_TPDO_Close.gif']

|  | TPDO object in specifies the reference number of the TPDO object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Heartbeat Close

[IMAGE alt='image' src='images/CANopen_Heartbeat_Close.gif']

|  | heartbeat object in specifies the reference number of the heartbeat object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Node Guarding Close

[IMAGE alt='image' src='images/CANopen_Node_Guard_Close.gif']

|  | node guarding object in specifies the reference number of the node guarding object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Emergency Close

[IMAGE alt='image' src='images/CANopen_Emergency_Close.gif']

|  | emergency object in specifies the reference number of the EMCY object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SYNC Close

[IMAGE alt='image' src='images/CANopen_SYNC_Close.gif']

|  | SYNC object in specifies the reference number of the SYNC object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen CAN Frame Read Close

[IMAGE alt='image' src='images/CANopen_ReadCanFrm_Close.gif']

|  | CAN frame read object in specifies the reference number of the CAN frame read object that you want to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-convert-to-data-vi.html language=enus -->
## TOPIC 00011: CANopen Convert to Data VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-convert-to-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-convert-to-data-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Converts LabVIEW-compatible data to a CANopen data array. Wire data to the data type input to determine the polymorphic instance to use or manually select the instance. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to sh

### CANopen Convert to Data VI

**Owning Palette:** Advanced VIs

Converts LabVIEW-compatible data to a CANopen data array. Wire data to the data type input to determine the polymorphic instance to use or manually select the instance.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

Details

CANopen Convert to Data [I8]

[IMAGE alt='image' src='images/canopen_convert_to_data_I8.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts signed 8-bit integer to one element and uses the converted element to replace an element of this array. |
|  | signed 8-bit integer specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with one element. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [I16]

[IMAGE alt='image' src='images/canopen_convert_to_data_i16.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts signed 16-bit integer to two elements and uses the converted elements to replace two elements of this array. |
|  | signed 16-bit integer specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with two elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [I32]

[IMAGE alt='image' src='images/canopen_convert_to_data_i32.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts signed 32-bit integer to four element and uses the converted elements to replace four elements of this array. |
|  | signed 32-bit integer specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with four elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [U8]

[IMAGE alt='image' src='images/canopen_convert_to_data_u8.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts unsigned 8-bit integer to one element and uses the converted element to replace an element of this array. |
|  | unsigned 8-bit integer specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with one element. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [U16]

[IMAGE alt='image' src='images/canopen_convert_to_data_u16.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts signed 16-bit integer to two elements and uses the converted elements to replace two elements of this array. |
|  | unsigned 16-bit integer specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with two elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [U32]

[IMAGE alt='image' src='images/canopen_convert_to_data_u32.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts unsigned 32-bit integer to four element and uses the converted elements to replace four elements of this array. |
|  | unsigned 32-bit integer specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with four elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [SGL]

[IMAGE alt='image' src='images/canopen_convert_to_data_sgl.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts 4-byte single to four elements and uses the converted elements to replace four elements of this array. |
|  | 4-byte single specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with four elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [DBL]

[IMAGE alt='image' src='images/canopen_convert_to_data_dbl.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts 8-byte double to eight elements and uses the converted elements to replace eight elements of this array. |
|  | 8-byte double specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array with eight elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data [STR]

[IMAGE alt='image' src='images/canopen_convert_to_data_str.gif']

|  | trim specifies whether this VI removes the empty elements from the end of the CANopen data array. Set trim to TRUE when you need to change the size of the output data array. Assume offset is x and the converted LabVIEW data contains y elements. If trim is TRUE, this VI removes all elements after the element x+y-1. The resulting CANopen data array contains only x+y elements. |
| --- | --- |
|  | CANopen data in specifies a CANopen data array. This VI converts signed 8-bit integer to one element and uses the converted element to replace an element of this array. |
|  | string specifies the LabVIEW data that you want to convert. This VI converts the LabVIEW data into an array. The length of string determines the number of the array elements. |
|  | offset specifies the index of an element of CANopen data in. This VI replaces this element and the following elements with the converted array. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the CANopen data array that contains an element of the converted LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Convert to Data Details

LabVIEW uses the big-endian format, which places the most significant byte first. CANopen uses the little-endian format, which places the least significant byte first. You can pass the resulting array to the CANopen PDO Write VI or the CANopen SDO Write VI.

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-create-vi.html language=enus -->
## TOPIC 00012: CANopen Create VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-create-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-create-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Creates an interface, a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a node guarding object, a synchronization (SYNC) object, an emergency (EMCY) object, or a CAN frame read object. You must manually select the polymorphic

### CANopen Create VI

**Owning Palette:** CANopen VIs

Creates an interface, a transmit-[process data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_pdo) (TPDO), a receive-process data object (RPDO), a [heartbeat](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, a [node guarding](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, a [synchronization](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sync_object) (SYNC) object, an [emergency](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_emergencies_emcy) (EMCY) object, or a CAN frame read object. You must manually select the polymorphic instance to use.

When you create objects on a CANopen network, ensure each object that receives data, such as RPDOs, SDOs, heartbeat objects, node guarding objects, and emergency object, has a unique COB-ID. Otherwise, this VI returns an error.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

CANopen Interface Create

[IMAGE alt='image' src='images/CANopen_Create.gif']

|  | interface name specifies the name of an interface that you want to create. The name of an interface must be CANopenXX, where XX is the interface number. The maximum interface number is 32. You can use Measurement & Automation Explorer to view the mapping relationship between each interface name and each specific piece of hardware. |
| --- | --- |
|  | baud rate specifies the baud rate of the CANopen interface. |
|  | termination? indicates whether to use the onboard termination of the NI-CANopen interface. The termination is a 120 Î© resistor. In a typical High-Speed CAN network, the termination of the network is on the BUS. However, you can use the onboard termination to simplify testing. Set termination? to True to use the onboard termination. The default is False. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the interface that you created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen TPDO Create

[IMAGE alt='image' src='images/CANopen_TPDO_Create.gif']

|  | node-ID specifies the node-ID of a device for which you want to create a PDO. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | PDO channel specifies a channel of the PDO. This VI uses PDO Channel and COB-ID to calculate the effective COB-ID. |
|  | COB-ID specifies the COB-ID of the PDO. The default is 0. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. If COB-ID is 0, this VI calculates the effective COB-ID by adding node-ID and the base COB-ID of PDO Channel. Otherwise, this VI ignores node-ID and PDO Channel and uses COB-ID as the effective COB-ID. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | buffer size specifies the maximum number of CAN frames that the TPDO receive buffer saves. The buffer is a first-in-first-out buffer. The default is 0. If buffer size is 0, the receive buffer contains only the latest received CAN frame. If buffer size is greater than 0, the TPDO keeps CAN frames in a queue when the TPDO receives CAN frames. If the TPDO receives more CAN frames than buffer size, the TPDO returns an overflow warning. |
|  | interface object out returns the refnum of interface object in. |
|  | TPDO object out returns the reference number of the TPDO object that you created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen RPDO Create

[IMAGE alt='image' src='images/CANopen_RPDO_Create.gif']

|  | node-ID specifies the node-ID of a device for which you want to create a PDO. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | PDO channel specifies a channel of the PDO. This VI uses PDO Channel and COB-ID to calculate the effective COB-ID. |
|  | COB-ID specifies the COB-ID of the PDO. The default is 0. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. If COB-ID is 0, this VI calculates the effective COB-ID by adding node-ID and the base COB-ID of PDO Channel. Otherwise, this VI ignores node-ID and PDO Channel and uses COB-ID as the effective COB-ID. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | RPDO object out returns the reference number of the RPDO object that you created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Create

[IMAGE alt='image' src='images/CANopen_SDO_Create.gif']

|  | node-ID specifies the node-ID of a device for which you want to create an SDO. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | client COB-ID specifies the COB-ID of the SDO client. The default is 0. If client COB-ID is 0, this VI calculates the effective client COB-ID by adding node-ID to a constant. The CANopen protocol defines the value of this constant. Otherwise, this VI ignores node-ID and uses client COB-ID as the effective client COB-ID. |
|  | server COB-ID specifies the COB-ID of the SDO server. The default is 0. If server COB-ID is 0, this VI calculates the effective server COB-ID by adding node-ID to a constant. The CANopen protocol defines the value of this constant. Otherwise, this VI ignores node-ID and uses server COB-ID as the effective server COB-ID. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | SDO object out returns the reference number of the SDO object that you created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SYNC Create

[IMAGE alt='image' src='images/CANopen_Sync_Create.gif']

|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
| --- | --- |
|  | COB-ID specifies the COB-ID of the SYNC object. The default is 0. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. If COB-ID is 0, this VI uses the effective COB-ID 0x80. Otherwise, this VI uses COB-ID as the effective COB-ID. Note You can create only one SYNC object in a CANopen network. |
|  | counter overflow value specifies the value of the synchronous counter overflow object. The valid range of counter overflow value is 0 and 2 to 240. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | SYNC object out returns the reference number of the SYNC object that this VI created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Heartbeat Create

[IMAGE alt='image' src='images/CANopen_Heartbeat_Create.gif']

|  | node-ID specifies the node-ID of the device for which you want to create a heartbeat object. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | COB-ID specifies the COB-ID of the heartbeat message. The default is 0. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. If COB-ID is 0, this VI calculates the effective COB-ID by adding the node-ID to 0x700 (1792 dec). Otherwise, this VI uses COB-ID as the effective COB-ID. |
|  | consumer time specifies the maximum time, in milliseconds, between the transmission of two subsequent heartbeat messages. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | factor specifies a tolerance factor of consumer time. The default is 2. LabVIEW multiplies consumer time by factor and uses the product as the timeout of consumer devices. |
|  | interface object out returns the refnum of interface object in. |
|  | heartbeat object out returns the reference number of the heartbeat object that you created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Node Guarding Create

[IMAGE alt='image' src='images/CANopen_Node_Guard_Create.gif']

|  | node-ID specifies the node-ID of the device for which you want to create a node guarding object. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | COB-ID specifies the COB-ID of the node guarding message. The default is 0. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. If COB-ID is 0, this VI calculates the effective COB-ID by adding the node-ID to 0x700 (1792 dec). Otherwise, this VI uses COB-ID as the effective COB-ID. |
|  | guard time specifies the time interval, in milliseconds, that the node guarding master sends requests to slave devices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | node guarding object out returns the reference number of the node guarding object that this VI created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Emergency Create

[IMAGE alt='image' src='images/CANopen_Emergency_Create.gif']

|  | node-ID specifies the node-ID of the device for which you want to create an EMCY object. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | COB-ID specifies the COB-ID of the EMCY message. The default is 0. CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. If COB-ID is 0, this VI calculates the effective COB-ID by adding the node-ID to 0x80 (128 dec). Otherwise, this VI uses COB-ID as the effective COB-ID. |
|  | buffer size specifies the maximum number of EMCY messages that the buffer saves. The buffer is a first-in-first-out buffer. The default is 0. If buffer size is 0, the buffer keeps only the latest EMCY message. If buffer size is greater than 0, the EMCY object keeps EMCY messages in a queue when the object receives EMCY messages. If the object receives more messages than buffer size, the object returns an overflow warning. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | emergency object out returns the reference number of the EMCY object that this VI created. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen CAN Frame Read Create

[IMAGE alt='image' src='images/CANopen_ReadCanFrm_Create.gif']

|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
| --- | --- |
|  | buffer size specifies the maximum number of CAN frames that the buffer saves. The buffer is a first-in-first-out buffer. The default is 0. If buffer size is 0, the buffer keeps only the latest CAN frame. If buffer size is greater than 0, the CAN frame read object keeps CAN frames in a queue when the object receives CAN frames. If the object receives more frames than buffer size, the object returns an overflow warning. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CAN frame read object out returns the reference number of the CAN frame read object that this VI created. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-emergency-convert-vi.html language=enus -->
## TOPIC 00013: CANopen Emergency Convert VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-emergency-convert-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-emergency-convert-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Converts a specified emergency (EMCY) message to an error description and a cluster containing the bit states of the error register. This VI is not optimized for real-time performance. emergency message specifies the emergency message that you want to convert. error code

### CANopen Emergency Convert VI

**Owning Palette:** Advanced VIs

Converts a specified [emergency](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_emergencies_emcy) (EMCY) message to an error description and a cluster containing the bit states of the [error register](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_emergencies_emcy).

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

[IMAGE alt='image' src='images/canopen_emergency_convert.gif']

|  | emergency message specifies the emergency message that you want to convert. error code specifies an error code that the EMCY message contains. This error code indicates an device-internal error. error register specifies an error register in a bit field. The error register contains a copy of the data of object 0x1001 in the object dictionary when the error occurs. The value of the error register represents the following error types: 0generic error1electric current error2voltage error3temperature error4communication error5device profile specific error6reserved7manufacturer specific error manufacturer specific error field specifies error messages that the device manufacturer provides. |
| --- | --- |
|  | error code specifies an error code that the EMCY message contains. This error code indicates an device-internal error. |
|  | error register specifies an error register in a bit field. The error register contains a copy of the data of object 0x1001 in the object dictionary when the error occurs. The value of the error register represents the following error types: 0generic error1electric current error2voltage error3temperature error4communication error5device profile specific error6reserved7manufacturer specific error |
| 0 | generic error |
| 1 | electric current error |
| 2 | voltage error |
| 3 | temperature error |
| 4 | communication error |
| 5 | device profile specific error |
| 6 | reserved |
| 7 | manufacturer specific error |
|  | manufacturer specific error field specifies error messages that the device manufacturer provides. |
|  | error description returns the description of error code. |
|  | error register bits returns a cluster containing the bit states of error register. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-error-control-read-vi.html language=enus -->
## TOPIC 00014: CANopen Error Control Read VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-error-control-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-error-control-read-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Controls errors of CANopen devices. Use this VI to read received messages of an emergency (EMCY) object, the current state of a heartbeat object, or the current state of a node guarding object. You must manually select the polymorphic instance to use. This VI is optimized

### CANopen Error Control Read VI

**Owning Palette:** CANopen VIs

Controls errors of CANopen devices. Use this VI to read received messages of an [emergency](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_emergencies_emcy) (EMCY) object, the current state of a [heartbeat](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, or the current state of a [node guarding](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object. You must manually select the polymorphic instance to use.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

CANopen Heartbeat State Read

[IMAGE alt='image' src='images/canopen_error_control_read.gif']

|  | heartbeat object in specifies the reference number of a heartbeat object. You can create a heartbeat object by using the CANopen Heartbeat Create VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | heartbeat object out returns the reference number of heartbeat object in. |
|  | state returns the state information of the heartbeat object. The state indicates the network management state of a device. Note The unknown status indicates that the heartbeat consumer device did not receive any messages from the heartbeat producer device. 0boot-up1unknown4stopped5operational127pre-operational128connection lost |
| 0 | boot-up |
| 1 | unknown |
| 4 | stopped |
| 5 | operational |
| 127 | pre-operational |
| 128 | connection lost |
|  | error out contains error information. This output provides standard error out functionality. |
|  | timestamp returns the device firmware time when the message arrives at the object. |

CANopen Node Guarding State Read

[IMAGE alt='image' src='images/canopen_node_guard_state_read.gif']

|  | node guarding object in specifies the reference number of a node guarding object. You can create a node guarding object by using the CANopen Node Guard Create VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | node guarding object out returns the reference number of node guarding object in. |
|  | state returns the state of the node guarding object. The state indicates the network management state of a device. Note The unknown status indicates that the node guarding master did not receive any messages from the slave device. 0boot-up1unknown4stopped5operational127pre-operational128connection lost |
| 0 | boot-up |
| 1 | unknown |
| 4 | stopped |
| 5 | operational |
| 127 | pre-operational |
| 128 | connection lost |
|  | error out contains error information. This output provides standard error out functionality. |
|  | timestamp returns the device firmware time when the message arrives at the object. |

CANopen Emergency Read

[IMAGE alt='image' src='images/canopen_emergency_read.gif']

|  | emergency object in specifies the reference number of an EMCY object. You can create an EMCY object by using the CANopen Emergency Create VI. |
| --- | --- |
|  | timeout specifies the time, in seconds, that this VI waits for the new EMCY message in the EMCY buffer. The buffer is a first-in-first-out (FIFO) buffer. The default is 0. You can enter decimal values such as 0.05. If timeout is 0, this VI returns a warning if the EMCY object has not received any messages since the object instance is started. If timeout is greater than 0, this VI returns an error if the EMCY object has not received any messages since the object instance is started. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | emergency object out returns the reference number of emergency object in. |
|  | new message? indicates whether emergency message is an unread message. If new message? is TRUE, no device or VI reads emergency message before this VI reads the message. |
|  | emergency message returns the EMCY message that this VI reads from the EMCY object. If the EMCY buffer receives a new message within timeout, emergency message returns the new message. If the EMCY buffer receives no messages within timeout, emergency message returns different values in the following cases: If the EMCY buffer size is greater than 0 and the FIFO buffer contains messages, emergency message returns the next new data in the FIFO buffer. If the EMCY buffer size is greater than 0 and all messages in the buffer have been read, emergency message returns the latest message and new message? returns FALSE. If the EMCY buffer size is 0, emergency message returns the latest message from the EMCY object. error code returns an error code that the EMCY message contains. This error code indicate an device-internal error. error register returns an error register in a bit field. The error register contains a copy of the data of object 0x1001 in the object dictionary when the error occurs. The value of the error register represents the following error types: 0generic error1electric current error2voltage error3temperature error4communication error5device profile specific error6reserved7manufacturer specific error manufacturer specific error field returns error messages that the device manufacturer provides. |
|  | error code returns an error code that the EMCY message contains. This error code indicate an device-internal error. |
|  | error register returns an error register in a bit field. The error register contains a copy of the data of object 0x1001 in the object dictionary when the error occurs. The value of the error register represents the following error types: 0generic error1electric current error2voltage error3temperature error4communication error5device profile specific error6reserved7manufacturer specific error |
| 0 | generic error |
| 1 | electric current error |
| 2 | voltage error |
| 3 | temperature error |
| 4 | communication error |
| 5 | device profile specific error |
| 6 | reserved |
| 7 | manufacturer specific error |
|  | manufacturer specific error field returns error messages that the device manufacturer provides. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | timestamp returns the device firmware time when the message arrives at the object. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-fetch-from-data-vi.html language=enus -->
## TOPIC 00015: CANopen Fetch from Data VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-fetch-from-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-fetch-from-data-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Converts a specified CANopen data array to LabVIEW-compatible data. You must manually select the polymorphic instance to use. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. Deta

### CANopen Fetch from Data VI

**Owning Palette:** Advanced VIs

Converts a specified CANopen data array to LabVIEW-compatible data. You must manually select the polymorphic instance to use.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

Details

CANopen Fetch from Data [I8]

[IMAGE alt='image' src='images/canopen_fetch_from_data_I8.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | signed 8-bit integer returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [I16]

[IMAGE alt='image' src='images/canopen_fetch_from_data_I16.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | signed 16-bit integer returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [I32]

[IMAGE alt='image' src='images/canopen_fetch_from_data_i32.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | signed 32-bit integer returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [U8]

[IMAGE alt='image' src='images/canopen_fetch_from_data_u8.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | unsigned 8-bit integer returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [U16]

[IMAGE alt='image' src='images/canopen_fetch_from_data_u16.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | unsigned 16-bit integer returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [U32]

[IMAGE alt='image' src='images/canopen_fetch_from_data_u32.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | unsigned 32-bit integer returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [SGL]

[IMAGE alt='image' src='images/canopen_fetch_from_data_sgl.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | 4-byte single returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [DBL]

[IMAGE alt='image' src='images/canopen_fetch_from_data_dbl.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | 8-byte double returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data [STR]

[IMAGE alt='image' src='images/canopen_fetch_from_data_str.gif']

|  | CANopen data in specifies the CANopen data array that contains the target element you want to convert. |
| --- | --- |
|  | offset specifies the index of a starting element. This VI converts the CANopen data from this element. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | string length specifies the maximum length of the resulting string. The default is –1, which specifies this VI returns all the values from offset to the end of the CANopen data in array. |
|  | CANopen data out returns the original data array in CANopen data in. |
|  | string returns the resulting LabVIEW data. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Fetch from Data Details

LabVIEW uses the big-endian format, which places the most significant byte first. CANopen uses the little-endian format, which places the least significant byte first. Use the CANopen SDO Read VI to read CANopen data and use this VI to convert CANopen data to LabVIEW-compatible data.

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-nmt-write-vi.html language=enus -->
## TOPIC 00016: CANopen NMT Write VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-nmt-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-nmt-write-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Transmits a network management (NMT) command over a CANopen network. This command controls NMT states of one or all devices on the network. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce

### CANopen NMT Write VI

**Owning Palette:** CANopen VIs

Transmits a [network management](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_network_management) (NMT) command over a CANopen network. This command controls NMT states of one or all devices on the network.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/canopen_nmt_write.gif']

|  | node-ID specifies the node-ID of a target device to which you want to send the command. If node-ID is 0, this VI sends the command to all devices on the CANopen network. The default is 0. |
| --- | --- |
|  | interface object in specifies the reference number of an interface object. This object is an interface to the CANopen network. You can create an interface by using the CANopen Interface Create VI. |
|  | command specifies the command that this VI sends. 1start remote node—Switches the device into the operational state. When the state is operational, the device supports all CANopen communication objects.2stop remote node—Switches the device into the stopped state. When the state is stopped, the device only supports NMT communication.128enter pre-operational—Switches the device into the pre-operational state. When the state is pre-operational, the device supports all CANopen communication objects with the exception of PDO objects.129reset node—Switches the device into the reset application state. When the state is reset application, the device resets the parameters of the manufacturer specific and the standardized device profile areas to power-on values. The device then enters the reset communication state.130reset communication—Switches the device into the reset communication state. When the state is reset communication, this device resets the parameters of the communication profile area to power-on values. The device then sends a boot-up message and enters the pre-operational state. |
| 1 | start remote node—Switches the device into the operational state. When the state is operational, the device supports all CANopen communication objects. |
| 2 | stop remote node—Switches the device into the stopped state. When the state is stopped, the device only supports NMT communication. |
| 128 | enter pre-operational—Switches the device into the pre-operational state. When the state is pre-operational, the device supports all CANopen communication objects with the exception of PDO objects. |
| 129 | reset node—Switches the device into the reset application state. When the state is reset application, the device resets the parameters of the manufacturer specific and the standardized device profile areas to power-on values. The device then enters the reset communication state. |
| 130 | reset communication—Switches the device into the reset communication state. When the state is reset communication, this device resets the parameters of the communication profile area to power-on values. The device then sends a boot-up message and enters the pre-operational state. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | interface object out returns the refnum of interface object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-node-id-change-vi.html language=enus -->
## TOPIC 00017: CANopen Node-ID Change VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-node-id-change-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-node-id-change-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Changes the node-ID of a specified device and resets the device to activate the new node-ID. This VI is not optimized for real-time performance. Details revision number specifies the revision information of a CANopen device. Each revision of a CANopen device has a unique

### CANopen Node-ID Change VI

**Owning Palette:** Advanced VIs

Changes the node-ID of a specified device and resets the device to activate the new node-ID.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

Details

[IMAGE alt='image' src='images/canopen_nodeid_change.gif']

|  | revision number specifies the revision information of a CANopen device. Each revision of a CANopen device has a unique revision number. The default is 0. |
| --- | --- |
|  | interface name specifies a name of the device interface. The interface corresponds to a CAN port on a CANopen board. You can use Measurement & Automation Explorer to view the mapping relationship between each interface name and each specific piece of hardware. |
|  | baud rate specifies the baud rate of the CANopen interface. |
|  | new node-ID specifies the new node-ID of the device. |
|  | vendor ID specifies the vendor information for the CANopen device. Each CANopen device vendor has a unique vendor ID. The default is 0. |
|  | product code specifies the product type of the device. Each type of CANopen device has a unique product code. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial number specifies the serial number of the device. Each CANopen device has a unique serial number. The default is 0. |
|  | error code returns the CANopen-specific error code of the device. This error code indicates a general error type of the device. |
|  | specific error returns specific error information of the CANopen device. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Node-ID Change Details

If the target device is the only device on the CANopen bus, you can set **revision number**, **vendor ID**, **product code**, and **serial number** to the default value 0. If the CANopen bus has multiple devices, you must specify these parameters of the target device.

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-rpdo-write-vi.html language=enus -->
## TOPIC 00018: CANopen RPDO Write VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-rpdo-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-rpdo-write-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Writes data to a specified receive-process data object (RPDO). This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. RPDO object in specifies the reference number of an RPDO to which yo

### CANopen RPDO Write VI

**Owning Palette:** CANopen VIs

Writes data to a specified receive-[process data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_pdo) (RPDO).

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/CANopen_RPDO_Write.gif']

|  | RPDO object in specifies the reference number of an RPDO to which you want to write data. You can create an RPDO by using the CANopen RPDO Create VI. |
| --- | --- |
|  | data specifies the CANopen data that you want to write to the object. Use the CANopen Convert to Data VI to convert LabVIEW data to CANopen data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RPDO object out returns the reference number of RPDO object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-sdo-batch-write-vi.html language=enus -->
## TOPIC 00019: CANopen SDO Batch Write VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-sdo-batch-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-sdo-batch-write-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Sends out a list of service data object (SDO) write requests. You can define the list in a batch SDO. You must create and deploy a batch SDO in the Project Explorer window before using this VI. This VI is not optimized for real-time performance. SDO object in specifies th

### CANopen SDO Batch Write VI

**Owning Palette:** CANopen VIs

Sends out a list of [service data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sdo) (SDO) write requests. You can define the list in a batch SDO. You must [create](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_create_bsdo) and deploy a batch SDO in the **Project Explorer** window before using this VI.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

[IMAGE alt='image' src='images/CANopen_SDO_Batch_Write.gif']

|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
| --- | --- |
|  | batch SDO name specifies the name of the batch SDO that you want to write. The name of the batch SDO must be identical to the batch SDO you created in the Project Explorer window. |
|  | timeout specifies the time, in seconds, that this VI waits for writing each SDO in the batch. The default is 1. You can enter decimal values such as 0.05. If this VI times out in writing any object that the batch SDO defines, this VI returns corresponding error codes at completion code and error out. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-sdo-completion-code-to-string-vi.html language=enus -->
## TOPIC 00020: CANopen SDO Completion Code to String VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-sdo-completion-code-to-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-sdo-completion-code-to-string-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Converts an SDO completion code to a description string. Use this VI to convert completion codes that the CANopen SDO Read VI, the CANopen SDO Write VI, or the CANopen SDO Batch Write VI returns. This VI is not optimized for real-time performance. SDO completion code spe

### CANopen SDO Completion Code to String VI

**Owning Palette:** Advanced VIs

Converts an SDO completion code to a description string. Use this VI to convert completion codes that the CANopen SDO Read VI, the CANopen SDO Write VI, or the CANopen SDO Batch Write VI returns.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

[IMAGE alt='image' src='images/canopen_sdo_completion_code_to_string.gif']

|  | SDO completion code specifies the completion code that you want to convert. |
| --- | --- |
|  | description returns the description of the completion code. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-sdo-read-vi.html language=enus -->
## TOPIC 00021: CANopen SDO Read VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-sdo-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-sdo-read-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Reads the value of an object dictionary entry by using a service data object (SDO). If an error occurs, this VI returns an empty value. You must manually select the polymorphic instance to use. This VI is not optimized for real-time performance. CANopen SDO Read [I32] tim

### CANopen SDO Read VI

**Owning Palette:** CANopen VIs

Reads the value of an [object dictionary](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_object_dictionary) entry by using a [service data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sdo) (SDO). If an error occurs, this VI returns an empty value. You must manually select the polymorphic instance to use.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

CANopen SDO Read [I32]

[IMAGE alt='image' src='images/CANopen_SDO_Read.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | I32 data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [I16]

[IMAGE alt='image' src='images/canopen_sdo_read_i16.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | I16 data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [I8]

[IMAGE alt='image' src='images/canopen_sdo_read_i8.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | I8 data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [U32]

[IMAGE alt='image' src='images/canopen_sdo_read_u32.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | U32 data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [U16]

[IMAGE alt='image' src='images/canopen_sdo_read_u16.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | U16 data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [U8]

[IMAGE alt='image' src='images/canopen_sdo_read_u8.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | U8 data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [SGL]

[IMAGE alt='image' src='images/canopen_sdo_read_sgl.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | SGL data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [STR]

[IMAGE alt='image' src='images/canopen_sdo_read_str.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data size specifies the data size, in bytes, of the object that you want to read. LabVIEW allocates a buffer of this size. This VI resizes the buffer to the actual data size of the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | string data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [DBL]

[IMAGE alt='image' src='images/canopen_sdo_read_dbl.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SDO object out returns the reference number of SDO object in. |
|  | DBL data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Read [Block]

[IMAGE alt='image' src='images/canopen_sdo_read_blk.gif']

|  | timeout specifies the time, in seconds, that this VI waits for reading the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not read data from the object within the timeout, this VI returns corresponding error codes at completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI uses the SDO to read objects in the object dictionary. |
|  | object index specifies the index of the dictionary object that you want to read. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to read. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data size specifies the data size, in bytes, of the object that you want to read. LabVIEW allocates a buffer of this size. This VI resizes the buffer to the actual data size of the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | block data returns the data of the SDO object. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-sdo-write-vi.html language=enus -->
## TOPIC 00022: CANopen SDO Write VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-sdo-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-sdo-write-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Writes the value of an object dictionary entry by using a service data object (SDO). You can write different types of data by selecting the corresponding polymorphic VI instances. Wire data to the data type data input to determine the polymorphic instance to use or manual

### CANopen SDO Write VI

**Owning Palette:** CANopen VIs

Writes the value of an [object dictionary](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_object_dictionary) entry by using a [service data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sdo) (SDO). You can write different types of data by selecting the corresponding polymorphic VI instances. Wire data to the **data type data** input to determine the polymorphic instance to use or manually select the instance.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

CANopen SDO Write [I32]

[IMAGE alt='image' src='images/CANopen_SDO_Write_I32_.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | I32 data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [I16]

[IMAGE alt='image' src='images/canopen_sdo_write_i16.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | I16 data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [I8]

[IMAGE alt='image' src='images/canopen_sdo_write_i8.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | I8 data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [U32]

[IMAGE alt='image' src='images/canopen_sdo_write_u32.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | U32 data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [U16]

[IMAGE alt='image' src='images/canopen_sdo_write_u16.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | U16 data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [U8]

[IMAGE alt='image' src='images/canopen_sdo_write_u8.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | U8 data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [SGL]

[IMAGE alt='image' src='images/canopen_sdo_write_sgl.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SGL data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [DBL]

[IMAGE alt='image' src='images/canopen_sdo_write_dbl.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DBL data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [STR]

[IMAGE alt='image' src='images/canopen_sdo_write_str.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | string data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SDO Write [Block]

[IMAGE alt='image' src='images/canopen_sdo_write_block.gif']

|  | timeout specifies the time, in seconds, that this VI waits for writing the SDO data. The default is 1. You can enter decimal values such as 0.05. If this VI does not write data to the object within the timeout, this VI returns corresponding error codes in completion code and error out. |
| --- | --- |
|  | SDO object in specifies the reference number of an SDO. This VI writes data to the batch SDO through this SDO. You can create an SDO by using the CANopen SDO Create VI. |
|  | object index specifies the index of the dictionary object that you want to write. |
|  | object sub-index specifies the sub-index of the dictionary object that you want to write. If the object does not have a sub-index, you can set object sub-index to 0. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | block data specifies the CANopen data that you want to write to the object. |
|  | SDO object out returns the reference number of SDO object in. |
|  | completion code returns the failure information of the SDO operation. If the SDO operation does not fail, completion code returns 0. You can pass this code to the CANopen SDO Completion Code to String VI to get extended information about the failure. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-start-vi.html language=enus -->
## TOPIC 00023: CANopen Start VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-start-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-start-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Starts a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a node guarding object, a synchronization (SYNC) object, an emergency (EMCY) object, or a CAN frame read object. LabVIEW automatically starts an object when the applic

### CANopen Start VI

**Owning Palette:** Advanced VIs

Starts a transmit-[process data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_pdo) (TPDO), a receive-process data object (RPDO), a [heartbeat](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, a [node guarding](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, a [synchronization](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sync_object) (SYNC) object, an [emergency](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_emergencies_emcy) (EMCY) object, or a CAN frame read object. LabVIEW automatically starts an object when the application reads or writes the object for the first time. Use this VI when you want to start and stop objects manually. You must manually select the polymorphic instance to use.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

CANopen TPDO Start

[IMAGE alt='image' src='images/CANopen_TPDO_Start.gif']

|  | TPDO object in specifies the reference number of the TPDO that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TPDO object out returns the reference number of TPDO object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen RPDO Start

[IMAGE alt='image' src='images/canopen_rpdo_start.gif']

|  | RPDO object in specifies the reference number of the RPDO object that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RPDO object out returns the reference number of RPDO object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Heartbeat Start

[IMAGE alt='image' src='images/canopen_heartbeat_start.gif']

|  | heartbeat object in specifies the reference number of the heartbeat object that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | heartbeat object out returns the reference number of heartbeat object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Node Guarding Start

[IMAGE alt='image' src='images/canopen_node_guard_start.gif']

|  | node guarding object in specifies the reference number of the node guarding object that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | node guarding object out returns the reference number of node guarding object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Emergency Start

[IMAGE alt='image' src='images/canopen_emergency_start.gif']

|  | emergency object in specifies the reference number of the EMCY object that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | emergency object out returns the reference number of emergency object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen CAN Frame Read Start

[IMAGE alt='image' src='images/canopen_readcanfrm_start.gif']

|  | CAN frame read object in specifies the reference number of the CAN frame read object that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CAN frame read object out returns the reference number of CAN frame read object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SYNC Start

[IMAGE alt='image' src='images/canopen_sync_start.gif']

|  | SYNC object in specifies the reference number of the SYNC object that you want to start. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SYNC object out returns the reference number of SYNC object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-stop-vi.html language=enus -->
## TOPIC 00024: CANopen Stop VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-stop-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-stop-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Stops a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a node guarding object, a synchronization (SYNC) object, an emergency (EMCY) object, or a CAN frame read object. LabVIEW stops all objects when you close an application

### CANopen Stop VI

**Owning Palette:** Advanced VIs

Stops a transmit-[process data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_pdo) (TPDO), a receive-process data object (RPDO), a [heartbeat](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, a [node guarding](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_heartbeat_and_node_guarding) object, a [synchronization](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sync_object) (SYNC) object, an [emergency](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_emergencies_emcy) (EMCY) object, or a CAN frame read object. LabVIEW stops all objects when you close an application. Use this VI when you want to start and stop objects manually. You must manually select the polymorphic instance to use.

This VI is not optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support).

CANopen TPDO Stop

[IMAGE alt='image' src='images/CANopen_TPDO_Stop.gif']

|  | TPDO object in specifies the reference number of the TPDO object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TPDO object out returns the reference number of TPDO object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen RPDO Stop

[IMAGE alt='image' src='images/canopen_rpdo_stop.gif']

|  | RPDO object in specifies the reference number of the RPDO object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RPDO object out returns the reference number of RPDO object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Heartbeat Stop

[IMAGE alt='image' src='images/canopen_heartbeat_stop.gif']

|  | heartbeat object in specifies the reference number of the heartbeat object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | heartbeat object out returns the reference number of heartbeat object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Node Guarding Stop

[IMAGE alt='image' src='images/canopen_node_guard_stop.gif']

|  | node guarding object in specifies the reference number of the node guarding object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | node guarding object out returns the reference number of node guarding object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen Emergency Stop

[IMAGE alt='image' src='images/canopen_emergency_stop.gif']

|  | emergency object in specifies the reference number of the EMCY object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | emergency object out returns the reference number of emergency object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen SYNC Stop

[IMAGE alt='image' src='images/canopen_sync_stop.gif']

|  | SYNC object in specifies the reference number of the SYNC object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SYNC object out returns the reference number of SYNC object in. |
|  | error out contains error information. This output provides standard error out functionality. |

CANopen CAN Frame Read Stop

[IMAGE alt='image' src='images/canopen_readcanfrm_stop.gif']

|  | CAN frame read object in specifies the reference number of the CAN frame read object that you want to stop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CAN frame read object out returns the reference number of CAN frame read object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-sync-reset-vi.html language=enus -->
## TOPIC 00025: CANopen SYNC Reset VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-sync-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-sync-reset-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Resets the synchronization (SYNC) counter value of the next SYNC message. Use this VI to start a new SYNC cycle before the counter value reaches the value of the synchronous counter overflow object. This VI is optimized for real-time performance. This VI executes with low

### CANopen SYNC Reset VI

**Owning Palette:** CANopen VIs

Resets the [synchronization](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sync_object) (SYNC) counter value of the next SYNC message. Use this VI to start a new SYNC cycle before the counter value reaches the value of the [synchronous counter overflow object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sync_object).

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/canopen_sync_reset.gif']

|  | SYNC object in specifies the reference number of the SYNC object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SYNC object out returns the reference number of SYNC object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-sync-send-vi.html language=enus -->
## TOPIC 00026: CANopen SYNC Send VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-sync-send-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-sync-send-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Sends out a synchronization (SYNC) message through a specified SYNC object. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. SYNC object in specifies the reference number of the SY

### CANopen SYNC Send VI

**Owning Palette:** CANopen VIs

Sends out a [synchronization](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sync_object) (SYNC) message through a specified SYNC object.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/canopen_sync_send.gif']

|  | SYNC object in specifies the reference number of the SYNC object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SYNC object out returns the reference number of SYNC object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-tpdo-read-vi.html language=enus -->
## TOPIC 00027: CANopen TPDO Read VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-tpdo-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-tpdo-read-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Reads data from the receive buffer of a specified transmit-process data object (TPDO). This VI also returns the device firmware time when the data arrives at the TPDO. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shar

### CANopen TPDO Read VI

**Owning Palette:** CANopen VIs

Reads data from the receive buffer of a specified transmit-[process data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_pdo) (TPDO). This VI also returns the device firmware time when the data arrives at the TPDO.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/CANopen_TPDO_Read.gif']

|  | TPDO object in specifies the TPDO object that you want to read. |
| --- | --- |
|  | timeout specifies the time, in seconds, that this VI waits for the new data in the TPDO buffer. The buffer is a first-in-first-out (FIFO) buffer. The default is 0, or no wait. You can enter decimal values such as 0.05. If timeout is 0, this VI returns a warning if the TPDO has not received any data since the TPDO instance is started. If timeout is greater than 0, this VI returns an error if the TPDO has not received any data since the TPDO instance is started. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TPDO object out returns the reference number of TPDO object in. |
|  | data returns the TPDO data that this VI reads. If the TPDO buffer receives new data within timeout, data returns the new data. If the TPDO buffer receives no data within timeout, data returns different values in the following cases: If the TPDO buffer size is greater than 0 and the buffer contains data, data returns the next new data in the FIFO buffer. If the TPDO buffer size is greater than 0 and all data in the TPDO buffer has been read, data returns the latest data and new data? returns FALSE. If the TPDO buffer size is 0, data returns the latest data from the TPDO. |
|  | new data? indicates whether data is unread. If new data? is TRUE, no device or VI reads data before this VI does. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | timestamp returns the device firmware time when the TPDO message arrives. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-tpdo-rtr-request-send-vi.html language=enus -->
## TOPIC 00028: CANopen TPDO RTR Request Send VI

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-tpdo-rtr-request-send-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-tpdo-rtr-request-send-vi.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: CANopen VIs Sends a remote transmission request (RTR) to a transmit-process data object (TPDO) producer. When the TPDO producer receives the RTR, the producer sends out a PDO to the CANopen network. The COB-ID of the TPDO corresponds to the COB-ID in TPDO object in. This VI is optimi

### CANopen TPDO RTR Request Send VI

**Owning Palette:** CANopen VIs

Sends a remote transmission request (RTR) to a transmit-[process data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_pdo) (TPDO) producer. When the TPDO producer receives the RTR, the producer sends out a PDO to the CANopen network. The COB-ID of the TPDO corresponds to the COB-ID in **TPDO object in**.

This VI is optimized for [real-time performance](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_rt_support). This VI executes with low cost and avoids access to shared resources that can induce jitter.

[IMAGE alt='image' src='images/CANopen_TPDO_RTR_Request_Send.gif']

|  | TPDO object in specifies the reference number of a TPDO. This VI sends an RTR to the producer of this TPDO object. You can create a TPDO by using the CANopen TPDO Create VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TPDO object out returns the reference number of TPDO object in. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

CANopen VIs

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen-vis.html language=enus -->
## TOPIC 00029: CANopen VIs

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen-vis.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the CANopen VIs to control and configure CANopen devices on a CANopen network. You can use 11-bit or 29-bit COB-IDs for the CANopen VIs. Palette ObjectDescriptionCANopen CreateCreates an interface, a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a

### CANopen VIs

Use the CANopen VIs to control and configure CANopen devices on a CANopen network. You can use 11-bit or 29-bit COB-IDs for the CANopen VIs.

| Palette Object | Description |
| --- | --- |
| CANopen Create | Creates an interface, a transmit-process data object (TPDO), a receive-process data object (RPDO), a heartbeat object, a node guarding object, a synchronization (SYNC) object, an emergency (EMCY) object, or a CAN frame read object. You must manually select the polymorphic instance to use. When you create objects on a CANopen network, ensure each object that receives data, such as RPDOs, SDOs, heartbeat objects, node guarding objects, and emergency object, has a unique COB-ID. Otherwise, this VI returns an error. This VI is not optimized for real-time performance. |
| CANopen Error Control Read | Controls errors of CANopen devices. Use this VI to read received messages of an emergency (EMCY) object, the current state of a heartbeat object, or the current state of a node guarding object. You must manually select the polymorphic instance to use. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen NMT Write | Transmits a network management (NMT) command over a CANopen network. This command controls NMT states of one or all devices on the network. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen RPDO Write | Writes data to a specified receive-process data object (RPDO). This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen SDO Batch Write | Sends out a list of service data object (SDO) write requests. You can define the list in a batch SDO. You must create and deploy a batch SDO in the Project Explorer window before using this VI. This VI is not optimized for real-time performance. |
| CANopen SDO Read | Reads the value of an object dictionary entry by using a service data object (SDO). If an error occurs, this VI returns an empty value. You must manually select the polymorphic instance to use. This VI is not optimized for real-time performance. |
| CANopen SDO Write | Writes the value of an object dictionary entry by using a service data object (SDO). You can write different types of data by selecting the corresponding polymorphic VI instances. Wire data to the data type data input to determine the polymorphic instance to use or manually select the instance. This VI is not optimized for real-time performance. |
| CANopen SYNC Reset | Resets the synchronization (SYNC) counter value of the next SYNC message. Use this VI to start a new SYNC cycle before the counter value reaches the value of the synchronous counter overflow object. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen SYNC Send | Sends out a synchronization (SYNC) message through a specified SYNC object. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen TPDO Read | Reads data from the receive buffer of a specified transmit-process data object (TPDO). This VI also returns the device firmware time when the data arrives at the TPDO. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |
| CANopen TPDO RTR Request Send | Sends a remote transmission request (RTR) to a transmit-process data object (TPDO) producer. When the TPDO producer receives the RTR, the producer sends out a PDO to the CANopen network. The COB-ID of the TPDO corresponds to the COB-ID in TPDO object in. This VI is optimized for real-time performance. This VI executes with low cost and avoids access to shared resources that can induce jitter. |

| Subpalette | Description |
| --- | --- |
| Advanced VIs | Use Advanced VIs to interact with CANopen objects, frames, and data arrays. |

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=canopen_intro.html language=enus -->
## TOPIC 00030: NI-Industrial Communications for CANopen Programming Reference Manual

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `canopen_intro.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/canopen_intro.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-Industrial Communications for CANopen Programming Reference Manual provides information about the CANopen VIs and error codes.

### NI-Industrial Communications for CANopen Programming Reference Manual

The NI-Industrial Communications for CANopen Programming Reference Manual provides information about the CANopen VIs and error codes.

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=change-device-baud-rate-dialog-box.html language=enus -->
## TOPIC 00031: Change Device Baud Rate Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `change-device-baud-rate-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/change-device-baud-rate-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click a target and select CANopen Utilities»Change Baud Rate from the shortcut menu to display this dialog box. Use this dialog box to change the baud rate of a CANopen device on a CANopen bus through the layer setting services (LSS). This dialog box includes th

### Change Device Baud Rate Dialog Box

In the **Project Explorer** window, right-click a target and select **CANopen Utilities»Change Baud Rate** from the shortcut menu to display this dialog box. Use this dialog box to change the baud rate of a CANopen device on a CANopen bus through the layer setting services (LSS).

This dialog box includes the following components:

- Interface Name âSpecifies the interface name of the device that you want to configure. Each interface name corresponds to a CAN port on the CANopen board. 
You can use Measurement & Automation Explorer to view the mapping relationship between each interface name and each specific piece of hardware.
- Current Baud Rate âSpecifies the current baud rate of the device. If you do not know the current baud rate of the device, place a checkmark in the Try all baud rates checkbox.
- Try all baud rates âSpecifies whether LabVIEW tries all possible baud rates to detect the baud rate of the current CANopen device. Note Enabling this checkbox may slow down the performance.
- New Baud Rate âSpecifies the new baud rate of the CANopen device.

If this dialog box fails to change the baud rate of a device, ensure the device supports LSS and is the only device on the CANopen bus.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=change-node-id-dialog-box.html language=enus -->
## TOPIC 00032: Change Node-ID Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `change-node-id-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/change-node-id-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click a target and select CANopen Utilities»Change Node-ID from the shortcut menu to display this dialog box. Use this dialog box to change the node-ID of a specified device through the layer setting services (LSS). Refer to the CiA 305: CANopen - Layer setting

### Change Node-ID Dialog Box

In the **Project Explorer** window, right-click a target and select **CANopen Utilities»Change Node-ID** from the shortcut menu to display this dialog box. Use this dialog box to change the node-ID of a specified device through the layer setting services (LSS). Refer to the CiA 305: CANopen - Layer setting services and protocol for more information about using LSS.

This dialog box includes the following components:

- Interface Name —Specifies the interface name of the device that you want to configure. Each interface name corresponds to a CAN port on the CANopen board. 
You can use Measurement & Automation Explorer to view the mapping relationship between each interface name and each specific piece of hardware.
- Interface Baud Rate —Specifies the baud rate of the device interface.
- New Node-ID —Specifies a new node-ID of the CANopen device.
- Multiple devices exist on the bus —Specifies whether the CANopen bus has multiple devices. If you place a checkmark in this checkbox, you must specify the target device that you want to change. 
You can use the following methods to specify the device: by node-ID or by identity.
  - By Node-ID —Specifies the node-ID of the target device.
  - By Identity —Specifies the following information about the target device:
    - Vendor ID
    - Product Code
    - Revision
    - Serial Number

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=eds-file-association-dialog-box.html language=enus -->
## TOPIC 00033: EDS File Association Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `eds-file-association-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/eds-file-association-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click a batch service data object (SDO) and select EDS File Association from the shortcut menu to display this dialog box. Use this dialog box to specify an electronic data sheet (EDS) file for the batch SDO. This dialog box includes the following components: Na

### EDS File Association Dialog Box

In the **Project Explorer** window, right-click a batch [service data object](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_sdo) (SDO) and select **EDS File Association** from the shortcut menu to display this dialog box.

Use this dialog box to specify an [electronic data sheet](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_eds_path_db) (EDS) file for the batch SDO.

This dialog box includes the following components:

- Name —Displays the name of the batch SDO.
- EDS File —Specifies the location of an electronic data sheet (EDS) file for the batch SDO. This EDS file is optional for a batch SDO.
- Location —Displays the location of the EDS file.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=eds-file-paths-dialog-box.html language=enus -->
## TOPIC 00034: EDS File Paths Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `eds-file-paths-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/eds-file-paths-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In LabVIEW, select Tools»CANopen EDS File Paths to display this dialog box. Use this dialog box to specify one or multiple default folders of electronic data sheet (EDS) files. LabVIEW searches these folders for the corresponding EDS file when you open a batch SDO object. If you list multiple folder

### EDS File Paths Dialog Box

In LabVIEW, select **Tools»CANopen EDS File Paths** to display this dialog box. Use this dialog box to specify one or multiple default folders of [electronic data sheet](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_object_dictionary) (EDS) files. LabVIEW searches these folders for the corresponding EDS file when you open a batch SDO object. If you list multiple folders as EDS file paths, LabVIEW searches these folders one by one according to the folder order in this dialog box. Use the **Up** and **Down** buttons to change the order of the folders.

Use this dialog box when you deploy CANopen projects from the development computer to another computer.

This dialog box includes the following components:

- List —Displays the current default EDS paths. You can add or remove paths by using the buttons in this dialog box.
- Add —Adds a folder to List .
- Remove —Removes a folder from List .
- Up —Moves a selected path in List up in the list order.
- Down —Moves a selected path in List down in the list order.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=error-codes.html language=enus -->
## TOPIC 00035: Error Codes

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `error-codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/error-codes.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The CANopen VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −2147137023 An internal fault occurred in the NI-IndCom for CANopen driver. Contact National Instruments and provide the copErrorLog.log file. On

### Error Codes

The CANopen VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −2147137023 | An internal fault occurred in the NI-IndCom for CANopen driver. Contact National Instruments and provide the copErrorLog.log file. On CompactRIO and PXI, this file is under C:\\ni-rt\\config. On Windows7 or Windows Vista, this file is under C:\\ProgramData\\National Instruments\\NI-IndCom for CANopen\\. On Windows XP, this file is under C:\\Documents and Settings\\All Users\\National Instruments\\NI-IndCom for CANopen\\. |
| −2147137022 | Board self-test failed (code 2). Reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147137020 | Board self-test failed (code 4). Reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147137019 | Board self-test failed (code 5). Reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147137018 | Board self-test failed (code 6). Reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147137017 | Computer went to the hibernation mode and the board lost power. Disable the hibernation mode in the Windows Control Panel. |
| −2147137016 | A write queue overflowed. Wait until the queue space becomes available and try again. |
| −2147137015 | The firmware of the board does not answer a command. Stop the application and execute a self-test. Try deactivating and reactivating the driver in the Device Manager. If the problem persists, contact National Instruments. |
| −2147137014 | The operation timed out. Specify a sufficient timeout value for the operation, or improve the performance of the operation (for example. read less data). |
| −2147137013 | A read queue overflowed. Reduce your data rate or call Read more frequently. |
| −2147137012 | The Read buffer is insufficient for a single frame. Provide a buffer large enough. |
| −2147137009 | The self-test cannot start because the board is occupied by an application. Stop all CANopen applications before executing a self-test. |
| −2147137008 | Allocation of memory failed. You do not have sufficient memory. |
| −2147137007 | The maximum number of sessions has exceeded. Reduce the session number and try again. |
| −2147137006 | The maximum number of connection objects has exceeded. Reduce the connection objects in sessions and try again. |
| −2147137005 | The maximum number of interface devices has exceeded. Reduce the device number and try again. |
| −2147137004 | A driver support file is missing. Reinstall the driver and try again. If the error persists, contact National Instruments. |
| −2147137003 | Board self-test failed (code 17). Reinstall the driver or switch the slot(s) of the board(s) before executing a self-test. If the error persists, contact National Instruments. |
| −2147136992 | An invalid reference has been passed to a CANopen function. Ensure the reference is from the CANopen VIs. |
| −2147136991 | An invalid handle has been passed to a CANopen system function. Ensure the system handle is valid. |
| −2147136990 | A device handle was expected for a CANopen function. |
| −2147136989 | An interface handle was expected for a CANopen function. |
| −2147136987 | LabVIEW cannot create a Timing Source VI on Windows. This VI is supported on LabVIEW Real-Time targets only. |
| −2147136911 | The transceiver value is invalid or you are trying to perform an operation that requires a different transceiver. |
| −2147136910 | The baud rate value is invalid. |
| −2147136909 | The baud rate value is empty. |
| −2147136908 | The bit timing value is invalid. Ensure the value is valid. |
| −2147136907 | The baud rate set does not match the allowed range of the transceiver. Change either the baud rate or the transceiver. |
| −2147136906 | The configured timing source is unknown for this interface. Ensure the timing source configuration is valid. |
| −2147136905 | The configured synchronization source is inappropriate for the hardware. Choose an appropriate timing source for the hardware. |
| −2147136904 | The source that you connected to the Master Timebase destination is missing. The interface verifies the source configuration when the interface receives a start trigger. Verify that your cables are configured correctly and that your timebase source is generating an appropriate waveform. |
| −2147136903 | The source that you connected to the Master Timebase destination does not generate an appropriate signal. The interface receives a signal with an unsupported frequency. Verify that your source is generating a signal at a supported frequency. |
| −2147136895 | An input value of a CANopen VI is invalid, for example, a null pointer is passed. Ensure the input values are valid. |
| −2147136892 | The CANopen hardware cannot be found. Ensure the CANopen hardware is correctly installed. Ensure you use the correct port name. You can get your device port name(s) in MAX. |
| −2147136880 | The specified interface is not valid or does not exist. Specify a valid and existing interface port name. |
| −2147136879 | The interface name is not valid. Ensure the interface name is valid. The name of the CANopen interface is an ASCII string with format "CANopenxx", where x is a decimal number starting at one that indicates which interface is being used. The valid range of interface names is from "CANopen01" to "CANopen32". |
| −2147136878 | The object handle passed in is not valid. Ensure you use a correct object handle returned from the CANopen VIs and make sure the object is not closed. |
| −2147136874 | The interface object already exists. You must specify another CAN interface to create an interface object. |
| −2147136873 | The object has not been started. You must start the object before using it. |
| −2147136872 | The object has already been created. The same object cannot be created again. |
| −2147136868 | The property size is not correct. Check the manual or header file to determine the correct property size. |
| −2147136867 | The property ID and the object handle do not match. For example, the property ID belongs to the SDO object, but the object handle passed in is a handle of the PDO object. Ensure you use an appropriate property ID for the given object type. |
| −2147136863 | The operation cannot be done in the current stage. Check the order of the operation and ensure the operation is at the appropriate stage. |
| −2147136862 | The buffer size is insufficient for the requested operation. Ensure the buffer size is sufficient for the requested operation. |
| −2147136858 | The property value or the parameter value is not valid. Ensure the property value or the parameter value is in the valid range. |
| −2147136856 | You tried to blink the port LEDs that are currently busy. Stop all applications running on that port. Do not access the port from MAX or the LabVIEW Project Explorer. |
| −2147136855 | You tried to set a queue size that exceeds the maximum queue size value. Specify an in-range queue size. |
| −2147136847 | The operation is invalid for this CANopen interface. Perform this operation on a suitable interface. |
| −2147136846 | The operation cannot be performed because the last service is pending. Wait for the last operation to complete or abort the operation. |
| −2147136845 | The response data is incorrect. Call the corresponding WaitForResponse function for the operation. |
| −2147136765 | The firmware received an unknown property code. Ensure the request property code is pre-defined. |
| −2147136764 | A bus off error occurs on the bus. Clear the bus off error physically. Then reopen the interface. Refer to the Troubleshooting CANopen Applications topic in the NI-Industrial Communications for CANopen Help for instructions of clearing bus off errors. |
| −2147136763 | The operation cannot be performed when the object is started. Stop the object and try again. |
| −2147136758 | The CANopen frames on this CANopen bus exceed the bandwidth of the CANopen hardware. Some of the CAN frames may be discarded. Reduce the CAN frames on the bus by connecting less CANopen devices or changing the device configuration. |
| −2147136756 | The CANopen driver is not installed correctly. Reinstall the CANopen driver and try again. |
| −2147136755 | The COB-ID is occupied. Choose a different COB-ID and try again. |
| −2147136754 | The buffer for sending out CAN frames is full. Adjust the speed of sending CAN frames. |
| −2147136753 | The value of COB-ID is invalid. Change the COB-ID to a valid value. If the COB-ID is an 11 bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29 bit COB-ID, the bit 29 (0-based) should be 1. |
| −2147136752 | The maximum number of total objects has exceeded. Create fewer objects (PDO, SDO etc). |
| −2147136733 | The size of the returned data does not match the requested data type. Check the data type of the object being read by SDO and choose the right data type when reading the SDO. |
| −2147136732 | The operation failed. |
| −2147136672 | One or multiple section names in the EDS file are empty or contain invalid characters. Correct the section name manually or contact the support of your CANopen device company to get a correct EDS file. |
| −2147136671 | One or multiple entry names in the EDS file are empty or contain invalid characters. Correct the entry name manually or contact the support of your CANopen device company to get a correct EDS file. |
| −2147136670 | The format of the EDS file is invalid. Correct the EDS file manually or contact the support of your CANopen device company to get a correct EDS file. |
| −2147136669 | One of the entries is not defined below a section. Correct the EDS file manually or contact the support of your CANopen device company to get a correct EDS file. |
| −2147136668 | The EDS file cannot be read. Ensure the EDS file exists and is readable. |
| −2147136667 | You are trying to start an interface that is missing bus power for the transceiver. Some physical layers on NI-CANopen hardware are internally powered, but others require external power in order for the port to operate. This error occurs when starting an interface on hardware that requires external power when no power is detected. Supply proper voltage to your transceiver. Refer to the CANopen Hardware book of the NI-Industrial Communications for CANopen Help for more information. |
| −2147136666 | Cannot create a connection to the CANopen module. Reinstall the CANopen driver and ensure the remote real-time target is turned on and working correctly. |
| −2147136665 | The device information (Vendor ID, Product Code, etc.) cannot be read by using SDO. Ensure the CANopen device is connected to the bus and the specified node-ID matches the node-ID of the CANopen device. |
| −2147136664 | Cannot connect to the remote real-time device. Ensure the IP address of the real-time device is correct and the CANopen driver is installed on the device. |
| −2147136663 | The device does not respond. Ensure the device supports LSS and use the correct device product information to communicate with the device again. |
| 346634 | The operation timed out. Specify a timeout long enough to complete the operation, or change the operation in a way that it can get completed in less time (for example, read less data). |
| 346635 | A read queue overflowed. Reduce your data rate or call Read more frequently. |

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=online-test-panel-dialog-box.html language=enus -->
## TOPIC 00036: Online Test Panel Dialog Box

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `online-test-panel-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/online-test-panel-dialog-box.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click a target and select CANopen Utilities»Online Test Panel to display the Device Baud Rate dialog box. In the Device Baud Rate dialog box, specify the interface name and the baud rate and click the OK button to display this dialog box. Use this dialog box to

### Online Test Panel Dialog Box

In the **Project Explorer** window, right-click a target and select **CANopen Utilities»Online Test Panel** to display the Device Baud Rate dialog box. In the **Device Baud Rate** dialog box, specify the interface name and the baud rate and click the **OK** button to display this dialog box. Use this dialog box to browse all devices on a CANopen network bus and perform [network management](/csh?context=ni-industrial-communications-canopen_canopenhelp_canopen_network_management) (NMT) operations.

This dialog box includes the following pages:

- Device List —Lists all devices with a specified baud rate on the CANopen bus.
  - List —Lists the detailed information of devices, such as Device Type (0x1000), Identity (0x1018), Error Register (0x1001), and NMT status.
  - Scan —Scans the CANopen bus again and refreshes Device List .
- NMT —Specifies the current NMT status of CANopen devices.
  - Select Devices —Specifies the target CANopen devices that you want to send the NMT message to.
  - Select NMT status —Specifies the NMT status of the target devices.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-canopen-api-ref path=project-explorer-window-environment.html language=enus -->
## TOPIC 00037: Project Explorer Window Environment

- bundle_id: `ni-industrial-communications-canopen-api-ref`
- source_path: `project-explorer-window-environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen-api-ref/raw/resource/enus/project-explorer-window-environment.html
- document_id: `ni-industrial-communications-canopen-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Project Explorer window displays the following NI-Industrial Communications for CANopen user interface items: Batch SDO Dialog Box Batch SDO General Settings Dialog Box Batch SDO - Object Dictionary Page Batch SDO - Batch SDO Preview Page Batch SDO - Online Validation Page Change Node-ID

### Project Explorer Window Environment

The LabVIEW Project Explorer window displays the following NI-Industrial Communications for CANopen user interface items:

- Batch SDO Dialog Box
- Batch SDO General Settings Dialog Box
- Batch SDO - Object Dictionary Page
- Batch SDO - Batch SDO Preview Page
- Batch SDO - Online Validation Page
- Change Node-ID Dialog Box
- Change Device Baud Rate Dialog Box
- EDS File Paths Dialog Box
- Online Test Panel Dialog Box
- EDS File Association Dialog Box
