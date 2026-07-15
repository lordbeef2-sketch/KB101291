# NI DOCUMENT BUNDLE: ni-digital-pattern-dot-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-digital-pattern-dot-net-api-ref start=1 end=139 -->
<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/001089b1-0b59-fe7c-b058-d6f201da163e.htm language=enus -->
## TOPIC 00001: ninetdigitalfx40ref/html/001089b1-0b59-fe7c-b058-d6f201da163e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/001089b1-0b59-fe7c-b058-d6f201da163e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/001089b1-0b59-fe7c-b058-d6f201da163e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinInformation Properties

DigitalPinInformation Properties

The [DigitalPinInformation](4bc9e97f-3516-cb4f-f159-84a50b1810f7.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChannelName | Gets the 0-based channel name. |
|  | PinName | Gets the pin name. |
|  | SiteNumber | Gets the site number. |

Top

##### See Also

###### Reference

DigitalPinInformation Structure

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/00bfb770-a323-0dd5-334f-e9b7e8a4008d.htm language=enus -->
## TOPIC 00002: ninetdigitalfx40ref/html/00bfb770-a323-0dd5-334f-e9b7e8a4008d.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/00bfb770-a323-0dd5-334f-e9b7e8a4008d.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/00bfb770-a323-0dd5-334f-e9b7e8a4008d.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalStartTrigger Methods

DigitalStartTrigger Methods

The [DigitalStartTrigger](cd3e7539-8614-cccc-d3c0-dd775a1a49a7.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Disable | Disables a previously configured start trigger and sets TriggerType to None. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalStartTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/012c5b74-388b-be8a-bd0d-6ecf41db64ca.htm language=enus -->
## TOPIC 00003: ninetdigitalfx40ref/html/012c5b74-388b-be8a-bd0d-6ecf41db64ca.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/012c5b74-388b-be8a-bd0d-6ecf41db64ca.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/012c5b74-388b-be8a-bd0d-6ecf41db64ca.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinSet.WriteStatic Method

DigitalPinSetWriteStatic Method

Writes a static state to the channels or pins represented by this pin set. These channels or pins remain in
 the specified state until the next pattern burst or call to this method.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void WriteStatic(
	PinState state
)
```

```text
Public Sub WriteStatic ( 
	state As PinState
)
```

###### Parameters

- **state**
  - Type: NationalInstruments.ModularInstruments.NIDigitalPinState The digital state to write to the channels or pins specified. Valid values are _0, _1, or X: _0 (0)Specifies to drive low._1 (1)Specifies to drive high.X (5)Specifies to put the driver in a non-drive pin state (L, H, X, V, M, E).

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for state is invalid. |

##### Remarks

SelectedFunction

Digital

SelectedFunction

Digital

If there are any changes to [DigitalLevels](ad49c1b4-fa66-1be0-7466-c0f1e54e6a8a.htm) or
 [TerminationMode](fbf03ec8-e738-72b8-59ba-22e2721dd3f0.htm) that have not yet been committed,
 this method commits them prior to writing.

##### See Also

###### Reference

DigitalPinSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0141fa30-73d8-9dac-df69-5188b9e72d1a.htm language=enus -->
## TOPIC 00004: ninetdigitalfx40ref/html/0141fa30-73d8-9dac-df69-5188b9e72d1a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0141fa30-73d8-9dac-df69-5188b9e72d1a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0141fa30-73d8-9dac-df69-5188b9e72d1a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevels.Voh Property

DigitalLevelsVoh Property

Gets or sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H).

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double Voh { get; set; }
```

```text
Public Property Voh As Double
	Get
	Set
```

###### Property Value

Double

The output voltage for a logic high input. The default value is 1.7.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for Voh is invalid. |

##### Remarks

This property is only applicable if [SelectedFunction](62d0b17e-b150-b9bc-eb36-758200f39dac.htm) 
 is set to [Digital](a794b815-cc6f-5dd5-528a-97a46c40f454.htm) for the pin set.

##### See Also

###### Reference

DigitalLevels Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/030bda1a-35d9-94f5-6acc-1d5ee37bc1c9.htm language=enus -->
## TOPIC 00005: ninetdigitalfx40ref/html/030bda1a-35d9-94f5-6acc-1d5ee37bc1c9.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/030bda1a-35d9-94f5-6acc-1d5ee37bc1c9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/030bda1a-35d9-94f5-6acc-1d5ee37bc1c9.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.LoadPinMap Method

NIDigitalLoadPinMap Method

Loads a pin map file.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void LoadPinMap(
	string filePath
)
```

```text
Public Sub LoadPinMap ( 
	filePath As String
)
```

###### Parameters

- **filePath**
  - Type: SystemString The absolute file path to the pin map file.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |

##### Remarks

For more information on using pin maps, refer to [Pin and Channel Map Editor](/csh?topicname=digipat/pin-channel-map-editor.html) in the Digital Pattern Help.

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/037f85c0-4d2c-8b38-77bd-3487c74fb183.htm language=enus -->
## TOPIC 00006: ninetdigitalfx40ref/html/037f85c0-4d2c-8b38-77bd-3487c74fb183.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/037f85c0-4d2c-8b38-77bd-3487c74fb183.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/037f85c0-4d2c-8b38-77bd-3487c74fb183.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.ConfigureEdgeMultiplier Method

DigitalTimeSetConfigureEdgeMultiplier Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureEdgeMultiplier(String, Int32) | Configures the edge multiplier of a time set. |
|  | ConfigureEdgeMultiplier(DigitalPinSet, Int32) | Configures the edge multiplier of a time set. |

Top

##### See Also

###### Reference

DigitalTimeSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0420e88a-7891-cef0-40f5-91c390bffe56.htm language=enus -->
## TOPIC 00007: ninetdigitalfx40ref/html/0420e88a-7891-cef0-40f5-91c390bffe56.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0420e88a-7891-cef0-40f5-91c390bffe56.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0420e88a-7891-cef0-40f5-91c390bffe56.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverOperation.ResetInterchangeCheck Method

DigitalDriverOperationResetInterchangeCheck Method

Resets the interchangeability checking algorithms of the NI-Digital Pattern Driver software 
 so that methods and properties that executed prior to calling this 
 method have no effect on whether future calls to the driver 
 generate interchangeability warnings.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ResetInterchangeCheck()
```

```text
Public Sub ResetInterchangeCheck
```

###### Implements

##### See Also

###### Reference

DigitalDriverOperation Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0485c29d-8eba-2e79-3615-663d7ef6cc39.htm language=enus -->
## TOPIC 00008: ninetdigitalfx40ref/html/0485c29d-8eba-2e79-3615-663d7ef6cc39.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0485c29d-8eba-2e79-3615-663d7ef6cc39.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0485c29d-8eba-2e79-3615-663d7ef6cc39.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

PpmuCurrentLimitBehavior Enumeration

PpmuCurrentLimitBehavior Enumeration

The output current's behavior when the current limit is reached.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public enum PpmuCurrentLimitBehavior
```

```text
Public Enumeration PpmuCurrentLimitBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | CurrentRegulate | 3100 | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/04923343-eecd-0149-38bd-b7146c418d69.htm language=enus -->
## TOPIC 00009: ninetdigitalfx40ref/html/04923343-eecd-0149-38bd-b7146c418d69.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/04923343-eecd-0149-38bd-b7146c418d69.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/04923343-eecd-0149-38bd-b7146c418d69.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceWaveforms.CreateSerial Method (DigitalPinSet, String, SourceDataMapping, UInt32, BitOrder)

DigitalSourceWaveformsCreateSerial Method (DigitalPinSet, String, SourceDataMapping, UInt32, BitOrder)

DigitalPinSet

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateSerial(
	DigitalPinSet pinSet,
	string waveformName,
	SourceDataMapping dataMapping,
	uint sampleWidth,
	BitOrder bitOrder
)
```

```text
Public Sub CreateSerial ( 
	pinSet As DigitalPinSet,
	waveformName As String,
	dataMapping As SourceDataMapping,
	sampleWidth As UInteger,
	bitOrder As BitOrder
)
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The set of pins or channels for which to create the waveform. The pinSet must match the source pins in the pattern that references the waveform. The pin order in the pin set determines the bit positions of the data written using one of the write waveform methods on the DigitalSourceWaveforms object.
- **waveformName**
  - Type: SystemString The name of the waveform to use in the pattern file. Waveform names must be unique. Use the waveformName with source_start opcode in your pattern.
- **dataMapping**
  - Type: NationalInstruments.ModularInstruments.NIDigitalSourceDataMapping Specifies whether the waveform is broadcast to all sites or a unique waveform is sourced per site.
- **sampleWidth**
  - Type: SystemUInt32 The width in bits of each serial sample. Valid values are between 1 and 32.
- **bitOrder**
  - Type: NationalInstruments.ModularInstruments.NIDigitalBitOrder The bit order significance. This can be most significant bit first or least significant bit first. MostSignificantBitFirst is the default value.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| ArgumentException | The value for waveformName is an empty string or contains an invalid character. |
| OutOfRangeException | The value for dataMapping is invalid.The value for sampleWidth is invalid.The value for bitOrder is invalid.The number of waveforms in source memory exceeds maximum number of waveforms allowed. |

##### Remarks

You cannot reconfigure settings after waveforms are created.

Opcodes

Source Waveform Configurations

##### See Also

###### Reference

DigitalSourceWaveforms Class

CreateSerial Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/04eae5c3-a542-3bd8-f4f3-41c932e3f53b.htm language=enus -->
## TOPIC 00010: ninetdigitalfx40ref/html/04eae5c3-a542-3bd8-f4f3-41c932e3f53b.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/04eae5c3-a542-3bd8-f4f3-41c932e3f53b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/04eae5c3-a542-3bd8-f4f3-41c932e3f53b.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCVoltage.ConfigureCurrentLimit Method

DigitalSourceDCVoltageConfigureCurrentLimit Method

Configures the current limit for the pin set when forcing voltage.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureCurrentLimit(
	PpmuCurrentLimitBehavior behavior,
	double limit
)
```

```text
Public Sub ConfigureCurrentLimit ( 
	behavior As PpmuCurrentLimitBehavior,
	limit As Double
)
```

###### Parameters

- **behavior**
  - Type: NationalInstruments.ModularInstruments.NIDigitalPpmuCurrentLimitBehaviorSpecifies how the output current behaves when the current limit is reached.
- **limit**
  - Type: SystemDoubleSpecifies the current limit, in amps, on the pins. The valid values for this parameter are defined by the CurrentLimitRange property.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for behavior is invalid.The value for limit is invalid. |

##### Remarks

OutputFunction

DCVoltage

limit

If the current required by the DUT exceeds the selected [CurrentLimitRange](a9bc6206-439a-462a-8498-51ef00dfe10b.htm), the voltage output may not meet the specified voltage level. Choose a larger current limit range if needed.

Changing this property does not take affect until you call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm). 
 You can call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm) to commit your changes even if the PPMU
 is already sourcing.

Not all instruments support this capability. Use the [IsCurrentLimitSupported](c6550a86-e0d6-a8ed-9e40-b1faee6420e0.htm) property to programmatically determine whether an instrument supports this capability. If high-accuracy current clamping functionality is required, consider using a Source Measure Unit (SMU) instrument.

##### See Also

###### Reference

DigitalSourceDCVoltage Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/06d21fb1-731d-1599-eea6-875c019c7f51.htm language=enus -->
## TOPIC 00011: ninetdigitalfx40ref/html/06d21fb1-731d-1599-eea6-875c019c7f51.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/06d21fb1-731d-1599-eea6-875c019c7f51.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/06d21fb1-731d-1599-eea6-875c019c7f51.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTiming.DeleteAllTimeSets Method

DigitalTimingDeleteAllTimeSets Method

Deletes all loaded and created time sets.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void DeleteAllTimeSets()
```

```text
Public Sub DeleteAllTimeSets
```

##### See Also

###### Reference

DigitalTiming Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/071c4453-965a-ae3d-a4cc-fea8649dc131.htm language=enus -->
## TOPIC 00012: ninetdigitalfx40ref/html/071c4453-965a-ae3d-a4cc-fea8649dc131.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/071c4453-965a-ae3d-a4cc-fea8649dc131.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/071c4453-965a-ae3d-a4cc-fea8649dc131.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalCaptureWaveforms.CreateParallel Method (String, String)

DigitalCaptureWaveformsCreateParallel Method (String, String)

Creates the capture waveform settings for parallel acquisition using a comma-delimited string of pins or channels.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateParallel(
	string pinSetString,
	string waveformName
)
```

```text
Public Sub CreateParallel ( 
	pinSetString As String,
	waveformName As String
)
```

###### Parameters

- **pinSetString**
  - Type: SystemString The set of pins or channels to create the waveform for.
- **waveformName**
  - Type: SystemStringSpecifies the waveform name to use. Use the waveformName with the capture_start opcode in your pattern.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| InvalidOperationException | The value for pinSetString contains a system pin. |
| ArgumentException | The value for waveformName is an empty string or contains an invalid character. |
| OutOfRangeException | The number of waveforms in capture memory exceeds the maximum number of waveforms allowed. |

##### Remarks

Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

Refer to [Working with Pin Sets](/csh?topicname=ninetdigitalfx40/net-pin-sets.html) for more information.

##### See Also

###### Reference

DigitalCaptureWaveforms Class

CreateParallel Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0834051d-634e-7a5a-2350-aee669e63641.htm language=enus -->
## TOPIC 00013: ninetdigitalfx40ref/html/0834051d-634e-7a5a-2350-aee669e63641.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0834051d-634e-7a5a-2350-aee669e63641.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0834051d-634e-7a5a-2350-aee669e63641.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalStartTrigger.OutputTerminal Property

DigitalStartTriggerOutputTerminal Property

Gets or sets the destination terminal for exporting the start trigger.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string OutputTerminal { get; set; }
```

```text
Public Property OutputTerminal As String
	Get
	Set
```

###### Property Value

String

##### Remarks

Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, 
 you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

##### See Also

###### Reference

DigitalStartTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/090a1180-cb94-a963-0ce4-4fd4237ea04f.htm language=enus -->
## TOPIC 00014: ninetdigitalfx40ref/html/090a1180-cb94-a963-0ce4-4fd4237ea04f.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/090a1180-cb94-a963-0ce4-4fd4237ea04f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/090a1180-cb94-a963-0ce4-4fd4237ea04f.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalStartTrigger.TriggerType Property

DigitalStartTriggerTriggerType Property

DigitalStartTrigger

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public TriggerType TriggerType { get; set; }
```

```text
Public Property TriggerType As TriggerType
	Get
	Set
```

###### Property Value

TriggerType

DigitalStartTrigger

None

##### Exceptions

| Exception | Condition |
| --- | --- |
| OutOfRangeException | The value for TriggerType is invalid. |

##### Remarks

The digital pattern instrument waits for this trigger after you initiate a pattern burst and does not burst a pattern until this trigger is received.

##### See Also

###### Reference

DigitalStartTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0975f385-0fd4-ae02-ed0f-caf8e5696bb5.htm language=enus -->
## TOPIC 00015: ninetdigitalfx40ref/html/0975f385-0fd4-ae02-ed0f-caf8e5696bb5.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0975f385-0fd4-ae02-ed0f-caf8e5696bb5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0975f385-0fd4-ae02-ed0f-caf8e5696bb5.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.WriteSequencerRegister Method

DigitalPatternControlWriteSequencerRegister Method

Writes a value to a pattern sequencer register.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void WriteSequencerRegister(
	string register,
	int value
)
```

```text
Public Sub WriteSequencerRegister ( 
	register As String,
	value As Integer
)
```

###### Parameters

- **register**
  - Type: SystemStringSpecifies the sequencer register to which you would like to write the specified value.
- **value**
  - Type: SystemInt32The value to write to the specified pattern sequence register.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| ArgumentException | The value for register is invalid.The value for value is invalid. |

##### Remarks

Use pattern sequencer registers to pass numeric values between the pattern sequencer and a run-time test program.

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0a306580-21b4-e63a-a905-4599ca3790cf.htm language=enus -->
## TOPIC 00016: ninetdigitalfx40ref/html/0a306580-21b4-e63a-a905-4599ca3790cf.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0a306580-21b4-e63a-a905-4599ca3790cf.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0a306580-21b4-e63a-a905-4599ca3790cf.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.SourceWaveforms Property

NIDigitalSourceWaveforms Property

DigitalSourceWaveforms

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalSourceWaveforms SourceWaveforms { get; }
```

```text
Public ReadOnly Property SourceWaveforms As DigitalSourceWaveforms
	Get
```

###### Property Value

DigitalSourceWaveforms

NIDigital

##### Remarks

For more information on source and capture functionality, refer to [Source and Capture](/csh?topicname=digipat6570/source-capture.html) in the Digital Pattern Help.

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0b9a4453-32ab-cc1c-66ed-0c7ea1ca3cb0.htm language=enus -->
## TOPIC 00017: ninetdigitalfx40ref/html/0b9a4453-32ab-cc1c-66ed-0c7ea1ca3cb0.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0b9a4453-32ab-cc1c-66ed-0c7ea1ca3cb0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0b9a4453-32ab-cc1c-66ed-0c7ea1ca3cb0.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPpmu.DCVoltage Property

DigitalPpmuDCVoltage Property

DigitalSourceDCVoltage

OutputFunction

DCVoltage

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalSourceDCVoltage DCVoltage { get; }
```

```text
Public ReadOnly Property DCVoltage As DigitalSourceDCVoltage
	Get
```

###### Property Value

DigitalSourceDCVoltage

OutputFunction

DCVoltage

DigitalPpmu

##### See Also

###### Reference

DigitalPpmu Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0ca049e3-cc8f-2b9a-c200-c136b8f4bee5.htm language=enus -->
## TOPIC 00018: ninetdigitalfx40ref/html/0ca049e3-cc8f-2b9a-c200-c136b8f4bee5.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0ca049e3-cc8f-2b9a-c200-c136b8f4bee5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0ca049e3-cc8f-2b9a-c200-c136b8f4bee5.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinAndChannelMap.EndChannelMap Method

DigitalPinAndChannelMapEndChannelMap Method

Completes the channel map configuration. No further changes can be made to the channel
 map or connections after calling this method.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void EndChannelMap()
```

```text
Public Sub EndChannelMap
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| InvalidOperationException | EndChannelMap is called before calling CreateChannelMap(Int32). |

##### Remarks

MapPinToChannel(String, Int32, String)

You must use [CreateChannelMap(Int32)](afde1123-ab34-f058-75b2-a35a417c3ced.htm)
 to begin creating a channel map, and you must call EndChannelMap
 to finalize the creation of that channel map.

##### See Also

###### Reference

DigitalPinAndChannelMap Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0ca924b3-dcdd-12f4-1ba2-dc96b37b5654.htm language=enus -->
## TOPIC 00019: ninetdigitalfx40ref/html/0ca924b3-dcdd-12f4-1ba2-dc96b37b5654.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0ca924b3-dcdd-12f4-1ba2-dc96b37b5654.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0ca924b3-dcdd-12f4-1ba2-dc96b37b5654.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinSet.Ppmu Property

DigitalPinSetPpmu Property

DigitalPpmu

SelectedFunction

Ppmu

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalPpmu Ppmu { get; }
```

```text
Public ReadOnly Property Ppmu As DigitalPpmu
	Get
```

###### Property Value

DigitalPpmu

Object used to configure and control PPMU. This object is created when the
 [DigitalPinSet](825d6612-d621-a76f-a885-7a42ba0f539b.htm) is created.

##### Remarks

You can use this property to begin sourcing or measuring current and voltage.

##### See Also

###### Reference

DigitalPinSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0d931469-2e5e-51c6-8ed5-f1a351c8d4f9.htm language=enus -->
## TOPIC 00020: ninetdigitalfx40ref/html/0d931469-2e5e-51c6-8ed5-f1a351c8d4f9.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0d931469-2e5e-51c6-8ed5-f1a351c8d4f9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0d931469-2e5e-51c6-8ed5-f1a351c8d4f9.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSoftwareConditionalJumpTrigger Methods

DigitalSoftwareConditionalJumpTrigger Methods

The [DigitalSoftwareConditionalJumpTrigger](324ef012-8ad2-652e-b8b5-00a87211ba5a.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the TriggerType for Software triggering. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | Send | Sends the Software Conditional Jump Trigger to a digital pattern instrument, forcing the Conditional Jump Trigger to assert, regardless of how the Conditional Jump Trigger is configured. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalSoftwareConditionalJumpTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0dd6495d-5e05-e571-59c4-5d55fd80c445.htm language=enus -->
## TOPIC 00021: ninetdigitalfx40ref/html/0dd6495d-5e05-e571-59c4-5d55fd80c445.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0dd6495d-5e05-e571-59c4-5d55fd80c445.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0dd6495d-5e05-e571-59c4-5d55fd80c445.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility Methods

DigitalDriverUtility Methods

The [DigitalDriverUtility](28a057c7-ce12-b9b9-334c-63df5caf985f.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Disable | Places the instrument in an inactive state as quickly as possible. |
|  | Dispose | Disposes the DigitalDriverUtility object. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | ErrorQuery | Reads an error code and the associated message from the NI-Digital Pattern Driver software error queue. |
|  | GetChannelName | Returns the channel name given a Int32 one-based index. |
|  | GetChannelNameFromString | Returns a comma-separated channel name list given a String index list. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPinResultsPinInformation(String) | Returns an array of pins and an array of sites corresponding to the specified channel list. |
|  | GetPinResultsPinInformation(DigitalPinSet) | Gets an array of pins or channels corresponding to the specified pin set. |
|  | GetSiteResultsSiteNumbers | Returns the site numbers that correspond to per-site data read from the digital pattern instrument. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Lock | Acquires a synchronization lock on this instance of the driver. |
|  | Lock(PrecisionTimeSpan) | Acquires a synchronization lock on this instance of the driver. |
|  | Reset | Resets the digital pattern instrument to a known state. |
|  | ResetAttribute(Int32) | Resets a driver attribute to its default state. |
|  | ResetAttribute(String, Int32) | Resets a driver attribute to its default state using a string to specify pins, pin groups, or channels. |
|  | ResetAttribute(DigitalPinSet, Int32) | Resets a driver attribute to its default state using a DigitalPinSet. |
|  | ResetDevice | Returns the digital pattern instrument to a known state. |
|  | ResetWithDefaults | Resets the digital pattern instrument to a known state, while also resetting properties and settings to the initial values specified during the construction of the NIDigital session. |
|  | SelfTest | Performs a self-test on the digital pattern instrument and returns the test result. |
|  | SortPinResultsBySite(NIDigital, String, Byte, String, Int32) | Organizes data read from multiple digital pattern instruments by grouping the data by site number. |
|  | SortPinResultsBySite(NIDigital, String, Double, String, Int32) | Organizes data read from multiple digital pattern instruments by grouping the data by site number. |
|  | SortPinResultsBySite(NIDigital, String, Int64, String, Int32) | Organizes data read from multiple digital pattern instruments by grouping the data by site number. |
|  | SortSiteResultsBySite(NIDigital, String, SiteResultType, Boolean, Int32) | Orders site data read from multiple instruments to match the site list you specify, and combines data from instruments mapped to the same site. |
|  | SortSiteResultsBySite(NIDigital, String, SiteResultType, UInt32, Int32) | Orders site data read from multiple instruments to match the site list you specify, and combines data from instruments mapped to the same site. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalDriverUtility Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/0f93d706-5748-70c0-17d5-b18bac4a9f2b.htm language=enus -->
## TOPIC 00022: ninetdigitalfx40ref/html/0f93d706-5748-70c0-17d5-b18bac4a9f2b.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/0f93d706-5748-70c0-17d5-b18bac4a9f2b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/0f93d706-5748-70c0-17d5-b18bac4a9f2b.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital Constructor

NIDigital Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | NIDigital(IntPtr) | Initializes a new instance of the NIDigital class. Initializes an instrument driver session from an existing instrument handle. |
|  | NIDigital(String, Boolean, Boolean) | Initializes a new instance of the NIDigital class. Initializes a digital pattern instrument driver session and sets the initial state of session properties. |
|  | NIDigital(String, Boolean, Boolean, String) | Initializes a new instance of the NIDigital class. This overload is reserved for future use. |

Top

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/149c2f1f-a770-3a7e-23bf-b0ee03734025.htm language=enus -->
## TOPIC 00023: ninetdigitalfx40ref/html/149c2f1f-a770-3a7e-23bf-b0ee03734025.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/149c2f1f-a770-3a7e-23bf-b0ee03734025.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/149c2f1f-a770-3a7e-23bf-b0ee03734025.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalCaptureWaveforms.CreateSerial Method (DigitalPinSet, String, UInt32, BitOrder)

DigitalCaptureWaveformsCreateSerial Method (DigitalPinSet, String, UInt32, BitOrder)

DigitalPinSet

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateSerial(
	DigitalPinSet pinSet,
	string waveformName,
	uint sampleWidth,
	BitOrder bitOrder
)
```

```text
Public Sub CreateSerial ( 
	pinSet As DigitalPinSet,
	waveformName As String,
	sampleWidth As UInteger,
	bitOrder As BitOrder
)
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The set of pins or channels for which to create the waveform.
- **waveformName**
  - Type: SystemStringSpecifies the waveform name to use. Use the waveformName with the capture_start opcode in your pattern.
- **sampleWidth**
  - Type: SystemUInt32 The width in bits of each serial sample. Valid values are between 1 and 32.
- **bitOrder**
  - Type: NationalInstruments.ModularInstruments.NIDigitalBitOrder The order in which to shift the bits. This can be most significant bit first or least significant bit first.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| InvalidOperationException | The pinSet contains a system pin. |
| ArgumentException | The value for waveformName is an empty string or contains an invalid character.The value for sampleWidth is invalid.The value for bitOrder is invalid. |
| OutOfRangeException | The number of waveforms in capture memory exceeds the maximum number of waveforms allowed. |

##### Remarks

The number of waveforms is limited to 512.

##### See Also

###### Reference

DigitalCaptureWaveforms Class

CreateSerial Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/14bcb1bd-5b40-e388-064d-d9202e455ae4.htm language=enus -->
## TOPIC 00024: ninetdigitalfx40ref/html/14bcb1bd-5b40-e388-064d-d9202e455ae4.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/14bcb1bd-5b40-e388-064d-d9202e455ae4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/14bcb1bd-5b40-e388-064d-d9202e455ae4.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCVoltage.CurrentLimit Property

DigitalSourceDCVoltageCurrentLimit Property

Gets or sets the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double CurrentLimit { get; set; }
```

```text
Public Property CurrentLimit As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |

##### Remarks

SelectedFunction

Ppmu

OutputFunction

DCVoltage

The PXIe-6570 and the PXIe-6571 do not support CurrentLimit, 
 and only allow the configuration of the [CurrentLimitRange](a9bc6206-439a-462a-8498-51ef00dfe10b.htm).

##### See Also

###### Reference

DigitalSourceDCVoltage Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/15937c43-891c-ef62-f284-b9a2fbfed1ef.htm language=enus -->
## TOPIC 00025: ninetdigitalfx40ref/html/15937c43-891c-ef62-f284-b9a2fbfed1ef.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/15937c43-891c-ef62-f284-b9a2fbfed1ef.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/15937c43-891c-ef62-f284-b9a2fbfed1ef.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinSet.ReadStatic Method

DigitalPinSetReadStatic Method

Reads the current state of comparators for the specified channels or pins.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PinState[] ReadStatic()
```

```text
Public Function ReadStatic As PinState()
```

###### Return Value

PinState

DigitalPinSet

GetPinSet(String)

GetPinResultsPinInformation(String)

Possible values are a logic low pin state ([L](9d9dc500-3675-9af4-49f6-a92441c45b6c.htm)),
 a logic high pin state ([H](9d9dc500-3675-9af4-49f6-a92441c45b6c.htm)),
 a midband pin state ([M](9d9dc500-3675-9af4-49f6-a92441c45b6c.htm)),
 or a value that is above Voh and below Vol, which can occur when you set Vol higher than Voh (V).

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |

##### Remarks

DigitalLevels

TerminationMode

##### See Also

###### Reference

DigitalPinSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/15eab349-2dad-3fd4-fbf1-a5ca77181f83.htm language=enus -->
## TOPIC 00026: ninetdigitalfx40ref/html/15eab349-2dad-3fd4-fbf1-a5ca77181f83.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/15eab349-2dad-3fd4-fbf1-a5ca77181f83.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/15eab349-2dad-3fd4-fbf1-a5ca77181f83.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeStartTrigger Class

DigitalEdgeStartTrigger Class

Contains properties and methods to configure and control the start trigger as a digital edge start trigger.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public class DigitalEdgeStartTrigger : DigitalSubObject
```

```text
Public Class DigitalEdgeStartTrigger
	Inherits DigitalSubObject
```

The DigitalEdgeStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Edge | Gets or sets the active edge for the start trigger. |
|  | Source | Gets or sets the source terminal for the start trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the TriggerType to Software, and configures the DigitalEdge and Edge properties. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/16064312-ca50-9fec-6613-f2552fc18191.htm language=enus -->
## TOPIC 00027: ninetdigitalfx40ref/html/16064312-ca50-9fec-6613-f2552fc18191.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/16064312-ca50-9fec-6613-f2552fc18191.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/16064312-ca50-9fec-6613-f2552fc18191.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCCurrent.VoltageLimitHigh Property

DigitalSourceDCCurrentVoltageLimitHigh Property

Gets or sets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double VoltageLimitHigh { get; set; }
```

```text
Public Property VoltageLimitHigh As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for VoltageLimitHigh is invalid. |

##### Remarks

This property is only applicable when you set the [SelectedFunction](62d0b17e-b150-b9bc-eb36-758200f39dac.htm) of the pin set
 to [Ppmu](a794b815-cc6f-5dd5-528a-97a46c40f454.htm) and set the PPMU
 [OutputFunction](655db2b5-0c24-cfe7-a61f-56272413faed.htm) to
 [DCCurrent](a50bb129-cc85-c191-93e2-ebdb282f0bcd.htm).

##### See Also

###### Reference

DigitalSourceDCCurrent Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/16075be3-d98e-4119-2ec7-049017c0ceb7.htm language=enus -->
## TOPIC 00028: ninetdigitalfx40ref/html/16075be3-d98e-4119-2ec7-049017c0ceb7.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/16075be3-d98e-4119-2ec7-049017c0ceb7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/16075be3-d98e-4119-2ec7-049017c0ceb7.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.Reset Method

DigitalDriverUtilityReset Method

Resets the digital pattern instrument to a known state.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void Reset()
```

```text
Public Sub Reset
```

###### Implements

##### Remarks

When this method is called, all pin drivers are put in a non-drive state, the active load and PPMUs are disconnected, and the I/O switches are opened. Also, pin map and time set configurations are cleared.

##### See Also

###### Reference

DigitalDriverUtility Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/18239669-5397-ac2e-8ed3-c8cd348d59ea.htm language=enus -->
## TOPIC 00029: ninetdigitalfx40ref/html/18239669-5397-ac2e-8ed3-c8cd348d59ea.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/18239669-5397-ac2e-8ed3-c8cd348d59ea.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/18239669-5397-ac2e-8ed3-c8cd348d59ea.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeConditionalJumpTrigger.Edge Property

DigitalEdgeConditionalJumpTriggerEdge Property

Gets or sets the active edge for the Conditional Jump Trigger.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalEdge Edge { get; set; }
```

```text
Public Property Edge As DigitalEdge
	Get
	Set
```

###### Property Value

DigitalEdge

The active edge for the Conditional Jump Trigger. This property is used when [TriggerType](7bdc5aa4-8b80-1b20-d6f5-15c12915cc44.htm) is set to
 [DigitalEdge](2d52a4c4-a149-d68c-3ce9-8c8e00fda490.htm). The default value is [Rising](702a95b8-60fe-7809-c1ff-ea6bca169a1f.htm).

##### Exceptions

| Exception | Condition |
| --- | --- |
| OutOfRangeException | The value for Edge is invalid. |

##### See Also

###### Reference

DigitalEdgeConditionalJumpTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/19c68c67-db34-fb32-b393-e0e4d15f7845.htm language=enus -->
## TOPIC 00030: ninetdigitalfx40ref/html/19c68c67-db34-fb32-b393-e0e4d15f7845.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/19c68c67-db34-fb32-b393-e0e4d15f7845.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/19c68c67-db34-fb32-b393-e0e4d15f7845.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSoftwareConditionalJumpTrigger.Send Method

DigitalSoftwareConditionalJumpTriggerSend Method

Sends the Software Conditional Jump Trigger to a digital pattern instrument, forcing the Conditional Jump
 Trigger to assert, regardless of how the Conditional Jump Trigger is configured.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void Send()
```

```text
Public Sub Send
```

##### See Also

###### Reference

DigitalSoftwareConditionalJumpTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/1b18b668-832a-9ec1-65be-d67c75747c5b.htm language=enus -->
## TOPIC 00031: ninetdigitalfx40ref/html/1b18b668-832a-9ec1-65be-d67c75747c5b.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/1b18b668-832a-9ec1-65be-d67c75747c5b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/1b18b668-832a-9ec1-65be-d67c75747c5b.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.ConfigureDriveEdges Method (String, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

DigitalTimeSetConfigureDriveEdges Method (String, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

Configures the drive format and the drive edge placement for the specified pins.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDriveEdges(
	string pinSetString,
	DriveFormat format,
	PrecisionTimeSpan driveOnEdge,
	PrecisionTimeSpan driveDataEdge,
	PrecisionTimeSpan driveReturnEdge,
	PrecisionTimeSpan driveOffEdge
)
```

```text
Public Sub ConfigureDriveEdges ( 
	pinSetString As String,
	format As DriveFormat,
	driveOnEdge As PrecisionTimeSpan,
	driveDataEdge As PrecisionTimeSpan,
	driveReturnEdge As PrecisionTimeSpan,
	driveOffEdge As PrecisionTimeSpan
)
```

###### Parameters

- **pinSetString**
  - Type: SystemString The pin set specified as a comma-delimited list of pins for which to configure the time set edges.
- **format**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDriveFormat The drive format of the time set.
- **driveOnEdge**
  - Type: Ivi.DriverPrecisionTimeSpan The delay from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive PinState (L, H, X, V, M, E). For the SurroundByComplement format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.
- **driveDataEdge**
  - Type: Ivi.DriverPrecisionTimeSpan The delay from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point.
- **driveReturnEdge**
  - Type: Ivi.DriverPrecisionTimeSpan The delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.
- **driveOffEdge**
  - Type: Ivi.DriverPrecisionTimeSpan The delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive PinState (L, H, X, V, M, E).

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | An instance of DigitalTimeSet represents a time set name that has not yet been applied.The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for format is invalid.The value for driveOnEdge is invalid.The value for driveDataEdge is invalid.The value for driveReturnEdge is invalid.The value for driveOffEdge is invalid. |

##### Remarks

Not all edges apply to all drive formats.

##### See Also

###### Reference

DigitalTimeSet Class

ConfigureDriveEdges Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/1b332f7a-aeb7-49f5-9e63-8c9859fd3948.htm language=enus -->
## TOPIC 00032: ninetdigitalfx40ref/html/1b332f7a-aeb7-49f5-9e63-8c9859fd3948.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/1b332f7a-aeb7-49f5-9e63-8c9859fd3948.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/1b332f7a-aeb7-49f5-9e63-8c9859fd3948.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.GetEdgeMultiplier Method (DigitalPinSet)

DigitalTimeSetGetEdgeMultiplier Method (DigitalPinSet)

Gets the edge multiplier of a time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public int GetEdgeMultiplier(
	DigitalPinSet pinSet
)
```

```text
Public Function GetEdgeMultiplier ( 
	pinSet As DigitalPinSet
) As Integer
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The pin set for which to get the edge multiplier.

###### Return Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

##### See Also

###### Reference

DigitalTimeSet Class

GetEdgeMultiplier Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/1c11ecc1-3e70-0752-bcaf-3e0e6f41374a.htm language=enus -->
## TOPIC 00033: ninetdigitalfx40ref/html/1c11ecc1-3e70-0752-bcaf-3e0e6f41374a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/1c11ecc1-3e70-0752-bcaf-3e0e6f41374a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/1c11ecc1-3e70-0752-bcaf-3e0e6f41374a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevels.Vol Property

DigitalLevelsVol Property

Gets or sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L).

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double Vol { get; set; }
```

```text
Public Property Vol As Double
	Get
	Set
```

###### Property Value

Double

The maximum output voltage for a logic low output. The default value is 1.6.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for Vol is invalid. |

##### Remarks

This property is only applicable if [SelectedFunction](62d0b17e-b150-b9bc-eb36-758200f39dac.htm) 
 is set to [Digital](a794b815-cc6f-5dd5-528a-97a46c40f454.htm) for the pin set.

##### See Also

###### Reference

DigitalLevels Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/1c529be6-0b51-c6db-3d5e-d862640febac.htm language=enus -->
## TOPIC 00034: ninetdigitalfx40ref/html/1c529be6-0b51-c6db-3d5e-d862640febac.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/1c529be6-0b51-c6db-3d5e-d862640febac.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/1c529be6-0b51-c6db-3d5e-d862640febac.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.GetPinResultsPinInformation Method

DigitalDriverUtilityGetPinResultsPinInformation Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetPinResultsPinInformation(String) | Returns an array of pins and an array of sites corresponding to the specified channel list. |
|  | GetPinResultsPinInformation(DigitalPinSet) | Gets an array of pins or channels corresponding to the specified pin set. |

Top

##### See Also

###### Reference

DigitalDriverUtility Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/1d7eccbd-cddb-262c-51f0-e0b10b58efa9.htm language=enus -->
## TOPIC 00035: ninetdigitalfx40ref/html/1d7eccbd-cddb-262c-51f0-e0b10b58efa9.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/1d7eccbd-cddb-262c-51f0-e0b10b58efa9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/1d7eccbd-cddb-262c-51f0-e0b10b58efa9.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinAndChannelMap.CreatePinGroup Method

DigitalPinAndChannelMapCreatePinGroup Method

Creates a pin group with the specified name. The pin group serves as an alias for a list
 of pins.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreatePinGroup(
	string name,
	string[] pins
)
```

```text
Public Sub CreatePinGroup ( 
	name As String,
	pins As String()
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the pin group to create.
- **pins**
  - Type: SystemString A one-dimensional array of strings that contains pin(s), pin group(s), and/or channel(s) to include in the pin group.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| ArgumentException | The value for name has invalid characters. |
| SelectorNameException | pins contains an invalid pin. |

##### See Also

###### Reference

DigitalPinAndChannelMap Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/1e538a6a-c4ed-1971-dbd5-d5ef3945d87a.htm language=enus -->
## TOPIC 00036: ninetdigitalfx40ref/html/1e538a6a-c4ed-1971-dbd5-d5ef3945d87a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/1e538a6a-c4ed-1971-dbd5-d5ef3945d87a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/1e538a6a-c4ed-1971-dbd5-d5ef3945d87a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRamCycleInformation.ExpectedPinStates Property

DigitalHistoryRamCycleInformationExpectedPinStates Property

Gets the pin state as expected by the loaded pattern in the order specified in pinList. Pins without defined edges in the specified DUT cycle will return NotAPinState.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PinState[][] ExpectedPinStates { get; }
```

```text
Public ReadOnly Property ExpectedPinStates As PinState()()
	Get
```

###### Property Value

PinState

##### Remarks

The first dimension is the DUT cycle index and the second dimension is the expected pin states.
 Only the first row will have expected pin states if the edge multiplier is 1.
 If the edge multiplier is greater than one, additional rows will be populated.

##### See Also

###### Reference

DigitalHistoryRamCycleInformation Structure

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/2014351c-287a-a6dd-68dc-ffff40386efe.htm language=enus -->
## TOPIC 00037: ninetdigitalfx40ref/html/2014351c-287a-a6dd-68dc-ffff40386efe.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/2014351c-287a-a6dd-68dc-ffff40386efe.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/2014351c-287a-a6dd-68dc-ffff40386efe.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital Properties

NIDigital Properties

The [NIDigital](b1c44701-b544-edf5-7a71-8f814cb19a16.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | CaptureWaveforms | Gets the DigitalCaptureWaveforms object containing methods for creating and fetching capture waveforms. |
|  | DriverOperation | Gets the DigitalDriverOperation object containing methods and properties that manage the operation of the driver. |
|  | Event | Gets the DigitalEvent object that contains the events for the NIDigital session. |
|  | HistoryRam | Gets the DigitalHistoryRam object containing methods for configuring and fetching History RAM contents. |
|  | Identity | Gets the DigitalDriverIdentity object, which contains properties that return information about the identity of the NI-Digital Pattern Driver software. |
|  | IsDisposed | Gets a value indicating whether the NIDigital session has been disposed. |
|  | NumberOfChannels | Gets the number of channels on the digital pattern instrument. |
|  | PatternControl | Gets the DigitalPatternControl control object, containing properties and methods for setting up and bursting a pattern. |
|  | PinAndChannelMap | Gets the DigitalPinAndChannelMap object that stores all the pin mapping information for the NIDigital session. |
|  | SourceWaveforms | Gets the DigitalSourceWaveforms object containing the functionality for creating and writing source waveforms. |
|  | Timing | Gets the DigitalTiming object that stores the time sets for the NIDigital session. |
|  | Trigger | Gets the DigitalTrigger object that contains the triggers for the NIDigital session. |
|  | Utility | Gets the DigitalDriverUtility object containing methods providing utility operations for the NI-Digital Pattern Driver. |

Top

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/24e92b80-d88d-2d87-a80a-036714c69e06.htm language=enus -->
## TOPIC 00038: ninetdigitalfx40ref/html/24e92b80-d88d-2d87-a80a-036714c69e06.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/24e92b80-d88d-2d87-a80a-036714c69e06.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/24e92b80-d88d-2d87-a80a-036714c69e06.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet Class

DigitalTimeSet Class

ApplyLevelsAndTiming(String, String, String)

ApplyLevelsAndTiming(String, String, String)

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalTimeSet : DigitalSubObject
```

```text
Public NotInheritable Class DigitalTimeSet
	Inherits DigitalSubObject
```

The DigitalTimeSet type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Name | Gets the name of the time set. |
|  | Period | Gets or sets the period of the time set. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureCompareEdgesStrobe(String, PrecisionTimeSpan) | Configures the strobe edge time for the specified pins. |
|  | ConfigureCompareEdgesStrobe(DigitalPinSet, PrecisionTimeSpan) | Configures the strobe edge time for the specified pin set. |
|  | ConfigureCompareEdgesStrobe(String, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the strobe edge times for the specified pins. |
|  | ConfigureCompareEdgesStrobe(DigitalPinSet, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the strobe edge times for the specified pin set. |
|  | ConfigureDriveEdges(String, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and the drive edge placement for the specified pins. |
|  | ConfigureDriveEdges(DigitalPinSet, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and drive edge placement for the specified pin set. |
|  | ConfigureDriveEdges(String, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and the drive edge placement for the specified pins. |
|  | ConfigureDriveEdges(DigitalPinSet, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and drive edge placement for the specified pin set. |
|  | ConfigureDriveFormat(String, DriveFormat) | Configures the drive format of a time set. |
|  | ConfigureDriveFormat(DigitalPinSet, DriveFormat) | Configures the drive format of a time set. |
|  | ConfigureEdge(String, TimeSetEdge, PrecisionTimeSpan) | Configures the edge of a time set. |
|  | ConfigureEdge(DigitalPinSet, TimeSetEdge, PrecisionTimeSpan) | Configures the edge of a time set. |
|  | ConfigureEdgeMultiplier(String, Int32) | Configures the edge multiplier of a time set. |
|  | ConfigureEdgeMultiplier(DigitalPinSet, Int32) | Configures the edge multiplier of a time set. |
|  | ConfigurePeriod | Configures the period of a time set. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetDriveFormat(String) | Gets the drive format of a time set. |
|  | GetDriveFormat(DigitalPinSet) | Gets the drive format of a time set. |
|  | GetEdge(String, TimeSetEdge) | Gets the edge time of a time set. |
|  | GetEdge(DigitalPinSet, TimeSetEdge) | Gets the edge time of a time set. |
|  | GetEdgeMultiplier(String) | Gets the edge multiplier of a time set. |
|  | GetEdgeMultiplier(DigitalPinSet) | Gets the edge multiplier of a time set. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

DigitalTimeSet

CreateTimeSet(String)

Timing

NIDigital

Use this class to configure the drive edges, strobe edges, and period of your time set.

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

Refer to [Timing](/csh?topicname=digipat/timingtwo.html) in the Digital Pattern Help for more information.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/25ebd605-a66c-a4bd-7c67-872a7fc659b3.htm language=enus -->
## TOPIC 00039: ninetdigitalfx40ref/html/25ebd605-a66c-a4bd-7c67-872a7fc659b3.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/25ebd605-a66c-a4bd-7c67-872a7fc659b3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/25ebd605-a66c-a4bd-7c67-872a7fc659b3.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.ConfigureDriveFormat Method (DigitalPinSet, DriveFormat)

DigitalTimeSetConfigureDriveFormat Method (DigitalPinSet, DriveFormat)

Configures the drive format of a time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDriveFormat(
	DigitalPinSet pinSet,
	DriveFormat driveFormat
)
```

```text
Public Sub ConfigureDriveFormat ( 
	pinSet As DigitalPinSet,
	driveFormat As DriveFormat
)
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The pin set for which to configure the drive format.
- **driveFormat**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDriveFormat The drive format of the time set.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for driveFormat is invalid. |

##### See Also

###### Reference

DigitalTimeSet Class

ConfigureDriveFormat Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/27e62d0b-194a-7978-02bb-c3f34a0216ee.htm language=enus -->
## TOPIC 00040: ninetdigitalfx40ref/html/27e62d0b-194a-7978-02bb-c3f34a0216ee.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/27e62d0b-194a-7978-02bb-c3f34a0216ee.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/27e62d0b-194a-7978-02bb-c3f34a0216ee.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalStartTrigger.Disable Method

DigitalStartTriggerDisable Method

TriggerType

None

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void Disable()
```

```text
Public Sub Disable
```

##### Remarks

The digital pattern instrument does not wait for a start trigger after you initiate the pattern burst before bursting a pattern.

##### See Also

###### Reference

DigitalStartTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/2a329da3-d788-7c64-636e-f56241df1e90.htm language=enus -->
## TOPIC 00041: ninetdigitalfx40ref/html/2a329da3-d788-7c64-636e-f56241df1e90.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/2a329da3-d788-7c64-636e-f56241df1e90.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/2a329da3-d788-7c64-636e-f56241df1e90.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPpmu.ApertureTime Property

DigitalPpmuApertureTime Property

Gets the measurement aperture time for the PPMU.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double ApertureTime { get; }
```

```text
Public ReadOnly Property ApertureTime As Double
	Get
```

###### Property Value

Double

ApertureTimeUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for ApertureTime is invalid. |

##### See Also

###### Reference

DigitalPpmu Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/2b706781-1105-8ba6-8a5d-1668a0c115f8.htm language=enus -->
## TOPIC 00042: ninetdigitalfx40ref/html/2b706781-1105-8ba6-8a5d-1668a0c115f8.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/2b706781-1105-8ba6-8a5d-1668a0c115f8.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/2b706781-1105-8ba6-8a5d-1668a0c115f8.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternOpcodeEvent.OutputTerminal Property

DigitalPatternOpcodeEventOutputTerminal Property

DigitalPatternOpcodeEvent

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string OutputTerminal { get; set; }
```

```text
Public Property OutputTerminal As String
	Get
	Set
```

###### Property Value

String

DigitalPatternOpcodeEvent

##### Remarks

You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0,
 you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

##### See Also

###### Reference

DigitalPatternOpcodeEvent Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/32f6cb88-4893-e84e-35f4-0dfcfd967441.htm language=enus -->
## TOPIC 00043: ninetdigitalfx40ref/html/32f6cb88-4893-e84e-35f4-0dfcfd967441.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/32f6cb88-4893-e84e-35f4-0dfcfd967441.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/32f6cb88-4893-e84e-35f4-0dfcfd967441.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinAndChannelMap Class

DigitalPinAndChannelMap Class

NIDigital

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalPinAndChannelMap : DigitalSubObject
```

```text
Public NotInheritable Class DigitalPinAndChannelMap
	Inherits DigitalSubObject
```

The DigitalPinAndChannelMap type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateChannelMap | Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap(String, String) before calling this method. |
|  | CreatePinGroup | Creates a pin group with the specified name. The pin group serves as an alias for a list of pins. |
|  | CreatePinMap | Creates and loads a pin map. Use this method if you are not loading a pin map file using LoadPinMap(String). |
|  | EndChannelMap | Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPinSet | Returns a DigitalPinSet object representing a set of either channels or pins. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MapPinToChannel | Maps a pin to a digital pattern instrument channel. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/339b4783-1483-b3b9-23dd-e262afbb1e5a.htm language=enus -->
## TOPIC 00044: ninetdigitalfx40ref/html/339b4783-1483-b3b9-23dd-e262afbb1e5a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/339b4783-1483-b3b9-23dd-e262afbb1e5a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/339b4783-1483-b3b9-23dd-e262afbb1e5a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternLabelHistoryRamTrigger Methods

DigitalPatternLabelHistoryRamTrigger Methods

The [DigitalPatternLabelHistoryRamTrigger](286ff3ca-714b-5864-ec16-47275dfa56c9.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the TriggerType to PatternLabel and configures Label, VectorOffset, CycleOffset, and PretriggerSamples. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalPatternLabelHistoryRamTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/355f439f-c84a-4314-53cc-8130297d405f.htm language=enus -->
## TOPIC 00045: ninetdigitalfx40ref/html/355f439f-c84a-4314-53cc-8130297d405f.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/355f439f-c84a-4314-53cc-8130297d405f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/355f439f-c84a-4314-53cc-8130297d405f.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalFrequencyCounter.MeasurementMode Property

DigitalFrequencyCounterMeasurementMode Property

Gets or sets the measurement mode for the frequency counter.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public FrequencyMeasurementMode MeasurementMode { get; set; }
```

```text
Public Property MeasurementMode As FrequencyMeasurementMode
	Get
	Set
```

###### Property Value

FrequencyMeasurementMode

Banked

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for MeasurementMode is invalid. |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | MeasurementMode was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalFrequencyCounter Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/36fb4e89-411e-6e72-f5ea-107b95cbb44e.htm language=enus -->
## TOPIC 00046: ninetdigitalfx40ref/html/36fb4e89-411e-6e72-f5ea-107b95cbb44e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/36fb4e89-411e-6e72-f5ea-107b95cbb44e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/36fb4e89-411e-6e72-f5ea-107b95cbb44e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.EnableSites Method

NIDigitalEnableSites Method

Enables the specified sites.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void EnableSites(
	string siteList
)
```

```text
Public Sub EnableSites ( 
	siteList As String
)
```

###### Parameters

- **siteList**
  - Type: SystemStringA comma-delimited list of strings of the form siteN, where N is the site number. All sites are enabled if the string is empty.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The specified siteList contains an invalid site. |

##### Remarks

NI TestStand Semiconductor Module requires all sites to always be enabled and manages the set of active sites without disabling the sites in the digital pattern instrument session. Do not use this method with the Semiconductor Module.

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/37878432-69aa-7d0a-7fff-45431fe4322c.htm language=enus -->
## TOPIC 00047: ninetdigitalfx40ref/html/37878432-69aa-7d0a-7fff-45431fe4322c.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/37878432-69aa-7d0a-7fff-45431fe4322c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/37878432-69aa-7d0a-7fff-45431fe4322c.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEvent Methods

DigitalEvent Methods

The [DigitalEvent](150fe4a2-0dba-3572-fa9d-509fc66319be.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalEvent Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/3a205d10-88fa-30f3-6883-18d7a55dfdae.htm language=enus -->
## TOPIC 00048: ninetdigitalfx40ref/html/3a205d10-88fa-30f3-6883-18d7a55dfdae.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/3a205d10-88fa-30f3-6883-18d7a55dfdae.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/3a205d10-88fa-30f3-6883-18d7a55dfdae.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalCycleNumberHistoryRamTrigger Class

DigitalCycleNumberHistoryRamTrigger Class

Contains properties and methods for configuring the cycle number History RAM trigger.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalCycleNumberHistoryRamTrigger : DigitalSubObject
```

```text
Public NotInheritable Class DigitalCycleNumberHistoryRamTrigger
	Inherits DigitalSubObject
```

The DigitalCycleNumberHistoryRamTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Number | Gets or sets the number of cycles to execute before the DigitalHistoryRamTrigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the TriggerType to CycleNumber and configures Number and PretriggerSamples. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/41c70fca-ef8f-b9c8-c1c3-6a6d95a7b7ab.htm language=enus -->
## TOPIC 00049: ninetdigitalfx40ref/html/41c70fca-ef8f-b9c8-c1c3-6a6d95a7b7ab.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/41c70fca-ef8f-b9c8-c1c3-6a6d95a7b7ab.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/41c70fca-ef8f-b9c8-c1c3-6a6d95a7b7ab.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.EnableMatchFailCombination Method (IntPtr)

DigitalPatternControlEnableMatchFailCombination Method (IntPtr)

Configures multiple digital pattern instruments in the session as well as the timing and synchronization instrument (PXIe-6674T) to combine pattern
 comparison results and control subsequent pattern execution across all digital pattern instruments in the session, based on those results.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void EnableMatchFailCombination(
	IntPtr syncSession
)
```

```text
Public Sub EnableMatchFailCombination ( 
	syncSession As IntPtr
)
```

###### Parameters

- **syncSession**
  - Type: SystemIntPtrThe NI-Sync session.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| ObjectDisposedException | DigitalPatternControl was accessed after the associated NIDigital object was disposed. |

##### Remarks

You must initialize the PXIe-6674T using NI-Sync before calling this method.

Use this method with multi-instrument sessions. Use [EnableMatchFailCombination(ITClockSynchronizableDevice, IntPtr)](f477f3e3-408d-c147-f3ea-f8aef96b7114.htm) with single-instrument sessions.

For more information, refer to the [Synchronizing Multiple Instruments](/csh?topicname=digipat6570/sync-multiple-modules.html) topic of the Digital Pattern Help.

##### See Also

###### Reference

DigitalPatternControl Class

EnableMatchFailCombination Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/46ac945c-ce98-59b0-629c-161211ba7c40.htm language=enus -->
## TOPIC 00050: ninetdigitalfx40ref/html/46ac945c-ce98-59b0-629c-161211ba7c40.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/46ac945c-ce98-59b0-629c-161211ba7c40.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/46ac945c-ce98-59b0-629c-161211ba7c40.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRam Methods

DigitalHistoryRam Methods

The [DigitalHistoryRam](cf1149e0-976e-24a7-23fc-7dcdb3de8288.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchCycleInformation(String, DigitalPinSet, Int64, Int64) | Fetches the pattern information acquired for the specified History RAM samples. |
|  | FetchCycleInformation(String, String, Int64, Int64) | Fetches the pattern information acquired for the specified History RAM samples. |
|  | FetchScanCycleNumbers | Fetches the scan cycle numbers acquired for the specified History RAM samples. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetSampleCount | Returns the number of samples History RAM acquired on the last pattern burst. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalHistoryRam Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/46c455e1-de7f-9e11-02fa-cc98eab6a99b.htm language=enus -->
## TOPIC 00051: ninetdigitalfx40ref/html/46c455e1-de7f-9e11-02fa-cc98eab6a99b.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/46c455e1-de7f-9e11-02fa-cc98eab6a99b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/46c455e1-de7f-9e11-02fa-cc98eab6a99b.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeStartTrigger Properties

DigitalEdgeStartTrigger Properties

The [DigitalEdgeStartTrigger](15eab349-2dad-3fd4-fbf1-a5ca77181f83.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Edge | Gets or sets the active edge for the start trigger. |
|  | Source | Gets or sets the source terminal for the start trigger. |

Top

##### See Also

###### Reference

DigitalEdgeStartTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/4b1ec562-c407-c5b9-e897-456920a24ea3.htm language=enus -->
## TOPIC 00052: ninetdigitalfx40ref/html/4b1ec562-c407-c5b9-e897-456920a24ea3.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/4b1ec562-c407-c5b9-e897-456920a24ea3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/4b1ec562-c407-c5b9-e897-456920a24ea3.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTrigger Properties

DigitalTrigger Properties

The [DigitalTrigger](7bacfb01-a6b1-1b95-d6e1-9ed535557cee.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ConditionalJumpTriggers | Gets the DigitalConditionalJumpTrigger objects used to configure and control conditional jump triggers. |
|  | HistoryRamTrigger | Gets the DigitalHistoryRamTrigger object used to configure and control History RAM triggers. |
|  | SequencerFlag | Gets the DigitalSequencerFlagTrigger object used to get the configuration for the sequencer flag trigger. |
|  | StartTrigger | Gets the DigitalStartTrigger object used to configure and control start triggers. |

Top

##### See Also

###### Reference

DigitalTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/4bf6644d-54da-a55a-c473-7e23ebc8a577.htm language=enus -->
## TOPIC 00053: ninetdigitalfx40ref/html/4bf6644d-54da-a55a-c473-7e23ebc8a577.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/4bf6644d-54da-a55a-c473-7e23ebc8a577.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/4bf6644d-54da-a55a-c473-7e23ebc8a577.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverIdentity.GetGroupCapabilities Method

DigitalDriverIdentityGetGroupCapabilities Method

Returns an array of strings containing the names of the IVI class capability groups, or standard methods and properties, that the 
 NI-Digital Pattern Driver software implements.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string[] GetGroupCapabilities()
```

```text
Public Function GetGroupCapabilities As String()
```

###### Return Value

String

###### Implements

##### Remarks

IVI Foundation website

##### See Also

###### Reference

DigitalDriverIdentity Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/4c34deaf-22aa-563d-48c6-739697490b94.htm language=enus -->
## TOPIC 00054: ninetdigitalfx40ref/html/4c34deaf-22aa-563d-48c6-739697490b94.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/4c34deaf-22aa-563d-48c6-739697490b94.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/4c34deaf-22aa-563d-48c6-739697490b94.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.BurstPatternSynchronized Method

DigitalPatternControlBurstPatternSynchronized Method

Starts a pattern burst on digital pattern instruments that you have previously synchronized using NI-TClk.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public static void BurstPatternSynchronized(
	NIDigital[] sessions,
	string siteList,
	string startLabel,
	bool selectDigitalFunction,
	bool waitUntilDone,
	TimeSpan maxTime
)
```

```text
Public Shared Sub BurstPatternSynchronized ( 
	sessions As NIDigital(),
	siteList As String,
	startLabel As String,
	selectDigitalFunction As Boolean,
	waitUntilDone As Boolean,
	maxTime As TimeSpan
)
```

###### Parameters

- **sessions**
  - Type: NationalInstruments.ModularInstruments.NIDigitalNIDigitalAn array of NIDigital sessions.
- **siteList**
  - Type: SystemStringThe sites on which to burst the pattern as a comma-delimited list of strings of the form siteN, where N is the site number. If you specify an empty string, the pattern is burst on all sites.
- **startLabel**
  - Type: SystemStringThe pattern name or exported pattern label from which to start bursting the pattern.
- **selectDigitalFunction**
  - Type: SystemBooleanIf , sets the SelectedFunction of the pins to Digital.
- **waitUntilDone**
  - Type: SystemBooleanIf , this method waits until the bursting is completed before returning; otherwise, initiates a pattern burst and returns.
- **maxTime**
  - Type: SystemTimeSpanThe maximum time allowed for BurstPatternSynchronized(NIDigital, String, String, Boolean, Boolean, TimeSpan) to complete.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The value for siteList contains an invalid site. |
| ArgumentException | sessions is or not initialized.sessions contains or an uninitialized session.The value for startLabel is invalid. or One or more of the configured properties of the underlying NI-Digital Pattern Driver were invalid. |

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/4ca97bd8-9a3b-9d2e-a4fd-d66936b36378.htm language=enus -->
## TOPIC 00055: ninetdigitalfx40ref/html/4ca97bd8-9a3b-9d2e-a4fd-d66936b36378.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/4ca97bd8-9a3b-9d2e-a4fd-d66936b36378.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/4ca97bd8-9a3b-9d2e-a4fd-d66936b36378.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalConditionalJumpTrigger.TerminalName Property

DigitalConditionalJumpTriggerTerminalName Property

DigitalConditionalJumpTrigger

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string TerminalName { get; }
```

```text
Public ReadOnly Property TerminalName As String
	Get
```

###### Property Value

String

The terminal name of the [DigitalConditionalJumpTrigger](dcf89d16-3a39-1b83-5600-f8762ea36b23.htm).

##### Remarks

You can use this terminal name as an input signal source for another trigger.

##### See Also

###### Reference

DigitalConditionalJumpTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/526596ab-f70e-9f21-2c43-dd9676c643c8.htm language=enus -->
## TOPIC 00056: ninetdigitalfx40ref/html/526596ab-f70e-9f21-2c43-dd9676c643c8.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/526596ab-f70e-9f21-2c43-dd9676c643c8.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/526596ab-f70e-9f21-2c43-dd9676c643c8.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.HaltOnKeepAliveOpcode Property

DigitalPatternControlHaltOnKeepAliveOpcode Property

Gets or sets a value that indicates whether keep_alive opcodes should behave like halt opcodes.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public bool HaltOnKeepAliveOpcode { get; set; }
```

```text
Public Property HaltOnKeepAliveOpcode As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/52b9019b-57d9-6b35-00a5-7b1db99cedc1.htm language=enus -->
## TOPIC 00057: ninetdigitalfx40ref/html/52b9019b-57d9-6b35-00a5-7b1db99cedc1.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/52b9019b-57d9-6b35-00a5-7b1db99cedc1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/52b9019b-57d9-6b35-00a5-7b1db99cedc1.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceWaveforms.WriteFromFile Method

DigitalSourceWaveformsWriteFromFile Method

Writes a source waveform based on the waveform data and the configuration information the file contains.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void WriteFromFile(
	string waveformName,
	string waveformFilePath
)
```

```text
Public Sub WriteFromFile ( 
	waveformName As String,
	waveformFilePath As String
)
```

###### Parameters

- **waveformName**
  - Type: SystemStringSpecifies the waveform name to use from the file. You must specify the waveform name if the file contains multiple waveforms. Use the waveformName with source_start opcode in your pattern.
- **waveformFilePath**
  - Type: SystemStringSpecifies the absolute file path to the source waveform file (.tdms).

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| ArgumentException | The waveform name specified by waveformName does not exist. |
| FileNotFoundException | The file was not found at the specified waveformFilePath. |

##### See Also

###### Reference

DigitalSourceWaveforms Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/58111c69-63f6-4200-dabe-78d83d0f97bc.htm language=enus -->
## TOPIC 00058: ninetdigitalfx40ref/html/58111c69-63f6-4200-dabe-78d83d0f97bc.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/58111c69-63f6-4200-dabe-78d83d0f97bc.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/58111c69-63f6-4200-dabe-78d83d0f97bc.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalCaptureWaveforms.CreateFromFile Method

DigitalCaptureWaveformsCreateFromFile Method

Creates a capture waveform using the configuration information from a .digicapture file.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateFromFile(
	string waveformName,
	string waveformFilePath
)
```

```text
Public Sub CreateFromFile ( 
	waveformName As String,
	waveformFilePath As String
)
```

###### Parameters

- **waveformName**
  - Type: SystemStringSpecifies the waveform name to use from the file. You must specify a waveform name if the file contains multiple waveforms. Use the waveformName with the capture_start opcode in your pattern.
- **waveformFilePath**
  - Type: SystemStringSpecifies the absolute file path to the capture waveform file (.digicapture) to load.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| ArgumentException | The waveform name specified by waveformName does not exist. |
| FileNotFoundException | The file was not found at the specified waveformFilePath. |

##### See Also

###### Reference

DigitalCaptureWaveforms Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/5d0927bb-bce4-f531-e730-58109874372f.htm language=enus -->
## TOPIC 00059: ninetdigitalfx40ref/html/5d0927bb-bce4-f531-e730-58109874372f.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/5d0927bb-bce4-f531-e730-58109874372f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/5d0927bb-bce4-f531-e730-58109874372f.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.UnloadSpecifications Method (IEnumerable(String))

NIDigitalUnloadSpecifications Method (IEnumerableString)

Unloads the given specifications sheets present in the previously loaded specifications files that you select.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void UnloadSpecifications(
	IEnumerable<string> filePaths
)
```

```text
Public Sub UnloadSpecifications ( 
	filePaths As IEnumerable(Of String)
)
```

###### Parameters

- **filePaths**
  - Type: System.Collections.GenericIEnumerableString The absolute file paths to loaded specifications files.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | UnloadSpecifications(IEnumerableString) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### Remarks

ApplyLevelsAndTiming(String, String, String)

##### See Also

###### Reference

NIDigital Class

UnloadSpecifications Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/5dc2795a-a913-2739-819f-4775ad3b3ac5.htm language=enus -->
## TOPIC 00060: ninetdigitalfx40ref/html/5dc2795a-a913-2739-819f-4775ad3b3ac5.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/5dc2795a-a913-2739-819f-4775ad3b3ac5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/5dc2795a-a913-2739-819f-4775ad3b3ac5.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRamTrigger.PretriggerSamples Property

DigitalHistoryRamTriggerPretriggerSamples Property

Gets or sets the number of samples to acquire before the History RAM trigger.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public int PretriggerSamples { get; set; }
```

```text
Public Property PretriggerSamples As Integer
	Get
	Set
```

###### Property Value

Int32

The number of samples to acquire before the History RAM trigger.
 The default value is 0.

##### Exceptions

| Exception | Condition |
| --- | --- |
| OutOfRangeException | The value for PretriggerSamples is invalid. |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | PretriggerSamples was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalHistoryRamTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/5ff393ce-f96d-2beb-60b6-249e078e185e.htm language=enus -->
## TOPIC 00061: ninetdigitalfx40ref/html/5ff393ce-f96d-2beb-60b6-249e078e185e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/5ff393ce-f96d-2beb-60b6-249e078e185e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/5ff393ce-f96d-2beb-60b6-249e078e185e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.GetEdge Method (String, TimeSetEdge)

DigitalTimeSetGetEdge Method (String, TimeSetEdge)

Gets the edge time of a time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PrecisionTimeSpan GetEdge(
	string pinSetString,
	TimeSetEdge edge
)
```

```text
Public Function GetEdge ( 
	pinSetString As String,
	edge As TimeSetEdge
) As PrecisionTimeSpan
```

###### Parameters

- **pinSetString**
  - Type: SystemString The pin set specified as a comma-delimited list of pins for which to get the edge.
- **edge**
  - Type: NationalInstruments.ModularInstruments.NIDigitalTimeSetEdge The edge of the time set to get.

###### Return Value

PrecisionTimeSpan

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |

##### See Also

###### Reference

DigitalTimeSet Class

GetEdge Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/5ff7e73f-8c2f-5f04-29da-5ef8d930c44a.htm language=enus -->
## TOPIC 00062: ninetdigitalfx40ref/html/5ff7e73f-8c2f-5f04-29da-5ef8d930c44a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/5ff7e73f-8c2f-5f04-29da-5ef8d930c44a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/5ff7e73f-8c2f-5f04-29da-5ef8d930c44a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.SortPinResultsBySite Method (NIDigital[], String, Byte[][], String[], Int32[])

DigitalDriverUtilitySortPinResultsBySite Method (NIDigital, String, Byte, String, Int32)

Organizes data read from multiple digital pattern instruments by grouping the data by site number.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public static byte[] SortPinResultsBySite(
	NIDigital[] sessions,
	string pinSetString,
	byte[][] resultsToSort,
	out string[] pinNames,
	out int[] siteNumbers
)
```

```text
Public Shared Function SortPinResultsBySite ( 
	sessions As NIDigital(),
	pinSetString As String,
	resultsToSort As Byte()(),
	<OutAttribute> ByRef pinNames As String(),
	<OutAttribute> ByRef siteNumbers As Integer()
) As Byte()
```

###### Parameters

- **sessions**
  - Type: NationalInstruments.ModularInstruments.NIDigitalNIDigitalThe instrument sessions to return data for.
- **pinSetString**
  - Type: SystemStringThe pin set from which to read data.
- **resultsToSort**
  - Type: SystemByteThe data read from the digital pattern instruments, combined into a two-dimensional array.
- **pinNames**
  - Type: SystemStringAn array of DUT pin names corresponding to the values in DUT pin results.
- **siteNumbers**
  - Type: SystemInt32An array of site numbers corresponding to the values in DUT pin results.

###### Return Value

Byte

pinNames

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

DigitalDriverUtility Class

SortPinResultsBySite Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/619b7cf6-ee5d-8589-7fef-52bc8d81e2b1.htm language=enus -->
## TOPIC 00063: ninetdigitalfx40ref/html/619b7cf6-ee5d-8589-7fef-52bc8d81e2b1.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/619b7cf6-ee5d-8589-7fef-52bc8d81e2b1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/619b7cf6-ee5d-8589-7fef-52bc8d81e2b1.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalCaptureWaveforms Class

DigitalCaptureWaveforms Class

Provides operations to create and fetch capture waveforms with the NI-Digital Pattern Driver.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalCaptureWaveforms : DigitalSubObject
```

```text
Public NotInheritable Class DigitalCaptureWaveforms
	Inherits DigitalSubObject
```

The DigitalCaptureWaveforms type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateFromFile | Creates a capture waveform using the configuration information from a .digicapture file. |
|  | CreateParallel(String, String) | Creates the capture waveform settings for parallel acquisition using a comma-delimited string of pins or channels. |
|  | CreateParallel(DigitalPinSet, String) | Creates the capture waveform settings for parallel acquisition using DigitalPinSet. |
|  | CreateSerial(String, String, UInt32, BitOrder) | Creates the capture waveform settings for serial acquisition using a comma-delimited string of pins or channels. |
|  | CreateSerial(DigitalPinSet, String, UInt32, BitOrder) | Creates the capture waveform settings for serial acquisition using DigitalPinSet. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Fetch | Fetches a defined number of samples for a specified list of sites. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

For more information on capture functionality, refer to [Capture](/csh?topicname=digipat6570/capture.html) in the Digital Pattern Help.

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/62d0b17e-b150-b9bc-eb36-758200f39dac.htm language=enus -->
## TOPIC 00064: ninetdigitalfx40ref/html/62d0b17e-b150-b9bc-eb36-758200f39dac.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/62d0b17e-b150-b9bc-eb36-758200f39dac.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/62d0b17e-b150-b9bc-eb36-758200f39dac.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinSet.SelectedFunction Property

DigitalPinSetSelectedFunction Property

Gets or sets the instrument function of this pin set. The changes take effect immediately.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public SelectedFunction SelectedFunction { get; set; }
```

```text
Public Property SelectedFunction As SelectedFunction
	Get
	Set
```

###### Property Value

SelectedFunction

The function of this pin set as [Digital](a794b815-cc6f-5dd5-528a-97a46c40f454.htm),
 [Ppmu](a794b815-cc6f-5dd5-528a-97a46c40f454.htm),
 [Off](a794b815-cc6f-5dd5-528a-97a46c40f454.htm),
 or [Disconnect](a794b815-cc6f-5dd5-528a-97a46c40f454.htm).
 The default value is [Disconnect](a794b815-cc6f-5dd5-528a-97a46c40f454.htm).

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for SelectedFunction is invalid. |

##### See Also

###### Reference

DigitalPinSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/63bca1b2-c0d5-7604-800c-a995fada3b01.htm language=enus -->
## TOPIC 00065: ninetdigitalfx40ref/html/63bca1b2-c0d5-7604-800c-a995fada3b01.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/63bca1b2-c0d5-7604-800c-a995fada3b01.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/63bca1b2-c0d5-7604-800c-a995fada3b01.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.ApplyLevelsAndTiming Method (String, String, String, String, String, String)

NIDigitalApplyLevelsAndTiming Method (String, String, String, String, String, String)

Applies digital levels and timing defined in the loaded levels and timing sheets.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ApplyLevelsAndTiming(
	string siteList,
	string levelsSheet,
	string timingSheet,
	string initialStateHighPins,
	string initialStateLowPins,
	string initialStateTristatePins
)
```

```text
Public Sub ApplyLevelsAndTiming ( 
	siteList As String,
	levelsSheet As String,
	timingSheet As String,
	initialStateHighPins As String,
	initialStateLowPins As String,
	initialStateTristatePins As String
)
```

###### Parameters

- **siteList**
  - Type: SystemString A comma-delimited list of strings of the form siteN, where N is the site number. Passing an empty string specifies all sites.
- **levelsSheet**
  - Type: SystemStringThe name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path used in the LoadLevels(String) method. The name of the levels sheet is the file name without the directory and the file extension.
- **timingSheet**
  - Type: SystemStringThe name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you used in the LoadTiming(String) method. The name of the timing sheet is the file name without the directory and file extension.
- **initialStateHighPins**
  - Type: SystemStringComma-delimited list of pins, pin groups, or channels to initialize to a high state.
- **initialStateLowPins**
  - Type: SystemStringComma-delimited list of pins, pin groups, or channels to initialize to a low state.
- **initialStateTristatePins**
  - Type: SystemStringComma-delimited list of pins, pin groups, or channels to initialize to a non-drive state.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The specified siteList contains an invalid site. |
| InvalidOperationException | The specified levelsSheet or timingSheet is not loaded. |
| ArgumentException | The specified initialStateHighPins, initialStateLowPins, or initialStateTristatePins contains an invalid pin or pin group name. |

##### Remarks

Levels

Timing

##### See Also

###### Reference

NIDigital Class

ApplyLevelsAndTiming Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/64a7a763-07a0-1426-40ff-4bde3794ff02.htm language=enus -->
## TOPIC 00066: ninetdigitalfx40ref/html/64a7a763-07a0-1426-40ff-4bde3794ff02.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/64a7a763-07a0-1426-40ff-4bde3794ff02.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/64a7a763-07a0-1426-40ff-4bde3794ff02.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternLabelHistoryRamTrigger.Configure Method

DigitalPatternLabelHistoryRamTriggerConfigure Method

TriggerType

PatternLabel

Label

VectorOffset

CycleOffset

PretriggerSamples

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void Configure(
	string label,
	long vectorOffset,
	long cycleOffset,
	int pretriggerSamples
)
```

```text
Public Sub Configure ( 
	label As String,
	vectorOffset As Long,
	cycleOffset As Long,
	pretriggerSamples As Integer
)
```

###### Parameters

- **label**
  - Type: SystemStringThe value at which to set Label.
- **vectorOffset**
  - Type: SystemInt64The value at which to set VectorOffset.
- **cycleOffset**
  - Type: SystemInt64The value at which to set CycleOffset.
- **pretriggerSamples**
  - Type: SystemInt32The number of samples to acquire before the DigitalHistoryRamTrigger.

##### Exceptions

| Exception | Condition |
| --- | --- |
| OutOfRangeException | The value for pretriggerSamples is invalid. |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | Configure(String, Int64, Int64, Int32) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalPatternLabelHistoryRamTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6517d734-8c15-0ecc-6870-a8c2a7e521d3.htm language=enus -->
## TOPIC 00067: ninetdigitalfx40ref/html/6517d734-8c15-0ecc-6870-a8c2a7e521d3.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6517d734-8c15-0ecc-6870-a8c2a7e521d3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6517d734-8c15-0ecc-6870-a8c2a7e521d3.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.LoadSpecifications Method (String)

NIDigitalLoadSpecifications Method (String)

Loads a specifications sheet from file.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void LoadSpecifications(
	string filePath
)
```

```text
Public Sub LoadSpecifications ( 
	filePath As String
)
```

###### Parameters

- **filePath**
  - Type: SystemString The absolute file path to the specifications file.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |

##### See Also

###### Reference

NIDigital Class

LoadSpecifications Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/655db2b5-0c24-cfe7-a61f-56272413faed.htm language=enus -->
## TOPIC 00068: ninetdigitalfx40ref/html/655db2b5-0c24-cfe7-a61f-56272413faed.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/655db2b5-0c24-cfe7-a61f-56272413faed.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/655db2b5-0c24-cfe7-a61f-56272413faed.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPpmu.OutputFunction Property

DigitalPpmuOutputFunction Property

Gets or sets whether the PPMU sources DC voltage or DC current.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PpmuOutputFunction OutputFunction { get; set; }
```

```text
Public Property OutputFunction As PpmuOutputFunction
	Get
	Set
```

###### Property Value

PpmuOutputFunction

DCVoltage

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for OutputFunction is invalid. |

##### Remarks

SelectedFunction

Ppmu

Changing this property does not take effect until you call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm).
 You must call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm) to commit your changes even if the PPMU is already sourcing.

##### See Also

###### Reference

DigitalPpmu Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/65dbbc5a-7d9b-957a-ba12-65c52c879387.htm language=enus -->
## TOPIC 00069: ninetdigitalfx40ref/html/65dbbc5a-7d9b-957a-ba12-65c52c879387.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/65dbbc5a-7d9b-957a-ba12-65c52c879387.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/65dbbc5a-7d9b-957a-ba12-65c52c879387.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.ConfigureEdge Method (DigitalPinSet, TimeSetEdge, PrecisionTimeSpan)

DigitalTimeSetConfigureEdge Method (DigitalPinSet, TimeSetEdge, PrecisionTimeSpan)

Configures the edge of a time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureEdge(
	DigitalPinSet pinSet,
	TimeSetEdge edge,
	PrecisionTimeSpan time
)
```

```text
Public Sub ConfigureEdge ( 
	pinSet As DigitalPinSet,
	edge As TimeSetEdge,
	time As PrecisionTimeSpan
)
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The pin set for which to configure the edge.
- **edge**
  - Type: NationalInstruments.ModularInstruments.NIDigitalTimeSetEdge The edge of the time set to configure.
- **time**
  - Type: Ivi.DriverPrecisionTimeSpan The time of the edge to configure.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

##### See Also

###### Reference

DigitalTimeSet Class

ConfigureEdge Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6607bd2e-6c48-8fdf-1b26-27cd38106cc5.htm language=enus -->
## TOPIC 00070: ninetdigitalfx40ref/html/6607bd2e-6c48-8fdf-1b26-27cd38106cc5.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6607bd2e-6c48-8fdf-1b26-27cd38106cc5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6607bd2e-6c48-8fdf-1b26-27cd38106cc5.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

PpmuApertureTimeUnits Enumeration

PpmuApertureTimeUnits Enumeration

Specifies the unit of the aperture time.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public enum PpmuApertureTimeUnits
```

```text
Public Enumeration PpmuApertureTimeUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 2100 | Unit in seconds. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6778ad5a-8e46-a3c9-1162-669f66895024.htm language=enus -->
## TOPIC 00071: ninetdigitalfx40ref/html/6778ad5a-8e46-a3c9-1162-669f66895024.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6778ad5a-8e46-a3c9-1162-669f66895024.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6778ad5a-8e46-a3c9-1162-669f66895024.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalConditionalJumpTrigger.Software Property

DigitalConditionalJumpTriggerSoftware Property

DigitalSoftwareConditionalJumpTrigger

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalSoftwareConditionalJumpTrigger Software { get; }
```

```text
Public ReadOnly Property Software As DigitalSoftwareConditionalJumpTrigger
	Get
```

###### Property Value

DigitalSoftwareConditionalJumpTrigger

Object used to configure and control the Conditional Jump Trigger as a software conditional jump trigger. This object is created when this [DigitalConditionalJumpTrigger](dcf89d16-3a39-1b83-5600-f8762ea36b23.htm) object is created.

##### See Also

###### Reference

DigitalConditionalJumpTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/68576858-bcdd-e24d-cd2c-ab94b49440b0.htm language=enus -->
## TOPIC 00072: ninetdigitalfx40ref/html/68576858-bcdd-e24d-cd2c-ab94b49440b0.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/68576858-bcdd-e24d-cd2c-ab94b49440b0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/68576858-bcdd-e24d-cd2c-ab94b49440b0.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalFrequencyCounter.MeasureFrequency Method

DigitalFrequencyCounterMeasureFrequency Method

Measures the frequency on the specified pins over the measurement time. All pins in the pin list should have the same measurement time.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double[] MeasureFrequency()
```

```text
Public Function MeasureFrequency As Double()
```

###### Return Value

Double

GetPinSet(String)

GetPinResultsPinInformation(String)

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| IviCDriverException | The selected function of one or more pins in the frequency measurement is not set to digital. Ensure that all pins have the selected function set to digital when you call MeasureFrequency. - or - The frequency measurement contains pins configured with different measurement times. Ensure that all pins you want to measure in the call to MeasureFrequency have the same measurement time. - or - The input signal is invalid for one or more pins. To prevent an invalid signal error, increase the measurement time, ensure the input signal produces a sufficient number of edges within the measurement time, or ensure the input signal is within the measurable frequency range of the instrument. - or - The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | MeasureFrequency was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### Remarks

BurstPattern(String, String, Boolean, TimeSpan)

GetSitePassFail(String)

##### See Also

###### Reference

DigitalFrequencyCounter Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6adeddec-2b47-06c2-3709-fd1beb99fe72.htm language=enus -->
## TOPIC 00073: ninetdigitalfx40ref/html/6adeddec-2b47-06c2-3709-fd1beb99fe72.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6adeddec-2b47-06c2-3709-fd1beb99fe72.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6adeddec-2b47-06c2-3709-fd1beb99fe72.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.StartLabel Property

DigitalPatternControlStartLabel Property

Gets or sets the pattern name or exported pattern label from which to start bursting the pattern.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string StartLabel { get; set; }
```

```text
Public Property StartLabel As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | The value for StartLabel is invalid. |

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6b28bd46-9bc0-417b-d1de-77d7b17fee00.htm language=enus -->
## TOPIC 00074: ninetdigitalfx40ref/html/6b28bd46-9bc0-417b-d1de-77d7b17fee00.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6b28bd46-9bc0-417b-d1de-77d7b17fee00.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6b28bd46-9bc0-417b-d1de-77d7b17fee00.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinSet.TdrOffset Property

DigitalPinSetTdrOffset Property

Gets the Time-Domain Reflectometry (TDR) offset for this pin set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PrecisionTimeSpan TdrOffset { get; }
```

```text
Public ReadOnly Property TdrOffset As PrecisionTimeSpan
	Get
```

###### Property Value

PrecisionTimeSpan

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for TdrOffset is invalid. |

##### Remarks

TDR

##### See Also

###### Reference

DigitalPinSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6e781245-de71-6af0-87ce-989d9633be33.htm language=enus -->
## TOPIC 00075: ninetdigitalfx40ref/html/6e781245-de71-6af0-87ce-989d9633be33.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6e781245-de71-6af0-87ce-989d9633be33.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6e781245-de71-6af0-87ce-989d9633be33.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalClockGenerator Class

DigitalClockGenerator Class

Drives a free-running clock that runs independently of the digital pattern on the specified pins.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalClockGenerator : DigitalSubObject
```

```text
Public NotInheritable Class DigitalClockGenerator
	Inherits DigitalSubObject
```

The DigitalClockGenerator type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Frequency | Gets or sets the frequency of the free-running clock. |
|  | IsRunning | Gets a value indicating whether the free-running clock is running. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Abort | Stops clock generation on the specified channel(s) or pin(s) and pin group(s). |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GenerateClock | Configures and initiates clock generation on the specified channel(s), or pin(s) and pin group(s). |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Initiate | Initiates clock generation on the specified channel(s) or pin(s) and pin group(s). |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

Use this class to drive a free-running clock at a specified frequency from a digital pin on the specified channel(s) or pin(s) and pin group(s).

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6ef6eb01-ff0d-ebb4-a89e-e0af077e28d2.htm language=enus -->
## TOPIC 00076: ninetdigitalfx40ref/html/6ef6eb01-ff0d-ebb4-a89e-e0af077e28d2.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6ef6eb01-ff0d-ebb4-a89e-e0af077e28d2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6ef6eb01-ff0d-ebb4-a89e-e0af077e28d2.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRamTrigger Class

DigitalHistoryRamTrigger Class

Provides configuration and controls for History RAM triggers that affect when to acquire pattern information.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalHistoryRamTrigger : DigitalSubObject
```

```text
Public NotInheritable Class DigitalHistoryRamTrigger
	Inherits DigitalSubObject
```

The DigitalHistoryRamTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | CycleNumber | Gets the DigitalCycleNumberHistoryRamTrigger object used to configure the History RAM trigger as a cycle number History RAM trigger. |
|  | FirstFailure | Gets the DigitalFirstFailureHistoryRamTrigger object used to configure the History RAM trigger as a first failure History RAM trigger. |
|  | PatternLabel | Gets the DigitalPatternLabelHistoryRamTrigger object used to configure the History RAM trigger as a pattern label History RAM trigger. |
|  | PretriggerSamples | Gets or sets the number of samples to acquire before the History RAM trigger. |
|  | TriggerType | Gets or sets the trigger type of the DigitalHistoryRamTrigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/6f8b9533-62fa-3242-2a58-a068c22586e0.htm language=enus -->
## TOPIC 00077: ninetdigitalfx40ref/html/6f8b9533-62fa-3242-2a58-a068c22586e0.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/6f8b9533-62fa-3242-2a58-a068c22586e0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/6f8b9533-62fa-3242-2a58-a068c22586e0.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRam.FetchScanCycleNumbers Method

DigitalHistoryRamFetchScanCycleNumbers Method

Fetches the scan cycle numbers acquired for the specified History RAM samples.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public long[] FetchScanCycleNumbers(
	string site,
	long position,
	long samplesToRead
)
```

```text
Public Function FetchScanCycleNumbers ( 
	site As String,
	position As Long,
	samplesToRead As Long
) As Long()
```

###### Parameters

- **site**
  - Type: SystemStringThe site to query.
- **position**
  - Type: SystemInt64The position from which to start fetching pattern information.
- **samplesToRead**
  - Type: SystemInt64The number of samples to read. Use -1 to fetch all samples.

###### Return Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| OperationPendingException | The specified operation cannot be performed during a pattern burst. |
| ArgumentException | The value for site is invalid.The value for position is invalid.The value for samplesToRead is invalid. - or - The position or the number of samples to read exceeded the number of samples available. |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | FetchScanCycleNumbers(String, Int64, Int64) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalHistoryRam Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/702a95b8-60fe-7809-c1ff-ea6bca169a1f.htm language=enus -->
## TOPIC 00078: ninetdigitalfx40ref/html/702a95b8-60fe-7809-c1ff-ea6bca169a1f.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/702a95b8-60fe-7809-c1ff-ea6bca169a1f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/702a95b8-60fe-7809-c1ff-ea6bca169a1f.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdge Enumeration

DigitalEdge Enumeration

Specifies the active edge for the start trigger.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public enum DigitalEdge
```

```text
Public Enumeration DigitalEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 1800 | Asserts the trigger when the signal transitions from low level to high level. |
|  | Falling | 1801 | Asserts the trigger when the signal transitions from high level to low level. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/73d41e06-0b55-4023-2121-ed9bde4b82e7.htm language=enus -->
## TOPIC 00079: ninetdigitalfx40ref/html/73d41e06-0b55-4023-2121-ed9bde4b82e7.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/73d41e06-0b55-4023-2121-ed9bde4b82e7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/73d41e06-0b55-4023-2121-ed9bde4b82e7.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.GetEdgeMultiplier Method

DigitalTimeSetGetEdgeMultiplier Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetEdgeMultiplier(String) | Gets the edge multiplier of a time set. |
|  | GetEdgeMultiplier(DigitalPinSet) | Gets the edge multiplier of a time set. |

Top

##### See Also

###### Reference

DigitalTimeSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/73f66f95-5a3f-0b41-35e0-6fd170f25c4e.htm language=enus -->
## TOPIC 00080: ninetdigitalfx40ref/html/73f66f95-5a3f-0b41-35e0-6fd170f25c4e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/73f66f95-5a3f-0b41-35e0-6fd170f25c4e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/73f66f95-5a3f-0b41-35e0-6fd170f25c4e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalFrequencyCounter.IsHysteresisEnabled Property

DigitalFrequencyCounterIsHysteresisEnabled Property

Gets or sets a value indicating whether frequency counter measurement hysteresis should be enabled.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public bool IsHysteresisEnabled { get; set; }
```

```text
Public Property IsHysteresisEnabled As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | IsHysteresisEnabled was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### Remarks

| Note |
| --- |
| Hysteresis is available only when MeasurementMode is set to parallel. |

##### See Also

###### Reference

DigitalFrequencyCounter Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/74817569-e3e3-3563-6128-ac04b07474c7.htm language=enus -->
## TOPIC 00081: ninetdigitalfx40ref/html/74817569-e3e3-3563-6128-ac04b07474c7.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/74817569-e3e3-3563-6128-ac04b07474c7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/74817569-e3e3-3563-6128-ac04b07474c7.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

TerminationMode Enumeration

TerminationMode Enumeration

Specifies the behavior of one or more pins when the driver is in a non-drive state.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public enum TerminationMode
```

```text
Public Enumeration TerminationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveLoad | 1200 | The active load provides a constant current to a commutating voltage (Vcom). |
|  | Vterm | 1201 | The pin driver drives Vterm. |
|  | HighZ | 1202 | The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/74f178ef-5401-374b-b8e8-d26bbd90e5be.htm language=enus -->
## TOPIC 00082: ninetdigitalfx40ref/html/74f178ef-5401-374b-b8e8-d26bbd90e5be.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/74f178ef-5401-374b-b8e8-d26bbd90e5be.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/74f178ef-5401-374b-b8e8-d26bbd90e5be.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.Lock Method

DigitalDriverUtilityLock Method

Acquires a synchronization lock on this instance of the driver.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public IIviDriverLock Lock()
```

```text
Public Function Lock As IIviDriverLock
```

###### Return Value

IIviDriverLock

###### Implements

##### Remarks

##### See Also

###### Reference

DigitalDriverUtility Class

Lock Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/74f6a60a-c5dc-1a33-31df-9897b4215a21.htm language=enus -->
## TOPIC 00083: ninetdigitalfx40ref/html/74f6a60a-c5dc-1a33-31df-9897b4215a21.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/74f6a60a-c5dc-1a33-31df-9897b4215a21.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/74f6a60a-c5dc-1a33-31df-9897b4215a21.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.AbortKeepAlive Method

DigitalPatternControlAbortKeepAlive Method

Stops the keep alive pattern if it is currently running.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void AbortKeepAlive()
```

```text
Public Sub AbortKeepAlive
```

##### Remarks

If a pattern burst is in progress, this method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.

For more information, refer to the [Keep Alive Patterns](/csh?topicname=digipat/keep-alive-patterns.html) topic of the Digital Pattern Help.

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/74fc4871-7f8a-23a4-8906-d39d45f03c42.htm language=enus -->
## TOPIC 00084: ninetdigitalfx40ref/html/74fc4871-7f8a-23a4-8906-d39d45f03c42.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/74fc4871-7f8a-23a4-8906-d39d45f03c42.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/74fc4871-7f8a-23a4-8906-d39d45f03c42.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverIdentity.GetSupportedInstrumentModels Method

DigitalDriverIdentityGetSupportedInstrumentModels Method

Returns an array of strings containing the names of the instrument models with which the NI-Digital Pattern Driver software is compatible.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string[] GetSupportedInstrumentModels()
```

```text
Public Function GetSupportedInstrumentModels As String()
```

###### Return Value

String

###### Implements

##### See Also

###### Reference

DigitalDriverIdentity Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/75888a4b-be9c-dc81-9398-eefa3fc31e24.htm language=enus -->
## TOPIC 00085: ninetdigitalfx40ref/html/75888a4b-be9c-dc81-9398-eefa3fc31e24.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/75888a4b-be9c-dc81-9398-eefa3fc31e24.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/75888a4b-be9c-dc81-9398-eefa3fc31e24.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCVoltage.VoltageLevel Property

DigitalSourceDCVoltageVoltageLevel Property

Gets or sets the voltage level, in volts, that the PPMU forces to the DUT.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double VoltageLevel { get; set; }
```

```text
Public Property VoltageLevel As Double
	Get
	Set
```

###### Property Value

Double

The voltage level in volts forced to the DUT. The default value is 0.0.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for VoltageLevel is invalid. |

##### Remarks

SelectedFunction

Ppmu

OutputFunction

DCVoltage

Changing this property does not take affect until you call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm). 
 You can call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm) to commit your changes even if the PPMU
 is already sourcing.

##### See Also

###### Reference

DigitalSourceDCVoltage Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/75c7d626-9322-fd39-50ff-14a34e18756d.htm language=enus -->
## TOPIC 00086: ninetdigitalfx40ref/html/75c7d626-9322-fd39-50ff-14a34e18756d.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/75c7d626-9322-fd39-50ff-14a34e18756d.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/75c7d626-9322-fd39-50ff-14a34e18756d.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.PinAndChannelMap Property

NIDigitalPinAndChannelMap Property

DigitalPinAndChannelMap

NIDigital

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalPinAndChannelMap PinAndChannelMap { get; }
```

```text
Public ReadOnly Property PinAndChannelMap As DigitalPinAndChannelMap
	Get
```

###### Property Value

DigitalPinAndChannelMap

NIDigital

NIDigital

##### Remarks

PinAndChannelMap

DigitalPinSet

GetPinSet(String)

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/769fb2da-ecbb-937c-8d93-89e08f73fbc9.htm language=enus -->
## TOPIC 00087: ninetdigitalfx40ref/html/769fb2da-ecbb-937c-8d93-89e08f73fbc9.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/769fb2da-ecbb-937c-8d93-89e08f73fbc9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/769fb2da-ecbb-937c-8d93-89e08f73fbc9.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceWaveforms.CreateSerial Method

DigitalSourceWaveformsCreateSerial Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateSerial(String, String, SourceDataMapping, UInt32, BitOrder) | Creates the source waveform settings used to source serial waveforms using a comma-delimited string of pins or channels. |
|  | CreateSerial(DigitalPinSet, String, SourceDataMapping, UInt32, BitOrder) | Creates the source waveform settings used to source serial waveforms using a specified DigitalPinSet. |

Top

##### See Also

###### Reference

DigitalSourceWaveforms Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/76ddee58-16ed-1988-b3bf-79bd08a9150c.htm language=enus -->
## TOPIC 00088: ninetdigitalfx40ref/html/76ddee58-16ed-1988-b3bf-79bd08a9150c.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/76ddee58-16ed-1988-b3bf-79bd08a9150c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/76ddee58-16ed-1988-b3bf-79bd08a9150c.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.GetChannelNameFromString Method

DigitalDriverUtilityGetChannelNameFromString Method

String

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string GetChannelNameFromString(
	string index
)
```

```text
Public Function GetChannelNameFromString ( 
	index As String
) As String
```

###### Parameters

- **index**
  - Type: SystemString Index list for the desired channels in the session. Valid values are from zero to one less than the number of channels in the session. The input string can be in one of the following formats: A comma-separated list—for example, "0,1,2,3"; a range using a hyphen—for example, "0-3"; or a range using a colon—for example, "0:3." You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated values are supported ("2,3,0","1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.

###### Return Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The GetChannelNameFromString(String) method was called after the associated NIDigital or DigitalDriverUtility object was disposed. |
| ArgumentException | If one of the indexes in the list is out of range (less than zero or greater than number of channels minus one) |
| SelectorNameException | If the input list does not have a valid format |
| IviCDriverException | If the input list is empty or null |

##### See Also

###### Reference

DigitalDriverUtility Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/76e190d0-4380-55af-cae0-906aaea81a76.htm language=enus -->
## TOPIC 00089: ninetdigitalfx40ref/html/76e190d0-4380-55af-cae0-906aaea81a76.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/76e190d0-4380-55af-cae0-906aaea81a76.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/76e190d0-4380-55af-cae0-906aaea81a76.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRam Properties

DigitalHistoryRam Properties

The [DigitalHistoryRam](cf1149e0-976e-24a7-23fc-7dcdb3de8288.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | BufferSizePerSite | Gets or sets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition. |
|  | CyclesToAcquire | Gets or sets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0. |
|  | MaximumSamplesToAcquirePerSite | Gets or sets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. |
|  | NumberOfSamplesIsFinite | Gets or sets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst. |

Top

##### See Also

###### Reference

DigitalHistoryRam Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/773c48d9-c3b6-1e4b-1afa-5a6586ed5932.htm language=enus -->
## TOPIC 00090: ninetdigitalfx40ref/html/773c48d9-c3b6-1e4b-1afa-5a6586ed5932.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/773c48d9-c3b6-1e4b-1afa-5a6586ed5932.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/773c48d9-c3b6-1e4b-1afa-5a6586ed5932.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinInformation.ChannelName Property

DigitalPinInformationChannelName Property

Gets the 0-based channel name.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string ChannelName { get; }
```

```text
Public ReadOnly Property ChannelName As String
	Get
```

###### Property Value

String

##### See Also

###### Reference

DigitalPinInformation Structure

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/779f3bf0-ee78-ef2a-3efb-227bb2e9f83b.htm language=enus -->
## TOPIC 00091: ninetdigitalfx40ref/html/779f3bf0-ee78-ef2a-3efb-227bb2e9f83b.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/779f3bf0-ee78-ef2a-3efb-227bb2e9f83b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/779f3bf0-ee78-ef2a-3efb-227bb2e9f83b.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.Dispose Method

DigitalDriverUtilityDispose Method

DigitalDriverUtility

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### See Also

###### Reference

DigitalDriverUtility Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/780602a7-f5b9-309f-06d0-e96d27922bb1.htm language=enus -->
## TOPIC 00092: ninetdigitalfx40ref/html/780602a7-f5b9-309f-06d0-e96d27922bb1.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/780602a7-f5b9-309f-06d0-e96d27922bb1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/780602a7-f5b9-309f-06d0-e96d27922bb1.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverOperation.IOResourceDescriptor Property

DigitalDriverOperationIOResourceDescriptor Property

Gets a string containing the resource name used to identify the instrument.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string IOResourceDescriptor { get; }
```

```text
Public ReadOnly Property IOResourceDescriptor As String
	Get
```

###### Property Value

String

###### Implements

##### See Also

###### Reference

DigitalDriverOperation Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/7bde57bb-3756-4976-977f-75606d5212c0.htm language=enus -->
## TOPIC 00093: ninetdigitalfx40ref/html/7bde57bb-3756-4976-977f-75606d5212c0.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/7bde57bb-3756-4976-977f-75606d5212c0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/7bde57bb-3756-4976-977f-75606d5212c0.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinAndChannelMap.CreatePinMap Method

DigitalPinAndChannelMapCreatePinMap Method

LoadPinMap(String)

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreatePinMap(
	string[] dutPins,
	string[] systemPins
)
```

```text
Public Sub CreatePinMap ( 
	dutPins As String(),
	systemPins As String()
)
```

###### Parameters

- **dutPins**
  - Type: SystemString An array of DUT pin names to include in the pin map. DUT pins are duplicated for all sites and are used in patterns.
- **systemPins**
  - Type: SystemString An array of system pin names to include in the pin map. System pins do not scale with the number of sites and are not used with pattern functions.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | dutPins or systemPins is or not initialized.dutPins or systemPins contains an invalid pin name. |

##### Remarks

dutPins

systemPins

DigitalPinAndChannelMap

MapPinToChannel(String, Int32, String)

##### See Also

###### Reference

DigitalPinAndChannelMap Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/849477ad-c845-f33c-484f-9bedf82c26af.htm language=enus -->
## TOPIC 00094: ninetdigitalfx40ref/html/849477ad-c845-f33c-484f-9bedf82c26af.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/849477ad-c845-f33c-484f-9bedf82c26af.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/849477ad-c845-f33c-484f-9bedf82c26af.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.LoadLevels Method (String)

NIDigitalLoadLevels Method (String)

Loads a levels sheet from file.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void LoadLevels(
	string filePath
)
```

```text
Public Sub LoadLevels ( 
	filePath As String
)
```

###### Parameters

- **filePath**
  - Type: SystemString The absolute file path to the pin levels file.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |

##### Remarks

If the levels sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas are evaluated at load time.

##### See Also

###### Reference

NIDigital Class

LoadLevels Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/85b5aa73-84c2-cfe6-e21a-9717dfdb005a.htm language=enus -->
## TOPIC 00095: ninetdigitalfx40ref/html/85b5aa73-84c2-cfe6-e21a-9717dfdb005a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/85b5aa73-84c2-cfe6-e21a-9717dfdb005a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/85b5aa73-84c2-cfe6-e21a-9717dfdb005a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSoftwareStartTrigger Methods

DigitalSoftwareStartTrigger Methods

The [DigitalSoftwareStartTrigger](bcc9a627-384c-3c41-8783-ad1dc176174b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the TriggerType for Software triggering. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | Send | Sends the software start trigger to a digital pattern instrument, forcing the start trigger to assert, regardless of how the start trigger is configured. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalSoftwareStartTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/888a241f-1135-ac5c-02ca-43b337faeee3.htm language=enus -->
## TOPIC 00096: ninetdigitalfx40ref/html/888a241f-1135-ac5c-02ca-43b337faeee3.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/888a241f-1135-ac5c-02ca-43b337faeee3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/888a241f-1135-ac5c-02ca-43b337faeee3.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.IsDone Property

DigitalPatternControlIsDone Property

Gets a value that indicates whether the pattern burst completed or if any errors have occurred.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public bool IsDone { get; }
```

```text
Public ReadOnly Property IsDone As Boolean
	Get
```

###### Property Value

Boolean

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/896277f4-295a-958b-8b12-b863bed9a8d4.htm language=enus -->
## TOPIC 00097: ninetdigitalfx40ref/html/896277f4-295a-958b-8b12-b863bed9a8d4.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/896277f4-295a-958b-8b12-b863bed9a8d4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/896277f4-295a-958b-8b12-b863bed9a8d4.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

TimeSetEdge Enumeration

TimeSetEdge Enumeration

Specifies the edge of the time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public enum TimeSetEdge
```

```text
Public Enumeration TimeSetEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DriveOn | 2800 | Specifies the drive on edge of the time set. |
|  | DriveData | 2801 | Specifies the drive data edge of the time set. |
|  | DriveReturn | 2802 | Specifies the drive return edge of the time set. |
|  | DriveOff | 2803 | Specifies the drive off edge of the time set. |
|  | CompareStrobe | 2804 | Specifies the compare strobe of the time set. |
|  | DriveData2 | 2805 | Specifies the drive data 2 edge of the time set. |
|  | DriveReturn2 | 2806 | Specifies the drive return 2 edge of the time set. |
|  | CompareStrobe2 | 2807 | Specifies the compare strobe 2 of the time set. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8a216e21-2767-9e1d-699e-3f3c7019b862.htm language=enus -->
## TOPIC 00098: ninetdigitalfx40ref/html/8a216e21-2767-9e1d-699e-3f3c7019b862.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8a216e21-2767-9e1d-699e-3f3c7019b862.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8a216e21-2767-9e1d-699e-3f3c7019b862.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverOperation.LogicalName Property

DigitalDriverOperationLogicalName Property

Gets a string containing the logical name that was specified when the current session was opened.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string LogicalName { get; }
```

```text
Public ReadOnly Property LogicalName As String
	Get
```

###### Property Value

String

NIDigital

###### Implements

##### See Also

###### Reference

DigitalDriverOperation Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8ac6ba59-0301-644d-8f5d-c97c83dd52c0.htm language=enus -->
## TOPIC 00099: ninetdigitalfx40ref/html/8ac6ba59-0301-644d-8f5d-c97c83dd52c0.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8ac6ba59-0301-644d-8f5d-c97c83dd52c0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8ac6ba59-0301-644d-8f5d-c97c83dd52c0.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceWaveforms.CreateParallel Method (String, String, SourceDataMapping)

DigitalSourceWaveformsCreateParallel Method (String, String, SourceDataMapping)

Creates source waveform settings used to source parallel data using a comma-delimited string of pins or channels.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateParallel(
	string pinSetString,
	string waveformName,
	SourceDataMapping dataMapping
)
```

```text
Public Sub CreateParallel ( 
	pinSetString As String,
	waveformName As String,
	dataMapping As SourceDataMapping
)
```

###### Parameters

- **pinSetString**
  - Type: SystemString The set of pins or channels for which to create the waveform. The pins or channels represented by the pinSetString must match the source pins in the pattern that references the waveform. The pin order in the pin set string determines the bit positions of the data written using one of the write waveform methods on the DigitalSourceWaveforms object.
- **waveformName**
  - Type: SystemString The name of the waveform to use in the pattern file. Waveform names must be unique. Use this waveformName with the source_start opcode in your pattern.
- **dataMapping**
  - Type: NationalInstruments.ModularInstruments.NIDigitalSourceDataMapping Specifies whether the waveform is broadcast to all sites or a unique waveform is sourced per site.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| ArgumentException | The value for waveformName is an empty string or contains an invalid character. |
| OutOfRangeException | The value for dataMapping is invalid.The number of waveforms in source memory exceeds maximum number of waveforms allowed. |

##### Remarks

You cannot reconfigure settings after waveforms are created.

Opcodes

Source Waveform Configurations

##### See Also

###### Reference

DigitalSourceWaveforms Class

CreateParallel Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8b13ac0b-0447-9e1b-c0a1-aed369a968f9.htm language=enus -->
## TOPIC 00100: ninetdigitalfx40ref/html/8b13ac0b-0447-9e1b-c0a1-aed369a968f9.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8b13ac0b-0447-9e1b-c0a1-aed369a968f9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8b13ac0b-0447-9e1b-c0a1-aed369a968f9.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverOperation.Dispose Method

DigitalDriverOperationDispose Method

DigitalDriverOperation

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### See Also

###### Reference

DigitalDriverOperation Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8bf859af-e730-b0ad-3451-25ec7316958a.htm language=enus -->
## TOPIC 00101: ninetdigitalfx40ref/html/8bf859af-e730-b0ad-3451-25ec7316958a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8bf859af-e730-b0ad-3451-25ec7316958a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8bf859af-e730-b0ad-3451-25ec7316958a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCVoltage Class

DigitalSourceDCVoltage Class

OutputFunction

DCVoltage

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalSourceDCVoltage : DigitalSubObject
```

```text
Public NotInheritable Class DigitalSourceDCVoltage
	Inherits DigitalSubObject
```

The DigitalSourceDCVoltage type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | CurrentLimit | Gets or sets the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. |
|  | CurrentLimitBehavior | Gets or sets the current limit behavior, which controls how the output current reacts when the current limit is reached. |
|  | CurrentLimitRange | Gets or sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. |
|  | IsCurrentLimitSupported | Gets a value indicating whether the instrument supports configuration of a current limit when you set the PPMU OutputFunction to DCVoltage. |
|  | VoltageLevel | Gets or sets the voltage level, in volts, that the PPMU forces to the DUT. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureCurrentLimit | Configures the current limit for the pin set when forcing voltage. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8e18911b-ffe2-677c-bd32-f1df33be3e42.htm language=enus -->
## TOPIC 00102: ninetdigitalfx40ref/html/8e18911b-ffe2-677c-bd32-f1df33be3e42.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8e18911b-ffe2-677c-bd32-f1df33be3e42.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8e18911b-ffe2-677c-bd32-f1df33be3e42.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRam.FetchCycleInformation Method (String, String, Int64, Int64)

DigitalHistoryRamFetchCycleInformation Method (String, String, Int64, Int64)

Fetches the pattern information acquired for the specified History RAM samples.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalHistoryRamCycleInformation[] FetchCycleInformation(
	string site,
	string pinSetString,
	long position,
	long samplesToRead
)
```

```text
Public Function FetchCycleInformation ( 
	site As String,
	pinSetString As String,
	position As Long,
	samplesToRead As Long
) As DigitalHistoryRamCycleInformation()
```

###### Parameters

- **site**
  - Type: SystemStringThe site to query.
- **pinSetString**
  - Type: SystemStringThe set of pins or channels for which to fetch pattern information.
- **position**
  - Type: SystemInt64The position from which to start fetching pattern information.
- **samplesToRead**
  - Type: SystemInt64The number of samples to read. Use -1 to fetch all samples.

###### Return Value

DigitalHistoryRamCycleInformation

DigitalHistoryRamCycleInformation

##### Exceptions

| Exception | Condition |
| --- | --- |
| OperationPendingException | The specified operation cannot be performed during a pattern burst. |
| ArgumentException | The value for site is invalid.The value for position is invalid.The value for samplesToRead is invalid. - or - The position or the number of samples to read exceeded the number of samples available. |
| SelectorNameException | The pinSetString contains a pin or pin group name not loaded in the pin map. |
| InvalidOperationException | The pinSetString contains a system pin. |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | FetchCycleInformation(String, String, Int64, Int64) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalHistoryRam Class

FetchCycleInformation Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8e5c7c31-f60e-b48a-e167-d786cbfda053.htm language=enus -->
## TOPIC 00103: ninetdigitalfx40ref/html/8e5c7c31-f60e-b48a-e167-d786cbfda053.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8e5c7c31-f60e-b48a-e167-d786cbfda053.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8e5c7c31-f60e-b48a-e167-d786cbfda053.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverIdentity.Description Property

DigitalDriverIdentityDescription Property

Gets a string containing a description of the specific NI-Digital Pattern Driver software.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string Description { get; }
```

```text
Public ReadOnly Property Description As String
	Get
```

###### Property Value

String

NIDigital

###### Implements

##### See Also

###### Reference

DigitalDriverIdentity Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/8ef87a48-513e-9bb8-b04c-423f4f9d2e7c.htm language=enus -->
## TOPIC 00104: ninetdigitalfx40ref/html/8ef87a48-513e-9bb8-b04c-423f4f9d2e7c.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/8ef87a48-513e-9bb8-b04c-423f4f9d2e7c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/8ef87a48-513e-9bb8-b04c-423f4f9d2e7c.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.ConfigureDriveEdges Method

DigitalTimeSetConfigureDriveEdges Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureDriveEdges(String, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and the drive edge placement for the specified pins. |
|  | ConfigureDriveEdges(DigitalPinSet, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and drive edge placement for the specified pin set. |
|  | ConfigureDriveEdges(String, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and the drive edge placement for the specified pins. |
|  | ConfigureDriveEdges(DigitalPinSet, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan) | Configures the drive format and drive edge placement for the specified pin set. |

Top

##### See Also

###### Reference

DigitalTimeSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/9525d59c-8a4c-350b-b608-fd190a8b457e.htm language=enus -->
## TOPIC 00105: ninetdigitalfx40ref/html/9525d59c-8a4c-350b-b608-fd190a8b457e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/9525d59c-8a4c-350b-b608-fd190a8b457e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/9525d59c-8a4c-350b-b608-fd190a8b457e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.BurstPattern Method (String, String, Boolean, Boolean, TimeSpan)

DigitalPatternControlBurstPattern Method (String, String, Boolean, Boolean, TimeSpan)

Starts a pattern burst and optionally blocks program execution until the pattern burst is complete.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void BurstPattern(
	string siteList,
	string startLabel,
	bool selectDigitalFunction,
	bool waitUntilDone,
	TimeSpan maxTime
)
```

```text
Public Sub BurstPattern ( 
	siteList As String,
	startLabel As String,
	selectDigitalFunction As Boolean,
	waitUntilDone As Boolean,
	maxTime As TimeSpan
)
```

###### Parameters

- **siteList**
  - Type: SystemString The sites on which to burst the pattern as a comma-delimited list of strings of the form siteN, where N is the site number. If you specify an empty string, the pattern is burst on all sites.
- **startLabel**
  - Type: SystemString The pattern name or exported pattern label from which to start bursting the pattern.
- **selectDigitalFunction**
  - Type: SystemBooleanIf , sets the SelectedFunction of the pins to Digital.
- **waitUntilDone**
  - Type: SystemBoolean If , waits until the pattern burst is completed; otherwise, initiates a pattern burst and returns.
- **maxTime**
  - Type: SystemTimeSpan The maximum time interval allowed for the pattern burst to complete.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| InvalidOperationException | BurstPattern(String, String, Boolean, Boolean, TimeSpan) is called before loading a pattern. |
| SelectorNameException | The value for siteList contains an invalid site. |
| MaxTimeExceededException | The value for waitUntilDone is set to , and the pattern burst took longer than the specified maxTime. |
| ArgumentException | One or more of the configured properties of the underlying NI-Digital Pattern Driver were invalid. |

##### Remarks

maxTime

GetSitePassFail(String)

For more information, refer to the [Session State Model](/csh?topicname=digipat/programming-states.html) topic of the Digital Pattern Help.

##### See Also

###### Reference

DigitalPatternControl Class

BurstPattern Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/95885e76-d048-addd-f106-e968203515cb.htm language=enus -->
## TOPIC 00106: ninetdigitalfx40ref/html/95885e76-d048-addd-f106-e968203515cb.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/95885e76-d048-addd-f106-e968203515cb.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/95885e76-d048-addd-f106-e968203515cb.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinAndChannelMap Methods

DigitalPinAndChannelMap Methods

The [DigitalPinAndChannelMap](32f6cb88-4893-e84e-35f4-0dfcfd967441.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateChannelMap | Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap(String, String) before calling this method. |
|  | CreatePinGroup | Creates a pin group with the specified name. The pin group serves as an alias for a list of pins. |
|  | CreatePinMap | Creates and loads a pin map. Use this method if you are not loading a pin map file using LoadPinMap(String). |
|  | EndChannelMap | Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPinSet | Returns a DigitalPinSet object representing a set of either channels or pins. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MapPinToChannel | Maps a pin to a digital pattern instrument channel. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalPinAndChannelMap Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/95e1c6d9-77da-6ab9-f739-79ac78216b0a.htm language=enus -->
## TOPIC 00107: ninetdigitalfx40ref/html/95e1c6d9-77da-6ab9-f739-79ac78216b0a.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/95e1c6d9-77da-6ab9-f739-79ac78216b0a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/95e1c6d9-77da-6ab9-f739-79ac78216b0a.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverIdentity Class

DigitalDriverIdentity Class

Provides information about the instrument and the NI-Digital Pattern Driver software.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalDriverIdentity : DigitalSubObject, 
	IIviDriverIdentity, IIviComponentIdentity
```

```text
Public NotInheritable Class DigitalDriverIdentity
	Inherits DigitalSubObject
	Implements IIviDriverIdentity, IIviComponentIdentity
```

The DigitalDriverIdentity type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets a string containing a description of the specific NI-Digital Pattern Driver software. |
|  | Identifier | Gets a string containing the case-sensitive unique identifier of the NI-Digital Pattern Driver software. |
|  | InstrumentFirmwareRevision | Gets a string containing the firmware revision information for the digital pattern instrument currently in use. |
|  | InstrumentManufacturer | Gets a string containing the name of the manufacturer for the digital pattern instrument currently in use. |
|  | InstrumentModel | Gets a string containing the model number or name of the digital pattern instrument currently in use. |
|  | Revision | Gets a string containing any additional version information about the NI-Digital Pattern Driver software. |
|  | SerialNumber | Gets a string containing the serial number of the digital pattern instrument currently in use. |
|  | SpecificationMajorVersion | Gets an integer that specifies the major version number of the class specification in accordance with which the NationalInstruments.ModularInstruments.NIDigital .NET class library was developed. |
|  | SpecificationMinorVersion | Gets an integer that specifies the minor version number of the class specification in accordance with which the NationalInstruments.ModularInstruments.NIDigital .NET class library was developed. |
|  | Vendor | Gets a string containing the name of the vendor that supplies the NI-Digital Pattern Driver software. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetGroupCapabilities | Returns an array of strings containing the names of the IVI class capability groups, or standard methods and properties, that the NI-Digital Pattern Driver software implements. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetSupportedInstrumentModels | Returns an array of strings containing the names of the instrument models with which the NI-Digital Pattern Driver software is compatible. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

Use this class to get information about the instrument, such as the vendor, manufacturer, or revision.

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/96d0b560-1ec5-fef2-dfe6-01cbe78183c7.htm language=enus -->
## TOPIC 00108: ninetdigitalfx40ref/html/96d0b560-1ec5-fef2-dfe6-01cbe78183c7.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/96d0b560-1ec5-fef2-dfe6-01cbe78183c7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/96d0b560-1ec5-fef2-dfe6-01cbe78183c7.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEvent.PatternOpcodeEvents Property

DigitalEventPatternOpcodeEvents Property

DigitalPatternOpcodeEvent

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalPatternOpcodeEvent[] PatternOpcodeEvents { get; }
```

```text
Public ReadOnly Property PatternOpcodeEvents As DigitalPatternOpcodeEvent()
	Get
```

###### Property Value

DigitalPatternOpcodeEvent

Object used to configure and control pattern opcode events. This object is created when the [DigitalEvent](150fe4a2-0dba-3572-fa9d-509fc66319be.htm) is created.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | DigitalPatternOpcodeEvent was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalEvent Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/96dc5f45-757b-3abe-5bef-4abc05c1a16c.htm language=enus -->
## TOPIC 00109: ninetdigitalfx40ref/html/96dc5f45-757b-3abe-5bef-4abc05c1a16c.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/96dc5f45-757b-3abe-5bef-4abc05c1a16c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/96dc5f45-757b-3abe-5bef-4abc05c1a16c.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.LoadTiming Method

NIDigitalLoadTiming Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | LoadTiming(IEnumerableString) | Loads one or more time sets from a list of timing sheet files. |
|  | LoadTiming(String) | Loads one or more time sets from a timing sheet file. |

Top

##### See Also

###### Reference

NIDigital Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/9a50c401-f132-4317-6d0a-488ada4a626e.htm language=enus -->
## TOPIC 00110: ninetdigitalfx40ref/html/9a50c401-f132-4317-6d0a-488ada4a626e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/9a50c401-f132-4317-6d0a-488ada4a626e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/9a50c401-f132-4317-6d0a-488ada4a626e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.GetEdge Method (DigitalPinSet, TimeSetEdge)

DigitalTimeSetGetEdge Method (DigitalPinSet, TimeSetEdge)

Gets the edge time of a time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PrecisionTimeSpan GetEdge(
	DigitalPinSet pinSet,
	TimeSetEdge edge
)
```

```text
Public Function GetEdge ( 
	pinSet As DigitalPinSet,
	edge As TimeSetEdge
) As PrecisionTimeSpan
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The pin set for which to get the edge.
- **edge**
  - Type: NationalInstruments.ModularInstruments.NIDigitalTimeSetEdge The edge of the time set to get.

###### Return Value

PrecisionTimeSpan

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

##### See Also

###### Reference

DigitalTimeSet Class

GetEdge Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/9aec1a01-42c7-28df-9508-da956c2eff36.htm language=enus -->
## TOPIC 00111: ninetdigitalfx40ref/html/9aec1a01-42c7-28df-9508-da956c2eff36.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/9aec1a01-42c7-28df-9508-da956c2eff36.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/9aec1a01-42c7-28df-9508-da956c2eff36.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSequencerFlagTrigger Class

DigitalSequencerFlagTrigger Class

Provides the configuration for the sequencer flag trigger.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalSequencerFlagTrigger : DigitalSubObject
```

```text
Public NotInheritable Class DigitalSequencerFlagTrigger
	Inherits DigitalSubObject
```

The DigitalSequencerFlagTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | TerminalName | Gets a string containing the terminal name of the DigitalSequencerFlagTrigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/9f69cb6c-9702-747f-782d-a2f775fcba05.htm language=enus -->
## TOPIC 00112: ninetdigitalfx40ref/html/9f69cb6c-9702-747f-782d-a2f775fcba05.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/9f69cb6c-9702-747f-782d-a2f775fcba05.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/9f69cb6c-9702-747f-782d-a2f775fcba05.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCCurrent.ConfigureVoltageLimits Method

DigitalSourceDCCurrentConfigureVoltageLimits Method

Specifies the voltage limit high, or high clamp voltage (Vch), and voltage limit low, or low clamp voltage (Vcl) for the pin set when forcing current.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureVoltageLimits(
	double voltageLimitLow,
	double voltageLimitHigh
)
```

```text
Public Sub ConfigureVoltageLimits ( 
	voltageLimitLow As Double,
	voltageLimitHigh As Double
)
```

###### Parameters

- **voltageLimitLow**
  - Type: SystemDouble The nominal voltage at the pin at which the low side voltage clamp activates when the PPMU forces current to the DUT.
- **voltageLimitHigh**
  - Type: SystemDouble The nominal voltage at the pin at which the high side voltage clamp activates when the PPMU forces current to the DUT.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for voltageLimitLow is invalid.The value for voltageLimitHigh is invalid. |

##### Remarks

SelectedFunction

Ppmu

When forcing current by setting the PPMU [OutputFunction](655db2b5-0c24-cfe7-a61f-56272413faed.htm) to
 [DCCurrent](a50bb129-cc85-c191-93e2-ebdb282f0bcd.htm), the voltage is clamped to the specified voltage limits. Select the smallest voltage limits appropriate for the DUT.

If the voltage required by the DUT exceeds the specified voltage limits, the current output may not meet the specified current level. Choose larger voltage limits as needed and appropriate for the DUT.

Changing this property does not take affect until you call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm). 
 You can call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm) to commit your changes even if the PPMU
 is already sourcing.

##### See Also

###### Reference

DigitalSourceDCCurrent Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/a3562d1d-f77b-0f43-87c3-03d634a9ae68.htm language=enus -->
## TOPIC 00113: ninetdigitalfx40ref/html/a3562d1d-f77b-0f43-87c3-03d634a9ae68.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/a3562d1d-f77b-0f43-87c3-03d634a9ae68.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/a3562d1d-f77b-0f43-87c3-03d634a9ae68.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl Properties

DigitalPatternControl Properties

The [DigitalPatternControl](a8acec70-bc5b-3361-e849-c1936b524399.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HaltOnKeepAliveOpcode | Gets or sets a value that indicates whether keep_alive opcodes should behave like halt opcodes. |
|  | IsDone | Gets a value that indicates whether the pattern burst completed or if any errors have occurred. |
|  | IsKeepAliveActive | Gets a value that indicates whether the instrument is driving a keep alive pattern. |
|  | StartLabel | Gets or sets the pattern name or exported pattern label from which to start bursting the pattern. |

Top

##### See Also

###### Reference

DigitalPatternControl Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/a3c3bd12-aad3-2a73-c053-532fe3042103.htm language=enus -->
## TOPIC 00114: ninetdigitalfx40ref/html/a3c3bd12-aad3-2a73-c053-532fe3042103.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/a3c3bd12-aad3-2a73-c053-532fe3042103.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/a3c3bd12-aad3-2a73-c053-532fe3042103.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.SortPinResultsBySite Method (NIDigital[], String, Int64[][], String[], Int32[])

DigitalDriverUtilitySortPinResultsBySite Method (NIDigital, String, Int64, String, Int32)

Organizes data read from multiple digital pattern instruments by grouping the data by site number.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public static long[] SortPinResultsBySite(
	NIDigital[] sessions,
	string pinSetString,
	long[][] resultsToSort,
	out string[] pinNames,
	out int[] siteNumbers
)
```

```text
Public Shared Function SortPinResultsBySite ( 
	sessions As NIDigital(),
	pinSetString As String,
	resultsToSort As Long()(),
	<OutAttribute> ByRef pinNames As String(),
	<OutAttribute> ByRef siteNumbers As Integer()
) As Long()
```

###### Parameters

- **sessions**
  - Type: NationalInstruments.ModularInstruments.NIDigitalNIDigitalThe instrument sessions to return data for.
- **pinSetString**
  - Type: SystemStringThe pin set from which to read data.
- **resultsToSort**
  - Type: SystemInt64The data read from the digital pattern instruments, combined into a two-dimensional array.
- **pinNames**
  - Type: SystemStringAn array of DUT pin names corresponding to the values in DUT pin results.
- **siteNumbers**
  - Type: SystemInt32An array of site numbers corresponding to the values in DUT pin results.

###### Return Value

Int64

pinNames

GetPinResultsPinInformation(String)

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

DigitalDriverUtility Class

SortPinResultsBySite Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/a3ef19cb-c95f-e064-54fe-24290ded6113.htm language=enus -->
## TOPIC 00115: ninetdigitalfx40ref/html/a3ef19cb-c95f-e064-54fe-24290ded6113.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/a3ef19cb-c95f-e064-54fe-24290ded6113.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/a3ef19cb-c95f-e064-54fe-24290ded6113.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinSet.ToString Method

DigitalPinSetToString Method

Returns the pin set string this pin set represents.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### See Also

###### Reference

DigitalPinSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/a4290594-1af8-15fa-338d-6c29633838fa.htm language=enus -->
## TOPIC 00116: ninetdigitalfx40ref/html/a4290594-1af8-15fa-338d-6c29633838fa.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/a4290594-1af8-15fa-338d-6c29633838fa.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/a4290594-1af8-15fa-338d-6c29633838fa.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital.LoadTiming Method (IEnumerable(String))

NIDigitalLoadTiming Method (IEnumerableString)

Loads one or more time sets from a list of timing sheet files.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void LoadTiming(
	IEnumerable<string> filePaths
)
```

```text
Public Sub LoadTiming ( 
	filePaths As IEnumerable(Of String)
)
```

###### Parameters

- **filePaths**
  - Type: System.Collections.GenericIEnumerableString The absolute file paths to the timing sheet files.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |

##### Remarks

If a timing sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas are evaluated at load time.

##### See Also

###### Reference

NIDigital Class

LoadTiming Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/a594d097-35cf-d000-2cb8-42f744f99759.htm language=enus -->
## TOPIC 00117: ninetdigitalfx40ref/html/a594d097-35cf-d000-2cb8-42f744f99759.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/a594d097-35cf-d000-2cb8-42f744f99759.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/a594d097-35cf-d000-2cb8-42f744f99759.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverOperation Properties

DigitalDriverOperation Properties

The [DigitalDriverOperation](3ef24f02-b47c-2085-3d20-23cedb5c5169.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Cache | Gets or sets a value indicating whether to cache the values of properties. |
|  | DriverSetup | Gets the string used to set the initial values for NIDigital properties. |
|  | InterchangeCheck | Gets or sets a value indicating whether to perform interchangeability checking and retrieve interchangeability warnings. |
|  | IOResourceDescriptor | Gets a string containing the resource name used to identify the instrument. |
|  | LogicalName | Gets a string containing the logical name that was specified when the current session was opened. |
|  | QueryInstrumentStatus | Gets or sets a value indicating whether the NI-Digital Pattern driver software queries the instrument status after each operation. |
|  | RangeCheck | Gets or sets a value indicating whether to validate values and method parameters. |
|  | RecordCoercions | Gets or sets a value indicating whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. |
|  | Simulate | Gets or sets a value indicating whether to simulate NI-Digital Pattern Driver software I/O operations. |

Top

##### See Also

###### Reference

DigitalDriverOperation Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/a9bc6206-439a-462a-8498-51ef00dfe10b.htm language=enus -->
## TOPIC 00118: ninetdigitalfx40ref/html/a9bc6206-439a-462a-8498-51ef00dfe10b.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/a9bc6206-439a-462a-8498-51ef00dfe10b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/a9bc6206-439a-462a-8498-51ef00dfe10b.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCVoltage.CurrentLimitRange Property

DigitalSourceDCVoltageCurrentLimitRange Property

Gets or sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public double CurrentLimitRange { get; set; }
```

```text
Public Property CurrentLimitRange As Double
	Get
	Set
```

###### Property Value

Double

Maximum current in amps that can be set. The default value is 2e-6.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for CurrentLimitRange is invalid. |

##### Remarks

SelectedFunction

Ppmu

OutputFunction

DCVoltage

Changing this property does not take affect until you call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm). 
 You can call [Source](3990109a-d47b-c9c8-5060-c68b62dd3203.htm) to commit your changes even if the PPMU
 is already sourcing.

##### See Also

###### Reference

DigitalSourceDCVoltage Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/ab234ddf-092c-34c6-4cb2-d01d9b18fa39.htm language=enus -->
## TOPIC 00119: ninetdigitalfx40ref/html/ab234ddf-092c-34c6-4cb2-d01d9b18fa39.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/ab234ddf-092c-34c6-4cb2-d01d9b18fa39.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/ab234ddf-092c-34c6-4cb2-d01d9b18fa39.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceDCVoltage.CurrentLimitBehavior Property

DigitalSourceDCVoltageCurrentLimitBehavior Property

Gets or sets the current limit behavior, which controls how the output current reacts when the current limit is reached.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public PpmuCurrentLimitBehavior CurrentLimitBehavior { get; set; }
```

```text
Public Property CurrentLimitBehavior As PpmuCurrentLimitBehavior
	Get
	Set
```

###### Property Value

PpmuCurrentLimitBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| OutOfRangeException | The value for CurrentLimitBehavior is invalid. |

##### See Also

###### Reference

DigitalSourceDCVoltage Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/afde1123-ab34-f058-75b2-a35a417c3ced.htm language=enus -->
## TOPIC 00120: ninetdigitalfx40ref/html/afde1123-ab34-f058-75b2-a35a417c3ced.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/afde1123-ab34-f058-75b2-a35a417c3ced.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/afde1123-ab34-f058-75b2-a35a417c3ced.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinAndChannelMap.CreateChannelMap Method

DigitalPinAndChannelMapCreateChannelMap Method

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateChannelMap(
	int numberOfSites
)
```

```text
Public Sub CreateChannelMap ( 
	numberOfSites As Integer
)
```

###### Parameters

- **numberOfSites**
  - Type: SystemInt32Number of sites in the channel map.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | The value for numberOfSites is invalid. |
| InvalidOperationException | The channel map has already been configured.The channel map configuration is not complete. |

##### Remarks

LoadPinMap(String)

You cannot modify the channel map within an instrument session after you load patterns or
 waveforms on the digital pattern instrument.

After calling this method, you can create channel map connections using [MapPinToChannel(String, Int32, String)](f2c3fcde-5ca9-6a3c-6888-01eed5e2a5f8.htm).
 You must call [EndChannelMap](0ca049e3-cc8f-2b9a-c200-c136b8f4bee5.htm)
 to finish creating a channel map.

##### See Also

###### Reference

DigitalPinAndChannelMap Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/b11a3137-5d6e-b0b9-8827-388ac828b49e.htm language=enus -->
## TOPIC 00121: ninetdigitalfx40ref/html/b11a3137-5d6e-b0b9-8827-388ac828b49e.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/b11a3137-5d6e-b0b9-8827-388ac828b49e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/b11a3137-5d6e-b0b9-8827-388ac828b49e.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRamTrigger.PatternLabel Property

DigitalHistoryRamTriggerPatternLabel Property

DigitalPatternLabelHistoryRamTrigger

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public DigitalPatternLabelHistoryRamTrigger PatternLabel { get; }
```

```text
Public ReadOnly Property PatternLabel As DigitalPatternLabelHistoryRamTrigger
	Get
```

###### Property Value

DigitalPatternLabelHistoryRamTrigger

Object used to configure and control the History RAM trigger as a pattern label History RAM trigger. This object is created when the
 [DigitalHistoryRamTrigger](6ef6eb01-ff0d-ebb4-a89e-e0af077e28d2.htm) object is created.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | PatternLabel was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalHistoryRamTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/b1c44701-b544-edf5-7a71-8f814cb19a16.htm language=enus -->
## TOPIC 00122: ninetdigitalfx40ref/html/b1c44701-b544-edf5-7a71-8f814cb19a16.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/b1c44701-b544-edf5-7a71-8f814cb19a16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/b1c44701-b544-edf5-7a71-8f814cb19a16.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

NIDigital Class

NIDigital Class

Represents a digital pattern instrument session.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class NIDigital : IDisposable, 
	IServiceProvider, IIviDriver, ITClockSynchronizableDevice
```

```text
Public NotInheritable Class NIDigital
	Implements IDisposable, IServiceProvider, IIviDriver, ITClockSynchronizableDevice
```

The NIDigital type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | NIDigital(IntPtr) | Initializes a new instance of the NIDigital class. Initializes an instrument driver session from an existing instrument handle. |
|  | NIDigital(String, Boolean, Boolean) | Initializes a new instance of the NIDigital class. Initializes a digital pattern instrument driver session and sets the initial state of session properties. |
|  | NIDigital(String, Boolean, Boolean, String) | Initializes a new instance of the NIDigital class. This overload is reserved for future use. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | CaptureWaveforms | Gets the DigitalCaptureWaveforms object containing methods for creating and fetching capture waveforms. |
|  | DriverOperation | Gets the DigitalDriverOperation object containing methods and properties that manage the operation of the driver. |
|  | Event | Gets the DigitalEvent object that contains the events for the NIDigital session. |
|  | HistoryRam | Gets the DigitalHistoryRam object containing methods for configuring and fetching History RAM contents. |
|  | Identity | Gets the DigitalDriverIdentity object, which contains properties that return information about the identity of the NI-Digital Pattern Driver software. |
|  | IsDisposed | Gets a value indicating whether the NIDigital session has been disposed. |
|  | NumberOfChannels | Gets the number of channels on the digital pattern instrument. |
|  | PatternControl | Gets the DigitalPatternControl control object, containing properties and methods for setting up and bursting a pattern. |
|  | PinAndChannelMap | Gets the DigitalPinAndChannelMap object that stores all the pin mapping information for the NIDigital session. |
|  | SourceWaveforms | Gets the DigitalSourceWaveforms object containing the functionality for creating and writing source waveforms. |
|  | Timing | Gets the DigitalTiming object that stores the time sets for the NIDigital session. |
|  | Trigger | Gets the DigitalTrigger object that contains the triggers for the NIDigital session. |
|  | Utility | Gets the DigitalDriverUtility object containing methods providing utility operations for the NI-Digital Pattern Driver. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ApplyLevelsAndTiming(String, String, String) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
|  | ApplyLevelsAndTiming(String, String, String, DigitalPinSet, DigitalPinSet, DigitalPinSet) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
|  | ApplyLevelsAndTiming(String, String, String, String, String, String) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
|  | Close | Closes the session with the digital pattern instrument. |
|  | DisableSites | Disables the specified sites. |
|  | Dispose | Disposes the NIDigital session. |
|  | EnableSites | Enables the specified sites. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | ExportSignal | Routes trigger and event signals to the specified outputTerminal. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetInstrumentHandle | Gets the SafeHandle to the NIDigital instrument session. |
|  | GetService | Gets the service object of the specified type. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | IsSiteEnabled | Returns whether the specified site is enabled or disabled. |
|  | LoadLevels(IEnumerableString) | Loads levels sheets from a list of pin levels files. |
|  | LoadLevels(String) | Loads a levels sheet from file. |
|  | LoadPattern | Loads a pattern to the hardware from a pattern file. |
|  | LoadPinMap | Loads a pin map file. |
|  | LoadSpecifications(IEnumerableString) | Loads specifications sheets from a list of specifications files. |
|  | LoadSpecifications(String) | Loads a specifications sheet from file. |
|  | LoadTiming(IEnumerableString) | Loads one or more time sets from a list of timing sheet files. |
|  | LoadTiming(String) | Loads one or more time sets from a timing sheet file. |
|  | SelfCalibrate | Performs a self-calibration on a digital pattern instrument. This operation may take several minutes to complete. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | UnloadAllPatterns | Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. |
|  | UnloadSpecifications(IEnumerableString) | Unloads the given specifications sheets present in the previously loaded specifications files that you select. |
|  | UnloadSpecifications(String) | Unloads the given specifications sheet present in the previously loaded specifications file that you select. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/b479ecd9-9626-a053-abe3-af6556df5732.htm language=enus -->
## TOPIC 00123: ninetdigitalfx40ref/html/b479ecd9-9626-a053-abe3-af6556df5732.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/b479ecd9-9626-a053-abe3-af6556df5732.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/b479ecd9-9626-a053-abe3-af6556df5732.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalHistoryRam.NumberOfSamplesIsFinite Property

DigitalHistoryRamNumberOfSamplesIsFinite Property

Gets or sets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public bool NumberOfSamplesIsFinite { get; set; }
```

```text
Public Property NumberOfSamplesIsFinite As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The underlying NI-Digital driver returned an error. |
| ObjectDisposedException | NumberOfSamplesIsFinite was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

##### See Also

###### Reference

DigitalHistoryRam Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/b5df7652-7832-8d52-637b-dd970bd79213.htm language=enus -->
## TOPIC 00124: ninetdigitalfx40ref/html/b5df7652-7832-8d52-637b-dd970bd79213.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/b5df7652-7832-8d52-637b-dd970bd79213.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/b5df7652-7832-8d52-637b-dd970bd79213.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevels Methods

DigitalLevels Methods

The [DigitalLevels](c8702f19-4028-4f17-645c-972206828b0e.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureActiveLoadLevels | Configures the Ioh, Iol, and Vcom values. |
|  | ConfigureVoltageLevels | Configures the high and low logic levels for voltage as well as the termination mode input voltage. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalLevels Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/cd3d191c-4eeb-6c09-3038-5641ac3c4081.htm language=enus -->
## TOPIC 00125: ninetdigitalfx40ref/html/cd3d191c-4eeb-6c09-3038-5641ac3c4081.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/cd3d191c-4eeb-6c09-3038-5641ac3c4081.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/cd3d191c-4eeb-6c09-3038-5641ac3c4081.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverIdentity.SpecificationMajorVersion Property

DigitalDriverIdentitySpecificationMajorVersion Property

NationalInstruments.ModularInstruments.NIDigital

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public int SpecificationMajorVersion { get; }
```

```text
Public ReadOnly Property SpecificationMajorVersion As Integer
	Get
```

###### Property Value

Int32

NationalInstruments.ModularInstruments.NIDigital

NationalInstruments.ModularInstruments.NIDigital

###### Implements

##### See Also

###### Reference

DigitalDriverIdentity Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/cd3e7539-8614-cccc-d3c0-dd775a1a49a7.htm language=enus -->
## TOPIC 00126: ninetdigitalfx40ref/html/cd3e7539-8614-cccc-d3c0-dd775a1a49a7.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/cd3e7539-8614-cccc-d3c0-dd775a1a49a7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/cd3e7539-8614-cccc-d3c0-dd775a1a49a7.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalStartTrigger Class

DigitalStartTrigger Class

Provides configuration and controls for start triggers that affect how the pattern burst begins.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public class DigitalStartTrigger : DigitalSubObject
```

```text
Public Class DigitalStartTrigger
	Inherits DigitalSubObject
```

The DigitalStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdge | Gets the DigitalEdgeStartTrigger object used to configure and control the start trigger as a digital edge start trigger. |
|  | OutputTerminal | Gets or sets the destination terminal for exporting the start trigger. |
|  | Software | Gets the DigitalSoftwareStartTrigger object used to configure and control the start trigger as a software start trigger. |
|  | TerminalName | Gets a string containing the terminal name of the DigitalStartTrigger. |
|  | TriggerType | Gets or sets the trigger type of the DigitalStartTrigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Disable | Disables a previously configured start trigger and sets TriggerType to None. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/d06a0ffb-15a9-3dee-fbdd-bf9095cf5a16.htm language=enus -->
## TOPIC 00127: ninetdigitalfx40ref/html/d06a0ffb-15a9-3dee-fbdd-bf9095cf5a16.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/d06a0ffb-15a9-3dee-fbdd-bf9095cf5a16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/d06a0ffb-15a9-3dee-fbdd-bf9095cf5a16.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTiming Methods

DigitalTiming Methods

The [DigitalTiming](59758f52-d870-95b5-4807-e1cac3274a63.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateTimeSet | Creates and returns a DigitalTimeSet. Use this method to create time set values after applying a timing sheet with ApplyLevelsAndTiming(String, String, String), or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to ApplyLevelsAndTiming(String, String, String), it only affects the values of the current timing context. |
|  | DeleteAllTimeSets | Deletes all loaded and created time sets. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetTimeSet | Returns a DigitalTimeSet specified by a name. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalTiming Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/d979393b-f86c-a836-4583-38919c3c06e3.htm language=enus -->
## TOPIC 00128: ninetdigitalfx40ref/html/d979393b-f86c-a836-4583-38919c3c06e3.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/d979393b-f86c-a836-4583-38919c3c06e3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/d979393b-f86c-a836-4583-38919c3c06e3.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternControl.BurstPattern Method (String, String, Boolean, TimeSpan)

DigitalPatternControlBurstPattern Method (String, String, Boolean, TimeSpan)

Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for each site.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public bool[] BurstPattern(
	string siteList,
	string startLabel,
	bool selectDigitalFunction,
	TimeSpan maxTime
)
```

```text
Public Function BurstPattern ( 
	siteList As String,
	startLabel As String,
	selectDigitalFunction As Boolean,
	maxTime As TimeSpan
) As Boolean()
```

###### Parameters

- **siteList**
  - Type: SystemString The sites on which to burst the pattern as a comma-delimited list of strings of the form siteN, where N is the site number. If you specify an empty string, the pattern is burst on all sites.
- **startLabel**
  - Type: SystemString The pattern name or exported pattern label from which to start bursting the pattern.
- **selectDigitalFunction**
  - Type: SystemBooleanIf , sets the SelectedFunction of the pins to Digital.
- **maxTime**
  - Type: SystemTimeSpan The maximum time interval allowed for the pattern burst to complete.

###### Return Value

Boolean

Boolean

GetSiteResultsSiteNumbers(String, SiteResultType)

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| InvalidOperationException | BurstPattern(String, String, Boolean, TimeSpan) is called without loading a pattern. |
| SelectorNameException | The value for siteList contains an invalid site. |
| MaxTimeExceededException | The pattern burst took longer than the specified maxTime. |
| ArgumentException | One or more of the configured properties of the underlying NI-Digital Pattern Driver were invalid. |

##### Remarks

Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to [WriteStatic(PinState)](012c5b74-388b-be8a-bd0d-6ecf41db64ca.htm), or a call to [ApplyLevelsAndTiming(String, String, String)](7bccea89-d7e3-5624-265d-1f5dbbe49dce.htm).

This overload will burst the pattern to completion and then return the site pass/fail results. Call this overload when you want to wait until the pattern burst is complete before continuing program execution.

For more information, refer to the [Session State Model](/csh?topicname=digipat/programming-states.html) topic of the Digital Pattern Help.

##### See Also

###### Reference

DigitalPatternControl Class

BurstPattern Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/d9cba6fc-3595-2e0d-1830-3222b7e02ede.htm language=enus -->
## TOPIC 00129: ninetdigitalfx40ref/html/d9cba6fc-3595-2e0d-1830-3222b7e02ede.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/d9cba6fc-3595-2e0d-1830-3222b7e02ede.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/d9cba6fc-3595-2e0d-1830-3222b7e02ede.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPpmu Class

DigitalPpmu Class

Configures current and voltage levels that the PPMU outputs to or measures from the DUT.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public sealed class DigitalPpmu : DigitalSubObject
```

```text
Public NotInheritable Class DigitalPpmu
	Inherits DigitalSubObject
```

The DigitalPpmu type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowExtendedVoltageRange | Gets or sets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
|  | ApertureTime | Gets the measurement aperture time for the PPMU. |
|  | ApertureTimeUnits | Gets the units of the measurement aperture time. |
|  | DCCurrent | Gets the DigitalSourceDCCurrent object containing the configuration for a PPMU for which the OutputFunction is DCCurrent. |
|  | DCVoltage | Gets the DigitalSourceDCVoltage object containing the configuration for a PPMU for which the OutputFunction is DCVoltage. |
|  | OutputFunction | Gets or sets whether the PPMU sources DC voltage or DC current. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureApertureTime | Sets the aperture time for the PPMU measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Measure | Instructs the PPMU to measure voltage or current. You can call this method to take a voltage measurement even if SelectedFunction is not set to Ppmu. |
|  | Source | Starts the sourcing voltage or current from the PPMU. This method automatically selects the Ppmu function. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

Refer to [Pin Parametric Measurement Unit (PPMU)](/csh?topicname=digipat6570/ppmu-overview.html)
 for more information on using the PPMU.

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-Digital\\Examples\\DotNET 4.x directory or in the Start menu at National InstrumentsNI Digital Pattern Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/da669431-5c87-d3d2-e679-f1ead52b03c1.htm language=enus -->
## TOPIC 00130: ninetdigitalfx40ref/html/da669431-5c87-d3d2-e679-f1ead52b03c1.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/da669431-5c87-d3d2-e679-f1ead52b03c1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/da669431-5c87-d3d2-e679-f1ead52b03c1.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceWaveforms.CreateSerial Method (String, String, SourceDataMapping, UInt32, BitOrder)

DigitalSourceWaveformsCreateSerial Method (String, String, SourceDataMapping, UInt32, BitOrder)

Creates the source waveform settings used to source serial waveforms using a comma-delimited string of pins or channels.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void CreateSerial(
	string pinSetString,
	string waveformName,
	SourceDataMapping dataMapping,
	uint sampleWidth,
	BitOrder bitOrder
)
```

```text
Public Sub CreateSerial ( 
	pinSetString As String,
	waveformName As String,
	dataMapping As SourceDataMapping,
	sampleWidth As UInteger,
	bitOrder As BitOrder
)
```

###### Parameters

- **pinSetString**
  - Type: SystemString The set of pins or channels for which to create the waveform. The pins or channels represented by the pinSetString must match the source pins in the pattern that references the waveform. The pin order in the pin set string determines the bit positions of the data written using one of the write waveform methods on the DigitalSourceWaveforms object.
- **waveformName**
  - Type: SystemString The name of the waveform to use in the pattern file. Waveform names must be unique. Use the waveformName with source_start opcode in your pattern.
- **dataMapping**
  - Type: NationalInstruments.ModularInstruments.NIDigitalSourceDataMapping Specifies whether the the waveform is broadcast to all sites or a unique waveform is sourced per site.
- **sampleWidth**
  - Type: SystemUInt32 The width in bits of each serial sample. Valid values are between 1 and 32.
- **bitOrder**
  - Type: NationalInstruments.ModularInstruments.NIDigitalBitOrder The bit order significance. This can be most significant bit first or least significant bit first. MostSignificantBitFirst is the default value.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| ArgumentException | The value for waveformName is an empty string or contains an invalid character.The value for dataMapping is invalid.The value for sampleWidth is invalid.The value for bitOrder is invalid.The number of waveforms in source memory exceeds maximum number of waveforms allowed. |

##### Remarks

You cannot reconfigure settings after waveforms are created.

Opcodes

Source Waveform Configurations

##### See Also

###### Reference

DigitalSourceWaveforms Class

CreateSerial Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/db753b13-d061-c3af-5ab8-bff633c92954.htm language=enus -->
## TOPIC 00131: ninetdigitalfx40ref/html/db753b13-d061-c3af-5ab8-bff633c92954.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/db753b13-d061-c3af-5ab8-bff633c92954.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/db753b13-d061-c3af-5ab8-bff633c92954.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPinInformation.PinName Property

DigitalPinInformationPinName Property

Gets the pin name.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string PinName { get; }
```

```text
Public ReadOnly Property PinName As String
	Get
```

###### Property Value

String

##### See Also

###### Reference

DigitalPinInformation Structure

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/db9aa4c0-5dfa-d87a-c951-55fb6c612d3c.htm language=enus -->
## TOPIC 00132: ninetdigitalfx40ref/html/db9aa4c0-5dfa-d87a-c951-55fb6c612d3c.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/db9aa4c0-5dfa-d87a-c951-55fb6c612d3c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/db9aa4c0-5dfa-d87a-c951-55fb6c612d3c.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.ResetAttribute Method (String, Int32)

DigitalDriverUtilityResetAttribute Method (String, Int32)

Resets a driver attribute to its default state using a string to specify pins, pin groups, or channels.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ResetAttribute(
	string pinSetString,
	int attributeId
)
```

```text
Public Sub ResetAttribute ( 
	pinSetString As String,
	attributeId As Integer
)
```

###### Parameters

- **pinSetString**
  - Type: SystemStringThe pin set string representing the pins, pin groups, or channels to reset the attribute for.
- **attributeId**
  - Type: SystemInt32The attribute to reset.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| OperationNotSupportedException | The value for attributeId is not a valid attribute identifier. |

##### See Also

###### Reference

DigitalDriverUtility Class

ResetAttribute Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/dc07dce3-17ff-855e-a9c0-253130493e38.htm language=enus -->
## TOPIC 00133: ninetdigitalfx40ref/html/dc07dce3-17ff-855e-a9c0-253130493e38.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/dc07dce3-17ff-855e-a9c0-253130493e38.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/dc07dce3-17ff-855e-a9c0-253130493e38.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.Name Property

DigitalTimeSetName Property

Gets the name of the time set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string Name { get; }
```

```text
Public ReadOnly Property Name As String
	Get
```

###### Property Value

String

DigitalTimeSet

GetTimeSet(String)

Timing

NIDigital

##### See Also

###### Reference

DigitalTimeSet Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/ddcd2dea-c17d-8ff6-e571-c8bce8a1d5fe.htm language=enus -->
## TOPIC 00134: ninetdigitalfx40ref/html/ddcd2dea-c17d-8ff6-e571-c8bce8a1d5fe.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/ddcd2dea-c17d-8ff6-e571-c8bce8a1d5fe.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/ddcd2dea-c17d-8ff6-e571-c8bce8a1d5fe.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPpmu Properties

DigitalPpmu Properties

The [DigitalPpmu](d9cba6fc-3595-2e0d-1830-3222b7e02ede.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowExtendedVoltageRange | Gets or sets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
|  | ApertureTime | Gets the measurement aperture time for the PPMU. |
|  | ApertureTimeUnits | Gets the units of the measurement aperture time. |
|  | DCCurrent | Gets the DigitalSourceDCCurrent object containing the configuration for a PPMU for which the OutputFunction is DCCurrent. |
|  | DCVoltage | Gets the DigitalSourceDCVoltage object containing the configuration for a PPMU for which the OutputFunction is DCVoltage. |
|  | OutputFunction | Gets or sets whether the PPMU sources DC voltage or DC current. |

Top

##### See Also

###### Reference

DigitalPpmu Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/de39c4bb-6a95-8a98-42e2-ec67162344e9.htm language=enus -->
## TOPIC 00135: ninetdigitalfx40ref/html/de39c4bb-6a95-8a98-42e2-ec67162344e9.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/de39c4bb-6a95-8a98-42e2-ec67162344e9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/de39c4bb-6a95-8a98-42e2-ec67162344e9.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeConditionalJumpTrigger.Source Property

DigitalEdgeConditionalJumpTriggerSource Property

Gets or sets the source terminal for the Conditional Jump Trigger.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string Source { get; set; }
```

```text
Public Property Source As String
	Get
	Set
```

###### Property Value

String

The source terminal for the Conditional Jump Trigger. This property is used when [TriggerType](7bdc5aa4-8b80-1b20-d6f5-15c12915cc44.htm) is set to
 [DigitalEdge](2d52a4c4-a149-d68c-3ce9-8c8e00fda490.htm). The default value is "".

##### See Also

###### Reference

DigitalEdgeConditionalJumpTrigger Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/e64d6980-c336-ef54-3411-17d0d38c761f.htm language=enus -->
## TOPIC 00136: ninetdigitalfx40ref/html/e64d6980-c336-ef54-3411-17d0d38c761f.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/e64d6980-c336-ef54-3411-17d0d38c761f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/e64d6980-c336-ef54-3411-17d0d38c761f.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

HistoryRamCycle Enumeration

HistoryRamCycle Enumeration

Specifies the History RAM cycles.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public enum HistoryRamCycle
```

```text
Public Enumeration HistoryRamCycle
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Failed | 2303 | Acquires failed cycles. |
|  | All | 2304 | Acquires all cycles. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/ea87e073-ec45-228b-3a5e-daf05398d241.htm language=enus -->
## TOPIC 00137: ninetdigitalfx40ref/html/ea87e073-ec45-228b-3a5e-daf05398d241.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/ea87e073-ec45-228b-3a5e-daf05398d241.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/ea87e073-ec45-228b-3a5e-daf05398d241.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSourceWaveforms Methods

DigitalSourceWaveforms Methods

The [DigitalSourceWaveforms](f1a5b57d-2d18-7548-2273-d75ab65ddbfb.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateFromFile | Creates the source waveform settings used to source waveforms with configuration information contained in a .tdms file. |
|  | CreateParallel(String, String, SourceDataMapping) | Creates source waveform settings used to source parallel data using a comma-delimited string of pins or channels. |
|  | CreateParallel(DigitalPinSet, String, SourceDataMapping) | Creates source waveform settings used to source parallel data using a specified DigitalPinSet. |
|  | CreateSerial(String, String, SourceDataMapping, UInt32, BitOrder) | Creates the source waveform settings used to source serial waveforms using a comma-delimited string of pins or channels. |
|  | CreateSerial(DigitalPinSet, String, SourceDataMapping, UInt32, BitOrder) | Creates the source waveform settings used to source serial waveforms using a specified DigitalPinSet. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WriteBroadcast | Writes the same source waveform data to all sites. |
|  | WriteFromFile | Writes a source waveform based on the waveform data and the configuration information the file contains. |
|  | WriteSiteUnique | Writes one source waveform to each of the specified sites. |

Top

##### See Also

###### Reference

DigitalSourceWaveforms Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/eae16387-c4ae-bd37-ce81-30241b155bb5.htm language=enus -->
## TOPIC 00138: ninetdigitalfx40ref/html/eae16387-c4ae-bd37-ce81-30241b155bb5.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/eae16387-c4ae-bd37-ce81-30241b155bb5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/eae16387-c4ae-bd37-ce81-30241b155bb5.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalTimeSet.ConfigureCompareEdgesStrobe Method (DigitalPinSet, PrecisionTimeSpan, PrecisionTimeSpan)

DigitalTimeSetConfigureCompareEdgesStrobe Method (DigitalPinSet, PrecisionTimeSpan, PrecisionTimeSpan)

Configures the strobe edge times for the specified pin set.

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureCompareEdgesStrobe(
	DigitalPinSet pinSet,
	PrecisionTimeSpan compareEdge,
	PrecisionTimeSpan compare2Edge
)
```

```text
Public Sub ConfigureCompareEdgesStrobe ( 
	pinSet As DigitalPinSet,
	compareEdge As PrecisionTimeSpan,
	compare2Edge As PrecisionTimeSpan
)
```

###### Parameters

- **pinSet**
  - Type: NationalInstruments.ModularInstruments.NIDigitalDigitalPinSet The pin set for which to configure the strobe edge time.
- **compareEdge**
  - Type: Ivi.DriverPrecisionTimeSpan The time within a vector period when the comparison happens.
- **compare2Edge**
  - Type: Ivi.DriverPrecisionTimeSpan The time when the comparison happens for the second DUT cycle within a vector period.

##### Exceptions

| Exception | Condition |
| --- | --- |
| IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

##### See Also

###### Reference

DigitalTimeSet Class

ConfigureCompareEdgesStrobe Overload

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-digital-pattern-dot-net-api-ref path=ninetdigitalfx40ref/html/ebcb8fee-9cfe-6a0f-ee7d-f3d0cc5b70a3.htm language=enus -->
## TOPIC 00139: ninetdigitalfx40ref/html/ebcb8fee-9cfe-6a0f-ee7d-f3d0cc5b70a3.htm

- bundle_id: `ni-digital-pattern-dot-net-api-ref`
- source_path: `ninetdigitalfx40ref/html/ebcb8fee-9cfe-6a0f-ee7d-f3d0cc5b70a3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-dot-net-api-ref/raw/resource/enus/ninetdigitalfx40ref/html/ebcb8fee-9cfe-6a0f-ee7d-f3d0cc5b70a3.htm
- document_id: `ni-digital-pattern-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalDriverUtility.GetChannelName Method

DigitalDriverUtilityGetChannelName Method

Int32

Namespace:

NationalInstruments.ModularInstruments.NIDigital

Assembly:

##### Syntax

C#

VB

```text
public string GetChannelName(
	int index
)
```

```text
Public Function GetChannelName ( 
	index As Integer
) As String
```

###### Parameters

- **index**
  - Type: SystemInt32 One-based index for the desired channel in the session. Valid values are from 1 to the number of channels in the session

###### Return Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The GetChannelName(Int32) method was called after the associated NIDigital or DigitalDriverUtility object was disposed. |
| ArgumentException | The indicated index is out of range (less than one or greater than the number of channels in the session) |

##### See Also

###### Reference

DigitalDriverUtility Class

NationalInstruments.ModularInstruments.NIDigital Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
