# NI DOCUMENT BUNDLE: ni-switch-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-switch-csharp-api-ref start=1 end=88 -->
<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-niswitch-dangerousgetinstrumenthandle.html language=enus -->
## TOPIC 00001: DangerousGetInstrumentHandle()

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-niswitch-dangerousgetinstrumenthandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-niswitch-dangerousgetinstrumenthandle.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the underlying instrument handle. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic IntPtr DangerousGetInstrumentHandle()ReturnsReturns an IntPtr representing the value of the underlying instrument handle. ExceptionsTypeDescriptionSystem.ObjectDisposedExcept

### DangerousGetInstrumentHandle()

Returns the value of the underlying instrument handle.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public IntPtr DangerousGetInstrumentHandle()

#### Returns

Returns an IntPtr representing the value of the underlying instrument handle.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DangerousGetInstrumentHandle method was accessed after the associated NISwitch object was disposed. |

Parent topic:

NISwitch Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-niswitch-driveroperation.html language=enus -->
## TOPIC 00002: DriverOperation

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-niswitch-driveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-niswitch-driveroperation.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a SwitchDriverOperation object that defines methods and properties for common operations on the NI-SWITCH driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic SwitchDriverOperation DriverOperation { get; }ReturnsReturns a SwitchDriverOperation object.

### DriverOperation

Gets a [SwitchDriverOperation](nationalinstruments-modularinstruments-niswitch-switchdriveroperation.html) object that defines methods and properties for common operations on the NI-SWITCH driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public [SwitchDriverOperation](nationalinstruments-modularinstruments-niswitch-switchdriveroperation.html) DriverOperation { get; }

#### Returns

Returns a [SwitchDriverOperation](nationalinstruments-modularinstruments-niswitch-switchdriveroperation.html) object.

Parent topic:

NISwitch Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-niswitch-getservice__type.html language=enus -->
## TOPIC 00003: GetService(Type)

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-niswitch-getservice__type.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-niswitch-getservice__type.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a service object on the basis of the type mentioned in the serviceType parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic object GetService(Type serviceType)ParametersNameTypeDescriptionserviceTypeTypeThe type of the object to be retrieved. ReturnsReturns an ob

### GetService(Type)

Returns a service object on the basis of the type mentioned in the serviceType parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public object GetService(Type serviceType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| serviceType | Type | The type of the object to be retrieved. |

#### Returns

Returns an object on the basis of the type mentioned in the serviceType parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetService method was accessed after the associated NISwitch object was disposed. |

Parent topic:

NISwitch Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchchannelcollection-this__string.html language=enus -->
## TOPIC 00004: this[string name]

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchchannelcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchchannelcollection-this__string.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SwitchChannel object which corresponds to the channel name used in the name parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic SwitchChannel this[string name] { get; }ParametersNameTypeDescriptionnamestringRepresents the name of the channel in the NI-SWITCH de

### this[string name]

Gets the [SwitchChannel](nationalinstruments-modularinstruments-niswitch-switchchannel.html) object which corresponds to the channel name used in the name parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public [SwitchChannel](nationalinstruments-modularinstruments-niswitch-switchchannel.html) this[string name] { get; }

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Represents the name of the channel in the NI-SWITCH device. |

#### Returns

Specifies a object of the type [SwitchChannel](nationalinstruments-modularinstruments-niswitch-switchchannel.html)

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | Returns the exception when the paramenter name passed is null. |
| System.ArgumentOutOfRangeException | Returns the exception when the name is not a valid channel name. |

Parent topic:

SwitchChannelCollection Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchcharacteristics-accurrentswitchingmax.html language=enus -->
## TOPIC 00005: ACCurrentSwitchingMax

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchcharacteristics-accurrentswitchingmax.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchcharacteristics-accurrentswitchingmax.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum AC current that the channel can switch. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic double ACCurrentSwitchingMax { get; }ReturnsSpecifies a Double to indicate the maximum AC current that the channel can switch. Returns the value, in Amperes RMS. Exceptions

### ACCurrentSwitchingMax

Gets the maximum AC current that the channel can switch.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public double ACCurrentSwitchingMax { get; }

#### Returns

Specifies a Double to indicate the maximum AC current that the channel can switch. 
 Returns the value, in Amperes RMS.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ACCurrentSwitchingMax was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchCharacteristics Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchcharacteristics-acpowercarrymax.html language=enus -->
## TOPIC 00006: ACPowerCarryMax

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchcharacteristics-acpowercarrymax.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchcharacteristics-acpowercarrymax.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum AC power that the channel can carry. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic double ACPowerCarryMax { get; }ReturnsSpecifies a Double to indicate the maximum AC power that the channel can carry. Returns the value, in volt-amperes. ExceptionsTypeDescrip

### ACPowerCarryMax

Gets the maximum AC power that the channel can carry.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public double ACPowerCarryMax { get; }

#### Returns

Specifies a Double to indicate the maximum AC power that the channel can carry. 
 Returns the value, in volt-amperes.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ACPowerCarryMax was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchCharacteristics Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchcharacteristics-dccurrentswitchingmax.html language=enus -->
## TOPIC 00007: DCCurrentSwitchingMax

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchcharacteristics-dccurrentswitchingmax.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchcharacteristics-dccurrentswitchingmax.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum DC current that the channel can switch. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic double DCCurrentSwitchingMax { get; }ReturnsSpecifies a Double to indicate the maximum DC current that the channel can switch. Returns the value, in amperes. ExceptionsType

### DCCurrentSwitchingMax

Gets the maximum DC current that the channel can switch.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public double DCCurrentSwitchingMax { get; }

#### Returns

Specifies a Double to indicate the maximum DC current that the channel can switch. 
 Returns the value, in amperes.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DCCurrentSwitchingMax was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchCharacteristics Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchcharacteristics.html language=enus -->
## TOPIC 00008: SwitchCharacteristics Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchcharacteristics.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchcharacteristics.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines properties used to obtain the characteristics of the NI-SWITCH device. These attributes are channel-based. The characteristics of all channels in a path determine the characteristics of the path. For example, the maximum current that a path can carry is the minimum of the maximum carry curre

### SwitchCharacteristics Class

Defines properties used to obtain the characteristics of the NI-SWITCH device. These attributes are channel-based. The characteristics of all channels in a path determine the characteristics of the path. For example, the maximum current that a path can carry is the minimum of the maximum carry currents of the individual switches in the path.

#### Derives from

- SwitchSubObject
- IIviSwtchCharacteristics

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchCharacteristics : SwitchSubObject, IIviSwtchCharacteristics

#### Remarks

For more information, refer to the [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| ACCurrentCarryMax | Gets the maximum AC current that the channel can carry. |
| ACCurrentSwitchingMax | Gets the maximum AC current that the channel can switch. |
| ACPowerCarryMax | Gets the maximum AC power that the channel can carry. |
| ACPowerSwitchingMax | Gets the maximum AC power the channel can switch. |
| ACVoltageMax | Gets the maximum AC voltage the channel can switch. |
| Bandwidth | Gets the bandwidth for the channel. |
| DCCurrentCarryMax | Gets the maximum DC current the channel can carry. |
| DCCurrentSwitchingMax | Gets the maximum DC current that the channel can switch. |
| DCPowerCarryMax | Gets the maximum DC power that the channel can carry. |
| DCPowerSwitchingMax | Gets the maximum DC power that the channel can switch. |
| DCVoltageMax | Gets the maximum DC voltage the channel can switch. |
| Impedance | Gets the characteristic impedance for the channel. |
| SettlingTime | Gets or sets the maximum length of time from after you make a connection until the signal flowing through the channel settles. The units are seconds. NOTE: If you use PXI-2501/2503/2565/2590/2591 the actual delay will always be the greater value of the SettlingTime and the value you specify as the Delay. |
| WireMode | Gets the wire mode of the switch device. This property affects the values of the NumberOfRows and NumberOfColumns attributes. The actual number of input and output lines on the switch device is fixed, but the number of channels depends on how many lines constitute each channel. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchcoercionwarningeventargs-text.html language=enus -->
## TOPIC 00009: Text

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchcoercionwarningeventargs-text.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchcoercionwarningeventargs-text.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string containing the description of the coercion event. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic string Text { get; }ReturnsReturns a string containing the description of the coercion.

### Text

Gets the string containing the description of the coercion event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public string Text { get; }

#### Returns

Returns a string containing the description of the coercion.

Parent topic:

SwitchCoercionWarningEventArgs Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11271wire64x1mux.html language=enus -->
## TOPIC 00010: Device11271Wire64x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11271wire64x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11271wire64x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1127 as a 1-wire 64x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11271Wire64x1Mux { get; }ReturnsReturns a S

### Device11271Wire64x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1127 as a 1-wire 64x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11271Wire64x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11272wire4x8matrix.html language=enus -->
## TOPIC 00011: Device11272Wire4x8Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11272wire4x8matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11272wire4x8matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1127 containing a 2-wire 4x8 matrix, while connecting your signals using the NI SCXI-1332 terminal block. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11272Wire4x8Matrix { get; }ReturnsReturns

### Device11272Wire4x8Matrix

Gets a value that indicates a topology which uses the NI SCXI-1127 containing a 2-wire 4x8 matrix, while connecting your signals using the NI SCXI-1332 terminal block.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11272Wire4x8Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device1127independent.html language=enus -->
## TOPIC 00012: Device1127Independent

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device1127independent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device1127independent.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI SCXI-1127 in the independent topology, while connecting your signals using the NI SCXI-1331 terminal block. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device1127Independent { get; }ReturnsReturns a String representing the t

### Device1127Independent

Gets a value that indicates the NI SCXI-1127 in the independent topology, while connecting your signals using the NI SCXI-1331 terminal block.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device1127Independent { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11282wire32x1mux.html language=enus -->
## TOPIC 00013: Device11282Wire32x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11282wire32x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11282wire32x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1128 as a 2-wire 32x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11282Wire32x1Mux { get; }ReturnsReturns a S

### Device11282Wire32x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1128 as a 2-wire 32x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11282Wire32x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11284wire16x1mux.html language=enus -->
## TOPIC 00014: Device11284Wire16x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11284wire16x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11284wire16x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1128 as a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11284Wire16x1Mux { get; }ReturnsReturns a String

### Device11284Wire16x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1128 as a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11284Wire16x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wire16x16matrix.html language=enus -->
## TOPIC 00015: Device11292Wire16x16Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wire16x16matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wire16x16matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the SCXI-1129 containing a 16x16 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11292Wire16x16Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device11292Wire16x16Matrix

Gets a value that indicates a topology which uses the SCXI-1129 containing a 16x16 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11292Wire16x16Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wire8x32matrix.html language=enus -->
## TOPIC 00016: Device11292Wire8x32Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wire8x32matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wire8x32matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the SCXI-1129 containing a 8x32 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11292Wire8x32Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device11292Wire8x32Matrix

Gets a value that indicates a topology which uses the SCXI-1129 containing a 8x32 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11292Wire8x32Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wiredual8x16matrix.html language=enus -->
## TOPIC 00017: Device11292WireDual8x16Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wiredual8x16matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11292wiredual8x16matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the SCXI-1129 containing two banks of 8x16 matrices. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11292WireDual8x16Matrix { get; }ReturnsReturns a String representing the topology of the device for the se

### Device11292WireDual8x16Matrix

Gets a value that indicates a topology which uses the SCXI-1129 containing two banks of 8x16 matrices.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11292WireDual8x16Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wire256x1mux.html language=enus -->
## TOPIC 00018: Device11301Wire256x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wire256x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wire256x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 256x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11301Wire256x1Mux { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device11301Wire256x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 256x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11301Wire256x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wire8x32matrix.html language=enus -->
## TOPIC 00019: Device11301Wire8x32Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wire8x32matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wire8x32matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 8x32 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11301Wire8x32Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device11301Wire8x32Matrix

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 8x32 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11301Wire8x32Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wireoctal32x1mux.html language=enus -->
## TOPIC 00020: Device11301WireOctal32x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wireoctal32x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wireoctal32x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire octal 32x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11301WireOctal32x1Mux { get; }ReturnsReturns a String representing the topology of the device for the sess

### Device11301WireOctal32x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire octal 32x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11301WireOctal32x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wiresixteen16x1mux.html language=enus -->
## TOPIC 00021: Device11301WireSixteen16x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wiresixteen16x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11301wiresixteen16x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1130 as sixteen independent 1-wire 16x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11301WireSixteen16x1Mux { get; }ReturnsReturns a String representing the topology of the devic

### Device11301WireSixteen16x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1130 as sixteen independent 1-wire 16x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11301WireSixteen16x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11302wire4x32matrix.html language=enus -->
## TOPIC 00022: Device11302Wire4x32Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11302wire4x32matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11302wire4x32matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 4x32 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11302Wire4x32Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device11302Wire4x32Matrix

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 4x32 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11302Wire4x32Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11304wire64x1mux.html language=enus -->
## TOPIC 00023: Device11304Wire64x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11304wire64x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device11304wire64x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 64x1 multiplexer. multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device11304Wire64x1Mux { get; }ReturnsReturns a String representing the topology of the device for t

### Device11304Wire64x1Mux

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 64x1 multiplexer. multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device11304Wire64x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device116016spdt.html language=enus -->
## TOPIC 00024: Device116016Spdt

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device116016spdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device116016spdt.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a the NI SCXI-1160 in the 16-SPDT general purpose topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device116016Spdt { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device116016Spdt

Gets a value that indicates a the NI SCXI-1160 in the 16-SPDT general purpose topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device116016Spdt { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device1169100spst.html language=enus -->
## TOPIC 00025: Device1169100Spst

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device1169100spst.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device1169100spst.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI SCXI-1169 in the 100-SPST topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device1169100Spst { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device1169100Spst

Gets a value that indicates the NI SCXI-1169 in the 100-SPST topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device1169100Spst { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25261wire158x1mux.html language=enus -->
## TOPIC 00026: Device25261Wire158x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25261wire158x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25261wire158x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value that indicates the NI PXIe-2526 1 wire 158x1 multiplexer topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25261Wire158x1Mux { get; }ReturnsThe value that indicates the NI PXIe-2526 1 wire 158x1 multiplexer topology.

### Device25261Wire158x1Mux

Gets the value that indicates the NI PXIe-2526 1 wire 158x1 multiplexer topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25261Wire158x1Mux { get; }

#### Returns

The value that indicates the NI PXIe-2526 1 wire 158x1 multiplexer topology.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25271wiredual32x1mux.html language=enus -->
## TOPIC 00027: Device25271WireDual32x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25271wiredual32x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25271wiredual32x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2527 as a 1-wire dual 32x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25271WireDual32x1Mux { get; }ReturnsReturns a String representing the topology of the device for the session

### Device25271WireDual32x1Mux

Gets a value that indicates a topology which uses the NI PXI-2527 as a 1-wire dual 32x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25271WireDual32x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25272wiredual16x1mux.html language=enus -->
## TOPIC 00028: Device25272WireDual16x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25272wiredual16x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25272wiredual16x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2527 as a 2-wire dual 16x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25272WireDual16x1Mux { get; }ReturnsReturns a String representing the topology of the device for the session

### Device25272WireDual16x1Mux

Gets a value that indicates a topology which uses the NI PXI-2527 as a 2-wire dual 16x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25272WireDual16x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25292wire4x32matrix.html language=enus -->
## TOPIC 00029: Device25292Wire4x32Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25292wire4x32matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25292wire4x32matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2529 as a 2-wire 4x32 matrix topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25292Wire4x32Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25292Wire4x32Matrix

Gets a value that indicates the NI PXI-2529 as a 2-wire 4x32 matrix topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25292Wire4x32Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wire128x1mux.html language=enus -->
## TOPIC 00030: Device25301Wire128x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wire128x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wire128x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire 128x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25301Wire128x1Mux { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25301Wire128x1Mux

Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire 128x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25301Wire128x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wire8x16matrix.html language=enus -->
## TOPIC 00031: Device25301Wire8x16Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wire8x16matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wire8x16matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2530 as a 1-wire 8x16 matrix topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25301Wire8x16Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25301Wire8x16Matrix

Gets a value that indicates the NI PXI-2530 as a 1-wire 8x16 matrix topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25301Wire8x16Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wireoctal16x1mux.html language=enus -->
## TOPIC 00032: Device25301WireOctal16x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wireoctal16x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25301wireoctal16x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire octal 16x1 multiplexer. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25301WireOctal16x1Mux { get; }ReturnsReturns a String representing the topology of the device for the sessi

### Device25301WireOctal16x1Mux

Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire octal 16x1 multiplexer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25301WireOctal16x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25311wire8x64matrix.html language=enus -->
## TOPIC 00033: Device25311Wire8x64Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25311wire8x64matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25311wire8x64matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 8×64 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25311Wire8x64Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25311Wire8x64Matrix

Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 8×64 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25311Wire8x64Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25321wire8x64matrix.html language=enus -->
## TOPIC 00034: Device25321Wire8x64Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25321wire8x64matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25321wire8x64matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 8×64 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25321Wire8x64Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25321Wire8x64Matrix

Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 8×64 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25321Wire8x64Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25322wire16x16matrix.html language=enus -->
## TOPIC 00035: Device25322Wire16x16Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25322wire16x16matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25322wire16x16matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 16×16 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25322Wire16x16Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25322Wire16x16Matrix

Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 16×16 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25322Wire16x16Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25322wire8x32matrix.html language=enus -->
## TOPIC 00036: Device25322Wire8x32Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25322wire8x32matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25322wire8x32matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 8×32 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25322Wire8x32Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25322Wire8x32Matrix

Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 8×32 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25322Wire8x32Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25331wire4x64matrix.html language=enus -->
## TOPIC 00037: Device25331Wire4x64Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25331wire4x64matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25331wire4x64matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2533 as a 1-wire 4×64 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25331Wire4x64Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25331Wire4x64Matrix

Gets a value that indicates a topology which uses the NI PXI-2533 as a 1-wire 4×64 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25331Wire4x64Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25351wire4x136matrix.html language=enus -->
## TOPIC 00038: Device25351Wire4x136Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25351wire4x136matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25351wire4x136matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2535 as a 1-wire 4×136 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25351Wire4x136Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25351Wire4x136Matrix

Gets a value that indicates a topology which uses the NI PXI-2535 as a 1-wire 4×136 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25351Wire4x136Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25401wire8x9matrix.html language=enus -->
## TOPIC 00039: Device25401Wire8X9Matrix

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25401wire8x9matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25401wire8x9matrix.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates a topology which uses the NI PXI-2540 as a 1-wire 8x9 matrix. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25401Wire8X9Matrix { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25401Wire8X9Matrix

Gets a value that indicates a topology which uses the NI PXI-2540 as a 1-wire 8x9 matrix.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25401Wire8X9Matrix { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2542quad2x1terminatedmux.html language=enus -->
## TOPIC 00040: Device2542Quad2x1TerminatedMux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2542quad2x1terminatedmux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2542quad2x1terminatedmux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI/PXIe-2542 in the quad 2×1 terminated multiplexer topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2542Quad2x1TerminatedMux { get; }ReturnsReturns a String representing the topology of the device for the sessio

### Device2542Quad2x1TerminatedMux

Gets a value that indicates the NI PXI/PXIe-2542 in the quad 2×1 terminated multiplexer topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2542Quad2x1TerminatedMux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25448x1terminatedmux.html language=enus -->
## TOPIC 00041: Device25448x1TerminatedMux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25448x1terminatedmux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device25448x1terminatedmux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI/PXIe-2544 in the 8×1 terminated multiplexer topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device25448x1TerminatedMux { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device25448x1TerminatedMux

Gets a value that indicates the NI PXI/PXIe-2544 in the 8×1 terminated multiplexer topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device25448x1TerminatedMux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2546dual4x1mux.html language=enus -->
## TOPIC 00042: Device2546Dual4x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2546dual4x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2546dual4x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2546 in the dual 4×1 multiplexer topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2546Dual4x1Mux { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device2546Dual4x1Mux

Gets a value that indicates the NI PXI-2546 in the dual 4×1 multiplexer topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2546Dual4x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2559terminated2spdt.html language=enus -->
## TOPIC 00043: Device2559Terminated2Spdt

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2559terminated2spdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2559terminated2spdt.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2559 in the dual terminated SPDT general-purpose topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2559Terminated2Spdt { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device2559Terminated2Spdt

Gets a value that indicates the NI PXI-2559 in the dual terminated SPDT general-purpose topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2559Terminated2Spdt { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device256516spst.html language=enus -->
## TOPIC 00044: Device256516Spst

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device256516spst.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device256516spst.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2565 in the 16-SPST topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device256516Spst { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device256516Spst

Gets a value that indicates the NI PXI-2565 in the 16-SPST topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device256516Spst { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2720independent.html language=enus -->
## TOPIC 00045: Device2720Independent

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2720independent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2720independent.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2720 in the independent topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2720Independent { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device2720Independent

Gets a value that indicates the NI PXI-2720 in the independent topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2720Independent { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2725independent.html language=enus -->
## TOPIC 00046: Device2725Independent

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2725independent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2725independent.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2725 in the independent topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2725Independent { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device2725Independent

Gets a value that indicates the NI PXI-2725 in the independent topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2725Independent { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2796dual6x1mux.html language=enus -->
## TOPIC 00047: Device2796Dual6x1Mux

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2796dual6x1mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2796dual6x1mux.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2796 in the dual 6×1 multiplexer topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2796Dual6x1Mux { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device2796Dual6x1Mux

Gets a value that indicates the NI PXI-2796 in the dual 6×1 multiplexer topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2796Dual6x1Mux { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2798dualtransfer.html language=enus -->
## TOPIC 00048: Device2798DualTransfer

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2798dualtransfer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology-device2798dualtransfer.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates the NI PXI-2798 in the dual transfer topology. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Device2798DualTransfer { get; }ReturnsReturns a String representing the topology of the device for the session.

### Device2798DualTransfer

Gets a value that indicates the NI PXI-2798 in the dual transfer topology.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Device2798DualTransfer { get; }

#### Returns

Returns a String representing the topology of the device for the session.

Parent topic:

SwitchDeviceTopology Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdevicetopology.html language=enus -->
## TOPIC 00049: SwitchDeviceTopology Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdevicetopology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdevicetopology.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the topology name you want to use for the NI-SWITCH device. See the constructor which takes the topology as one of the parameters in the NISwitch class for more information about topologies. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic class SwitchDe

### SwitchDeviceTopology Class

Defines the topology name you want to use for the NI-SWITCH device. See the constructor which takes the topology as one of the parameters in the [NISwitch](nationalinstruments-modularinstruments-niswitch-niswitch.html) class for more information about topologies.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchDeviceTopology

#### Remarks

For more information, refer to [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Device11271Wire64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1127 as a 1-wire 64x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device11272Wire32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1127 as a 2-wire 32x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device11272Wire4x8Matrix | Gets a value that indicates a topology which uses the NI SCXI-1127 containing a 2-wire 4x8 matrix, while connecting your signals using the NI SCXI-1332 terminal block. |
| Device11274Wire16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1127 containing a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device1127Independent | Gets a value that indicates the NI SCXI-1127 in the independent topology, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device11281Wire64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1128 as a 1-wire 64x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device11282Wire32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1128 as a 2-wire 32x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device11282Wire4x8Matrix | Gets a value that indicates a topology which uses the NI SCXI-1128 containing a 2-wire 4x8 matrix, while connecting your signals using the NI SCXI-1332 terminal block. |
| Device11284Wire16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1128 as a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device1128Independent | Gets a value that uses the independent topology, while connecting your signals using the NI SCXI-1331 terminal block. |
| Device11292Wire16x16Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing a 16x16 matrix. |
| Device11292Wire4x64Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing a 4x64 matrix. |
| Device11292Wire8x32Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing a 8x32 matrix. |
| Device11292WireDual4x32Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing two 4x32 matrices. |
| Device11292WireDual8x16Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing two banks of 8x16 matrices. |
| Device11292WireQuad4x16Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing four banks of 4x16 matrices. |
| Device11301Wire256x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 256x1 multiplexer. |
| Device11301Wire4x64Matrix | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 4x64 matrix. |
| Device11301Wire8x32Matrix | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 8x32 matrix. |
| Device11301WireDual128x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 128x1 multiplexer. |
| Device11301WireOctal32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire octal 32x1 multiplexer. |
| Device11301WireQuad64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire quad 64x1 multiplexer. |
| Device11301WireSixteen16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as sixteen independent 1-wire 16x1 multiplexer. |
| Device11302Wire128x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 128x1 multiplexer. |
| Device11302Wire4x32Matrix | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 4x32 matrix. |
| Device11302WireOctal16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire octal 16x1 multiplexer. |
| Device11302WireQuad32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire quad 32x1 multiplexer. multiplexer. |
| Device11304Wire64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 64x1 multiplexer. multiplexer. |
| Device11304WireQuad16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 16x1 multiplexer. |
| Device1130Independent | Gets a value that indicates the NI SCXI-1130 in the independent topology, while connecting your signals using the NI SCXI-1377 terminal block. |
| Device116016Spdt | Gets a value that indicates a the NI SCXI-1160 in the 16-SPDT general purpose topology. |
| Device11618Spdt | Gets a value that indicates the NI SCXI-1161 in the 8-SPDT general purpose topology. |
| Device1163ROctal4x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1163R in the octal 4x1 multiplexer topology. |
| Device116616Dpdt | Gets a value that indicates a topology which uses the NI SCXI-1166 in the 16-DPDT topology. |
| Device116632Spdt | Gets a value that indicates a topology which uses the NI SCXI-1166 in the 32-SPDT topology. |
| Device1167Independent | Gets a value that indicates the NI SCXI-1167 in the independent topology. |
| Device1169100Spst | Gets a value that indicates the NI SCXI-1169 in the 100-SPST topology. |
| Device116950Dpst | Gets a value that indicates the NI SCXI-1169 in the 50-SPST topology. |
| Device11751Wire196x1Mux | Gets a value that indicates the NI SCXI-1175 in the 1-wire 196x1 multiplexer topology. |
| Device11752Wire95x1Mux | Gets a value that indicates the NI SCXI-1175 in the 2-wire 95x1 multiplexer topology. |
| Device11752Wire98x1Mux | Gets a value that indicates the NI SCXI-1175 in the 2-wire 98x1 multiplexer topology. |
| Device1190Quad4x1Mux | Gets a value that indicates the NI SCXI-1190 in the quad 4x1 multiplexer topology. |
| Device1191Quad4x1Mux | Gets a value that indicates the NI SCXI-1191 in the quad 4x1 multiplexer topology. |
| Device11928Spdt | Gets a value that indicates the NI SCXI-1192 in the 8-SPDT general-purpose topology. |
| Device119316x1TerminatedMux | Gets a value that indicates the NI SCXI-1193 16x1 in the terminated multiplexer topology. |
| Device119332x1Mux | Gets a value that indicates the NI SCXI-1193 in the 32x1 multiplexer topology. |
| Device1193Dual16x1Mux | Gets a value that indicates the NI SCXI-1193 in the dual 16x1 multiplexer topology. |
| Device1193Dual8x1TerminatedMux | Gets a value that indicates the NI SCXI-1193 in the dual 8x1 terminated multiplexer topology. |
| Device1193Independent | Gets a value that indicates the NI SCXI-1193 in the independent topology. |
| Device1193Quad4x1TerminatedMux | Gets a value that indicates the NI SCXI-1193 in the quad 4x1 terminated multiplexer topology. |
| Device1193Quad8x1Mux | Gets a value that indicates the NI SCXI-1193 in the quad 8x1 multiplexer topology. |
| Device1194Quad4x1Mux | Gets a value that indicates the NI SCXI-1194 in the quad 4x1 multiplexer topology. |
| Device1195Quad4x1Mux | Gets a value that indicates the NI SCXI-1195 in the quad 4x1 multiplexer topology. |
| Device25011Wire48x1AmplifiedMux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 1-wire 48x1 amplified multiplexer. |
| Device25011Wire48x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 1-wire 48x1 multiplexer. |
| Device25012Wire24x1AmplifiedMux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire 24x1 amplified multiplexer. |
| Device25012Wire24x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire 24x1 multiplexer. |
| Device25012Wire4x6Matrix | Use this topology, when using the NI PXI-2501 as a 2-wire 4x6 matrix. |
| Device25012WireDual12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire dual 12x1 multiplexer. |
| Device25012WireQuad6x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire quad 6x1 multiplexer. |
| Device25014Wire12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 4-wire 12x1 multiplexer. |
| Device25031Wire48x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 1-wire 48x1 multiplexer. |
| Device25032Wire24x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire 24x1 multiplexer. |
| Device25032Wire4x6Matrix | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire 4x6 matrix. |
| Device25032WireDual12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire dual 12x1 multiplexer. |
| Device25032WireQuad6x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire quad 6x1 multiplexer. |
| Device25034Wire12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 4-wire 12x1 multiplexer. |
| Device2510Independent | Gets a value that indicates the NI PXI-2510 in the independent topology. |
| Device2512Independent | Gets a value that indicates the NI PXI-2512 in the independent topology. |
| Device2514Independent | Gets a value that indicates the NI PXI-2514 in the independent topology. |
| Device2515Independent | Gets a value that indicates the NI PXI-2515 in the independent topology. |
| Device252080Spst | Gets a value that indicates the NI PXI-2520 in the 80 SPST topology. |
| Device252140Dpst | Gets a value that indicates the NI PXI-2521 in the 40 DPST topology. |
| Device252253Spdt | Gets a value that indicates the NI PXI-2522 in the 53 SPDT topology. |
| Device252326Dpdt | Gets a value that indicates the NI PXI-2523 in the 26 DPDT topology. |
| Device25241Wire128x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire 128x1 multiplexer topology. |
| Device25241WireDual64x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire dual 64x1 multiplexer topology. |
| Device25241WireOctal16x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire octal 16x1 multiplexer topology. |
| Device25241WireQuad32x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire quad 32x1 multiplexer topology. |
| Device25241WireSixteen8x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire sixteen 8x1 multiplexer topology. |
| Device25252Wire64x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire 64x1 multiplexer topology. |
| Device25252WireDual32x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire dual 32x1 multiplexer topology. |
| Device25252WireOctal8x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire octal 8x1 multiplexer topology. |
| Device25252WireQuad16x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire quad 16x1 multiplexer topology. |
| Device25252WireSixteen4x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire sixteen 4x1 multiplexer topology. |
| Device25261Wire158x1Mux | Gets the value that indicates the NI PXIe-2526 1 wire 158x1 multiplexer topology. |
| Device25262Wire79x1Mux | Gets the value that indicates the NI PXIe-2526 2 wire 79x1 multiplexer topology. |
| Device25271Wire64x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 1-wire 64x1 multiplexer. |
| Device25271WireDual32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 1-wire dual 32x1 multiplexer. |
| Device25272Wire32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 2-wire 32x1 multiplexer. |
| Device25272WireDual16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 2-wire dual 16x1 multiplexer. |
| Device25274Wire16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 4-wire 16x1 multiplexer. |
| Device2527Independent | Gets a value that indicates the NI PXI-2527 in the independent topology. |
| Device25292Wire4x32Matrix | Gets a value that indicates the NI PXI-2529 as a 2-wire 4x32 matrix topology. |
| Device25292Wire8x16Matrix | Gets a value that indicates the NI PXI-2529 as a 2-wire 8x16 matrix topology. |
| Device25292WireDual4x16Matrix | Gets a value that indicates the NI PXI-2529 as a 2-wire dual 4x16 matrix topology. |
| Device25301Wire128x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire 128x1 multiplexer. |
| Device25301Wire4x32Matrix | Gets a value that indicates the NI PXI-2530 as a 1-wire 4x32 matrix topology. |
| Device25301Wire8x16Matrix | Gets a value that indicates the NI PXI-2530 as a 1-wire 8x16 matrix topology. |
| Device25301WireDual64x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire dual 64x1 multiplexer. |
| Device25301WireOctal16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire octal 16x1 multiplexer. |
| Device25301WireQuad32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire quad 32x1 multiplexer. |
| Device25302Wire4x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire 4×16 matrix topology. |
| Device25302Wire64x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire 64x1 multiplexer. |
| Device25302WireDual32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire dual 32×1 multiplexer. |
| Device25302WireQuad16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire quad 16×1 multiplexer. |
| Device25304Wire32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 4-wire 32x1 multiplexer. |
| Device25304WireDual16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 4-wire dual 16×1 multiplexer. |
| Device2530Independent | Gets a value that uses the NI PXI-2530 in the independent topology. |
| Device25311Wire4x128Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 4×128 matrix. |
| Device25311Wire8x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 8×64 matrix. |
| Device25311WireDual4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire dual 4×64 matrix. |
| Device25311WireDual8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire dual 8×32 matrix. |
| Device25311WireSixteen2x16Matrix | Gets the value that indicates the NI PXI/PXIe-2531 1 wire sixteen 2x16 matrix topology. |
| Device25321Wire16x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 16×32 matrix. |
| Device25321Wire4x128Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 4×128 matrix. |
| Device25321Wire8x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 8×64 matrix. |
| Device25321WireDual16x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire dual 16×16 matrix. |
| Device25321WireDual4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire dual 4×64 matrix. |
| Device25321WireDual8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire dual 8×32 matrix. |
| Device25321WireQuad4x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire quad 4×32 matrix. |
| Device25321WireSixteen2x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire sixteen 2×16 matrix. |
| Device25322Wire16x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 16×16 matrix. |
| Device25322Wire4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 4×64 matrix. |
| Device25322Wire8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 8×32 matrix. |
| Device25322WireDual4x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire dual 4×32 matrix. |
| Device25331Wire4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2533 as a 1-wire 4×64 matrix. |
| Device25341Wire8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2534 as a 1-wire 8×32 matrix. |
| Device25351Wire4x136Matrix | Gets a value that indicates a topology which uses the NI PXI-2535 as a 1-wire 4×136 matrix. |
| Device25361Wire8x68Matrix | Gets a value that indicates a topology which uses the NI PXI-2536 as a 1-wire 8×68 matrix. |
| Device25401Wire8X9Matrix | Gets a value that indicates a topology which uses the NI PXI-2540 as a 1-wire 8x9 matrix. |
| Device25411Wire8X12Matrix | Gets a value that indicates a topology which uses the NI PXI-2541 as a 1-wire 8x12 matrix. |
| Device2542Quad2x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2542 in the quad 2×1 terminated multiplexer topology. |
| Device2543Dual4x1TerminatedMux | Gets a value that indicates the NI PXI-2543 in the dual 4×1 terminated multiplexer topology. |
| Device25448x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2544 in the 8×1 terminated multiplexer topology. |
| Device25454x1TerminatedMux | Gets a value that indicates the NI PXI-2545 in the terminated 4×1 multiplexer topology. |
| Device2546Dual4x1Mux | Gets a value that indicates the NI PXI-2546 in the dual 4×1 multiplexer topology. |
| Device25478x1Mux | Gets a value that indicates the NI PXI-2547 in the 8×1 multiplexer topology. |
| Device25484Spdt | Gets a value that indicates the NI PXI-2548 in the quad SPDT general-purpose topology. |
| Device2549Terminated2Spdt | Gets a value that indicates the NI PXI-2549 in the dual terminated SPDT general-purpose topology. |
| Device25544x1Mux | Gets a value that indicates the NI PXI-2554 in the 4×1 multiplexer topology. |
| Device25554x1TerminatedMux | Gets a value that indicates the NI PXI-2555 in the 4×1 terminated multiplexer topology. |
| Device2556Dual4x1Mux | Gets a value that indicates the NI PXI-2556 in the dual 4×1 multiplexer topology. |
| Device25578x1Mux | Gets a value that indicates the NI PXI-2557 in the dual 8×1 multiplexer topology. |
| Device25584Spdt | Gets a value that indicates the NI PXI-2558 in the quad SPDT general-purpose topology. |
| Device2559Terminated2Spdt | Gets a value that indicates the NI PXI-2559 in the dual terminated SPDT general-purpose topology. |
| Device256416Spst | Gets a value that indicates the NI PXI-2564 in the 16-SPST topology. |
| Device25648Dpst | Gets a value that indicates the NI PXI-2564 in the 8-DPST topology. |
| Device256516Spst | Gets a value that indicates the NI PXI-2565 in the 16-SPST topology. |
| Device256616Spdt | Gets a value that indicates the NI PXI-2566 in the 16-SPDT topology. |
| Device25668Dpdt | Gets a value that indicates the NI PXI-2566 in the 8-DPDT topology. |
| Device2567Independent | Gets a value that indicates the NI PXI-2567 in the independent topology. |
| Device256815Dpst | Gets a value that indicates the NI PXI-2568 in the 15-DPST topology. |
| Device256831Spst | Gets a value that indicates the NI PXI-2568 in the 31-SPST topology. |
| Device2569100Spst | Gets a value that indicates the NI PXI-2569 in the 100-SPST topology. |
| Device256950Dpst | Gets a value that indicates the NI PXI-2569 in the 50-DPST topology. |
| Device257020Dpdt | Gets a value that indicates the NI PXI-2570 in the 20-DPDT topology. |
| Device257040Spdt | Gets a value that indicates the NI PXI-2570 in the 40-SPDT topology. |
| Device257166Spdt | Gets a value that indicates the NI PXI-2571 in the 66-SPDT topology. |
| Device25751Wire196x1Mux | Gets a value that indicates the NI PXI/PXIe-2575 (NI 2575) in the 1-wire 196×1 multiplexer topology. |
| Device25752Wire95x1Mux | Gets a value that indicates the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 95×1 multiplexer topology. |
| Device25752Wire98x1Mux | Gets a value that indicates the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 98×1 multiplexer topology. |
| Device25762Wire64x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire 64×1 multiplexer topology. |
| Device25762WireDual32x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire dual 32×1 multiplexer topology. |
| Device25762WireOctal8x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire octal 8×1 multiplexer topology. |
| Device25762WireQuad16x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire quad 16×1 multiplexer topology. |
| Device25762WireSixteen4x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire sixteen 4×1 multiplexer topology. |
| Device2576Independent | Gets a value that indicates the NI PXI-2576 in the independent topology. |
| Device25841Wire12x1Mux | Gets a value that indicates the NI PXI-2584 in the 1-wire 12×1 multiplexer topology. |
| Device25841WireDual6x1Mux | Gets a value that indicates the NI PXI-2584 in the 1-wire dual 6×1 multiplexer topology. |
| Device25842Wire6x1Mux | Gets a value that indicates the NI PXI-2584 in the 2-wire 6×1 multiplexer topology. |
| Device2584Independent | Gets a value that indicates the NI PXI-2584 in the independent topology. |
| Device25851Wire10x1Mux | Gets a value that indicates the NI PXI-2585 in the 1-wire 10×1 multiplexer topology. |
| Device258610Spst | Gets a value that indicates the NI PXI-2586 in the 10-SPST topology. |
| Device25865Dpst | Gets a value that indicates the NI PXI-2586 in the 5-DPST topology. |
| Device25904x1Mux | Gets a value that indicates the NI PXI-2590 in the 4×1 multiplexer topology. |
| Device25914x1Mux | Gets a value that indicates the NI PXI-2591 in the 4×1 multiplexer topology. |
| Device259316x1Mux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a 16×1 multiplexer topology. |
| Device25938x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a 8×1 terminated multiplexer topology. |
| Device2593Dual4x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a dual 4×1 terminated multiplexer topology. |
| Device2593Dual8x1Mux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a dual 8×1 multiplexer topology. |
| Device2593Independent | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) in the independent topology. |
| Device25944x1Mux | Gets a value that indicates the NI PXI-2594 in the 4×1 multiplexer topology. |
| Device25954x1Mux | Gets a value that indicates the NI PXI-2595 in the 4×1 multiplexer topology. |
| Device2596Dual6x1Mux | Gets a value that indicates the NI PXI-2596 in the dual 6×1 multiplexer topology. |
| Device25976x1TerminatedMux | Gets a value that indicates the NI PXI-2597 in the 6×1 terminated multiplexer topology. |
| Device2598DualTransfer | Gets a value that indicates the NI PXI-2598 in the dual transfer switch topology. |
| Device25992Spdt | Gets a value that indicates the NI PXI-2599 in the 2-SPDT general-purpose topology. |
| Device2720Independent | Gets a value that indicates the NI PXI-2720 in the independent topology. |
| Device2722Independent | Gets a value that indicates the NI PXI-2722 in the independent topology. |
| Device2725Independent | Gets a value that indicates the NI PXI-2725 in the independent topology. |
| Device2727Independent | Gets a value that indicates the NI PXI-2727 in the independent topology. |
| Device27372Wire4x64matrix | Gets the value that indicates the NI PXIe-2737 2 wire 4x64 matrix topology. |
| Device27382Wire8x32Matrix | Gets the value that indicates the NI PXIe-2738 2 wire 8x32 matrix topology. |
| Device27392Wire16x16Matrix | Gets the value that indicates the NI PXIe-2739 2 wire 16x16 matrix topology. |
| Device2746Quad4x1Mux | Gets the value that indicates the NI PXIe-2746 quad 4x1 multiplexer topology. |
| Device2747Dual8x1Mux | Gets the value that indicates the NI PXIe-2747 dual 8x1 multiplexer topology. |
| Device274816x1Mux | Gets the value that indicates the NI PXIe-2748 16x1 multiplexer topology. |
| Device2790Independent | Gets a value that indicates the NI PXI-2790 in the independent topology. |
| Device2796Dual6x1Mux | Gets a value that indicates the NI PXI-2796 in the dual 6×1 multiplexer topology. |
| Device27976x1TerminatedMux | Gets a value that indicates the NI PXI-2797 in the 6x1 terminated multiplexer topology. |
| Device2798DualTransfer | Gets a value that indicates the NI PXI-2798 in the dual transfer topology. |
| Device27992Spdt | Gets a value that indicates the NI PXI-2799 in the 2-SPDT topology. |
| Device28651Wire4x84Matrix | Gets a value that indicates the NI 2865 in the 4×84 terminated matrix topology. |
| DeviceConfiguredTopology | Gets a value that indicates the last topology that was configured for the device in MAX. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveridentity-description.html language=enus -->
## TOPIC 00050: Description

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveridentity-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveridentity-description.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a String that contains a brief description of the specific driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic string Description { get; }ReturnsReturns a System.String that contains a brief description about the NI-SWITCH driver. ExceptionsTypeDescriptionSystem.Objec

### Description

Gets a String that contains a brief description of the specific driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public string Description { get; }

#### Returns

Returns a System.String that contains a brief description about the NI-SWITCH driver.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Descriptionwas accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchDriverIdentity Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveridentity-getsupportedinstrumentmodels.html language=enus -->
## TOPIC 00051: GetSupportedInstrumentModels()

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveridentity-getsupportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveridentity-getsupportedinstrumentmodels.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of names of instrument models with which the IVI-specific driver is compatible. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic String[] GetSupportedInstrumentModels()ReturnsReturns a String containing the list of names of instrument models with which the IVI-sp

### GetSupportedInstrumentModels()

Returns a list of names of instrument models with which the IVI-specific driver is compatible.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public String[] GetSupportedInstrumentModels()

#### Returns

Returns a String containing the list of names of instrument models with which the IVI-specific driver is compatible.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetSupportedInstrumentModels method was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchDriverIdentity Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveridentity-instrumentmanufacturer.html language=enus -->
## TOPIC 00052: InstrumentManufacturer

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveridentity-instrumentmanufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveridentity-instrumentmanufacturer.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the instrument manufacturer of the NI-SWITCH device that is currently in use. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic string InstrumentManufacturer { get; }ReturnsReturns a System.String that contains the name of the instrument manufacturer of the NI-S

### InstrumentManufacturer

Gets the name of the instrument manufacturer of the NI-SWITCH device that is currently in use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public string InstrumentManufacturer { get; }

#### Returns

Returns a System.String that contains the name of the instrument manufacturer of the NI-SWITCH device that is currently in use.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The InstrumentManufacturer was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchDriverIdentity Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveridentity-specificationmajorversion.html language=enus -->
## TOPIC 00053: SpecificationMajorVersion

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveridentity-specificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveridentity-specificationmajorversion.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the major version number of the IviSwtch class specification. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic int SpecificationMajorVersion { get; }ReturnsReturns a System.Int32 representing the major version number of the IviSwtch class specification.

### SpecificationMajorVersion

Gets the major version number of the IviSwtch class specification.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public int SpecificationMajorVersion { get; }

#### Returns

Returns a System.Int32 representing the major version number of the IviSwtch class specification.

Parent topic:

SwitchDriverIdentity Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveridentity-specificationminorversion.html language=enus -->
## TOPIC 00054: SpecificationMinorVersion

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveridentity-specificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveridentity-specificationminorversion.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minor version number of the class specification with which NI-SWITCH driver is compliant. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic int SpecificationMinorVersion { get; }ReturnsReturns a System.Int32 representing the minor version number of the class specificati

### SpecificationMinorVersion

Gets the minor version number of the class specification with which NI-SWITCH driver is compliant.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public int SpecificationMinorVersion { get; }

#### Returns

Returns a System.Int32 representing the minor version number of the class specification with which NI-SWITCH driver is compliant.

Parent topic:

SwitchDriverIdentity Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveridentity.html language=enus -->
## TOPIC 00055: SwitchDriverIdentity Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveridentity.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveridentity.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the methods and properties that provide information about the instrument and the NI-SWITCH driver. Derives fromSwitchSubObjectIIviDriverIdentitySyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic class SwitchDriverIdentity : SwitchSubObject, IIviDriverIdentityRemarksFor mo

### SwitchDriverIdentity Class

Defines the methods and properties that provide information about the instrument and the NI-SWITCH driver.

#### Derives from

- SwitchSubObject
- IIviDriverIdentity

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchDriverIdentity : SwitchSubObject, IIviDriverIdentity

#### Remarks

For more information, refer to [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Description | Gets a String that contains a brief description of the specific driver. |
| Identifier | Gets the String that contains an identifier for NI-Switch .NET API. |
| InstrumentFirmwareRevision | Gets a string that contains the firmware revision information for the NI-SWITCH device that is currently in use. |
| InstrumentManufacturer | Gets the name of the instrument manufacturer of the NI-SWITCH device that is currently in use. |
| InstrumentModel | Gets the model number or name of the NI-SWITCH device that is currently in use. |
| Revision | Gets a string which contains additional version information about the NI-SWITCH instrument driver. |
| SpecificationMajorVersion | Gets the major version number of the IviSwtch class specification. |
| SpecificationMinorVersion | Gets the minor version number of the class specification with which NI-SWITCH driver is compliant. |
| Vendor | Gets the the name of the vendor that supplies the NI-SWITCH driver. |

#### Methods

| Name | Description |
| --- | --- |
| GetGroupCapabilities() | Returns a list of names of class capability groups that the IVI-specific driver implements. |
| GetSupportedInstrumentModels() | Returns a list of names of instrument models with which the IVI-specific driver is compatible. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriverlock-switchdriverlock__iividriverlock.html language=enus -->
## TOPIC 00056: SwitchDriverLock(IIviDriverLock)

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriverlock-switchdriverlock__iividriverlock.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriverlock-switchdriverlock__iividriverlock.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Constructs an NI-SWITCH driver lock. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic SwitchDriverLock(IIviDriverLock iviDriverLock)ParametersNameTypeDescriptioniviDriverLockIIviDriverLockSpecifies the base interface for synchronization locks obtained on the driver session.

### SwitchDriverLock(IIviDriverLock)

Constructs an NI-SWITCH driver lock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public SwitchDriverLock(IIviDriverLock iviDriverLock)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| iviDriverLock | IIviDriverLock | Specifies the base interface for synchronization locks obtained on the driver session. |

Parent topic:

SwitchDriverLock Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveroperation-cache.html language=enus -->
## TOPIC 00057: Cache

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveroperation-cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveroperation-cache.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to cache the value of properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic bool Cache { get; set; }RemarksIf you set this property to true, NI-SWITCH tracks the current NI-SWITCH device settings and avoids sending redundant commands to the device. N

### Cache

Gets or sets whether to cache the value of properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public bool Cache { get; set; }

#### Remarks

If you set this property to true, NI-SWITCH tracks the current NI-SWITCH device settings and avoids sending redundant commands to the device. NI-SWITCH can always cache or never cache particular properties, regardless of the setting of this property.

#### Returns

true if caching is enabled; otherwise, false. The default value is true.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Cache was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchDriverOperation Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveroperation-coercion.html language=enus -->
## TOPIC 00058: Coercion

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveroperation-coercion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveroperation-coercion.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when the NI-SWITCH driver creates a coercion warning. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic EventHandler< SwitchCoercionWarningEventArgs > Coercion

### Coercion

Occurs when the NI-SWITCH driver creates a coercion warning.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public EventHandler< [SwitchCoercionWarningEventArgs](nationalinstruments-modularinstruments-niswitch-switchcoercionwarningeventargs.html) > Coercion

Parent topic:

SwitchDriverOperation Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveroperation-dispose.html language=enus -->
## TOPIC 00059: Dispose()

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveroperation-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveroperation-dispose.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic void Dispose()

### Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public void Dispose()

Parent topic:

SwitchDriverOperation Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveroperation-interchangecheck.html language=enus -->
## TOPIC 00060: InterchangeCheck

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveroperation-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveroperation-interchangecheck.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic bool InterchangeCheck { get; set; }RemarksNI-SWITCH does not support interchangeability check. Returnstrue if interchangeabilit

### InterchangeCheck

Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public bool InterchangeCheck { get; set; }

#### Remarks

NI-SWITCH does not support interchangeability check.

#### Returns

true if interchangeability checking is enabled; otherwise false. The default value is false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The InterchangeCheck was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchDriverOperation Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchdriveroperation-queryinstrumentstatus.html language=enus -->
## TOPIC 00061: QueryInstrumentStatus

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchdriveroperation-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchdriveroperation-queryinstrumentstatus.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether NI-SWITCH queries the NI-SWITCH device status after each operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic bool QueryInstrumentStatus { get; set; }RemarksNI-SWITCH can choose to ignore status checking for particular properties, regardless of the s

### QueryInstrumentStatus

Gets or sets whether NI-SWITCH queries the NI-SWITCH device status after each operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public bool QueryInstrumentStatus { get; set; }

#### Remarks

NI-SWITCH can choose to ignore status checking for particular properties, regardless of the setting of this property.

Querying the device status is useful for debugging. After you validate your program, you can set this property to false to disable status checking and maximize performance.

#### Returns

true if querying is enabled; otherwise, false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The QueryInstrumentStatus was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchDriverOperation Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switcherrorqueryresult-errormessage.html language=enus -->
## TOPIC 00062: ErrorMessage

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switcherrorqueryresult-errormessage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switcherrorqueryresult-errormessage.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the user readable error string. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic string ErrorMessage { get; }ReturnsReturns a String representing the error string.

### ErrorMessage

Gets the user readable error string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public string ErrorMessage { get; }

#### Returns

Returns a String representing the error string.

Parent topic:

SwitchErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics-numberofrelays.html language=enus -->
## TOPIC 00063: NumberOfRelays

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics-numberofrelays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics-numberofrelays.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of relays. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic int NumberOfRelays { get; }ReturnsSpecifies an Int32 which indicates the number of relays. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe NumberOfRelays property was accessed after the assoc

### NumberOfRelays

Gets the number of relays.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public int NumberOfRelays { get; }

#### Returns

Specifies an Int32 which indicates the number of relays.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The NumberOfRelays property was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchModuleCharacteristics Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics-serialnumber.html language=enus -->
## TOPIC 00064: SerialNumber

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics-serialnumber.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the serial number for the switch controlled by NI-SWITCH. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic string SerialNumber { get; }RemarksIf the device does not return a serial number, NI-SWITCH returns the Invalid Attribute error. ReturnsSpecifies a String that indica

### SerialNumber

Gets the serial number for the switch controlled by NI-SWITCH.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public string SerialNumber { get; }

#### Remarks

If the device does not return a serial number, NI-SWITCH returns the Invalid Attribute error.

#### Returns

Specifies a String that indicates the serial number for the switch controlled by the NI-SWITCH driver.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SerialNumber was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchModuleCharacteristics Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics.html language=enus -->
## TOPIC 00065: SwitchModuleCharacteristics Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchmodulecharacteristics.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the methods and properties that provide information about the inherent characteristics of the NI-SWITCH driver. Derives fromSwitchSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic class SwitchModuleCharacteristics : SwitchSubObjectRemarksFor more information, re

### SwitchModuleCharacteristics Class

Defines the methods and properties that provide information about the inherent characteristics of the NI-SWITCH driver.

#### Derives from

- SwitchSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchModuleCharacteristics : SwitchSubObject

#### Remarks

For more information, refer to [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| NumberOfColumns | Gets the number of channels on the column of a matrix or scanner. If the switch is a scanner, this value is the number of input channels. |
| NumberOfRelays | Gets the number of relays. |
| NumberOfRows | Gets the number of channels on a row of a matrix or scanner. If the switch is a scanner, this value is the number of output channels. |
| PowerDownLatchingRelaysAfterDebounce | Gets or sets a value which indicates whether to power down latching relays after waiting for the relays to settle. |
| SerialNumber | Gets the serial number for the switch controlled by NI-SWITCH. |
| Temperature | Gets the temperature, in degrees Celcius, for the switch module. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchpath-canconnect__string-string.html language=enus -->
## TOPIC 00066: CanConnect(string, string)

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchpath-canconnect__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchpath-canconnect__string-string.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies that you can create a path between channel1 and channel2. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic SwitchPathCapability CanConnect(string channel1, string channel2)RemarksIf a path is possible in the switch module, the availability of that path is returned give

### CanConnect(string, string)

Verifies that you can create a path between channel1 and channel2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public [SwitchPathCapability](nationalinstruments-modularinstruments-niswitch-switchpathcapability.html) CanConnect(string channel1, string channel2)

#### Remarks

If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an [ImplicitConnectionExistsWarningCode](nationalinstruments-modularinstruments-niswitch-switchwarning-implicitconnectionexistswarningcode.html) warning is returned.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel1 | string | Indicates one of the channel name of the desired path. |
| channel2 | string | Indicates the name of the other channel name of the desired path. |

#### Returns

Returns a [SwitchPathCapability](nationalinstruments-modularinstruments-niswitch-switchpathcapability.html) object indicating whether a path is valid.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CanConnect was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchPath Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchpath-connect__string-string.html language=enus -->
## TOPIC 00067: Connect(string, string)

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchpath-connect__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchpath-connect__string-string.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a path between channel1 and channel2. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic void Connect(string channel1, string channel2)ParametersNameTypeDescriptionchannel1stringIndicates one of the channel name of the desired path. channel2stringIndicates the name of the

### Connect(string, string)

Creates a path between channel1 and channel2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public void Connect(string channel1, string channel2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel1 | string | Indicates one of the channel name of the desired path. |
| channel2 | string | Indicates the name of the other channel name of the desired path. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Swtch.ExplicitConnectionExistsException | The two channels are already explicitly connected by calling either the Connect or SetPath methods. |
| Ivi.Swtch.IsConfigurationChannelException | One of the channels is a configuration channel. |
| Ivi.Swtch.AttemptToConnectSourcesException | Both channels are connected to a different source. |
| Ivi.Swtch.CannotConnectToItselfException | channel1 and channel2 are one and the same channel |
| Ivi.Swtch.PathNotFoundException | Driver cannot find a path between the two channels. |
| Ivi.Driver.SelectorNameException | A repeated capability selector is expected, but the driver does not recognise the provided name. |
| Ivi.Driver.IviCDriverException | When an underlying IVI-C driver was called to perform an action, the IVI-C driver action did not succeed. |
| System.ObjectDisposedException | The Connect was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchPath Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchrevisionqueryresult-operator_neq__switchrevisionqueryresult-switchrevisionqueryresult.html language=enus -->
## TOPIC 00068: operator!=(SwitchRevisionQueryResult, SwitchRevisionQueryResult)

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchrevisionqueryresult-operator_neq__switchrevisionqueryresult-switchrevisionqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchrevisionqueryresult-operator_neq__switchrevisionqueryresult-switchrevisionqueryresult.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of SwitchRevisionQueryResult are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static bool operator!=(SwitchRevisionQueryResult result1, SwitchRevisionQueryResult result2)ParametersNameTypeDescriptionresult1SwitchRevisionQueryResultA

### operator!=(SwitchRevisionQueryResult, SwitchRevisionQueryResult)

Checks whether the two instances of [SwitchRevisionQueryResult](nationalinstruments-modularinstruments-niswitch-switchrevisionqueryresult.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static bool operator!=(SwitchRevisionQueryResult result1, SwitchRevisionQueryResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | SwitchRevisionQueryResult | A SwitchRevisionQueryResult object. |
| result2 | SwitchRevisionQueryResult | A SwitchRevisionQueryResult object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

SwitchRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscan-mode.html language=enus -->
## TOPIC 00069: Mode

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscan-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscan-mode.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies what happens to existing connections that conflict with the connections you make in a List. For example, if CH1 is already connected to CH2 and the List instructs the switch to connect CH1 to CH3, this attribute specifies what happens to the connection between CH1 and CH2. If the value of

### Mode

Specifies what happens to existing connections that conflict with the connections you make in a [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html). For example, if CH1 is already connected to CH2 and the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html) instructs the switch to connect CH1 to CH3, this attribute specifies what happens to the connection between CH1 and CH2. If the value of this attribute is [None](nationalinstruments-modularinstruments-niswitch-switchscanmode.html), the switch takes no action on existing paths. If the value is [BreakBeforeMake](nationalinstruments-modularinstruments-niswitch-switchscanmode.html), the switch breaks conflicting paths before making new ones. If the value is [BreakBeforeMake](nationalinstruments-modularinstruments-niswitch-switchscanmode.html), the switch breaks conflicting paths after making new ones. Most switches support only one of the possible values. In such cases, this attribute serves as an indicator of the device's behavior.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public [SwitchScanMode](nationalinstruments-modularinstruments-niswitch-switchscanmode.html) Mode { get; set; }

#### Returns

The values for the property are defined in [SwitchScanMode](nationalinstruments-modularinstruments-niswitch-switchscanmode.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Mode was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscan-scan__string-switchscaninitiation.html language=enus -->
## TOPIC 00070: Scan(string, SwitchScanInitiation)

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscan-scan__string-switchscaninitiation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscan-scan__string-switchscaninitiation.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes the List provided, programs the switching hardware and initiates the scan. Once initiation is complete, the operation will return. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic void Scan(string scanList, SwitchScanInitiation initiation)RemarksThe List itself is compris

### Scan(string, SwitchScanInitiation)

Takes the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html) provided, programs the switching hardware and initiates the scan. Once initiation is complete, the operation will return.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public void Scan(string scanList, SwitchScanInitiation initiation)

#### Remarks

List

List

List

To see the status of the scan, you can call either [IsScanning](nationalinstruments-modularinstruments-niswitch-switchscan-isscanning.html) or [WaitForScanComplete](nationalinstruments-modularinstruments-niswitch-switchscan-waitforscancomplete__precisiontimespan.html). Use the [ConfigureTrigger](nationalinstruments-modularinstruments-niswitch-switchscan-configuretrigger__precisiontimespan-string-string.html) method to configure the scan trigger. Use the [Abort](nationalinstruments-modularinstruments-niswitch-switchscan-abort.html) method to stop the scan if you are in continuous scan mode (Refer to [Continuous](nationalinstruments-modularinstruments-niswitch-switchscan-continuous.html) otherwise the scan halts automatically when the end of the scan list is reached. For reference, this operation is equivalent to calling [ConfigureList](nationalinstruments-modularinstruments-niswitch-switchscan-configurelist__string-switchscanmode.html) and [Initiate](nationalinstruments-modularinstruments-niswitch-switchscan-initiate.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scanList | string | Pass the List you want the instrument to use. |
| initiation | SwitchScanInitiation | Use the initiation parameter to specify whether the switch or the measurement device initiates the scan trigger handshake. This parameter determines whether to wait for the scan to reach a trigger point before completing. If the measurement device initiates the scan, set this parameter to MeasurementDeviceInitiated. This method then waits until the switch is waiting for a trigger from the measurement device before completing. If the switch initiates the scan, set this parameter to SwitchInitiated. This function then completes immediately after initiating the scan. You should have already set up your DMM to wait for a trigger before calling this function with Initiation set to SwitchInitiated. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Swtch.InvalidScanListException | This exception is used when the driver finds that the given scan list string does not have the correct syntax, or the scan list syntax cannot be implemented by the switch. |
| Ivi.Swtch.NoSuchPathException | This exception is used when no explicit path exists between the two channels.. |
| Ivi.Swtch.ExplicitConnectionExistsException | This exception is used when an attempt is made to connect two channels that are already explicitly connected. |
| Ivi.Driver.IviCDriverException | When an underlying IVI-C driver was called to perform an action, the IVI-C driver action did not succeed. |
| System.ObjectDisposedException | The Scan method was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscan-sendsoftwaretrigger.html language=enus -->
## TOPIC 00071: SendSoftwareTrigger()

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscan-sendsoftwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscan-sendsoftwaretrigger.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a software trigger to the switch specified in the NI-SWITCH session. When the TriggerInput is set to SoftwareTrigger through either the ConfigureTrigger function or the TriggerInput attribute, the scan does not proceed from a semicolon (wait for trigger) until SendSoftwareTrigger is called. Sy

### SendSoftwareTrigger()

Sends a software trigger to the switch specified in the NI-SWITCH session. When the [TriggerInput](nationalinstruments-modularinstruments-niswitch-switchscan-triggerinput.html) is set to [SoftwareTrigger](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-softwaretrigger.html) through either the [ConfigureTrigger](nationalinstruments-modularinstruments-niswitch-switchscan-configuretrigger__precisiontimespan-string-string.html) function or the [TriggerInput](nationalinstruments-modularinstruments-niswitch-switchscan-triggerinput.html) attribute, the scan does not proceed from a semicolon (wait for trigger) until SendSoftwareTrigger is called.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public void SendSoftwareTrigger()

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.TriggerNotSoftwareException | A Send Software Trigger method could not send a software trigger. |
| System.ObjectDisposedException | The SendSoftwareTrigger method was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscan-triggerinput.html language=enus -->
## TOPIC 00072: TriggerInput

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscan-triggerinput.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscan-triggerinput.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value which specifies the source of the trigger for which the switch can wait when processing a List. The switch waits for a trigger when it encounters a semicolon in a List. When the trigger occurs, the switch advances to the next entry in the List. SyntaxNamespace: NationalInstrumen

### TriggerInput

Gets or sets a value which specifies the source of the trigger for which the switch can wait when processing a [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html). The switch waits for a trigger when it encounters a semicolon in a [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html). When the trigger occurs, the switch advances to the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public string TriggerInput { get; set; }

#### Remarks

- [Immediate](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-immediate.html): The switch does not wait for a trigger before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [External](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-external.html): The switch waits until it receives a trigger from an external source through the "trigger in" connector.
- [SoftwareTrigger](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-softwaretrigger.html): The switch waits until you call the [SendSoftwareTrigger](nationalinstruments-modularinstruments-niswitch-switchscan-sendsoftwaretrigger.html) method.
- [Ttl0](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl0.html): The switch waits until it receives a trigger on the SCXI or PXI_TRIG0 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl1](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl1.html): The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl2](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl2.html): The switch waits until it receives a trigger on the SCXI or PXI_TRIG2 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl3](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl3.html): The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl4](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl4.html): The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl5](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl5.html): The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl6](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl6.html): The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [Ttl7](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl7.html): The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [PxiStar](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-pxistar.html): The switch waits until it receives a trigger on the PXI STAR trigger bus before processing the next entry in the [List](nationalinstruments-modularinstruments-niswitch-switchscan-list.html).
- [RearConnector](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-rearconnector.html): The switch waits until it receives a trigger on the Rear connector before processing the next entry in the scan list. This value is valid for SCXI scanners that consist of a single device. If more than one device is used, you must use [RouteTriggerInput](nationalinstruments-modularinstruments-niswitch-switchscan-routetriggerinput__string-string-bool.html) or [RouteScanAdvancedOutput](nationalinstruments-modularinstruments-niswitch-switchscan-routescanadvancedoutput__string-string-bool.html) functions to route a trigger from the connector on another module to one of the TTL lines instead.
- [FrontConnector](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-frontconnector.html): The switch waits until it receives a trigger on the front connector before processing the next entry in the scan list. When using SCXI scanners, this variable is valid for scanners that consist of a single device. If more than one device is used, you must use the [RouteTriggerInput](nationalinstruments-modularinstruments-niswitch-switchscan-routetriggerinput__string-string-bool.html) or [RouteScanAdvancedOutput](nationalinstruments-modularinstruments-niswitch-switchscan-routescanadvancedoutput__string-string-bool.html) functions to route a trigger from the connector on another module to one of the TTL lines instead.

#### Returns

The values accepted by this property are defined in [SwitchScanTriggerInput](nationalinstruments-modularinstruments-niswitch-switchscantriggerinput.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TriggerInput was accessed after the associated NISwitch object was disposed. |

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscan.html language=enus -->
## TOPIC 00073: SwitchScan Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscan.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the properties used to configure a switch device using a scan list string. Derives fromSwitchSubObjectIIviSwtchScanSyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic class SwitchScan : SwitchSubObject, IIviSwtchScanRemarksFor more information, refer to NI Switches Help. T

### SwitchScan Class

Defines the properties used to configure a switch device using a scan list string.

#### Derives from

- SwitchSubObject
- IIviSwtchScan

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchScan : SwitchSubObject, IIviSwtchScan

#### Remarks

For more information, refer to [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AdvancedOutput | Gets or sets a value which specifies the method you want to use to notify another instrument that all signals going through the switch have settled following the processing of one entry in the List. |
| AdvancedPolarity | Gets or sets the advance polarity for the scan. |
| Continuous | Gets or sets a value that indicates whether a switch device stops scanning at the end of the scan, or continues scanning from the top of the scan list. Notice that if you set the scan to continuous true, the WaitForScanComplete method will always time out and you must call Abort to stop the scan. |
| Delay | Gets or sets a value which indicates the minimum amount of time, in seconds, the Switch device waits before it asserts the AdvancedOutput trigger after opening or closing the switch. The switch always WaitForDebounce before asserting the trigger. |
| DigitalFilterEnable | Gets or sets a value which indicates whether to apply the pulse width to the TriggerInput. Set the property to true to prevent the switch module from being triggered by pulses that are less than 150 ns on PXI trigger lines 0-7. When this property is set to false, noise on the PXI trigger lines might trigger the switch module. If the device triggering the switch module can send pulses greater than 150 ns, do not disable this property. |
| HandshakingInitiation | Gets or sets a value which specifies how to start handshaking with a measurement device. |
| IsScanning | Gets or sets a value which indicates whether the switch has completed the scan operation. The value true indicates that the scan is complete. |
| IsWaitingForTrigger | In a List, a semicolon (;) is used to indicate that at that point in the List, the scan engine should pause until a trigger is received from the TriggerInput. If that trigger is user generated through either a hardware pulse or the SendSoftwareTrigger method, it is necessary for the user to know when the scan engine has reached such a state. |
| List | This property contains a List, which is a string that specifies channel connections and trigger conditions. The Initiate function makes or breaks connections and waits for triggers according to the instructions in the List. The List is comprised of channel names that you separate with special characters. These special characters determine the operations the scanner performs on the channels when it executes this scan list. To create a path between two channels, use the following character between the two channel names: -> (a dash followed by a '>' sign) Example: "CH1->CH2" tells the switch to make a path from channel CH1 to channel CH2. To break or clear a path, use the following character as a prefix before the path: ~ (tilde) Example: "~CH1->CH2" tells the switch to break the path from channel CH1 to channel CH2. To create a path between two channels, use the following character between the two channel names: -> (a dash followed by a '>' sign) Example: "CH1->CH2" tells the switch to make a path from channel CH1 to channel CH2. To tell the switch device to create multiple paths simultaneously, use the following character as a separator between the paths: , (comma) Example: "A->B;CH1->CH2,CH3->CH4" instructs the scanner to make the path between channels A and B, wait for a trigger, and then simultaneously make the paths between channels CH1 and CH2 and between channels CH3 and CH4. |
| Mode | Specifies what happens to existing connections that conflict with the connections you make in a List. For example, if CH1 is already connected to CH2 and the List instructs the switch to connect CH1 to CH3, this attribute specifies what happens to the connection between CH1 and CH2. If the value of this attribute is None, the switch takes no action on existing paths. If the value is BreakBeforeMake, the switch breaks conflicting paths before making new ones. If the value is BreakBeforeMake, the switch breaks conflicting paths after making new ones. Most switches support only one of the possible values. In such cases, this attribute serves as an indicator of the device's behavior. |
| TriggerInput | Gets or sets a value which specifies the source of the trigger for which the switch can wait when processing a List. The switch waits for a trigger when it encounters a semicolon in a List. When the trigger occurs, the switch advances to the next entry in the List. |
| TriggerInputPolarity | Gets or sets a value which determines the behavior of the trigger input. |

#### Methods

| Name | Description |
| --- | --- |
| Abort() | Aborts the scan in progress. Initiate a scan with Initiate. If the switch module is not scanning, Ivi.Swtch.NoScanInProgressException exception is returned. |
| Commit() | Downloads the configured List and trigger settings to hardware. |
| ConfigureList(string, SwitchScanMode) | Configures the List and Mode used for scanning. Refer to Switch Device Help to determine if the switch module supports scanning. The List is comprised of a list of channel connections separated by semicolons. For example, the following scan list will scan the first three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer to List for more information on scan list syntax. To see the status of the scan, call either IsScanning or WaitForScanComplete. Use the ConfigureTrigger method to configure the scan trigger. Use the Initiate method to start the scan. |
| ConfigureTrigger(PrecisionTimeSpan, string, string) | Configures the scan triggers for the scan list established with ConfigureList. Refer to Device Help to determine if the switch module supports scanning. ConfigureTrigger sets the location that the switch expects to receive an input trigger to advance through the List. This method also sets the location where it outputs a scan advanced signal after it completes an entry in the scan list. |
| Initiate() | Commits the configured List and trigger settings to hardware and initiates the scan. If Commit was called earlier, Initiate only initiates the scan and returns immediately. Once the scanning operation begins, you cannot perform any other operation other than GetAttribute, Abort, or SendSoftwareTrigger. All other functions return the Ivi.Swtch.ScanInProgressException Exception. To stop the scanning operation, call Abort. |
| RouteScanAdvancedOutput(string, string, bool) | Routes the AdvancedOutput from a trigger bus line (TTLx) to the front or rear connector. |
| RouteTriggerInput(string, string, bool) | Routes the TriggerInput from the front or rear connector to a trigger bus line (TTLx). To disconnect the route, call this function again and specify None for trigger bus line parameter. |
| Scan(string, SwitchScanInitiation) | Takes the List provided, programs the switching hardware and initiates the scan. Once initiation is complete, the operation will return. |
| SendSoftwareTrigger() | Sends a software trigger to the switch specified in the NI-SWITCH session. When the TriggerInput is set to SoftwareTrigger through either the ConfigureTrigger function or the TriggerInput attribute, the scan does not proceed from a semicolon (wait for trigger) until SendSoftwareTrigger is called. |
| WaitForScanComplete(PrecisionTimeSpan) | Pauses until the switch stops scanning or until the maximum time has elapsed, when NI-SWITCH returns a timeout error. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-frontconnectormodule2.html language=enus -->
## TOPIC 00074: FrontConnectorModule2

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-frontconnectormodule2.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-frontconnectormodule2.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to the FrontConnectorModule2 trigger. The switch waits until it receives a trigger on the front connector module 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string FrontConnectorModule2 { get; }ReturnsReturns the String corresponding to

### FrontConnectorModule2

Gets a value corresponding to the FrontConnectorModule2 trigger. The switch waits until it receives a trigger on the front connector module 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string FrontConnectorModule2 { get; }

#### Returns

Returns the String corresponding to the FrontConnectorModule2 trigger.

Parent topic:

SwitchScanAdvancedOutput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-rearconnectormodule6.html language=enus -->
## TOPIC 00075: RearConnectorModule6

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-rearconnectormodule6.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-rearconnectormodule6.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to the RearConnectorModule6 trigger. The switch waits until it receives a trigger on the rear connector module 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string RearConnectorModule6 { get; }ReturnsReturns the String corresponding to th

### RearConnectorModule6

Gets a value corresponding to the RearConnectorModule6 trigger. The switch waits until it receives a trigger on the rear connector module 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string RearConnectorModule6 { get; }

#### Returns

Returns the String corresponding to the RearConnectorModule6 trigger.

Parent topic:

SwitchScanAdvancedOutput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-rearconnectormodule8.html language=enus -->
## TOPIC 00076: RearConnectorModule8

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-rearconnectormodule8.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-rearconnectormodule8.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to the RearConnectorModule8 trigger. The switch waits until it receives a trigger on the rear connector module 8. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string RearConnectorModule8 { get; }ReturnsReturns the String corresponding to th

### RearConnectorModule8

Gets a value corresponding to the RearConnectorModule8 trigger. The switch waits until it receives a trigger on the rear connector module 8.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string RearConnectorModule8 { get; }

#### Returns

Returns the String corresponding to the RearConnectorModule8 trigger.

Parent topic:

SwitchScanAdvancedOutput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl0.html language=enus -->
## TOPIC 00077: Ttl0

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl0.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl0.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl0 { get; }ReturnsReturns the St

### Ttl0

Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl0 { get; }

#### Returns

Returns the String corresponding to the Ttl0 trigger.

Parent topic:

SwitchScanAdvancedOutput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl3.html language=enus -->
## TOPIC 00078: Ttl3

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl3.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl3.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl3 { get; }ReturnsReturns the St

### Ttl3

Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl3 { get; }

#### Returns

Returns the String corresponding to the Ttl3 trigger.

Parent topic:

SwitchScanAdvancedOutput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl6.html language=enus -->
## TOPIC 00079: Ttl6

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl6.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput-ttl6.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl6 { get; }ReturnsReturns the St

### Ttl6

Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl6 { get; }

#### Returns

Returns the String corresponding to the Ttl6 trigger.

Parent topic:

SwitchScanAdvancedOutput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput.html language=enus -->
## TOPIC 00080: SwitchScanAdvancedOutput Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutput.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines properties that indicate the output destination of the scan advanced trigger signal. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic class SwitchScanAdvancedOutputRemarksFor more information, refer to NI Switches Help. Thread SafetyAll members of this t

### SwitchScanAdvancedOutput Class

Defines properties that indicate the output destination of the scan advanced trigger signal.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchScanAdvancedOutput

#### Remarks

For more information, refer to [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| External | Gets a value for the external trigger. The switch waits until it receives a trigger from an external source through the external trigger input before processing the next entry in the scan list. |
| FrontConnector | Gets a value corresponding to the FrontConnector trigger. The switch waits until it receives a trigger on the front connector. |
| FrontConnectorModule1 | Gets a value corresponding to the FrontConnectorModule1 trigger. The switch waits until it receives a trigger on the front connector module 1. |
| FrontConnectorModule10 | Gets a value corresponding to the FrontConnectorModule10 trigger. The switch waits until it receives a trigger on the front connector module 10. |
| FrontConnectorModule11 | Gets a value corresponding to the FrontConnectorModule11 trigger. The switch waits until it receives a trigger on the front connector module 11. |
| FrontConnectorModule12 | Gets a value corresponding to the FrontConnectorModule12 trigger. The switch waits until it receives a trigger on the front connector module 12. |
| FrontConnectorModule2 | Gets a value corresponding to the FrontConnectorModule2 trigger. The switch waits until it receives a trigger on the front connector module 2. |
| FrontConnectorModule3 | Gets a value corresponding to the FrontConnectorModule3 trigger. The switch waits until it receives a trigger on the front connector module 3. |
| FrontConnectorModule4 | Gets a value corresponding to the FrontConnectorModule4 trigger. The switch waits until it receives a trigger on the front connector module 4. |
| FrontConnectorModule5 | Gets a value corresponding to the FrontConnectorModule5 trigger. The switch waits until it receives a trigger on the front connector module 5. |
| FrontConnectorModule6 | Gets a value corresponding to the FrontConnectorModule6 trigger. The switch waits until it receives a trigger on the front connector module 6. |
| FrontConnectorModule7 | Gets a value corresponding to the FrontConnectorModule10 trigger. The switch waits until it receives a trigger on the front connector module 7. |
| FrontConnectorModule8 | Gets a value corresponding to the FrontConnectorModule8 trigger. The switch waits until it receives a trigger on the front connector module 8. |
| FrontConnectorModule9 | Gets a value corresponding to the FrontConnectorModule10 trigger. The switch waits until it receives a trigger on the front connector module 9. |
| None | Gets a value that indicates no implicit action on scanning connections. |
| PxiStar | Gets a value corresponding to a trigger on the PXI star trigger bus before processing the next entry in the scan list. |
| RearConnector | Gets a value corresponding to the RearConnector trigger. The switch waits until it receives a trigger on the rear connector. |
| RearConnectorModule1 | Gets a value corresponding to the RearConnectorModule1 trigger. The switch waits until it receives a trigger on the rear connector module 1. |
| RearConnectorModule10 | Gets a value corresponding to the RearConnectorModule10 trigger.The switch waits until it receives a trigger on the rear connector module 10. |
| RearConnectorModule11 | Gets a value corresponding to the RearConnectorModule11 trigger.The switch waits until it receives a trigger on the rear connector module 11. |
| RearConnectorModule12 | Gets a value corresponding to the RearConnectorModule12 trigger. The switch waits until it receives a trigger on the rear connector module 12. |
| RearConnectorModule2 | Gets a value corresponding to the RearConnectorModule2 trigger.The switch waits until it receives a trigger on the rear connector module 2. |
| RearConnectorModule3 | Gets a value corresponding to the RearConnectorModule3 trigger. The switch waits until it receives a trigger on the rear connector module 3. |
| RearConnectorModule4 | Gets a value corresponding to the RearConnectorModule4 trigger. The switch waits until it receives a trigger on the rear connector module 4. |
| RearConnectorModule5 | Gets a value corresponding to the RearConnectorModule5 trigger. The switch waits until it receives a trigger on the rear connector module 5. |
| RearConnectorModule6 | Gets a value corresponding to the RearConnectorModule6 trigger. The switch waits until it receives a trigger on the rear connector module 6. |
| RearConnectorModule7 | Gets a value corresponding to the RearConnectorModule7 trigger. The switch waits until it receives a trigger on the rear connector module 7. |
| RearConnectorModule8 | Gets a value corresponding to the RearConnectorModule8 trigger. The switch waits until it receives a trigger on the rear connector module 8. |
| RearConnectorModule9 | Gets a value corresponding to the RearConnectorModule9 trigger. The switch waits until it receives a trigger on the rear connector module 9. |
| Ttl0 | Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. |
| Ttl1 | Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. |
| Ttl2 | Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. |
| Ttl3 | Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. |
| Ttl4 | Gets a value corresponding to a trigger on the PXI_TRIG4 line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. |
| Ttl5 | Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. |
| Ttl6 | Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. |
| Ttl7 | Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutputbusline-ttl0.html language=enus -->
## TOPIC 00081: Ttl0

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutputbusline-ttl0.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscanadvancedoutputbusline-ttl0.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl0 { get; }ReturnsReturns the St

### Ttl0

Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl0 { get; }

#### Returns

Returns the String corresponding to the Ttl0 trigger.

Parent topic:

SwitchScanAdvancedOutputBusLine Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl2.html language=enus -->
## TOPIC 00082: Ttl2

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl2.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl2.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl2 { get; }ReturnsReturns the St

### Ttl2

Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl2 { get; }

#### Returns

Returns the String corresponding to the Ttl2 trigger.

Parent topic:

SwitchScanTriggerInput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl4.html language=enus -->
## TOPIC 00083: Ttl4

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl4.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl4.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG4line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl4 { get; }ReturnsReturns the Str

### Ttl4

Gets a value corresponding to a trigger on the PXI_TRIG4line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl4 { get; }

#### Returns

Returns the String corresponding to the Ttl4 trigger.

Parent topic:

SwitchScanTriggerInput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl5.html language=enus -->
## TOPIC 00084: Ttl5

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl5.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscantriggerinput-ttl5.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl5 { get; }ReturnsReturns the St

### Ttl5

Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl5 { get; }

#### Returns

Returns the String corresponding to the Ttl5 trigger.

Parent topic:

SwitchScanTriggerInput Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscantriggerinputbusline-ttl1.html language=enus -->
## TOPIC 00085: Ttl1

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscantriggerinputbusline-ttl1.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscantriggerinputbusline-ttl1.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl1 { get; }ReturnsReturns the St

### Ttl1

Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl1 { get; }

#### Returns

Returns the String corresponding to the Ttl1 trigger.

Parent topic:

SwitchScanTriggerInputBusLine Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchscantriggerinputbusline-ttl5.html language=enus -->
## TOPIC 00086: Ttl5

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchscantriggerinputbusline-ttl5.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchscantriggerinputbusline-ttl5.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static string Ttl5 { get; }ReturnsReturns the St

### Ttl5

Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static string Ttl5 { get; }

#### Returns

Returns the String corresponding to the Ttl5 trigger.

Parent topic:

SwitchScanTriggerInputBusLine Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchwarning-unexpecteddriverwarningcode.html language=enus -->
## TOPIC 00087: UnexpectedDriverWarningCode

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchwarning-unexpecteddriverwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchwarning-unexpecteddriverwarningcode.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code for an unexpected driver warning. SyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic static Guid UnexpectedDriverWarningCode { get; }ReturnsReturns the GUID ("9E568AC9-7D95-406d-8971-D98185DE921C") of the warning.

### UnexpectedDriverWarningCode

Gets the warning code for an unexpected driver warning.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public static Guid UnexpectedDriverWarningCode { get; }

#### Returns

Returns the GUID ("9E568AC9-7D95-406d-8971-D98185DE921C") of the warning.

Parent topic:

SwitchWarning Class

<!--NI_TOPIC bundle=ni-switch-csharp-api-ref path=nationalinstruments-modularinstruments-niswitch-switchwarningeventargs.html language=enus -->
## TOPIC 00088: SwitchWarningEventArgs Class

- bundle_id: `ni-switch-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-niswitch-switchwarningeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-niswitch-switchwarningeventargs.html
- document_id: `ni-switch-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the SwitchWarning event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.ModularInstruments.NISwitchpublic class SwitchWarningEventArgs : EventArgsRemarksFor more information, refer to NI Switches Help. Thread SafetyAll members of this type are safe for multithreaded oper

### SwitchWarningEventArgs Class

Provides data for the [SwitchWarning](nationalinstruments-modularinstruments-niswitch-switchwarning.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NISwitch](nationalinstruments-modularinstruments-niswitch.html)

public class SwitchWarningEventArgs : EventArgs

#### Remarks

For more information, refer to [NI Switches Help](/csh?context=ni-switch_switch_programming).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets the Warning Event Args code. |
| Message | Gets the Warning Event Args message. |
| Warning | Gets the warning set in the Warning Event Args. |

Parent topic:

NationalInstruments.ModularInstruments.NISwitch
