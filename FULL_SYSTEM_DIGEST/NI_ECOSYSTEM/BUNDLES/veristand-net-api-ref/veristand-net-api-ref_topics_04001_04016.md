# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=4001 end=4016 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-waveform-units.html language=enus -->
## TOPIC 04001: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-waveform-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-waveform-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units associated with the waveform. This can be any arbitrary string. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Units { get; set; }ReturnsThe units.

### Units

Gets or sets the units associated with the waveform. This can be any arbitrary string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Units { get; set; }

#### Returns

The units.

Parent topic:

Waveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-waveform.html language=enus -->
## TOPIC 04002: Waveform Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-waveform.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-waveform.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a waveform in the system definition. This is a base class for more specific waveform classes, including hardware waveforms, custom device waveforms, and so on. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Waveform : BaseNodeRemarksUse

### Waveform Class

Represents a waveform in the system definition. This is a base class for more specific waveform classes, including hardware waveforms, custom device waveforms, and so on.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Waveform : BaseNode

#### Remarks

Use the members of this class to get and set basic properties of a waveform, including its data type and associated units.

**Accessing this Class**

You cannot explicitly construct a Waveform object. Use an object of a type that inherits this class to access its members.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| DataType | Gets or sets the data type associated with the waveform. |
| Units | Gets or sets the units associated with the waveform. This can be any arbitrary string. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-windowconditiontype.html language=enus -->
## TOPIC 04003: WindowConditionType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-windowconditiontype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-windowconditiontype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the signal condition that causes a window trigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum WindowConditionTypeMembersNameValueDescriptionEnteringWindow10163The signal is entering the window. LeavingWindow10208The signal is leaving the window.

### WindowConditionType Enumeration

Defines the signal condition that causes a window trigger.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum WindowConditionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| EnteringWindow | 10163 | The signal is entering the window. |
| LeavingWindow | 10208 | The signal is leaving the window. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet-decimation.html language=enus -->
## TOPIC 04004: Decimation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet-decimation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet-decimation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for inline incoming and outgoing frames of an XNET device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between

### Decimation

Gets or sets the processing rate for inline incoming and outgoing frames of an [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Decimation { get; set; }

#### Remarks

Use the members of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html), [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html), or [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html) class to configure inlining of frames under an NI-XNET port.

#### Returns

The default value is 100 Hz.

Parent topic:

XNET Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet-disablexnet.html language=enus -->
## TOPIC 04005: DisableXNET()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet-disablexnet.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet-disablexnet.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the XNET section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void DisableXNET()

### DisableXNET()

Disables the XNET section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void DisableXNET()

Parent topic:

XNET Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet-enablexnet.html language=enus -->
## TOPIC 04006: EnableXNET()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet-enablexnet.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet-enablexnet.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the XNET section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void EnableXNET()

### EnableXNET()

Enables the XNET section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void EnableXNET()

Parent topic:

XNET Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet-getcan.html language=enus -->
## TOPIC 04007: GetCAN()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet-getcan.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet-getcan.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CAN section, from which you can add and access CAN ports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CAN GetCAN()RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW Walkthrough: Modifying a System D

### GetCAN()

Gets the [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) section, from which you can add and access CAN ports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) GetCAN()

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

A [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) object.

Parent topic:

XNET Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet-getflexray.html language=enus -->
## TOPIC 04008: GetFlexRay()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet-getflexray.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet-getflexray.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FlexRay section, from which you can add and access FlexRay ports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FlexRay GetFlexRay()ReturnsA FlexRay object.

### GetFlexRay()

Gets the [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) section, from which you can add and access FlexRay ports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) GetFlexRay()

#### Returns

A [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) object.

Parent topic:

XNET Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet-getlin.html language=enus -->
## TOPIC 04009: GetLIN()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet-getlin.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet-getlin.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the LIN class, from which you can add and access LIN ports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LIN GetLIN()ReturnsA LIN object.

### GetLIN()

Gets the [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html) class, from which you can add and access LIN ports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html) GetLIN()

#### Returns

A [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html) object.

Parent topic:

XNET Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnet.html language=enus -->
## TOPIC 04010: XNET Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnet.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnet.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the NI-XNET section of a Chassis, which contains any CAN, LIN, or FlexRay devices you configure. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class XNET : SectionRemarksUse the members of this class to enable or disable the XNET section and t

### XNET Class

Represents the **NI-XNET** section of a [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html), which contains any [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html), [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html), or [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) devices you configure.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class XNET : Section

#### Remarks

Note

You must install NI-XNET driver software to interact with NI-XNET devices in NI VeriStand.

**Accessing this Class**

- [GetXNET](nationalinstruments-veristand-systemdefinitionapi-chassis-getxnet.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Decimation | Gets or sets the processing rate for inline incoming and outgoing frames of an XNET device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device. |

#### Methods

| Name | Description |
| --- | --- |
| DisableXNET() | Disables the XNET section. |
| EnableXNET() | Enables the XNET section. |
| GetCAN() | Gets the CAN section, from which you can add and access CAN ports. |
| GetFlexRay() | Gets the FlexRay section, from which you can add and access FlexRay ports. |
| GetLIN() | Gets the LIN class, from which you can add and access LIN ports. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-adddatabase__database-out.html language=enus -->
## TOPIC 04011: AddDatabase(Database, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-adddatabase__database-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-adddatabase__database-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Database to the XNETDatabases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDatabase(Database database, out Error error)ParametersNameTypeDescriptiondatabaseDatabaseThe database to add.errorout ErrorReturns an NationalInstruments.VeriSta

### AddDatabase(Database, out Error)

Adds the specified [Database](nationalinstruments-veristand-systemdefinitionapi-database.html) to the [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDatabase(Database database, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| database | Database | The database to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the database was added successfully.

Parent topic:

XNETDatabases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-adddatabase__database.html language=enus -->
## TOPIC 04012: AddDatabase(Database)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-adddatabase__database.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-adddatabase__database.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Database to the XNETDatabases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDatabase(Database database)ParametersNameTypeDescriptiondatabaseDatabaseThe database to add.Returnstrue if the database was added successfully.

### AddDatabase(Database)

Adds the specified [Database](nationalinstruments-veristand-systemdefinitionapi-database.html) to the [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDatabase(Database database)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| database | Database | The database to add. |

#### Returns

true if the database was added successfully.

Parent topic:

XNETDatabases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-getdatabaselist.html language=enus -->
## TOPIC 04013: GetDatabaseList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-getdatabaselist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-getdatabaselist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Database elements of the current XNETDatabases section. This method gets the NI-XNET databases that have been added to the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Database[] GetDatabaseList()RemarksModifications you

### GetDatabaseList()

Gets an array that contains the [Database](nationalinstruments-veristand-systemdefinitionapi-database.html) elements of the current [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) section. This method gets the NI-XNET databases that have been added to the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Database](nationalinstruments-veristand-systemdefinitionapi-database.html)[] GetDatabaseList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Database](nationalinstruments-veristand-systemdefinitionapi-database.html) elements of the current [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) section.

Parent topic:

XNETDatabases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html language=enus -->
## TOPIC 04014: XNETDatabases Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the XNET Databases section of a Target, which contains any XNET Databases you add to the system definition to run XNET devices. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class XNETDatabases : SectionRemarksUse the members of this class to

### XNETDatabases Class

Represents the **XNET Databases** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains any XNET Databases you add to the system definition to run [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) devices.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class XNETDatabases : Section

#### Remarks

Note

You must install NI-XNET driver software to interact with NI-XNET devices in NI VeriStand.

**Accessing this Class**

- [GetXNETDatabases](nationalinstruments-veristand-systemdefinitionapi-target-getxnetdatabases.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDatabase(Database, out Error) | Adds the specified Database to the XNETDatabases section. |
| AddDatabase(Database) | Adds the specified Database to the XNETDatabases section. |
| GetDatabaseList() | Gets an array that contains the Database elements of the current XNETDatabases section. This method gets the NI-XNET databases that have been added to the system definition. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-xnettermination.html language=enus -->
## TOPIC 04015: XNETTermination Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-xnettermination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-xnettermination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures onboard termination for the XNET port. Termination behavior differs depending on the type of device you are using (CAN, FlexRay, or LIN). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum XNETTerminationRemarksValueDescriptionOffCANHigh-Speed CAN: Termination i

### XNETTermination Enumeration

Configures onboard termination for the XNET port. Termination behavior differs depending on the type of device you are using (CAN, FlexRay, or LIN).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum XNETTermination

#### Remarks

| Value | Description |
| --- | --- |
| Off | CANHigh-Speed CAN: Termination is disabled.Low-Speed CAN: Termination is set to 1.11 k ΩSingle-Wire Transceivers: ISO standard requires a 9.09 k Ω resistor. No additional configuration is supported.FlexRayThe interface is not terminated. This setting applies to both FlexRay communication channels (A and B).LINTermination is disabled. |
| On | CANHigh-Speed CAN: Termination is enabled (120 Ω )Low-Speed CAN: Termination is set to 4.99 k Ω . Single-Wire Transceivers: ISO standard requires a 9.09 k Ω resistor. No additional configuration is supported.FlexRayThe interface is terminated. This setting applies to both FlexRay communication channels (A and B).LINTermination is enabled. Per the LIN 2.1 standard, the master ECU has a ~1 k Ω termination resistor between Vbat and Vbus. Therefore, set termination to On only if you are using your interface as the master and do not already have external termination. |

Note

- High-Speed CAN — High-Speed CAN networks are typically terminated on the bus itself, instead of within an individual CAN node. However, NI-XNET allows you to configure termination within the node to simplify testing. If your bus already has the correct amount of termination, set [Termination](nationalinstruments-veristand-systemdefinitionapi-canport-termination.html) to Off.
- Low-Speed CAN — Every node on a Low-Speed CAN network requires termination for each CAN data line. This configuration allows the Low-Speed/Fault-Tolerant CAN port to provide fault detection and recovery. In general, if the existing network has an overall network termination of 125 Ω or less, set [Termination](nationalinstruments-veristand-systemdefinitionapi-canport-termination.html) to On to enable the 4.99 k Ω option. Otherwise, select Off for the 1.11 k Ω option.
- Single-Wire Transceivers — The ISO standard requires Single-Wire transceivers to have a 9.09 k Ω resistor. No additional configuration is supported.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | Termination is off. Termination behavior depends on the device type you are using. |
| On | 1 | Termination is on. Termination behavior depends on the device type you are using. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi.html language=enus -->
## TOPIC 04016: NationalInstruments.VeriStand.SystemDefinitionAPI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionAccelerationRepresents a calculated channel with the acceleration function. AlarmRepresents an alarm, which notifies the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a specified procedure. Ala

### NationalInstruments.VeriStand.SystemDefinitionAPI

#### Classes

| Name | Description |
| --- | --- |
| Acceleration | Represents a calculated channel with the acceleration function. |
| Alarm | Represents an alarm, which notifies the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a specified procedure. |
| AlarmFolder | Represents an alarm folder, which organizes alarms under the Alarms section. |
| AlarmStatus | A channel that indicates the current status of an alarm. |
| Alarming | Represents an Alarm Command, or Alarming, step that you can add to a Procedure. This step performs the specified Function on the specified Alarm when the step executes. |
| Alarms | Represents the Alarms section of a Target, which contains any configured Alarm and AlarmFolder objects. |
| Alias | Represents an alias, which defines an alternate name for a channel in a system definition file. You can use the alias name, rather than the full channel path, in the Workspace window and Stimulus Profile Editor. |
| AliasFolder | Represents a folder under the Aliases section of the system definition. Folders simply organize aliases into logical groups. |
| Aliases | Represents the Aliases section of the system definition, which contains Alias objects that define names you can use in place of full channel paths. |
| AutomaticFrameProcessing | Represents an Automatic Frame Processing section under an outgoing frame of an NI-XNET CAN port. The Automatic Frame Processing section contains CRC and Counter channels. |
| Average | Represents a calculated channel with the average function. The average function calculates the average value of the channel you specify every n points. |
| BaseNode | Represents generic nodes in the system definition and provides access to options and configuration settings that all nodes support. |
| CAN | Represents the CAN section under XNET in the system definition. |
| CANInterfaceChannels | Represents the Interface section under an NI-XNET CAN port. This section contains the port-specific channel that controls the port's sleep mode and channels which provide status information. |
| CANPort | Represents a port under the NI-XNET CAN section. |
| CRC | Represents the CRC section under the AutomaticFrameProcessing section of an outgoing frame of an NI-XNET CAN port. This feature performs a cyclic redundancy check. |
| CalculatedChannel | Represents a calculated channel, which produces new values based on calculations performed on other channels in the system definition. |
| CalculatedChannelFolder | Represents a folder under the CalculatedChannels section of the system definition. Folders simply organize CalculatedChannels into logical groups. |
| CalculatedChannels | Represents the Calculated Channels section of a Target. This section contains CalculatedChannel objects that perform calculations on other channels in the system. |
| CallProcedure | Represents a Call Procedure step that you can add to a Procedure. The Call Procedure step calls a procedure when the step executes. |
| Channel | Represents a channel in the system definition. This is a base class for more specific channel classes, including hardware channels, system channels, user channels, calculated channels, and so on. |
| Chassis | Represents a chassis, which contains any NI-DAQ devices, reflective memory devices, NI FPGA targets, NI-XNET devices, and timing and sync devices you add. |
| Command | Represents a parent class for the different Procedure command types. |
| Condition | Represents a Condition step that you can add to a procedure. The Condition step executes a GotoLabel step based on the comparison of a constant value or channel value. |
| Conditional | Represents a CalculatedChannel with the conditional function. The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value. |
| Counter | Represents the Counter section under the AutomaticFrameProcessing section of an outgoing frame of an NI-XNET CANPort. This feature increments specific bits every time the frame is transmitted across the bus. |
| CustomDevice | Represents a custom device in NI VeriStand. |
| CustomDeviceBase | Defines a base class for NI VeriStand custom devices. |
| CustomDeviceChannel | Represents a channel in a custom device. |
| CustomDeviceSection | Represents a section under a custom device. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. |
| CustomDeviceWaveform | Represents a waveform in a custom device. |
| CustomDevices | Represents the top-level Custom Devices section of a Target. This section contains all the custom devices (except timing and sync devices) that you add to the system definition. |
| Cyclic | Represents the Cyclic section that contains outgoing cyclic frames under an NI-XNET CAN or FlexRay port. Use cyclic frames when you want data changes to arrive at other ECUs within a well-defined deadline. |
| CyclicEvent | Represents the CyclicEvent section that contains outgoing cyclic/event frames under an NI-XNET CAN port. Use cyclic/event frames when you want data changes to arrive at other ECUs within a well-defined deadline with the additional ability to send frames on demand. |
| DAQ | Represents the DAQ section of a Chassis in the system definition. This section contains all the DAQ devices you add under the chassis. |
| DAQAnalogInput | Represents a DAQ analog input channel. |
| DAQAnalogInputs | Represents an Analog Input section under a DAQDevice, which contains all DAQAnalogInput channels you add for the device. |
| DAQAnalogOutput | Represents a DAQ analog output channel. |
| DAQAnalogOutputs | Represents an Analog Output section under a DAQDevice, which contains all DAQAnalogOutput channels you add for the device. |
| DAQChannel | Provides an abstract base class for implementing DAQ device channels and their measurement types based on DAQ plug-in XML files. |
| DAQCountUpDown | Represents a DAQCounter channel with the count up/down task type. |
| DAQCounter | Represents a DAQ counter channel. |
| DAQCounterInput | Initializes a new instance of the DAQCounterInput class. |
| DAQCounterOutput | Initializes a new instance of the DAQCounterOutput class. |
| DAQCounters | Represents a Counter section under a DAQDevice, which contains all DAQCounter channels you add for the device. |
| DAQDIOPort | Represents a DAQ DIO port, which contains DAQDigitalInput and/or DAQDigitalOutput channels. |
| DAQDevice | Represents a DAQ device. |
| DAQDigitalInput | Represents a DAQ digital input channel. |
| DAQDigitalInputs | Represents a Digital Input section under a DAQDevice, which contains the DAQDIOPort ports for DAQDigitalInput channels. |
| DAQDigitalOutput | Represents a DAQ digital output channel. |
| DAQDigitalOutputs | Represents a Digital Output section under a DAQDevice, which contains the DAQDIOPort ports for DAQDigitalOutput channels. |
| DAQFrequencyMeasurement | Represents a DAQCounter channel with the frequency measurement task type. |
| DAQInternalChannel | Represents a DAQ internal channel. |
| DAQInternalChannels | Represents an Internal Channels section under a DAQDevice, which contains any DAQInternalChannel objects to add to the device. |
| DAQLogging | Represents the Logging section of a DAQTaskAI. |
| DAQPeriodMeasurement | Represents a DAQCounter channel with the period measurement task type. |
| DAQPositionMeasurement | Represents a DAQCounter channel with the position measurement task type. |
| DAQPulseGeneration | Represents a DAQ Counter measurement section of input channels. |
| DAQPulseMeasurement | Represents a DAQ Counter measurement section of input channels. |
| DAQSectionType | Represents a generic DAQ data section. |
| DAQTask | Provides an abstract base class for different types of tasks you can assign to DAQ channels. |
| DAQTaskAI | Represents a DAQmx task you can assign to one or more DAQ analog input channels to configure timing properties, triggers, and logging. |
| DAQTaskCommand | Represents one of the channels under the DAQTaskAI, DAQTriggers, or DAQLogging sections. Task command channels control the execution of the DAQTaskAI. |
| DAQTasks | Represents the Waveform Tasks section in a system definition. This section contains DAQTask objects. |
| DAQTrigger | Provides an abstract base class for different types of triggers you can use to configure a DAQTaskAI to start acquiring under certain conditions. |
| DAQTriggerAnalogEdge | Represents an analog edge trigger that can configure a DAQTaskAI to start acquiring under certain conditions. |
| DAQTriggerAnalogWindow | Represents an analog window trigger that can configure a DAQTaskAI to start acquiring under certain conditions. |
| DAQTriggerDigitalEdge | Represents a digital edge trigger that can configure a DAQTaskAI to start acquiring under certain conditions. |
| DAQTriggerNone | Represents a disabled DAQTrigger. |
| DAQTriggerSoftware | Represents a software trigger that can configure a DAQTaskAI to start acquiring under certain conditions. |
| DAQTriggers | Represents the Triggers section of a DAQTaskAI. |
| DAQWaveform | Represents a generic DAQ waveform. |
| DAQWaveformAnalogInput | Represents a DAQ analog input waveform used in a buffered acquisition. |
| DataFileError | Represents the Error channel associated with a raw frame data logging file or data replay file under an NI-XNET port. |
| DataFileReplay | Represents a data replay file, which is a raw frame data logging (TDMS or NCL) file that you replay onto a CAN bus. |
| DataFileStatus | Represents the Status channel associated with a raw frame data logging file or data replay file under an NI-XNET port. |
| DataLoggingFile | Represents a raw frame data logging (TDMS or NCL) file under an NI-XNET port. You can use raw frame data logging files to record incoming frame data during an NI-XNET session. |
| DataReplay | Represents the Data Replay section under an NI-XNET CAN port, which contains any DataFileReplay files you want to replay onto the CAN bus. |
| DataSharing | Represents the Data Sharing section under a Chassis. This section contains any reflective memory devices you add to the system definition. |
| DataSharingNetwork | Represents the Data Sharing Network section of the system definition, under which you can add and configure a reflective memory network. You can only configure one reflective memory network per system definition. |
| Database | Represents an XNET database. XNET databases can be CANdb (.dbc), NI-CAN (.ncd), LDF (.ldf), or FIBEX (.xml) files. |
| DependentFile | Represents a dependent file, which can be any file that another node requires. For example, model files, bitfiles, and VIs that make up custom devices can all be dependent files. |
| DependentNode | Represents a dependent node that encapsulates the path to another node in the system definition. |
| Dictionary | Represents a dictionary, which is an associative array. You can set dictionaries as values for CustomDevice and TimingAndSyncDevice items. |
| DictionaryElement | Represents an element, or a key/value pair, in a Dictionary. |
| Dwell | Represents a Dwell step that you add to a procedure. The Dwell step suspends the procedure by the amount of time you specify. |
| DynamicSignal | Represents a dynamic signal contained in a multiplexed frame. NI VeriStand organizes dynamic signals under Mode nodes. |
| ECUNetworkCluster | Represents an ECU network cluster as a specialized type of Model. Use the ECU network cluster to configure the communication between VirtualECU and an XNET device. |
| End | Represents an End step that you can add to a procedure. The End step stops the procedure. |
| EventTriggered | Represents the Event Triggered section under an Outgoing section of an NI-XNET CAN or FlexRay port. |
| Execution | Represents the Execution section under a Model. This section contains channels that get and set execution details of the model, such as its current status and the amount of time that has elapsed since it began executing. |
| ExecutionOrder | Represents the Execution Order section under SimulationModels, which contains information about the order that your models execute relative to each other in the VeriStand Engine. |
| ExitSubroutine | Represents an Exit Subroutine step that you can add to a procedure. The Exit Subroutine step is typically used in procedures that are called from other procedures by a CallProcedure step. The Exit Subroutine step stops the current procedure and returns to the calling procedure. |
| FPGA | Represents the FPGA section of a Chassis in the system definition. This section contains all the FPGA devices you add under the chassis. |
| FPGAAICategory | Represents the Input » Analog section under an FPGADevice. |
| FPGAAOCategory | Represents the Output » Analog section under an FPGADevice. |
| FPGAAnalogInput | Represents an FPGA analog input channel. |
| FPGAAnalogOutput | Represents an FPGA analog output channel. |
| FPGACategory | Represents a section under an FPGA device. Sections organize channels according to type. For example, Input » Analog, Output » Digital, and so on. |
| FPGAChannel | Represents a channel of an FPGA device. |
| FPGADICategory | Represents the Input » Digital section under an FPGADevice. |
| FPGADOCategory | Represents the Output » Digital section under an FPGADevice. |
| FPGADevice | Represents an FPGA target under the FPGA section. |
| FPGADigitalInput | Represents an FPGA digital input channel. |
| FPGADigitalOutput | Represents an FPGA digital output channel. |
| FPGAPWMInCategory | Represents the Input » PWM section under an FPGADevice. |
| FPGAPWMInput | Represents an FPGA PWM input channel. |
| FPGAPWMOutCategory | Represents the Output » PWM section under an FPGADevice. |
| FPGAPWMOutput | Represents an FPGA PWM output channel. |
| FinishedFiles | Represents a Finished Files channel associated with an NI-XNET RawFrameDataLogging file. This channel stores the number of completed log files for the current session of the VeriStand Engine. You can use this channel to determine when a file is ready for use by other processes. |
| FlexRay | Represents the FlexRay section under XNET in the system definition. |
| FlexRayInterfaceChannels | Represents the Interface section under an NI-XNET FlexRay port. This section contains the port-specific channels which provide status information. |
| FlexRayPort | Represents a port under an NI-XNET FlexRay device. |
| Formula | Represents a calculated channel with the formula function. This function calculates the result of a formula you specify. |
| FrameFaulting | Represents a Frame Faulting section under an outgoing cyclic frame of an NI-XNET CAN port. This section contains channels you can use to configure the transmission of cyclic frames. |
| FrameID | Represents a Frame ID channel under the FrameInformation section of an incoming, raw data format NI-XNET frame. This channel contains the ID number that identifies the frame. |
| FrameInformation | Represents a Frame Information section under an incoming NI-XNET frame. This section contains channels that store information about the frame, such as the timestamp at which it was received and the ID number of the current frame. |
| Generator | Represents a stimulus generator in the Legacy Stimulus Profile Editor, which produces simulated real-world signals that stimulus profiles use to perform tests on a system. |
| GotoLabel | Represents a Goto Label step that you can add to a procedure. When this step executes, the procedure jumps to the step specified by M:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel.Label. |
| Hardware | Represents the Hardware section of a Target, which contains any chassis you add. |
| Incoming | Represent the Incoming section under an NI-XNET CAN, LIN, or FlexRay ports, which contains any incoming frames and data logging files . |
| Inport | Represents a model inport, or input. |
| InportGroup | Represents a sub-section of the Inports section of a model. Inport groups provide organization within the model. |
| Inports | Represents the top-level Inports section under a Model. This section contains all the Inport and InportGroup objects for the model. |
| InputOverflowChannel | Represents an input overflow count channel, which tracks the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A single custom device can have only one input overflow count channel. |
| LIN | Represents the LIN section under XNET in the system definition. |
| LINInterfaceChannels | Represents the Interface section under an NI-XNET LIN port. This section contains the port-specific channels which provide status information. |
| LINPort | Represents a port under an NI-XNET LIN device. |
| LINScheduler | Represents the LIN Scheduler channel under an NI-XNET LINPort. The LIN Scheduler specifies which schedule to use to determine when to transmit frames. This channel is only valid if the LINPort to which is belongs is configured as the master port (IsMaster is true). |
| LUTValue | Represents a pair of values in a LookupTable scale: a pre-scaled value and the corresponding scaled value. |
| LookupTable | Represents a lookup table Scale, which maps an array of pre-scaled values to an array of corresponding scaled values. |
| LowpassFilter | Represents a calculated channel with the Lowpass Filter function. This function applies a lowpass Butterworth filter to the value of the specified ChannelToFilter. |
| Maximum | Represents a calculated channel with the Maximum function. This function compares two values (x and y) and returns the larger value. |
| Minimum | Represents a calculated channel with the Minimum function. This function compares two values (x and y) and returns the smaller value. |
| Mode | Represents a Mode section under a signal format NI-XNET CAN frame. The Mode section organizes dynamic (multiplexed) signals according to their mode values. |
| ModeInformation | Represents a Mode Information section under an NI-XNET CAN multiplexer mode. This section contains channels that store information about the mode, such as the timestamp at which it was received. |
| ModeReceiveTime | Represents the Mode Receive Time channel for an incoming NI-XNET CAN multiplexer mode. This channel contains the most recent timestamp at which the mode was received. |
| ModeTimeDifference | Represents the Mode Time Difference channel for an incoming NI-XNET CAN multiplexer mode. This channel stores the difference between the two most recent ModeReceiveTime timestamps. |
| Model | Represents a model, which is a mathematical representation of a real-world system. A model responds to stimuli by producing outputs in a way that emulates the behavior of the modeled item. Models contain inputs and outputs that send and receive data. Models contain parameters you can manipulate and signals whose values you can view. For example, a model that generates a sine wave contains parameters that adjust the amplitude and frequency of the sine wave. You can view the value of the sine wave using the model signal. |
| ModelCommand | Represents a Model Command channel, which you can use to send commands to the model running on the target. |
| ModelDefaultGroup | Represents a parent class for the different types of sub-folders and sections a model can have. |
| ModelParameter | Represents a model parameter. |
| ModelParameterGroup | Represents a sub-section of the ModelParameters section of a model. Parameter groups provide organization within the model. |
| ModelParameters | Represents the top-level Parameters section under a Model. This section contains all the ModelParameter and ModelParameterGroup objects under the model. |
| ModelSignal | Represents a model signal. |
| ModelSignalGroup | Represents a sub-section of the ModelSignals section of a model. Signal groups provide organization within the model. |
| ModelSignals | Represents the top-level Signal section under a Model. This section contains all the ModelSignal and ModelSignalGroup objects under the model. |
| ModelStatus | Represents a Model Status channel, which you can use to get information about the current status of the model running on the target. |
| ModelTime | Represents a Model Time channel, which you can use to get information about the current running time, in seconds, of the model running on the target. |
| Models | Represents the Models section under SimulationModels. This section contains any compiled or uncompiled models you add to the system definition. NI VeriStand supports importing .dll, .mdl, and .lvmodel file types. |
| Multiplexer | Represents a multiplexer signal under an NI-XNET signal format CAN frame. The multiplexer signal defines an area within the frame to contain different DynamicSignal signals. |
| NodeIDUtil | Provides methods for converting node IDs, or pointers, to nodes in a system definition file into item references to the same node. |
| Outgoing | Represents the Outgoing section under an NI-XNET CAN, LIN, or FlexRay port, which contains any outgoing frames and data replay files. |
| Outport | Represents a model outport, or output. |
| OutportGroup | Represents a sub-section of the Outports section of a model. Outport groups provide organization within the model. |
| Outports | Represents the top-level Outports section under a Model. This section contains all the Outport and OutportGroup objects for the model. |
| OutputUnderflowChannel | Represents an output underflow count channel, which tracks the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A single custom device can have only one output underflow count channel. |
| PeakAndValley | Represents a calculated channel with the Peak & Valley function. This function calculates the peak, valley, and offset of a cyclical waveform on the channel you specify. The calculated channel stores the peak value, and the channels you specify when you configure the calculated channel store the valley and offset values. |
| PendingFrames | Represents a Pending Frames channel associate with an NI-XNET DataFileReplay file. This channel stores the number of frames in the outgoing transmission queue of the current NI-XNET streaming session. You can use this channel to determine whether data is replaying as expected. |
| PolynomialScale | Represents a polynomial Scale, which converts values using a polynomial equation with up to ten coefficients. |
| Procedure | Represents a procedure, which determines a set of actions that the VeriStand Engine executes. You can configure procedures to run in response to an alarm, when called from another procedure, or on startup. |
| Procedures | Represents the Procedures section of a Target, which contains all the Procedure objects you configure. |
| RawDataBasedChannel | Represents a raw data format channel under an NI-XNET RawDataBasedFrame. |
| RawDataBasedFrame | Represents a raw data format frame of an NI-XNET CAN, LIN, or FlexRay device. |
| RawFrameDataLogging | Represents the Raw Frame Data Logging section under an NI-XNET CAN, LIN, or FlexRay port. |
| RealTimeSequenceCommand | A procedure command for commanding real-time sequences. |
| ReceiveTime | Represents the Receive Time channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel contains the most recent timestamp at which the frame was received. |
| ReflectiveMemory | Represents a reflective memory device under the DataSharing section of the system definition. A reflective memory device is a target on a ReflectiveMemoryNetwork. |
| ReflectiveMemoryDataChannel | Represents a data channel under a ReflectiveMemory device. |
| ReflectiveMemoryDataChannels | Represents the top-level Data Channels section of a ReflectiveMemory device. This section contains all the data channels for the device, as well as sub-folders that you can use to organize the channels. |
| ReflectiveMemoryFolder | Represents a folder under a reflective memory device. Folders can contain data channels or additional sub-folders. |
| ReflectiveMemoryInformationChannels | Represents the Information Channels section under a reflective memory device. |
| ReflectiveMemoryNetwork | Represents the reflective memory network that ReflectiveMemory devices use to share data. A single system definition can have only one reflective memory network. |
| ReflectiveMemoryRingReadLateCount | Represents a Ring Read Late Count channel of a reflective memory device. This channel increments any time the device is not able to read a section of data from reflective memory because the section was still getting written to by another device. If this channel increments, the section of invalid data was not copied to the local channels. |
| ReflectiveMemoryWriteLateCount | Represents a Node Write Late Count channel of a reflective memory device. This channel increments any time the device is not able to write data to the reflective memory network because a new iteration of the Primary Control Loop started before the write operation was complete. In this situation, the PCL does not write or read any data for the iteration where the write operation failed to complete. |
| Root | Represents the root node of the system definition. |
| RuntimeConfigurableSection | Represents a section where child nodes (sections and channels) can be dynamically added while the system is deployed using IRuntimeConfigurationManager. |
| RuntimeConfiguration | Represents a runtime configuration file, which contains section property and channels that can be applied under RuntimeConfigurableSection without having to undeploy the system using APIs from NationalInstruments.VeriStand.ClientAPI.IRuntimeConfiguration. |
| SCXI1100 | Represents an SCXI-1100 module that you can add to an SCXIChassis. |
| SCXI1102 | Represents an SCXI-1102 module that you can add to an SCXIChassis. |
| SCXI1102B | Represents an SCXI-1102B module that you can add to an SCXIChassis. |
| SCXI1102C | Represents an SCXI-1102C module that you can add to an SCXIChassis. |
| SCXI1104 | Represents an SCXI-1104 module that you can add to an SCXIChassis. |
| SCXI1104C | Represents an SCXI-1104C module that you can add to an SCXIChassis. |
| SCXI1112 | Represents an SCXI-1112 module that you can add to an SCXIChassis. |
| SCXI1120 | Represents an SCXI-1120 module that you can add to an SCXIChassis. |
| SCXI1120D | Represents an SCXI-1120D module that you can add to an SCXIChassis. |
| SCXI1121 | Represents an SCXI-1121 module that you can add to an SCXIChassis. |
| SCXI1122 | Represents an SCXI-1122 module that you can add to an SCXIChassis. |
| SCXI1124 | Represents an SCXI-1124 module that you can add to an SCXIChassis. |
| SCXI1125 | Represents an SCXI-1125 module that you can add to an SCXIChassis. |
| SCXI1126 | Represents an SCXI-1126 module that you can add to an SCXIChassis. |
| SCXI1127 | Represents an SCXI-1127 module that you can add to an SCXIChassis. |
| SCXI1128 | Represents an SCXI-1128 module that you can add to an SCXIChassis. |
| SCXI1140 | Represents an SCXI-1140 module that you can add to an SCXIChassis. |
| SCXI1141 | Represents an SCXI-1141 module that you can add to an SCXIChassis. |
| SCXI1142 | Represents an SCXI-1142 module that you can add to an SCXIChassis. |
| SCXI1143 | Represents an SCXI-1143 module that you can add to an SCXIChassis. |
| SCXI1160 | Represents an SCXI-1160 module that you can add to an SCXIChassis. |
| SCXI1161 | Represents an SCXI-1161 module that you can add to an SCXIChassis. |
| SCXI1162 | Represents an SCXI-1162 module that you can add to an SCXIChassis. |
| SCXI1162HV | Represents an SCXI-1162HV module that you can add to an SCXIChassis. |
| SCXI1163 | Represents an SCXI-1163 module that you can add to an SCXIChassis. |
| SCXI1163R | Represents an SCXI-1163R module that you can add to an SCXIChassis. |
| SCXI1190 | Represents an SCXI-1190 module that you can add to an SCXIChassis. |
| SCXI1191 | Represents an SCXI-1191 module that you can add to an SCXIChassis. |
| SCXI1192 | Represents an SCXI-1192 module that you can add to an SCXIChassis. |
| SCXI1520 | Represents an SCXI-1520 module that you can add to an SCXIChassis. |
| SCXI1530 | Represents an SCXI-1530 module that you can add to an SCXIChassis. |
| SCXI1531 | Represents an SCXI-1531 module that you can add to an SCXIChassis. |
| SCXI1540 | Represents an SCXI-1540 module that you can add to an SCXIChassis. |
| SCXI1581 | Represents an SCXI-1581 module that you can add to an SCXIChassis. |
| SCXIChassis | Represents an SCXI chassis under a DAQDevice. |
| SCXIModule | Represents an SCXI module under an SCXIChassis. |
| SLSC | Represents the SLSC section of a Hardware. |
| SLSCChassis | Represents the SLSCChassis section of the SLSC. |
| SLSCChassisChannel | Represents the SLSC chassis channel node of a SLSCChassisChannelSection. |
| SLSCChassisChannelSection | Represents the SLSC chassis channel category section of an SLSCChassis. |
| SLSCChassisChannels | Represents the SLSCChassisChannels section of the SLSCChassis. |
| SLSCModuleCustomDevice | Represents an SLSC module custom device. |
| SLSCModules | Represents the SLSCModules section of the SLSCChassis. |
| Scale | Defines a base class for different types of scales allowed in system definition files. You can create scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator. |
| ScaleFolder | Represents a folder under the Scales section of the system definition. Folders simply organize scales into logical groups. |
| Scales | Represents the Scales section of the system definition, which contains Scale objects. Use scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator. |
| Section | Represents a section or node in the system definition. A section represents any node that contains additional nodes. |
| SetMultipleVariables | Represents a Set Multiple Variables step that you can add to a procedure. This step sets the values of multiple channels to constant values. |
| SetVariable | Represents a Set Variable step that you can add to a procedure. This step sets a channel, Variable, to a certain value. The value can be a constant or the result of a calculation using a Function you specify. |
| SignalBasedFrame | Represents a signal format frame under an NI-XNET LIN, FlexRay, or CAN port. |
| SignalBasedSignal | Represents a signal format signal under an NI-XNET SignalBasedFrame. |
| SimulationModels | Represents the Simulation Models section of a Target, which contains any models you import and information about the order in which they execute. |
| SinglePoint | Represents the Single-Point section under an Incoming section of an NI-XNET CAN, LIN, or FlexRay port. When you import single-point frames, NI VeriStand reads the most recent value received for the frame. |
| SkipCyclicFrames | Represents the Skip Cyclic Frames channel under the FrameFaulting section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies to skip transmission of a specified number of cyclic frames across the CAN bus when a specified trigger channel has a non-zero value. |
| SleepMode | Represents a Transceiver State, or Sleep Mode, channel under the CANInterfaceChannels section of an NI-XNET CAN port. This channel controls the sleep mode option on the CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame. |
| Sporadic | Represents the Sporadic section that contains outgoing, sporadic frames under an NI-XNET LIN port. |
| Stimulus | Represents the Stimulus section of a Target, which contains the stimulus generators available in the Legacy Stimulus Profile Editor. |
| StimulusChannel | Represents a stimulus channel of a Generator. |
| SystemChannel | Represents a system channel under the SystemChannels section. System channels monitor the state and condition of various aspects of the system. |
| SystemChannels | Represents the System Channels section of a Target, which contains a variety of channels that monitor the state and condition of various aspects of the system. |
| SystemDefinition | Represents a system definition file, which contains configuration settings for the VeriStand Engine. This class is the base class for configuring system definitions through this API. |
| SystemDefinitionExtensions | Extension methods to assist with manipulating the SystemDefinition. |
| SystemInitialization | Represents the System Initialization section of the system definition, which contains information about the order that multiple targets deploy relative to each other. |
| SystemMappings | Represents the System Mappings section of the system definition, which stores information about how source channels within the system definition map to destination channels. Destination channels store the mapping information. |
| Target | Represents a target in the system definition. |
| Targets | Represents the Targets section of the system definition, which contains all the targets you configure. |
| ThermocoupleScale | Represents a thermocouple Scale, which converts raw values from a thermocouple to Kelvins or degrees Celsius, Fahrenheit, or Rankine. |
| TimeDifference | Represents the Time Difference channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel stores the difference between the two most recent ReceiveTime timestamps. |
| TimeStepDuration | Represents a Time Step Duration channel, which you can use to get information about the duration, in microseconds, of the last time step of the model running on the target. |
| TimingAndSync | Represents the Timing and Sync section of the system definition, which contains all configured timing and sync devices. |
| TimingAndSyncDevice | Represents a timing and sync device, which is a custom device that can drive the RTSI 0 line and synchronize all the hardware I/O devices in the system. |
| TransmitTime | Represents a Transmit Time under the FrameFaulting section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies the amount of time that must elapse between subsequent transmissions of the cyclic frame. |
| Unconditional | Represents the Unconditional section that contains outgoing, unconditional frames under an NI-XNET LIN port. |
| UserChannel | Represents a user channel, which stores a single value. You can use user channels as variables in procedures, stimulus profiles, and so on. |
| UserChannels | Represents the User Channels section of a Target, which contains any user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on. |
| UserChannelsFolder | Represents a folder under the UserChannels section of a target. Folders simply organize user channels into logical groups. |
| Utilities | Class that provides a way to perform various common operations within the system definition, such as stripping paths, converting data types, and creating channel mappings. |
| Variant | Represents a variant value that encapsulates the type descriptor and data bytes. |
| VirtualECU | Represents a virtual ECU as a specialized type of Model and inherits all the capabilities of Model. Virtual ECUs within the same network cluster are automatically connected to each other and to real ECUs via an XNET interface. |
| Waveform | Represents a waveform in the system definition. This is a base class for more specific waveform classes, including hardware waveforms, custom device waveforms, and so on. |
| XNET | Represents the NI-XNET section of a Chassis, which contains any CAN, LIN, or FlexRay devices you configure. |
| XNETDatabases | Represents the XNET Databases section of a Target, which contains any XNET Databases you add to the system definition to run XNET devices. |

#### Interfaces

| Name | Description |
| --- | --- |
| ICANConfiguration | Represents the configuration for CAN communication. |
| IChannel | An interface defining system definition channel behavior. |
| ICustomDevicePluginNodeFactory | Defines a factory interface for creating and initializing custom device plugin nodes. |
| IECUNetworkClusterConfiguration | Interface for an ECU network cluster configuration. |
| IEthernetConfiguration | Represents the configuration for Ethernet communication. |
| ILINConfiguration | Represents the configuration for LIN communication. |
| IPluginNodeFactory | Defines a factory interface for creating plugin nodes from system storage data. |

#### Structures

| Name | Description |
| --- | --- |
| ValueSource | Represents the source of a channel value as a constant or a channel. |

#### Enumerations

| Name | Description |
| --- | --- |
| AcquisitionMode | Defines the acquisition mode of a DAQTask. |
| AcquisitionUnits | Defines whether the size of acquisitions is represented as samples per channel or time, in seconds. |
| ActionOnNew | Defines the location to which to log data when a DAQTaskAI begins a new acquisition. |
| AlarmMode | The action that occurs when the alarm is triggered on the target. |
| AlarmPriority | This enumeration is deprecated in NI VeriStand 2011 and later. Use the PriorityNumber property instead. |
| AlarmState | The state of an alarm on the target. |
| AlarmingStepFunction | The function of an alarm running on the target. |
| CANIOMode | I/O Mode used by the interface when transmitting a CAN frame. |
| CANTransceiverType | The transceiver type of an NI-XNET CAN port. |
| CANTransmitOrderType | The order in which the CAN interface transmits frames from the internal queue. |
| CDChannel_Type | Specifies the type (Input or Output) of a custom device channel. |
| CDDriverExecMode | Specifies the execution mode, or device type, of a custom device. The execution mode defines how the device interacts with the VeriStand Engine. |
| CDLoopType | Specifies the type of loop in which an asynchronous custom device executes. |
| CDTimeLoopPriority | Specifies the priority of the Timed Loop that an asynchronous custom device with a CDLoopType of TimedLoop executes in. If you want to wire this value to the input terminal of a Timed Loop in LabVIEW, you must first convert it to a positive integer between 1 and 65,535. |
| ChannelNames | Specifies how the names of DAQ channels appear in log files this task creates and in the list of available triggers. |
| CommunicationProtocol | Protocol used by the virtual ECU Network Cluster to communicate with the real ECU network. |
| ConditionStepComparison | The condition to use when comparing Variable and Value in a Condition step. |
| DAQAnalogChannelType | Specifies the measurement type of an analog DAQ channel. |
| DAQCM_Active_Edge | Specifies the edge on which the sample clock pulses to acquire or generate samples. |
| DAQCM_Clock_Source | Specifies the source of the sample clock. |
| DAQCM_Export_Clk_On_Line | Specifies the line that receives the pulse from the sample clock. |
| DAQCM_Export_Sample_Clock | Specifies the sample clock to export. |
| DAQCM_Export_StartTrigger_On_Line | Specifies the line that exports the Start Trigger. |
| DAQCM_Export_Start_Trigger | Specifies the start trigger to export. |
| DAQCM_Slope | Specifies the edge on which to trigger the device. |
| DAQCM_Trigger_Line | Specifies the line that triggers the acquisition or generation of samples. |
| DAQConversionRate | Specifies the rate used to run the analog-digital converters (ADCs) on a DAQ device. |
| DAQCounterCountMode | Specifies the mode of the count direction. |
| DAQCounterDecoding | Specifies the method used to count and interpret the pulses the encoder generates on signal A and signal B. Decoding1X, Decoding2X, and Decoding4X are valid for quadrature encoders only. |
| DAQCounterEdge | Specifies the mode the counter uses to count the edge. |
| DAQCounterType | Specifies the type of task the DAQ counter performs. |
| DAQCounterZIndexMode | Specifies the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than AHighBHigh. When signal Z transitions to high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B. |
| DAQDataChannelType | Specifies the type of data channel in a DAQ measurement DAQSectionType section. |
| DAQDeviceInputConfiguration | Specifies the input terminal configuration to apply to the device channels. |
| DAQMeasurementType | Specifies the measurement type of a DAQ channel. |
| DataLoggingFilterType | Specifies the type of filtering applied to a DataLoggingFile under an NI-XNET port. |
| DataLoggingOperationType | Specifies the action taken when a trigger condition is met. |
| DataLoggingTriggerType | Specifies the type of trigger used to start or stop logging data to a DataLoggingFile. |
| Delimiter | Defines the delimiter of the ParameterFile. |
| DependentFileType | Specifies the type of path used for the location of a DependentFile. |
| DirectionType | Defines the direction of a signal slope or edge that causes a trigger. |
| EdgeType | Defines the edge type of the sample clock. |
| FDISOMode | Specifies whether the interface is working in the ISO CAN FD standard (ISO standard 11898-1:2015) or non-ISO CAN FD standard (Bosch CAN FD 1.0 specification). Two ports using different standards (ISO CAN FD vs. non-ISO CAN FD) cannot communicate with each other. |
| FileLimitationType | Specifies the type of limit used to stop logging incoming frame data to an NI-XNET DataLoggingFile. |
| FileType | Specifies the file type of an NI-XNET DataLoggingFile. |
| FramePhaseType | Specifies whether to reset the timer of a software cyclic trigger after each transmission of an outgoing frame. |
| FrameTriggerType | Specifies a condition that a trigger channel must meet to trigger transmission of an outgoing frame. |
| FrameType | Specifies the type of a CAN or FlexRay frame. |
| GlobalParameterScopes | Specifies whether global parameters in a Model share their values with other models. |
| GlobalSequenceCommand | Specifies the command for all running sequences. |
| LogMode | The logging mode that determines whether components in the NI VeriStand system can read data as you log it. |
| ModelCommandState | Specifies the current state of the model. |
| PXIBackplaneReferenceClock | Specifies the PXI chassis backplane reference clock. |
| ParameterAccess | Defines the parameter access mode on the engine. The user can select to access only the imported parameters or all the parameters from the models. |
| ReflectiveMemoryDataChannelAccessType | Specifies the access type (read or write) of a data channel on a reflective memory device. |
| ReflectiveMemoryDataChannelDataType | Specifies the data type of a data channel on a reflective memory device. |
| ReflectiveMemoryInterruptType | Specifies the type of interrupt a ReflectiveMemory device sends or receives. |
| ReplayBehavior | Specifies whether and how frames in a data replay file on an NI-XNET CAN port are filtered. |
| SampleMode | Whether the AI acquisition is single-point or buffered. |
| ScaleType | This enumeration is used to select the Scale Type. |
| SetVariableStepFunction | Specifies the function to use on Value1 and Value2 of a SetVariable procedure step. |
| TargetControlLoopTimingSource | Specifies the timing source for the system. The timing source times the system by sending ticks to the Primary Control Loop. |
| TargetExecutionMode | Specifies the execution mode for the loops of the VeriStand Engine. |
| TargetTimingMode | The timing mode of the target. |
| TaskType | This enumeration is used to select the Task Type. |
| TemperatureUnit | Defines the Temperature Unit of the thermocouple. |
| ThermocoupleCJCType | Defines the CJC type. |
| ThermocoupleType | Defines the thermocouple type. |
| TimingSourceSettingsOptions | Specifies the DAQ timing source setting for the Primary Control Loop when the PCL timing source is set to DAQ. |
| TriggerType | Defines the type of a DAQTrigger. |
| VirtualECUToolchain | Toolchain that was used to build virtual ECUs. |
| WindowConditionType | Defines the signal condition that causes a window trigger. |
| XNETTermination | Configures onboard termination for the XNET port. Termination behavior differs depending on the type of device you are using (CAN, FlexRay, or LIN). |

#### Delegates

None
