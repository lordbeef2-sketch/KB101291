# NI DOCUMENT BUNDLE: ni-modinst-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-modinst-lvnxg-api-ref start=1 end=6 -->
<!--NI_TOPIC bundle=ni-modinst-lvnxg-api-ref path=close-installed-devices-session.html language=enus -->
## TOPIC 00001: Close Installed Devices Session

- bundle_id: `ni-modinst-lvnxg-api-ref`
- source_path: `close-installed-devices-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-lvnxg-api-ref/raw/resource/enus/close-installed-devices-session.html
- document_id: `ni-modinst-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-ModInst session and deletes the session handle. session in Handle of the session to close. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error in

Close Installed Devices Session

Closes an NI-ModInst session and deletes the session handle.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session in

Handle of the session to close.

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

Parent topic:

NI-ModInst Nodes

<!--NI_TOPIC bundle=ni-modinst-lvnxg-api-ref path=get-installed-device-attribute-i32.html language=enus -->
## TOPIC 00002: I32

- bundle_id: `ni-modinst-lvnxg-api-ref`
- source_path: `get-installed-device-attribute-i32.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-lvnxg-api-ref/raw/resource/enus/get-installed-device-attribute-i32.html
- document_id: `ni-modinst-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the specified integer attribute. session in Session handle created by niModinst Open Installed Devices Session. index in Zero-based index that specifies the device for which you want the attribute. Valid Range device count device count niModinst Open Installed Devices Session attribute ID ID

I32

Returns the specified integer attribute.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session in

Session handle created by niModinst Open Installed Devices Session.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index in

Zero-based index that specifies the device for which you want the attribute.

##### Valid Range

device count

device count

niModinst Open Installed Devices Session

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### attribute ID

ID of the integer attribute you want to query.

| Value | Attribute |
| --- | --- |
| Slot Number | The chassis slot in which the device is installed. This attribute can only be queried for PXI modules installed in a chassis that has been properly identified in MAX. |
| Chassis Number | The number of the chassis in which the device is installed. This attribute can only be queried for PXI modules installed in a chassis that has been properly identified in MAX. |
| Bus Number | The bus on which the device or module has been enumerated. |
| Socket Number | The socket number on which the device has been enumerated. |

Note

n

x

n

x

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session out

Session handle identical to the session in handle.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### index out

Zero-based index identical to the index in value.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### attribute value

Value of the requested attribute.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Get Installed Device Attribute

<!--NI_TOPIC bundle=ni-modinst-lvnxg-api-ref path=get-installed-device-attribute-string.html language=enus -->
## TOPIC 00003: String

- bundle_id: `ni-modinst-lvnxg-api-ref`
- source_path: `get-installed-device-attribute-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-lvnxg-api-ref/raw/resource/enus/get-installed-device-attribute-string.html
- document_id: `ni-modinst-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a specified string attribute. session in Session handle created by niModinst Open Installed Devices Session. index in Zero-based index that specifies the device for which you want the attribute. Valid Range device count device count niModinst Open Installed Devices Session attribute ID ID of

String

Returns a specified string attribute.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session in

Session handle created by niModinst Open Installed Devices Session.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index in

Zero-based index that specifies the device for which you want the attribute.

##### Valid Range

device count

device count

niModinst Open Installed Devices Session

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### attribute ID

ID of the string attribute you want to query.

| Value | Returned Attribute |
| --- | --- |
| Device Name | The name of the device, which you can use to open an instrument driver session for that device. |
| Device Model | The model of the device. |
| Serial Number | The serial number of the device. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session out

Session handle identical to the session in handle.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### index out

Zero-based index identical to the index in value.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### attribute value

Value of the requested attribute.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Get Installed Device Attribute

<!--NI_TOPIC bundle=ni-modinst-lvnxg-api-ref path=get-installed-device-attribute.html language=enus -->
## TOPIC 00004: Get Installed Device Attribute

- bundle_id: `ni-modinst-lvnxg-api-ref`
- source_path: `get-installed-device-attribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-lvnxg-api-ref/raw/resource/enus/get-installed-device-attribute.html
- document_id: `ni-modinst-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an attribute for a device. Use the index in parameter to select a device from a session handle created by Open Installed Devices Session.

Get Installed Device Attribute

Returns an attribute for a device.
 Use the index in parameter to select a device from a session handle created by Open Installed Devices Session.

NI-ModInst Nodes

Get information about modular instruments installed in your system.

I32

Returns the specified integer attribute.

String

Returns a specified string attribute.

Parent topic:

NI-ModInst Nodes

<!--NI_TOPIC bundle=ni-modinst-lvnxg-api-ref path=open-installed-devices-session.html language=enus -->
## TOPIC 00005: Open Installed Devices Session

- bundle_id: `ni-modinst-lvnxg-api-ref`
- source_path: `open-installed-devices-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-lvnxg-api-ref/raw/resource/enus/open-installed-devices-session.html
- document_id: `ni-modinst-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a handle to a list of installed devices supported by the specified driver. Call this node and select the name of a National Instruments instrument driver, such as NI-SCOPE, from the driver control. This node searches the system and constructs a list of all the installed devices that are supp

Open Installed Devices Session

Creates a handle to a list of installed devices supported by the specified driver. Call this node and select the name of a National Instruments instrument driver, such as NI-SCOPE, from the driver control. This node searches the system and constructs a list of all the installed devices that are supported by that driver, and returns both a handle and the number of devices found. The handle is used with other functions to query for attributes such as device name and model, and to safely discard the list when finished.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### driver

Specifies the driver whose supported devices you want to find.

Note

session

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session out

The opened NI-ModInst session.

This acts as a handle to the list of installed devices and is used in other NI-ModInst functions.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### device count

Returns the number of devices found in the system that are supported by the driver specified in the driver parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-ModInst Nodes

<!--NI_TOPIC bundle=ni-modinst-lvnxg-api-ref path=overview.html language=enus -->
## TOPIC 00006: NI-ModInst Nodes

- bundle_id: `ni-modinst-lvnxg-api-ref`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-lvnxg-api-ref/raw/resource/enus/overview.html
- document_id: `ni-modinst-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get information about modular instruments installed in your system.

NI-ModInst Nodes

Get information about modular instruments installed in your system.

Open Installed Devices Session

Creates a handle to a list of installed devices supported by the specified driver.

Get Installed Device Attribute

Returns an attribute for a device. Use the index in parameter to select a device from a session handle created by Open Installed Devices Session.

Close Installed Devices Session

Closes an NI-ModInst session and deletes the session handle.
