# NI DOCUMENT BUNDLE: ni-dcpower-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-csharp-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced-powersourceinuse.html language=enus -->
## TOPIC 00001: PowerSourceInUse

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced-powersourceinuse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced-powersourceinuse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the device is using the internal or auxiliary power source to generate power. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPowerSourceInUse PowerSourceInUse { get; }RemarksThis property is not supported in sessions initialized with the NIDCPower(string,

### PowerSourceInUse

Gets whether the device is using the internal or auxiliary power source to generate power.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPowerSourceInUse](nationalinstruments-modularinstruments-nidcpower-dcpowerpowersourceinuse.html) PowerSourceInUse { get; }

#### Remarks

Note

This property is not supported in sessions initialized with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor.

Returns an object of type [DCPowerPowerSourceInUse](nationalinstruments-modularinstruments-nidcpower-dcpowerpowersourceinuse.html).

Parent topic:

DCPowerAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowercalibration.html language=enus -->
## TOPIC 00002: DCPowerCalibration Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowercalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowercalibration.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides objects of specific types to calibrate NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerCalibration : DCPowerSubObjectRemarksExternal calibration is not supported for NI-DCPower. For more information, refer to NI DC

### DCPowerCalibration Class

Provides objects of specific types to calibrate NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerCalibration : DCPowerSubObject

#### Remarks

External calibration is not supported for NI-DCPower. For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| External | Gets the DCPowerExternalCalibration sub-object that provides properties and methods for external calibration. |
| Self | Gets the DCPowerSelfCalibration sub-object that provides properties and methods for self calibration. |
| Utility | Gets the DCPowerCalibrationUtility sub-object that provides utility calibration methods. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowercalibrationutility.html language=enus -->
## TOPIC 00003: DCPowerCalibrationUtility Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowercalibrationutility.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowercalibrationutility.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents NI-DCPower calibration utility. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerCalibrationUtility : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyAll members of this

### DCPowerCalibrationUtility Class

Represents NI-DCPower calibration utility.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerCalibrationUtility : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Methods

| Name | Description |
| --- | --- |
| ReadCurrentTemperature() | Returns the current onboard temperature, in degrees Celsius, of the device. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-abort.html language=enus -->
## TOPIC 00004: Abort()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-abort.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transitions the NI-DCPower session from the Running state to the Uncommitted state. If a sequence is running, then the NI-DCPower session is stopped. Any configuration methods called after this method are not applied until the Initiate method is called. If power output is enabled when you call the A

### Abort()

Transitions the NI-DCPower session from the Running state to the Uncommitted state. If a sequence is running, then the NI-DCPower session is stopped. Any configuration methods called after this method are not applied until the [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html) method is called. If power output is enabled when you call the Abort method, the channels remain in their current state and continue providing power. Use the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property to disable power output on a per channel basis. Use the [Reset](nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-reset.html) method to disable output on all channels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Abort()

#### Remarks

For information about the specific NI-DCPower software states, refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help*.

Parent topic:

DCPowerControl Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html language=enus -->
## TOPIC 00005: Initiate()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts generation or acquisition, causing the NI-DCPower session to leave the Uncommitted state or Committed state and enter the Running state. To return to the Uncommitted state call the Abort method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Initiate()RemarksFor

### Initiate()

Starts generation or acquisition, causing the NI-DCPower session to leave the Uncommitted state or Committed state and enter the Running state. To return to the Uncommitted state call the [Abort](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-abort.html) method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Initiate()

#### Remarks

For more information about the specific NI-DCPower software states, refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help*.

Parent topic:

DCPowerControl Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-equals__object.html language=enus -->
## TOPIC 00006: Equals(object)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-equals__object.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be

### Equals(object)

Determines whether the current instance of [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-gethashcode.html language=enus -->
## TOPIC 00007: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of DCPowerDigit

### GetHashCode()

Returns the hash code for the current instance of [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-operator-dcpowerdigitaledgemeasuretriggerinputterminal__string.html language=enus -->
## TOPIC 00008: operator DCPowerDigitalEdgeMeasureTriggerInputTerminal(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-operator-dcpowerdigitaledgemeasuretriggerinputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-operator-dcpowerdigitaledgemeasuretriggerinputterminal__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent DCPowerDigitalEdgeMeasureTriggerInputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator DCPowerDigitalEdgeMeasureTriggerInputTerminal(string inputTerminal)ParametersNameTypeDescriptioninput

### operator DCPowerDigitalEdgeMeasureTriggerInputTerminal(string)

Converts the specified string to the equivalent [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator DCPowerDigitalEdgeMeasureTriggerInputTerminal(string inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | string | Specifies the string to be converted to the equivalent DCPowerDigitalEdgeMeasureTriggerInputTerminal object. |

#### Returns

Returns an object of type [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) from the string passed in inputTerminal.

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-operator_neq__dcpowerdigitaledgemeasuretriggerinputterminal-dcpowerdigitaledgemeasuretriggerinputterminal.html language=enus -->
## TOPIC 00009: operator!=(DCPowerDigitalEdgeMeasureTriggerInputTerminal, DCPowerDigitalEdgeMeasureTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-operator_neq__dcpowerdigitaledgemeasuretriggerinputterminal-dcpowerdigitaledgemeasuretriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-operator_neq__dcpowerdigitaledgemeasuretriggerinputterminal-dcpowerdigitaledgemeasuretriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerDigitalEdgeMeasureTriggerInputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerDigitalEdgeMeasureTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeMeasureTriggerInputTerminal in

### operator!=(DCPowerDigitalEdgeMeasureTriggerInputTerminal, DCPowerDigitalEdgeMeasureTriggerInputTerminal)

Checks whether the two instances of [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerDigitalEdgeMeasureTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeMeasureTriggerInputTerminal inputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal1 | DCPowerDigitalEdgeMeasureTriggerInputTerminal | Specifies DCPowerDigitalEdgeMeasureTriggerInputTerminal object. |
| inputTerminal2 | DCPowerDigitalEdgeMeasureTriggerInputTerminal | Specifies DCPowerDigitalEdgeMeasureTriggerInputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00010: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeMeasureTriggerInputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerDigitalEdgeMeasureTriggerInput

### PxiTriggerLine0

Gets the input terminal when the signal is imported from the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00011: PxiTriggerLine5

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline5.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeMeasureTriggerInputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type DCPowerDigitalEdgeMeasureTriggerInput

### PxiTriggerLine5

Gets the input terminal when the signal is imported from the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) representing the string "PXI_Trig5".

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00012: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeMeasureTriggerInputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerDigitalEdgeMeasureTriggerInput

### PxiTriggerLine6

Gets the input terminal when the signal is imported from the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeMeasureTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html language=enus -->
## TOPIC 00013: DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the input terminal for DCPowerDigitalEdgeMeasureTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerDigitalEdgeMeasureTriggerInputTerminalRemarksSee InputTerminal. Thread SafetyAll members of this type are safe for multithreaded op

### DCPowerDigitalEdgeMeasureTriggerInputTerminal Class

Represents the input terminal for [DCPowerDigitalEdgeMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerDigitalEdgeMeasureTriggerInputTerminal

#### Remarks

See [InputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgemeasuretrigger-inputterminal.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| None | Gets the input terminal which specifies that no signal is imported. |
| PxiTriggerLine0 | Gets the input terminal when the signal is imported from the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the input terminal when the signal is imported from the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the input terminal when the signal is imported from the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the input terminal when the signal is imported from the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the input terminal when the signal is imported from the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the input terminal when the signal is imported from the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the input terminal when the signal is imported from the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the input terminal when the signal is imported from the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates a DCPowerDigitalEdgeMeasureTriggerInputTerminal object from the specified string. |
| Equals(DCPowerDigitalEdgeMeasureTriggerInputTerminal) | Determines whether the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal and the DCPowerDigitalEdgeMeasureTriggerInputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal. |
| ToString() | Converts the current instance of DCPowerDigitalEdgeMeasureTriggerInputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator DCPowerDigitalEdgeMeasureTriggerInputTerminal(string) | Converts the specified string to the equivalent DCPowerDigitalEdgeMeasureTriggerInputTerminal object. |
| operator string(DCPowerDigitalEdgeMeasureTriggerInputTerminal) | Converts the DCPowerDigitalEdgeMeasureTriggerInputTerminal object to the equivalent string. |
| operator!=(DCPowerDigitalEdgeMeasureTriggerInputTerminal, DCPowerDigitalEdgeMeasureTriggerInputTerminal) | Checks whether the two instances of DCPowerDigitalEdgeMeasureTriggerInputTerminal are unequal. |
| operator==(DCPowerDigitalEdgeMeasureTriggerInputTerminal, DCPowerDigitalEdgeMeasureTriggerInputTerminal) | Checks whether the two instances of DCPowerDigitalEdgeMeasureTriggerInputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetrigger-configure__dcpowerdigitaledgepulsetriggerinputterminal-dcpowertriggeredge.html language=enus -->
## TOPIC 00014: Configure(DCPowerDigitalEdgePulseTriggerInputTerminal, DCPowerTriggerEdge)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetrigger-configure__dcpowerdigitaledgepulsetriggerinputterminal-dcpowertriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetrigger-configure__dcpowerdigitaledgepulsetriggerinputterminal-dcpowertriggeredge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PulseTrigger for digital edge triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Configure(DCPowerDigitalEdgePulseTriggerInputTerminal inputTerminal, DCPowerTriggerEdge edge)ParametersNameTypeDescriptioninputTerminalDCPowerDigitalEdgePulseTriggerI

### Configure(DCPowerDigitalEdgePulseTriggerInputTerminal, DCPowerTriggerEdge)

Configures the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-pulsetrigger.html) for digital edge triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Configure(DCPowerDigitalEdgePulseTriggerInputTerminal inputTerminal, DCPowerTriggerEdge edge)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgePulseTriggerInputTerminal | Specifies the input terminal of the digital edge for the PulseTrigger. |
| edge | DCPowerTriggerEdge | Specifies whether to configure the PulseTrigger to assert on the rising or falling edge. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Configure method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgePulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetrigger-edge.html language=enus -->
## TOPIC 00015: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to configure the PulseTrigger to assert on the rising or falling edge. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksSpecifies the DCPowerTriggerEdge enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposed

### Edge

Gets or sets whether to configure the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-pulsetrigger.html) to assert on the rising or falling edge.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Edge property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgePulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-none.html language=enus -->
## TOPIC 00016: None

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-none.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal which specifies that no signal is imported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgePulseTriggerInputTerminal None { get; }RemarksReturns an object of type DCPowerDigitalEdgePulseTriggerInputTerminal representing an emp

### None

Gets the input terminal which specifies that no signal is imported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) None { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) representing an empty string.

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-operator-string__dcpowerdigitaledgepulsetriggerinputterminal.html language=enus -->
## TOPIC 00017: operator string(DCPowerDigitalEdgePulseTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-operator-string__dcpowerdigitaledgepulsetriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-operator-string__dcpowerdigitaledgepulsetriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the DCPowerDigitalEdgePulseTriggerInputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator string(DCPowerDigitalEdgePulseTriggerInputTerminal inputTerminal)ParametersNameTypeDescriptioninputTerminalDCPowe

### operator string(DCPowerDigitalEdgePulseTriggerInputTerminal)

Converts the [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator string(DCPowerDigitalEdgePulseTriggerInputTerminal inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgePulseTriggerInputTerminal | Specifies the DCPowerDigitalEdgePulseTriggerInputTerminal object to be converted to string. |

#### Returns

Returns a string from the [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) object.

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00018: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgePulseTriggerInputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerDigitalEdgePulseTriggerInputTerm

### PxiTriggerLine0

Gets the input terminal when the signal is imported from the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00019: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgePulseTriggerInputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerDigitalEdgePulseTriggerInputTerm

### PxiTriggerLine1

Gets the input terminal when the signal is imported from the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00020: PxiTriggerLine2

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline2.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgePulseTriggerInputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type DCPowerDigitalEdgePulseTriggerInputTerm

### PxiTriggerLine2

Gets the input terminal when the signal is imported from the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) representing the string "PXI_Trig2".

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00021: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgePulseTriggerInputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerDigitalEdgePulseTriggerInputTerm

### PxiTriggerLine7

Gets the input terminal when the signal is imported from the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-tostring.html language=enus -->
## TOPIC 00022: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerDigitalEdgePulseTriggerInputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a string that represents the current instance of DCPowerDigitalEdgePulseTriggerInputTerminal.

### ToString()

Converts the current instance of [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgePulseTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger-edge.html language=enus -->
## TOPIC 00023: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active edge for the Digital Edge SequenceAdvanceTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksSpecifies the DCPowerTriggerEdge enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Edge

### Edge

Gets or sets the active edge for the Digital Edge [SequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-sequenceadvancetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Edge property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger-inputterminal.html language=enus -->
## TOPIC 00024: InputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger-inputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the Digital Edge Sequence Advance trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal InputTerminal { get; set; }RemarksUse this property only when the DCPowerStartTriggerType prope

### InputTerminal

Gets or sets the input terminal for the Digital Edge Sequence Advance trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) InputTerminal { get; set; }

#### Remarks

Use this property only when the [DCPowerStartTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html) property is set to [DigitalEdge](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html).

Specifies the [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The InputTerminal property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger.html language=enus -->
## TOPIC 00025: DCPowerDigitalEdgeSequenceAdvanceTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure digital edge for the SequenceAdvanceTrigger. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerDigitalEdgeSequenceAdvanceTrigger : DCPowerSubObjectRemarksFor more information, refer

### DCPowerDigitalEdgeSequenceAdvanceTrigger Class

Represents the methods and properties used to configure digital edge for the [SequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-sequenceadvancetrigger.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerDigitalEdgeSequenceAdvanceTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets the active edge for the Digital Edge SequenceAdvanceTrigger. |
| InputTerminal | Gets or sets the input terminal for the Digital Edge Sequence Advance trigger. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal, DCPowerTriggerEdge) | Configures the SequenceAdvanceTrigger for digital edge triggering. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-equals__dcpowerdigitaledgesequenceadvancetriggerinputterminal.html language=enus -->
## TOPIC 00026: Equals(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-equals__dcpowerdigitaledgesequenceadvancetriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-equals__dcpowerdigitaledgesequenceadvancetriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal and the DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerDigitalEdgeSequ

### Equals(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal)

Determines whether the current instance of [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) and the [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal | Specifies the DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal object to be compared to the current instance of DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-operator_eq__dcpowerdigitaledgesequenceadvancetriggerinputterminal-dcpowerdigitale...d85e395.html language=enus -->
## TOPIC 00027: operator==(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal, DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-operator_eq__dcpowerdigitaledgesequenceadvancetriggerinputterminal-dcpowerdigitale...d85e395.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-operator_eq__dcpowerdigitaledgesequenceadvancetriggerinputterminal-dcpowerdigitale...d85e395.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeSequenceAdvanceT

### operator==(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal, DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal)

Checks whether the two instances of [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal1 | DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal | Specifies a DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal object. |
| inputTerminal2 | DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal | Specifies a DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-operator_neq__dcpowerdigitaledgesequenceadvancetriggerinputterminal-dcpowerdigital...d85e339.html language=enus -->
## TOPIC 00028: operator!=(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal, DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-operator_neq__dcpowerdigitaledgesequenceadvancetriggerinputterminal-dcpowerdigital...d85e339.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-operator_neq__dcpowerdigitaledgesequenceadvancetriggerinputterminal-dcpowerdigital...d85e339.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeSequenceAdvanc

### operator!=(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal, DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal)

Checks whether the two instances of [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal inputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal1 | DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal | Specifies DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal object. |
| inputTerminal2 | DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal | Specifies DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00029: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSequenceAdv

### PxiTriggerLine0

Gets the input terminal when the signal is imported from the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00030: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSequenceAdv

### PxiTriggerLine1

Gets the input terminal when the signal is imported from the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00031: PxiTriggerLine2

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline2.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSequenceAdv

### PxiTriggerLine2

Gets the input terminal when the signal is imported from the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) representing the string "PXI_Trig2".

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00032: PxiTriggerLine4

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline4.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSequenceAdv

### PxiTriggerLine4

Gets the input terminal when the signal is imported from the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) representing the string "PXI_Trig4".

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00033: PxiTriggerLine5

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline5.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSequenceAdv

### PxiTriggerLine5

Gets the input terminal when the signal is imported from the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) representing the string "PXI_Trig5".

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00034: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSequenceAdv

### PxiTriggerLine7

Gets the input terminal when the signal is imported from the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-tostring.html language=enus -->
## TOPIC 00035: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a String that represents the current instance of DCPowerDigitalEdgeSequenceAdvanceTrigg

### ToString()

Converts the current instance of [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a String that represents the current instance of [DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesequenceadvancetriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-fromstring__string.html language=enus -->
## TOPIC 00036: FromString(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-fromstring__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DCPowerDigitalEdgeShutdownTriggerInputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeShutdownTriggerInputTerminal FromString(string inputTerminal)ParametersNameTypeDescriptioninputTerminalstringSpe

### FromString(string)

Creates a [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) FromString(string inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | string | Specifies a string that is the input terminal of DCPowerOutputDigitalEdgeShutdownTrigger |

#### Returns

Returns an object of type [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-none.html language=enus -->
## TOPIC 00037: None

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-none.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal which specifies that no signal is imported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeShutdownTriggerInputTerminal None { get; }RemarksReturns an object of type DCPowerDigitalEdgeShutdownTriggerInputTerminal representing

### None

Gets the input terminal which specifies that no signal is imported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) None { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) representing an empty string.

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-operator_eq__dcpowerdigitaledgeshutdowntriggerinputterminal-dcpowerdigitaledgeshutdowntri...d104e395.html language=enus -->
## TOPIC 00038: operator==(DCPowerDigitalEdgeShutdownTriggerInputTerminal, DCPowerDigitalEdgeShutdownTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-operator_eq__dcpowerdigitaledgeshutdowntriggerinputterminal-dcpowerdigitaledgeshutdowntri...d104e395.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-operator_eq__dcpowerdigitaledgeshutdowntriggerinputterminal-dcpowerdigitaledgeshutdowntri...d104e395.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerDigitalEdgeShutdownTriggerInputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerDigitalEdgeShutdownTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeShutdownTriggerInputTerminal i

### operator==(DCPowerDigitalEdgeShutdownTriggerInputTerminal, DCPowerDigitalEdgeShutdownTriggerInputTerminal)

Checks whether the two instances of [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerDigitalEdgeShutdownTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeShutdownTriggerInputTerminal inputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal1 | DCPowerDigitalEdgeShutdownTriggerInputTerminal | Specifies a DCPowerDigitalEdgeShutdownTriggerInputTerminal object. |
| inputTerminal2 | DCPowerDigitalEdgeShutdownTriggerInputTerminal | Specifies a DCPowerDigitalEdgeShutdownTriggerInputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-operator_neq__dcpowerdigitaledgeshutdowntriggerinputterminal-dcpowerdigitaledgeshutdowntr...d104e339.html language=enus -->
## TOPIC 00039: operator!=(DCPowerDigitalEdgeShutdownTriggerInputTerminal, DCPowerDigitalEdgeShutdownTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-operator_neq__dcpowerdigitaledgeshutdowntriggerinputterminal-dcpowerdigitaledgeshutdowntr...d104e339.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-operator_neq__dcpowerdigitaledgeshutdowntriggerinputterminal-dcpowerdigitaledgeshutdowntr...d104e339.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerDigitalEdgeShutdownTriggerInputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerDigitalEdgeShutdownTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeShutdownTriggerInputTerminal

### operator!=(DCPowerDigitalEdgeShutdownTriggerInputTerminal, DCPowerDigitalEdgeShutdownTriggerInputTerminal)

Checks whether the two instances of [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerDigitalEdgeShutdownTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeShutdownTriggerInputTerminal inputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal1 | DCPowerDigitalEdgeShutdownTriggerInputTerminal | Specifies DCPowerDigitalEdgeShutdownTriggerInputTerminal object. |
| inputTerminal2 | DCPowerDigitalEdgeShutdownTriggerInputTerminal | Specifies DCPowerDigitalEdgeShutdownTriggerInputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00040: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeShutdownTriggerInputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerDigitalEdgeShutdownTriggerInp

### PxiTriggerLine0

Gets the input terminal when the signal is imported from the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00041: PxiTriggerLine2

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline2.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeShutdownTriggerInputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type DCPowerDigitalEdgeShutdownTriggerInp

### PxiTriggerLine2

Gets the input terminal when the signal is imported from the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) representing the string "PXI_Trig2".

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00042: PxiTriggerLine3

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline3.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeShutdownTriggerInputTerminal PxiTriggerLine3 { get; }RemarksReturns an object of type DCPowerDigitalEdgeShutdownTriggerInp

### PxiTriggerLine3

Gets the input terminal when the signal is imported from the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) representing the string "PXI_Trig3".

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00043: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeShutdownTriggerInputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerDigitalEdgeShutdownTriggerInp

### PxiTriggerLine7

Gets the input terminal when the signal is imported from the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-tostring.html language=enus -->
## TOPIC 00044: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerDigitalEdgeShutdownTriggerInputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a string that represents the current instance of DCPowerDigitalEdgeShutdownTriggerInputTermina

### ToString()

Converts the current instance of [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeShutdownTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger-edge.html language=enus -->
## TOPIC 00045: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active edge for the DCPowerDigitalEdgeSourceTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksSpecifies the DCPowerTriggerEdge enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Edge prop

### Edge

Gets or sets the active edge for the [DCPowerDigitalEdgeSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Edge property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgeSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger-inputterminal.html language=enus -->
## TOPIC 00046: InputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger-inputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the DCPowerDigitalEdgeSourceTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerDigitalEdgeSourceTriggerInputTerminal InputTerminal { get; set; }RemarksUse this property only when the Type property is set to DigitalEdge. Specifi

### InputTerminal

Gets or sets the input terminal for the [DCPowerDigitalEdgeSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) InputTerminal { get; set; }

#### Remarks

Use this property only when the [Type](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetrigger-type.html) property is set to [DigitalEdge](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggertype.html).

Specifies the [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The InputTerminal property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgeSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger.html language=enus -->
## TOPIC 00047: DCPowerDigitalEdgeSourceTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure DCPowerDigitalEdgeSourceTrigger. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerDigitalEdgeSourceTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs

### DCPowerDigitalEdgeSourceTrigger Class

Represents the properties used to configure DCPowerDigitalEdgeSourceTrigger.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerDigitalEdgeSourceTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets the active edge for the DCPowerDigitalEdgeSourceTrigger. |
| InputTerminal | Gets or sets the input terminal for the DCPowerDigitalEdgeSourceTrigger. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(DCPowerDigitalEdgeSourceTriggerInputTerminal, DCPowerTriggerEdge) | Configures the SourceTrigger for digital edge triggering. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-equals__dcpowerdigitaledgesourcetriggerinputterminal.html language=enus -->
## TOPIC 00048: Equals(DCPowerDigitalEdgeSourceTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-equals__dcpowerdigitaledgesourcetriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-equals__dcpowerdigitaledgesourcetriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerDigitalEdgeSourceTriggerInputTerminal and the DCPowerDigitalEdgeSourceTriggerInputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerDigitalEdgeSourceTriggerInputTerm

### Equals(DCPowerDigitalEdgeSourceTriggerInputTerminal)

Determines whether the current instance of [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) and the [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerDigitalEdgeSourceTriggerInputTerminal inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgeSourceTriggerInputTerminal | Specifies the DCPowerDigitalEdgeSourceTriggerInputTerminal object to be compared to the current instance of DCPowerDigitalEdgeSourceTriggerInputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeSourceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-operator-string__dcpowerdigitaledgesourcetriggerinputterminal.html language=enus -->
## TOPIC 00049: operator string(DCPowerDigitalEdgeSourceTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-operator-string__dcpowerdigitaledgesourcetriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-operator-string__dcpowerdigitaledgesourcetriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the DCPowerDigitalEdgeSourceTriggerInputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator string(DCPowerDigitalEdgeSourceTriggerInputTerminal inputTerminal)ParametersNameTypeDescriptioninputTerminalDCPo

### operator string(DCPowerDigitalEdgeSourceTriggerInputTerminal)

Converts the [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator string(DCPowerDigitalEdgeSourceTriggerInputTerminal inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgeSourceTriggerInputTerminal | Specifies the DCPowerDigitalEdgeSourceTriggerInputTerminal object to be converted to string. |

#### Returns

Returns a String from the [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) object.

Parent topic:

DCPowerDigitalEdgeSourceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00050: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is imported from the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSourceTriggerInputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSourceTriggerI

### PxiTriggerLine0

Gets the destination terminal when the signal is imported from the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerDigitalEdgeSourceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00051: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is imported from the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSourceTriggerInputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSourceTriggerI

### PxiTriggerLine1

Gets the destination terminal when the signal is imported from the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerDigitalEdgeSourceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00052: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is imported from the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeSourceTriggerInputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerDigitalEdgeSourceTriggerI

### PxiTriggerLine6

Gets the destination terminal when the signal is imported from the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeSourceTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgesourcetriggerinputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerDigitalEdgeSourceTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger-edge.html language=enus -->
## TOPIC 00053: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active edge for the DCPowerDigitalEdgeStartTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksSpecifies the DCPowerTriggerEdge enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Edge prope

### Edge

Gets or sets the active edge for the [DCPowerDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Edge property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger.html language=enus -->
## TOPIC 00054: DCPowerDigitalEdgeStartTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure DCPowerDigitalEdgeStartTrigger. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerDigitalEdgeStartTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs H

### DCPowerDigitalEdgeStartTrigger Class

Represents the properties used to configure DCPowerDigitalEdgeStartTrigger.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerDigitalEdgeStartTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets the active edge for the DCPowerDigitalEdgeStartTrigger. |
| InputTerminal | Gets or sets the input terminal for the DCPowerDigitalEdgeStartTrigger. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(DCPowerDigitalEdgeStartTriggerInputTerminal, DCPowerTriggerEdge) | Configures the StartTrigger for digital edge triggering. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-equals__dcpowerdigitaledgestarttriggerinputterminal.html language=enus -->
## TOPIC 00055: Equals(DCPowerDigitalEdgeStartTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-equals__dcpowerdigitaledgestarttriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-equals__dcpowerdigitaledgestarttriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal and the DCPowerDigitalEdgeStartTriggerInputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerDigitalEdgeStartTriggerInputTermina

### Equals(DCPowerDigitalEdgeStartTriggerInputTerminal)

Determines whether the current instance of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) and the [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerDigitalEdgeStartTriggerInputTerminal inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgeStartTriggerInputTerminal | Specifies the DCPowerDigitalEdgeStartTriggerInputTerminal object to be compared to the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-equals__object.html language=enus -->
## TOPIC 00056: Equals(object)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-equals__object.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be c

### Equals(object)

Determines whether the current instance of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-fromstring__string.html language=enus -->
## TOPIC 00057: FromString(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-fromstring__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an DCPowerDigitalEdgeStartTriggerInputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeStartTriggerInputTerminal FromString(string inputTerminal)ParametersNameTypeDescriptioninputTerminalstringSpecifie

### FromString(string)

Creates an [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) FromString(string inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | string | Specifies a string that is the input terminal of DCPowerDigitalEdgeStartTrigger. |

#### Returns

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-gethashcode.html language=enus -->
## TOPIC 00058: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of DCPowerDigital

### GetHashCode()

Returns the hash code for the current instance of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-none.html language=enus -->
## TOPIC 00059: None

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-none.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal which specifies that no signal is imported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeStartTriggerInputTerminal None { get; }RemarksReturns an object of type DCPowerDigitalEdgeStartTriggerInputTerminal representing an emp

### None

Gets the input terminal which specifies that no signal is imported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) None { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) representing an empty string.

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-operator-dcpowerdigitaledgestarttriggerinputterminal__string.html language=enus -->
## TOPIC 00060: operator DCPowerDigitalEdgeStartTriggerInputTerminal(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-operator-dcpowerdigitaledgestarttriggerinputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-operator-dcpowerdigitaledgestarttriggerinputterminal__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent DCPowerDigitalEdgeStartTriggerInputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator DCPowerDigitalEdgeStartTriggerInputTerminal(string inputTerminal)ParametersNameTypeDescriptioninputTerm

### operator DCPowerDigitalEdgeStartTriggerInputTerminal(string)

Converts the specified string to the equivalent [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator DCPowerDigitalEdgeStartTriggerInputTerminal(string inputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | string | Specifies the string to be converted to the equivalent DCPowerDigitalEdgeStartTriggerInputTerminal object. |

#### Returns

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) from the string passed in *inputTerminal*.

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-operator_eq__dcpowerdigitaledgestarttriggerinputterminal-dcpowerdigitaledgestarttriggerinputterminal.html language=enus -->
## TOPIC 00061: operator==(DCPowerDigitalEdgeStartTriggerInputTerminal, DCPowerDigitalEdgeStartTriggerInputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-operator_eq__dcpowerdigitaledgestarttriggerinputterminal-dcpowerdigitaledgestarttriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-operator_eq__dcpowerdigitaledgestarttriggerinputterminal-dcpowerdigitaledgestarttriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerDigitalEdgeStartTriggerInputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerDigitalEdgeStartTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeStartTriggerInputTerminal inputTermi

### operator==(DCPowerDigitalEdgeStartTriggerInputTerminal, DCPowerDigitalEdgeStartTriggerInputTerminal)

Checks whether the two instances of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerDigitalEdgeStartTriggerInputTerminal inputTerminal1, DCPowerDigitalEdgeStartTriggerInputTerminal inputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal1 | DCPowerDigitalEdgeStartTriggerInputTerminal | Specifies a DCPowerDigitalEdgeStartTriggerInputTerminal object. |
| inputTerminal2 | DCPowerDigitalEdgeStartTriggerInputTerminal | Specifies a DCPowerDigitalEdgeStartTriggerInputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00062: PxiTriggerLine3

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline3.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeStartTriggerInputTerminal PxiTriggerLine3 { get; }RemarksReturns an object of type DCPowerDigitalEdgeStartTriggerInputTerm

### PxiTriggerLine3

Gets the input terminal when the signal is imported from the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) representing the string "PXI_Trig3".

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00063: PxiTriggerLine4

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline4.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeStartTriggerInputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type DCPowerDigitalEdgeStartTriggerInputTerm

### PxiTriggerLine4

Gets the input terminal when the signal is imported from the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) representing the string "PXI_Trig4".

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00064: PxiTriggerLine5

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline5.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeStartTriggerInputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type DCPowerDigitalEdgeStartTriggerInputTerm

### PxiTriggerLine5

Gets the input terminal when the signal is imported from the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) representing the string "PXI_Trig5".

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00065: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input terminal when the signal is imported from the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerDigitalEdgeStartTriggerInputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerDigitalEdgeStartTriggerInputTerm

### PxiTriggerLine6

Gets the input terminal when the signal is imported from the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-tostring.html language=enus -->
## TOPIC 00066: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a String that represents the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal.

### ToString()

Converts the current instance of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a String that represents the current instance of [DCPowerDigitalEdgeStartTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html).

Parent topic:

DCPowerDigitalEdgeStartTriggerInputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html language=enus -->
## TOPIC 00067: DCPowerDigitalEdgeStartTriggerInputTerminal Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttriggerinputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the input terminal for DCPowerDigitalEdgeStartTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerDigitalEdgeStartTriggerInputTerminalRemarksSee InputTerminal. Thread SafetyAll members of this type are safe for multithreaded operat

### DCPowerDigitalEdgeStartTriggerInputTerminal Class

Represents the input terminal for [DCPowerDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerDigitalEdgeStartTriggerInputTerminal

#### Remarks

See [InputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgestarttrigger-inputterminal.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| None | Gets the input terminal which specifies that no signal is imported. |
| PxiTriggerLine0 | Gets the input terminal when the signal is imported from the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the input terminal when the signal is imported from the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the input terminal when the signal is imported from the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the input terminal when the signal is imported from the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the input terminal when the signal is imported from the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the input terminal when the signal is imported from the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the input terminal when the signal is imported from the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the input terminal when the signal is imported from the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an DCPowerDigitalEdgeStartTriggerInputTerminal object from the specified string. |
| Equals(DCPowerDigitalEdgeStartTriggerInputTerminal) | Determines whether the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal and the DCPowerDigitalEdgeStartTriggerInputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal. |
| ToString() | Converts the current instance of DCPowerDigitalEdgeStartTriggerInputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator DCPowerDigitalEdgeStartTriggerInputTerminal(string) | Converts the specified string to the equivalent DCPowerDigitalEdgeStartTriggerInputTerminal object. |
| operator string(DCPowerDigitalEdgeStartTriggerInputTerminal) | Converts the DCPowerDigitalEdgeStartTriggerInputTerminal object to the equivalent string. |
| operator!=(DCPowerDigitalEdgeStartTriggerInputTerminal, DCPowerDigitalEdgeStartTriggerInputTerminal) | Checks whether the two instances of DCPowerDigitalEdgeStartTriggerInputTerminal are unequal. |
| operator==(DCPowerDigitalEdgeStartTriggerInputTerminal, DCPowerDigitalEdgeStartTriggerInputTerminal) | Checks whether the two instances of DCPowerDigitalEdgeStartTriggerInputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-description.html language=enus -->
## TOPIC 00068: Description

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-description.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string that contains a brief description of NI-DCPower driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string Description { get; }RemarksReturns a String that contains a brief description about NI-DCPower driver. ExceptionsTypeDescriptionSystem.ObjectDisposedEx

### Description

Gets a string that contains a brief description of NI-DCPower driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string Description { get; }

#### Remarks

Returns a String that contains a brief description about NI-DCPower driver.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Description property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverIdentity Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-serialnumber.html language=enus -->
## TOPIC 00069: SerialNumber

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-serialnumber.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the serial number of the NI-DCPower device currently in use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string SerialNumber { get; }RemarksReturns a String that contains the serial number of the NI-DCPower device currently in use. ExceptionsTypeDescriptionSystem.Obj

### SerialNumber

Gets the serial number of the NI-DCPower device currently in use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string SerialNumber { get; }

#### Remarks

Returns a String that contains the serial number of the NI-DCPower device currently in use.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SerialNumber property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverIdentity Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-specificationminorversion.html language=enus -->
## TOPIC 00070: SpecificationMinorVersion

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-specificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveridentity-specificationminorversion.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a integer that specifies the minor version number of the class specification in accordance with which the NI-DCPower .NET assembly was developed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic int SpecificationMinorVersion { get; }RemarksReturns a Int32 that contains th

### SpecificationMinorVersion

Gets a integer that specifies the minor version number of the class specification in accordance with which the NI-DCPower .NET assembly was developed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public int SpecificationMinorVersion { get; }

#### Remarks

Returns a Int32 that contains the minor version number of the NI-DCPower .NET assembly.

Parent topic:

DCPowerDriverIdentity Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriverlock-unlock.html language=enus -->
## TOPIC 00071: Unlock()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriverlock-unlock.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriverlock-unlock.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases a driver synchronization lock. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Unlock()

### Unlock()

Releases a driver synchronization lock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Unlock()

Parent topic:

DCPowerDriverLock Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-dispose.html language=enus -->
## TOPIC 00072: Dispose()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-dispose.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified session and deallocates the reserved resources, if not already disposed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Dispose()RemarksYou can call this method safely more than once, even if the session is already closed. A call to this method disp

### Dispose()

Closes the specified session and deallocates the reserved resources, if not already disposed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Dispose()

#### Remarks

You can call this method safely more than once, even if the session is already closed.

A call to this method disposes the **SafeHandle** class used to hold the instrument handle. If the call to this method fails due to some reason, like the session being closed by some external means, you will not be notified about the failure. To help you identify failures in the **ReleaseHandle** method of the **SafeHandle** class, managed debugging assistant (MDA) is activated.

For details refer to [. The call to this method fails when you externally close a session by: Initializing a session with a resource name for which the session is already open, within the same process. This causes the instrument handle held by the existing session to become invalid. Getting the instrument handle out using the method and closing this handle directly.](http://msdn.microsoft.com/en-us/library/85eak4a0.aspx)

Parent topic:

DCPowerDriverOperation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-ioresourcedescriptor.html language=enus -->
## TOPIC 00073: IOResourceDescriptor

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-ioresourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-ioresourcedescriptor.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resource name that the NI-DCPower uses to identify the resource(s) used by the NI-DCPower session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string IOResourceDescriptor { get; }RemarksReturns a String representing the resource descriptor that the user specified

### IOResourceDescriptor

Gets the resource name that the NI-DCPower uses to identify the resource(s) used by the NI-DCPower session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string IOResourceDescriptor { get; }

#### Remarks

Returns a String representing the resource descriptor that the user specified for the physical device.

The resource name specified with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor can include instrument(s) and/or channel(s) but does not support logical names.

If you initialize NI-DCPower with a logical name using a deprecated [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor, this property contains the resource name that corresponds to the entry in the IVI configuration utility. If you initialize NI-DCPower with the resource name, this property contains that value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The IOResourceDescriptor property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverOperation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-recordcoercions.html language=enus -->
## TOPIC 00074: RecordCoercions

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-recordcoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-recordcoercions.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool RecordCoercions { get; set; }Remarkstrue if the IVI engine keeps a list of the value coercions; otherwis

### RecordCoercions

Gets or sets whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool RecordCoercions { get; set; }

#### Remarks

true if the IVI engine keeps a list of the value coercions; otherwise, false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The RecordCoercions property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverOperation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-simulate.html language=enus -->
## TOPIC 00075: Simulate

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriveroperation-simulate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether or not to simulate NI-DCPower I/O operations. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Simulate { get; set; }Remarkstrue if NI-DCPower simulates instrument driver I/O operations; false if NI-DCPower communicates directly with the instrument. This prop

### Simulate

Gets whether or not to simulate NI-DCPower I/O operations.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Simulate { get; set; }

#### Remarks

true if NI-DCPower simulates instrument driver I/O operations; false if NI-DCPower communicates directly with the instrument.

This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Simulate property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverOperation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-exportattributeconfigurationbuffer.html language=enus -->
## TOPIC 00076: ExportAttributeConfigurationBuffer()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-exportattributeconfigurationbuffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-exportattributeconfigurationbuffer.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to a System.Byte array buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic byte[] ExportAttributeConfigurationBuffer()RemarksYou can export and import supported configurations only between NI-DCPower devices with identical model numbers and

### ExportAttributeConfigurationBuffer()

Exports a session configuration to a System.Byte array buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public byte[] ExportAttributeConfigurationBuffer()

#### Remarks

You can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same number of initialized channels.

This method verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI-DCPower returns an Ivi.Driver.IviCDriverException.

**Supported Configurations**

- Attribute configurations
- Advanced sequences

**Support for this Method**

You must set the source mode to Sequence in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the independent channel [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor cannot be imported into sessions created with deprecated [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructors.

Note

Exporting and importing simple sequences between sessions in Sequence source mode is unsupported.

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order you specify in the resourceName input to the independent channel [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor.

Refer to *Import/Export Attribute Configuration Mapping Behavior* in the *NI DC Power Supplies and SMUs Help* for details.

#### Returns

Returns a System.Byte array that contains the exported configuration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportAttributeConfigurationBuffer method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerDriverUtility Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-getchannelnamefromstring__string.html language=enus -->
## TOPIC 00077: GetChannelNameFromString(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-getchannelnamefromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-getchannelnamefromstring__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated list of channel names from a string index list. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string GetChannelNameFromString(string index)ParametersNameTypeDescriptionindexstringSpecifies an index list for the channels in the session. Valid values

### GetChannelNameFromString(string)

Returns a comma-separated list of channel names from a string index list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string GetChannelNameFromString(string index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | string | Specifies an index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats: a comma-separated list ("0,2,3,1"); a range using a hyphen ("0-3"); or a range using a colon ("0:3"). You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indicies are supported ("2,3,0", "1,2,2,3"). Whitespace characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing. |

#### Returns

Returns a System.String of the channel name(s) in the same order the indices appear in the input string.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetChannelNameFromString method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OutOfRangeException | If one of the indices in the list is greater than or equal to the number of channels in the session. |
| Ivi.Driver.SelectorNameException | If the input list does not have a valid format or contains a negative index. |
| Ivi.Driver.IviCDriverException | If the input list is empty. |

Parent topic:

DCPowerDriverUtility Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-importattributeconfigurationbuffer__byte_arr1.html language=enus -->
## TOPIC 00078: ImportAttributeConfigurationBuffer(byte[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-importattributeconfigurationbuffer__byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-importattributeconfigurationbuffer__byte_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ImportAttributeConfigurationBuffer(byte[] configuration)RemarksYou can export and import supported configurations only between NI-DCPower devices with identi

### ImportAttributeConfigurationBuffer(byte[])

Imports a *configuration*  to the session from the specified buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ImportAttributeConfigurationBuffer(byte[] configuration)

#### Remarks

Note

You cannot call this method while the session is in the [Running](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) state.

**Supported Configurations**

- Attribute configurations
- Advanced sequences

**Support for this Method**

You must set the source mode to Sequence in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the independent channel [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor cannot be imported into sessions created with deprecated [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructors.

Note

Exporting and importing simple sequences between sessions in Sequence source mode is unsupported.

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order you specify in the resourceName input to the independent channel [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor.

Refer to *Import/Export Attribute Configuration Mapping Behavior* in the *NI DC Power Supplies and SMUs Help* for details.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configuration | byte[] | The System.Byte array that contains the configuration to import. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The method was called with a null configuration array. |
| System.ObjectDisposedException | The ImportAttributeConfigurationBuffer method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerDriverUtility Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-resetdevice.html language=enus -->
## TOPIC 00079: ResetDevice()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-resetdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-resetdevice.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all instruments in the session to a known state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ResetDevice()RemarksThe method disables power generation, resets all properties for all instruments included in the session to their default values, clears errors such

### ResetDevice()

Resets all instruments in the session to a known state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ResetDevice()

#### Remarks

The method disables power generation, resets all properties for all instruments included in the session to their default values, clears errors such as overtemperature and unexpected loss of auxiliary power, commits the instrument properties, and leaves the instrument(s) in the Uncommitted state. This method also performs a hard reset on the instrument(s) and driver software. This method has the same functionality as using reset in Measurement and Automation Explorer.

This method opens the output relay on instruments that have an output relay.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ResetDevice method was called after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverUtility Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-selftest.html language=enus -->
## TOPIC 00080: SelfTest()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-selftest.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-selftest.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the instrument self-test routine and returns the test result(s). Calling this method implicitly calls the Reset method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSelfTestResult SelfTest()RemarksWhen calling this method with the PXIe-4162/4163, specify al

### SelfTest()

Performs the instrument self-test routine and returns the test result(s). Calling this method implicitly calls the [Reset](nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-reset.html) method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSelfTestResult](nationalinstruments-modularinstruments-nidcpower-dcpowerselftestresult.html) SelfTest()

#### Remarks

When calling this method with the PXIe-4162/4163, specify all channels of your PXIe-4162/4163 with the resourceName input of the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. You cannot self test a subset of PXIe-4162/4163 channels.

#### Returns

Returns an object of type Ivi.Driver.SelfTestResult.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SelfTest method was called after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerDriverUtility Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerevents-pulsecompleteevent.html language=enus -->
## TOPIC 00081: PulseCompleteEvent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerevents-pulsecompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerevents-pulsecompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerPulseCompleteEvent sub-object that is used to configure the Pulse Complete event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulseCompleteEvent PulseCompleteEvent { get; }RemarksReturns an object of type DCPowerPulseCompleteEvent.

### PulseCompleteEvent

Gets the [DCPowerPulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteevent.html) sub-object that is used to configure the Pulse Complete event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteevent.html) PulseCompleteEvent { get; }

#### Remarks

Returns an object of type [DCPowerPulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteevent.html).

Parent topic:

DCPowerEvents Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sequenceiterationcompleteevent.html language=enus -->
## TOPIC 00082: SequenceIterationCompleteEvent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sequenceiterationcompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sequenceiterationcompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerSequenceIterationCompleteEvent sub-object that is used to configure the Sequence Iteration Complete event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSequenceIterationCompleteEvent SequenceIterationCompleteEvent { get; }RemarksReturns an object of

### SequenceIterationCompleteEvent

Gets the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html) sub-object that is used to configure the Sequence Iteration Complete event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html) SequenceIterationCompleteEvent { get; }

#### Remarks

Returns an object of type [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html).

Parent topic:

DCPowerEvents Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sourcecompleteevent.html language=enus -->
## TOPIC 00083: SourceCompleteEvent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sourcecompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sourcecompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerSourceCompleteEvent sub-object that is used to configure the Source Complete event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceCompleteEvent SourceCompleteEvent { get; }RemarksReturns an object of type DCPowerSourceCompleteEvent.

### SourceCompleteEvent

Gets the [DCPowerSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent.html) sub-object that is used to configure the Source Complete event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent.html) SourceCompleteEvent { get; }

#### Remarks

Returns an object of type [DCPowerSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent.html).

Parent topic:

DCPowerEvents Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerexternalcalibration-calibrationuserdefinedinfo.html language=enus -->
## TOPIC 00084: CalibrationUserDefinedInfo

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerexternalcalibration-calibrationuserdefinedinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerexternalcalibration-calibrationuserdefinedinfo.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the user-defined information in the instrument onboard EEPROM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string CalibrationUserDefinedInfo { get; set; }RemarksSetting this property overwrites any existing user-defined information.This property can only be u

### CalibrationUserDefinedInfo

Gets or sets the user-defined information in the instrument onboard EEPROM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string CalibrationUserDefinedInfo { get; set; }

#### Remarks

Setting this property overwrites any existing user-defined information.

Note

This property can only be used in a session initialized to a single instrument.

Returns a String representing the information stored in the instrument onboard EEPROM.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CalibrationUserDefinedInfo property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerExternalCalibration Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerexternalcalibration-calibrationuserdefinedinfomaxsize.html language=enus -->
## TOPIC 00085: CalibrationUserDefinedInfoMaxSize

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerexternalcalibration-calibrationuserdefinedinfomaxsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerexternalcalibration-calibrationuserdefinedinfomaxsize.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of characters that can be used to store user-defined information in the instrument onboard EEPROM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic int CalibrationUserDefinedInfoMaxSize { get; }RemarksThis property can only be used in a session initiali

### CalibrationUserDefinedInfoMaxSize

Gets the maximum number of characters that can be used to store user-defined information in the instrument onboard EEPROM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public int CalibrationUserDefinedInfoMaxSize { get; }

#### Remarks

Note

This property can only be used in a session initialized to a single instrument.

Returns an Int32 representing the number of characters of user-defined information.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CalibrationUserDefinedInfoMaxSize property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerExternalCalibration Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-currentmeasurements.html language=enus -->
## TOPIC 00086: CurrentMeasurements

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-currentmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-currentmeasurements.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the array of current measurements retrieved from the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double[] CurrentMeasurements { get; }RemarksReturns an array of System.Double that represents the current measurements retrieved from the device. ReturnsSpecifies

### CurrentMeasurements

Get the array of current measurements retrieved from the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double[] CurrentMeasurements { get; }

#### Remarks

Returns an array of System.Double that represents the current measurements retrieved from the device.

#### Returns

Specifies an array of System.Double that contain current measurements retrieved from the device.

Parent topic:

DCPowerFetchResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-incompliance.html language=enus -->
## TOPIC 00087: InCompliance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-incompliance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-incompliance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of inCompliance measurements retrieved from the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool[] InCompliance { get; }RemarksReturns an array of System.Boolean of inCompliance measurements retrieved from the device. ReturnsReturns an array of Syste

### InCompliance

Gets an array of inCompliance measurements retrieved from the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool[] InCompliance { get; }

#### Remarks

Returns an array of System.Boolean of inCompliance measurements retrieved from the device.

#### Returns

Returns an array of System.Boolean that indicates whether the output was inCompliance at the time the measurement was taken.

Parent topic:

DCPowerFetchResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-operator_eq__dcpowerfetchresult-dcpowerfetchresult.html language=enus -->
## TOPIC 00088: operator==(DCPowerFetchResult, DCPowerFetchResult)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-operator_eq__dcpowerfetchresult-dcpowerfetchresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-operator_eq__dcpowerfetchresult-dcpowerfetchresult.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerFetchResult are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerFetchResult result1, DCPowerFetchResult result2)ParametersNameTypeDescriptionresult1DCPowerFetchResultSpecifies a DCPowerFetchResult

### operator==(DCPowerFetchResult, DCPowerFetchResult)

Checks whether the two instances of [DCPowerFetchResult](nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerFetchResult result1, DCPowerFetchResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | DCPowerFetchResult | Specifies a DCPowerFetchResult object. |
| result2 | DCPowerFetchResult | Specifies a DCPowerFetchResult object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerFetchResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-voltagemeasurements.html language=enus -->
## TOPIC 00089: VoltageMeasurements

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-voltagemeasurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerfetchresult-voltagemeasurements.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of voltage measurements retrieved from the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double[] VoltageMeasurements { get; }RemarksReturns an array of System.Double that contain voltage measurements retrieved from the device. ReturnsReturns an array

### VoltageMeasurements

Gets the array of voltage measurements retrieved from the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double[] VoltageMeasurements { get; }

#### Remarks

Returns an array of System.Double that contain voltage measurements retrieved from the device.

#### Returns

Returns an array of System.Double that contain voltage measurements retrieved from the device.

Parent topic:

DCPowerFetchResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument-name.html language=enus -->
## TOPIC 00090: Name

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument-name.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the DCPowerInstrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string Name { get; }RemarksReturns a String that represents the name of the DCPowerInstrument.

### Name

Gets the name of the [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string Name { get; }

#### Remarks

Returns a String that represents the name of the [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html).

Parent topic:

DCPowerInstrument Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentadvanced.html language=enus -->
## TOPIC 00091: DCPowerInstrumentAdvanced Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentadvanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentadvanced.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides advanced properties for the instrument. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerInstrumentAdvanced : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyAll members of

### DCPowerInstrumentAdvanced Class

Provides advanced properties for the instrument.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerInstrumentAdvanced : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| IsInterlockInputOpen | Gets a value indicating whether the safety interlock circuit is open. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcalibration-self.html language=enus -->
## TOPIC 00092: Self

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcalibration-self.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcalibration-self.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerInstrumentSelfCalibration sub-object that provides properties for self calibration of the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerInstrumentSelfCalibration Self { get; }RemarksReturns an object of type DCPowerInstrumentSelfCalibratio

### Self

Gets the [DCPowerInstrumentSelfCalibration](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentselfcalibration.html) sub-object that provides properties for self calibration of the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerInstrumentSelfCalibration](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentselfcalibration.html) Self { get; }

#### Remarks

Returns an object of type [DCPowerInstrumentSelfCalibration](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentselfcalibration.html).

Parent topic:

DCPowerInstrumentCalibration Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcalibration.html language=enus -->
## TOPIC 00093: DCPowerInstrumentCalibration Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcalibration.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides objects of specific types to configure calibration of the instrument. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerInstrumentCalibration : DCPowerSubObjectRemarksExternal calibration is not supported for NI-DCPower. For mor

### DCPowerInstrumentCalibration Class

Provides objects of specific types to configure calibration of the instrument.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerInstrumentCalibration : DCPowerSubObject

#### Remarks

External calibration is not supported for NI-DCPower. For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Self | Gets the DCPowerInstrumentSelfCalibration sub-object that provides properties for self calibration of the instrument. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection-count.html language=enus -->
## TOPIC 00094: Count

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection-count.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of instruments in the session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic int Count { get; }RemarksReturns the number of instruments in the session.

### Count

Gets the number of instruments in the session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public int Count { get; }

#### Remarks

Returns the number of instruments in the session.

Parent topic:

DCPowerInstrumentCollection Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection-this__string.html language=enus -->
## TOPIC 00095: this[string name]

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection-this__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DCPowerInstrument with the specified name. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerInstrument this[string name] { get; }RemarksReturns the DCPowerInstrument corresponding to the specified name. In Visual C#, this property is the indexer. If the instrumen

### this[string name]

Gets a [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html) this[string name] { get; }

#### Remarks

Returns the [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html) corresponding to the specified name.

In Visual C#, this property is the indexer. If the instrument name corresponds to an instrument present in the session, the corresponding [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html) is returned from the collection. Otherwise, a new [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html) is created with the specified name and returned. The [DCPowerInstrument](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrument.html) created is not added to the collection.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the instrument. Use empty string to specify all instruments in the session. |

Parent topic:

DCPowerInstrumentCollection Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentidentity-instrumentmanufacturer.html language=enus -->
## TOPIC 00096: InstrumentManufacturer

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentidentity-instrumentmanufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentidentity-instrumentmanufacturer.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the manufacturer for the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string InstrumentManufacturer { get; }RemarksTo use the per-instrument version of this property, you must first initialize the session with the NIDCPower(string, bool, string

### InstrumentManufacturer

Gets the name of the manufacturer for the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string InstrumentManufacturer { get; }

#### Remarks

Note

To use the per-instrument version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead.

Returns a String that contains the name of the manufacturer for the instrument.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The InstrumentManufacturer property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerInstrumentIdentity Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentselfcalibration.html language=enus -->
## TOPIC 00097: DCPowerInstrumentSelfCalibration Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentselfcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentselfcalibration.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines properties used to configure self calibration of the instrument. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerInstrumentSelfCalibration : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs He

### DCPowerInstrumentSelfCalibration Class

Defines properties used to configure self calibration of the instrument.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerInstrumentSelfCalibration : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| SelfCalibrationPersistence | Specifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the ResetDevice method is called or the machine is powered down. This property affects the behavior of the SelfCalibrate method. If you set this property to KeepInMemory, the values calculated by the DCPowerSelfCalibration method are used in the existing session, as well as in all further sessions until you call the ResetDevice method or restart the machine. When you set this property to WriteToEeprom, the values calculated by the DCPowerSelfCalibration method are written to hardware and used in the existing session and in all subsequent sessions until another call to the DCPowerSelfCalibration method is made. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerinterchangecheckwarningeventargs-text.html language=enus -->
## TOPIC 00098: Text

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerinterchangecheckwarningeventargs-text.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerinterchangecheckwarningeventargs-text.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the interchange check warning message. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string Text { get; }RemarksReturns a String that represent the interchange check warning message.

### Text

Gets the interchange check warning message.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string Text { get; }

#### Remarks

Returns a String that represent the interchange check warning message.

Parent topic:

DCPowerInterchangeCheckWarningEventArgs Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerisolationstate.html language=enus -->
## TOPIC 00099: DCPowerIsolationState Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerisolationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerisolationstate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for the IsolationState property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerIsolationStateMembersNameValueDescriptionIsolated1128The channel is disconnected from chassis ground. NonIsolated1129The channel is connected to chassis ground.

### DCPowerIsolationState Enumeration

Specifies values for the [IsolationState](nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced-isolationstate.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerIsolationState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Isolated | 1128 | The channel is disconnected from chassis ground. |
| NonIsolated | 1129 | The channel is connected to chassis ground. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrautomaticlevelcontrol.html language=enus -->
## TOPIC 00100: DCPowerLCRAutomaticLevelControl Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrautomaticlevelcontrol.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrautomaticlevelcontrol.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for the AutomaticLevelControl and DCBiasAutomaticLevelControl properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerLCRAutomaticLevelControlMembersNameValueDescriptionOff0The channel does not correct for variation in stimulus across the DUT.

### DCPowerLCRAutomaticLevelControl Enumeration

Specifies values for the [AutomaticLevelControl](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-automaticlevelcontrol.html) and [DCBiasAutomaticLevelControl](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiasautomaticlevelcontrol.html) properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerLCRAutomaticLevelControl

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | The channel does not correct for variation in stimulus across the DUT. Because the PXIe-4190 output impedance is a function of the impedance range, selecting this option may result in an actual AC stimulus amplitude at the load that is different from the value you specify. Impedance measurements take this difference into account and remain accurate. |
| On | 1 | The channel actively attempts to maintain a constant stimulus across the DUT. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiassource.html language=enus -->
## TOPIC 00101: DCPowerLCRDCBiasSource Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiassource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiassource.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for the DCBiasSource property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerLCRDCBiasSourceMembersNameValueDescriptionOff1065Disables DC bias in LCR mode. Voltage1066Applies a constant voltage bias, as defined by DCBiasVoltageLevel. Current1067

### DCPowerLCRDCBiasSource Enumeration

Specifies values for the [DCBiasSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiassource.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerLCRDCBiasSource

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 1065 | Disables DC bias in LCR mode. |
| Voltage | 1066 | Applies a constant voltage bias, as defined by DCBiasVoltageLevel. |
| Current | 1067 | Applies a constant current bias, as defined by DCBiasCurrentLevel. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiastransientresponse.html language=enus -->
## TOPIC 00102: DCPowerLCRDCBiasTransientResponse Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiastransientresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiastransientresponse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for the DCBiasTransientResponse property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerLCRDCBiasTransientResponseMembersNameValueDescriptionNormal1151NI-DCPower automatically applies transient response values for DC bias. Custom1152NI-DCPower a

### DCPowerLCRDCBiasTransientResponse Enumeration

Specifies values for the [DCBiasTransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-dcbiastransientresponse.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerLCRDCBiasTransientResponse

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 1151 | NI-DCPower automatically applies transient response values for DC bias. |
| Custom | 1152 | NI-DCPower applies the transient response that you set manually with TransientResponse for DC bias. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-frequency.html language=enus -->
## TOPIC 00103: Frequency

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-frequency.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of the load compensation specification. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Frequency { get; }RemarksFrequency (Hz)

### Frequency

Gets the frequency of the load compensation specification.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Frequency { get; }

#### Remarks

Frequency (Hz)

Parent topic:

DCPowerLCRLoadCompensationSpot Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-referencevaluea.html language=enus -->
## TOPIC 00104: ReferenceValueA

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-referencevaluea.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-referencevaluea.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference measurement value of the load compensation specification. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double ReferenceValueA { get; }RemarksReference A measurement value

### ReferenceValueA

Gets the reference measurement value of the load compensation specification.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double ReferenceValueA { get; }

#### Remarks

Reference A measurement value

Parent topic:

DCPowerLCRLoadCompensationSpot Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-referencevalueb.html language=enus -->
## TOPIC 00105: ReferenceValueB

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-referencevalueb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot-referencevalueb.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference measurement value of the load compensation specification if applicable. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double ReferenceValueB { get; }RemarksReference B measurement value

### ReferenceValueB

Gets the reference measurement value of the load compensation specification if applicable.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double ReferenceValueB { get; }

#### Remarks

Reference B measurement value

Parent topic:

DCPowerLCRLoadCompensationSpot Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot.html language=enus -->
## TOPIC 00106: DCPowerLCRLoadCompensationSpot Data Structure

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerlcrloadcompensationspot.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a load measurement for performing compensation. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic struct DCPowerLCRLoadCompensationSpotRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyAll members of this type are s

### DCPowerLCRLoadCompensationSpot Data Structure

Specifies a load measurement for performing compensation.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public struct DCPowerLCRLoadCompensationSpot

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DCPowerLCRLoadCompensationSpot(double, DCPowerLCRReferenceValueType, double, double) | Constructs a DUT specification for a given frequency to use in LCR load compensation. |

#### Properties

| Name | Description |
| --- | --- |
| Frequency | Gets the frequency of the load compensation specification. |
| ReferenceValueA | Gets the reference measurement value of the load compensation specification. |
| ReferenceValueB | Gets the reference measurement value of the load compensation specification if applicable. |
| ReferenceValueType | Gets the reference type of the load compensation specification. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasureaperturetimeunits.html language=enus -->
## TOPIC 00107: DCPowerMeasureApertureTimeUnits Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasureaperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasureaperturetimeunits.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for ApertureTimeUnits property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerMeasureApertureTimeUnitsMembersNameValueDescriptionSeconds1028Specifies the aperture time, in seconds. PowerLineCycles1029Specifies the aperture time, in power line cy

### DCPowerMeasureApertureTimeUnits Enumeration

Specifies values for [ApertureTimeUnits](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-aperturetimeunits.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerMeasureApertureTimeUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 1028 | Specifies the aperture time, in seconds. |
| PowerLineCycles | 1029 | Specifies the aperture time, in power line cycles (PLCs). |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent-outputbehavior.html language=enus -->
## TOPIC 00108: OutputBehavior

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent-outputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent-outputbehavior.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output behavior of the MeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventOutputBehavior OutputBehavior { get; set; }RemarksSpecifies the DCPowerEventOutputBehavior for exporting the MeasureCompleteEvent event.This property is n

### OutputBehavior

Gets or sets the output behavior of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-measurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventOutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html) OutputBehavior { get; set; }

#### Remarks

Specifies the [DCPowerEventOutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html) for exporting the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-measurecompleteevent.html) event.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerMeasureCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent.html language=enus -->
## TOPIC 00109: DCPowerMeasureCompleteEvent Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the underlying hardware MeasureCompleteEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerMeasureCompleteEvent : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies

### DCPowerMeasureCompleteEvent Class

Represents the properties used to configure the underlying hardware [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-measurecompleteevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerMeasureCompleteEvent : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Delay | Gets or sets the amount of time to delay the generation of the MeasureCompleteEvent. |
| OutputBehavior | Gets or sets the output behavior of the MeasureCompleteEvent. |
| OutputTerminal | Gets or sets the output terminal for exporting the MeasureCompleteEvent. |
| Pulse | Gets the pulse characteristics of the MeasureCompleteEvent. |
| Toggle | Gets and sets the toggle initial state characteristics of the MeasureCompleteEvent. |

#### Methods

| Name | Description |
| --- | --- |
| WaitForEvent(NationalInstruments.PrecisionTimeSpan) | Waits until the device has generated the specified event. The session monitors whether each type of event has occurred at least once since the last time this method or the Initiate method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-equals__dcpowermeasurecompleteeventoutputterminal.html language=enus -->
## TOPIC 00110: Equals(DCPowerMeasureCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-equals__dcpowermeasurecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-equals__dcpowermeasurecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerMeasureCompleteEventOutputTerminal and the DCPowerMeasureCompleteEventOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerMeasureCompleteEventOutputTerminal outp

### Equals(DCPowerMeasureCompleteEventOutputTerminal)

Determines whether the current instance of [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) and the [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerMeasureCompleteEventOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerMeasureCompleteEventOutputTerminal | Specifies the DCPowerMeasureCompleteEventOutputTerminal object to be compared to the current instance of DCPowerMeasureCompleteEventOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-gethashcode.html language=enus -->
## TOPIC 00111: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerMeasureCompleteEventOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of DCPowerMeasureCo

### GetHashCode()

Returns the hash code for the current instance of [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html).

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-operator-string__dcpowermeasurecompleteeventoutputterminal.html language=enus -->
## TOPIC 00112: operator string(DCPowerMeasureCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-operator-string__dcpowermeasurecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-operator-string__dcpowermeasurecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the DCPowerMeasureCompleteEventOutputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator string(DCPowerMeasureCompleteEventOutputTerminal outputTerminal)ParametersNameTypeDescriptionoutputTerminalDCPowerM

### operator string(DCPowerMeasureCompleteEventOutputTerminal)

Converts the [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator string(DCPowerMeasureCompleteEventOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerMeasureCompleteEventOutputTerminal | Specifies the DCPowerMeasureCompleteEventOutputTerminal object to be converted to string. |

#### Returns

Returns a String from the [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) object.

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-operator_neq__dcpowermeasurecompleteeventoutputterminal-dcpowermeasurecompleteeventoutputterminal.html language=enus -->
## TOPIC 00113: operator!=(DCPowerMeasureCompleteEventOutputTerminal, DCPowerMeasureCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-operator_neq__dcpowermeasurecompleteeventoutputterminal-dcpowermeasurecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-operator_neq__dcpowermeasurecompleteeventoutputterminal-dcpowermeasurecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerMeasureCompleteEventOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerMeasureCompleteEventOutputTerminal outputTerminal1, DCPowerMeasureCompleteEventOutputTerminal outputTermina

### operator!=(DCPowerMeasureCompleteEventOutputTerminal, DCPowerMeasureCompleteEventOutputTerminal)

Checks whether the two instances of [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerMeasureCompleteEventOutputTerminal outputTerminal1, DCPowerMeasureCompleteEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerMeasureCompleteEventOutputTerminal | Specifies DCPowerMeasureCompleteEventOutputTerminal object. |
| outputTerminal2 | DCPowerMeasureCompleteEventOutputTerminal | Specifies DCPowerMeasureCompleteEventOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00114: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureCompleteEventOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerMeasureCompleteEventOutputTerminal

### PxiTriggerLine0

Gets the output terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00115: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureCompleteEventOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerMeasureCompleteEventOutputTerminal

### PxiTriggerLine1

Gets the output terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00116: PxiTriggerLine4

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline4.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureCompleteEventOutputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type DCPowerMeasureCompleteEventOutputTerminal

### PxiTriggerLine4

Gets the output terminal when the signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) representing the string "PXI_Trig4".

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00117: PxiTriggerLine5

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline5.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureCompleteEventOutputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type DCPowerMeasureCompleteEventOutputTerminal

### PxiTriggerLine5

Gets the output terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00118: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureCompleteEventOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerMeasureCompleteEventOutputTerminal

### PxiTriggerLine6

Gets the output terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerMeasureCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html language=enus -->
## TOPIC 00119: DCPowerMeasureCompleteEventOutputTerminal Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the output terminal for DCPowerMeasureCompleteEvent. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerMeasureCompleteEventOutputTerminalRemarksSee OutputTerminal. Thread SafetyAll members of this type are safe for multithreaded operation

### DCPowerMeasureCompleteEventOutputTerminal Class

Represents the output terminal for [DCPowerMeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerMeasureCompleteEventOutputTerminal

#### Remarks

See [OutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent-outputterminal.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DoNotExport | Gets the output terminal when the signal is not exported. |
| PxiTriggerLine0 | Gets the output terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the output terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the output terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the output terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the output terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the output terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the output terminal when the signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the output terminal when the signal is exported to the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates a DCPowerMeasureCompleteEventOutputTerminal object from the specified string. |
| Equals(DCPowerMeasureCompleteEventOutputTerminal) | Determines whether the current instance of DCPowerMeasureCompleteEventOutputTerminal and the DCPowerMeasureCompleteEventOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerMeasureCompleteEventOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerMeasureCompleteEventOutputTerminal. |
| ToString() | Converts the current instance of DCPowerMeasureCompleteEventOutputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator DCPowerMeasureCompleteEventOutputTerminal(string) | Converts the specified string to the equivalent DCPowerMeasureCompleteEventOutputTerminal object. |
| operator string(DCPowerMeasureCompleteEventOutputTerminal) | Converts the DCPowerMeasureCompleteEventOutputTerminal object to the equivalent string. |
| operator!=(DCPowerMeasureCompleteEventOutputTerminal, DCPowerMeasureCompleteEventOutputTerminal) | Checks whether the two instances of DCPowerMeasureCompleteEventOutputTerminal are unequal. |
| operator==(DCPowerMeasureCompleteEventOutputTerminal, DCPowerMeasureCompleteEventOutputTerminal) | Checks whether the two instances of DCPowerMeasureCompleteEventOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventpulse-polarity.html language=enus -->
## TOPIC 00120: Polarity

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventpulse-polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventpulse-polarity.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the behavior of the DCPowerMeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulsePolarity Polarity { get; set; }RemarksThe default value is ActiveHigh. Specifies the DCPowerPulsePolarity enumeration. This property is not supported by a

### Polarity

Gets or sets the behavior of the [DCPowerMeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) Polarity { get; set; }

#### Remarks

The default value is [ActiveHigh](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html). Specifies the [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) enumeration.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerMeasureCompleteEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-configuration.html language=enus -->
## TOPIC 00121: Configuration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-configuration.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerMeasurementConfiguration sub-object that contains properties to configure all measurement channels in the session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasurementConfiguration Configuration { get; }RemarksReturns an object of type DCPowerMea

### Configuration

Gets the [DCPowerMeasurementConfiguration](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration.html) sub-object that contains properties to configure all measurement channels in the session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerMeasurementConfiguration](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration.html) Configuration { get; }

#### Remarks

Returns an object of type [DCPowerMeasurementConfiguration](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration.html) that contains properties used to configure all measurement channels in the session.

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-dispose.html language=enus -->
## TOPIC 00122: Dispose()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-dispose.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees the resources held. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Dispose()

### Dispose()

Frees the resources held.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Dispose()

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetchbacklog.html language=enus -->
## TOPIC 00123: FetchBacklog

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetchbacklog.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetchbacklog.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of measurements acquired that have not been fetched yet. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic int FetchBacklog { get; }RemarksReturns the number of measurements acquired that have not been fetched yet. ReturnsReturns the number of measurements ac

### FetchBacklog

Returns the number of measurements acquired that have not been fetched yet.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public int FetchBacklog { get; }

#### Remarks

Returns the number of measurements acquired that have not been fetched yet.

#### Returns

Returns the number of measurements acquired that have not been fetched yet.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FetchBacklog method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetchlcr__string-precisiontimespan-int.html language=enus -->
## TOPIC 00124: FetchLCR(string, PrecisionTimeSpan, int)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetchlcr__string-precisiontimespan-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetchlcr__string-precisiontimespan-int.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an NILCRMeasurement array of previously measured LCR data on the specified channel that have been taken and stored in a buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NILCRMeasurement[] FetchLCR(string channelString, PrecisionTimeSpan timeout, int pointsToFet

### FetchLCR(string, PrecisionTimeSpan, int)

Returns an [NILCRMeasurement](nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement.html) array of previously measured LCR data on the specified channel that have been taken and stored in a buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [NILCRMeasurement](nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement.html)[] FetchLCR(string channelString, PrecisionTimeSpan timeout, int pointsToFetch)

#### Remarks

To use this method:

- Set [MeasureWhen](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-measurewhen.html) to [AutomaticallyAfterSourceComplete](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html) or [OnMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html)
- Put the channel in the Running state (call [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html))

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelString | string | Specifies which channel to fetch measurements from. You can specify only a single channel. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. If the session has only a single channel, you may specify an empty string to select that channel. |
| timeout | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete, in seconds. If the method does not complete within this time interval, NI-DCPower returns an error. |
| pointsToFetch | int | Specifies the number of measurements to fetch. |

#### Returns

Returns a [NILCRMeasurement](nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement.html) array.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FetchLCR method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-queryincompliance__string.html language=enus -->
## TOPIC 00125: QueryInCompliance(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-queryincompliance__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-queryincompliance__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the specified channel to determine if it is operating at the compliance limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool QueryInCompliance(string channelString)RemarksThe compliance limit is the current limit when the Function property is set to DCVoltage,

### QueryInCompliance(string)

Queries the specified channel to determine if it is operating at the compliance limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool QueryInCompliance(string channelString)

#### Remarks

- The compliance limit is the current limit when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [DCVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html), [PulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html), [ConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) or [ConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html). If the output is operating at the compliance limit, the output reaches the current limit before the desired voltage, resistance or power level.
- The compliance limit is the voltage limit when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [DCCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) or [PulseCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html). If the output is operating at the compliance limit, the output reaches the voltage limit before the desired current level.

Function

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelString | string | Specifies the channel to query. The compliance status can only be queried for one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. |

#### Returns

Returns whether the specified channel is in compliance.

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html language=enus -->
## TOPIC 00126: QueryLatchedOutputCutoffState(string, DCPowerOutputCutoffReason)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Discovers if an output cutoff limit was exceeded for the specified reason. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool QueryLatchedOutputCutoffState(string channelString, DCPowerOutputCutoffReason outputCutoffReason)RemarksWhen an output cutoff is engaged, the output

### QueryLatchedOutputCutoffState(string, DCPowerOutputCutoffReason)

Discovers if an output cutoff limit was exceeded for the specified reason.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool QueryLatchedOutputCutoffState(string channelString, DCPowerOutputCutoffReason outputCutoffReason)

#### Remarks

When an output cutoff is engaged, the output of the channel(s) is disconnected. If a limit was exceeded, the state is latched until you clear it with the [ClearLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-clearlatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method or the [Reset](nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-reset.html) method.

outputCutoffReason specifies the conditions for which an output is disconnected.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelString | string | Specifies the channels to query. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not provide channel(s), all channels in the session are used. |
| outputCutoffReason | DCPowerOutputCutoffReason | Specifies which output cutoff conditions to query. |

#### Returns

Returns whether output from the specified channel(s) has been cut off due to the specified outputCutoffReason.

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querystate__string-dcpowermeasurementoutputstate.html language=enus -->
## TOPIC 00127: QueryState(string, DCPowerMeasurementOutputState)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querystate__string-dcpowermeasurementoutputstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querystate__string-dcpowermeasurementoutputstate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the specified channel to determine if the channel is currently in the state specified by outputState. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool QueryState(string channelString, DCPowerMeasurementOutputState outputState)RemarksNI-DCPower uses the terms "sour

### QueryState(string, DCPowerMeasurementOutputState)

Queries the specified channel to determine if the channel is currently in the state specified by outputState.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool QueryState(string channelString, DCPowerMeasurementOutputState outputState)

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is [ConstantVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementoutputstate.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelString | string | Specifies the channel to query. The output state may only be queried for one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. |
| outputState | DCPowerMeasurementOutputState | Specifies the outputState of the channel that is being queried. |

#### Returns

Returns whether the specified channel is in the specified state.

Parent topic:

DCPowerMeasurement Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement.html language=enus -->
## TOPIC 00128: DCPowerMeasurement Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents properties related to all measurement channels in session. Derives fromDCPowerSubObjectISupportSynchronizationContextIDisposableSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerMeasurement : DCPowerSubObject, ISupportSynchronizationContext, IDisposableR

### DCPowerMeasurement Class

Represents properties related to all measurement channels in session.

#### Derives from

- DCPowerSubObject
- ISupportSynchronizationContext
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerMeasurement : DCPowerSubObject, ISupportSynchronizationContext, IDisposable

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the DCPowerMeasurementConfiguration sub-object that contains properties to configure all measurement channels in the session. |
| FetchBacklog | Returns the number of measurements acquired that have not been fetched yet. |
| SynchronizeCallbacks | Gets or sets how events and callback delegates are invoked. |

#### Methods

| Name | Description |
| --- | --- |
| BeginFetch(string, PrecisionTimeSpan, int, DCPowerFetchResult, AsyncCallback, object) | Returns a IAsyncResult struct that represents pending Asynchronous fetch. |
| BeginMeasure(string, DCPowerMeasureResult, AsyncCallback, object) | Returns a IAsyncResult struct that represents pending Asynchronous measure. |
| ClearLatchedOutputCutoffState(string, DCPowerOutputCutoffReason) | Clears the state of an output cutoff that was engaged. |
| Dispose() | Frees the resources held. |
| EndFetch(IAsyncResult) | Waits for a pending asynchronous fetch to complete. |
| EndMeasure(IAsyncResult) | Waits for a pending asynchronous measure to complete. |
| Fetch(string, PrecisionTimeSpan, int) | Returns DCPowerFetchResult struct created from measurements. |
| FetchLCR(string, PrecisionTimeSpan, int) | Returns an NILCRMeasurement array of previously measured LCR data on the specified channel that have been taken and stored in a buffer. |
| Measure(string) | Returns a DCPowerMeasureResult struct that contains arrays of measured voltage and current. |
| MeasureLCR(string) | Measures and returns an NILCRMeasurement array of LCR data on the specified channel(s). |
| QueryInCompliance(string) | Queries the specified channel to determine if it is operating at the compliance limit. |
| QueryLatchedOutputCutoffState(string, DCPowerOutputCutoffReason) | Discovers if an output cutoff limit was exceeded for the specified reason. |
| QueryState(string, DCPowerMeasurementOutputState) | Queries the specified channel to determine if the channel is currently in the state specified by outputState. |

#### Events

| Name | Description |
| --- | --- |
| FetchCompleted | Occurs when asynchronous call for fetch multiple operation completes. |
| MeasureCompleted | Occurs when asynchronous call for measure multiple operation completes. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementautorangethresholdmode.html language=enus -->
## TOPIC 00129: DCPowerMeasurementAutorangeThresholdMode Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementautorangethresholdmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementautorangethresholdmode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for the AutorangeThresholdMode property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerMeasurementAutorangeThresholdModeMembersNameValueDescriptionNormal1112Thresholds are selected based on a balance between accuracy and hysteresis. FastStep1113

### DCPowerMeasurementAutorangeThresholdMode Enumeration

Specifies values for the [AutorangeThresholdMode](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-autorangethresholdmode.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerMeasurementAutorangeThresholdMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 1112 | Thresholds are selected based on a balance between accuracy and hysteresis. |
| FastStep | 1113 | Optimized for faster changes in the measured signal. Thresholds for range up are configured to be a smaller percentage of the range to allow range change to happen earlier in slew of signal. |
| HighHysteresis | 1114 | Optimized for noisy signals to avoid thrashing of range changes. Thresholds are configured to be a larger percentage of the range. |
| MediumHysteresis | 1115 | Optimized for noisy signals to avoid thrashing of range changes. Thresholds are configured to be a medium percentage of the range. |
| Hold | 1116 | Attempt to maintain the existing range. Thresholds will favor the existing range. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-measurewhen.html language=enus -->
## TOPIC 00130: MeasureWhen

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-measurewhen.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-measurewhen.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets when the measure unit should acquire measurements. Unless this property is configured to OnMeasureTrigger, the DCPowerMeasureTriggerType property is ignored. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasurementWhen MeasureWhen { get; set; }RemarksTh

### MeasureWhen

Gets or sets when the measure unit should acquire measurements. Unless this property is configured to [OnMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html), the [DCPowerMeasureTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggertype.html) property is ignored.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerMeasurementWhen](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html) MeasureWhen { get; set; }

#### Remarks

The default value is [OnDemand](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html), if you set the [DCPowerSourceMode](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) property to [SinglePoint](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html). This value supports only the [Measure](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-measure__string.html) method and [Measure](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-measure__string.html) method. The default value is [AutomaticallyAfterSourceComplete](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html), if you set the [DCPowerSourceMode](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) property to [Sequence](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html). This value supports only the [Fetch](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-fetch__string-precisiontimespan-int.html) method.

Parent topic:

DCPowerMeasurementConfiguration Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-recorddeltatime.html language=enus -->
## TOPIC 00131: RecordDeltaTime

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-recorddeltatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-recorddeltatime.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the amount of time between the starts of two consecutive measurements in a measure record. Use this property only after you commit the desired measurement settings. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double RecordDeltaTime { get; }RemarksReturns the amount o

### RecordDeltaTime

Gets the amount of time between the starts of two consecutive measurements in a measure record. Use this property only after you commit the desired measurement settings.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double RecordDeltaTime { get; }

#### Remarks

Returns the amount of time between the starts of two consecutive measurements in a measure record.

DCPowerMeasurementAutoZero

Once

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerMeasurementConfiguration Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs-dcpowermeasurementeventargs__exception-bool-object-t.html language=enus -->
## TOPIC 00132: DCPowerMeasurementEventArgs(Exception, bool, object, T)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs-dcpowermeasurementeventargs__exception-bool-object-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs-dcpowermeasurementeventargs__exception-bool-object-t.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of type NationalInstruments.ModularInstruments.NIDCPower.DCPowerMeasurementEventArgs<T>. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasurementEventArgs(Exception error, bool canceled, object userState, T result)ParametersNameTypeDescrip

### DCPowerMeasurementEventArgs(Exception, bool, object, T)

Initializes a new instance of type NationalInstruments.ModularInstruments.NIDCPower.DCPowerMeasurementEventArgs<T>.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public DCPowerMeasurementEventArgs(Exception error, bool canceled, object userState, T result)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | Exception | Specifies the exception thrown during the operation. |
| canceled | bool | Specifies whether the operation was completed or cancelled. |
| userState | object | Specifies the object used to associate client state, such as a task ID, with this particular asynchronous operation. |
| result | T | Specifies the reading obtained from the operation. |

Parent topic:

DCPowerMeasurementEventArgs<T> Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs-result.html language=enus -->
## TOPIC 00133: Result

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs-result.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs-result.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the result obtained by the measurement operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic T Result { get; }RemarksContains a single value for a single point measurement, or an array of values for a multipoint measurement or waveform datatype for waveform measurem

### Result

Gets the result obtained by the measurement operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public T Result { get; }

#### Remarks

Contains a single value for a single point measurement, or an array of values for a multipoint measurement or waveform datatype for waveform measurement.

Parent topic:

DCPowerMeasurementEventArgs<T> Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs.html language=enus -->
## TOPIC 00134: DCPowerMeasurementEventArgs<T> Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementeventargs.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Holds the event data obtained after asynchronous measurement completion. Derives fromAsyncCompletedEventArgsSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerMeasurementEventArgs : AsyncCompletedEventArgsRemarksThis class derives from System.ComponentModel.AsyncCom

### DCPowerMeasurementEventArgs<T> Class

Holds the event data obtained after asynchronous measurement completion.

#### Derives from

- AsyncCompletedEventArgs

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerMeasurementEventArgs : AsyncCompletedEventArgs

#### Remarks

This class derives from System.ComponentModel.AsyncCompletedEventArgs that contains System.ComponentModel.AsyncCompletedEventArgs.Error and System.ComponentModel.AsyncCompletedEventArgs.Cancelled. System.ComponentModel.AsyncCompletedEventArgs.Error contains exception that was thrown during that operation. System.ComponentModel.AsyncCompletedEventArgs.Cancelled is used to indicate whether the operation was completed or cancelled. This class also contains readings that are obtained as a result of the operation.

#### Type Parameters

| Name | Description |
| --- | --- |
| T | Refers to DCPowerMeasureResult when used with BeginMeasure. Refers to DCPowerFetchResult when used with BeginFetch. |

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DCPowerMeasurementEventArgs(Exception, bool, object, T) | Initializes a new instance of type NationalInstruments.ModularInstruments.NIDCPower.DCPowerMeasurementEventArgs<T>. |

#### Properties

| Name | Description |
| --- | --- |
| Result | Gets the result obtained by the measurement operation. |

#### See Also

- DCPowerTriggers

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementnoiserejection.html language=enus -->
## TOPIC 00135: DCPowerMeasurementNoiseRejection Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementnoiserejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementnoiserejection.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of NoiseRejection. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerMeasurementNoiseRejectionMembersNameValueDescriptionNormal1044Specifies normal rejection of DC noise. SecondOrder1043Specifies a second-order rejection of DC noise.

### DCPowerMeasurementNoiseRejection Enumeration

Specifies the type of [NoiseRejection](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-noiserejection.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerMeasurementNoiseRejection

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 1044 | Specifies normal rejection of DC noise. |
| SecondOrder | 1043 | Specifies a second-order rejection of DC noise. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-currentmeasurements.html language=enus -->
## TOPIC 00136: CurrentMeasurements

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-currentmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-currentmeasurements.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of current measurements retrieved from the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double[] CurrentMeasurements { get; }RemarksReturns a System.Double[]. ReturnsReturns a System.Double[] that contains current measurements retrieved from the devi

### CurrentMeasurements

Gets the array of current measurements retrieved from the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double[] CurrentMeasurements { get; }

#### Remarks

Returns a System.Double[].

#### Returns

Returns a System.Double[] that contains current measurements retrieved from the device.

Parent topic:

DCPowerMeasureResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-equals__dcpowermeasureresult.html language=enus -->
## TOPIC 00137: Equals(DCPowerMeasureResult)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-equals__dcpowermeasureresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-equals__dcpowermeasureresult.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerMeasureResult and the DCPowerMeasureResult object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerMeasureResult result)ParametersNameTypeDescriptionresultDCPowerMeasureResultSpeci

### Equals(DCPowerMeasureResult)

Determines whether the current instance of [DCPowerMeasureResult](nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult.html) and the [DCPowerMeasureResult](nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerMeasureResult result)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result | DCPowerMeasureResult | Specifies the DCPowerMeasureResult object to be compared to the current instance of DCPowerMeasureResult. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerMeasureResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-equals__object.html language=enus -->
## TOPIC 00138: Equals(object)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-equals__object.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of the DCPowerMeasureResult object and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to t

### Equals(object)

Determines whether the current instance of the [DCPowerMeasureResult](nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult.html) object and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of the DCPowerMeasureResult object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerMeasureResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-voltagemeasurements.html language=enus -->
## TOPIC 00139: VoltageMeasurements

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-voltagemeasurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasureresult-voltagemeasurements.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of voltage measurements retrieved from the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double[] VoltageMeasurements { get; }RemarksReturns a System.Double[]. ReturnsReturns a System.Double[] that contain voltage measurements retrieved from the devic

### VoltageMeasurements

Gets the array of voltage measurements retrieved from the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double[] VoltageMeasurements { get; }

#### Remarks

Returns a System.Double[].

#### Returns

Returns a System.Double[] that contain voltage measurements retrieved from the device.

Parent topic:

DCPowerMeasureResult Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-configuresoftwareedgetrigger.html language=enus -->
## TOPIC 00140: ConfigureSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-configuresoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-configuresoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the MeasureTrigger for software triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ConfigureSoftwareEdgeTrigger()ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe ConfigureSoftwareEdgeTrigger method was accessed after the associated NIDCPower

### ConfigureSoftwareEdgeTrigger()

Configures the [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-measuretrigger.html) for software triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ConfigureSoftwareEdgeTrigger()

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ConfigureSoftwareEdgeTrigger method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerMeasureTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00141: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a Software Edge MeasureTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method can override an external edge trigger. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe SendSoftwareEdgeTrigger method was accessed

### SendSoftwareEdgeTrigger()

Sends a Software Edge [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-measuretrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

This method can override an external edge trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SendSoftwareEdgeTrigger method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerMeasureTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html language=enus -->
## TOPIC 00142: DCPowerMeasureTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the Measure trigger for NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerMeasureTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help.

### DCPowerMeasureTrigger Class

Represents the properties used to configure the Measure trigger for NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerMeasureTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerDigitalEdgeMeasureTrigger sub-object to configure the device to wait for digital edge MeasureTrigger. |
| ExportedOutputTerminal | Gets or sets the MeasureTrigger exported output terminal. |
| Type | Gets or sets the MeasureTrigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the MeasureTrigger for software triggering. |
| SendSoftwareEdgeTrigger() | Sends a Software Edge MeasureTrigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-equals__dcpowermeasuretriggerexportedoutputterminal.html language=enus -->
## TOPIC 00143: Equals(DCPowerMeasureTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-equals__dcpowermeasuretriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-equals__dcpowermeasuretriggerexportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerMeasureTriggerExportedOutputTerminal and the DCPowerMeasureTriggerExportedOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerMeasureTriggerExportedOutputTermina

### Equals(DCPowerMeasureTriggerExportedOutputTerminal)

Determines whether the current instance of [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) and the [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerMeasureTriggerExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerMeasureTriggerExportedOutputTerminal | Specifies the DCPowerMeasureTriggerExportedOutputTerminal object to be compared to the current instance of DCPowerMeasureTriggerExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerMeasureTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00144: FromString(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-fromstring__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DCPowerMeasureTriggerExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureTriggerExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpecifi

### FromString(string)

Creates a [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string that is the output terminal of DCPowerMeasureTrigger. |

#### Returns

Returns an object of type [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html).

Parent topic:

DCPowerMeasureTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-gethashcode.html language=enus -->
## TOPIC 00145: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerMeasureTriggerExportedOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of DCPowerMeasure

### GetHashCode()

Returns the hash code for the current instance of [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html).

Parent topic:

DCPowerMeasureTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-operator-string__dcpowermeasuretriggerexportedoutputterminal.html language=enus -->
## TOPIC 00146: operator string(DCPowerMeasureTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-operator-string__dcpowermeasuretriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-operator-string__dcpowermeasuretriggerexportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the DCPowerMeasureTriggerExportedOutputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator string(DCPowerMeasureTriggerExportedOutputTerminal outputTerminal)ParametersNameTypeDescriptionoutputTerminalDCPo

### operator string(DCPowerMeasureTriggerExportedOutputTerminal)

Converts the [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator string(DCPowerMeasureTriggerExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerMeasureTriggerExportedOutputTerminal | Specifies the DCPowerMeasureTriggerExportedOutputTerminal object to be converted to string. |

#### Returns

Returns a string from the [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) object.

Parent topic:

DCPowerMeasureTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00147: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureTriggerExportedOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerMeasureTriggerExportedOutputTermi

### PxiTriggerLine0

Gets the output terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerMeasureTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00148: PxiTriggerLine4

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal-pxitriggerline4.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerMeasureTriggerExportedOutputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type DCPowerMeasureTriggerExportedOutputTermi

### PxiTriggerLine4

Gets the output terminal when the signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) representing the string "PXI_Trig4".

Parent topic:

DCPowerMeasureTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html language=enus -->
## TOPIC 00149: DCPowerMeasureTriggerExportedOutputTerminal Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the output terminal for exporting the DCPowerMeasureTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerMeasureTriggerExportedOutputTerminalRemarksSee ExportedOutputTerminal. Thread SafetyAll members of this type are safe for multi

### DCPowerMeasureTriggerExportedOutputTerminal Class

Represents the output terminal for exporting the [DCPowerMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerMeasureTriggerExportedOutputTerminal

#### Remarks

See [ExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger-exportedoutputterminal.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DoNotExport | Gets the output terminal when the signal is not exported. |
| PxiTriggerLine0 | Gets the output terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the output terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the output terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the output terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the output terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the output terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the output terminal when the signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the output terminal when the signal is exported to the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates a DCPowerMeasureTriggerExportedOutputTerminal object from the specified string. |
| Equals(DCPowerMeasureTriggerExportedOutputTerminal) | Determines whether the current instance of DCPowerMeasureTriggerExportedOutputTerminal and the DCPowerMeasureTriggerExportedOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerMeasureTriggerExportedOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerMeasureTriggerExportedOutputTerminal. |
| ToString() | Converts the current instance of DCPowerMeasureTriggerExportedOutputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator DCPowerMeasureTriggerExportedOutputTerminal(string) | Converts the specified string to the equivalent DCPowerMeasureTriggerExportedOutputTerminal object. |
| operator string(DCPowerMeasureTriggerExportedOutputTerminal) | Converts the DCPowerMeasureTriggerExportedOutputTerminal object to the equivalent string. |
| operator!=(DCPowerMeasureTriggerExportedOutputTerminal, DCPowerMeasureTriggerExportedOutputTerminal) | Checks whether the two instances of DCPowerMeasureTriggerExportedOutputTerminal are unequal. |
| operator==(DCPowerMeasureTriggerExportedOutputTerminal, DCPowerMeasureTriggerExportedOutputTerminal) | Checks whether the two instances of DCPowerMeasureTriggerExportedOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-events.html language=enus -->
## TOPIC 00150: Events

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-events.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputEvents sub-object to configure NI-DCPower events. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputEvents Events { get; }RemarksReturns an object of type DCPowerOutputEvents.

### Events

Gets the [DCPowerOutputEvents](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents.html) sub-object to configure NI-DCPower events.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputEvents](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents.html) Events { get; }

#### Remarks

Returns an object of type [DCPowerOutputEvents](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents.html).

Parent topic:

DCPowerOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-measurement.html language=enus -->
## TOPIC 00151: Measurement

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-measurement.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputMeasurement sub-object used to configure channel specific properties of the source unit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputMeasurement Measurement { get; }RemarksReturns an object of type DCPowerOutputMeasurement.

### Measurement

Gets the [DCPowerOutputMeasurement](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement.html) sub-object used to configure channel specific properties of the source unit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputMeasurement](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement.html) Measurement { get; }

#### Remarks

Returns an object of type [DCPowerOutputMeasurement](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement.html).

Parent topic:

DCPowerOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-name.html language=enus -->
## TOPIC 00152: Name

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-name.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the DCPowerOutput channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string Name { get; }RemarksReturns a String that represents the name of the DCPowerOutput channel.

### Name

Gets the name of the [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string Name { get; }

#### Remarks

Returns a String that represents the name of the [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) channel.

Parent topic:

DCPowerOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-source.html language=enus -->
## TOPIC 00153: Source

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-source.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputSource sub-object used to configure channel specific properties of the source unit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSource Source { get; }RemarksReturns an object of type DCPowerOutputSource.

### Source

Gets the [DCPowerOutputSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource.html) sub-object used to configure channel specific properties of the source unit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource.html) Source { get; }

#### Remarks

Returns an object of type [DCPowerOutputSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource.html).

Parent topic:

DCPowerOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-triggers.html language=enus -->
## TOPIC 00154: Triggers

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutput-triggers.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputTriggers sub-object that is used to configure NI-DCPower triggers. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputTriggers Triggers { get; }RemarksReturns an object of type DCPowerOutputTriggers.

### Triggers

Gets the [DCPowerOutputTriggers](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers.html) sub-object that is used to configure NI-DCPower triggers.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputTriggers](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers.html) Triggers { get; }

#### Remarks

Returns an object of type [DCPowerOutputTriggers](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers.html).

Parent topic:

DCPowerOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcollection-this__string.html language=enus -->
## TOPIC 00155: this[string name]

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcollection-this__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DCPowerOutput channel with the specified name. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutput this[string name] { get; }RemarksReturns the DCPowerOutput corresponding to the name of the channel. In Visual C#, this property is the indexer. If the channel

### this[string name]

Gets a [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) channel with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) this[string name] { get; }

#### Remarks

Returns the [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) corresponding to the name of the channel.

In Visual C#, this property is the indexer. If the channel name corresponds to a simple channel string present in the session ("0", "1"), the corresponding [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) channel is returned from the collection. Otherwise, a new [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) channel is created with the specified name and returned. The [DCPowerOutput](nationalinstruments-modularinstruments-nidcpower-dcpoweroutput.html) channel created is not added to the collection.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. Use empty string to specify all channels in the session. |

Parent topic:

DCPowerOutputCollection Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-initiate.html language=enus -->
## TOPIC 00156: Initiate()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-initiate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts generation or acquisition, causing the specified channel(s) to leave the Uncommitted state or Committed state and enter the Running state. To return to the Uncommitted state, call the Abort method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Initiate()RemarksR

### Initiate()

Starts generation or acquisition, causing the specified channel(s) to leave the Uncommitted state or Committed state and enter the Running state. To return to the Uncommitted state, call the [Abort](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-abort.html) method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Initiate()

#### Remarks

Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific software states.

Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not provide channel(s), all channels in the session are used.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputControl Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdevicespecificlcr.html language=enus -->
## TOPIC 00157: DCPowerOutputDeviceSpecificLCR Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdevicespecificlcr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdevicespecificlcr.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides LCR meter specific properties related to NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputDeviceSpecificLCR : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread Sa

### DCPowerOutputDeviceSpecificLCR Class

Provides LCR meter specific properties related to NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputDeviceSpecificLCR : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| CableLength | Specifies how to apply cable compensation data for instruments that support LCR functionality. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgemeasuretrigger-configure__dcpowerdigitaledgemeasuretriggerinputterminal-dcpowertriggeredge.html language=enus -->
## TOPIC 00158: Configure(DCPowerDigitalEdgeMeasureTriggerInputTerminal, DCPowerTriggerEdge)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgemeasuretrigger-configure__dcpowerdigitaledgemeasuretriggerinputterminal-dcpowertriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgemeasuretrigger-configure__dcpowerdigitaledgemeasuretriggerinputterminal-dcpowertriggeredge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the MeasureTrigger for digital edge triggering for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Configure(DCPowerDigitalEdgeMeasureTriggerInputTerminal inputTerminal, DCPowerTriggerEdge edge)RemarksThis method cannot be called for

### Configure(DCPowerDigitalEdgeMeasureTriggerInputTerminal, DCPowerTriggerEdge)

Configures the [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-measuretrigger.html) for digital edge triggering for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Configure(DCPowerDigitalEdgeMeasureTriggerInputTerminal inputTerminal, DCPowerTriggerEdge edge)

#### Remarks

Note

This method cannot be called for channels that are in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgeMeasureTriggerInputTerminal | Specifies the input terminal for the digital edge MeasureTrigger.You can specify any valid input terminal. Valid terminals are listed in MAX under the Device Routes tab or in the Signal Routing topic for the instrument.Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent. |
| edge | DCPowerTriggerEdge | Specifies whether to configure the MeasureTrigger to assert on the rising or falling edge. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| System.ArgumentNullException | The method was called with a null input terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgeMeasureTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgemeasuretrigger-edge.html language=enus -->
## TOPIC 00159: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgemeasuretrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgemeasuretrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to configure the MeasureTrigger to assert on the rising or falling edge. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by De

### Edge

Gets or sets whether to configure the [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-measuretrigger.html) to assert on the rising or falling edge.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgeMeasureTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-configure__dcpowerdigitaledgepulsetriggerinputterminal-dcpowertriggeredge.html language=enus -->
## TOPIC 00160: Configure(DCPowerDigitalEdgePulseTriggerInputTerminal, DCPowerTriggerEdge)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-configure__dcpowerdigitaledgepulsetriggerinputterminal-dcpowertriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-configure__dcpowerdigitaledgepulsetriggerinputterminal-dcpowertriggeredge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PulseTrigger for digital edge triggering for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Configure(DCPowerDigitalEdgePulseTriggerInputTerminal inputTerminal, DCPowerTriggerEdge edge)RemarksThis method cannot be called in the R

### Configure(DCPowerDigitalEdgePulseTriggerInputTerminal, DCPowerTriggerEdge)

Configures the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-pulsetrigger.html) for digital edge triggering for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Configure(DCPowerDigitalEdgePulseTriggerInputTerminal inputTerminal, DCPowerTriggerEdge edge)

#### Remarks

Note

This method cannot be called in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputTerminal | DCPowerDigitalEdgePulseTriggerInputTerminal | Specifies the input terminal for the digital edge PulseTrigger.You can specify any valid input terminal. Valid terminals are listed in MAX under the Device Routes tab or in the Signal Routing topic for the instrument.Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent. |
| edge | DCPowerTriggerEdge | Specifies whether to configure the PulseTrigger to assert on the rising or falling edge. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| System.ArgumentNullException | The method was called with a null input terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgePulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-edge.html language=enus -->
## TOPIC 00161: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to configure the PulseTrigger to assert on the rising or falling edge. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Devi

### Edge

Gets or sets whether to configure the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-pulsetrigger.html) to assert on the rising or falling edge.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgePulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-inputterminal.html language=enus -->
## TOPIC 00162: InputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgepulsetrigger-inputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the PulseTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerDigitalEdgePulseTriggerInputTerminal InputTerminal { get; set; }RemarksUse this property only when the Type property is set to DigitalEdge. You can specify any valid i

### InputTerminal

Gets or sets the input terminal for the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-pulsetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) InputTerminal { get; set; }

#### Remarks

Use this property only when the [Type](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-type.html) property is set to [DigitalEdge](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggertype.html). You can specify any valid input terminal for this property. Valid terminals are listed in Measurement and Automation Explorer under the **Device Routes** tab or in the documentation for your device.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0.

Note

You must specify the input terminal for a PXI-4132 using the form /Dev1/PXI_Trig0, where Dev1 is a PXI-4132 and PXI_Trig0 is the terminal.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerDigitalEdgePulseTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgepulsetriggerinputterminal.html) value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| System.ArgumentNullException | The property was set with a null input terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgePulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgeshutdowntrigger-inputterminal.html language=enus -->
## TOPIC 00163: InputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgeshutdowntrigger-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgeshutdowntrigger-inputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the ShutdownTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerDigitalEdgeShutdownTriggerInputTerminal InputTerminal { get; set; }RemarksUse this property only when the Type property is set to DigitalEdge. This property is not

### InputTerminal

Gets or sets the input terminal for the [ShutdownTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-shutdowntrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) InputTerminal { get; set; }

#### Remarks

Type

DigitalEdge

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Specifies the [DCPowerDigitalEdgeShutdownTriggerInputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerdigitaledgeshutdowntriggerinputterminal.html) value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| System.ArgumentNullException | The property was set with a null input terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgeShutdownTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesourcetrigger.html language=enus -->
## TOPIC 00164: DCPowerOutputDigitalEdgeSourceTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesourcetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesourcetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure the digital edge for the SourceTrigger for the specified channel(s). Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputDigitalEdgeSourceTrigger : DCPowerSubObjectRemarksFor mo

### DCPowerOutputDigitalEdgeSourceTrigger Class

Represents the methods and properties used to configure the digital edge for the [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-sourcetrigger.html) for the specified channel(s).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputDigitalEdgeSourceTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets whether to configure the SourceTrigger to assert on the rising or falling edge. |
| InputTerminal | Gets or sets the input terminal for the SourceTrigger. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(DCPowerDigitalEdgeSourceTriggerInputTerminal, DCPowerTriggerEdge) | Configures the SourceTrigger for digital edge triggering for the specified channel(s). |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgestarttrigger-edge.html language=enus -->
## TOPIC 00165: Edge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgestarttrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgestarttrigger-edge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to configure the StartTrigger to assert on the rising or falling edge. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggerEdge Edge { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Devi

### Edge

Gets or sets whether to configure the [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html) to assert on the rising or falling edge.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) Edge { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Specifies the [DCPowerTriggerEdge](nationalinstruments-modularinstruments-nidcpower-dcpowertriggeredge.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputDigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sequenceenginedoneevent.html language=enus -->
## TOPIC 00166: SequenceEngineDoneEvent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sequenceenginedoneevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sequenceenginedoneevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputSequenceEngineDoneEvent sub-object that is used to configure the Sequence Engine Done event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSequenceEngineDoneEvent SequenceEngineDoneEvent { get; }RemarksReturns an object of type DCPowerOutp

### SequenceEngineDoneEvent

Gets the [DCPowerOutputSequenceEngineDoneEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceenginedoneevent.html) sub-object that is used to configure the Sequence Engine Done event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSequenceEngineDoneEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceenginedoneevent.html) SequenceEngineDoneEvent { get; }

#### Remarks

Returns an object of type [DCPowerOutputSequenceEngineDoneEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceenginedoneevent.html).

Parent topic:

DCPowerOutputEvents Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html language=enus -->
## TOPIC 00167: SourceCompleteEvent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputSourceCompleteEvent sub-object that is used to configure the Source Complete event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceCompleteEvent SourceCompleteEvent { get; }RemarksReturns an object of type DCPowerOutputSourceCompleteE

### SourceCompleteEvent

Gets the [DCPowerOutputSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html) sub-object that is used to configure the Source Complete event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html) SourceCompleteEvent { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html).

Parent topic:

DCPowerOutputEvents Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-automaticlevelcontrol.html language=enus -->
## TOPIC 00168: AutomaticLevelControl

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-automaticlevelcontrol.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-automaticlevelcontrol.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerLCRAutomaticLevelControl AutomaticLevelControl { get; set; }RemarksThe use of voltage or

### AutomaticLevelControl

Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerLCRAutomaticLevelControl](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrautomaticlevelcontrol.html) AutomaticLevelControl { get; set; }

#### Remarks

The use of voltage or current depends on the test signal you configure with the [StimulusFunction](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-stimulusfunction.html) property.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is [On](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrautomaticlevelcontrol.html).

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-compensation.html language=enus -->
## TOPIC 00169: Compensation

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-compensation.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputLCRCompensation sub-object that is used to configure NI-DCPower LCR measurement compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputLCRCompensation Compensation { get; }RemarksReturns an object of type DCPowerOutputLCRCompensation.

### Compensation

Gets the [DCPowerOutputLCRCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation.html) sub-object that is used to configure NI-DCPower LCR measurement compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputLCRCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation.html) Compensation { get; }

#### Remarks

Returns an object of type [DCPowerOutputLCRCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation.html).

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-custommeasurementtime.html language=enus -->
## TOPIC 00170: CustomMeasurementTime

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-custommeasurementtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-custommeasurementtime.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LCR measurement aperture time for a channel, in seconds, when the MeasurementTime property is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CustomMeasurementTime { get; set; }RemarksThis property is not supported by all instruments. Refer

### CustomMeasurementTime

Specifies the LCR measurement aperture time for a channel, in seconds, when the [MeasurementTime](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-measurementtime.html) property is set to **Custom**.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CustomMeasurementTime { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Valid values: 0 seconds to 0.99999 seconds

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiascurrentlevel.html language=enus -->
## TOPIC 00171: DCBiasCurrentLevel

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiascurrentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiascurrentlevel.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC bias current level, in amperes, when the DCBiasSource is set to Current. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double DCBiasCurrentLevel { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Devi

### DCBiasCurrentLevel

Specifies the DC bias current level, in amperes, when the [DCBiasSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiassource.html) is set to [Current](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiassource.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double DCBiasCurrentLevel { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Bias current (amps). Valid values: -0.1 A to 0.1 A.

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiasvoltagelevel.html language=enus -->
## TOPIC 00172: DCBiasVoltageLevel

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiasvoltagelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiasvoltagelevel.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC bias voltage level, in volts, when the DCBiasSource is set to Voltage. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double DCBiasVoltageLevel { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device

### DCBiasVoltageLevel

Specifies the DC bias voltage level, in volts, when the [DCBiasSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiassource.html) is set to [Voltage](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrdcbiassource.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double DCBiasVoltageLevel { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

Bias voltage (volts). Valid values: -40 V to 40 V.

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedanceautorange.html language=enus -->
## TOPIC 00173: ImpedanceAutoRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedanceautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedanceautorange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerLCRImpedanceAutorange ImpedanceAutoRange { get; set; }RemarksImpedance autoranging may be enabled on

### ImpedanceAutoRange

Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerLCRImpedanceAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrimpedanceautorange.html) ImpedanceAutoRange { get; set; }

#### Remarks

Impedance autoranging may be enabled only when both:

- The source mode is set to single point
- [MeasureWhen](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-measurewhen.html) is set to a value other than [OnMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html)

You can read [ImpedanceRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedancerange.html) back after a measurement to determine the actual range used.

When enabled, impedance autoranging overrides impedance range settings you configure manually with any other properties.

When using a load with unknown impedance, you can set this property to **On** to determine the correct impedance range for the load. When you know the load impedance, you can achieve faster performance by setting this property to **Off** and setting [ImpedanceRangeSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedancerangesource.html) to [LoadConfiguration](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrimpedancerangesource.html).

The default value is **On**.

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedancerangesource.html language=enus -->
## TOPIC 00174: ImpedanceRangeSource

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedancerangesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedancerangesource.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the impedance range for LCR measurements is determined. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerLCRImpedanceRangeSource ImpedanceRangeSource { get; set; }RemarksImpedanceAutoRange overrides any impedance range determined by this property.This prop

### ImpedanceRangeSource

Specifies how the impedance range for LCR measurements is determined.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerLCRImpedanceRangeSource](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrimpedancerangesource.html) ImpedanceRangeSource { get; set; }

#### Remarks

Note

[ImpedanceAutoRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedanceautorange.html) overrides any impedance range determined by this property.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is [ImpedanceRange](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrimpedancerangesource.html).

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-loadresistance.html language=enus -->
## TOPIC 00175: LoadResistance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-loadresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-loadresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the ImpedanceRangeSource is set to Load Configuration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double LoadResistance { get; set; }RemarksThis pr

### LoadResistance

Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the [ImpedanceRangeSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-impedancerangesource.html) is set to **Load Configuration**.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double LoadResistance { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Valid values: [0 ohms, +inf ohms)

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-sourcedelaymode.html language=enus -->
## TOPIC 00176: SourceDelayMode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-sourcedelaymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-sourcedelaymode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerLCRSourceDelayMode SourceDelayMode { get; set; }RemarksYou can r

### SourceDelayMode

For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerLCRSourceDelayMode](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrsourcedelaymode.html) SourceDelayMode { get; set; }

#### Remarks

You can return the source delay duration for either option by reading [SourceDelay](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-sourcedelay.html).

Note

When you use this property to manually set the source delay, it is possible to set source delays short enough to unbalance the bridge and affect measurement accuracy. LCR measurement methods report whether the bridge is unbalanced.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is **Automatic**.

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-voltageamplitude.html language=enus -->
## TOPIC 00177: VoltageAmplitude

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-voltageamplitude.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-voltageamplitude.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amplitude, in V RMS, of the AC voltage test signal applied to the DUT for LCR measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double VoltageAmplitude { get; set; }RemarksThis property applies when StimulusFunction is set to ACVoltage.This property

### VoltageAmplitude

Specifies the amplitude, in V RMS, of the AC voltage test signal applied to the DUT for LCR measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageAmplitude { get; set; }

#### Remarks

This property applies when [StimulusFunction](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-stimulusfunction.html) is set to [ACVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowerlcrstimulusfunction.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

RMS voltage (volts) for AC stimulus. Valid values: 7.08e-4 V RMS to 7.07 V RMS.

Parent topic:

DCPowerOutputLCR Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-acditherenabled.html language=enus -->
## TOPIC 00178: ACDitherEnabled

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-acditherenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-acditherenabled.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether dithering is enabled during LCR measurements. Dithering adds out-of-band noise to improve measurements of small voltage and current signals. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool ACDitherEnabled { get; set; }RemarksIf this property is set to t

### ACDitherEnabled

Specifies whether dithering is enabled during LCR measurements. Dithering adds out-of-band noise to improve measurements of small voltage and current signals.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool ACDitherEnabled { get; set; }

#### Remarks

If this property is set to **true**, dithering is applied to LCR measurements. If this property is set to **false**, dithering is not applied to LCR measurements.

Note

Hardware is only warranted to meet its accuracy specs with dither enabled. You can disable dither if the added noise interferes with your device-under-test.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerOutputLCRAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-currentrange.html language=enus -->
## TOPIC 00179: CurrentRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-currentrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-currentrange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current range, in amps RMS, that defines the values to which you can set the CurrentAmplitude for the specified channel(s). For valid ranges, refer to the specifications for your instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentRange { g

### CurrentRange

Specifies the current range, in amps RMS, that defines the values to which you can set the [CurrentAmplitude](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-currentamplitude.html) for the specified channel(s). For valid ranges, refer to the specifications for your instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentRange { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The AC current range, in amps RMS.

Parent topic:

DCPowerOutputLCRAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-dcbiasvoltagerange.html language=enus -->
## TOPIC 00180: DCBiasVoltageRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-dcbiasvoltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-dcbiasvoltagerange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC bias voltage range, in volts, that defines the values to which you can set the DCBiasVoltageLevel for the specified channel(s). For valid ranges, refer to the specifications for your instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double DCBiasVol

### DCBiasVoltageRange

Specifies the DC bias voltage range, in volts, that defines the values to which you can set the [DCBiasVoltageLevel](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcr-dcbiasvoltagelevel.html) for the specified channel(s). For valid ranges, refer to the specifications for your instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double DCBiasVoltageRange { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The DC Bias voltage range, in volts.

Parent topic:

DCPowerOutputLCRAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-sourceaperturetime.html language=enus -->
## TOPIC 00181: SourceApertureTime

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-sourceaperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcradvanced-sourceaperturetime.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LCR source aperture time, in seconds, for a channel in LCR mode. Use this property to adjust the aperture time for the LCR control loop. In systems that use multiple tones that are equally spaced, setting this property to 1/(Tone Spacing in Hz) can reduce the impact of external interfe

### SourceApertureTime

Specifies the LCR source aperture time, in seconds, for a channel in LCR mode. Use this property to adjust the aperture time for the LCR control loop. In systems that use multiple tones that are equally spaced, setting this property to 1/(Tone Spacing in Hz) can reduce the impact of external interference and still maintain an integer number of cycles for all multi-tones. Increasing LCR source aperture time can increase the required settling time.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double SourceApertureTime { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Valid values: 5.0e-6 seconds to 100.0e-3 seconds

Parent topic:

DCPowerOutputLCRAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-actualloadresistance.html language=enus -->
## TOPIC 00182: ActualLoadResistance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-actualloadresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-actualloadresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the actual resistance, in ohms, of the load used for load LCR compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double ActualLoadResistance { get; set; }RemarksThis property applies when OpenShortLoadCompensationDataSource is set to AsDefined.This proper

### ActualLoadResistance

Specifies the actual resistance, in ohms, of the load used for load LCR compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double ActualLoadResistance { get; set; }

#### Remarks

This property applies when [OpenShortLoadCompensationDataSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-openshortloadcompensationdatasource.html) is set to **AsDefined**.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is **0.0**.

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-configurecompensation__byte_arr1.html language=enus -->
## TOPIC 00183: ConfigureCompensation(byte[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-configurecompensation__byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-configurecompensation__byte_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies previously generated open, short, load, as well as open and short custom cable compensationData to LCR measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ConfigureCompensation(byte[] compensationData)RemarksThis method applies open, short and load comp

### ConfigureCompensation(byte[])

Applies previously generated open, short, load, as well as open and short custom cable *compensationData*  to LCR measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ConfigureCompensation(byte[] compensationData)

#### Remarks

This method applies open, short and load compensation data when you have set [OpenShortLoadCompensationDataSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-openshortloadcompensationdatasource.html) to [AsConfigured](nationalinstruments-modularinstruments-nidcpower-dcpowerlcropenshortloadcompensationdatasource.html), and it also applies custom cable compensation data when you have set [CableLength](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdevicespecificlcr-cablelength.html) to [CustomAsConfigured](nationalinstruments-modularinstruments-nidcpower-dcpowercablelength.html).

Call this method after you have obtained LCR compensation data. If [ShortCustomCableCompensationEnabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-shortcustomcablecompensationenabled.html) is set to true, you must generate data with both [PerformOpenCustomCableCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencustomcablecompensation.html) and [PerformShortCustomCableCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performshortcustomcablecompensation.html); if false, you must only use [PerformOpenCustomCableCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencustomcablecompensation.html), and NI-DCPower uses default short data.

Call [GetCompensationData](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-getcompensationdata.html) and pass the compensation data to this method.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| compensationData | byte[] | The System.Byte array that contains the compensation data to import. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The method was called with a null compensationData array. |

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-loadcompensationenabled.html language=enus -->
## TOPIC 00184: LoadCompensationEnabled

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-loadcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-loadcompensationenabled.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply load LCR compensation data to LCR measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool LoadCompensationEnabled { get; set; }RemarksBoth OpenCompensationEnabled and ShortCompensationEnabled must be set to true in order to set this prope

### LoadCompensationEnabled

Specifies whether to apply load LCR compensation data to LCR measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool LoadCompensationEnabled { get; set; }

#### Remarks

Both [OpenCompensationEnabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-opencompensationenabled.html) and [ShortCompensationEnabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-shortcompensationenabled.html) must be set to true in order to set this property to true.

Use [OpenShortLoadCompensationDataSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-openshortloadcompensationdatasource.html) to define where the load compensation data that is applied to LCR measurements comes from.

Note

Load compensation data are applied only for those specific frequencies you define with [PerformLoadCompensation](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performloadcompensation__dcpowerlcrloadcompensationspot_arr1.html); load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

| True | Load LCR compensation data are applied. |
| --- | --- |
| False | Load LCR compensation data are not applied. |

The default value is false.

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-opensusceptance.html language=enus -->
## TOPIC 00185: OpenSusceptance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-opensusceptance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-opensusceptance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the susceptance, in siemens, of the circuit used for open LCR compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double OpenSusceptance { get; set; }RemarksThis property applies when OpenShortLoadCompensationDataSource is set to AsDefined.This property is

### OpenSusceptance

Specifies the susceptance, in siemens, of the circuit used for open LCR compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double OpenSusceptance { get; set; }

#### Remarks

This property applies when [OpenShortLoadCompensationDataSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-openshortloadcompensationdatasource.html) is set to **AsDefined**.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is **0.0**.

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performloadcompensation__dcpowerlcrloadcompensationspot_arr1.html language=enus -->
## TOPIC 00186: PerformLoadCompensation(DCPowerLCRLoadCompensationSpot[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performloadcompensation__dcpowerlcrloadcompensationspot_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performloadcompensation__dcpowerlcrloadcompensationspot_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates load compensation data for LCR measurements for the test spots you specify. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void PerformLoadCompensation(DCPowerLCRLoadCompensationSpot[] spots)RemarksYou must physically configure your LCR circuit with an appropriate

### PerformLoadCompensation(DCPowerLCRLoadCompensationSpot[])

Generates load compensation data for LCR measurements for the test *spots*  you specify.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void PerformLoadCompensation(DCPowerLCRLoadCompensationSpot[] spots)

#### Remarks

You must physically configure your LCR circuit with an appropriate reference load to use this method to generate valid load compensation data.

Note

- The load compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

To apply the load compensation data you generate with this method to your LCR measurements, set [LoadCompensationEnabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-loadcompensationenabled.html) to true.

Note

Load compensation data are generated only for those specific frequencies you define with this method; load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| spots | DCPowerLCRLoadCompensationSpot[] | Defines the DCPowerLCRLoadCompensationSpot array to use for LCR load compensation. You can specify <=1000 spot frequencies. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencompensation__double_arr1.html language=enus -->
## TOPIC 00187: PerformOpenCompensation(double[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencompensation__double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencompensation__double_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void PerformOpenCompensation(double[] frequencies)RemarksYou must physical

### PerformOpenCompensation(double[])

Generates open compensation data for LCR measurements based on a default set of test *frequencies*  and, optionally, additional frequencies you can specify.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void PerformOpenCompensation(double[] frequencies)

#### Remarks

You must physically configure an open LCR circuit to use this method to generate valid open compensation data.

Note

- The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

To apply the open compensation data you generate with this method to your LCR measurements, set [OpenCompensationEnabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-opencompensationenabled.html) to true.

Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Open Compensation Frequencies**

By default, NI-DCPower uses the following frequencies for LCR open compensation:

- 10 logarithmic steps at 1 kHz frequency decade
- 10 logarithmic steps at 10 kHz frequency decade
- 100 logarithmic steps at 100 kHz frequency decade
- 100 logarithmic steps at 1 MHz frequency decade

Note

The actual frequencies used depend on the bandwidth of your instrument.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| frequencies | double[] | Defines a System.Double array of further frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencustomcablecompensation.html language=enus -->
## TOPIC 00188: PerformOpenCustomCableCompensation()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencustomcablecompensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performopencustomcablecompensation.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates open custom cable compensation data for LCR measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void PerformOpenCustomCableCompensation()RemarksTo use this method, you must physically configure an open LCR circuit to generate valid open custom cable compen

### PerformOpenCustomCableCompensation()

Generates open custom cable compensation data for LCR measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void PerformOpenCustomCableCompensation()

#### Remarks

To use this method, you must physically configure an open LCR circuit to generate valid open custom cable compensation data.

Note

- The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performshortcompensation__double_arr1.html language=enus -->
## TOPIC 00189: PerformShortCompensation(double[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performshortcompensation__double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-performshortcompensation__double_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void PerformShortCompensation(double[] frequencies)RemarksYou must physic

### PerformShortCompensation(double[])

Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional *frequencies*  you can specify.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void PerformShortCompensation(double[] frequencies)

#### Remarks

You must physically configure your LCR circuit with a short to use this method to generate valid short compensation data.

Note

- The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

To apply the short compensation data you generate with this method to your LCR measurements, set [ShortCompensationEnabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-shortcompensationenabled.html) to true.

Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Short Compensation Frequencies**

By default, NI-DCPower uses the following frequencies for LCR short compensation:

- 10 logarithmic steps at 1 kHz frequency decade
- 10 logarithmic steps at 10 kHz frequency decade
- 100 logarithmic steps at 100 kHz frequency decade
- 100 logarithmic steps at 1 MHz frequency decade

Note

The actual frequencies used depend on the bandwidth of your instruments.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| frequencies | double[] | Defines a System.Double array of further frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-shortresistance.html language=enus -->
## TOPIC 00190: ShortResistance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-shortresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-shortresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance, in ohms, of the circuit used for short LCR compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double ShortResistance { get; set; }RemarksThis property applies when OpenShortLoadCompensationDataSource is set to AsDefined.This property is no

### ShortResistance

Specifies the resistance, in ohms, of the circuit used for short LCR compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double ShortResistance { get; set; }

#### Remarks

This property applies when [OpenShortLoadCompensationDataSource](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation-openshortloadcompensationdatasource.html) is set to **AsDefined**.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is **0.0**.

Parent topic:

DCPowerOutputLCRCompensation Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation.html language=enus -->
## TOPIC 00191: DCPowerOutputLCRCompensation Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputlcrcompensation.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties related to NI-DCPower LCR compensation-specific operations. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputLCRCompensation : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs

### DCPowerOutputLCRCompensation Class

Contains properties related to NI-DCPower LCR compensation-specific operations.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputLCRCompensation : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AcElectricalCableLengthDelay | Specifies the one-way electrical length delay of the cable, in seconds. |
| ActualLoadReactance | Specifies the actual reactance, in ohms, of the load used for load LCR compensation. |
| ActualLoadResistance | Specifies the actual resistance, in ohms, of the load used for load LCR compensation. |
| LoadCompensationEnabled | Specifies whether to apply load LCR compensation data to LCR measurements. |
| MeasuredLoadReactance | Specifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument. |
| MeasuredLoadResistance | Specifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument. |
| OpenCompensationEnabled | Specifies whether to apply open LCR compensation data to LCR measurements. |
| OpenConductance | Specifies the conductance, in siemens, of the circuit used for open LCR compensation. |
| OpenShortLoadCompensationDataSource | Specifies the source of the LCR compensation data NI-DCPower applies to LCR measurements. |
| OpenSusceptance | Specifies the susceptance, in siemens, of the circuit used for open LCR compensation. |
| ShortCompensationEnabled | Specifies whether to apply short LCR compensation data to LCR measurements. |
| ShortCustomCableCompensationEnabled | Defines how to apply short custom cable compenation in LCR mode when CableLength is set to CustomOnboardStorage or CustomAsConfigured. |
| ShortReactance | Specifies the reactance, in ohms, of the circuit used for short LCR compensation. |
| ShortResistance | Specifies the resistance, in ohms, of the circuit used for short LCR compensation. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureCompensation(byte[]) | Applies previously generated open, short, load, as well as open and short custom cable compensationData to LCR measurements. |
| GetCompensationData() | Returns previously generated open, short, load, and custom cable compensation data that you can apply to LCR measurements with ConfigureCompensation(byte[]). |
| GetCompensationLastDateAndTime(DCPowerLCRCompensationType) | Returns the date and time the specified type of compensation data for LCR measurements was most recently generated. |
| PerformLoadCompensation(DCPowerLCRLoadCompensationSpot[]) | Generates load compensation data for LCR measurements for the test spots you specify. |
| PerformOpenCompensation(double[]) | Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify. |
| PerformOpenCustomCableCompensation() | Generates open custom cable compensation data for LCR measurements. |
| PerformShortCompensation(double[]) | Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify. |
| PerformShortCustomCableCompensation() | Generates short custom cable compensation data for LCR measurements. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-delay.html language=enus -->
## TOPIC 00192: Delay

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-delay.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time to delay the generation of the MeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic PrecisionTimeSpan Delay { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topi

### Delay

Gets or sets the amount of time to delay the generation of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public PrecisionTimeSpan Delay { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies a PrecisionTimeSpan that represents the amount of time, to delay the generation of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputMeasureCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-outputbehavior.html language=enus -->
## TOPIC 00193: OutputBehavior

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-outputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-outputbehavior.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output behavior of the MeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventOutputBehavior OutputBehavior { get; set; }RemarksSpecifies the DCPowerEventOutputBehavior for exporting the MeasureCompleteEvent event.This property is n

### OutputBehavior

Gets or sets the output behavior of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventOutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html) OutputBehavior { get; set; }

#### Remarks

Specifies the [DCPowerEventOutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html) for exporting the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html) event.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerOutputMeasureCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-outputterminal.html language=enus -->
## TOPIC 00194: OutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-outputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output terminal for exporting the MeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasureCompleteEventOutputTerminal OutputTerminal { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Prop

### OutputTerminal

Gets or sets the output terminal for exporting the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) OutputTerminal { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerMeasureCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventoutputterminal.html) value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| System.ArgumentNullException | The property was set with a null output terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputMeasureCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-pulse.html language=enus -->
## TOPIC 00195: Pulse

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-pulse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse characteristics of the MeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputMeasureCompleteEventPulse Pulse { get; }RemarksReturns a DCPowerMeasureCompleteEventPulse that is used to configure the pulse characteristics of the Measur

### Pulse

Gets the pulse characteristics of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputMeasureCompleteEventPulse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteeventpulse.html) Pulse { get; }

#### Remarks

Returns a [DCPowerMeasureCompleteEventPulse](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurecompleteeventpulse.html) that is used to configure the pulse characteristics of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

Parent topic:

DCPowerOutputMeasureCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-toggle.html language=enus -->
## TOPIC 00196: Toggle

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-toggle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteevent-toggle.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets and sets the toggle initial state characteristics of the MeasureCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputMeasureCompleteEventToggle Toggle { get; set; }RemarksReturns a DCPowerOutputMeasureCompleteEventToggle that is used to configure t

### Toggle

Gets and sets the toggle initial state characteristics of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputMeasureCompleteEventToggle](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteeventtoggle.html) Toggle { get; set; }

#### Remarks

Returns a [DCPowerOutputMeasureCompleteEventToggle](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurecompleteeventtoggle.html) that is used to configure the toggle characteristics of the [MeasureCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-measurecompleteevent.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerOutputMeasureCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger-configuresoftwareedgetrigger.html language=enus -->
## TOPIC 00197: ConfigureSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger-configuresoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger-configuresoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the MeasureTrigger for software edge triggering for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ConfigureSoftwareEdgeTrigger()RemarksThis method cannot be called for channels that are in the Running state. Refer to the Programming

### ConfigureSoftwareEdgeTrigger()

Configures the [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-measuretrigger.html) for software edge triggering for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ConfigureSoftwareEdgeTrigger()

#### Remarks

Note

This method cannot be called for channels that are in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputMeasureTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger-exportedoutputterminal.html language=enus -->
## TOPIC 00198: ExportedOutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger-exportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger-exportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the MeasureTrigger exported output terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasureTriggerExportedOutputTerminal ExportedOutputTerminal { get; set; }RemarksSpecify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instr

### ExportedOutputTerminal

Gets or sets the [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-measuretrigger.html) exported output terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html) ExportedOutputTerminal { get; set; }

#### Remarks

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerMeasureTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretriggerexportedoutputterminal.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputMeasureTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger.html language=enus -->
## TOPIC 00199: DCPowerOutputMeasureTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasuretrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure the MeasureTrigger for NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputMeasureTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplie

### DCPowerOutputMeasureTrigger Class

Represents the methods and properties used to configure the [MeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-measuretrigger.html) for NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputMeasureTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerOutputDigitalEdgeMeasureTrigger sub-object to configure the device to wait for digital edge MeasureTrigger. |
| ExportedOutputTerminal | Gets or sets the MeasureTrigger exported output terminal. |
| Type | Gets or sets the MeasureTrigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the MeasureTrigger for software edge triggering for the specified channel(s). |
| SendSoftwareEdgeTrigger() | Asserts the MeasureTrigger for software triggering. This method can override an external edge trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent-outputterminal.html language=enus -->
## TOPIC 00200: OutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent-outputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output terminal for exporting the PulseCompleteEvent. Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened termina

### OutputTerminal

Gets or sets the output terminal for exporting the [PulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-pulsecompleteevent.html). Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) OutputTerminal { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| System.ArgumentNullException | The property was set with a null output terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputPulseCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent-pulse.html language=enus -->
## TOPIC 00201: Pulse

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent-pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent-pulse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse characteristics of the PulseCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputPulseCompleteEventPulse Pulse { get; }RemarksReturns a DCPowerOutputPulseCompleteEventPulse that is used to configure the pulse characteristics of the PulseC

### Pulse

Gets the pulse characteristics of the [PulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-pulsecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputPulseCompleteEventPulse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteeventpulse.html) Pulse { get; }

#### Remarks

Returns a [DCPowerOutputPulseCompleteEventPulse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteeventpulse.html) that is used to configure the pulse characteristics of the [PulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-pulsecompleteevent.html).

Parent topic:

DCPowerOutputPulseCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent.html language=enus -->
## TOPIC 00202: DCPowerOutputPulseCompleteEvent Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsecompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the underlying hardware PulseCompleteEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputPulseCompleteEvent : DCPowerSubObjectRemarksFor more information about events, refer to NI DC

### DCPowerOutputPulseCompleteEvent Class

Represents the properties used to configure the underlying hardware [PulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-pulsecompleteevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputPulseCompleteEvent : DCPowerSubObject

#### Remarks

For more information about events, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| OutputTerminal | Gets or sets the output terminal for exporting the PulseCompleteEvent. Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. |
| Pulse | Gets the pulse characteristics of the PulseCompleteEvent. |

#### Methods

| Name | Description |
| --- | --- |
| WaitForEvent(NationalInstruments.PrecisionTimeSpan) | Waits until the specified channel(s) have generated the PulseCompleteEvent. The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the Initiate method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-disable.html language=enus -->
## TOPIC 00203: Disable()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-disable.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the PulseTrigger The specified channel(s) do not wait for a Pulse trigger when starting generation or acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Disable()RemarksThis method is necessary only if you configured a PulseTrigger in the past and now

### Disable()

Disables the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-pulsetrigger.html) The specified channel(s) do not wait for a Pulse trigger when starting generation or acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Disable()

#### Remarks

PulseTrigger

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputPulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00204: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the StartTrigger for software triggering. This method can override an external edge trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method is not supported by all instruments. Refer to the Supported Functions by Devic

### SendSoftwareEdgeTrigger()

Asserts the [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html) for software triggering. This method can override an external edge trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputPulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger.html language=enus -->
## TOPIC 00205: DCPowerOutputPulseTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputpulsetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure the PulseTrigger for NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputPulseTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies an

### DCPowerOutputPulseTrigger Class

Represents the methods and properties used to configure the [PulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-pulsetrigger.html) for NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputPulseTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerOutputDigitalEdgePulseTrigger sub-object to configure the device to wait for digital edge PulseTrigger. |
| ExportedOutputTerminal | Gets or sets the PulseTrigger exported output terminal. |
| Type | Gets or sets the PulseTrigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the PulseTrigger for software edge triggering for the specified channel(s). |
| Disable() | Disables the PulseTrigger The specified channel(s) do not wait for a Pulse trigger when starting generation or acquisition. |
| SendSoftwareEdgeTrigger() | Asserts the StartTrigger for software triggering. This method can override an external edge trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggerevent-waitforevent__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00206: WaitForEvent(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggerevent-waitforevent__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggerevent-waitforevent__nationalinstruments.precisiontimespan.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the specified channel(s) have generated the ReadyForPulseTriggerEvent. The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the Initiate method was called. If an event has only been generated once, and

### WaitForEvent(NationalInstruments.PrecisionTimeSpan)

Waits until the specified channel(s) have generated the [ReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-readyforpulsetriggerevent.html). The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-initiate.html) method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void WaitForEvent(NationalInstruments.PrecisionTimeSpan timeout)

#### Remarks

Note

This method must only be called when the specified channel(s) are in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete, in seconds. If the method does not complete within this time interval, NI-DCPower returns an error. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputReadyForPulseTriggerEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggereventpulse-polarity.html language=enus -->
## TOPIC 00207: Polarity

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggereventpulse-polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggereventpulse-polarity.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the behavior of the DCPowerOutputReadyForPulseTriggerEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulsePolarity Polarity { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topic in t

### Polarity

Gets or sets the behavior of the [DCPowerOutputReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggerevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) Polarity { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputReadyForPulseTriggerEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggereventpulse.html language=enus -->
## TOPIC 00208: DCPowerOutputReadyForPulseTriggerEventPulse Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggereventpulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputreadyforpulsetriggereventpulse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the pulse of ReadyForPulseTriggerEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputReadyForPulseTriggerEventPulse : DCPowerSubObjectRemarksFor more information, refer to NI DC Powe

### DCPowerOutputReadyForPulseTriggerEventPulse Class

Represents the properties used to configure the pulse of [ReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-readyforpulsetriggerevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputReadyForPulseTriggerEventPulse : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Polarity | Gets or sets the behavior of the DCPowerOutputReadyForPulseTriggerEvent. |
| Width | Gets or sets the width, in seconds, of the DCPowerOutputReadyForPulseTriggerEvent event pulse. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-digitaledge.html language=enus -->
## TOPIC 00209: DigitalEdge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-digitaledge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputDigitalEdgeSequenceAdvanceTrigger sub-object to configure the device to wait for digital edge SequenceAdvanceTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputDigitalEdgeSequenceAdvanceTrigger DigitalEdge { get; }RemarksReturns an obj

### DigitalEdge

Gets the [DCPowerOutputDigitalEdgeSequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesequenceadvancetrigger.html) sub-object to configure the device to wait for digital edge [SequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sequenceadvancetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputDigitalEdgeSequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesequenceadvancetrigger.html) DigitalEdge { get; }

#### Remarks

Returns an object of type [DCPowerOutputDigitalEdgeSequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesequenceadvancetrigger.html).

Parent topic:

DCPowerOutputSequenceAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-disable.html language=enus -->
## TOPIC 00210: Disable()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-disable.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the SequenceAdvanceTrigger. The specified channel(s) do not wait for a Sequence Advance trigger before advancing to the next part of the sequence. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Disable()RemarksThis method is necessary only if you configured a S

### Disable()

Disables the [SequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sequenceadvancetrigger.html). The specified channel(s) do not wait for a Sequence Advance trigger before advancing to the next part of the sequence.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Disable()

#### Remarks

SequenceAdvanceTrigger

Note

This method cannot be called in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSequenceAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-type.html language=enus -->
## TOPIC 00211: Type

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger-type.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the SequenceAdvanceTrigger type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSequenceAdvanceTriggerType Type { get; set; }RemarksRefer to the Configure Triggers and Events topic in your instrument user manual for more information about triggers and eve

### Type

Gets or sets the [SequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sequenceadvancetrigger.html) type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSequenceAdvanceTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggertype.html) Type { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerSequenceAdvanceTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggertype.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSequenceAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceenginedoneevent.html language=enus -->
## TOPIC 00212: DCPowerOutputSequenceEngineDoneEvent Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceenginedoneevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceenginedoneevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the underlying hardware SequenceEngineDoneEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSequenceEngineDoneEvent : DCPowerSubObjectRemarksFor more information, refer to NI DC Po

### DCPowerOutputSequenceEngineDoneEvent Class

Represents the properties used to configure the underlying hardware [SequenceEngineDoneEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sequenceenginedoneevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSequenceEngineDoneEvent : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| OutputBehavior | Gets or sets the output behavior of the SequenceEngineDoneEvent |
| OutputTerminal | Gets or sets the output terminal for exporting the SequenceEngineDoneEvent. |
| Pulse | Gets the pulse characteristics of the SequenceEngineDoneEvent. |
| Toggle | Gets and sets toggle characteristics of the SequenceEngineDoneEvent. |

#### Methods

| Name | Description |
| --- | --- |
| WaitForEvent(NationalInstruments.PrecisionTimeSpan) | Waits until the specified channel(s) have generated the SequenceEngineDoneEvent. The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the Initiate method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceiterationcompleteeventpulse-polarity.html language=enus -->
## TOPIC 00213: Polarity

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceiterationcompleteeventpulse-polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceiterationcompleteeventpulse-polarity.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the behavior of the SequenceIterationCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulsePolarity Polarity { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topic in the NI DC

### Polarity

Gets or sets the behavior of the [SequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sequenceiterationcompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) Polarity { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSequenceIterationCompleteEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger.html language=enus -->
## TOPIC 00214: DCPowerOutputShutdownTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure the ShutdownTrigger for NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputShutdownTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Suppl

### DCPowerOutputShutdownTrigger Class

Represents the methods and properties used to configure the [ShutdownTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-shutdowntrigger.html) for NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputShutdownTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerOutputDigitalEdgeShutdownTrigger sub-object to configure the device to wait for digital edge ShutdownTrigger. |
| Type | Gets or sets the ShutdownTrigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the ShutdownTrigger for software triggering. |
| Disable() | Disables the ShutdownTrigger. |
| SendSoftwareEdgeTrigger() | Asserts the ShutdownTrigger for software triggering. This method can override an external edge trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-constantpower.html language=enus -->
## TOPIC 00215: ConstantPower

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-constantpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-constantpower.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel settings when the channel is configured for the ConstantPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceConstantPower ConstantPower { get; }RemarksReturns an object of type DCPowerOutputSourceConstantPower.

### ConstantPower

Specifies the channel settings when the channel is configured for the [ConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower.html) ConstantPower { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower.html).

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-constantresistance.html language=enus -->
## TOPIC 00216: ConstantResistance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-constantresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-constantresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel settings when the channel is configured for the ConstantResistance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceConstantResistance ConstantResistance { get; }RemarksReturns an object of type DCPowerOutputSourceConstantResistance.

### ConstantResistance

Specifies the channel settings when the channel is configured for the [ConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance.html) ConstantResistance { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance.html).

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-mode.html language=enus -->
## TOPIC 00217: Mode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-mode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to run a single output point or a sequence for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceMode Mode { get; set; }RemarksRefer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Su

### Mode

Gets or sets whether to run a single output point or a sequence for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceMode](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) Mode { get; set; }

#### Remarks

Refer to the [Single Point Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_singlept) and [Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing) topics in the *NI DC Power Supplies and SMUs Help* for more information about source modes.

Note

If you specify a channel name when accessing this property, the session must be initialized with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is [SinglePoint](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-outputshorted.html language=enus -->
## TOPIC 00218: OutputShorted

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-outputshorted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-outputshorted.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the input of the instrument simulates a short circuit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool OutputShorted { get; set; }RemarksWhen this property is set to true, the electronic load will simulate a short circuit across the channel/input termin

### OutputShorted

Specifies whether the input of the instrument simulates a short circuit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool OutputShorted { get; set; }

#### Remarks

- When this property is set to true, the electronic load will simulate a short circuit across the channel/input terminals. The electronic load uses the maximum rated current and range to simulate the short circuit. This property will only take effect when both [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) and [Connected](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-connected.html) are true.
- When this property is set to false, the instrument will resume normal operation based on its existing settings on the specified channel(s).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-ovpenabled.html language=enus -->
## TOPIC 00219: OvpEnabled

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-ovpenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-ovpenabled.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to enable or disable overvoltage protection (OVP). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool OvpEnabled { get; set; }RemarksThe default value is true. This property is not supported by all instruments. Refer to the Supported Properties by Devic

### OvpEnabled

Gets or sets whether to enable or disable overvoltage protection (OVP).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool OvpEnabled { get; set; }

#### Remarks

The default value is true.

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was set to true in a session to unsupported hardware. |
| Ivi.Driver.SelectorNameRequiredException | The property was accessed in a multi-channel session without specifying a channel. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel or a badly-formed channel string. |

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulsecurrent.html language=enus -->
## TOPIC 00220: PulseCurrent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulsecurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulsecurrent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel settings when the channel is configured for the PulseCurrent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourcePulseCurrent PulseCurrent { get; }RemarksReturns an object of type DCPowerOutputSourcePulseCurrent.

### PulseCurrent

Gets the channel settings when the channel is configured for the [PulseCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourcePulseCurrent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent.html) PulseCurrent { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourcePulseCurrent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent.html).

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulseontime.html language=enus -->
## TOPIC 00221: PulseOnTime

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulseontime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulseontime.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the length, in seconds, of the on phase of a pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double PulseOnTime { get; set; }RemarksReturns a double value that determines the length, in seconds, of the on phase of a pulse. This property is not supported by

### PulseOnTime

Gets or sets the length, in seconds, of the on phase of a pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double PulseOnTime { get; set; }

#### Remarks

Returns a double value that determines the length, in seconds, of the on phase of a pulse.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulsevoltage.html language=enus -->
## TOPIC 00222: PulseVoltage

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulsevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-pulsevoltage.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel settings when the channel is configured for the PulseVoltage. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourcePulseVoltage PulseVoltage { get; }RemarksReturns an object of type DCPowerOutputSourcePulseVoltage.

### PulseVoltage

Gets the channel settings when the channel is configured for the [PulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourcePulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage.html) PulseVoltage { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourcePulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage.html).

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-queryvoltagelevelmax__double.html language=enus -->
## TOPIC 00223: QueryVoltageLevelMax(double)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-queryvoltagelevelmax__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-queryvoltagelevelmax__double.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the maximum voltage level on a channel if you set the channel to the specified currentLimit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double QueryVoltageLevelMax(double currentLimit)ParametersNameTypeDescriptioncurrentLimitdoubleSpecifies the current limit to u

### QueryVoltageLevelMax(double)

Queries the maximum voltage level on a channel if you set the channel to the specified currentLimit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double QueryVoltageLevelMax(double currentLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| currentLimit | double | Specifies the current limit to use when calculating the maximum voltage level. |

#### Returns

Returns the maximum voltage level that can be set on a channel with the specified currentLimit.

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sequenceloopcount.html language=enus -->
## TOPIC 00224: SequenceLoopCount

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sequenceloopcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sequenceloopcount.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of times a sequence is run after initiation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic int SequenceLoopCount { get; set; }RemarksRefer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequ

### SequenceLoopCount

Gets or sets the number of times a sequence is run after initiation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public int SequenceLoopCount { get; set; }

#### Remarks

Sequence Source Mode

NI DC Power Supplies and SMUs Help

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

The default value is 1.

Valid values range from 1 to 2147483647.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1-nationalinstruments.precisiontimespan_arr1.html language=enus -->
## TOPIC 00225: SetSequence(double[], NationalInstruments.PrecisionTimeSpan[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1-nationalinstruments.precisiontimespan_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1-nationalinstruments.precisiontimespan_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a series of voltage or current outputs and corresponding source delays. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SetSequence(double[] values, NationalInstruments.PrecisionTimeSpan[] sourceDelays)RemarksThe source mode must be set to Sequence for this me

### SetSequence(double[], NationalInstruments.PrecisionTimeSpan[])

Configures a series of voltage or current outputs and corresponding source delays.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SetSequence(double[] values, NationalInstruments.PrecisionTimeSpan[] sourceDelays)

#### Remarks

The source mode must be set to [Sequence](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) for this method to take effect.

Use this method in the Uncommitted or Committed programming states. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Using this method with Advanced Sequence methods for the same channel in the same session is not supported.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The valid values for this parameter are defined by the voltage level range or current level range.

**Valid Values:**

For the PXIe-4051, 0 to 39 seconds.

For the PXIe-4147, 0 to 26.5 seconds.

For the PXIe-4151, 0 to 42 seconds.

For the PXIe-4162/4163 and PXIe-4190, 0 to 23 seconds.

For all other supported instruments, 0 to 167 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| values | double[] | Specifies the series of voltage levels or current levels, depending on the configured output method. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceDelays | NationalInstruments.PrecisionTimeSpan[] | Specifies the source delay, in seconds, that follows the configuration of each value in the sequence. |

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1.html language=enus -->
## TOPIC 00226: SetSequence(double[])

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a series of voltage, current, resistance or power outputs and corresponding source delays. The source mode must be set to Sequence for this method to take effect. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SetSequence(double[] values)RemarksUse this metho

### SetSequence(double[])

Configures a series of voltage, current, resistance or power outputs and corresponding source delays. The source mode must be set to [Sequence](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) for this method to take effect.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SetSequence(double[] values)

#### Remarks

Use this method in the Uncommitted or Committed programming states. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for more information about NI-DCPower programming states.

Using this method with Advanced Sequence methods for the same channel in the same session is not supported.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The valid values for this parameter are defined by the voltage level range, current level range, constant resistance level range or constant power level range.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| values | double[] | Specifies the series of voltage, current, resistance or power levels, depending on the configured output method. |

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sourcedelay.html language=enus -->
## TOPIC 00227: SourceDelay

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sourcedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sourcedelay.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time, in seconds, when the device generates the SourceCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NationalInstruments.PrecisionTimeSpan SourceDelay { get; set; }RemarksValid Values:For the PXIe-4051, 0 to 39 seconds.For the PXIe-4147, 0 to

### SourceDelay

Gets or sets the time, in seconds, when the device generates the [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sourcecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NationalInstruments.PrecisionTimeSpan SourceDelay { get; set; }

#### Remarks

**Valid Values:**

For the PXIe-4051, 0 to 39 seconds.

For the PXIe-4147, 0 to 26.5 seconds.

For the PXIe-4151, 0 to 42 seconds.

For the PXIe-4162/4163 and PXIe-4190, 0 to 23 seconds.

For all other supported instruments, 0 to 167 seconds.

The default value is 0.01667.

SourceCompleteEvent

DCPowerMeasurementWhen

AutomaticallyAfterSourceComplete

Single Point Source Mode

Sequence Source Mode

NI DC Power Supplies and SMUs Help

Note

The NI PXI-4110 and NI PXI-4130 do not support this property.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html language=enus -->
## TOPIC 00228: TransientResponse

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the transient response. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceTransientResponse TransientResponse { get; set; }RemarksThe default value is Normal. This property is not supported by all instruments. Refer to the Supported Properties by Devic

### TransientResponse

Gets or sets the transient response.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceTransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) TransientResponse { get; set; }

#### Remarks

The default value is [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-voltage.html language=enus -->
## TOPIC 00229: Voltage

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-voltage.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputSourceVoltage sub-object used to configure the Voltage properties of source unit channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceVoltage Voltage { get; }RemarksReturns an object of type DCPowerOutputSourceVoltage.

### Voltage

Gets the [DCPowerOutputSourceVoltage](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage.html) sub-object used to configure the Voltage properties of source unit channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceVoltage](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage.html) Voltage { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceVoltage](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage.html).

Parent topic:

DCPowerOutputSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource.html language=enus -->
## TOPIC 00230: DCPowerOutputSource Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source unit channel. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSource : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyAll members of this type are safe

### DCPowerOutputSource Class

Represents the source unit channel.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSource : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| ActualPowerAllocation | Gets the power, in watts, the device is sourcing on each active channel if the PowerAllocationMode property is set to Automatic or Manual. |
| AdvancedSequencing | Gets the DCPowerOutputSourceAdvancedSequencing sub-object used to configure the advanced sequence properties of the source unit channel. |
| ComplianceLimitSymmetry | Specifies whether compliance limits for current generation and voltage generation for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A. |
| ConductionVoltageMode | Specifies whether the conduction voltage feature is enabled on the specified channel(s). |
| ConductionVoltageOffThreshold | Specifies the minimum voltage, in volts, at the input of the specified channel(s) below which the instrument stops sinking on the specified channel(s) when the conduction voltage feature is enabled. |
| ConductionVoltageOnThreshold | Specifies the required minimum voltage, in volts, at the input of the specified channel(s) before the instrument starts sinking on the specified channel(s) when the conduction voltage feature is enabled. |
| ConstantPower | Specifies the channel settings when the channel is configured for the ConstantPower. |
| ConstantResistance | Specifies the channel settings when the channel is configured for the ConstantResistance. |
| Current | Gets the DCPowerOutputSourceCurrent sub-object used to configure the current properties of the source unit channel. |
| CustomTransientResponse | Gets the DCPowerOutputSourceCustomTransientResponse sub-object used to configure the custom transient response of the source unit channel. |
| IsSequenceLoopCountFinite | Gets or sets whether a sequence should repeat indefinitely. |
| MergedChannels | Gets or sets the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument. |
| Mode | Gets or sets whether to run a single output point or a sequence for the specified channel(s). |
| Output | Gets the DCPowerOutputSourceOutput sub-object used to configure the source unit channel output. |
| OutputCapacitance | Gets or sets whether to use a low or high capacitance on the output for the specified channel(s). |
| OutputCutoff | Gets the channel settings that define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected. |
| OutputShorted | Specifies whether the input of the instrument simulates a short circuit. |
| OverrangingEnabled | Gets or sets whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the device specification limits. |
| OvpEnabled | Gets or sets whether to enable or disable overvoltage protection (OVP). |
| OvpLimit | Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. For example, setting the OVP Limit to 65 will configure the OVP feature to trigger an OVP error if the output exceeds ±65 V. |
| PowerAllocationMode | Gets or sets whether the device sources the power its output configuration requires or a specific wattage you request; gets or sets whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device. |
| PulseBiasDelay | Gets or sets the time, in seconds, when the device generates the PulseCompleteEvent. |
| PulseCurrent | Gets the channel settings when the channel is configured for the PulseCurrent. |
| PulseOffTime | Gets or sets the length, in seconds, of the off phase of a pulse. |
| PulseOnTime | Gets or sets the length, in seconds, of the on phase of a pulse. |
| PulseVoltage | Gets the channel settings when the channel is configured for the PulseVoltage. |
| RequestedPowerAllocation | Gets or sets the power, in watts, to request the device to source from each active channel. |
| SequenceLoopCount | Gets or sets the number of times a sequence is run after initiation. |
| SequenceStepDeltaTime | Gets or sets the amount of time, in seconds, between the start of two consecutive steps in a sequence. |
| SequenceStepDeltaTimeEnabled | Gets or sets whether the SequenceStepDeltaTime property is enabled (true) or disabled (false). |
| SourceDelay | Gets or sets the time, in seconds, when the device generates the SourceCompleteEvent. |
| TransientResponse | Gets or sets the transient response. |
| Voltage | Gets the DCPowerOutputSourceVoltage sub-object used to configure the Voltage properties of source unit channel. |

#### Methods

| Name | Description |
| --- | --- |
| QueryCurrentLimitMax(double) | Queries the maximum current limit on a channel if the channel is set to the specified voltageLevel. |
| QueryCurrentLimitMin(double) | Queries the minimum current limit on a channel if the channel is set to the specified voltageLevel. |
| QueryVoltageLevelMax(double) | Queries the maximum voltage level on a channel if you set the channel to the specified currentLimit. |
| SetSequence(double[]) | Configures a series of voltage, current, resistance or power outputs and corresponding source delays. The source mode must be set to Sequence for this method to take effect. |
| SetSequence(double[], NationalInstruments.PrecisionTimeSpan[]) | Configures a series of voltage or current outputs and corresponding source delays. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-outputcapacitance.html language=enus -->
## TOPIC 00231: OutputCapacitance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-outputcapacitance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-outputcapacitance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use a low or high capacitance on the output for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceOutputCapacitance OutputCapacitance { get; set; }RemarksA value indicating whether to use a low or high capacitance on t

### OutputCapacitance

Specifies whether to use a low or high capacitance on the output for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceOutputCapacitance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputcapacitance.html) OutputCapacitance { get; set; }

#### Remarks

A value indicating whether to use a low or high capacitance on the output for the specified channel(s).

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments. Refer to the NI PXI-4130 Output Capacitance Selection topic for more information about capacitance.

Parent topic:

DCPowerOutputSourceAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-ovpenabled.html language=enus -->
## TOPIC 00232: OvpEnabled

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-ovpenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-ovpenabled.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to enable or disable overvoltage protection (OVP). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool OvpEnabled { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topic in the NI DC Power

### OvpEnabled

Gets or sets whether to enable or disable overvoltage protection (OVP).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool OvpEnabled { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

true, if OVP is enabled; false, if OVP is disabled. The default value is true

Parent topic:

DCPowerOutputSourceAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-sourcedelay.html language=enus -->
## TOPIC 00233: SourceDelay

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-sourcedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced-sourcedelay.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the MeasureWhen attribute is set to AutomaticallyAfterSourceComplete. Refer to the Single Point Source Mode and Sequence Source Mode topics for more information. Note: The NI PXI-4110 a

### SourceDelay

Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the [MeasureWhen](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementconfiguration-measurewhen.html) attribute is set to [AutomaticallyAfterSourceComplete](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurementwhen.html). Refer to the Single Point Source Mode and Sequence Source Mode topics for more information. Note: The NI PXI-4110 and NI PXI-4130 do not support this attribute.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double SourceDelay { get; set; }

#### Remarks

A value representing when, in seconds, the device generates the Source Complete event. **Valid Values:**

For the PXIe-4051, 0 to 39 seconds.

For the PXIe-4147, 0 to 26.5 seconds.

For the PXIe-4151, 0 to 42 seconds.

For the PXIe-4162/4163 and PXIe-4190, 0 to 23 seconds.

For all other supported instruments, 0 to 167 seconds.

The default value is 0.01667.

Parent topic:

DCPowerOutputSourceAdvanced Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced.html language=enus -->
## TOPIC 00234: DCPowerOutputSourceAdvanced Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvanced.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties for controlling the advanced features of the source unit. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceAdvanced : DCPowerSubObjectPropertiesNameDescriptionOutputCapacitanceSpecifies whether to use a low or hig

### DCPowerOutputSourceAdvanced Class

Properties for controlling the advanced features of the source unit.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceAdvanced : DCPowerSubObject

#### Properties

| Name | Description |
| --- | --- |
| OutputCapacitance | Specifies whether to use a low or high capacitance on the output for the specified channel(s). |
| OvpEnabled | Gets or sets whether to enable or disable overvoltage protection (OVP). |
| SourceDelay | Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the MeasureWhen attribute is set to AutomaticallyAfterSourceComplete. Refer to the Single Point Source Mode and Sequence Source Mode topics for more information. Note: The NI PXI-4110 and NI PXI-4130 do not support this attribute. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequence__string-dcpoweradvancedsequenceproperty_arr1-bool.html language=enus -->
## TOPIC 00235: CreateAdvancedSequence(string, DCPowerAdvancedSequenceProperty[], bool)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequence__string-dcpoweradvancedsequenceproperty_arr1-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequence__string-dcpoweradvancedsequenceproperty_arr1-bool.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty advanced sequence. Call the CreateAdvancedSequenceStep method to add steps to the active advanced sequence, or the CreateAdvancedSequenceCommitStep method to add a Commit step. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void CreateAdvancedSequence(string

### CreateAdvancedSequence(string, DCPowerAdvancedSequenceProperty[], bool)

Creates an empty advanced sequence. Call the [CreateAdvancedSequenceStep](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequencestep__bool.html) method to add steps to the active advanced sequence, or the [CreateAdvancedSequenceCommitStep](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequencecommitstep__bool.html) method to add a Commit step.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void CreateAdvancedSequence(string sequenceName, DCPowerAdvancedSequenceProperty[] properties, bool setAsActiveSequence)

#### Remarks

You can create mnultiple advanced sequences for a channel. Advanced sequences for a particular channel are independent from any advanced sequences of other channels. You can configure advanced sequences for one channel at a time or you can configure identical advanced sequences for multiple channels in unison.

Note

Each channel can have only one active advanced sequence at a time.

You must set the [Mode](nationalinstruments-modularinstruments-nidcpower-dcpowersource-mode.html) to [Sequence](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) to use this method. Refer to [DCPowerAdvancedSequenceProperty](nationalinstruments-modularinstruments-nidcpower-dcpoweradvancedsequenceproperty.html) for more information about supported properties.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Using the [SetSequence](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1.html) method with Advanced Sequence methods for the same channel in the same session is unsupported.

Use this method in the Uncommitted or Committed programming states. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for more information about NI-DCPower programming states.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequenceName | string | Specifies the name of the sequence to create. |
| properties | DCPowerAdvancedSequenceProperty[] | Specifies the properties you reconfigure per step in the advanced sequence. |
| setAsActiveSequence | bool | Specifies that the current sequence is active. |

Parent topic:

DCPowerOutputSourceAdvancedSequencing Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequencecommitstep__bool.html language=enus -->
## TOPIC 00236: CreateAdvancedSequenceCommitStep(bool)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequencecommitstep__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequencecommitstep__bool.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Commit step in the active advanced sequence. A Commit step configures the channels to a user-defined known state before starting the advanced sequence. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void CreateAdvancedSequenceCommitStep(bool setAsActiveStep)Remarks

### CreateAdvancedSequenceCommitStep(bool)

Creates a Commit step in the active advanced sequence. A Commit step configures the channels to a user-defined known state before starting the advanced sequence.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void CreateAdvancedSequenceCommitStep(bool setAsActiveStep)

#### Remarks

When you create an advanced sequence step or Commit step, each property you passed to [CreateAdvancedSequence](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequence__string-dcpoweradvancedsequenceproperty_arr1-bool.html) is reset to its default value for the new step. To configure the Commit step, you must first designate the Commit step as the active step by setting the [ActiveAdvancedSequenceStep](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-activeadvancedsequencestep.html) property to -1 or the *setAsActiveStep*  parameter of this method to true. Once the step is active, you can configure the properties for the step.

You must set the [Mode](nationalinstruments-modularinstruments-nidcpower-dcpowersource-mode.html) to [Sequence](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) to use this method. Refer to [DCPowerAdvancedSequenceProperty](nationalinstruments-modularinstruments-nidcpower-dcpoweradvancedsequenceproperty.html) for more information about supported properties.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Using the [SetSequence](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-setsequence__double_arr1.html) method with Advanced Sequence methods for the same channel in the same session is unsupported.

Function

PulseVoltage

PulseCurrent

**When Does the Commit Step Run in a Sequence?**

The driver applies the Commit step to the device when the session transitions to the Committed state. After the driver applies the Commit step to the device, the driver waits until the Source Delay has elpased before waiting for the Start trigger.

Note

- You can provide a specific [SourceDelay](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sourcedelay.html) for the Commit step if you set [SourceDelay](nationalinstruments-modularinstruments-nidcpower-dcpoweradvancedsequenceproperty.html) as one of the properties to be configured with [CreateAdvancedSequence](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing-createadvancedsequence__string-dcpoweradvancedsequenceproperty_arr1-bool.html).
- If you call [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html) while the device is in the Uncommitted state, the session implicitly moves through the Commited state before moving to the Running state.

**Differences Between the Commit Step and Other Steps**

- The source unit does not wait on any triggers before running the Commit step.
- The source unit does not emit a Source Complete Event when the Commit step is complete.
- No measurements are taken in the Commit step, therefore you cannot set the [ApertureTime](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-aperturetime.html), [RecordLength](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-recordlength.html), or [NoiseRejection](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputmeasurement-noiserejection.html) properties in the Commit step.
- The [SequenceStepDeltaTime](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-sequencestepdeltatime.html) property does not apply to the Commit step, and you cannot configure the SequenceStepDeltaTime property in the Commit step.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| setAsActiveStep | bool | Specifies that this current step in the active sequence is active. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called in a session to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSourceAdvancedSequencing Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing.html language=enus -->
## TOPIC 00237: DCPowerOutputSourceAdvancedSequencing Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceadvancedsequencing.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods and properties for configuring the source and measure unit with a series of property values. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceAdvancedSequencing : DCPowerSubObjectRemarksYou must set the Mode

### DCPowerOutputSourceAdvancedSequencing Class

Provides methods and properties for configuring the source and measure unit with a series of property values.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceAdvancedSequencing : DCPowerSubObject

#### Remarks

You must set the [Mode](nationalinstruments-modularinstruments-nidcpower-dcpowersource-mode.html) to [Sequence](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html). For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| ActiveAdvancedSequence | Gets or sets the advanced sequence to configure or generate. |
| ActiveAdvancedSequenceStep | Gets or sets the advanced sequence step to configure. |

#### Methods

| Name | Description |
| --- | --- |
| CreateAdvancedSequence(string, DCPowerAdvancedSequenceProperty[], bool) | Creates an empty advanced sequence. Call the CreateAdvancedSequenceStep method to add steps to the active advanced sequence, or the CreateAdvancedSequenceCommitStep method to add a Commit step. |
| CreateAdvancedSequenceCommitStep(bool) | Creates a Commit step in the active advanced sequence. A Commit step configures the channels to a user-defined known state before starting the advanced sequence. |
| CreateAdvancedSequenceStep(bool) | Creates a new advanced sequence step in the active advanced sequence, specified by the ActiveAdvancedSequence property. You can configure properties for the new step only after the step is created. |
| DeleteAdvancedSequence(string) | Deletes a previously created advanced sequence and all the advanced sequence steps in the advanced sequence. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-outputterminal.html language=enus -->
## TOPIC 00238: OutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-outputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output terminal for exporting the DCPowerOutputSourceCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceCompleteEventOutputTerminal OutputTerminal { get; set; }RemarksThis property is not supported by all instruments. Refer to the Sup

### OutputTerminal

Gets or sets the output terminal for exporting the [DCPowerOutputSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) OutputTerminal { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies an object of type OutputTerminal.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| System.ArgumentNullException | The property was set with a null output terminal. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSourceCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-waitforevent__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00239: WaitForEvent(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-waitforevent__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-waitforevent__nationalinstruments.precisiontimespan.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the specified channel(s) have generated the SourceCompleteEvent. The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the Initiate method was called. If an event has only been generated once, and you ca

### WaitForEvent(NationalInstruments.PrecisionTimeSpan)

Waits until the specified channel(s) have generated the [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html). The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-initiate.html) method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void WaitForEvent(NationalInstruments.PrecisionTimeSpan timeout)

#### Remarks

Note

This method must only be called when the specified channel(s) are in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete, in seconds. If the method does not complete within this time interval, NIDCPower returns an error. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSourceCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html language=enus -->
## TOPIC 00240: DCPowerOutputSourceCompleteEvent Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the underlying hardware SourceCompleteEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceCompleteEvent : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supp

### DCPowerOutputSourceCompleteEvent Class

Represents the properties used to configure the underlying hardware [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceCompleteEvent : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| OutputBehavior | Gets or sets the output behavior of the SourceCompleteEvent |
| OutputTerminal | Gets or sets the output terminal for exporting the DCPowerOutputSourceCompleteEvent. |
| Pulse | Gets the pulse characteristics of the SourceCompleteEvent. |
| Toggle | Gets and sets the toggle characteristics of the SourceCompleteEvent. |

#### Methods

| Name | Description |
| --- | --- |
| WaitForEvent(NationalInstruments.PrecisionTimeSpan) | Waits until the specified channel(s) have generated the SourceCompleteEvent. The session monitors whether each type of event has occurred at least once for the specified channel(s) since the last time this method or the Initiate method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventpulse-width.html language=enus -->
## TOPIC 00241: Width

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventpulse-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventpulse-width.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the width, in seconds, of the SourceCompleteEvent pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic PrecisionTimeSpan Width { get; set; }RemarksNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these corre

### Width

Gets or sets the width, in seconds, of the [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html) pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public PrecisionTimeSpan Width { get; set; }

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Parent topic:

DCPowerOutputSourceCompleteEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventtoggle-initialstate.html language=enus -->
## TOPIC 00242: InitialState

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventtoggle-initialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventtoggle-initialstate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial toggle state of the event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventToggleInitialState InitialState { get; set; }RemarksSpecifies the initial toggle state of the SourceCompleteEvent if you set the OutputBehavior to Toggle. NI-DCPower u

### InitialState

Specifies the initial toggle state of the event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventToggleInitialState](nationalinstruments-modularinstruments-nidcpower-dcpowereventtoggleinitialstate.html) InitialState { get; set; }

#### Remarks

Specifies the initial toggle state of the [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputevents-sourcecompleteevent.html) if you set the [OutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteevent-outputbehavior.html) to [Toggle](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html).

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerOutputSourceCompleteEventToggle Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventtoggle.html language=enus -->
## TOPIC 00243: DCPowerOutputSourceCompleteEventToggle Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventtoggle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecompleteeventtoggle.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the toggle for output source complete event. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceCompleteEventToggle : DCPowerSubObjectPropertiesNameDescriptionInitialStateSpecifies t

### DCPowerOutputSourceCompleteEventToggle Class

Represents the properties used to configure the toggle for output source complete event.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceCompleteEventToggle : DCPowerSubObject

#### Properties

| Name | Description |
| --- | --- |
| InitialState | Specifies the initial toggle state of the event. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-currentlimit.html language=enus -->
## TOPIC 00244: CurrentLimit

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-currentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-currentlimit.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentLimit { get; set; }RemarksThe valid values for this property are determined b

### CurrentLimit

Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLimit { get; set; }

#### Remarks

The valid values for this property are determined by the selected value for [LevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-levelrange.html).

Function

ConstantPower

ComplianceLimitSymmetry

Symmetric

The device will operate in Constant Current mode if the current exceeds the specified limit.

The channel must be enabled for the specified current limit to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceConstantPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-level.html language=enus -->
## TOPIC 00245: Level

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-level.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level, in watts, that the device attempts to generate on the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Level { get; set; }RemarksThe valid values for this property are determined by the selected value for LevelRange.This

### Level

Specifies the power level, in watts, that the device attempts to generate on the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Level { get; set; }

#### Remarks

The valid values for this property are determined by the selected value for [LevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-levelrange.html).

Function

ConstantPower

The channel must be enabled for the specified power level to take effect.

Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceConstantPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-levelrange.html language=enus -->
## TOPIC 00246: LevelRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-levelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower-levelrange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level range, in watts, for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double LevelRange { get; set; }RemarksFor valid ranges, refer to the specifications for your instrument.This property is applicable only if the Function pr

### LevelRange

Specifies the power level range, in watts, for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double LevelRange { get; set; }

#### Remarks

For valid ranges, refer to the specifications for your instrument.

Function

ConstantPower

The voltage range and current range used by the instrument are automatically determined by the selected power level range. For more information, refer to the specifications for your instrument.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceConstantPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower.html language=enus -->
## TOPIC 00247: DCPowerOutputSourceConstantPower Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantpower.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties that change channel settings when the channel is configured for ConstantPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceConstantPower : DCPowerSubObjectRemarksFor more information, refer to NI DC

### DCPowerOutputSourceConstantPower Class

Contains properties that change channel settings when the channel is configured for [ConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceConstantPower : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Properties

| Name | Description |
| --- | --- |
| CurrentLimit | Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s). |
| Level | Specifies the power level, in watts, that the device attempts to generate on the specified channel(s). |
| LevelRange | Specifies the power level range, in watts, for the specified channel(s). |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-currentlimit.html language=enus -->
## TOPIC 00248: CurrentLimit

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-currentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-currentlimit.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed when generating the desired resistance level on the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentLimit { get; set; }RemarksThe valid values for this property are determi

### CurrentLimit

Specifies the current limit, in amps, that the output cannot exceed when generating the desired resistance level on the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLimit { get; set; }

#### Remarks

The valid values for this property are determined by the selected value for [LevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-levelrange.html).

Function

ConstantResistance

ComplianceLimitSymmetry

Symmetric

The device will operate in Constant Current mode if the current exceeds the specified limit.

The channel must be enabled for the specified current limit to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceConstantResistance Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-level.html language=enus -->
## TOPIC 00249: Level

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-level.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance level, in ohms, that the device attempts to generate on the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Level { get; set; }RemarksThe valid values for this property are determined by the selected value for LevelRange.T

### Level

Specifies the resistance level, in ohms, that the device attempts to generate on the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Level { get; set; }

#### Remarks

The valid values for this property are determined by the selected value for [LevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-levelrange.html).

Function

ConstantResistance

The channel must be enabled for the specified resistance level to take effect.

Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceConstantResistance Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-levelrange.html language=enus -->
## TOPIC 00250: LevelRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-levelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance-levelrange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance level range, in ohms, for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double LevelRange { get; set; }RemarksThe range defines the valid values to which you can set the resistance level. For valid ranges, refer to the spec

### LevelRange

Specifies the resistance level range, in ohms, for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double LevelRange { get; set; }

#### Remarks

The range defines the valid values to which you can set the resistance level. For valid ranges, refer to the specifications for your instrument.

Function

ConstantResistance

The voltage range and current range used by the instrument are automatically determined by the selected resistance level range. For more information, refer to the specifications for your instrument.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceConstantResistance Class
