# NI DOCUMENT BUNDLE: ni_rfsg-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni_rfsg-csharp-api-ref start=251 end=360 -->
<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-digitaledge.html language=enus -->
## TOPIC 00251: DigitalEdge

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-digitaledge.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the configuration parameters needed if the selected TriggerType type is DigitalEdge. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDigitalEdgeScriptTrigger DigitalEdge { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTrigger. ExceptionsTypeDescriptionSyst

### DigitalEdge

Gets the configuration parameters needed if the selected [TriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-triggertype.html) type is [DigitalEdge](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDigitalEdgeScriptTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger.html) DigitalEdge { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DigitalEdge property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-disable.html language=enus -->
## TOPIC 00252: Disable()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-disable.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for the specified Script trigger after the Initiate method is called. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Disable()RemarksCalling this method is only necessary if the Script trigger has been previously configured and must be dis

### Disable()

Configures the device to not wait for the specified Script trigger after the [Initiate](nationalinstruments-modularinstruments-nirfsg-nirfsg-initiate.html) method is called.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Disable()

#### Remarks

Calling this method is only necessary if the Script trigger has been previously configured and must be disabled.

The NI-RFSG device must be in the Configuration state before you call this method.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Disable method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-exportedoutputterminal.html language=enus -->
## TOPIC 00253: ExportedOutputTerminal

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-exportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-exportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination terminal for exporting the Script trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgScriptTriggerExportedOutputTerminal ExportedOutputTerminal { get; set; }RemarksSpecifies an object of type RfsgScriptTriggerExportedOutputTerminal. To set

### ExportedOutputTerminal

Gets or sets the destination terminal for exporting the Script trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) ExportedOutputTerminal { get; set; }

#### Remarks

Specifies an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html).

To set this property, the NI-RFSG device must be in the Configuration state. For trigger delay information, refer to the triggering section in the *NI RF Signal Generators Help*.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportedOutputTerminal property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00254: SendSoftwareEdgeTrigger()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-sendsoftwareedgetrigger.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Forces a particular trigger to occur. The specified trigger is generated regardless of whether the trigger has been configured as a software trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void SendSoftwareEdgeTrigger()ExceptionsTypeDescriptionSystem.ObjectDisposedExcep

### SendSoftwareEdgeTrigger()

Forces a particular trigger to occur. The specified trigger is generated regardless of whether the trigger has been configured as a software trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void SendSoftwareEdgeTrigger()

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SendSoftwareEdgeTrigger method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-synchronized.html language=enus -->
## TOPIC 00255: Synchronized

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-synchronized.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-synchronized.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the properties used for synchronizing the Script trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgSynchronizedScriptTrigger Synchronized { get; }RemarksReturns an object of type RfsgSynchronizedScriptTrigger. ExceptionsTypeDescriptionSystem.ObjectDisposedExc

### Synchronized

Provides the properties used for synchronizing the Script trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgSynchronizedScriptTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttrigger.html) Synchronized { get; }

#### Remarks

Returns an object of type [RfsgSynchronizedScriptTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttrigger.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Synchronized property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-terminalname.html language=enus -->
## TOPIC 00256: TerminalName

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-terminalname.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fully-qualified signal name as a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string TerminalName { get; }RemarksReturns a String representing the fully-qualified signal name. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe TerminalName property wa

### TerminalName

Gets the fully-qualified signal name as a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string TerminalName { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the fully-qualified signal name.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TerminalName property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-triggertype.html language=enus -->
## TOPIC 00257: TriggerType

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-triggertype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Script trigger type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgScriptTriggerType TriggerType { get; set; }RemarksSpecifies the RfsgScriptTriggerType enumeration. Depending upon the value of this property, more properties may be needed to fully configur

### TriggerType

Gets or sets the Script trigger type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgScriptTriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html) TriggerType { get; set; }

#### Remarks

Specifies the [RfsgScriptTriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html) enumeration.

Depending upon the value of this property, more properties may be needed to fully configure the trigger.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TriggerType property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger.html language=enus -->
## TOPIC 00258: RfsgScriptTrigger Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the channel-based methods and properties used to configure the Script trigger. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgScriptTrigger : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programmi

### RfsgScriptTrigger Class

Represents the channel-based methods and properties used to configure the Script trigger.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgScriptTrigger : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the configuration parameters needed if the selected TriggerType type is DigitalEdge. |
| DigitalLevel | Gets the configuration parameters needed if the selected TriggerType type is DigitalLevel. |
| ExportedOutputTerminal | Gets or sets the destination terminal for exporting the Script trigger. |
| Synchronized | Provides the properties used for synchronizing the Script trigger. |
| TerminalName | Gets the fully-qualified signal name as a string. |
| TriggerType | Gets or sets the Script trigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareTrigger() | Configures the Script trigger for software triggering. |
| Disable() | Configures the device to not wait for the specified Script trigger after the Initiate method is called. |
| SendSoftwareEdgeTrigger() | Forces a particular trigger to occur. The specified trigger is generated regardless of whether the trigger has been configured as a software trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio2.html language=enus -->
## TOPIC 00259: Dio2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Dio2 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the string "DI

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "DIO/PFI2".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio3.html language=enus -->
## TOPIC 00260: Dio3

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio3.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Dio3 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the string "DI

### Dio3

Gets the source terminal when the trigger is received on the DIO PFI3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Dio3 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "DIO/PFI3".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00261: Dio4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dio4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the string "DI

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dioo.html language=enus -->
## TOPIC 00262: DioO

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-dioo.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal DioO { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the string "DI

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) DioO { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "DIO/PFI0".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-donotexport.html language=enus -->
## TOPIC 00263: DoNotExport

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-donotexport.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-donotexport.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal DoNotExport { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing an empty string

### DoNotExport

Gets the destination terminal when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) DoNotExport { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing an empty string.

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-equals__object.html language=enus -->
## TOPIC 00264: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgScriptTriggerExportedOutputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to compared to

### Equals(object)

Determines whether the current instance of [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to compared to the current instance of RfsgScriptTriggerExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00265: FromString(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-fromstring__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsgScriptTriggerExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpecifies a strin

### FromString(string)

Creates an [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string representing the output terminal of RfsgScriptTrigger. |

#### Returns

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html).

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-operator-string__rfsgscripttriggerexportedoutputterminal.html language=enus -->
## TOPIC 00266: operator string(RfsgScriptTriggerExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-operator-string__rfsgscripttriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-operator-string__rfsgscripttriggerexportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsgScriptTriggerExportedOutputTerminal object to equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator string(RfsgScriptTriggerExportedOutputTerminal outputTerminal)ParametersNameTypeDescriptionoutputTerminalRfsgScriptTriggerEx

### operator string(RfsgScriptTriggerExportedOutputTerminal)

Converts the [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) object to equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator string(RfsgScriptTriggerExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsgScriptTriggerExportedOutputTerminal | Specifies the RfsgScriptTriggerExportedOutputTerminal object to be converted to string. |

#### Returns

Returns a string from the [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) object.

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi0.html language=enus -->
## TOPIC 00267: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Pfi0 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the

### Pfi0

Gets the destination terminal when the signal is exported to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PFI0".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi1.html language=enus -->
## TOPIC 00268: Pfi1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 1 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Pfi1 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the

### Pfi1

Gets the destination terminal when the signal is exported to the PFI 1 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Pfi1 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PFI1".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi4.html language=enus -->
## TOPIC 00269: Pfi4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 4 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Pfi4 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the

### Pfi4

Gets the destination terminal when the signal is exported to the PFI 4 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Pfi4 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PFI4".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi5.html language=enus -->
## TOPIC 00270: Pfi5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pfi5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 5 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal Pfi5 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal representing the

### Pfi5

Gets the destination terminal when the signal is exported to the PFI 5 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) Pfi5 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PFI5".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxiedstarc.html language=enus -->
## TOPIC 00271: PXIeDStarC

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxiedstarc.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxiedstarc.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid only on the PXIe-5820/5830/5831/5832/5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PXIeDStarC { get; }RemarksRet

### PXIeDStarC

Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid only on the PXIe-5820/5830/5831/5832/5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PXIeDStarC { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXIe_DStarC".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00272: PxiTriggerLine0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine0

Gets the destination terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00273: PxiTriggerLine1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine1

Gets the destination terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00274: PxiTriggerLine2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine2

Gets the destination terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00275: PxiTriggerLine3

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline3.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine3 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine3

Gets the destination terminal when the signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig3".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00276: PxiTriggerLine4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine4

Gets the destination terminal when the signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig4".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00277: PxiTriggerLine5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine5

Gets the destination terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00278: PxiTriggerLine6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-pxitriggerline6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgScriptTriggerExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type RfsgScriptTriggerExportedOutputTerminal re

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-tostring.html language=enus -->
## TOPIC 00279: ToString()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal-tostring.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsgStartTriggerExportedOutputTerminal to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override string ToString()ReturnsReturns a string that represents the current instance of RfsgScriptTriggerExportedOutputTerminal.

### ToString()

Converts the current instance of [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsgScriptTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html).

Parent topic:

RfsgScriptTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html language=enus -->
## TOPIC 00280: RfsgScriptTriggerExportedOutputTerminal Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggerexportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the destination terminal of RfsgScriptTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgScriptTriggerExportedOutputTerminalRemarksSee ExportedOutputTerminal. PropertiesNameDescriptionDio1Gets the source terminal when the trigger is rec

### RfsgScriptTriggerExportedOutputTerminal Class

Represents the destination terminal of [RfsgScriptTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgScriptTriggerExportedOutputTerminal

#### Remarks

See [ExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-exportedoutputterminal.html).

#### Properties

| Name | Description |
| --- | --- |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| DoNotExport | Gets the destination terminal when the signal is not exported. |
| Pfi0 | Gets the destination terminal when the signal is exported to the PFI 0 connector. |
| Pfi1 | Gets the destination terminal when the signal is exported to the PFI 1 connector. |
| Pfi4 | Gets the destination terminal when the signal is exported to the PFI 4 connector. |
| Pfi5 | Gets the destination terminal when the signal is exported to the PFI 5 connector. |
| PXIeDStarC | Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid only on the PXIe-5820/5830/5831/5832/5840. |
| PxiTriggerLine0 | Gets the destination terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the destination terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the destination terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the destination terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the destination terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the destination terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the destination terminal when the signal is exported to the PXI trigger line 6. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgScriptTriggerExportedOutputTerminal object from the specified string. |
| Equals(RfsgScriptTriggerExportedOutputTerminal) | Determines whether the current instance of RfsgScriptTriggerExportedOutputTerminal and the RfsgScriptTriggerExportedOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgScriptTriggerExportedOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgScriptTriggerExportedOutputTerminal. |
| ToString() | Converts the current instance of RfsgStartTriggerExportedOutputTerminal to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgScriptTriggerExportedOutputTerminal(string) | Convert the specified string to equivalent RfsgScriptTriggerExportedOutputTerminal object. |
| operator string(RfsgScriptTriggerExportedOutputTerminal) | Converts the RfsgScriptTriggerExportedOutputTerminal object to equivalent string. |
| operator!=(RfsgScriptTriggerExportedOutputTerminal, RfsgScriptTriggerExportedOutputTerminal) | Checks whether the two instances of RfsgScriptTriggerExportedOutputTerminal are unequal. |
| operator==(RfsgScriptTriggerExportedOutputTerminal, RfsgScriptTriggerExportedOutputTerminal) | Checks whether the two instances of RfsgScriptTriggerExportedOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html language=enus -->
## TOPIC 00281: RfsgScriptTriggerType Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Script trigger type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgScriptTriggerTypeMembersNameValueDescriptionNone(int)0No trigger is configured. Signal generation starts immediately. DigitalEdge(int)1The data operation does not start until a digital ed

### RfsgScriptTriggerType Enumeration

Specifies the Script trigger type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgScriptTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | (int)0 | No trigger is configured. Signal generation starts immediately. |
| DigitalEdge | (int)1 | The data operation does not start until a digital edge is detected. The source of the digital edge is specified in Source and the active edge is specified in Edge. |
| DigitalLevel | (int)8000 | The data operation does not start until a digital level is detected. The source of the digital level is specified in Source and the active level is specified in Level. |
| Software | (int)2 | The data operation does not start until a software event occurs. You may create a software event by calling SendSoftwareEdgeTrigger. |

#### See Also

- TriggerType

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-alignlodaisychain5840__bool-string-string-rfsgrfporttype_arr1-double-double.html language=enus -->
## TOPIC 00282: AlignLODaisyChain5840(bool, string, string, RfsgRFPortType[], double, double)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-alignlodaisychain5840__bool-string-string-rfsgrfporttype_arr1-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-alignlodaisychain5840__bool-string-string-rfsgrfporttype_arr1-double-double.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs an external LO alignment by adjusting the LOInPower (dBm) property settings for optimal use with the PXIe-5653. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void AlignLODaisyChain5840(bool useExternalLO, string externalLO, string resourceName, RfsgRFPortType[] portTy

### AlignLODaisyChain5840(bool, string, string, RfsgRFPortType[], double, double)

Performs an external LO alignment by adjusting the [LOInPower](nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-loinpower.html) (dBm) property settings for optimal use with the PXIe-5653.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void AlignLODaisyChain5840(bool useExternalLO, string externalLO, string resourceName, RfsgRFPortType[] portTypes, double startFrequency, double stopFrequency)

#### Remarks

Ensure the PXIe-5840 is unassociated from the PXIe-5653 in Measurement and Automation Explorer before calling this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| useExternalLO | bool | Specifies whether the PXIe-5653 is used as the external LO. The default value is TRUE. |
| externalLO | string | Specifies the resource name of the PXIe-5653. |
| resourceName | string | Specifies the resource name of the daisy-chained PXIe-5840 device. |
| portTypes | RfsgRFPortType[] | Specifies the port type of the daisy-chained PXIe-5840. |
| startFrequency | double | Specifies the lower limit of a span of frequencies, in hertz (Hz). |
| stopFrequency | double | Specifies the upper limit of a span of frequencies, in hertz (Hz). |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AlignLODaisyChain5840 method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-clearselfcalibraterange.html language=enus -->
## TOPIC 00283: ClearSelfCalibrateRange()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-clearselfcalibraterange.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-clearselfcalibraterange.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the data obtained from SelfCalibrateRange. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ClearSelfCalibrateRange()ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe ClearSelfCalibrateRange method was accessed after the associated NIRfsg object was disposed.

### ClearSelfCalibrateRange()

Clears the data obtained from [SelfCalibrateRange](nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibraterange__rfsgselfcalibrationsteps-double-double-double-double.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ClearSelfCalibrateRange()

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ClearSelfCalibrateRange method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-getselfcalibrationlastdateandtime__rfsgdevicemodule.html language=enus -->
## TOPIC 00284: GetSelfCalibrationLastDateAndTime(RfsgDeviceModule)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-getselfcalibrationlastdateandtime__rfsgdevicemodule.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-getselfcalibrationlastdateandtime__rfsgdevicemodule.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic DateTime GetSelfCalibrationLastDateAndTime(RfsgDeviceModule module)ParametersNameTypeDescriptionmoduleRfsgDeviceModuleSpecifies from which module to retrieve the la

### GetSelfCalibrationLastDateAndTime(RfsgDeviceModule)

Returns the date and time of the last successful self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public DateTime GetSelfCalibrationLastDateAndTime(RfsgDeviceModule module)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| module | RfsgDeviceModule | Specifies from which module to retrieve the last successful self-calibration date and time. |

#### Returns

Returns the date and time of the last successful calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetSelfCalibrationLastDateAndTime method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-getselfcalibrationtemperature__rfsgdevicemodule.html language=enus -->
## TOPIC 00285: GetSelfCalibrationTemperature(RfsgDeviceModule)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-getselfcalibrationtemperature__rfsgdevicemodule.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-getselfcalibrationtemperature__rfsgdevicemodule.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double GetSelfCalibrationTemperature(RfsgDeviceModule module)RemarksSupported Devices: NI5610, NI5653, NI5670/5671/5672/5673/567

### GetSelfCalibrationTemperature(RfsgDeviceModule)

Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double GetSelfCalibrationTemperature(RfsgDeviceModule module)

#### Remarks

Supported Devices: NI 5610, NI 5653, NI 5670/5671/5672/5673/5673E

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| module | RfsgDeviceModule | Specifies the module to retrieve the last successful self-calibration temperature. Default Value: PrimaryModule |

#### Returns

Returns the temperature of the device at the last successful self-calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetSelfCalibrationTemperature method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-lastselfcalibrationtemperature.html language=enus -->
## TOPIC 00286: LastSelfCalibrationTemperature

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-lastselfcalibrationtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-lastselfcalibrationtemperature.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the temperature of the device at the time of the last self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double LastSelfCalibrationTemperature { get; }RemarksReturns a Double representing the temperature, in degrees Celsius (C), of the device at the time of

### LastSelfCalibrationTemperature

Gets the temperature of the device at the time of the last self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double LastSelfCalibrationTemperature { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the temperature, in degrees Celsius (°C), of the device at the time of the last self-calibration.

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibrate.html language=enus -->
## TOPIC 00287: SelfCalibrate()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibrate.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs an internal self-calibration on the device and associated modules that support self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void SelfCalibrate()RemarksIf the calibration is successful, new calibration data and constants are stored in the onboard non

### SelfCalibrate()

Performs an internal self-calibration on the device and associated modules that support self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void SelfCalibrate()

#### Remarks

If the calibration is successful, new calibration data and constants are stored in the onboard non-volatile memory of the module. If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840 while this method runs, it may remain open but cannot be used for operations that access the hardware. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SelfCalibrate method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibraterange__rfsgselfcalibrationsteps-double-double-double-double.html language=enus -->
## TOPIC 00288: SelfCalibrateRange(RfsgSelfCalibrationSteps, double, double, double, double)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibraterange__rfsgselfcalibrationsteps-double-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-selfcalibraterange__rfsgselfcalibrationsteps-double-double-double-double.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-calibration on the configurations within the specified frequency and peak power level limits. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void SelfCalibrateRange(RfsgSelfCalibrationSteps stepsToOmit, double minFrequency, double maxFrequency, double minPowerLe

### SelfCalibrateRange(RfsgSelfCalibrationSteps, double, double, double, double)

Performs a self-calibration on the configurations within the specified frequency and peak power level limits.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void SelfCalibrateRange(RfsgSelfCalibrationSteps stepsToOmit, double minFrequency, double maxFrequency, double minPowerLevel, double maxPowerLevel)

#### Remarks

NI recommends that no external signals are present on the RF In or IQ In ports during the calibration. This method does not update self calibration date and temperature.

Self-calibration range data is valid until you restart the system or call the [ClearSelfCalibrateRange](nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration-clearselfcalibraterange.html) method.

NI recommends that no external signals are present on the RF In port while the calibration is taking place.

For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit that step for faster execution.

Note

If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840 while this method runs, it may remain open but cannot beused for operations that access the hardware, for example Commit or Initiate.

Note

If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this method runs.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stepsToOmit | RfsgSelfCalibrationSteps | Specifies the steps to omit during self-calibration. |
| minFrequency | double | Specifies the minimum frequency. |
| maxFrequency | double | Specifies the maximum frequency. |
| minPowerLevel | double | Specifies the minimum power level. |
| maxPowerLevel | double | Specifies the maximum power level. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SelfCalibrateRange method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSelfCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration.html language=enus -->
## TOPIC 00289: RfsgSelfCalibration Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the methods and properties to perform self-calibration and to query data related to self-calibration. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgSelfCalibration : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Inst

### RfsgSelfCalibration Class

Provides the methods and properties to perform self-calibration and to query data related to self-calibration.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgSelfCalibration : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| LastSelfCalibrationTemperature | Gets the temperature of the device at the time of the last self-calibration. |

#### Methods

| Name | Description |
| --- | --- |
| AlignLODaisyChain5840(bool, string, string, RfsgRFPortType[], double, double) | Performs an external LO alignment by adjusting the LOInPower (dBm) property settings for optimal use with the PXIe-5653. |
| ClearSelfCalibrateRange() | Clears the data obtained from SelfCalibrateRange. |
| GetSelfCalibrationLastDateAndTime(RfsgDeviceModule) | Returns the date and time of the last successful self-calibration. |
| GetSelfCalibrationTemperature(RfsgDeviceModule) | Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration. |
| SelfCalibrate() | Performs an internal self-calibration on the device and associated modules that support self-calibration. |
| SelfCalibrateRange(RfsgSelfCalibrationSteps, double, double, double, double) | Performs a self-calibration on the configurations within the specified frequency and peak power level limits. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibrationsteps.html language=enus -->
## TOPIC 00290: RfsgSelfCalibrationSteps Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibrationsteps.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibrationsteps.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which calibration steps to skip as part of the self-calibration process. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgSelfCalibrationStepsMembersNameValueDescriptionOmitNone(long)0x0000000000000000Specifies that no calibration steps are omitted. LOSelfCal(l

### RfsgSelfCalibrationSteps Enumeration

Specifies which calibration steps to skip as part of the self-calibration process.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgSelfCalibrationSteps

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OmitNone | (long)0x0000000000000000 | Specifies that no calibration steps are omitted. |
| LOSelfCal | (long)0x0000000000000001 | Omits the LO Self Cal step. |
| PowerLevelAccuracy | (long)0x0000000000000002 | Omits the Power Level Accuracy step. |
| ResidualLOPower | (long)0x0000000000000004 | Omits the Residual LO Power step. |
| ImageSuppression | (long)0x0000000000000008 | Omits the Image Suppression step. |
| SynthesizerAlignment | (long)0x0000000000000010 | Omits the Voltage Controlled Oscillator (VCO) Alignment step. |

#### See Also

- SelfCalibrateRange

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-code.html language=enus -->
## TOPIC 00291: Code

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-code.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-code.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the numeric result from the self-test operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic int Code { get; }RemarksReturns an Int32 containing the self test code.

### Code

Gets the numeric result from the self-test operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public int Code { get; }

#### Remarks

Returns an [Int32](https://learn.microsoft.com/dotnet/api/system.int32) containing the self test code.

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-equals__object.html language=enus -->
## TOPIC 00292: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of SelfTest and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the current instance of Rfs

### Equals(object)

Determines whether the current instance of [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsgSelfTestResult. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-equals__rfsgselftestresult.html language=enus -->
## TOPIC 00293: Equals(RfsgSelfTestResult)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-equals__rfsgselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-equals__rfsgselftestresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgSelfTestResult and the RfsgSelfTestResult object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgSelfTestResult result)ParametersNameTypeDescriptionresultRfsgSelfTestResultSpecifies the Rf

### Equals(RfsgSelfTestResult)

Determines whether the current instance of [RfsgSelfTestResult](nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult.html) and the [RfsgSelfTestResult](nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgSelfTestResult result)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result | RfsgSelfTestResult | Specifies the RfsgSelfTestResult object to be compared to the current instance of RfsgSelfTestResult. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-gethashcode.html language=enus -->
## TOPIC 00294: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of SelfTest. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of SelfTest.

### GetHashCode()

Returns the hash code for the current instance of [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html).

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-message.html language=enus -->
## TOPIC 00295: Message

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-message.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-message.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string returned from the instrument SelfTest. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string Message { get; }RemarksReturns a String representing the string returned from the instrument SelfTest.

### Message

Gets the string returned from the instrument [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string Message { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the string returned from the instrument [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html).

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-operator_eq__rfsgselftestresult-rfsgselftestresult.html language=enus -->
## TOPIC 00296: operator==(RfsgSelfTestResult, RfsgSelfTestResult)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-operator_eq__rfsgselftestresult-rfsgselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-operator_eq__rfsgselftestresult-rfsgselftestresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether two SelfTest instances have the same value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgSelfTestResult result1, RfsgSelfTestResult result2)ParametersNameTypeDescriptionresult1RfsgSelfTestResultSpecifies an RfsgSelfTestResult inst

### operator==(RfsgSelfTestResult, RfsgSelfTestResult)

Determines whether two [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html) instances have the same value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgSelfTestResult result1, RfsgSelfTestResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | RfsgSelfTestResult | Specifies an RfsgSelfTestResult instance to compare with result1. |
| result2 | RfsgSelfTestResult | Specifies an RfsgSelfTestResult instance to compare with result2. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-operator_neq__rfsgselftestresult-rfsgselftestresult.html language=enus -->
## TOPIC 00297: operator!=(RfsgSelfTestResult, RfsgSelfTestResult)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-operator_neq__rfsgselftestresult-rfsgselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-operator_neq__rfsgselftestresult-rfsgselftestresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether two instances of SelfTest are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgSelfTestResult result1, RfsgSelfTestResult result2)ParametersNameTypeDescriptionresult1RfsgSelfTestResultSpecifies an RfsgSelfTestResult instance to c

### operator!=(RfsgSelfTestResult, RfsgSelfTestResult)

Checks whether two instances of [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgSelfTestResult result1, RfsgSelfTestResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | RfsgSelfTestResult | Specifies an RfsgSelfTestResult instance to compare with result1. |
| result2 | RfsgSelfTestResult | Specifies an RfsgSelfTestResult instance to compare with result2. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-rfsgselftestresult__int-string.html language=enus -->
## TOPIC 00298: RfsgSelfTestResult(int, string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-rfsgselftestresult__int-string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult-rfsgselftestresult__int-string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RfsgSelfTestResult. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgSelfTestResult(int code, string message)ParametersNameTypeDescriptioncodeintSpecifies the numeric result from the self-test operation. 0 = no error (test passed).messagestringSp

### RfsgSelfTestResult(int, string)

Initializes a new instance of [RfsgSelfTestResult](nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public RfsgSelfTestResult(int code, string message)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| code | int | Specifies the numeric result from the self-test operation. 0 = no error (test passed). |
| message | string | Specifies the self-test status message. |

Parent topic:

RfsgSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult.html language=enus -->
## TOPIC 00299: RfsgSelfTestResult Data Structure

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgselftestresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the result of the SelfTest. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic struct RfsgSelfTestResultRemarksFor more information, refer to the NI RF Signal Generators Help. ConstructorsNameDescriptionRfsgSelfTestResult(int, string)Initializes a new ins

### RfsgSelfTestResult Data Structure

Represents the result of the [SelfTest](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-selftest.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public struct RfsgSelfTestResult

#### Remarks

For more information, refer to the *NI RF Signal Generators Help*.

#### Constructors

| Name | Description |
| --- | --- |
| RfsgSelfTestResult(int, string) | Initializes a new instance of RfsgSelfTestResult. |

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets the numeric result from the self-test operation. |
| Message | Gets the string returned from the instrument SelfTest. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(RfsgSelfTestResult) | Determines whether the current instance of RfsgSelfTestResult and the RfsgSelfTestResult object that you specify are equal. |
| Equals(object) | Determines whether the current instance of SelfTest and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of SelfTest. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(RfsgSelfTestResult, RfsgSelfTestResult) | Checks whether two instances of SelfTest are unequal. |
| operator==(RfsgSelfTestResult, RfsgSelfTestResult) | Determines whether two SelfTest instances have the same value. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-equals__object.html language=enus -->
## TOPIC 00300: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgSignalIdentifier and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the current ins

### Equals(object)

Determines whether the current instance of [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsgSignalIdentifier. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-equals__rfsgsignalidentifier.html language=enus -->
## TOPIC 00301: Equals(RfsgSignalIdentifier)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-equals__rfsgsignalidentifier.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-equals__rfsgsignalidentifier.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgSignalIdentifier and the RfsgSignalIdentifier object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgSignalIdentifier signalIdentifier)ParametersNameTypeDescriptionsignalIdentifierRfsgSign

### Equals(RfsgSignalIdentifier)

Determines whether the current instance of [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) and the [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgSignalIdentifier signalIdentifier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalIdentifier | RfsgSignalIdentifier | Specifies the RfsgSignalIdentifier object to be compared to the current instance of RfsgSignalIdentifier. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-fromstring__string.html language=enus -->
## TOPIC 00302: FromString(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-fromstring__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsgSignalIdentifier object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSignalIdentifier FromString(string signalIdentifier)ParametersNameTypeDescriptionsignalIdentifierstringSpecifies a string that is the signal identifier of

### FromString(string)

Creates an [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) FromString(string signalIdentifier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalIdentifier | string | Specifies a string that is the signal identifier of RfsgSignalIdentifier. |

#### Returns

Returns an object of type [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html).

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-gethashcode.html language=enus -->
## TOPIC 00303: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgSignalIdentifier. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgSignalIdentifier.

### GetHashCode()

Returns the hash code for the current instance of [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html).

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-marker0.html language=enus -->
## TOPIC 00304: Marker0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-marker0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-marker0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies Marker 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSignalIdentifier Marker0 { get; }RemarksReturns an object of type RfsgSignalIdentifier representing the string "Marker0".

### Marker0

Specifies Marker 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) Marker0 { get; }

#### Remarks

Returns an object of type [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) representing the string "Marker0".

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-marker1.html language=enus -->
## TOPIC 00305: Marker1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-marker1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-marker1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies Marker 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSignalIdentifier Marker1 { get; }RemarksReturns an object of type RfsgSignalIdentifier representing the string "Marker1".

### Marker1

Specifies Marker 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) Marker1 { get; }

#### Remarks

Returns an object of type [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) representing the string "Marker1".

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-operator-string__rfsgsignalidentifier.html language=enus -->
## TOPIC 00306: operator string(RfsgSignalIdentifier)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-operator-string__rfsgsignalidentifier.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier-operator-string__rfsgsignalidentifier.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsgSignalIdentifier object to equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator string(RfsgSignalIdentifier signalIdentifier)ParametersNameTypeDescriptionsignalIdentifierRfsgSignalIdentifierSpecifies the RfsgSignalIdentifie

### operator string(RfsgSignalIdentifier)

Converts the [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) object to equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator string(RfsgSignalIdentifier signalIdentifier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalIdentifier | RfsgSignalIdentifier | Specifies the RfsgSignalIdentifier object to be converted to string. |

#### Returns

Returns a string from the [RfsgSignalIdentifier](nationalinstruments-modularinstruments-nirfsg-rfsgsignalidentifier.html) object.

Parent topic:

RfsgSignalIdentifier Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalpath-maxfundamentalsilofrequency.html language=enus -->
## TOPIC 00307: MaxFundamentalSiloFrequency

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalpath-maxfundamentalsilofrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalpath-maxfundamentalsilofrequency.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum fundamental silo frequency. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double MaxFundamentalSiloFrequency { get; }RemarksSpecifies the maximum fundamental silo frequency in Hz. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe MaxFundamentalSiloFre

### MaxFundamentalSiloFrequency

Gets the maximum fundamental silo frequency.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double MaxFundamentalSiloFrequency { get; }

#### Remarks

Specifies the maximum fundamental silo frequency in Hz.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The MaxFundamentalSiloFrequency property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSignalPath Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsignalpath-minfundamentalsilofrequency.html language=enus -->
## TOPIC 00308: MinFundamentalSiloFrequency

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsignalpath-minfundamentalsilofrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsignalpath-minfundamentalsilofrequency.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum fundamental silo frequency. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double MinFundamentalSiloFrequency { get; }RemarksSpecifies the minimum fundamental silo frequency in Hz. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe MinFundamentalSiloFre

### MinFundamentalSiloFrequency

Gets the minimum fundamental silo frequency.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double MinFundamentalSiloFrequency { get; }

#### Remarks

Specifies the minimum fundamental silo frequency in Hz.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The MinFundamentalSiloFrequency property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSignalPath Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent-exportedoutputterminal.html language=enus -->
## TOPIC 00309: ExportedOutputTerminal

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent-exportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent-exportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination terminal for exporting the Started event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgStartedEventExportedOutputTerminal ExportedOutputTerminal { get; set; }RemarksSpecifies an object of type RfsgStartedEventExportedOutputTerminal. To set thi

### ExportedOutputTerminal

Gets or sets the destination terminal for exporting the Started event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) ExportedOutputTerminal { get; set; }

#### Remarks

Specifies an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html).

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportedOutputTerminal property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgStartedEvent Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent.html language=enus -->
## TOPIC 00310: RfsgStartedEvent Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the properties to configure Started events. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgStartedEvent : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Signal Gene

### RfsgStartedEvent Class

Provides the properties to configure Started events.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgStartedEvent : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| ExportedOutputTerminal | Gets or sets the destination terminal for exporting the Started event. |
| TerminalName | Gets the fully-qualified signal name as a string. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00311: Dio4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-dio4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal representing the string "DIO/

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-dioo.html language=enus -->
## TOPIC 00312: DioO

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-dioo.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal DioO { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal representing the string "DIO/

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) DioO { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "DIO/PFI0".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-equals__rfsgstartedeventexportedoutputterminal.html language=enus -->
## TOPIC 00313: Equals(RfsgStartedEventExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-equals__rfsgstartedeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-equals__rfsgstartedeventexportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgStartedEventExportedOutputTerminal and the RfsgStartedEventExportedOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgStartedEventExportedOutputTerminal outputTerminal)P

### Equals(RfsgStartedEventExportedOutputTerminal)

Determines whether the current instance of [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) and the [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgStartedEventExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsgStartedEventExportedOutputTerminal | Specifies the RfsgStartedEventExportedOutputTerminal object to be compared to the current instance of RfsgStartedEventExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pfi0.html language=enus -->
## TOPIC 00314: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal Pfi0 { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal representing the s

### Pfi0

Gets the destination terminal when the signal is exported to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "PFI0".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00315: PxiTriggerLine2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal repr

### PxiTriggerLine2

Gets the destination terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00316: PxiTriggerLine4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal repr

### PxiTriggerLine4

Gets the destination terminal when the signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "PXI_Trig4".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00317: PxiTriggerLine5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal repr

### PxiTriggerLine5

Gets the destination terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00318: PxiTriggerLine6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal-pxitriggerline6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartedEventExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type RfsgStartedEventExportedOutputTerminal repr

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [RfsgStartedEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstartedeventexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

RfsgStartedEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-configuresoftwaretrigger.html language=enus -->
## TOPIC 00319: ConfigureSoftwareTrigger()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-configuresoftwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-configuresoftwaretrigger.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for software triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ConfigureSoftwareTrigger()RemarksRefer SendSoftwareEdgeTrigger for more information about using a software trigger. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionT

### ConfigureSoftwareTrigger()

Configures the Start trigger for software triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ConfigureSoftwareTrigger()

#### Remarks

Refer [SendSoftwareEdgeTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-sendsoftwareedgetrigger.html) for more information about using a software trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ConfigureSoftwareTrigger method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgStartTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-digitaledge.html language=enus -->
## TOPIC 00320: DigitalEdge

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-digitaledge.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the configuration parameters needed if the selected Start trigger type is DigitalEdge. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDigitalEdgeStartTrigger DigitalEdge { get; }RemarksReturns an object of type RfsgDigitalEdgeStartTrigger. ExceptionsTypeDescriptionSyst

### DigitalEdge

Gets the configuration parameters needed if the selected Start trigger type is [DigitalEdge](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgestarttrigger.html) DigitalEdge { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgestarttrigger.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DigitalEdge property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgStartTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-disable.html language=enus -->
## TOPIC 00321: Disable()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-disable.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a Start trigger after Initiate is called. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Disable()RemarksCalling this method is only necessary if the Start trigger has been previously configured and now must be disabled. The NI-RFSG de

### Disable()

Configures the device to not wait for a Start trigger after [Initiate](nationalinstruments-modularinstruments-nirfsg-nirfsg-initiate.html) is called.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Disable()

#### Remarks

Calling this method is only necessary if the Start trigger has been previously configured and now must be disabled.

The NI-RFSG device must be in the Configuration state before you call this method.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Disable method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgStartTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-triggertype.html language=enus -->
## TOPIC 00322: TriggerType

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttrigger-triggertype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Start trigger type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgStartTriggerType TriggerType { get; set; }RemarksSpecifies the RfsgStartTriggerType enumeration. Depending upon the value of this property, more properties may be needed to fully configure t

### TriggerType

Gets or sets the Start trigger type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgStartTriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggertype.html) TriggerType { get; set; }

#### Remarks

Specifies the [RfsgStartTriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggertype.html) enumeration.

Depending upon the value of this property, more properties may be needed to fully configure the trigger.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TriggerType property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgStartTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-dio2.html language=enus -->
## TOPIC 00323: Dio2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-dio2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartTriggerExportedOutputTerminal Dio2 { get; }RemarksReturns an object of type RfsgStartTriggerExportedOutputTerminal representing the string "DIO/

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) representing the string "DIO/PFI2".

Parent topic:

RfsgStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-dio5.html language=enus -->
## TOPIC 00324: Dio5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-dio5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-dio5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartTriggerExportedOutputTerminal Dio5 { get; }RemarksReturns an object of type RfsgStartTriggerExportedOutputTerminal representing the string "DIO/

### Dio5

Gets the source terminal when the trigger is received on the DIO PFI5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) Dio5 { get; }

#### Remarks

Returns an object of type [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) representing the string "DIO/PFI5".

Parent topic:

RfsgStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-operator_neq__rfsgstarttriggerexportedoutputterminal-rfsgstarttriggerexportedoutputterminal.html language=enus -->
## TOPIC 00325: operator!=(RfsgStartTriggerExportedOutputTerminal, RfsgStartTriggerExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-operator_neq__rfsgstarttriggerexportedoutputterminal-rfsgstarttriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-operator_neq__rfsgstarttriggerexportedoutputterminal-rfsgstarttriggerexportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgStartTriggerExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgStartTriggerExportedOutputTerminal outputTerminal1, RfsgStartTriggerExportedOutputTerminal outputTerminal2)Parameter

### operator!=(RfsgStartTriggerExportedOutputTerminal, RfsgStartTriggerExportedOutputTerminal)

Checks whether the two instances of [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgStartTriggerExportedOutputTerminal outputTerminal1, RfsgStartTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsgStartTriggerExportedOutputTerminal | Specifies an RfsgStartTriggerExportedOutputTerminal object. |
| outputTerminal2 | RfsgStartTriggerExportedOutputTerminal | Specifies an RfsgStartTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pfi0.html language=enus -->
## TOPIC 00326: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartTriggerExportedOutputTerminal Pfi0 { get; }RemarksReturns an object of type RfsgStartTriggerExportedOutputTerminal representing the s

### Pfi0

Gets the destination terminal when the signal is exported to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) representing the string "PFI0".

Parent topic:

RfsgStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pfi1.html language=enus -->
## TOPIC 00327: Pfi1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pfi1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 1 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartTriggerExportedOutputTerminal Pfi1 { get; }RemarksReturns an object of type RfsgStartTriggerExportedOutputTerminal representing the s

### Pfi1

Gets the destination terminal when the signal is exported to the PFI 1 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) Pfi1 { get; }

#### Remarks

Returns an object of type [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) representing the string "PFI1".

Parent topic:

RfsgStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00328: PxiTriggerLine6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal-pxitriggerline6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgStartTriggerExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type RfsgPxiChassisClock10Source representing th

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgstarttriggerexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) representing the string "PXI_Trig6".

Parent topic:

RfsgStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedsampleclockdistributionline-tostring.html language=enus -->
## TOPIC 00329: ToString()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedsampleclockdistributionline-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedsampleclockdistributionline-tostring.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsgSynchronizedSampleClockDistributionLine to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override string ToString()ReturnsReturns a string that represents the current instance of RfsgSynchronizedSampleClockDistributionLine.

### ToString()

Converts the current instance of [RfsgSynchronizedSampleClockDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedsampleclockdistributionline.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsgSynchronizedSampleClockDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedsampleclockdistributionline.html).

Parent topic:

RfsgSynchronizedSampleClockDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-equals__rfsgsynchronizedscripttriggerdistributionline.html language=enus -->
## TOPIC 00330: Equals(RfsgSynchronizedScriptTriggerDistributionLine)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-equals__rfsgsynchronizedscripttriggerdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-equals__rfsgsynchronizedscripttriggerdistributionline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgSynchronizedScriptTriggerDistributionLine and the RfsgSynchronizedScriptTriggerDistributionLine object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgSynchronizedScriptTriggerDistribution

### Equals(RfsgSynchronizedScriptTriggerDistributionLine)

Determines whether the current instance of [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) and the [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgSynchronizedScriptTriggerDistributionLine distributionLine)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| distributionLine | RfsgSynchronizedScriptTriggerDistributionLine | Specifies the RfsgSynchronizedScriptTriggerDistributionLine object to be compared to the current instance of RfsgSynchronizedScriptTriggerDistributionLine. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-gethashcode.html language=enus -->
## TOPIC 00331: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgSynchronizedScriptTriggerDistributionLine. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgSynchronizedScriptTrig

### GetHashCode()

Returns the hash code for the current instance of [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html).

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-operator-string__rfsgsynchronizedscripttriggerdistributionline.html language=enus -->
## TOPIC 00332: operator string(RfsgSynchronizedScriptTriggerDistributionLine)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-operator-string__rfsgsynchronizedscripttriggerdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-operator-string__rfsgsynchronizedscripttriggerdistributionline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsgSynchronizedScriptTriggerDistributionLine object to equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator string(RfsgSynchronizedScriptTriggerDistributionLine distributionLine)ParametersNameTypeDescriptiondistributionLineRfs

### operator string(RfsgSynchronizedScriptTriggerDistributionLine)

Converts the [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) object to equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator string(RfsgSynchronizedScriptTriggerDistributionLine distributionLine)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| distributionLine | RfsgSynchronizedScriptTriggerDistributionLine | Specifies the RfsgSynchronizedScriptTriggerDistributionLine object to be converted to string. |

#### Returns

Returns a string from the [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) object.

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-operator_eq__rfsgsynchronizedscripttriggerdistributionline-rfsgsynchronizedscripttriggerdistributionline.html language=enus -->
## TOPIC 00333: operator==(RfsgSynchronizedScriptTriggerDistributionLine, RfsgSynchronizedScriptTriggerDistributionLine)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-operator_eq__rfsgsynchronizedscripttriggerdistributionline-rfsgsynchronizedscripttriggerdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-operator_eq__rfsgsynchronizedscripttriggerdistributionline-rfsgsynchronizedscripttriggerdistributionline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgSynchronizedScriptTriggerDistributionLine are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgSynchronizedScriptTriggerDistributionLine distributionLine1, RfsgSynchronizedScriptTriggerDistributionLine dist

### operator==(RfsgSynchronizedScriptTriggerDistributionLine, RfsgSynchronizedScriptTriggerDistributionLine)

Checks whether the two instances of [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgSynchronizedScriptTriggerDistributionLine distributionLine1, RfsgSynchronizedScriptTriggerDistributionLine distributionLine2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| distributionLine1 | RfsgSynchronizedScriptTriggerDistributionLine | Specifies an RfsgSynchronizedScriptTriggerDistributionLine object. |
| distributionLine2 | RfsgSynchronizedScriptTriggerDistributionLine | Specifies an RfsgSynchronizedScriptTriggerDistributionLine object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline2.html language=enus -->
## TOPIC 00334: PxiTriggerLine2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external line when synchronized trigger is distributed to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSynchronizedScriptTriggerDistributionLine PxiTriggerLine2 { get; }RemarksReturns an object of type RfsgSynchronizedScriptTriggerD

### PxiTriggerLine2

Gets the external line when synchronized trigger is distributed to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) representing the string "PXI_Trig2".

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline4.html language=enus -->
## TOPIC 00335: PxiTriggerLine4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external line when synchronized trigger is distributed to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSynchronizedScriptTriggerDistributionLine PxiTriggerLine4 { get; }RemarksReturns an object of type RfsgSynchronizedScriptTriggerD

### PxiTriggerLine4

Gets the external line when synchronized trigger is distributed to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) representing the string "PXI_Trig4".

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline7.html language=enus -->
## TOPIC 00336: PxiTriggerLine7

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline-pxitriggerline7.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSynchronizedScriptTriggerDistributionLine PxiTriggerLine7 { get; }RemarksPxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSynchronizedScriptTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedscripttriggerdistributionline.html) PxiTriggerLine7 { get; }

#### Remarks

PxiTriggerLine7

Parent topic:

RfsgSynchronizedScriptTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttrigger-ismaster.html language=enus -->
## TOPIC 00337: IsMaster

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttrigger-ismaster.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttrigger-ismaster.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the device is the master device when synchronizing the Start trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool IsMaster { get; set; }Remarkstrue if the device is the master device when synchronizing the Start trigger; otherwise, false. The defaul

### IsMaster

Gets or sets whether the device is the master device when synchronizing the Start trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool IsMaster { get; set; }

#### Remarks

true if the device is the master device when synchronizing the Start trigger; otherwise, false. The default value is false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The IsMaster property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgSynchronizedStartTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline-equals__object.html language=enus -->
## TOPIC 00338: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgSynchronizedStartTriggerDistributionLine and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to compar

### Equals(object)

Determines whether the current instance of [RfsgSynchronizedStartTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to compared to the current instance of RfsgSynchronizedStartTriggerDistributionLine. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgSynchronizedStartTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline-pfi0.html language=enus -->
## TOPIC 00339: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external line when synchronized trigger is distributed to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgSynchronizedStartTriggerDistributionLine Pfi0 { get; }RemarksReturns an object of type RfsgSynchronizedStartTriggerDistributionLine

### Pfi0

Gets the external line when synchronized trigger is distributed to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgSynchronizedStartTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgSynchronizedStartTriggerDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgsynchronizedstarttriggerdistributionline.html) representing the string "PFI0".

Parent topic:

RfsgSynchronizedStartTriggerDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html language=enus -->
## TOPIC 00340: RfsgTriggerLevel Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active level for the Script trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgTriggerLevelMembersNameValueDescriptionActiveHigh(int)9000Trigger when the digital signal is high. ActiveLow(int)9001Trigger when the digital signal is low. See AlsoLevel

### RfsgTriggerLevel Enumeration

Specifies the active level for the Script trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgTriggerLevel

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | (int)9000 | Trigger when the digital signal is high. |
| ActiveLow | (int)9001 | Trigger when the digital signal is low. |

#### See Also

- Level

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-fromstring__string.html language=enus -->
## TOPIC 00341: FromString(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-fromstring__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsgTriggerSyncDistributionLine object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgTriggerSyncDistributionLine FromString(string distributionLine)ParametersNameTypeDescriptiondistributionLinestringSpecifies a string representi

### FromString(string)

Creates an [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) FromString(string distributionLine)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| distributionLine | string | Specifies a string representing the output terminal of RfsgScriptTrigger. |

#### Returns

Returns an object of type [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html).

Parent topic:

RfsgTriggerSyncDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-gethashcode.html language=enus -->
## TOPIC 00342: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgTriggerSyncDistributionLine. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgTriggerSyncDistributionLine.

### GetHashCode()

Returns the hash code for the current instance of [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html).

Parent topic:

RfsgTriggerSyncDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-operator_eq__rfsgtriggersyncdistributionline-rfsgtriggersyncdistributionline.html language=enus -->
## TOPIC 00343: operator==(RfsgTriggerSyncDistributionLine, RfsgTriggerSyncDistributionLine)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-operator_eq__rfsgtriggersyncdistributionline-rfsgtriggersyncdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-operator_eq__rfsgtriggersyncdistributionline-rfsgtriggersyncdistributionline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgTriggerSyncDistributionLine are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgTriggerSyncDistributionLine distributionLine1, RfsgTriggerSyncDistributionLine distributionLine2)ParametersNameTypeDescriptio

### operator==(RfsgTriggerSyncDistributionLine, RfsgTriggerSyncDistributionLine)

Checks whether the two instances of [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgTriggerSyncDistributionLine distributionLine1, RfsgTriggerSyncDistributionLine distributionLine2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| distributionLine1 | RfsgTriggerSyncDistributionLine | Specifies an RfsgTriggerSyncDistributionLine object. |
| distributionLine2 | RfsgTriggerSyncDistributionLine | Specifies an RfsgTriggerSyncDistributionLine object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgTriggerSyncDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-operator_neq__rfsgtriggersyncdistributionline-rfsgtriggersyncdistributionline.html language=enus -->
## TOPIC 00344: operator!=(RfsgTriggerSyncDistributionLine, RfsgTriggerSyncDistributionLine)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-operator_neq__rfsgtriggersyncdistributionline-rfsgtriggersyncdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-operator_neq__rfsgtriggersyncdistributionline-rfsgtriggersyncdistributionline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgTriggerSyncDistributionLine are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgTriggerSyncDistributionLine distributionLine1, RfsgTriggerSyncDistributionLine distributionLine2)ParametersNameTypeDescript

### operator!=(RfsgTriggerSyncDistributionLine, RfsgTriggerSyncDistributionLine)

Checks whether the two instances of [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgTriggerSyncDistributionLine distributionLine1, RfsgTriggerSyncDistributionLine distributionLine2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| distributionLine1 | RfsgTriggerSyncDistributionLine | Specifies an RfsgTriggerSyncDistributionLine object. |
| distributionLine2 | RfsgTriggerSyncDistributionLine | Specifies an RfsgTriggerSyncDistributionLine object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgTriggerSyncDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-pxitriggerline2.html language=enus -->
## TOPIC 00345: PxiTriggerLine2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-pxitriggerline2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external line when synchronized trigger is distributed to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgTriggerSyncDistributionLine PxiTriggerLine2 { get; }RemarksReturns an object of type RfsgTriggerSyncDistributionLine representing

### PxiTriggerLine2

Gets the external line when synchronized trigger is distributed to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) representing the string "PXI_Trig2".

Parent topic:

RfsgTriggerSyncDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-pxitriggerline5.html language=enus -->
## TOPIC 00346: PxiTriggerLine5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline-pxitriggerline5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external line when synchronized trigger is distributed to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgTriggerSyncDistributionLine PxiTriggerLine5 { get; }RemarksReturns an object of type RfsgTriggerSyncDistributionLine representing

### PxiTriggerLine5

Gets the external line when synchronized trigger is distributed to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [RfsgTriggerSyncDistributionLine](nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html) representing the string "PXI_Trig5".

Parent topic:

RfsgTriggerSyncDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html language=enus -->
## TOPIC 00347: RfsgTriggerSyncDistributionLine Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgtriggersyncdistributionline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the distribution line for synchronized start and script triggers. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgTriggerSyncDistributionLineRemarksSee NationalInstruments.ModularInstruments.NIRfsg.RfsgSyncStartTrigger.DistributionLine and Na

### RfsgTriggerSyncDistributionLine Class

Represents the distribution line for synchronized start and script triggers.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgTriggerSyncDistributionLine

#### Remarks

See NationalInstruments.ModularInstruments.NIRfsg.RfsgSyncStartTrigger.DistributionLine and NationalInstruments.ModularInstruments.NIRfsg.RfsgSyncScriptTrigger.DistributionLine.

#### Properties

| Name | Description |
| --- | --- |
| DoNotExport | Gets the external line when synchronized trigger is not distributed. |
| Pfi0 | Gets the external line when synchronized trigger is distributed to the PFI 0 connector. |
| PxiTriggerLine0 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the external line when synchronized trigger is distributed to the PXI trigger line 6. |
| PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgTriggerSyncDistributionLine object from the specified string. |
| Equals(RfsgTriggerSyncDistributionLine) | Determines whether the current instance of RfsgTriggerSyncDistributionLine and the RfsgTriggerSyncDistributionLine object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgTriggerSyncDistributionLine and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgTriggerSyncDistributionLine. |
| ToString() | Converts the current instance of RfsgTriggerSyncDistributionLine to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgTriggerSyncDistributionLine(string) | Convert the specified string to equivalent RfsgTriggerSyncDistributionLine object. |
| operator string(RfsgTriggerSyncDistributionLine) | Converts the RfsgTriggerSyncDistributionLine object to equivalent string. |
| operator!=(RfsgTriggerSyncDistributionLine, RfsgTriggerSyncDistributionLine) | Checks whether the two instances of RfsgTriggerSyncDistributionLine are unequal. |
| operator==(RfsgTriggerSyncDistributionLine, RfsgTriggerSyncDistributionLine) | Checks whether the two instances of RfsgTriggerSyncDistributionLine are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-cicfilteroverflowwarningcode.html language=enus -->
## TOPIC 00348: CicFilterOverflowWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-cicfilteroverflowwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-cicfilteroverflowwarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when overflow is detected in the Arb's CIC filter and output waveform was clipped. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid CicFilterOverflowWarningCode { get; }RemarksReturns the GUID ("163629A2-787A-4f6c-B03B-B44217855DE8") of the warni

### CicFilterOverflowWarningCode

Gets the warning code when overflow is detected in the Arb's CIC filter and output waveform was clipped.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid CicFilterOverflowWarningCode { get; }

#### Remarks

Returns the GUID ("163629A2-787A-4f6c-B03B-B44217855DE8") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-code.html language=enus -->
## TOPIC 00349: Code

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-code.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-code.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the error code that is assigned to the warning. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic Guid Code { get; private set; }RemarksReturns the GUID of the warning.

### Code

Gets the error code that is assigned to the warning.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public Guid Code { get; private set; }

#### Remarks

Returns the GUID of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-equals__object.html language=enus -->
## TOPIC 00350: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgWarning and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the current instance of

### Equals(object)

Determines whether the current instance of [RfsgWarning](nationalinstruments-modularinstruments-nirfsg-rfsgwarning.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsgWarning. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-firfilteroverflowwarningcode.html language=enus -->
## TOPIC 00351: FirFilterOverflowWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-firfilteroverflowwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-firfilteroverflowwarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when overflow is detected in the Arb's FIR Filter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid FirFilterOverflowWarningCode { get; }RemarksReturns the GUID ("6F1E35CD-7C30-40d8-96C0-465C31D0D07F") of the warning.

### FirFilterOverflowWarningCode

Gets the warning code when overflow is detected in the Arb's FIR Filter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid FirFilterOverflowWarningCode { get; }

#### Remarks

Returns the GUID ("6F1E35CD-7C30-40d8-96C0-465C31D0D07F") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-invalidwaveformfilepathwarningcode.html language=enus -->
## TOPIC 00352: InvalidWaveformFilepathWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-invalidwaveformfilepathwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-invalidwaveformfilepathwarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when the waveform filepath is invalid. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid InvalidWaveformFilepathWarningCode { get; }RemarksReturns the GUID ("7D02A2AF-A625-4971-A306-50FAD71069FD") of the warning.

### InvalidWaveformFilepathWarningCode

Gets the warning code when the waveform filepath is invalid.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid InvalidWaveformFilepathWarningCode { get; }

#### Remarks

Returns the GUID ("7D02A2AF-A625-4971-A306-50FAD71069FD") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-iqsumoverflowwarningcode.html language=enus -->
## TOPIC 00353: IQSumOverflowWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-iqsumoverflowwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-iqsumoverflowwarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when the Arb's OSP circuit detected an overflow due to an IQ pair with an absolute value greater than 1.0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid IQSumOverflowWarningCode { get; }RemarksReturns the GUID ("7D0975A4-C700-4676-95A6-D4EB27B

### IQSumOverflowWarningCode

Gets the warning code when the Arb's OSP circuit detected an overflow due to an IQ pair with an absolute value greater than 1.0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid IQSumOverflowWarningCode { get; }

#### Remarks

Returns the GUID ("7D0975A4-C700-4676-95A6-D4EB27BBA939") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-operator_eq__rfsgwarning-rfsgwarning.html language=enus -->
## TOPIC 00354: operator==(RfsgWarning, RfsgWarning)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-operator_eq__rfsgwarning-rfsgwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-operator_eq__rfsgwarning-rfsgwarning.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgWarning are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgWarning warning1, RfsgWarning warning2)ParametersNameTypeDescriptionwarning1RfsgWarningSpecifies an RfsgWarning object. warning2RfsgWarningSpecif

### operator==(RfsgWarning, RfsgWarning)

Checks whether the two instances of [RfsgWarning](nationalinstruments-modularinstruments-nirfsg-rfsgwarning.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgWarning warning1, RfsgWarning warning2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warning1 | RfsgWarning | Specifies an RfsgWarning object. |
| warning2 | RfsgWarning | Specifies an RfsgWarning object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-operator_neq__rfsgwarning-rfsgwarning.html language=enus -->
## TOPIC 00355: operator!=(RfsgWarning, RfsgWarning)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-operator_neq__rfsgwarning-rfsgwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-operator_neq__rfsgwarning-rfsgwarning.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgWarning are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgWarning warning1, RfsgWarning warning2)ParametersNameTypeDescriptionwarning1RfsgWarningSpecifies an RfsgWarning object. warning2RfsgWarningSpec

### operator!=(RfsgWarning, RfsgWarning)

Checks whether the two instances of [RfsgWarning](nationalinstruments-modularinstruments-nirfsg-rfsgwarning.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgWarning warning1, RfsgWarning warning2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warning1 | RfsgWarning | Specifies an RfsgWarning object. |
| warning2 | RfsgWarning | Specifies an RfsgWarning object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-poweroutofrangewarningcode.html language=enus -->
## TOPIC 00356: PowerOutOfRangeWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-poweroutofrangewarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-poweroutofrangewarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when attenuator hold is enabled, and the requested power level is out of range for the selected attenuator. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid PowerOutOfRangeWarningCode { get; }RemarksReturns the GUID ("8612FC3B-49BE-4066-902E-CB50

### PowerOutOfRangeWarningCode

Gets the warning code when attenuator hold is enabled, and the requested power level is out of range for the selected attenuator.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid PowerOutOfRangeWarningCode { get; }

#### Remarks

Returns the GUID ("8612FC3B-49BE-4066-902E-CB5009978E89") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-readanddownloadunsuccessfulwarningcode.html language=enus -->
## TOPIC 00357: ReadAndDownloadUnsuccessfulWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-readanddownloadunsuccessfulwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-readanddownloadunsuccessfulwarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when reading the waveforms from a TDMS file is unsuccessful. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid ReadAndDownloadUnsuccessfulWarningCode { get; }RemarksReturns the GUID ("A68AE13B-6DD6-4E69-A8ED-21F2C5ED2288") of the warning.

### ReadAndDownloadUnsuccessfulWarningCode

Gets the warning code when reading the waveforms from a TDMS file is unsuccessful.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid ReadAndDownloadUnsuccessfulWarningCode { get; }

#### Remarks

Returns the GUID ("A68AE13B-6DD6-4E69-A8ED-21F2C5ED2288") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarning-reversepowerprotectionwarningcode.html language=enus -->
## TOPIC 00358: ReversePowerProtectionWarningCode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarning-reversepowerprotectionwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarning-reversepowerprotectionwarningcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when the specified value is outside the valid range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static Guid ReversePowerProtectionWarningCode { get; }RemarksReturns the GUID ("DC21D531-7DFF-4cc2-A7A3-85AC08BF3E69") of the warning.

### ReversePowerProtectionWarningCode

Gets the warning code when the specified value is outside the valid range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static Guid ReversePowerProtectionWarningCode { get; }

#### Remarks

Returns the GUID ("DC21D531-7DFF-4cc2-A7A3-85AC08BF3E69") of the warning.

Parent topic:

RfsgWarning Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwarningeventargs.html language=enus -->
## TOPIC 00359: RfsgWarningEventArgs Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwarningeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwarningeventargs.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents properties under Warning Event Args. Derives fromEventArgsSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgWarningEventArgs : EventArgsRemarksContains the warning event args data. PropertiesNameDescriptionCodeGets Warning Event Args code. MessageGets Warning

### RfsgWarningEventArgs Class

Represents properties under Warning Event Args.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgWarningEventArgs : EventArgs

#### Remarks

Contains the warning event args data.

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets Warning Event Args code. |
| Message | Gets Warning Event Args message. |
| Warning | Gets or sets the warning set in the Warning Event Args. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html language=enus -->
## TOPIC 00360: RfsgWaveformGenerationMode Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies type of signal to generate, on calling the Initiate method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgWaveformGenerationModeMembersNameValueDescriptionContinuousWave(int)1000Configures the RF signal generator to generate a continuous wave (CW) signal. Ar

### RfsgWaveformGenerationMode Enumeration

Specifies type of signal to generate, on calling the [Initiate](nationalinstruments-modularinstruments-nirfsg-nirfsg-initiate.html) method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgWaveformGenerationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ContinuousWave | (int)1000 | Configures the RF signal generator to generate a continuous wave (CW) signal. |
| ArbitraryWaveform | (int)1001 | Configures the RF signal generator to generate the arbitrary waveform specified by the SelectedWaveform property. |
| Script | (int)1002 | Configures the RF signal generator to generate arbitrary waveforms as specified by the SelectedScriptName property. |

#### See Also

- GenerationMode

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg
