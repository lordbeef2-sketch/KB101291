# NI DOCUMENT BUNDLE: ni-industrial-communications-ethernetip-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-industrial-communications-ethernetip-api-ref start=1 end=20 -->
<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=activating-your-software.html language=enus -->
## TOPIC 00001: Activating Your Software

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `activating-your-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/activating-your-software.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the Interactive Activation Guide for license activation.

### Activating Your Software

Refer to the [Interactive Activation Guide](https://ni.com/my/s/support/activation-guide) for license activation.

Parent topic:

NI-Industrial Communications for EtherNet/IP Help

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=advanced.html language=enus -->
## TOPIC 00002: Advanced

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/advanced.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Ethernet/IP Industrial CommunicationInstalled With: LabVIEWUse these VIs to explicitly open or close a session. It is generally not necessary to explicitly manage a session because sessions are opened and closed automatically. Explicitly closing a session will immediately abort any b

### Advanced

**Owning Palette:** [Ethernet/IP Industrial Communication](ethernet-ip-industrial-communication.html)**Installed With:** LabVIEW

Use these VIs to explicitly open or close a session. It is generally not necessary to explicitly manage a session because sessions are opened and closed automatically. Explicitly closing a session will immediately abort any blocking operations which are using that session.

| Palette Object | Description |
| --- | --- |
| EthernetIP Open Session | Explicitly opens a session. It is generally not necessary to explicitly open a session because sessions are opened automatically. |
| EthernetIP Close Session | Explicitly closes a session. It is generally not necessary to explicitly close a session because sessions are closed automatically. Explicitly closing a session will immediately abort any blocking operations which are using that session. |

Parent topic:

Ethernet/IP Industrial Communication

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=configuring-the-plc.html language=enus -->
## TOPIC 00003: Configuring the PLC

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `configuring-the-plc.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/configuring-the-plc.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You must configure the PLC to add the LabVIEW system as a remote I/O device. To configure the PLC using RSLogix 5000, create a new module of type Generic Ethernet Module. 29 When you configure a PLC using RSLogix 5000, you may need to adjust the following settings in the New Module dialog box. For d

### Configuring the PLC

You must configure the PLC to add the LabVIEW system as a remote I/O device. To configure the PLC using RSLogix 5000, create a new module of type **Generic Ethernet Module**.

Figure 29.

[IMAGE alt='image' src='images/RockwellConfiguration.gif']

When you configure a PLC using RSLogix 5000, you may need to adjust the following settings in the New Module dialog box. For detailed instructions, consult the documentation for your software.

| Control Name | Description |
| --- | --- |
| Comm Format | Specifies the data type of the assembly array on the PLC. |
| Input | Corresponds to the producing assembly on the LabVIEW system. The following controls are available: Assembly Instance–specifies the instance ID of the assembly Size–specifies the size of the assembly |
| Output | Corresponds to the consuming assembly on the LabVIEW system. The following controls are available: Assembly Instance–specifies the instance ID of the assembly Size–specifies the size of the assembly |
| Configuration | Corresponds to the configuration assembly on the LabVIEW system. The following controls are available: Assembly Instance–specifies the instance ID of the assembly Size–specifies the size of the assembly. The size of the configuration assembly can typically remain set as 0 to indicate that it is unused. |

Parent topic:

I/O Data

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=error-codes.html language=enus -->
## TOPIC 00004: Error Codes

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `error-codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/error-codes.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ethernet/IP VIs can return the following error codes. Error CodeDescription –251723776 Internal Error. –251723775 Operation has been cancelled. –251723774 The data amount requested is too large. –251723773 The data type returned for the request does not match the data type requested by the user. –25

### Error Codes

Ethernet/IP VIs can return the following error codes.

| Error Code | Description |
| --- | --- |
| –251723776 | Internal Error. |
| –251723775 | Operation has been cancelled. |
| –251723774 | The data amount requested is too large. |
| –251723773 | The data type returned for the request does not match the data type requested by the user. |
| –251723772 | The tag name is not correctly formatted. |
| –251723771 | The requested session name is already in use. |
| –251723770 | The session is invalid. |
| –251723769 | Not enough free memory to complete the operation. |
| –251723768 | The session name is invalid. |
| –251723767 | Unable to connect to the network path specified. |
| –251723766 | Unknown error. |
| –251723765 | Error initializing the Ethernet/IP stack. |
| –251723764 | Too many concurrent network peers. |
| –251723763 | Too many concurrent network connections. |
| –251723762 | Too many pending object requests. |
| –251723761 | Too many multiple service requests. |
| –251723760 | CIP Error—Extended status may be available. |
| –251723759 | The attribute requested is unknown. |
| –251723758 | The attribute being set is out of range. |
| –251723757 | The specified assembly instance ID already exists. |
| –251723756 | The specified assembly instance ID already exists in a different session. |
| –251723755 | The specified assembly type is invalid. |
| –251723754 | The specified assembly instance ID was not found. |
| –251723753 | The length of the assembly data exceeds the length of the assembly. |
| –251723752 | The request response was not received in the requested timeout period. |
| –251723751 | The specified connection instance is invalid. |
| –251723750 | The maximum number of assemblies has been reached. |
| –251723749 | Unable to allocate space within the assembly buffers. |
| –251723748 | The specified assembly size is too large. |
| –251723747 | The specified assembly is in use by one or more active connections. |
| –251723746 | Unable to bind to the local IP address. |
| –251723745 | PCCC status error. |
| –251723744 | Calculated masked write bitmask is larger than 16 bits wide. |
| –251723743 | Bitmask provided does not match data size. |
| –251723742 | A new request for a currently populated request group specifies a different target IP or host IP. |
| –251723741 | An unknown index was specified when trying to get an object response. |
| –251723740 | The response on the request sent has not yet been received. |
| –251723739 | The specified offset and size combination overlap with an already configured assembly. |
| –251723738 | The specified assembly instance has not been configured. |
| –251723737 | A NULL Forward Open request was made while an existing one still is being processed. |
| –251723736 | An input parameter for opening a connection is invalid. |
| –251723735 | The message data size for a class3 connection is too large. |
| –251723734 | The buffer size is too small for STRINGI. |
| –251723733 | The specified operation is not supported. |
| –251723732 | The STRINGI data format is not correct. |
| –251723731 | The specified assembly name already exists. |

Parent topic:

Ethernet/IP Industrial Communication

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernet-ip-industrial-communication.html language=enus -->
## TOPIC 00005: Ethernet/IP Industrial Communication

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernet-ip-industrial-communication.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernet-ip-industrial-communication.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Installed With: LabVIEWThe Ethernet/IP Industrial Protocol Support API allows a LabVIEW system to communicate with devices on an EtherNet/IP network. The API supports Explicit Messaging and I/O Data communications. Subpalette Description Messaging The VIs on this palette use explicit messaging conne

### Ethernet/IP Industrial Communication

**Installed With:** LabVIEW

The Ethernet/IP Industrial Protocol Support API allows a LabVIEW system to communicate with devices on an EtherNet/IP network. The API supports Explicit Messaging and I/O Data communications.

| Subpalette | Description |
| --- | --- |
| Messaging | The VIs on this palette use explicit messaging connections to read from or write to a target. |
| I/O Data | The VIs on this palette allow the LabVIEW system to create an I/O assembly and function as an adapter for a remote PLC. This type of communication is referred to as Class 1 or I/O server communication. Class 1 communication allows the PLC to establish an implicit I/O data connection with the LabVIEW system and repeatedly exchange assembly data at a specific rate. |
| Advanced | Use these VIs to explicitly open or close a session. It is generally not necessary to explicitly manage a session because sessions are opened and closed automatically. Explicitly closing a session will immediately abort any blocking operations which are using that session. |

Parent topic:

NI-Industrial Communications for EtherNet/IP Help

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-add-assembly-instance-vi.html language=enus -->
## TOPIC 00006: EthernetIP Add Assembly Instance VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-add-assembly-instance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-add-assembly-instance-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: I/O DataInstalled With: LabVIEWAllows the LabVIEW system to create an I/O assembly and function as an adapter for a remote PLC. Assemblies are treated as shared memory that is used to produce or consume data. A producing assembly provides input to the PLC. A consuming assembly accept

### EthernetIP Add Assembly Instance VI

**Owning Palette:** [I/O Data](i-o-data.html)**Installed With:** LabVIEW

Allows the LabVIEW system to create an I/O assembly and function as an adapter for a remote PLC.

Assemblies are treated as shared memory that is used to produce or consume data. A producing assembly provides input to the PLC. A consuming assembly accepts output from the PLC. The PLC uses an instance ID to map each assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. Refer to [Configuring the PLC](configuring-the-plc.html) for more information about configuring the PLC.

Figure 25.

[IMAGE alt='image' src='images/EthernetIP_Add_Assembly_Instance.gif']

|  | Name (optional) provides an optional name to identify the assembly. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Instance ID in specifies the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | Type specifies the type of the assembly. Valid values are Producing, Consuming, and Configuration. A producing assembly provides input to the PLC. A consuming assembly accepts output from the PLC. A configuration assembly transfers configuration parameters. Configuration assemblies are not recommended for normal use. |
|  | Size (bytes) specifies the number of 8-bit bytes of data that the assembly contains. You may need to convert the size if the PLC is configured to use a different word size. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Instance ID out provides the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

I/O Data

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-cip-get-attribute-single-vi.html language=enus -->
## TOPIC 00007: EthernetIP CIP Get Attribute Single VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-cip-get-attribute-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-cip-get-attribute-single-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: MessagingInstalled With: LabVIEWAllows you to read attribute information from a CIP object. 23 Timeout (ms) is the operation timeout limit in milliseconds. Session in represents the current session used for the operation. Network Path is typically the IP address of the remote PLC tar

### EthernetIP CIP Get Attribute Single VI

**Owning Palette:** [Messaging](messaging.html)**Installed With:** LabVIEW

Allows you to read attribute information from a CIP object.

Figure 23.

[IMAGE alt='image' src='images/EthernetIP_CIP_Get_Attribute_Single.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | error in describes the error status before this VI or function runs. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Class specifies the class of the CIP object. For example, a value of 0x01 indicates the identity object. |
|  | Instance specifies the instance of the CIP object. For example, a value of 0x01 indicates the first instance of the object. |
|  | Attribute specifies the attribute of the CIP object. For example, with the identity object, a value of 0x01 indicates the product vendor ID. |
|  | Session out represents the current session used for the operation. |
|  | Data returns an array of bytes from the attribute. The size of the data matches the size of the attribute. The format of the data varies according to the specification of the CIP object and attrbute. |
|  | error out contains error information. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Messaging

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-cip-set-attribute-single-vi.html language=enus -->
## TOPIC 00008: EthernetIP CIP Set Attribute Single VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-cip-set-attribute-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-cip-set-attribute-single-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: MessagingInstalled With: LabVIEWAllows you to write attribute information to a CIP object. 24 Timeout (ms) is the operation timeout limit in milliseconds. Session in represents the current session used for the operation. Data specifies an array of bytes to write to the attribute. The

### EthernetIP CIP Set Attribute Single VI

**Owning Palette:** [Messaging](messaging.html)**Installed With:** LabVIEW

Allows you to write attribute information to a CIP object.

Figure 24.

[IMAGE alt='image' src='images/EthernetIP_CIP_Set_Attribute_Single.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Data specifies an array of bytes to write to the attribute. The size of the data must match the size of the attribute. The format of the data varies according to the specification of the CIP object and attrbute. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | error in describes the error status before this VI or function runs. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Class specifies the class of the CIP object. For example, a value of 0x01 indicates the identity object. |
|  | Instance specifies the instance of the CIP object. For example, a value of 0x01 indicates the first instance of the object. |
|  | Attribute specifies the attribute of the CIP object. For example, with the identity object, a value of 0x01 indicates the product vendor ID. |
|  | Session out represents the current session used for the operation. |
|  | error out contains error information. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Messaging

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-close-session-vi.html language=enus -->
## TOPIC 00009: EthernetIP Close Session VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-close-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-close-session-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: AdvancedInstalled With: LabVIEWExplicitly closes a session. It is generally not necessary to explicitly close a session because sessions are closed automatically. Explicitly closing a session will immediately abort any blocking operations which are using that session. 31 Session in r

### EthernetIP Close Session VI

**Owning Palette:** [Advanced](advanced.html)**Installed With:** LabVIEW

Explicitly closes a session. It is generally not necessary to explicitly close a session because sessions are closed automatically. Explicitly closing a session will immediately abort any blocking operations which are using that session.

Figure 31.

[IMAGE alt='image' src='images/EthernetIP_Close_Session.gif']

|  | Session in represents the current session used for the operation. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-get-assembly-instance-data-vi.html language=enus -->
## TOPIC 00010: EthernetIP Get Assembly Instance Data VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-get-assembly-instance-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-get-assembly-instance-data-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: I/O DataInstalled With: LabVIEWReads the data in an assembly as one large block of data. The access to the data is atomic, which means that all the data must be read at once. Because the data is read as a raw bytestream, you must convert the data to the correct data type. In LabVIEW,

### EthernetIP Get Assembly Instance Data VI

**Owning Palette:** [I/O Data](i-o-data.html)**Installed With:** LabVIEW

Reads the data in an assembly as one large block of data. The access to the data is atomic, which means that all the data must be read at once.

Because the data is read as a raw bytestream, you must convert the data to the correct data type. In LabVIEW, use the Unflatten From String function to convert the data to a specific data type. Note that you must specify little-endian byte order.

On the PLC, the assembly is created as an array of a single, fixed data type. If the assembly data type does not match the data type used for fields within the assembly, you can use the COP or CPS commands within RSLogix5000 to extract the data and cast it into the appropriate data type.

Figure 27.

[IMAGE alt='image' src='images/EthernetIP_Get_Assembly_Instance_Data.gif']

|  | Session in represents the current session used for the operation. |
| --- | --- |
|  | Instance ID in specifies the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Instance ID out provides the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | Data returns data from a tag as an array of 8-bit unsigned integers. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

I/O Data

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-open-session-vi.html language=enus -->
## TOPIC 00011: EthernetIP Open Session VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-open-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-open-session-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: AdvancedInstalled With: LabVIEWExplicitly opens a session. It is generally not necessary to explicitly open a session because sessions are opened automatically. 30 Session in represents the current session used for the operation. error in describes the error status before this VI or

### EthernetIP Open Session VI

**Owning Palette:** [Advanced](advanced.html)**Installed With:** LabVIEW

Explicitly opens a session. It is generally not necessary to explicitly open a session because sessions are opened automatically.

Figure 30.

[IMAGE alt='image' src='images/EthernetIP_Open_Session.gif']

|  | Session in represents the current session used for the operation. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-remove-assembly-instance-vi.html language=enus -->
## TOPIC 00012: EthernetIP Remove Assembly Instance VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-remove-assembly-instance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-remove-assembly-instance-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: I/O DataInstalled With: LabVIEWAllows the LabVIEW system to destroy an I/O assembly. 26 Session in represents the current session used for the operation. Instance ID specifies the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instan

### EthernetIP Remove Assembly Instance VI

**Owning Palette:** [I/O Data](i-o-data.html)**Installed With:** LabVIEW

Allows the LabVIEW system to destroy an I/O assembly.

Figure 26.

[IMAGE alt='image' src='images/EthernetIP_Remove_Assembly_Instance.gif']

|  | Session in represents the current session used for the operation. |
| --- | --- |
|  | Instance ID specifies the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

I/O Data

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-set-assembly-instance-data-vi.html language=enus -->
## TOPIC 00013: EthernetIP Set Assembly Instance Data VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-set-assembly-instance-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-set-assembly-instance-data-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: I/O DataInstalled With: LabVIEWWrites the data to an assembly as one large block of data. The access to the data is atomic, which means that all the data must be read at once. Because the data is written as a raw bytestream, you must convert the data to the correct data type. In LabV

### EthernetIP Set Assembly Instance Data VI

**Owning Palette:** [I/O Data](i-o-data.html)**Installed With:** LabVIEW

Writes the data to an assembly as one large block of data. The access to the data is atomic, which means that all the data must be read at once.

Because the data is written as a raw bytestream, you must convert the data to the correct data type. In LabVIEW, use the Flatten To String function to convert the data to a specific data type. Note that you must specify little-endian byte order.

On the PLC, the assembly is created as an array of a single, fixed data type. If the assembly data type does not match the data type used for fields within the assembly, you can use the COP or CPS commands within RSLogix5000 to extract the data and cast it into the appropriate data type.

Figure 28.

[IMAGE alt='image' src='images/EthernetIP_Set_Assembly_Instance_Data.gif']

|  | Session in represents the current session used for the operation. |
| --- | --- |
|  | Instance ID in specifies the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | Data accepts an array of 8-bit unsigned integer type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Instance ID out provides the instance ID of the assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

I/O Data

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-slc500-read-vi.html language=enus -->
## TOPIC 00014: EthernetIP SLC500 Read VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-slc500-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-slc500-read-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: MessagingInstalled With: LabVIEWAllows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as the SLC 500 and MicroLogix series from Rockwell Automation. The interface supports reading from integer, float, a

### EthernetIP SLC500 Read VI

**Owning Palette:** [Messaging](messaging.html)**Installed With:** LabVIEW

Allows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as the SLC 500 and MicroLogix series from Rockwell Automation. The interface supports reading from integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format of the raw data.

Use the pull-down menu to select an instance of this VI.

| Select an instance EthernetIP SLC500 Read Integer EthernetIP SLC500 Read Float EthernetIP SLC500 Read Bit EthernetIP SLC500 Read Raw |
| --- |

EthernetIP SLC500 Read Integer

Allows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell’s SLC500 and MicroLogix series. The interface supports reading from integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format of the raw data.

Figure 15.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Read_Integer.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Number of Elements controls the number of elements read, starting at the offset specified in the element number. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to reading. Writing is implicitly controlled by the size of the passed data array. |
|  | Data returns data from a tag as an array of 16-bit signed integers. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP SLC500 Read Float

Allows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell’s SLC500 and MicroLogix series. The interface supports reading from integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format of the raw data.

Figure 16.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Read_Float.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Number of Elements controls the number of elements read, starting at the offset specified in the element number. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to reading. Writing is implicitly controlled by the size of the passed data array. |
|  | Data returns data from a tag as an array of single-precision floating-point integers. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP SLC500 Read Bit

Allows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell's SLC500 and MicroLogix series. The interface supports reading from integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format of the raw data.

Figure 17.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Read_Bit.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Number of Bits controls the number of bits read, starting at the specified Bit Offset. |
|  | error in describes the error status before this VI or function runs. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Bit Offset specifies the starting offset of the bits to read. |
|  | Session out represents the current session used for the operation. |
|  | Data returns data from a register as an array of Boolean values. |
|  | error out contains error information. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP SLC500 Read Raw

Allows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell's SLC500 and MicroLogix series. The interface supports reading from integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format of the raw data.

Figure 18.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Read_Raw.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Number of Bytes controls the number of bytes read. |
|  | error in describes the error status before this VI or function runs. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | File Type specifies the type of the data to write. If the File Type does not match the data type of the register, the PLC returns an error. |
|  | Subelement Number specifies the individual subelement to access when an element consists of multiple subelements. |
|  | Session out represents the current session used for the operation. |
|  | Data returns raw data from a register as an array of 8-bit unsigned integers. |
|  | error out contains error information. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Messaging

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-slc500-write-vi.html language=enus -->
## TOPIC 00015: EthernetIP SLC500 Write VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-slc500-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-slc500-write-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: MessagingInstalled With: LabVIEWAllows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as the SLC 500 and MicroLogix series from Rockwell Automation. The interface supports writing to integer, float, and

### EthernetIP SLC500 Write VI

**Owning Palette:** [Messaging](messaging.html)**Installed With:** LabVIEW

Allows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as the SLC 500 and MicroLogix series from Rockwell Automation. The interface supports writing to integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format of the raw data.

Use the pull-down menu to select an instance of this VI.

| Select an instance EthernetIP SLC500 Write Integer EthernetIP SLC500 Write Float EthernetIP SLC500 Write Bit EthernetIP SLC500 Write Raw |
| --- |

EthernetIP SLC500 Write Integer

Allows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell’s SLC500 and MicroLogix series. The interface supports writing to integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format of the raw data.

Figure 19.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Write_Integer.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Data accepts an array of 16-bit signed integer type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP SLC500 Write Float

Allows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell’s SLC500 and MicroLogix series. The interface supports writing to integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format of the raw data.

Figure 20.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Write_Float.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Data accepts an array of single-precision floating-point type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP SLC500 Write Bit

Allows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell's SLC500 and MicroLogix series. The interface supports writing to integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format of the raw data.

Figure 21.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Write_Bit.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Data accepts an array of Boolean value type data.. |
|  | error in describes the error status before this VI or function runs. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Bit Offset specifies the starting offset of the bits to write. The VI returns an error if the combined length of the Mask and the Bit Offset exceeds 16 bits. |
|  | Mask (optional) accepts an array of Boolean values as a bitmask for the provided Data. The VI returns an error if the combined length of the Mask and the Bit Offset exceeds 16 bits. |
|  | Session out represents the current session used for the operation. |
|  | error out contains error information. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP SLC500 Write Raw

Allows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as Rockwell's SLC500 and MicroLogix series. The interface supports writing to integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format of the raw data.

Figure 22.

[IMAGE alt='image' src='images/EthernetIP_SLC500_Write_Raw.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | File Number specifies the number of the register file to access. The default value is the default value for the specified register file type. For example, if float is specified as the register type, the default value is 8 because the default float register file is F8. |
|  | Session in represents the current session used for the operation. |
|  | Network Path is typically the IP address of the remote PLC target. |
|  | Element Number specifies the individual element to access within the register file. For example, to access the element N7:5, the element number value is 5. |
|  | Data accepts an array of 8-bit unsigned integer type data to write as raw data. |
|  | error in describes the error status before this VI or function runs. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | File Type specifies the type of the data to write. If the File Type does not match the data type of the register, the PLC returns an error. |
|  | Subelement Number specifies the individual subelement to access when an element consists of multiple subelements. |
|  | Mask accepts an unsigned 16-bit value. |
|  | Session out represents the current session used for the operation. |
|  | error out contains error information. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Messaging

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-tag-read-vi.html language=enus -->
## TOPIC 00016: EthernetIP Tag Read VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-tag-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-tag-read-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: MessagingInstalled With: LabVIEWAllows you to read from a target that supports Messaging class communications using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series. The interface supports multiple native PLC data types. Supported numeric types in

### EthernetIP Tag Read VI

**Owning Palette:** [Messaging](messaging.html)**Installed With:** LabVIEW

Allows you to read from a target that supports Messaging class communications using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series. The interface supports multiple native PLC data types. Supported numeric types include SINT (U8), INT (U16), DINT (U32), and REAL (SGL). Supported non-numeric types include string and Boolean values. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format used for tag communications.

Use the pull-down menu to select an instance of this VI.

| Select an instance EthernetIP Tag Read SINT EthernetIP Tag Read INT EthernetIP Tag Read DINT EthernetIP Tag Read REAL EthernetIP Tag Read BOOL EthernetIP Tag Read STRING EthernetIP Tag Read Raw |
| --- |

EthernetIP Tag Read SINT

Figure 1.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_SINT.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Number of Elements controls the number of elements read from a tag, starting at the offset specified in the tag name. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to tag reading. Tag writing is implicitly controlled by the size of the passed data array. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag as an array of 8-bit signed integers. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Read INT

Figure 2.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_INT.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Number of Elements controls the number of elements read from a tag, starting at the offset specified in the tag name. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to tag reading. Tag writing is implicitly controlled by the size of the passed data array. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag as an array of 16-bit signed integers. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Read DINT

Figure 3.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_DINT.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Number of Elements controls the number of elements read from a tag, starting at the offset specified in the tag name. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to tag reading. Tag writing is implicitly controlled by the size of the passed data array. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag as an array of 32-bit signed integers. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Read REAL

Figure 4.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_REAL.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Number of Elements controls the number of elements read from a tag, starting at the offset specified in the tag name. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to tag reading. Tag writing is implicitly controlled by the size of the passed data array. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag as an array of single-precision floating-point integers. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Read BOOL

Figure 5.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_BOOL.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Number of Elements controls the number of elements read from a tag, starting at the offset specified in the tag name. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to tag reading. Tag writing is implicitly controlled by the size of the passed data array. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag as an array of Boolean values. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Read STRING

Figure 6.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_STRING.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag in the form of a string. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Read Raw

Figure 7.

[IMAGE alt='image' src='images/EthernetIP_Tag_Read_Raw.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Number of Elements controls the number of elements read from a tag, starting at the offset specified in the tag name. Set Number of Elements to greater than one to read more than one element from an array. Number of Elements applies only to tag reading. Tag writing is implicitly controlled by the size of the passed data array. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | Data returns data from a tag as an array of 8-bit signed integers. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Messaging

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ethernetip-tag-write-vi.html language=enus -->
## TOPIC 00017: EthernetIP Tag Write VI

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ethernetip-tag-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ethernetip-tag-write-vi.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: MessagingInstalled With: LabVIEWAllows you to write to a target that supports Messaging class communications using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series. The interface supports multiple native PLC data types. Supported numeric types inc

### EthernetIP Tag Write VI

**Owning Palette:** [Messaging](messaging.html)**Installed With:** LabVIEW

Allows you to write to a target that supports Messaging class communications using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series. The interface supports multiple native PLC data types. Supported numeric types include SINT (U8), INT (U16), DINT (U32), and REAL (SGL). Supported non-numeric types include string and Boolean values. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format used for tag communications.

Use the pull-down menu to select an instance of this VI.

| Select an instance EthernetIP Tag Write SINT EthernetIP Tag Write INT EthernetIP Tag Write DINT EthernetIP Tag Write REAL EthernetIP Tag Write BOOL EthernetIP Tag Write STRING EthernetIP Tag Write Raw |
| --- |

EthernetIP Tag Write SINT

Figure 8.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_SINT.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts an array of 8-bit signed integer type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Write INT

Figure 9.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_INT.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts an array of 16-bit signed integer type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Write DINT

Figure 10.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_DINT.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts an array of 32-bit signed integer type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Write REAL

Figure 11.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_REAL.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts an array of single-precision floating-point type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Write BOOL

Figure 12.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_BOOL.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts an array of Boolean value type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Write STRING

Figure 13.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_STRING.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts string type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

EthernetIP Tag Write Raw

Figure 14.

[IMAGE alt='image' src='images/EthernetIP_Tag_Write_Raw.gif']

|  | Timeout (ms) is the operation timeout limit in milliseconds. |
| --- | --- |
|  | Session in represents the current session used for the operation. |
|  | Network Path is the routing path for the request to the target. The syntax for a simple system is <PLC address>,<backplane port number>,<Logix slot number>. For example, 10.0.0.1,1,0 is the routing path for a ControlLogix 5561 with IP address 10.0.0.1 and with the processor in slot 0 of an AB-1756 4-slot backplane. |
|  | Tag Name is the textual name of the tag to read or write. To access a sub-element of a tag, use a period followed by the name of the sub-element. To address an offset into an array, use bracket notation ([index]). For example, MyObjectTag.InputDataItem.Control[3] addresses the fourth element in the Control array within the sub-element InputDataItem. |
|  | Data accepts an array of 8-bit signed integer type data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session out represents the current session used for the operation. The default session name is default. It is possible to perform multiple concurrent reads and writes within the same session. Multiple sessions within a single application are only necessary to programmatically cancel some outstanding requests (by closing the session) while leaving another session running. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Messaging

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=i-o-data.html language=enus -->
## TOPIC 00018: I/O Data

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `i-o-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/i-o-data.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Ethernet/IP Industrial CommunicationInstalled With: LabVIEWThe VIs on this palette allow the LabVIEW system to create an I/O assembly and function as an adapter for a remote PLC. This type of communication is referred to as Class 1 or I/O server communication. Class 1 communication a

### I/O Data

**Owning Palette:** [Ethernet/IP Industrial Communication](ethernet-ip-industrial-communication.html)**Installed With:** LabVIEW

The VIs on this palette allow the LabVIEW system to create an I/O assembly and function as an adapter for a remote PLC. This type of communication is referred to as Class 1 or I/O server communication. Class 1 communication allows the PLC to establish an implicit I/O data connection with the LabVIEW system and repeatedly exchange assembly data at a specific rate.

Assemblies are treated as shared memory that is used to produce or consume data. A producing assembly provides input to the PLC. A consuming assembly accepts output from the PLC. The PLC uses an instance ID to map each assembly. Because the PLC uses the instance ID to connect to the assembly, the instance ID must match the configuration of the PLC. Refer to [Configuring the PLC](configuring-the-plc.html) for more information about configuring the PLC.

| Palette Object | Description |
| --- | --- |
| EthernetIP Add Assembly Instance | Allows the LabVIEW system to create an I/O assembly and function as an adapter for a remote PLC. |
| EthernetIP Remove Assembly Instance | Allows the LabVIEW system to destroy an I/O assembly. |
| EthernetIP Get Assembly Instance Data | Reads the data in an assembly as one large block of data. The access to the data is atomic, which means that all the data must be read at once. |
| EthernetIP Set Assembly Instance Data | Writes the data to an assembly as one large block of data. The access to the data is atomic, which means that all the data must be read at once. |

Parent topic:

Ethernet/IP Industrial Communication

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=messaging.html language=enus -->
## TOPIC 00019: Messaging

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `messaging.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/messaging.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Ethernet/IP Industrial CommunicationInstalled With: LabVIEWThe VIs on this palette use explicit messaging connections to read from or write to a target. Palette Object Description EthernetIP Tag Read Allows you to read from a target that supports Messaging class communications using

### Messaging

**Owning Palette:** [Ethernet/IP Industrial Communication](ethernet-ip-industrial-communication.html)**Installed With:** LabVIEW

The VIs on this palette use explicit messaging connections to read from or write to a target.

| Palette Object | Description |
| --- | --- |
| EthernetIP Tag Read | Allows you to read from a target that supports Messaging class communications using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series. The interface supports multiple native PLC data types. Supported numeric types include SINT (U8), INT (U16), DINT (U32), and REAL (SGL). Supported non-numeric types include string and Boolean values. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format used for tag communications. |
| EthernetIP Tag Write | Allows you to write to a target that supports Messaging class communications using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series. The interface supports multiple native PLC data types. Supported numeric types include SINT (U8), INT (U16), DINT (U32), and REAL (SGL). Supported non-numeric types include string and Boolean values. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format used for tag communications. |
| EthernetIP SLC500 Read | Allows you to read from a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as the SLC 500 and MicroLogix series from Rockwell Automation. The interface supports reading from integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Reading raw data requires familiarity with the data format of the raw data. |
| EthernetIP SLC500 Write | Allows you to write to a target that supports Messaging class communications using PCCC communication. Valid targets include PLCs such as the SLC 500 and MicroLogix series from Rockwell Automation. The interface supports writing to integer, float, and bit register files hosted on the PLC. The API also supports raw data to accommodate unsupported or custom data types. Writing raw data requires familiarity with the data format of the raw data. |
| EthernetIP CIP Get Attribute Single | Allows you to read attribute information from a CIP object. |
| EthernetIP CIP Set Attribute Single | Allows you to write attribute information to a CIP object. |

Parent topic:

Ethernet/IP Industrial Communication

<!--NI_TOPIC bundle=ni-industrial-communications-ethernetip-api-ref path=ni-industrial-communications-for-ethernet-ip.html language=enus -->
## TOPIC 00020: NI-Industrial Communications for EtherNet/IP Help

- bundle_id: `ni-industrial-communications-ethernetip-api-ref`
- source_path: `ni-industrial-communications-for-ethernet-ip.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethernetip-api-ref/raw/resource/enus/ni-industrial-communications-for-ethernet-ip.html
- document_id: `ni-industrial-communications-ethernetip-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-Industrial Communications for EtherNet/IP API allows a LabVIEW system to communicate with devices on an EtherNet/IP network. The API supports Explicit Messaging and I/O Data communications.

### NI-Industrial Communications for EtherNet/IP Help

The NI-Industrial Communications for EtherNet/IP API allows a LabVIEW system to communicate with devices on an EtherNet/IP network. The API supports Explicit Messaging and I/O Data communications.
