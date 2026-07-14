# NI DOCUMENT BUNDLE: ni-modinst-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-modinst-labview-api-ref start=1 end=8 -->
<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/dir-mnu.html language=enus -->
## TOPIC 00001: NI-ModInst

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/dir-mnu.html
- document_id: `ni-modinst-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI-ModInst to query the system for information about installed NI Modular Instruments devices. icon

### NI-ModInst

Use NI-ModInst to query the system for information about installed NI Modular Instruments devices.

[IMAGE alt='icon' src='dir-mnu.png']

- [niModInst Open Installed Devices Session VI](../../instr-lib/nimodinst/nimodinst-open-installed-devices-session-vi.html) Creates a handle to a list of installed devices supported by the specified driver. Call this VI and select the name of a National Instruments instrument driver, such as NI-SCOPE, from the driver control. This VI searches the system and constructs a list of all the installed devices that are supported by that driver, and returns both a handle and the number of devices found. The handle is used with other functions to query for attributes such as device name and model, and to safely discard the list when finished.
- [niModInst Get Installed Device Attribute (poly) VI](../../instr-lib/nimodinst/nimodinst-get-installed-device-attribute-poly-vi.html) Returns an attribute (either an integer or a string) specified by the attribute ID parameter for a device specified by the session in and index in parameters.
- [niModInst Close Installed Devices Session VI](../../instr-lib/nimodinst/nimodinst-close-installed-devices-session-vi.html) Cleans up the NI-ModInst session created by a call to niModInst Open Installed Devices Session . Call this VI when you are finished using the session handle and do not use this handle again.

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/nimodinst-close-installed-devices-session-vi.html language=enus -->
## TOPIC 00002: niModInst Close Installed Devices Session VI

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/nimodinst-close-installed-devices-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/nimodinst-close-installed-devices-session-vi.html
- document_id: `ni-modinst-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cleans up the NI-ModInst session created by a call to niModInst Open Installed Devices Session. Call this VI when you are finished using the session handle and do not use this handle again. icon Inputs/Outputs cgenclassrn.png session session is the NI-ModInst session handle, which acts as a handle t

### niModInst Close Installed Devices Session VI

Cleans up the NI-ModInst session created by a call to [niModInst Open Installed Devices Session](nimodinst-open-installed-devices-session-vi.html). Call this VI when you are finished using the session handle and do not use this handle again.

[IMAGE alt='icon' src='nimodinst-close-installed-devices-session-vi.png']

#### Inputs/Outputs

| session — session is the NI-ModInst session handle, which acts as a handle to the list of installed devices and is used in other NI-ModInst functions. error in (no error) — error in describes error conditions that occur before this VI or function runs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

NI-ModInst

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/nimodinst-get-installed-device-attribute-i32-vi.html language=enus -->
## TOPIC 00003: niModInst Get Installed Device Attribute (I32) VI

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/nimodinst-get-installed-device-attribute-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/nimodinst-get-installed-device-attribute-i32-vi.html
- document_id: `ni-modinst-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an integer attribute specified by the attribute ID parameter for a device specified by the session in and index in parameters. The session in parameter is expected to be a valid handle returned by niModInst Open Installed Devices Session. Therefore, this parameter acts as a handle to a list

### niModInst Get Installed Device Attribute (I32) VI

Returns an integer attribute specified by the **attribute ID** parameter for a device specified by the **session in** and **index in** parameters.

The **session in** parameter is expected to be a valid handle returned by [niModInst Open Installed Devices Session](nimodinst-open-installed-devices-session-vi.html). Therefore, this parameter acts as a handle to a list of installed devices. The **index in** parameter specifies the device in the list for which you want the attribute.

[IMAGE alt='icon' src='nimodinst-get-installed-device-attribute-i32-vi.png']

#### Inputs/Outputs

| session in — session in is the NI-ModInst session handle created by niModInst Open Installed Devices Session. index in — index in is a zero-based index that specifies the device for which you want the attribute. The index in parameter should be between 0 and (device count – 1), inclusive, where device count is the number of installed devices returned by niModinst Open Installed Devices Session. attribute ID — attribute ID is the ID of the integer attribute you want to query. Valid Values Slot Number—the slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX. Chassis Number—the number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX. Bus Number—the bus on which the device has been enumerated. Socket Number—the socket number on which the device has been enumerated. Note The bus number and socket number can be used to form a VISA resource string for the device, of the form PXIn::x::INSTR, where n is the bus number and x is the socket number. For example, for bus number 2 and socket number 13, use PXI2::13::INSTR. error in (no error) — error in describes error conditions that occur before this VI or function runs. session out — session out has the same value as session in. index out — index out has the same value as index in. attribute value — attribute value returns the value of the requested attribute. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

niModInst Get Installed Device Attribute (poly) VI

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/nimodinst-get-installed-device-attribute-poly-vi.html language=enus -->
## TOPIC 00004: niModInst Get Installed Device Attribute (poly) VI

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/nimodinst-get-installed-device-attribute-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/nimodinst-get-installed-device-attribute-poly-vi.html
- document_id: `ni-modinst-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an attribute (either an integer or a string) specified by the attribute ID parameter for a device specified by the session in and index in parameters. The session in parameter is expected to be a valid handle returned by niModInst Open Installed Devices Session. Therefore, this parameter act

### niModInst Get Installed Device Attribute (poly) VI

Returns an attribute (either an integer or a string) specified by the **attribute ID** parameter for a device specified by the **session in** and **index in** parameters.

The **session in** parameter is expected to be a valid handle returned by [niModInst Open Installed Devices Session](nimodinst-open-installed-devices-session-vi.html). Therefore, this parameter acts as a handle to a list of installed devices. The **index in** parameter specifies the device in the list for which you want the attribute.

[IMAGE alt='icon' src='nimodinst-get-installed-device-attribute-poly-vi.png']

- [niModInst Get Installed Device Attribute (String) VI](../../instr-lib/nimodinst/nimodinst-get-installed-device-attribute-string-vi.html) Returns a string attribute specified by the attribute ID parameter for a device specified by the session in and index in parameters.
- [niModInst Get Installed Device Attribute (I32) VI](../../instr-lib/nimodinst/nimodinst-get-installed-device-attribute-i32-vi.html) Returns an integer attribute specified by the attribute ID parameter for a device specified by the session in and index in parameters.

Parent topic:

NI-ModInst

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/nimodinst-get-installed-device-attribute-string-vi.html language=enus -->
## TOPIC 00005: niModInst Get Installed Device Attribute (String) VI

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/nimodinst-get-installed-device-attribute-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/nimodinst-get-installed-device-attribute-string-vi.html
- document_id: `ni-modinst-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string attribute specified by the attribute ID parameter for a device specified by the session in and index in parameters. The session in parameter is expected to be a valid handle returned by niModInst Open Installed Devices Session. Therefore, this parameter acts as a handle to a list of

### niModInst Get Installed Device Attribute (String) VI

Returns a string attribute specified by the **attribute ID** parameter for a device specified by the **session in** and **index in** parameters.

The **session in** parameter is expected to be a valid handle returned by [niModInst Open Installed Devices Session](nimodinst-open-installed-devices-session-vi.html). Therefore, this parameter acts as a handle to a list of installed devices. The **index in** parameter specifies the device in the list for which you want the attribute.

[IMAGE alt='icon' src='nimodinst-get-installed-device-attribute-string-vi.png']

#### Inputs/Outputs

| session in — session in is the NI-ModInst session handle created by niModInst Open Installed Devices Session. index in — index in is a zero-based index that specifies the device for which you want the attribute. The index in parameter should be between 0 and (device count – 1), inclusive, where device count is the number of installed devices returned by niModinst Open Installed Devices Session. attribute ID — attribute ID is the ID of the string attribute you want to query. Valid Values Device Name—the name of the device, which can be used to open an instrument driver session for that device Device Model—the model of the device (for example, NI PXI-5122) Serial Number—the serial number of the device error in (no error) — error in describes error conditions that occur before this VI or function runs. session out — session out has the same value as session in. index out — index out has the same value as index in. attribute value — attribute value returns the value of the requested attribute. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

niModInst Get Installed Device Attribute (poly) VI

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/nimodinst-open-installed-devices-session-vi.html language=enus -->
## TOPIC 00006: niModInst Open Installed Devices Session VI

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/nimodinst-open-installed-devices-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/nimodinst-open-installed-devices-session-vi.html
- document_id: `ni-modinst-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a handle to a list of installed devices supported by the specified driver. Call this VI and select the name of a National Instruments instrument driver, such as NI-SCOPE, from the driver control. This VI searches the system and constructs a list of all the installed devices that are supporte

### niModInst Open Installed Devices Session VI

Creates a handle to a list of installed devices supported by the specified driver. Call this VI and select the name of a National Instruments instrument driver, such as NI-SCOPE, from the **driver** control. This VI searches the system and constructs a list of all the installed devices that are supported by that driver, and returns both a handle and the number of devices found. The handle is used with other functions to query for attributes such as device name and model, and to safely discard the list when finished.

Note

niModInst_Close Installed Devices Session

[IMAGE alt='icon' src='nimodinst-open-installed-devices-session-vi.png']

#### Inputs/Outputs

| driver — driver specifies the driver whose supported devices you want to find. This string is not case-sensitive. Some examples are: NI-SCOPE niScope NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If you do not wire an input or an empty string for this parameter, NI-ModInst creates a list of all Modular Instruments devices installed in the system. error in (no error) — error in describes error conditions that occur before this VI or function runs. session — session is the NI-ModInst session handle, which acts as a handle to the list of installed devices and is used in other NI-ModInst functions. device count — device count returns the number of devices found in the system that are supported by the driver specified in the driver parameter. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

NI-ModInst

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00007: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/standard-functionality-for-error-in-parameters.html
- document_id: `ni-modinst-labview-api-ref`
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

<!--NI_TOPIC bundle=ni-modinst-labview-api-ref path=instr-lib/nimodinst/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00008: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-modinst-labview-api-ref`
- source_path: `instr-lib/nimodinst/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-modinst-labview-api-ref/raw/resource/enus/instr-lib/nimodinst/standard-functionality-for-error-out-parameters.html
- document_id: `ni-modinst-labview-api-ref`
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
