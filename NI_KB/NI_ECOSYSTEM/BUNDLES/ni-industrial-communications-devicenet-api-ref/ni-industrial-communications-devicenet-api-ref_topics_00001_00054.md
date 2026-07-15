# NI DOCUMENT BUNDLE: ni-industrial-communications-devicenet-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-industrial-communications-devicenet-api-ref start=1 end=54 -->
<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=advanced-vis.html language=enus -->
## TOPIC 00001: Advanced VIs

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `advanced-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/advanced-vis.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Advanced VIs to read and write the DeviceNet Explicit Messages and to set and get driver attributes. Palette ObjectDescriptionGet Driver AttributeGets the value of an attribute from the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-suppl

### Advanced VIs

Use the Advanced VIs to read and write the DeviceNet Explicit Messages and to set and get driver attributes.

| Palette Object | Description |
| --- | --- |
| Get Driver Attribute | Gets the value of an attribute from the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-supplied information. |
| Open CAN Frame Read | Opens a CAN Frame Read Object and returns a handle of this object. You can use this handle to read the raw CAN frames in the Read CAN Frame VI. |
| Read CAN Frame | Reads a CAN frame on a DeviceNet interface. |
| Read DeviceNet Explicit Message | Reads an Explicit Message response from an Explicit Messaging Object. |
| Set Driver Attribute | Sets the value of an attribute in the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-supplied information. |
| Write CAN Frame | Sends a CAN frame on the DeviceNet bus. Use this VI to implement advanced CAN applications. |
| Write DeviceNet Explicit Message | Writes an Explicit Message request using an Explicit Messaging Object. |

| Subpalette | Description |
| --- | --- |
| Function Block | Use the DeviceNet Explicit Message Function Block and DeviceNet device for your project. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=close-object-vi.html language=enus -->
## TOPIC 00002: Close Object VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `close-object-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/close-object-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Closes a DeviceNet object. When you use this VI to close an open DeviceNet object, the NI-Industrial Communications for DeviceNet software stops all DeviceNet communication on that object. Details object handle in specifies the object handle of the object that you want

### Close Object VI

**Owning Palette:** DeviceNet VIs

Closes a DeviceNet object. When you use this VI to close an open DeviceNet object, the NI-Industrial Communications for DeviceNet software stops all DeviceNet communication on that object.

Details

[IMAGE alt='image' src='images/Close_Object.gif']

|  | object handle in specifies the object handle of the object that you want to close. The object can be an open Interface Object, an Explicit Messaging Object, an I/O Object, or a CAN Frame Read Object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Close Object Details

Do not close the Explicit Messaging Objects or I/O Objects before stopping the objects. Close the Interface Object in any mode. If you close an Interface Object, NI-IndCom for DeviceNet stops and closes all Explicit Messaging Objects and I/O Objects on this interface.

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=convert-for-devicenet-write-vi.html language=enus -->
## TOPIC 00003: Convert For DeviceNet Write VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `convert-for-devicenet-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/convert-for-devicenet-write-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Converts LabVIEW data to DeviceNet data for writing on a DeviceNet network. byte offset specifies the byte offset in the DeviceNet data in input where the data begins for the DeviceNet data you want to replace. The value ranges from 0 to 255. The default is 0. DeviceNet

### Convert For DeviceNet Write VI

**Owning Palette:** DeviceNet VIs

Converts LabVIEW data to [DeviceNet data](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_type_comparison) for writing on a DeviceNet network.

[IMAGE alt='image' src='images/Convert_For_DeviceNet_Write.gif']

|  | byte offset specifies the byte offset in the DeviceNet data in input where the data begins for the DeviceNet data you want to replace. The value ranges from 0 to 255. The default is 0. |
| --- | --- |
|  | DeviceNet type specifies the DeviceNet data type to convert from the LabVIEW data type. This VI converts the specific LabVIEW data to DeviceNet data accordingly. You can find the LabVIEW data type in parentheses for each DeviceNet data type in the following table. For example, when you select BOOL, this VI converts the byte from an array of eight LabVIEW Booleans to a DeviceNet data type. Use byte offset to indicate this byte. 0BOOL: (8[TF]) (Default)1SINT: (I8)2INT: (I16)3DINT: (I32)4USINT: (U8)5UINT: (U16)6UDINT: (U32)7REAL: (SGL)8LREAL: (DBL)9SHORT_STRING: (String, 0-FF)10STRING: (String, 0-FFFF) |
| 0 | BOOL: (8[TF]) (Default) |
| 1 | SINT: (I8) |
| 2 | INT: (I16) |
| 3 | DINT: (I32) |
| 4 | USINT: (U8) |
| 5 | UINT: (U16) |
| 6 | UDINT: (U32) |
| 7 | REAL: (SGL) |
| 8 | LREAL: (DBL) |
| 9 | SHORT_STRING: (String, 0-FF) |
| 10 | STRING: (String, 0-FFFF) |
|  | DeviceNet data in specifies the initial data bytes that NI-IndCom for DeviceNet reads from the DeviceNet network. The default is 0. |
|  | U32/U16/U8 in specifies the LabVIEW data to convert into DeviceNet data if DeviceNet type is USINT, UINT, or UDINT. The default is 0. |
|  | I32/I16/I8 in specifies the LabVIEW data to convert into DeviceNet data if DeviceNet type is SINT, INT, or DINT. The default is 0. |
|  | 8 [TF] in specifies a LabVIEW array of eight booleans. If DeviceNet type is BOOL, this input provides the LabVIEW data to convert into a DeviceNet data member. You can index into this array to change specific Boolean members. The Boolean at index zero is the least significant bit (bit 0); the Boolean at index one is the second least significant (bit 1); and so on. The default is FALSE. |
|  | DBL/SGL in specifies the LabVIEW data to convert into DeviceNet data if DeviceNet type is REAL or LREAL. The default is 0.00. |
|  | string in specifies the LabVIEW data to convert into DeviceNet data if DeviceNet type is SHORT_STRING or STRING. The default is an empty string. Use SHORT_STRING when the length of your string ranges from 0 to FF. Use STRING when the length of your string ranges from 0 to FFFF. |
|  | DeviceNet data out returns the DeviceNet data bytes with the original DeviceNet data and the new data converted from LabVIEW data. Use the Write DeviceNet IO VI, the Set DeviceNet Attribute VI, or the Write DeviceNet Explicit Message VI to write these data bytes on the DeviceNet network. If you need to convert the LabVIEW data types to multiple DeviceNet data types, you can also wire this output to the DeviceNet data in input of a subsequent use of this VI. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=convert-from-devicenet-read-vi.html language=enus -->
## TOPIC 00004: Convert From DeviceNet Read VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `convert-from-devicenet-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/convert-from-devicenet-read-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Converts DeviceNet data from the DeviceNet network to LabVIEW data. DeviceNet data in specifies the initial data bytes that NI-IndCom for DeviceNet reads from the DeviceNet network. If you need to convert multiple DeviceNet data types to the LabVIEW data types, you can

### Convert From DeviceNet Read VI

**Owning Palette:** DeviceNet VIs

Converts DeviceNet data from the DeviceNet network to [LabVIEW data](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_type_comparison).

[IMAGE alt='image' src='images/Convert_From_DeviceNet_Read.gif']

|  | DeviceNet data in specifies the initial data bytes that NI-IndCom for DeviceNet reads from the DeviceNet network. If you need to convert multiple DeviceNet data types to the LabVIEW data types, you can wire this input to DeviceNet data out of a previous instance of this VI. The default is 0. |
| --- | --- |
|  | DeviceNet type specifies the DeviceNet data type to convert. This VI converts DeviceNet data to the specific LabVIEW data accordingly. You can see the LabVIEW data type in parentheses for each DeviceNet data type in the following table. For example, when you select the DeviceNet data type BOOL, this VI converts the byte to an array of eight LabVIEW Booleans. Use byte offset to indicate this byte. 0BOOL: (8[TF]) (Default)1SINT: (I8)2INT: (I16)3DINT: (I32)4USINT: (U8)5UINT: (U16)6UDINT: (U32)7REAL: (SGL)8LREAL: (DBL)9SHORT_STRING: (String, 0-FF)10STRING: (String, 0-FFFF) |
| 0 | BOOL: (8[TF]) (Default) |
| 1 | SINT: (I8) |
| 2 | INT: (I16) |
| 3 | DINT: (I32) |
| 4 | USINT: (U8) |
| 5 | UINT: (U16) |
| 6 | UDINT: (U32) |
| 7 | REAL: (SGL) |
| 8 | LREAL: (DBL) |
| 9 | SHORT_STRING: (String, 0-FF) |
| 10 | STRING: (String, 0-FFFF) |
|  | byte offset specifies the offset byte in DeviceNet data in where the data begins. The value ranges from 0 to 255. The default is 0. |
|  | string out returns the converted DeviceNet data if the DeviceNet type is SHORT_STRING or STRING. Use SHORT_STRING when the length of your string ranges from 0 to FF. Use STRING when the length of your string ranges from 0 to FFFF. |
|  | DeviceNet data out returns the unchanged DeviceNet data bytes passed through the VI from DeviceNet data in. |
|  | U32/U16/U8 out returns the converted DeviceNet data if DeviceNet type is USINT, UINT, or UDINT. |
|  | I32/I16/I8 out returns the converted DeviceNet data if DeviceNet type is SINT, INT, or DINT. |
|  | 8 [TF] out returns the converted DeviceNet data if DeviceNet type is BOOL. The LabVIEW data type for this output terminal is an array of eight LabVIEW Booleans. You can index into this array to use specific Boolean members. The Boolean at index zero is the least significant bit (bit 0); the Boolean at index one is the next least significant (bit 1); and so on. |
|  | DBL/SGL out returns the converted DeviceNet data if DeviceNet type is REAL or LREAL. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=device-state-page.html language=enus -->
## TOPIC 00005: Device State Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `device-state-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/device-state-page.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Device State Page provides the state of each device added to the master interface. This page contains the following properties: Address—The DeviceNet address of the device. Name—The name of the slave device. State—The current slave device online state: Connected or Disconnected.

### Device State Page

The **Device State Page** provides the state of each device added to the master interface.

This page contains the following properties:

- Address —The DeviceNet address of the device.
- Name —The name of the slave device.
- State —The current slave device online state: Connected or Disconnected.

Parent topic:

DeviceNet Master Interface Online Test Panel

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=device-state-page2.html language=enus -->
## TOPIC 00006: Device State Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `device-state-page2.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/device-state-page2.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides the DeviceNet slave device online state, and includes the following items: Address—Displays the DeviceNet address of the slave device. Name—Displays the name of the slave device. State—Displays current slave device online state: Connected or Disconnected. Verify the device—Verifie

### Device State Page

This page provides the DeviceNet slave device online state, and includes the following items:

- Address —Displays the DeviceNet address of the slave device.
- Name —Displays the name of the slave device.
- State —Displays current slave device online state: Connected or Disconnected.
- Verify the device —Verifies whether the device supports the I/O connection type that the EDS file claims.
- Verification Results —Displays the result of Verify the device .

Parent topic:

DeviceNet Slave Device Online Test Panel

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-basic-page.html language=enus -->
## TOPIC 00007: DeviceNet:Basic Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-basic-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-basic-page.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides basic DeviceNet master properties. The following table describes each property on the page. Property Description AccessAddress The DeviceNet address of the interface. Read/writeBaud Rate The baud rate of the interface. Read/write

### DeviceNet:Basic Page

This page provides basic DeviceNet master properties.

The following table describes each property on the page.

| Property | Description | Access |
| --- | --- | --- |
| Address | The DeviceNet address of the interface. | Read/write |
| Baud Rate | The baud rate of the interface. | Read/write |

Parent topic:

DeviceNet Master Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-basic-page2.html language=enus -->
## TOPIC 00008: DeviceNet:Basic Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-basic-page2.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-basic-page2.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page allows you to set the address of the slave device. The following table describes each property. Property Description AccessAddress The DeviceNet address of the slave device. Read/write

### DeviceNet:Basic Page

This page allows you to set the address of the slave device.

The following table describes each property.

| Property | Description | Access |
| --- | --- | --- |
| Address | The DeviceNet address of the slave device. | Read/write |

Parent topic:

DeviceNet Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-change-slave-address-dialog-box.html language=enus -->
## TOPIC 00009: DeviceNet Change Slave Address Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-change-slave-address-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-change-slave-address-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DeviceNet Change Slave Address dialog box allows you to change a slave device address. The dialog box contains the following properties: Property Description AccessDevice List Lists all of the devices connected to the master interface. This property allows you to select the device you want to se

### DeviceNet Change Slave Address Dialog Box

The **DeviceNet Change Slave Address** dialog box allows you to [change a slave device address](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_cfg_changeslaveaddress). The dialog box contains the following properties:

| Property | Description | Access |
| --- | --- | --- |
| Device List | Lists all of the devices connected to the master interface. This property allows you to select the device you want to set. | Read/write |
| New Address | Lists the new addresses to which you can set your device. | Read/write |

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-change-slave-baud-rate-dialog-box.html language=enus -->
## TOPIC 00010: DeviceNet Change Slave Baud Rate Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-change-slave-baud-rate-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-change-slave-baud-rate-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DeviceNet Change Slave Baud Rate dialog box allows you to change a slave device baud rate. This dialog box contains the following properties: Property Description AccessDevice List Lists all of the devices connected to the master interface. This property allows you to select the device you want

### DeviceNet Change Slave Baud Rate Dialog Box

The **DeviceNet Change Slave Baud Rate** dialog box allows you to [change a slave device baud rate](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_cfg_changeslavebaudrate). This dialog box contains the following properties:

| Property | Description | Access |
| --- | --- | --- |
| Device List | Lists all of the devices connected to the master interface. This property allows you to select the device you want to set. | Read/write |
| New Baud Rate | Lists the baud rates to which you can set your device. | Read/write |

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-datasheet-dialog-box.html language=enus -->
## TOPIC 00011: DeviceNet Datasheet Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-datasheet-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-datasheet-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DeviceNet Datasheet dialog box allows you to import a device datasheet. This dialog box contains the following properties: Property Description AccessData Sheet List Lists the current data sheet files according to the vendor and product type. Select the file that matches your slave device and ad

### DeviceNet Datasheet Dialog Box

The **DeviceNet Datasheet** dialog box allows you to [import a device datasheet](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_cfg_importdatasheet). This dialog box contains the following properties:

| Property | Description | Access |
| --- | --- | --- |
| Data Sheet List | Lists the current data sheet files according to the vendor and product type. Select the file that matches your slave device and add other valid data sheet files into the device tree. | Read/write |
| Vendor | Indicates the vendor name of the device. | Read |
| Type | Indicates the type of the device. | Read |
| Product | Indicates the product name of the device. | Read |
| Revision | Indicates the revision of the device. | Read |
| Data Sheet | Indicates the data sheet filename of the device. | Read |
| Add Files | Adds new data sheet files into the Data Sheet List. | Write |

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-device.html language=enus -->
## TOPIC 00012: DeviceNet Device

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-device.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A DeviceNet Device represents a DeviceNet slave device connected to your DeviceNet master interface device. The DeviceNet Explicit Message Function Block uses this I/O control. Create a DeviceNet device and function block from the Function Block palette. You can also drag a project slave device item

### DeviceNet Device

A DeviceNet Device represents a DeviceNet slave device connected to your DeviceNet master interface device. The [DeviceNet Explicit Message Function Block](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_api_fb_expmsg) uses this I/O control.

Create a DeviceNet device and function block from the [Function Block palette](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_functionb). You can also drag a project slave device item and drop it onto the front panel or block diagram to create an I/O constant. When you click the **Browse** button for the I/O control, you get a list of all the slave items under the same target in the same project. If a VI does not belong to the same target in the same project, or the related target has no slave device items, no list appears.

Parent topic:

Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-explicit-message-function-block.html language=enus -->
## TOPIC 00013: DeviceNet Explicit Message Function Block

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-explicit-message-function-block.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-explicit-message-function-block.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A DeviceNet Explicit Message Function Block is an asynchronous module that finishes the Explicit Message operations that take a long time to complete. Create and use a DeviceNet Explicit Message Function Block from the LabVIEW palette. error in (no error) describes error conditions that occur before

### DeviceNet Explicit Message Function Block

A DeviceNet Explicit Message Function Block is an asynchronous module that finishes the Explicit Message operations that take a long time to complete. Create and [use a DeviceNet Explicit Message Function Block](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_getstarted_step_06) from the LabVIEW [palette](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_api_palette).

[IMAGE alt='image' src='images/dnet_lv_api_FB.png']

|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | execute specifies the action for the function block to run when a rising edge occurs, if the function block is not already executing an operation. A rising edge occurs when the function block was previously invoked with execute set to FALSE and then invoked again with execute set to TRUE. This condition also occurs when the function block is invoked for the first time with execute set to TRUE. |
|  | device in specifies the refnum that identifies the slave device object. |
|  | request service code specifies the service code being requested. The device vendor provides documentation for the vendor-specific service codes. |
|  | class id specifies the class which contains the attribute. The value ranges from 0 to FFFF. Although the DeviceNet Specification allows 16-bit class IDs, most class IDs are 8-bit. NI-IndCom for DeviceNet uses the class ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | instance id specifies the instance which contains the attribute. The value ranges from 0 to FFFF hex. You can use instance ID 0 to get an attribute from the class. Other instance IDs typically start at 1. For example, the primary Identity Object in a device uses instance ID 1. Although the DeviceNet Specification allows 16-bit instance IDs, most instance IDs are 8-bit. NI-IndCom for DeviceNet uses the class ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | request data specifies the service data bytes for the request. The format of this data is specific to service code that you used. For object-specific service codes, the object specification defines the format of the data. For vendor-specific service codes, the device vendor defines the format of the data. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | done returns TRUE only when the function block completes execution on success or error condition. done can also return TRUE if error in contains an error condition and execute is TRUE. |
|  | device out returns the refnum that identifies the slave device object. |
|  | response service code returns the service response as either success or error. Refer to the DeviceNet Specification for more information about service code. Although the DeviceNet Specification requires the high bit of the service code (hex 80) to be set in all Explicit Message responses, NI-IndCom for DeviceNet clears this response indicator so that you can compare the actual service code to the value used with the Write DeviceNet Explicit Message VI. |
|  | response data returns the service data bytes from response. If the response shows a success, these bytes are formatted as the service defines. If the response shows en error, the first byte (service data[0]) contains a General Error Code, and the second byte (service data[1]) contains an Additional Code. Either the DeviceNet Specification or the object itself defines the error codes. |

Parent topic:

Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-i-o-configuration-page.html language=enus -->
## TOPIC 00014: DeviceNet: I/O Configuration Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-i-o-configuration-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-i-o-configuration-page.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page allows you to configure the I/O connection settings. You can select the following items to configure poll mode according to your needs: Scanner—Sets a foreground rate for each polled I/O connection to the same value used for all strobed I/O. This option also allows you to set a background

### DeviceNet: I/O Configuration Page

This page allows you to configure the I/O connection settings. You can select the following items to configure [poll mode](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_poll_mode) according to your needs:

- Scanner —Sets a foreground rate for each polled I/O connection to the same value used for all strobed I/O. This option also allows you to set a background rate for all polled I/O.
  - Foreground Expected Packet Rate(ms) —Sets the expected rate, in milliseconds, of messages used for all strobed I/O. Devices in this group generally respond quickly to poll commands or have data that changes relatively quickly.
  - Foreground to Background Poll Ratio —Sets the background poll rate as an exact multiple of the foreground poll rate. Devices in this group generally respond slowly to poll commands or have data that changes relatively slowly.
- Individual —Sets the expected packet rate to the same value used for all strobed I/O. This option also allows you to set an individual rate for each polled I/O.
  - Strobe Expected Packet Rate(ms) —Indicates the rate of messages, in milliseconds, used for all strobed I/O.

Parent topic:

DeviceNet Master Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-i-o-configuration-page2.html language=enus -->
## TOPIC 00015: DeviceNet:I/O Configuration Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-i-o-configuration-page2.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-i-o-configuration-page2.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page allows you to enable slave device I/O connections and configure I/O variables. The page includes the following items: I/O Connection—Determines the I/O connection type supported by the slave device. Type—Enables one I/O connection by selecting a supported I/O connection type. Disable the I

### DeviceNet:I/O Configuration Page

This page allows you to enable slave device I/O connections and configure I/O variables.

The page includes the following items:

- I/O Connection —Determines the I/O connection type supported by the slave device.
  - Type —Enables one I/O connection by selecting a supported I/O connection type. Disable the I/O connection by selecting None .
  - Expected Packet Rate(ms) —Determines the expected packet rate (EPR) for the I/O connection. Depending on the interface poll mode configuration and the I/O connection type, the EPR may be read-only or writable.
  - Description —Provides the description of the selected I/O connection type from the data sheet.
- I/O Variables —Configures I/O variables for the selected I/O connection.
  - Variables —Lists the input or output connection belonging to the selected I/O connection type. Select an input or output connection to add I/O variables under it.
  - Add —Selects this item to access the I/O Item Editor dialog box where you can add new I/O variables for this slave.
  - Edit —Selects an I/O variable and click this button to access the I/O Item Editor dialog box, where you can change the name, Data Type, and position of the I/O variable.
  - Remove —Selects an I/O variable and click this button to remove the selected I/O variable.
  - Overview —Provides the I/O layout map for the selected I/O connection.

Parent topic:

DeviceNet Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-i-o-item-editor-dialog-box.html language=enus -->
## TOPIC 00016: DeviceNet I/O Item Editor Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-i-o-item-editor-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-i-o-item-editor-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DeviceNet I/O Item Editor dialog box allows you to edit DeviceNet I/O variables. This dialog box contains the following properties: Property Description AccessName The name of the I/O variable. Read/writeData Type The data type of the I/O variable. Read/writeSize(in bits) The number of bits in t

### DeviceNet I/O Item Editor Dialog Box

The **DeviceNet I/O Item Editor** dialog box allows you to edit DeviceNet I/O variables. This dialog box contains the following properties:

| Property | Description | Access |
| --- | --- | --- |
| Name | The name of the I/O variable. | Read/write |
| Data Type | The data type of the I/O variable. | Read/write |
| Size(in bits) | The number of bits in the I/O variable. | Read/write |
| I/O Mapping Overview | Provides an overview of the mappings between I/O variables and the physical channels of the slave device. | Read |
| Move Up | Moves up the start location of the I/O variable in the I/O Mapping Overview. | Write |
| Move Down | Moves down the start location of the I/O variable in the I/O Mapping Overview. | Write |

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-master-interface-online-test-panel.html language=enus -->
## TOPIC 00017: DeviceNet Master Interface Online Test Panel

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-master-interface-online-test-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-master-interface-online-test-panel.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This panel indicates the state of the devices added into the interface. Right-click the DeviceNet master item and select Utilities»Online Test Panel to display the DeviceNet Master Interface Online Test Panel dialog box. The DeviceNet Master Interface Online Test Panel dialog box includes the Device

### DeviceNet Master Interface Online Test Panel

This panel indicates the state of the devices added into the interface. Right-click the DeviceNet master item and select **Utilities»Online Test Panel** to display the **DeviceNet Master Interface Online Test Panel** dialog box.

The **DeviceNet Master Interface Online Test Panel** dialog box includes the [Device State Page](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_env_master_testpanel_state).

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-master-properties-dialog-box.html language=enus -->
## TOPIC 00018: DeviceNet Master Properties Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-master-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-master-properties-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DeviceNet Master Properties dialog box allows you to edit a DeviceNet master device property. To access the dialog box, right-click the DeviceNet master item and select Properties from the shortcut menu. This dialog box includes the following pages: General DeviceNet:Basic DeviceNet:I/O Configur

### DeviceNet Master Properties Dialog Box

The **DeviceNet Master Properties** dialog box allows you to edit a DeviceNet master device property. To access the dialog box, right-click the DeviceNet master item and select **Properties** from the shortcut menu.

This dialog box includes the following pages:

- General
- DeviceNet:Basic
- DeviceNet:I/O Configuration Page

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-master-settings-dialog-box.html language=enus -->
## TOPIC 00019: DeviceNet Master Settings Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-master-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-master-settings-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog box appears after you add a DeviceNet Master, and allows you set the interface, MAC ID, and baud rate of the master. This dialog box contains the following properties: Property Description AccessMaster Interface Indicates current master interface. Read/WriteAddress Displays the DeviceNet

### DeviceNet Master Settings Dialog Box

This dialog box appears after you [add a DeviceNet Master](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_cfg_addmasterintf), and allows you set the interface, MAC ID, and baud rate of the master.

This dialog box contains the following properties:

| Property | Description | Access |
| --- | --- | --- |
| Master Interface | Indicates current master interface. | Read/Write |
| Address | Displays the DeviceNet address of the master. | Read/Write |
| Baud Rate | Displays the baud rate of the master. | Read/Write |
| Discover Option | Determines whether the master scans the devices immediately after adding the master. | Read/Write |

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-option-page.html language=enus -->
## TOPIC 00020: DeviceNet:Option Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-option-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-option-page.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides the following DeviceNet protocol options: Keep the Explicit Messaging connection—Determines whether or not to keep an Explicit Messaging connection open when not in use. Suppress the acknowledgments (COS or Cyclic)—Determines whether acknowledgments are used (FALSE) or suppressed

### DeviceNet:Option Page

This page provides the following DeviceNet protocol options:

- Keep the Explicit Messaging connection —Determines whether or not to keep an Explicit Messaging connection open when not in use.
- Suppress the acknowledgments (COS or Cyclic) —Determines whether acknowledgments are used (FALSE) or suppressed (TRUE) in COS or Cyclic I/O connections.
- Minimum delay time between subsequent data productions (COS) —Configures the minimum delay time between subsequent data productions and can limit the amount of network traffic used for COS messages from devices with frequently changing I/O. This attribute applies only to COS I/O connections. The value is provided in milliseconds.

Parent topic:

DeviceNet Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-parameter-editor-dialog-box.html language=enus -->
## TOPIC 00021: DeviceNet Parameter Editor Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-parameter-editor-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-parameter-editor-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To edit a DeviceNet parameter, double-click the parameter, or select Edit on one parameter in the Property:Parameters list or the Online Test Panel:Parameters list. The DeviceNet Parameter Editor dialog box appears. You can edit the selected parameters in this dialog box. If a parameter is read only

### DeviceNet Parameter Editor Dialog Box

Edit

Property:Parameters

Online Test Panel:Parameters

DeviceNet Parameter Editor

Note

publish list

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-parameter-publish-option-dialog-box.html language=enus -->
## TOPIC 00022: DeviceNet Parameter Publish Option Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-parameter-publish-option-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-parameter-publish-option-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog box contains the following lists: Parameter listâLists the parameters that are not read only. You do not write these parameters to the slave device. Publish to DeviceNetâLists the parameters that are not read only. You do not write these parameters to the slave device when the Scan E

### DeviceNet Parameter Publish Option Dialog Box

This dialog box contains the following lists:

- Parameter list âLists the parameters that are not read only. You do not write these parameters to the slave device.
- Publish to DeviceNet âLists the parameters that are not read only. You do not write these parameters to the slave device when the Scan Engine mode changes from Configuration to Active.

Use **Add**, **Add All**, **Remove**, and **Remove All** buttons to configure which parameter is in the publish list.

- Publishing One Parameter to the Publish ListâSelects one parameter from the parameter list, clicks the Add button to remove that parameter from the parameter list, and adds it to Publish to DeviceNet .
- Publishing All Parameters to the Publish ListâClicks the Add All button to remove all parameters from the parameter list and adds them to Publish to DeviceNet .
- Removing One Parameter from the Publish ListâSelects one parameter in the Publish to DeviceNet list and clicks the Remove button. You can also remove the selected parameter from the Publish to DeviceNet list and add to the parameter list.
- Removing All Parameters from the Publish ListâClicks the Remove All button to remove all parameters from the Publish to DeviceNet and those added to the parameter list.

Note

Parameter Editor

Online Test Panel:Parameters

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-parameters-page.html language=enus -->
## TOPIC 00023: DeviceNet:Parameters Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-parameters-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-parameters-page.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides slave device parameter information. You can perform online access to the slave parameters from this page. The dialog box includes the following items: Category—This item allows you to choose the type of parameters to show from the pull-down menu. The default is to show all paramet

### DeviceNet:Parameters Page

This page provides slave device parameter information. You can perform online access to the slave parameters from this page.

The dialog box includes the following items:

- Category —This item allows you to choose the type of parameters to show from the pull-down menu. The default is to show all parameters.
- The parameter numeric value is shown in hexadecimal —If this is checked, the parameter value is shown in hexadecimal format. If this is unchecked, the parameter value is shown in decimal format.
- Parameters —The slave device parameters, including the following columns:
 Property Description Access#
The parameter number.
Read onlyFlag
If the parameter is read-only, the flag value is R. If the parameter supports scaling, the flag value is S, which means the indicated parameter value is calculated by the scaling expression listed in the parameter description.
Read onlyParameter
The parameter name.
Read onlyValue
The parameter value. This value can not be changed if the R flag is set.
Read/WriteUnit
The unit of the parameter value.
Read onlyType
The type of the parameter value, such as BOOL, BYTE, INT, SINT, UINT, USINT, etc.
Read onlySize
The size of the parameter value.
Read onlyClassID
The class ID of the parameter.
Read onlyInstanceID
The instance ID of the parameter.
Read onlyAttributeID
The attribute ID of the parameter.
Read only
- Edit —Click this button to access the Parameter Editor dialog box where you can edit the parameter values.
- Publish Option —Click this button to access the DeviceNet Parameter Publish Option dialog box where you can configure the parameters and publish these parameters to DeviceNet.
- Parameter Description —Provides a detailed description of the selected parameter.

Changes to parameters on this page only change the [project data](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_scanengine_3data).

To read or write the connected slave device parameter directly, use the [DeviceNet Slave Device Online Test Panel](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_env_slave_testpanel_dlg).

Parent topic:

DeviceNet Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-parameters-page2.html language=enus -->
## TOPIC 00024: DeviceNet: Parameters Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-parameters-page2.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-parameters-page2.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides slave device parameter information. You can access slave parameters online from this page. The dialog box includes the following items: CategoryâChoose which types of parameters to show from the pull-down menu. The default is to show all parameters. Show the parameter numeric va

### DeviceNet: Parameters Page

This page provides slave device parameter information. You can access slave parameters online from this page.

The dialog box includes the following items:

- Category âChoose which types of parameters to show from the pull-down menu. The default is to show all parameters.
- Show the parameter numeric value in hex âPlace a checkmark to display the parameter value in hexadecimal format; or remove the checkmark to display the parameter value in decimal format.
- Parameters âThe slave device parameters include the following columns:
 Property Description Access#
The parameter number.
Read onlyFlag
If the parameter is read-only, the flag value is **R**. If the parameter supports scaling, the flag value is **S**, which means the indicated parameter value is calculated by the scaling expression listed in the parameter description.
Read onlyParameter
The parameter name.
Read onlyValue
The parameter value. The user can not change this value if the **R** flag is set.
Read/WriteUnit
The unit of the parameter value.
Read onlyType
The type of the parameter value, such as BOOL, BYTE, INT, SINT, UINT, USINT, etc.
Read onlySize
The size of the parameter value.
Read onlyClassID
The class ID of the parameter.
Read onlyInstanceID
The instance ID of the parameter.
Read onlyAttributeID
The attribute ID of the parameter.
Read only
- Edit âClicks this button to access the Parameter Editor dialog box where you can edit the parameter values.
- Publish Option âClicks this button to access the DeviceNet Parameter Publish Option dialog box.
- Online Access âRead or write the device parameters directly.
  - Scope âChooses All to read or write all of the parameters. Choose Selected to upload or deploy the selected parameter.
  - Read âClicks this button to read the parameters from the DeviceNet slave device.
  - Write âClicks this button to write the selected parameters to the DeviceNet slave device.
- Parameter Description âProvides a detailed description of the selected parameter.

Note

DeviceNet Explicit Message function block

importing a device datasheet

Parent topic:

DeviceNet Slave Device Online Test Panel

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-slave-device-online-test-panel.html language=enus -->
## TOPIC 00025: DeviceNet Slave Device Online Test Panel

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-slave-device-online-test-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-slave-device-online-test-panel.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the DeviceNet slave device item and select Utilities»Online Test Panel to display the DeviceNet Slave Device Online Test Panel dialog box. Click the OK button to save the parameter values to the LabVIEW project data. This dialog box includes the following pages: Device State DeviceNet:Pa

### DeviceNet Slave Device Online Test Panel

Right-click the [DeviceNet slave device item](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_env_item) and select **Utilities»Online Test Panel** to display the **DeviceNet Slave Device Online Test Panel** dialog box. Click the **OK** button to save the parameter values to the LabVIEW project data.

This dialog box includes the following pages:

- Device State
- DeviceNet:Parameters

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-slave-device-properties-dialog-box.html language=enus -->
## TOPIC 00026: DeviceNet Slave Device Properties Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-slave-device-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-slave-device-properties-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the DeviceNet slave device item and select Properties to display the DeviceNet Slave Device Properties dialog box. This dialog box includes the following pages: General DeviceNet:Basic DeviceNet:Option DeviceNet:Parameters DeviceNet:I/O Configuration

### DeviceNet Slave Device Properties Dialog Box

Right-click the [DeviceNet slave device item](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_proj_env_item) and select **Properties** to display the **DeviceNet Slave Device Properties** dialog box.

This dialog box includes the following pages:

- General
- DeviceNet:Basic
- DeviceNet:Option
- DeviceNet:Parameters
- DeviceNet:I/O Configuration

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-slave-settings-dialog-box.html language=enus -->
## TOPIC 00027: DeviceNet Slave Settings Dialog Box

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-slave-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-slave-settings-dialog-box.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog box allows you to designate slave settings including Media Access Control Identifier (MAC ID) and Electronic Data Sheets (EDS). The dialog box includes the following items: Address—The DeviceNet address of the slave device. Data Sheet—The EDS file for this slave. You may specify the EDS

### DeviceNet Slave Settings Dialog Box

This dialog box allows you to designate slave settings including Media Access Control Identifier (MAC ID) and Electronic Data Sheets (EDS).

The dialog box includes the following items:

- Address —The DeviceNet address of the slave device.
- Data Sheet —The EDS file for this slave. You may specify the EDS data sheet for the slave device by clicking the Browse button to access the DeviceNet Datasheet dialog box and choosing the appropriate EDS file through that dialog box.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet-vis.html language=enus -->
## TOPIC 00028: DeviceNet VIs

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet-vis.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DeviceNet VIs to control and configure DeviceNet devices on a DeviceNet network. Palette ObjectDescriptionClose ObjectCloses a DeviceNet object. When you use this VI to close an open DeviceNet object, the NI-Industrial Communications for DeviceNet software stops all DeviceNet communication o

### DeviceNet VIs

Use the DeviceNet VIs to control and configure DeviceNet devices on a DeviceNet network.

| Palette Object | Description |
| --- | --- |
| Close Object | Closes a DeviceNet object. When you use this VI to close an open DeviceNet object, the NI-Industrial Communications for DeviceNet software stops all DeviceNet communication on that object. |
| Convert For DeviceNet Write | Converts LabVIEW data to DeviceNet data for writing on a DeviceNet network. |
| Convert From DeviceNet Read | Converts DeviceNet data from the DeviceNet network to LabVIEW data. |
| Easy IO Close | Closes an Interface Object and multiple device objects. |
| Easy IO Config | Configures and starts an Interface Object and multiple I/O Objects. This VI also returns the Interface Object and device object handles for all the other objects. |
| Get DeviceNet Attribute | Gets an attribute value from a DeviceNet device using an Explicit Messaging Object and executes the Get Attribute Single service on a remote DeviceNet device. |
| Open DeviceNet Explicit Messaging | Configures and opens an Explicit Messaging Object and returns a handle of this object. |
| Open DeviceNet Interface | Configures and opens an Interface Object and returns a handle of this object. You must open an Interface Object before you start any application on the real-time CompactRIO controller. Before you open the interface, a delay occurs due to a loading process for a few seconds. This process establishes communications between the controller and the NI-Industrial Communications for DeviceNet module. |
| Open DeviceNet IO | Configures and opens an I/O Object and returns a handle of this object. |
| Operate DeviceNet Interface | Performs an operation on an Interface Object. |
| Read DeviceNet IO | Reads input data from an I/O Object. |
| Set DeviceNet Attribute | Sets an attribute value for a DeviceNet device using an Explicit Messaging Object and executes the Set Attribute Single service on a remote DeviceNet device. |
| Wait For State | Waits for the Established state or the Read Avail state of an Explicit Messaging Object, an I/O Object, or a CAN Frame Read Object. |
| Write DeviceNet IO | Writes output data to an I/O Object. |

| Subpalette | Description |
| --- | --- |
| Advanced VIs | Use the Advanced VIs to read and write the DeviceNet Explicit Messages and to set and get driver attributes. |

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=devicenet_intro.html language=enus -->
## TOPIC 00029: NI-Industrial Communications for DeviceNet Programming Reference Manual

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `devicenet_intro.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/devicenet_intro.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-Industrial Communications for DeviceNet Programming Reference Manual provides information about the DeviceNET VIs and error codes.

### NI-Industrial Communications for DeviceNet Programming Reference Manual

The NI-Industrial Communications for DeviceNet Programming Reference Manual provides information about the DeviceNET VIs and error codes.

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=easy-io-close-vi.html language=enus -->
## TOPIC 00030: Easy IO Close VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `easy-io-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/easy-io-close-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Closes an Interface Object and multiple device objects. This VI stops an Interface Object, closes all the object handles passed in device object handle in, and then closes the Interface Object. Interface Object handle in specifies an object handle of an open Interface O

### Easy IO Close VI

**Owning Palette:** DeviceNet VIs

Closes an [Interface Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_interface_object) and multiple device objects.

This VI stops an Interface Object, closes all the object handles passed in **device
object handle in**, and then closes the Interface Object.

[IMAGE alt='image' src='images/Easy_IO_Close.gif']

|  | Interface Object handle in specifies an object handle of an open Interface Object. |
| --- | --- |
|  | device object handle in specifies the array of the I/O Objects handles this VI closes. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=easy-io-config-vi.html language=enus -->
## TOPIC 00031: Easy IO Config VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `easy-io-config-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/easy-io-config-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Configures and starts an Interface Object and multiple I/O Objects. This VI also returns the Interface Object and device object handles for all the other objects. To open an Explicit Messaging Object, you need to stop the interface first and then use the Open DeviceNet

### Easy IO Config VI

**Owning Palette:** DeviceNet VIs

Configures and starts an [Interface Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_interface_object) and multiple [I/O Objects](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_io_object). This VI also returns the Interface Object and device object handles for all the other objects.

To open an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message), you need to stop the interface first and then use the Open DeviceNet Explicit Messaging VI separately after using this VI.

[IMAGE alt='image' src='images/Easy_IO_Config.gif']

|  | interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 to 31. You can use NI Measurement & Automation Explorer (MAX) to view the relationship between each interface name and each piece of hardware. |
| --- | --- |
|  | device configuration specifies an array of the I/O Object configuration clusters. This input contains any number of I/O connections that you want to open. device MAC ID specifies the device address of the remote DeviceNet device. The value ranges from 0 to 63. The default is 0. Many devices use physical switches to set the device MAC IDs. For these devices, examine these switches to get the MAC IDs. Many devices use 63 as the factory default. In most cases, you use I/O communication as a master to a remote slave device. When device MAC ID is the MAC ID of the remote DeviceNet slave device, device MAC ID is different from your interface MAC ID. If you want to configure I/O communication as a slave with a remote master, set device MAC ID to the same as interface MAC ID. Set interface MAC ID by using the Open DeviceNet Interface VI. connection type specifies the type of master/slave I/O connection. 0Poll (Default)1Strobe2COS3Cyclic input length specifies the number of bytes that NI-IndCom for DeviceNet reads from the I/O connection. The default is 1. Refer to the Electronic Data Sheets (EDS) from the device vendor for the specific value of input length. The specific input length setting varies for the following connection types: Poll, COS, and Cyclic—The input length is the same as the number of bytes of the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The input length is the same as the number of bytes of the strobe response message. The value ranges from 0 to 8. Strobe as slave—device MAC ID is equal to interface MAC ID. The input length is 1. You can obtain the input data consisting of a single Boolean value in bit from the master's strobe command message by using interface MAC ID.The Read DeviceNet IO VI returns this Boolean value as a single byte. output length specifies the number of bytes written to the I/O connection using the Write DeviceNet IO VI. The default is 1. Refer to the EDS file from the device vendor for the specific value of output length. The specific output length setting varies for the following connection types: Poll, COS, and Cyclic—The output length is the same as the number of bytes consumed from the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The output length is 1. The output data consists of a single Boolean value that passes into the strobe command message using device MAC ID. You can also use this Boolean value in the Write DeviceNet IO VI as a single byte. Strobe as slave—device MAC ID is equal to interface MAC ID. The value ranges from 0 to 8, which is the same as the number of bytes produced in the strobe response message. expected packet rate specifies the expected packet rate of I/O message production in milliseconds. The EPR setting only applies to the I/O Objects used for communication as a master. For I/O Objects used for communication as a slave, your device ignores your slave EPR setting, because the remote master determines the EPR on behalf of your slave. The default is 200. The value ranges from 1 to 60,000. The value is a multiple of 4. If the value is not a multiple of 4, NI-IndCom of DeviceNet rounds up the value to a multiple of 4. For example, if the value is 5 or 6, NI-IndCom for DeviceNet rounds up the value to 8. If the value is 1 or 2, NI-IndCom for DeviceNet rounds up the value to 4. You can use the Get Driver Attribute VI to get the actual EPR you use after the interface starts. |
|  | device MAC ID specifies the device address of the remote DeviceNet device. The value ranges from 0 to 63. The default is 0. Many devices use physical switches to set the device MAC IDs. For these devices, examine these switches to get the MAC IDs. Many devices use 63 as the factory default. In most cases, you use I/O communication as a master to a remote slave device. When device MAC ID is the MAC ID of the remote DeviceNet slave device, device MAC ID is different from your interface MAC ID. If you want to configure I/O communication as a slave with a remote master, set device MAC ID to the same as interface MAC ID. Set interface MAC ID by using the Open DeviceNet Interface VI. |
|  | connection type specifies the type of master/slave I/O connection. 0Poll (Default)1Strobe2COS3Cyclic |
| 0 | Poll (Default) |
| 1 | Strobe |
| 2 | COS |
| 3 | Cyclic |
|  | input length specifies the number of bytes that NI-IndCom for DeviceNet reads from the I/O connection. The default is 1. Refer to the Electronic Data Sheets (EDS) from the device vendor for the specific value of input length. The specific input length setting varies for the following connection types: Poll, COS, and Cyclic—The input length is the same as the number of bytes of the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The input length is the same as the number of bytes of the strobe response message. The value ranges from 0 to 8. Strobe as slave—device MAC ID is equal to interface MAC ID. The input length is 1. You can obtain the input data consisting of a single Boolean value in bit from the master's strobe command message by using interface MAC ID.The Read DeviceNet IO VI returns this Boolean value as a single byte. |
|  | output length specifies the number of bytes written to the I/O connection using the Write DeviceNet IO VI. The default is 1. Refer to the EDS file from the device vendor for the specific value of output length. The specific output length setting varies for the following connection types: Poll, COS, and Cyclic—The output length is the same as the number of bytes consumed from the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The output length is 1. The output data consists of a single Boolean value that passes into the strobe command message using device MAC ID. You can also use this Boolean value in the Write DeviceNet IO VI as a single byte. Strobe as slave—device MAC ID is equal to interface MAC ID. The value ranges from 0 to 8, which is the same as the number of bytes produced in the strobe response message. |
|  | expected packet rate specifies the expected packet rate of I/O message production in milliseconds. The EPR setting only applies to the I/O Objects used for communication as a master. For I/O Objects used for communication as a slave, your device ignores your slave EPR setting, because the remote master determines the EPR on behalf of your slave. The default is 200. The value ranges from 1 to 60,000. The value is a multiple of 4. If the value is not a multiple of 4, NI-IndCom of DeviceNet rounds up the value to a multiple of 4. For example, if the value is 5 or 6, NI-IndCom for DeviceNet rounds up the value to 8. If the value is 1 or 2, NI-IndCom for DeviceNet rounds up the value to 4. You can use the Get Driver Attribute VI to get the actual EPR you use after the interface starts. |
|  | interface configuration specifies configurations for an Interface Object. interface MAC ID specifies the MAC ID of a DeviceNet interface to communicate with other DeviceNet devices. The value ranges from 0 to 63. The default is 0. A device MAC ID indicates the priority of sending DeviceNet messages on the network. The lower numbered MAC ID has the higher priority. Set the MAC ID to 0 if the DeviceNet interface is the only master on the network. baud rate specifies the network baud rate, in bit per second (b/s), the NI-IndCom for DeviceNet uses to communicate with devices. 0125000 (Default)12500002500000 poll mode specifies the communication scheme used for all polled I/O connections in which the interface acts as a master. In poll mode, the interface uses this scheme to transmit poll requests to slave devices. 0Automatic (Default)1Scanned2Individual |
|  | interface MAC ID specifies the MAC ID of a DeviceNet interface to communicate with other DeviceNet devices. The value ranges from 0 to 63. The default is 0. A device MAC ID indicates the priority of sending DeviceNet messages on the network. The lower numbered MAC ID has the higher priority. Set the MAC ID to 0 if the DeviceNet interface is the only master on the network. |
|  | baud rate specifies the network baud rate, in bit per second (b/s), the NI-IndCom for DeviceNet uses to communicate with devices. 0125000 (Default)12500002500000 |
| 0 | 125000 (Default) |
| 1 | 250000 |
| 2 | 500000 |
|  | poll mode specifies the communication scheme used for all polled I/O connections in which the interface acts as a master. In poll mode, the interface uses this scheme to transmit poll requests to slave devices. 0Automatic (Default)1Scanned2Individual |
| 0 | Automatic (Default) |
| 1 | Scanned |
| 2 | Individual |
|  | interface object handle out returns the object handle that passes through this VI as an output that you use this output with all subsequent VIs for the Interface Object. |
|  | device object handle out returns the array of object handles to retrieve individual I/O handles for reading and writing data. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=error-codes.html language=enus -->
## TOPIC 00032: Error Codes

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `error-codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/error-codes.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DeviceNet VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −2147136510 Board self test failed (code 2). Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists

### Error Codes

The DeviceNet VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −2147136510 | Board self test failed (code 2). Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147136509 | Board self test failed (code 3). Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147136508 | Board self test failed (code 4). Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147136507 | Board self test failed (code 5). Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147136506 | Board self test failed (code 6). Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147136505 | The computer goes to the hibernation mode and the board is powered off. Solution: Prevent the computer from going to the hibernation mode by using the control panel. |
| −2147136504 | A Write queue is overflowed. Solution: Wait until queue space becomes available and try again. |
| −2147136503 | The firmware of the board does not answer a command. Solution: Stop your application and execute a self test. Try to deactivate or reactivate the driver in the Device Manager. If the problem persists, contact National Instruments. |
| −2147136502 | The operation is timeout. Solution: Specify a timeout period that is long enough to complete the operation. Or use less time to complete the operation. For example, read less data in an operation. |
| −2147136501 | A Read queue is overflowed. Solution: Reduce your data rate or call Read more frequently. |
| −2147136500 | The Read buffer is too small to hold a single frame. Solution: Provide a buffer that is large enough. |
| −2147136497 | You cannot conduct a self test because the board is in use by an application. Solution: Stop all the DeviceNet applications before executing a self test. |
| −2147136496 | Allocation of memory failed. You do not have enough memory. Solution: Add more RAM or try to use fewer resources in your applications. The resources include IO variables and function blocks. |
| −2147136495 | The maximum number of sessions is exceeded. Solution: Use fewer sessions. |
| −2147136494 | The maximum number of connection objects is exceeded. Solution: Use fewer connection objects in your sessions. |
| −2147136493 | The maximum number of interface devices is detected. Solution: Use fewer devices. |
| −2147136492 | A driver support file is missing. Solution: Try to reinstall the driver. If the error persists, contact National Instruments. |
| −2147136480 | An invalid reference has been passed to a DeviceNet function. Solution: Only pass a reference retrieved from the DeviceNet function or an I/O control name in a LabVIEW project. |
| −2147136479 | An invalid handle has been passed to a DeviceNet system function. Solution: Only pass a valid system handle. |
| −2147136478 | A device handle was expected for a DeviceNet function. Solution: Only pass a device handle. |
| −2147136477 | An interface handle was expected for a DeviceNet function. Solution: Only pass an interface handle. |
| −2147136475 | Create Timing Source VI is not supported on Windows. This VI is supported on LabVIEW Real-Time targets only. |
| −2147136399 | The transceiver value is invalid or you are trying to perform an operation that requires a different transceiver. Solution: Set a valid value. |
| −2147136398 | The baud rate value is invalid. Solution: Set a valid value. |
| −2147136397 | The baud rate value is invalid. Solution: Set a valid value. |
| −2147136396 | The bit timing value is invalid. Solution: Set a valid value. |
| −2147136395 | The baud rate setting does not match the allowed range of the transceiver. Solution: Change the setting of either the baud rate or the transceiver. |
| −2147136394 | The configured timing source is not known by this interface. Solution: Make sure that you pass a valid timing value. |
| −2147136393 | The configured synchronization source is inappropriate for the hardware. Solution: Pick an appropriate timing source for the hardware. |
| −2147136392 | The source that you connected to the Master Timebase destination is missing. When the start trigger is received, the interface verifies that a signal is present on the configured source. This check has determined that this signal is missing. Solution: Verify that your cables are configured correctly and that your timebase source is generating an appropriate waveform. |
| −2147136391 | The source that you connected to the Master Timebase destination is not generating an appropriate signal. When the start trigger is received, the interface verifies that a signal of a known frequency is present on the configured source. This check has determined that this source is generating a signal, but that the signal is not one of the supported frequencies for this hardware. Solution: Verify that your source is generating a signal at a supported frequency. |
| −2147136383 | An invalid parameter has been passed to a DeviceNet VI. For example, a null pointer is passed in. Solution: Check the input parameters and ensure they are valid. You can reference the VI description to know each parameter. |
| −2147136382 | Error occurs when you acquire the driver resource. Solution: Add more RAM or try to use fewer resources in your applications. The resources include IO variables and function blocks. |
| −2147136381 | The operation is timeout. Solution: Specify a timeout period that is long enough to complete the operation or change the operation that can be complete in less time. |
| −2147136380 | The DeviceNet hardware can not be found or has been removed. Solution: 1. Ensure the DeviceNet hardware is correctly installed. 2. Ensure you use the correct port name. Get the port name of your device by using MAX. |
| −2147136368 | The interface name given does not specify a valid and existing interface. Solution: Use a valid and existing interface port name. |
| −2147136367 | The interface name is invalid. Solution: Ensure you use a valid interface name. The name of the DeviceNet interface is an ASCII string with format "DeviceNetx", where x is a decimal number starting at one that indicates which interface is being used. For example, "DeviceNet1", "DeviceNet2", and "DeviceNet32". |
| −2147136366 | The object handle passed in is invalid. Solution: Use a correct object handle returned from the Open DeviceNet Interface VI, the Open DeviceNet Explicit Messaging VI, or the Open DeviceNet IO VI. |
| −2147136365 | The property ID is invalid for the specified object type. Solution: Ensure you use a valid property ID. |
| −2147136364 | A object handle is passed in, but the corresponding object has not been opened or has been closed. Solution: Use an object handle in the following sequence: open, use, and close. |
| −2147136363 | The interface object has not been opened before it is used. Solution: Use an object handle in the following sequence: open, use, and close. |
| −2147136362 | The I/O connection object has not been opened before it is used. Solution: Use an object handle in the following sequence: open, use, and close. |
| −2147136361 | The interface object has not been started. Solution: Start the interface before performing this operation. |
| −2147136360 | The I/O connection input length is not valid. Solution: Use a valid input length. The valid input length for Poll, COS, and Cyclic ranges from 0 to 255. The valid input length for Strobe ranges from 0 to 8. |
| −2147136359 | The I/O connection output length is not valid. Solution: Use a valid output length. The valid output length for Poll, COS, and Cyclic ranges from 0 to 255. The valid output length for Strobe is 1. |
| −2147136358 | The property is get-only and can not be set. Solution: Check the property ID and find out some properties are get-only. |
| −2147136357 | The property is set-only and can not be used to get an attribute. Solution: Check the property ID and find out some properties are set-only. |
| −2147136356 | The property size passed in is not correct. Solution: Check the manual or header file to determine the correct property size. |
| −2147136355 | The property ID and the object handle do not match. For example, the property ID is an I/O connection property, but the object handle passed in is an Explicit Messaging Object. Solution: Use appropriate property ID for the given object type. |
| −2147136354 | This error occurs when you start an EM request or response cycle before the previous cycle finished. At any given time, only one EM request or response cycle is allowed to use a DeviceNet interface port. Solution: Use the following order for the EM request or response: write EM, wait for read available, and read EM. |
| −2147136353 | This error occurs when you try to send an EM request to a slave device but an EM request or response cycle is still pending on another slave device. At any given time, an EM request or response cycle can only pend on a single slave device. Solution: The existing EM request or response cycle on a slave device must end before a new EM request or response cycle starts. |
| −2147136352 | This error occurs when you try to get an EM response from a slave device, but the EM request or response cycle is pending on another slave device. Solution: Ensure an EM request or response cycle is performed on a single slave device in the following order: write EM (Slave 1) , wait for read available, read EM (Slave 1), write EM (Slave 2), wait for read available, and write EM (Slave 2). |
| −2147136350 | The buffer size is not enough for the requested operation. Solution: Ensure the buffer is large enough for the requested operation. |
| −2147136349 | The error occurs when you try to get an EM response, but you have not sent out an request. Solution: Call the Write DeviceNet Explicit Message VI to send out an request first |
| −2147136347 | The feature requested is not supported in current version. Solution: Only use supported feature. |
| −2147136346 | The property value is invalid. Solution: Ensure the property value is in a valid range. |
| −2147136345 | You try to open two or more types of I/O connections on the same slave device. Solution: Only open one type of I/O connections on a slave device at the same time. Only one type of IO connections can be opened on a slave device at same time. |
| −2147136344 | You try to blink the port LEDs but these LEDs are busy. Solution: Stop all applications that are running on that port. Do not access the applications from MAX or from LabVIEW. |
| −2147136343 | You tried to set a queue size that is bigger than the maximum allowed. Solution: Specify an in-range queue size. |
| −2147136336 | RPC connection is timeout. Solution: Ensure you have correctly configured the ethernet connection between the host and the real-time controller. |
| −2147136335 | The operation is invalid for this DeviceNet interface. Solution: Run this operation on a suitable interface. |
| −2147136334 | The driver is not communicating with the device. Solution: Make sure you connect the device to the computer. |
| −2147136304 | An invalid configuration XML file has been deployed to the target. Solution: Ensure you use LabVIEW to produces a valid configuration file. |
| −2147136288 | The DeviceNet I/O control tag name is invalid. Solution: Enter a valid tag name. |
| −2147136285 | You change the device I/O control tag when the function block is busy. Solution: Do not change the device I/O control tag when the function block is busy. |
| −2147136284 | The EM object handle is invalid. Solution: Ensure the DeviceNet I/O control is opened successfully to make the EM object handle valid. |
| −2147136255 | The firmware receives an unknown service code. Solution: Ensure the service code is predefined. |
| −2147136254 | An object is not in a proper state when you execute some operations. Solution: Ensure the object is in a proper state. |
| −2147136253 | The firmware meets an unknown property code. Solution: Ensure the request property code is predefined. |
| −2147136252 | The user calls a service which is not available at the moment. Solution: Wait a few seconds and call this service again. |
| −2147136251 | Exceeded limit for length of Write DeviceNet Explicit Message. The maximum length of an explicit message request is 240 service data bytes. Solution: Decrease the length of the explicit message request. |
| −2147136250 | EM request data size is too large. Solution: Ensure the EM request data size is valid. |
| −2147136249 | Exceeded limit for length of Read DeviceNet Explicit Message. The maximum length of an explicit message response is 240 service data bytes. The response larger than the maximum length cannot be handled. Solution: Configure the device to return a response of a smaller size. |
| −2147136247 | A Bus Off error occurs on the bus. Solution: Clear the Bus Off error physically and wait for the firmware to recover from this error automatically. |
| −2147136224 | The EM established is timeout. Solution: Specify a timeout period that is long enough to establish the EM connection or check whether the slave is connected. |
| −2147136223 | An internal error occurs in the firmware. Solution: Try to reinstall the driver or switch the slot(s) of the board(s). If the error persists, contact National Instruments. |
| −2147136221 | The object is already open in another application. Solution: Ensure that only one application at a time uses an object , and that you close all objects prior to exiting your application |
| −2147136220 | The DeviceNet Interface Object is already open with a different Poll Mode. Or you used the automatic Poll Mode and opened an I/O connection after start. Solutions: Match all Poll Mode parameters. Or stop communication before trying to add I/O connections. |
| −2147136219 | You tried to open a DeviceNet COS I/O connection with a Cyclic I/O connection. The Cyclic I/O connection is already open for that device. Solution: COS and Cyclic connections are mutually exclusive, so you can only open one type for a given device. |
| −2147136218 | CAN bus problems caused all communications to stop. This error corresponds to Bus Off state. Solution: Verify the following issues: cabling is correct; devices are connected and operational; proper bus power is applied. |
| −2147136217 | Exceeded resource limit for DeviceNet I/O tables. Solution: Decrease the number of slave device I/O connections; Decrease the Input Length or Output Length used for a given I/O Object. |
| −2147136214 | You try to use the Write DeviceNet Explicit Message VI before a response from a previous Write arrives. Only one explicit message can be pending. Solution: Complete a Write, Wait, and Read circle before sending another Write DeviceNet Explicit Message request. |
| −2147136213 | The DeviceNet duplicate MAC ID check fails for the Interface Object. Solution: Determine an unused MAC ID in your DeviceNet system and use that MAC ID for Open DeviceNet Interface. |
| −2147136212 | Miscellaneous device initialization error. Solution: Verify that the configuration specified in Open functions matches the capabilities of your device. |
| −2147136211 | DeviceNet device does not initialize due to unsupported connection types. For example, if the device only supports Strobed I/O, but you configure Polled I/O for this device. This error occurs. Solution: Refer to the device documentation for valid connection types. |
| −2147136210 | DeviceNet device does not initialize due to unsupported Expected Packet Rate (EPR). Solution: Some devices place a lower or upper limit on the EPR. Adjust the EPR if an overflow or underflow occurs. |
| −2147136209 | DeviceNet device does not initialize because the vendor ID of the device differs from the driver attribute. Solution: If you replaced the device, use the new vendor ID as the driver attribute. If you do not want to verify the ID, do not set the driver attribute. |
| −2147136208 | DeviceNet device does not initialize because the device type of the device differs from the driver attribute. Solution: If you replaced the device, use the new device type as the driver attribute. If you do not want to verify the type, do not set the driver attribute. |
| −2147136207 | DeviceNet device does not initialize because the product code of the device differs from the driver attribute. Solution: If you replaced the device, use the new product code as the driver attribute. If you do not want to verify the code, do not set the driver attribute. |
| −2147136206 | DeviceNet device not found. A connection could not be established with the MAC ID specified in the Open function. Solution: Verify that the device exists at the expected MAC ID or verify that the cabling is correct. |
| −2147136205 | Board self test fails. Solution: Try to reinstall the driver or switch the slots of the boards. If the error persists, contact National Instruments. |
| −2147136203 | Driver fails to communicate with the device. Solution: Ensure that the device is connected. |
| −2147136202 | FPGA image version between the host and the remote target does not match. Solution: Update installation from the host to the remote target. |
| −2147136200 | The operation cannot be performed when the object has been started. Solution: Stop the object before performing this operation. |
| −2147136199 | The operation cannot be performed when the interface has been started. Solution: Stop the interface before performing this operation. |
| −2147136191 | You are trying to start an interface that does not have bus power for the transceiver. Some physical layers on DeviceNet hardware are internally powered on, but other hardware might require external power for the port to operate. This error occurs when starting an interface on hardware that requires external power but no power is detected. Solution: Supply proper voltage to your transceiver. |
| −2147136190 | The error occurs when you send out an EM request and try to get an EM response. The EM response has not arrived. Solution: Call the Wait for State VI to wait for the Read Available state before calling the Read DeviceNet Explicit Message VI to get the response. |
| −2147136188 | The error occurs when you send out an fragment EM request and receive an EM ACK, indicating the EM request is too long. Solution: Send a shorter EM request. |
| −2147136187 | The error occurs when you send out an fragment EM request and receive an EM ACK with an invalid error code. Solution: Resend the EM request. |
| −2147136186 | You can only use this property in master mode. You cannot use this property when the EM or IO is in slave mode. Solution: Check the property IDs to see that some properties are master only. |
| −2147136185 | Firmware of C Series modules is corrupted. Solution: Reinstall the firmware by using ModuleFirmwareUpdate.exe in the National Instruments\\NI-IndCom for DeviceNet\\Utilities directory. |
| −2147136184 | Firmware image version is incompatible with C Series modules. Solution: Update the firmware by using ModuleFirmwareUpdate.exe in the National Instruments\\NI-IndCom for DeviceNet\\Utilities directory. |
| 347137 | The connection to the DeviceNet device is timeout, so the device does not respond to messages sent by DeviceNet. Solution: Increase the value of the Expected Packet Rate in the Open DeviceNet IO VI and verify that the device is operational. |
| 347138 | The object is already open, but you are allowed to use a duplicate handle. Solution: Ensure that only one application at a time uses an object , and that you close all objects prior to exiting your application. Do not use the LabVIEW toolbar Abort button. |
| 347139 | You try to use the Write DeviceNet Explicit Message VI before a response from a previous Write arrives. Only one explicit message can be pending. Solution: Complete a Write, Wait, and Read circle before sending another Write DeviceNet Explicit Message request. |
| 347140 | The property size passed in is invalid. Solution: Use a valid property size. |
| 347184 | The slave parameters cannot be downloaded successfully. Solution: Verify the EDS file is correct and the parameter is writable for the slave device. |
| 347185 | The DeviceNet slave is not connected. Solution: Ensure the slave is connected to the network. |
| 347186 | IO data is not available. Solution: Waiting for data becomes available before reading IO data. |
| 347187 | The data length of the I/O connection does not equal the predefined output length. Solution: Ensure that the data length in the Write DeviceNet IO VI equals the output length. |
| 347188 | CAN frames are not available for reading. Solution: Wait for data to be available before reading CAN frames. |
| 347189 | Read CAN Frame queue is overflowed. Solution: Reduce your data rate or call Read CAN Frame more frequently. |

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=function-block.html language=enus -->
## TOPIC 00033: Function Block

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `function-block.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/function-block.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Use the DeviceNet Explicit Message Function Block and DeviceNet device for your project.

### Function Block

**Owning Palette:** Advanced VIs 
Use the [DeviceNet Explicit Message Function Block](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_api_fb_expmsg) and [DeviceNet device](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dnet_lv_api_iocontrol) for your project.

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=general-page.html language=enus -->
## TOPIC 00034: General Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `general-page.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/general-page.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides general information about the DeviceNet master including vendor information, adapter information, and the DeviceNet master name. The following table describes each property on the page. Property Description AccessName The DeviceNet master name. This name is unique for each control

### General Page

This page provides general information about the DeviceNet master including vendor information, adapter information, and the DeviceNet master name.

The following table describes each property on the page.

| Property | Description | Access |
| --- | --- | --- |
| Name | The DeviceNet master name. This name is unique for each controller if multiple DeviceNet masters are on a controller. | Read/write |
| Physical Interface | Determines the interface that you use. You can select from DeviceNet1 to DeviceNet32. | Read/write |
| Protocol | The protocol used by the DeviceNet master. The protocol is always DeviceNet. | Read only |
| Vendor | The vendor name of the DeviceNet master. The vendor name is always National Instruments. | Read only |
| Type | The physical type of the DeviceNet master. The type is always Communication Adapter. | Read only |
| Product | The product category of the DeviceNet master. The category is always DeviceNet Interface. | Read only |

Parent topic:

DeviceNet Master Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=general-page2.html language=enus -->
## TOPIC 00035: General Page

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `general-page2.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/general-page2.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page provides the properties of the DeviceNet slave device, including vendor and device information. The following table describes each property. Property Description AccessName Sets and displays the name of the slave device. Read/writeVendor Displays the vendor name of the slave device. Read o

### General Page

This page provides the properties of the DeviceNet slave device, including vendor and device information.

The following table describes each property.

| Property | Description | Access |
| --- | --- | --- |
| Name | Sets and displays the name of the slave device. | Read/write |
| Vendor | Displays the vendor name of the slave device. | Read only |
| Type | Displays the type name of the slave device. | Read only |
| Product | Displays the product code of the slave device. | Read only |
| Revision | Displays the revision number of the slave device. | Read only |
| Serial Number | Displays the serial number of the slave device. | Read only |

Parent topic:

DeviceNet Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=get-devicenet-attribute-vi.html language=enus -->
## TOPIC 00036: Get DeviceNet Attribute VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `get-devicenet-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/get-devicenet-attribute-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Gets an attribute value from a DeviceNet device using an Explicit Messaging Object and executes the Get Attribute Single service on a remote DeviceNet device. timeout specifies the maximum time, in milliseconds, that the NI-IndCom for DeviceNet uses to wait for a respon

### Get DeviceNet Attribute VI

**Owning Palette:** DeviceNet VIs

Gets an attribute value from a DeviceNet device using an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message) and executes the Get Attribute Single service on a remote DeviceNet device.

[IMAGE alt='image' src='images/Get_DeviceNet_Attribute.gif']

|  | timeout specifies the maximum time, in milliseconds, that the NI-IndCom for DeviceNet uses to wait for a response from a device. The default is 100 ms. Set the timeout value of FFFFFFFF hex to wait indefinitely. To get an attribute from the device, NI-IndCom for DeviceNet sends an Explicit Message request for the Get Attribute Single service to the device. After sending the service request, this VI waits for the Explicit Message response for the Get Attribute Single service. If timeout expires before receiving the response from the device, this VI returns an error. |
| --- | --- |
|  | object handle in specifies the object handle of the object from which you want to get the DeviceNet attribute. The object can only be an Explicit Messaging Object. |
|  | class ID specifies the class ID. The value ranges from 0 to FFFF hex. The default is 0. The device vendor provides vendor-specific classes. Although the DeviceNet Specification allows 16-bit class IDs, most class IDs are 8-bit. NI-IndCom for DeviceNet uses the class ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | instance ID specifies the instance ID. The value ranges from 0 to FFFF hex. The default is 0. DeviceNet reserves instance ID 0 to get an attribute from the class itself. Use values other than 0 to get the attribute from other instances within the class. For example, the primary Identity Object in a device uses instance ID 1. Although the DeviceNet Specification allows both 8-bit and 16-bit instance IDs, most instance IDs are 8-bit. NI-IndCom for DeviceNet uses the instance ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | attribute ID specifies the attribute to get. Refer to the DeviceNet Specification for more information of the attribute ID from the description of the class and instance. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | device error returns the error codes from the error response of a device. If the remote device responds to the Get Attribute Single service, error out does not return an error and device error returns 0. If the remote device does not respond to the Get Attribute Single service, error out returns an error and device error returns the error code from the response. The low byte of device error returns the General Error Code from the error response of a device. Common values for General Error Code include Attribute Not Supported (14 hex), Object Does Not Exist (16 hex), and Invalid Attribute Value (09 hex). The high byte of device error returns the Additional Code from the error response of a device. The Additional Code provides additional information that further describes the error. If no additional information is necessary, the high byte returns FF hex. Values for the General Error Code and Additional Code are in the DeviceNet Specification. Refer to Appendix H, DeviceNet Error Codes of the DeviceNet Specification for more information of the common error code values. You can also find object-specific error codes in the object description and vendor-specific error codes in your device documentation. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | attribute data returns the attribute value from device. The DeviceNet data type defines the format of the data returned in attribute data. The Convert From DeviceNet Read VI can convert the DeviceNet data type into the LabVIEW data type. |
|  | actual attribute data length returns the number of attribute data bytes returned. You can obtain this length from the Actual Get Attribute Single response message. The value ranges from 0 to 240. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=get-driver-attribute-vi.html language=enus -->
## TOPIC 00037: Get Driver Attribute VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `get-driver-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/get-driver-attribute-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Gets the value of an attribute from the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-supplied information. You cannot use this VI to get an attribute from a remote DeviceNet slave device. To get an attribute from a

### Get Driver Attribute VI

**Owning Palette:** Advanced VIs

Gets the value of an attribute from the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-supplied information.

You cannot use this VI to get an attribute from a remote DeviceNet slave device. To get an attribute from a remote DeviceNet slave device, use the Get DeviceNet Attribute VI.

[IMAGE alt='image' src='images/Get_Driver_Attribute.gif']

|  | user supplied attribute ID specifies the identifier of a user-supplied attribute. Use this input to define an attribute you want to use other than the other attributes in this VI. You also need to set attribute ID to <User Supplied AttrID> to use a user-supplied attribute. The default is 0. |
| --- | --- |
|  | object handle in specifies the object handle of the object that you use to get the driver attribute. The object can be an open Interface Object, an Explicit Messaging Object, or an I/O Object. |
|  | attribute ID specifies the attribute of which you want to get the value from the NI-IndCom for DeviceNet driver. 0Current State—(Default) Applies to the Explicit Messaging Object and I/O Object of both the master and the slave.Select this attribute to get the current Read Avail and Established states from the driver. You can get the following attribute values: 1 hex stands for the Read Avail state. 8 hex stands for the Established state. 9 hex stands for a combination of the two states.1Intf Protocol Version—Applies to the Interface Object of both the master and the slave.Select this attribute to get the version of the DeviceNet Specification the NI-IndCom for DeviceNet software conforms to.2Intf Software Version—Applies to the Interface Object of both the master and the slave.Select this attribute to get the version of the NI-IndCom for DeviceNet software.3Intf Baud Rate—Applies to the Interface Object of both the master and the slave.Select this attribute to get the interface baud rate that you originally set in the Open DeviceNet Interface VI.4Intf Poll Mode—Applies to the Interface Object of both the master and the slave.Select this attribute to get the interface poll mode that you originally set in the Open DeviceNet Interface VI.5MAC ID—Applies to the Interface Object, the Explicit Messaging Object, and the I/O Object of both the master and the slave.Select this attribute to get the MAC ID that you originally set in the Open DeviceNet Interface VI.6Vendor ID—Applies to the Explicit Messaging Object and I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute.7Product Code—Applies to the Explicit Messaging Object and I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute.8Device Type—Applies to the Explicit Messaging Object and I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute.9I/O Input Length—Applies only to the I/O Object of both the master and the slave.Select this attribute to get the I/O input length that you originally set in the Open DeviceNet IO VI.10I/O Output length—Applies to the I/O Object of both the master and the slave.Select this attribute to get the I/O output length that you originally set in the Open DeviceNet IO VI.11I/O Exp Packet Rate—Applies to the I/O Object of the master.Select this attribute to get the I/O expected packet rate that you originally set in the Open DeviceNet IO VI.12COS/Cyclic Ack Suppress—Applies to Change of State (COS) and Cyclic I/O Objects of the master.Refer to the Set Driver Attribute VI for more details of this attribute.13COS Inhibit Timer—Applies to the COS I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute.14<User Supplied AttrID>—Identifies a user-supplied attribute. Apply to both the master and the slave.Select this attribute to get the value of a user-supplied attribute.15Termination Resistor—Applies to the Interface Object of both the master and the slave.Refer to the Set Driver Attribute VI for more details of this attribute.16Reset State—Applies to the Interface Object of the slave.The Reset request message specifies whether the Identity Object (Class Code 01 hex) and DeviceNet Object (Class Code 03 hex) receive a Reset request and what the Reset service parameter is if either object receives a Reset request.When the value is 0, no Identity Object or DeviceNet Object receives Reset requests from the master. When the objects receive Reset requests, you can choose to ignore the requests or to use the requests to reset your devices according to your needs.17Ack Timer—Applies to the I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 0 | Current State—(Default) Applies to the Explicit Messaging Object and I/O Object of both the master and the slave.Select this attribute to get the current Read Avail and Established states from the driver. You can get the following attribute values: 1 hex stands for the Read Avail state. 8 hex stands for the Established state. 9 hex stands for a combination of the two states. |
| 1 | Intf Protocol Version—Applies to the Interface Object of both the master and the slave.Select this attribute to get the version of the DeviceNet Specification the NI-IndCom for DeviceNet software conforms to. |
| 2 | Intf Software Version—Applies to the Interface Object of both the master and the slave.Select this attribute to get the version of the NI-IndCom for DeviceNet software. |
| 3 | Intf Baud Rate—Applies to the Interface Object of both the master and the slave.Select this attribute to get the interface baud rate that you originally set in the Open DeviceNet Interface VI. |
| 4 | Intf Poll Mode—Applies to the Interface Object of both the master and the slave.Select this attribute to get the interface poll mode that you originally set in the Open DeviceNet Interface VI. |
| 5 | MAC ID—Applies to the Interface Object, the Explicit Messaging Object, and the I/O Object of both the master and the slave.Select this attribute to get the MAC ID that you originally set in the Open DeviceNet Interface VI. |
| 6 | Vendor ID—Applies to the Explicit Messaging Object and I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 7 | Product Code—Applies to the Explicit Messaging Object and I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 8 | Device Type—Applies to the Explicit Messaging Object and I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 9 | I/O Input Length—Applies only to the I/O Object of both the master and the slave.Select this attribute to get the I/O input length that you originally set in the Open DeviceNet IO VI. |
| 10 | I/O Output length—Applies to the I/O Object of both the master and the slave.Select this attribute to get the I/O output length that you originally set in the Open DeviceNet IO VI. |
| 11 | I/O Exp Packet Rate—Applies to the I/O Object of the master.Select this attribute to get the I/O expected packet rate that you originally set in the Open DeviceNet IO VI. |
| 12 | COS/Cyclic Ack Suppress—Applies to Change of State (COS) and Cyclic I/O Objects of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 13 | COS Inhibit Timer—Applies to the COS I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 14 | <User Supplied AttrID>—Identifies a user-supplied attribute. Apply to both the master and the slave.Select this attribute to get the value of a user-supplied attribute. |
| 15 | Termination Resistor—Applies to the Interface Object of both the master and the slave.Refer to the Set Driver Attribute VI for more details of this attribute. |
| 16 | Reset State—Applies to the Interface Object of the slave.The Reset request message specifies whether the Identity Object (Class Code 01 hex) and DeviceNet Object (Class Code 03 hex) receive a Reset request and what the Reset service parameter is if either object receives a Reset request.When the value is 0, no Identity Object or DeviceNet Object receives Reset requests from the master. When the objects receive Reset requests, you can choose to ignore the requests or to use the requests to reset your devices according to your needs. |
| 17 | Ack Timer—Applies to the I/O Object of the master.Refer to the Set Driver Attribute VI for more details of this attribute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | attribute value returns the attribute value of NI-IndCom for DeviceNet driver. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=labview-project-item-menus.html language=enus -->
## TOPIC 00038: LabVIEW Project Item Menus

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `labview-project-item-menus.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/labview-project-item-menus.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you right-click a DeviceNet project item, you can access the following item context menus: Project root item menu: New»Targets and Devices—Displays the Add Targets and Devices dialog box to add a real-time controller target. My Computer/Real-Time target item menu: New»Targets and Devices—Displa

### LabVIEW Project Item Menus

When you right-click a DeviceNet project item, you can access the following item context menus:

- Project root item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add a real-time controller target.

- My Computer/Real-Time target item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add a DeviceNet master .

- DeviceNet master item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add a DeviceNet slave device .
  - Utilities»Online Test Panel —Displays the Online Test Panel to indicate the state of the devices added into the interface.
  - Utilities»Change Slave Address —Displays the Change Slave Address dialog box to change the address of a slave device.
  - Utilities»Change Slave Baud Rate —Displays the Change Slave Baud Rate dialog box to change the baud rate of a slave device.
  - Deploy —Deploys the configuration to the target controller.
  - Undeploy —Removes the configuration from the target controller.
  - Remove from Project —Removes the item from the project.
  - Rename —Renames the item.
  - Help —Displays this help file.
  - Properties —Displays the DeviceNet Master Properties dialog box.

- DeviceNet slave device item menu:
  - Configure I/O —Displays the DeviceNet Slave Device Properties dialog box to configure I/O variables.
  - Utilities»Online Test Panel —Displays the DeviceNet Slave Device Online Test Panel dialog box.
  - Datasheet —Displays the Datasheet dialog box to import a device datasheet.
  - Remove from Project —Removes the item from the project.
  - Rename —Renames the item.
  - Help —Displays this help file.
  - Properties —Displays the DeviceNet Slave Device Properties dialog box.

- I/O variable item menu:
  - Properties —Displays the I/O Variable Properties dialog box.

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=labview-project-items.html language=enus -->
## TOPIC 00039: LabVIEW Project Items

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `labview-project-items.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/labview-project-items.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Project Explorer window includes the following items: Project rootâThe top-level device trunk, containing all of the sub-items in the Project Explorer window. My Computer/Real-Time targetâThe host or real-time target that controls the following DeviceNet items: DeviceNet MasterâA m

### LabVIEW Project Items

The LabVIEW Project Explorer window includes the following items:

- Project root âThe top-level device trunk, containing all of the sub-items in the Project Explorer window.
- My Computer/Real-Time target âThe host or real-time target that controls the following DeviceNet items:
  - DeviceNet Master âA master device using the DeviceNet Port for the DeviceNet network.
  - DeviceNet Slave device âA DeviceNet slave device.
  - I/O Variable âVariables to which the physical channels of the slave device are mapped. A slave device can have multiple I/O variables.

Note

Project root

My Computer

- Add a Real-Time Controller
- Add a DeviceNet Master
- Add a DeviceNet Slave Device

Parent topic:

Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=open-can-frame-read-vi.html language=enus -->
## TOPIC 00040: Open CAN Frame Read VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `open-can-frame-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/open-can-frame-read-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Opens a CAN Frame Read Object and returns a handle of this object. You can use this handle to read the raw CAN frames in the Read CAN Frame VI. interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface nu

### Open CAN Frame Read VI

**Owning Palette:** Advanced VIs

Opens a CAN Frame Read Object and returns a handle of this object. You can use this handle to read the raw CAN frames in the Read CAN Frame VI.

[IMAGE alt='image' src='images/Open_CAN_Frame_Read.gif']

|  | interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 to 31. You can use NI Measurement & Automation Explorer (MAX) to view the relationship between each interface name and each piece of hardware. |
| --- | --- |
|  | buffer size specifies the maximum number of CAN frames that the buffer saves. The buffer is a first-in-first-out buffer. The default is 64. The CAN Frame Read object keeps CAN frames in a queue when the object receives CAN frames. If this object receives more frames than buffer size, the object returns an overflow warning. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns a handle of the CAN Frame Read Object and passes the handle to the Read CAN Frame VI to read the raw CAN frames. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=open-devicenet-explicit-messaging-vi.html language=enus -->
## TOPIC 00041: Open DeviceNet Explicit Messaging VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `open-devicenet-explicit-messaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/open-devicenet-explicit-messaging-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Configures and opens an Explicit Messaging Object and returns a handle of this object. interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 t

### Open DeviceNet Explicit Messaging VI

**Owning Palette:** DeviceNet VIs

Configures and opens an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message) and returns a handle of this object.

[IMAGE alt='image' src='images/Open_DeviceNet_Explicit_Messaging.gif']

|  | interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 to 31. You can use NI Measurement & Automation Explorer (MAX) to view the relationship between each interface name and each piece of hardware. |
| --- | --- |
|  | device MAC ID specifies the device address of the remote DeviceNet device. The value ranges from 0 to 63. The default is 0. If a device uses physical switches to set the device MAC ID, examine these switches to get the MAC ID. Many devices use 63 as the factory default. You can only use this VI when you configure the I/O communication as a master to a remote slave device. Do not use this VI when you configure the I/O communication as a slave. You can use the Write DeviceNet Explicit Message VI for slave devices to respond to the Explicit Messaging requests but not to send the Explicit Messaging requests spontaneously. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=open-devicenet-interface-vi.html language=enus -->
## TOPIC 00042: Open DeviceNet Interface VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `open-devicenet-interface-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/open-devicenet-interface-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Configures and opens an Interface Object and returns a handle of this object. You must open an Interface Object before you start any application on the real-time CompactRIO controller. Before you open the interface, a delay occurs due to a loading process for a few seco

### Open DeviceNet Interface VI

**Owning Palette:** DeviceNet VIs

Configures and opens an [Interface Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_interface_object) and returns a handle of this object.

You must open an Interface Object before you start any application on the real-time CompactRIO controller. Before you open the interface, a delay occurs due to a [loading process](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_load) for a few seconds. This process [establishes communications](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_get_started_crio05) between the controller and the NI-Industrial Communications for DeviceNet module.

Details

[IMAGE alt='image' src='images/Open_DeviceNet_Interface.gif']

|  | interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 to 31. You can use NI Measurement & Automation Explorer (MAX) to view the relationship between each interface name and each piece of hardware. |
| --- | --- |
|  | interface configuration specifies configurations for an Interface Object. interface MAC ID specifies the MAC ID of a DeviceNet interface to communicate with other DeviceNet devices. The value ranges from 0 to 63. The default is 0. A device MAC ID indicates the priority of sending DeviceNet messages on the network. The lower numbered MAC ID has the higher priority. Set the MAC ID to 0 if the DeviceNet interface is the only master on the network. baud rate specifies the network baud rate, in bit per second (b/s), the NI-IndCom for DeviceNet uses to communicate with devices. 0125000 (Default)12500002500000 poll mode specifies the communication scheme used for all polled I/O connections in which the interface acts as a master. In poll mode, the interface uses this scheme to transmit poll requests to slave devices. 0Automatic (Default)1Scanned2Individual |
|  | interface MAC ID specifies the MAC ID of a DeviceNet interface to communicate with other DeviceNet devices. The value ranges from 0 to 63. The default is 0. A device MAC ID indicates the priority of sending DeviceNet messages on the network. The lower numbered MAC ID has the higher priority. Set the MAC ID to 0 if the DeviceNet interface is the only master on the network. |
|  | baud rate specifies the network baud rate, in bit per second (b/s), the NI-IndCom for DeviceNet uses to communicate with devices. 0125000 (Default)12500002500000 |
| 0 | 125000 (Default) |
| 1 | 250000 |
| 2 | 500000 |
|  | poll mode specifies the communication scheme used for all polled I/O connections in which the interface acts as a master. In poll mode, the interface uses this scheme to transmit poll requests to slave devices. 0Automatic (Default)1Scanned2Individual |
| 0 | Automatic (Default) |
| 1 | Scanned |
| 2 | Individual |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Open DeviceNet Interface Details

For any NI-IndCom for DeviceNet LabVIEW application, you can only open the interface once. If you open the interface twice, this VI returns an error the second time. You must use the Close Object VI to close the interface.

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=open-devicenet-io-vi.html language=enus -->
## TOPIC 00043: Open DeviceNet IO VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `open-devicenet-io-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/open-devicenet-io-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Configures and opens an I/O Object and returns a handle of this object. interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 to 31. You can u

### Open DeviceNet IO VI

**Owning Palette:** DeviceNet VIs

Configures and opens an [I/O Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_io_object) and returns a handle of this object.

[IMAGE alt='image' src='images/Open_DeviceNet_IO.gif']

|  | interface name specifies the name of a DeviceNet interface. The name of an interface must be dnetx, where x is the interface number. The value of this interface number ranges from 0 to 31. You can use NI Measurement & Automation Explorer (MAX) to view the relationship between each interface name and each piece of hardware. |
| --- | --- |
|  | DeviceNet IO configuration specifies configurations for the attributes passed into this VI. device MAC ID specifies the device address of the remote DeviceNet device. The value ranges from 0 to 63. Many devices use physical switches to set the device MAC IDs. For these devices, examine these switches to get the MAC IDs. Many devices use 63 as the factory default. When you configure I/O communication as a master to a remote slave device, set device MAC ID different from the interface MAC ID of your DeviceNet interface. When you configure I/O communication as a slave with a remote master, set device MAC ID the same as the interface MAC ID of your DeviceNet interface. connection type specifies the type of master/slave I/O connection. 0Poll (Default)1Strobe2COS3Cyclic input length specifies the number of bytes that NI-IndCom for DeviceNet reads from the I/O connection. The default is 1. Refer to the Electronic Data Sheets (EDS) for specifications. The specific input length setting varies for the following connection types: Poll, COS, and Cyclic—The input length is the same as the number of bytes of the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The input length is the same as the number of bytes of the strobe response message. The value ranges from 0 to 8. Strobe as slave—device MAC ID is equal to interface MAC ID. The input length must be 1. You can obtain the input data consisting of a single Boolean value in bit from the master's strobe command message by using interface MAC ID. The Read DeviceNet IO VI returns this Boolean value as a single byte. Refer to the device vendor's documentation for more information about how to choose a specific value. output length specifies the number of bytes the Write DeviceNet IO VI writes to the I/O connection. The default is 1. Refer to the EDS file for specifications. The specific output length setting varies for the following connection types: Poll, COS, and Cyclic—The output length is the same as the number of bytes consumed from the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The output length must be 1. The output data consists of a single Boolean value that passes into the strobe command message using device MAC ID. You can also use this Boolean value in the Write DeviceNet IO VI as a single byte. Strobe as slave—device MAC ID is equal to interface MAC ID. The value ranges from 0 to 8, which is the same as the number of bytes produced in the strobe response message. expected packet rate specifies the expected packet rate (EPR) of I/O message production in milliseconds. The EPR setting only applies to the I/O Objects used for communication as a master. For I/O Objects used for communication as a slave, your device ignores your slave EPR setting, because the remote master determines the EPR on behalf of your slave. The default is 200. The value ranges from 1 to 60,000. The value must be a multiple of 4. If the value is not a multiple of 4, NI-IndCom of DeviceNet rounds up the value to a multiple of 4. For example, if the value is 5 or 6, NI-IndCom for DeviceNet rounds up the value to 8. If the value is 1 or 2, NI-IndCom for DeviceNet rounds up the value to 4. You can use the Get Driver Attribute VI to get the EPR you use after the interface starts. |
|  | device MAC ID specifies the device address of the remote DeviceNet device. The value ranges from 0 to 63. Many devices use physical switches to set the device MAC IDs. For these devices, examine these switches to get the MAC IDs. Many devices use 63 as the factory default. When you configure I/O communication as a master to a remote slave device, set device MAC ID different from the interface MAC ID of your DeviceNet interface. When you configure I/O communication as a slave with a remote master, set device MAC ID the same as the interface MAC ID of your DeviceNet interface. |
|  | connection type specifies the type of master/slave I/O connection. 0Poll (Default)1Strobe2COS3Cyclic |
| 0 | Poll (Default) |
| 1 | Strobe |
| 2 | COS |
| 3 | Cyclic |
|  | input length specifies the number of bytes that NI-IndCom for DeviceNet reads from the I/O connection. The default is 1. Refer to the Electronic Data Sheets (EDS) for specifications. The specific input length setting varies for the following connection types: Poll, COS, and Cyclic—The input length is the same as the number of bytes of the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The input length is the same as the number of bytes of the strobe response message. The value ranges from 0 to 8. Strobe as slave—device MAC ID is equal to interface MAC ID. The input length must be 1. You can obtain the input data consisting of a single Boolean value in bit from the master's strobe command message by using interface MAC ID. The Read DeviceNet IO VI returns this Boolean value as a single byte. Refer to the device vendor's documentation for more information about how to choose a specific value. |
|  | output length specifies the number of bytes the Write DeviceNet IO VI writes to the I/O connection. The default is 1. Refer to the EDS file for specifications. The specific output length setting varies for the following connection types: Poll, COS, and Cyclic—The output length is the same as the number of bytes consumed from the remote device. The value ranges from 0 to 255. Strobe as master—device MAC ID is not equal to interface MAC ID. The output length must be 1. The output data consists of a single Boolean value that passes into the strobe command message using device MAC ID. You can also use this Boolean value in the Write DeviceNet IO VI as a single byte. Strobe as slave—device MAC ID is equal to interface MAC ID. The value ranges from 0 to 8, which is the same as the number of bytes produced in the strobe response message. |
|  | expected packet rate specifies the expected packet rate (EPR) of I/O message production in milliseconds. The EPR setting only applies to the I/O Objects used for communication as a master. For I/O Objects used for communication as a slave, your device ignores your slave EPR setting, because the remote master determines the EPR on behalf of your slave. The default is 200. The value ranges from 1 to 60,000. The value must be a multiple of 4. If the value is not a multiple of 4, NI-IndCom of DeviceNet rounds up the value to a multiple of 4. For example, if the value is 5 or 6, NI-IndCom for DeviceNet rounds up the value to 8. If the value is 1 or 2, NI-IndCom for DeviceNet rounds up the value to 4. You can use the Get Driver Attribute VI to get the EPR you use after the interface starts. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=operate-devicenet-interface-vi.html language=enus -->
## TOPIC 00044: Operate DeviceNet Interface VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `operate-devicenet-interface-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/operate-devicenet-interface-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Performs an operation on an Interface Object. Use this VI to start and stop all DeviceNet communication for the associated interface, including all Explicit Messaging connections and I/O connections. You also can use this VI to place the outputs of all I/O connections i

### Operate DeviceNet Interface VI

**Owning Palette:** DeviceNet VIs

Performs an operation on an [Interface Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_interface_object).

Use this VI to start and stop all DeviceNet communication for the associated interface, including all Explicit Messaging connections and I/O connections. You also can use this VI to place the outputs of all I/O connections into active mode or idle mode.

After you open the [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message) and the [I/O Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_io_object), you must use this VI to start communication and to stop communication before terminating your application.

[IMAGE alt='image' src='images/Operate_DeviceNet_Interface.gif']

|  | object handle in specifies the object handle of the object that you want to operate for the DeviceNet interface. |
| --- | --- |
|  | operation code specifies which operation to perform on the Interface Object. The DeviceNet Specification does not define the behavior of a slave device on reception of a zero length I/O message. 0Start—(Default) Starts all DeviceNet communication for the associated interface. For each open Explicit Messaging Object and open I/O Object for the interface, this operation establishes the DeviceNet connection with the remote device. When the operation establishes I/O connections, the operation produces data on the network. If the default all bytes zero data is not valid for your application, use the Write DeviceNet IO VI for each I/O Object to initialize valid output data prior to starting communication. This operation has no effect after starting the interface.1Stop—Stops all DeviceNet communication for the associated interface. For each open Explicit Messaging Object and open I/O Object for the interface, this operation closes the DeviceNet connection with the remote device. You cannot close Explicit Messaging Object or I/O Object before stopping the objects. You can close Interface Object in any mode. Closing Interface Object stops and closes all Explicit Messaging Objects and I/O Objects.2Active—Places all DeviceNet I/O communication for the associated interface into active mode. When an I/O connection is in active mode, it produces data in its outgoing I/O message. Use this operation after using Idle mode to restore normal communication on all I/O Objects associated with the interface. This operation has no effect when the interface is already in active mode or stop mode.3Idle—Places all DeviceNet I/O communication for all associated interface into idle mode. When an I/O connection is in idle mode, it does not produce data in its outgoing I/O message, but keeps the I/O connection open by producing an I/O message with zero data bytes. Use this operation when valid output data is no longer available from your application. This operation has no effect when the interface is already in idle mode or stop mode. Many slave devices exhibit unexpected behavior when you use the Idle operation. If you need to suspend your application while keeping I/O connections open, provide idle values for outputs using the Write DeviceNet IO VI rather than using the Idle operation. |
| 0 | Start—(Default) Starts all DeviceNet communication for the associated interface. For each open Explicit Messaging Object and open I/O Object for the interface, this operation establishes the DeviceNet connection with the remote device. When the operation establishes I/O connections, the operation produces data on the network. If the default all bytes zero data is not valid for your application, use the Write DeviceNet IO VI for each I/O Object to initialize valid output data prior to starting communication. This operation has no effect after starting the interface. |
| 1 | Stop—Stops all DeviceNet communication for the associated interface. For each open Explicit Messaging Object and open I/O Object for the interface, this operation closes the DeviceNet connection with the remote device. You cannot close Explicit Messaging Object or I/O Object before stopping the objects. You can close Interface Object in any mode. Closing Interface Object stops and closes all Explicit Messaging Objects and I/O Objects. |
| 2 | Active—Places all DeviceNet I/O communication for the associated interface into active mode. When an I/O connection is in active mode, it produces data in its outgoing I/O message. Use this operation after using Idle mode to restore normal communication on all I/O Objects associated with the interface. This operation has no effect when the interface is already in active mode or stop mode. |
| 3 | Idle—Places all DeviceNet I/O communication for all associated interface into idle mode. When an I/O connection is in idle mode, it does not produce data in its outgoing I/O message, but keeps the I/O connection open by producing an I/O message with zero data bytes. Use this operation when valid output data is no longer available from your application. This operation has no effect when the interface is already in idle mode or stop mode. Many slave devices exhibit unexpected behavior when you use the Idle operation. If you need to suspend your application while keeping I/O connections open, provide idle values for outputs using the Write DeviceNet IO VI rather than using the Idle operation. |
|  | operation code parameter specifies what operation code defines. Because none of the operations currently use this additional parameter, this VI ignores operation code parameter. Set the parameter to 0. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=project-explorer-window-environment.html language=enus -->
## TOPIC 00045: Project Explorer Window Environment

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `project-explorer-window-environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/project-explorer-window-environment.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Project Explorer window displays the following NI-Industrial Communications for DeviceNet user interface items: LabVIEW Project Items and related item menus DeviceNet Change Slave Address Dialog Box DeviceNet Change Slave Baud Rate Dialog Box DeviceNet Datasheet Dialog Box DeviceNet I/O

### Project Explorer Window Environment

The LabVIEW Project Explorer window displays the following NI-Industrial Communications for DeviceNet user interface items:

- LabVIEW Project Items and related item menus
- DeviceNet Change Slave Address Dialog Box
- DeviceNet Change Slave Baud Rate Dialog Box
- DeviceNet Datasheet Dialog Box
- DeviceNet I/O Item Editor Dialog Box
- DeviceNet Master Interface Online Test Panel Dialog box
- DeviceNet Master Properties Dialog Box
- DeviceNet Master Setting Dialog Box
- DeviceNet Slave Device Online Test Panel Dialog Box
- DeviceNet Slave Device Properties Dialog Box
- DeviceNet Slave Setting Dialog Box
- DeviceNet Parameter Editor Dialog Box
- DeviceNet Parameter Publish Option Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=read-can-frame-vi.html language=enus -->
## TOPIC 00046: Read CAN Frame VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `read-can-frame-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/read-can-frame-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Reads a CAN frame on a DeviceNet interface. National Instruments recommends that you use the Wait for State VI to wait for CAN frames after opening the CAN Frame Read Object but before reading the frames. Because if you do not wait, you may have no CAN frame available to

### Read CAN Frame VI

**Owning Palette:** Advanced VIs

Reads a CAN frame on a DeviceNet interface.

National Instruments recommends that you use the Wait for State VI to wait for CAN frames after opening the CAN Frame Read Object but before reading the frames. Because if you do not wait, you may have no CAN frame available to read.

[IMAGE alt='image' src='images/Read_CAN_Frame.gif']

|  | object handle in specifies the object handle of the object that you want to use to read the CAN frame. Use the Open CAN Frame Read VI to generate this object handle. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RTR? indicates whether this CAN frame is a remote transmission request. |
|  | object handle out returns the object handle of the Interface Object. Use this output in subsequent VIs for this object. |
|  | arbitration ID returns the arbitration ID of the CAN frame that the VI reads. |
|  | CAN message data returns the data of the CAN frames that the VI reads. If the buffer of the CAN Frame Read Object receives a new frame, CAN message data returns the data of the new frame. If the buffer receives no frame, CAN message data returns an empty array and error out returns a warning, indicating that no CAN frame is available for reading. If the buffer contains more frames than the buffer size, CAN message data returns the data of the CAN frames and error out returns an overflow warning. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | timestamp returns the time of your target when the CAN frames arrive at the NI-IndCom for DeviceNet module. A target can be a computer, a CompactRIO controller, or a PXI. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=read-devicenet-explicit-message-vi.html language=enus -->
## TOPIC 00047: Read DeviceNet Explicit Message VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `read-devicenet-explicit-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/read-devicenet-explicit-message-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Reads an Explicit Message response from an Explicit Messaging Object. Details object handle in specifies the object handle of the object that you use to read the DeviceNet Explicit Message. error in describes error conditions that occur before this node runs. This input

### Read DeviceNet Explicit Message VI

**Owning Palette:** Advanced VIs

Reads an Explicit Message response from an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message).

Details

[IMAGE alt='image' src='images/Read_DeviceNet_Explicit_Message.gif']

|  | object handle in specifies the object handle of the object that you use to read the DeviceNet Explicit Message. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | service code specifies the service response as either a success or an error. Refer to the DeviceNet Specification for more information about service code. Although the DeviceNet Specification requires to set the high bit of the service code (hex 80) in all Explicit Message responses, NI-IndCom for DeviceNet clears this response indicator. You can compare the actual service code with service code of the Write DeviceNet Explicit Message VI. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | actual service data length returns the number of service data bytes in the response. Obtain this length from the Actual Response Message. |
|  | service data returns the service data bytes from the response. If the response shows a success, the service defines the format of these bytes. If the response shows an error, the first byte (service data[0]) contains a General Error Code, and the second byte (service data[1]) contains an Additional Code. Either the DeviceNet Specification or the object itself defines the error codes. |
|  | error out contains error information. This output provides standard error out functionality. |

Read DeviceNet Explicit Message Details

Although the DeviceNet Specification defines the overall format of DeviceNet services, in most cases their meaning and service data are object specific or vendor specific.

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=read-devicenet-io-vi.html language=enus -->
## TOPIC 00048: Read DeviceNet IO VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `read-devicenet-io-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/read-devicenet-io-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Reads input data from an I/O Object. Because each I/O Object continuously acquires input data from the DeviceNet network, you need to wait for new input data to become available before using this VI. By waiting for new input data, the application can receive I/O data at

### Read DeviceNet IO VI

**Owning Palette:** DeviceNet VIs

Reads input data from an [I/O Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_io_object).

Because each I/O Object continuously acquires input data from the DeviceNet network, you need to wait for new input data to become available before using this VI. By waiting for new input data, the application can receive I/O data at the same rate as the DeviceNet I/O communication. Use the Wait For State VI to wait for new input data before reading the input data.

Details

[IMAGE alt='image' src='images/Read_DeviceNet_IO.gif']

|  | object handle in specifies the object handle of the object that you want to use to read the I/O Object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | data returns the data bytes obtained from a remote DeviceNet slave device. Refer to the documentation of the device vendor or the DeviceNet Specification for the information about the format of the input assembly of the remote DeviceNet slave device. |
|  | error out contains error information. This output provides standard error out functionality. |

Read DeviceNet IO Details

The input bytes of a device often consist of multiple data members rather than a single value. You can obtain each data member from the input bytes using the Convert From DeviceNet Read VI.

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=set-devicenet-attribute-vi.html language=enus -->
## TOPIC 00049: Set DeviceNet Attribute VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `set-devicenet-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/set-devicenet-attribute-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Sets an attribute value for a DeviceNet device using an Explicit Messaging Object and executes the Set Attribute Single service on a remote DeviceNet device. attribute data length specifies the number of attribute data bytes to set. This length also specifies the number

### Set DeviceNet Attribute VI

**Owning Palette:** DeviceNet VIs

Sets an attribute value for a DeviceNet device using an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message) and executes the Set Attribute Single service on a remote DeviceNet device.

[IMAGE alt='image' src='images/Set_DeviceNet_Attribute.gif']

|  | attribute data length specifies the number of attribute data bytes to set. This length also specifies the number of bytes in attribute data. The value ranges from 0 to 239. The default is 0. |
| --- | --- |
|  | attribute data specifies the attribute value to set in device. The DeviceNet data type in the description of the attribute defines the format of the data. The default is 0. |
|  | object handle in specifies the object handle of the object that you want to use to set the DeviceNet attribute. The object can only be an Explicit Messaging Object. |
|  | class ID specifies the class ID. The value ranges from 0 to FFFF hex. The default is 0. The device vendor provides vendor-specific classes. Although the DeviceNet Specification allows 16-bit class IDs, most class IDs are 8-bit. NI-IndCom for DeviceNet uses the class ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | instance ID specifies the instance ID. The value ranges from 0 to FFFF hex. The default is 0. DeviceNet reserves instance ID 0 to get an attribute from the class itself. Use values other than 0 to get the attribute from other instances within the class. For example, the primary Identity Object in a device uses instance ID 1. Although the DeviceNet Specification allows both 8-bit and 16-bit instance IDs, most instance IDs are 8-bit. NI-IndCom for DeviceNet uses the instance ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | attribute ID specifies the attribute to set. Refer to the DeviceNet Specification for more information of the attribute ID from the description of the class and instance. The value ranges from 0 to FF hex. The default is 0. |
|  | timeout specifies the maximum time, in milliseconds, that the NI-IndCom for DeviceNet waits for a response from a device. The default is 100 ms. Set timeout value of FFFFFFFF hex to wait indefinitely. To set the attribute for the device, NI-IndCom for DeviceNet sends an Explicit Message request for the Set Attribute Single service to the device. After sending the service request, this VI must wait for the Explicit Message response for Set Attribute Single service. If timeout expires before receiving the response from the master interface, this VI returns an error. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | device error returns the error codes from the error response of a device. If the remote device responds to the Get Attribute Single service, error out does not return an error and device error returns 0. If the remote device does not respond to the Get Attribute Single service, error out returns an error and device error returns the error code from the response. The low byte of device error returns the General Error Code from the error response of a device. Common values for General Error Code include Attribute Not Supported (14 hex), Object Does Not Exist (16 hex), and Invalid Attribute Value (09 hex). The high byte of device error returns the Additional Code from the error response of a device. The Additional Code provides additional information that further describes the error. If no additional information is necessary, the high byte returns FF hex. Values for the General Error Code and Additional Code are in the DeviceNet Specification. Refer to Appendix H, DeviceNet Error Codes of the DeviceNet Specification for more information of the common error code values. You can also find object-specific error codes in the object description and vendor-specific error codes in your device documentation. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=set-driver-attribute-vi.html language=enus -->
## TOPIC 00050: Set Driver Attribute VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `set-driver-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/set-driver-attribute-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Sets the value of an attribute in the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-supplied information. You cannot use this VI to set an attribute in a remote DeviceNet slave device. To set an attribute in a remote

### Set Driver Attribute VI

**Owning Palette:** Advanced VIs

Sets the value of an attribute in the NI-Industrial Communications for DeviceNet driver. Attributes represent configuration and other user-supplied information.

You cannot use this VI to set an attribute in a remote DeviceNet slave device. To set an attribute in a remote DeviceNet slave device, use the Set DeviceNet Attribute VI.

[IMAGE alt='image' src='images/Set_Driver_Attribute.gif']

|  | user supplied attribute ID specifies the identifier of a user-supplied attribute. Use this input to define an attribute you want to use other than the other attributes in this VI. You also need to set attribute ID to <User Supplied AttrID> to use a user-supplied attribute. The default is 0. |
| --- | --- |
|  | object handle in specifies the object handle of the object that you use to set the driver attribute. The object can be an open Interface Object, an Explicit Messaging Object, or an I/O Object. |
|  | attribute value specifies the new attribute value of NI-IndCom for DeviceNet. The default is 0. |
|  | attribute ID specifies the NI-IndCom for DeviceNet attribute. 0Vendor ID—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute specifies a number that the Open Device Vendor's Association (ODVA) assigns to the device vendor. If this attribute is different from the Vendor ID of your slave device, NI-IndCom for DeviceNet returns the error DnetErrDevInitVendor.The default is 0. When Vendor ID is 0, NI-IndCom for DeviceNet does not verify the Vendor ID of your device.1Product Code—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute provides a vendor-specific value that identifies a particular product within a device type. If this attribute is different from the Product Code of your slave device, NI-IndCom for DeviceNet returns the error DnetErrDevInitProdCode.The default is 0. When Product Code is 0, NI-IndCom for DeviceNet does not verify the Product Code of your device.2Device Type—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute verifies whether the Device Type is the one that your application expects. If this attribute is different from the Device Type of your slave device, NI-IndCom for DeviceNet returns the error DnetErrDevInitDevType.The default is 0. When Device Type is 0, NI-IndCom does not verify the Device Type of your device.3COS/Cyclic Ack Suppress (Default) —Applies to Change of State (COS) and Cyclic I/O Objects of the master.This attribute determines whether you use the acknowledgements (FALSE) or suppress the acknowledgements (TRUE). NI-IndCom for DeviceNet produces the acknowledgement when input length of the Easy IO Config VI or the Open DeviceNet IO VI is nonzero. NI-IndCom for DeviceNet consumes the acknowledgement when output length of the same two VIs is nonzero.The default is FALSE. NI-IndCom for DeviceNet can suppress the acknowledgement after verifying the successful device operation. For example, if you open a polled I/O connection in addition to the COS or Cyclic I/O connection, you can set this attribute to TRUE.4COS Inhibit Timer—Applies to the COS I/O Object of the master.This attribute configures the minimum delay time between subsequent data productions. This attribute limits the amount of network traffic used for COS messages from devices with frequently changing I/O.The default is 0 as the DeviceNet Specification specifies. When the value is 0, NI-IndCom for DeviceNet does not limit the network for COS messages.5<User Supplied AttrID>—Identifies a user-supplied attribute. Apply to both the master and the slave.6Keep Explicit Messaging—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute ensures that an Explicit Messaging connection to the device remains open.The default is TRUE. When this attribute is TRUE by default, NI-IndCom for DeviceNet sends the Get Single Attribute service to the device every few seconds to ensure that the Explicit Messaging connection does not time out. When this attribute is FALSE, NI-IndCom for DeviceNet does not ping the Explicit Messaging connection.7Termination Resistor—Applies to the Interface Object of both the master and the slave.This attribute indicates whether to use the onboard termination of the NI-IndCom for DeviceNet interface. The termination is a 120 Ω resistor. In a typical High-Speed CAN network, the termination of the network is on the BUS. However, you can use the onboard termination to simplify testing. Set this attribute to TRUE to use the onboard termination.The default is FALSE.8Reset State—Applies to the Interface Object of the slave.This attribute removes all previous Reset request messages.The default is 0 and the value can only be 0. When the value is 0, NI-IndCom for DeviceNet removes all previous Reset request messages from the Interface Object of the slave.9Ack Timer—Applies to the I/O Object of the master.This attribute specifies the time that the NI-IndCom for DeviceNet software waits for acknowledgement before resending messages.The default is 16. The value ranges from 1 to 65,535. |
| 0 | Vendor ID—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute specifies a number that the Open Device Vendor's Association (ODVA) assigns to the device vendor. If this attribute is different from the Vendor ID of your slave device, NI-IndCom for DeviceNet returns the error DnetErrDevInitVendor.The default is 0. When Vendor ID is 0, NI-IndCom for DeviceNet does not verify the Vendor ID of your device. |
| 1 | Product Code—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute provides a vendor-specific value that identifies a particular product within a device type. If this attribute is different from the Product Code of your slave device, NI-IndCom for DeviceNet returns the error DnetErrDevInitProdCode.The default is 0. When Product Code is 0, NI-IndCom for DeviceNet does not verify the Product Code of your device. |
| 2 | Device Type—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute verifies whether the Device Type is the one that your application expects. If this attribute is different from the Device Type of your slave device, NI-IndCom for DeviceNet returns the error DnetErrDevInitDevType.The default is 0. When Device Type is 0, NI-IndCom does not verify the Device Type of your device. |
| 3 | COS/Cyclic Ack Suppress (Default) —Applies to Change of State (COS) and Cyclic I/O Objects of the master.This attribute determines whether you use the acknowledgements (FALSE) or suppress the acknowledgements (TRUE). NI-IndCom for DeviceNet produces the acknowledgement when input length of the Easy IO Config VI or the Open DeviceNet IO VI is nonzero. NI-IndCom for DeviceNet consumes the acknowledgement when output length of the same two VIs is nonzero.The default is FALSE. NI-IndCom for DeviceNet can suppress the acknowledgement after verifying the successful device operation. For example, if you open a polled I/O connection in addition to the COS or Cyclic I/O connection, you can set this attribute to TRUE. |
| 4 | COS Inhibit Timer—Applies to the COS I/O Object of the master.This attribute configures the minimum delay time between subsequent data productions. This attribute limits the amount of network traffic used for COS messages from devices with frequently changing I/O.The default is 0 as the DeviceNet Specification specifies. When the value is 0, NI-IndCom for DeviceNet does not limit the network for COS messages. |
| 5 | <User Supplied AttrID>—Identifies a user-supplied attribute. Apply to both the master and the slave. |
| 6 | Keep Explicit Messaging—Applies to the Explicit Messaging Object and I/O Object of the master.This attribute ensures that an Explicit Messaging connection to the device remains open.The default is TRUE. When this attribute is TRUE by default, NI-IndCom for DeviceNet sends the Get Single Attribute service to the device every few seconds to ensure that the Explicit Messaging connection does not time out. When this attribute is FALSE, NI-IndCom for DeviceNet does not ping the Explicit Messaging connection. |
| 7 | Termination Resistor—Applies to the Interface Object of both the master and the slave.This attribute indicates whether to use the onboard termination of the NI-IndCom for DeviceNet interface. The termination is a 120 Ω resistor. In a typical High-Speed CAN network, the termination of the network is on the BUS. However, you can use the onboard termination to simplify testing. Set this attribute to TRUE to use the onboard termination.The default is FALSE. |
| 8 | Reset State—Applies to the Interface Object of the slave.This attribute removes all previous Reset request messages.The default is 0 and the value can only be 0. When the value is 0, NI-IndCom for DeviceNet removes all previous Reset request messages from the Interface Object of the slave. |
| 9 | Ack Timer—Applies to the I/O Object of the master.This attribute specifies the time that the NI-IndCom for DeviceNet software waits for acknowledgement before resending messages.The default is 16. The value ranges from 1 to 65,535. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | attribute ID used returns the attribute ID you used. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=wait-for-state-vi.html language=enus -->
## TOPIC 00051: Wait For State VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `wait-for-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/wait-for-state-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Waits for the Established state or the Read Avail state of an Explicit Messaging Object, an I/O Object, or a CAN Frame Read Object. While waiting for the desired states, this VI suspends the current execution. You can access your front panel and execute the other VIs th

### Wait For State VI

**Owning Palette:** DeviceNet VIs

Waits for the Established state or the Read Avail state of an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message), an [I/O Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_io_object), or a CAN Frame Read Object.

While waiting for the desired states, this VI suspends the current execution. You can access your front panel and execute the other VIs that are not directly connected to this VI.

[IMAGE alt='image' src='images/Wait_For_State.gif']

|  | object handle in specifies the object handle of the object that you want to wait for state. The object can be an Explicit Messaging Object, an I/O Object, or a CAN Frame Read Object. |
| --- | --- |
|  | desired state specifies the state that the DeviceNet interface waits for. 0Read Avail—(Default)For the I/O Object, the Read Avail state works when the I/O Object receives a new input message from the network. The Read Avail state clears when you use the Read DeviceNet IO VI. For example, for a Change-of-State (COS) connection type I/O Object, the Read Avail state works when you receive a COS input message.For the Explicit Messaging Object, the Read Avail state works when you receive an Explicit Message response from the network. The Read Avail state does not clear when you use the Read DeviceNet Explicit Message VI. You can receive an Explicit Message response only after you send an explicit message request using the Write DeviceNet Explicit Message VI.For the CAN Frame Read Object, the CAN Frame Read Object keeps CAN frames in a queue when the CAN Frame Read Object receives CAN frames. The Read Avail state works when any CAN frame is in the queue. You can use the Read CAN Frame VI to read one CAN frame each time and remove this CAN frame from the queue.1Established—For the Explicit Messaging Object, the Established state is not established before you start communication using the Operate DeviceNet Interface VI. After you start communication, the Established state is not established until the Explicit Message connection has been successfully established with the remote DeviceNet device. After establishing the Explicit Message connection, the Established state establishes and remains as long as the Explicit Message connection is open. Before you use any of these VIs in your application, you must first wait for the Established state to set. After the Established state sets, unless communication problems occur with the device returning the error CanErrFunctionTimeout, the Established state remains until you stop communication using the Operate DeviceNet Interface VI. |
| 0 | Read Avail—(Default)For the I/O Object, the Read Avail state works when the I/O Object receives a new input message from the network. The Read Avail state clears when you use the Read DeviceNet IO VI. For example, for a Change-of-State (COS) connection type I/O Object, the Read Avail state works when you receive a COS input message.For the Explicit Messaging Object, the Read Avail state works when you receive an Explicit Message response from the network. The Read Avail state does not clear when you use the Read DeviceNet Explicit Message VI. You can receive an Explicit Message response only after you send an explicit message request using the Write DeviceNet Explicit Message VI.For the CAN Frame Read Object, the CAN Frame Read Object keeps CAN frames in a queue when the CAN Frame Read Object receives CAN frames. The Read Avail state works when any CAN frame is in the queue. You can use the Read CAN Frame VI to read one CAN frame each time and remove this CAN frame from the queue. |
| 1 | Established—For the Explicit Messaging Object, the Established state is not established before you start communication using the Operate DeviceNet Interface VI. After you start communication, the Established state is not established until the Explicit Message connection has been successfully established with the remote DeviceNet device. After establishing the Explicit Message connection, the Established state establishes and remains as long as the Explicit Message connection is open. Before you use any of these VIs in your application, you must first wait for the Established state to set. After the Established state sets, unless communication problems occur with the device returning the error CanErrFunctionTimeout, the Established state remains until you stop communication using the Operate DeviceNet Interface VI. |
|  | timeout specifies the maximum time, in milliseconds, to wait for one of the desired states. The default is 0 ms. If timeout expires before one of the desired states occurs, this VI returns an error. Set the value of timeout to FFFFFFFF hex to wait indefinitely. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | current state returns the current state of the object. If one of the desired states occurs, the state provides the current value of the Read Avail and Established states. If timeout expires before one of the desired states occurs, this output returns 0. If the state is Read Avail, the value is 1 hex. If the state is Established, the value is 8 hex. If the states are a combination of Read Avail and Established, the value is 9 hex. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=write-can-frame-vi.html language=enus -->
## TOPIC 00052: Write CAN Frame VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `write-can-frame-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/write-can-frame-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Sends a CAN frame on the DeviceNet bus. Use this VI to implement advanced CAN applications. object handle in specifies the object handle of the object that you want to use to send the CAN frames. You can only generate this handle by using the Open DeviceNet Interface VI.

### Write CAN Frame VI

**Owning Palette:** Advanced VIs

Sends a CAN frame on the DeviceNet bus. Use this VI to implement advanced CAN applications.

[IMAGE alt='image' src='images/Write_CAN_Frame.gif']

|  | object handle in specifies the object handle of the object that you want to use to send the CAN frames. You can only generate this handle by using the Open DeviceNet Interface VI. |
| --- | --- |
|  | arbitration ID specifies the arbitration ID of the CAN frame that you want to send. DeviceNet uses 11-bit COB-IDs and supports 29-bit COB-IDs. If the COB-ID is a 11-bit COB-ID, the bit 29 (0-based) should be 0. If the COB-ID is a 29-bit COB-ID, the bit 29 (0-based) should be 1. The default is 0. |
|  | CAN message data specifies the data of the CAN frame. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RTR? specifies whether this frame is a remote transmission request (RTR). The default is FALSE. |
|  | object handle out returns the object handle of the Interface Object. Use this output in subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=write-devicenet-explicit-message-vi.html language=enus -->
## TOPIC 00053: Write DeviceNet Explicit Message VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `write-devicenet-explicit-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/write-devicenet-explicit-message-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Advanced VIs Writes an Explicit Message request using an Explicit Messaging Object. service data specifies the service data bytes for the request. The format of this data is specific to the service code. The default is 0. For object-specific service codes, the object specification de

### Write DeviceNet Explicit Message VI

**Owning Palette:** Advanced VIs

Writes an Explicit Message request using an [Explicit Messaging Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_explicit_message).

[IMAGE alt='image' src='images/Write_DeviceNet_Explicit_Message.gif']

|  | service data specifies the service data bytes for the request. The format of this data is specific to the service code. The default is 0. For object-specific service codes, the object specification defines the format of the data. For vendor-specific service codes, the device vendor defines the format of the data. The service data length input specifies the number of the service data bytes you want to send in the request. Refer to the DeviceNet Specification, the Electronic Data Sheets (EDS), or the specification of a remote device for more information about service data and service data length. |
| --- | --- |
|  | service code specifies the service that you request for. The default is 0. |
|  | object handle in specifies the object handle of the object that you want to use to write DeviceNet Explicit Message. |
|  | class ID specifies the class ID. The value ranges from 0 to FFFF hex. The default is 0. The device vendor provides vendor-specific classes. Although the DeviceNet Specification allows 16-bit class IDs, most class IDs are 8-bit. NI-IndCom for DeviceNet uses the class ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | instance ID specifies the instance ID. The value ranges from 0 to FFFF hex. The default is 0. DeviceNet reserves instance ID 0 to get an attribute from the class itself. Use values other than 0 to get the attribute from other instances within the class. For example, the primary Identity Object in a device uses instance ID 1. Although the DeviceNet Specification allows both 8-bit and 16-bit instance IDs, most instance IDs are 8-bit. NI-IndCom for DeviceNet uses the instance ID size, 16-bit or 8-bit, that is appropriate for your device. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | service data length specifies the number of service data bytes for request. The length also specifies the number of bytes provided in service data. The value ranges from 0 to 240. The default is 0. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Advanced VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet-api-ref path=write-devicenet-io-vi.html language=enus -->
## TOPIC 00054: Write DeviceNet IO VI

- bundle_id: `ni-industrial-communications-devicenet-api-ref`
- source_path: `write-devicenet-io-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet-api-ref/raw/resource/enus/write-devicenet-io-vi.html
- document_id: `ni-industrial-communications-devicenet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DeviceNet VIs Writes output data to an I/O Object. Because each I/O Object continuously produces output data onto the DeviceNet network at a specified rate, using this VI multiple times for each output data is redundant and wastes processor time. To minimize the redundancy, you can u

### Write DeviceNet IO VI

**Owning Palette:** DeviceNet VIs

Writes output data to an [I/O Object](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_io_object).

Because each I/O Object continuously produces output data onto the DeviceNet network at a specified rate, using this VI multiple times for each output data is redundant and wastes processor time. To minimize the redundancy, you can use this VI to write data to I/O Objects regularly according to the [Expected Packet Rate](/csh?context=ni-industrial-communications-devicenet_indcomdnet_dv_epr) value.

[IMAGE alt='image' src='images/Write_DeviceNet_IO.gif']

|  | object handle in specifies the object handle of the object that you use to write to the I/O Object. The object can only be an I/O Object. |
| --- | --- |
|  | data specifies the data bytes that NI-IndCom for DeviceNet sends out. The default is 0. Refer to the documentation of the device vendor or the DeviceNet Specification for information of the format of the output assembly. The bytes of the output assembly of a device often consist of multiple data members. To obtain each data member from the input bytes, use the Convert From DeviceNet Read VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | object handle out returns the object handle that passes through this VI as an output so that you can use this output for subsequent VIs for this object. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

DeviceNet VIs
