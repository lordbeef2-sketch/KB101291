# NI DOCUMENT BUNDLE: rfmx-instr-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-instr-dotnet start=1 end=181 -->
<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/03486df7-30eb-ae6e-5270-5e48c7a749d6.htm language=enus -->
## TOPIC 00001: rfmxinstrdotnet/html/03486df7-30eb-ae6e-5270-5e48c7a749d6.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/03486df7-30eb-ae6e-5270-5e48c7a749d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/03486df7-30eb-ae6e-5270-5e48c7a749d6.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFrequencyReferenceFrequency Method

RFmxInstrMXGetFrequencyReferenceFrequency Method

Gets the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyReferenceFrequency(
	string channelName,
	out double value
)
```

```text
Public Function GetFrequencyReferenceFrequency ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

FrequencyReferenceFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/03c0094d-9c2e-ae6a-444a-6169478cd848.htm language=enus -->
## TOPIC 00002: rfmxinstrdotnet/html/03c0094d-9c2e-ae6a-444a-6169478cd848.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/03c0094d-9c2e-ae6a-444a-6169478cd848.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/03c0094d-9c2e-ae6a-444a-6169478cd848.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetFftWidth Method

RFmxInstrMXSetFftWidth Method

Sets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftWidth(
	string channelName,
	double value
)
```

```text
Public Function SetFftWidth ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

###### Return Value

Int32

##### Remarks

FftWidth

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/04da3154-0881-ec4e-154f-a261144e8de3.htm language=enus -->
## TOPIC 00003: rfmxinstrdotnet/html/04da3154-0881-ec4e-154f-a261144e8de3.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/04da3154-0881-ec4e-154f-a261144e8de3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/04da3154-0881-ec4e-154f-a261144e8de3.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetReadyForReferenceEventOutputTerminal Method

RFmxInstrMXSetReadyForReferenceEventOutputTerminal Method

Sets the destination terminal for the Ready for Reference event.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReadyForReferenceEventOutputTerminal(
	string selectorString,
	string value
)
```

```text
Public Function SetReadyForReferenceEventOutputTerminal ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Specifies the destination terminal for the Ready for Reference event.

###### Return Value

Int32

##### Remarks

ReadyForReferenceEventOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/04db90d1-a729-2055-f057-d4b962e8597c.htm language=enus -->
## TOPIC 00004: rfmxinstrdotnet/html/04db90d1-a729-2055-f057-d4b962e8597c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/04db90d1-a729-2055-f057-d4b962e8597c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/04db90d1-a729-2055-f057-d4b962e8597c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxException(SerializationInfo, StreamingContext) Constructor

RFmxException(SerializationInfo, StreamingContext) Constructor

RFmxException

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
protected RFmxException(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Protected Sub New ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info SerializationInfo**
  - Specifies the SerializationInfo that holds the serialized object data about the exception being thrown.
- **context StreamingContext**
  - Specifies the StreamingContext that contains contextual information about the source or destination.

##### See Also

###### Reference

RFmxException Class

RFmxException Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/0548f60a-d580-733c-5f31-0b7e8bd6eae0.htm language=enus -->
## TOPIC 00005: rfmxinstrdotnet/html/0548f60a-d580-733c-5f31-0b7e8bd6eae0.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/0548f60a-d580-733c-5f31-0b7e8bd6eae0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/0548f60a-d580-733c-5f31-0b7e8bd6eae0.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.BuildPortString2 Method

RFmxInstrMXBuildPortString2 Method

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildPortString2(
	string selectorString,
	string portName,
	string deviceName,
	int channelNumber
)
```

```text
Public Shared Function BuildPortString2 ( 
	selectorString As String,
	portName As String,
	deviceName As String,
	channelNumber As Integer
) As String
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane string when used for building port string for the external attenuation table methods. If you do not specify the calibration plane string, the default calibration plane instance is used. Example:"""calplane::plane0"
- **portName String**
  - Specifies the port for building the selector string.
- **deviceName String**
  - specifies the name of the initialized device for building the selector string.
- **channelNumber Int32**
  - specifies the channel for building the selector string. Specify 0 as the value for this parameter.

###### Return Value

String

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/06d35ebb-ac45-3cb9-ada5-4146814e40e1.htm language=enus -->
## TOPIC 00006: rfmxinstrdotnet/html/06d35ebb-ac45-3cb9-ada5-4146814e40e1.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/06d35ebb-ac45-3cb9-ada5-4146814e40e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/06d35ebb-ac45-3cb9-ada5-4146814e40e1.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxException Constructor

RFmxException Constructor

RFmxException

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxException()
```

```text
Public Sub New
```

##### See Also

###### Reference

RFmxException Class

RFmxException Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/06e348ca-dab9-ade7-b584-09ce18d6f3db.htm language=enus -->
## TOPIC 00007: rfmxinstrdotnet/html/06e348ca-dab9-ade7-b584-09ce18d6f3db.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/06e348ca-dab9-ade7-b584-09ce18d6f3db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/06e348ca-dab9-ade7-b584-09ce18d6f3db.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeDoubleArray Method

RFmxInstrMXGetAttributeDoubleArray Method

Gets the value of a double array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeDoubleArray(
	string channelName,
	int attributeIdentifier,
	ref double[] value
)
```

```text
Public Function GetAttributeDoubleArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Double**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/0b613de9-3618-bf4d-ef0c-e13c90968101.htm language=enus -->
## TOPIC 00008: rfmxinstrdotnet/html/0b613de9-3618-bf4d-ef0c-e13c90968101.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/0b613de9-3618-bf4d-ef0c-e13c90968101.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/0b613de9-3618-bf4d-ef0c-e13c90968101.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeComplexDoubleArray Method

RFmxInstrMXGetAttributeComplexDoubleArray Method

Gets the value of a ComplexDouble array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeComplexDoubleArray(
	string channelName,
	int attributeIdentifier,
	ref ComplexDouble[] value
)
```

```text
Public Function GetAttributeComplexDoubleArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As ComplexDouble()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value ComplexDouble**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/0c2bb091-4ba7-0b96-0223-5c7a3fe0eb16.htm language=enus -->
## TOPIC 00009: rfmxinstrdotnet/html/0c2bb091-4ba7-0b96-0223-5c7a3fe0eb16.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/0c2bb091-4ba7-0b96-0223-5c7a3fe0eb16.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/0c2bb091-4ba7-0b96-0223-5c7a3fe0eb16.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SelectActiveExternalAttenuationTable Method

RFmxInstrMXSelectActiveExternalAttenuationTable Method

tableName

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SelectActiveExternalAttenuationTable(
	string selectorString,
	string tableName
)
```

```text
Public Function SelectActiveExternalAttenuationTable ( 
	selectorString As String,
	tableName As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which either the S-parameter table or the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session, the default "" (empty string) selects the active external attenuation table for all the MIMO Ports. To configure external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0"
- **tableName String**
  - Specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/0c303c74-900d-3c61-bf48-e9f73dd41636.htm language=enus -->
## TOPIC 00010: rfmxinstrdotnet/html/0c303c74-900d-3c61-bf48-e9f73dd41636.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/0c303c74-900d-3c61-bf48-e9f73dd41636.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/0c303c74-900d-3c61-bf48-e9f73dd41636.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetCleanerSpectrum Method

RFmxInstrMXGetCleanerSpectrum Method

Gets how to obtain the lowest noise floor or faster measurement speed.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCleanerSpectrum(
	string channelName,
	out RFmxInstrMXCleanerSpectrum value
)
```

```text
Public Function GetCleanerSpectrum ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXCleanerSpectrum
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXCleanerSpectrum**
  - Upon return, contains how to obtain the lowest noise floor or faster measurement speed.

###### Return Value

Int32

##### Remarks

CleanerSpectrum

Disabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/0d2ecff4-f73e-f6a5-a8b3-65e38fe07825.htm language=enus -->
## TOPIC 00011: rfmxinstrdotnet/html/0d2ecff4-f73e-f6a5-a8b3-65e38fe07825.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/0d2ecff4-f73e-f6a5-a8b3-65e38fe07825.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/0d2ecff4-f73e-f6a5-a8b3-65e38fe07825.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeLongArray Method

RFmxInstrMXGetAttributeLongArray Method

Gets the value of a long array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeLongArray(
	string channelName,
	int attributeIdentifier,
	ref long[] value
)
```

```text
Public Function GetAttributeLongArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As Long()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int64**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/0ef5664a-895f-1192-4446-43a1b04d4e6c.htm language=enus -->
## TOPIC 00012: rfmxinstrdotnet/html/0ef5664a-895f-1192-4446-43a1b04d4e6c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/0ef5664a-895f-1192-4446-43a1b04d4e6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/0ef5664a-895f-1192-4446-43a1b04d4e6c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetInstrumentFirmwareRevision Method

RFmxInstrMXGetInstrumentFirmwareRevision Method

Gets a string containing the firmware revision information of the RF downconverter for the composite device you are currently using.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetInstrumentFirmwareRevision(
	string channelName,
	out string value
)
```

```text
Public Function GetInstrumentFirmwareRevision ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value String**
  - Upon return, contains a string containing the firmware revision information of the RF downconverter for the composite device you are currently using.

###### Return Value

Int32

##### Remarks

InstrumentFirmwareRevision

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/116527bd-dd86-2672-6bcf-fa4817ea8c52.htm language=enus -->
## TOPIC 00013: rfmxinstrdotnet/html/116527bd-dd86-2672-6bcf-fa4817ea8c52.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/116527bd-dd86-2672-6bcf-fa4817ea8c52.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/116527bd-dd86-2672-6bcf-fa4817ea8c52.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRFPreampPresent Method

RFmxInstrMXGetRFPreampPresent Method

Indicates whether an RF preamplifier is available on the RF downconverter module.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRFPreampPresent(
	string channelName,
	out bool value
)
```

```text
Public Function GetRFPreampPresent ( 
	channelName As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value Boolean**
  - Indicates whether an RF preamplifier is available on the RF downconverter module.

###### Return Value

Int32

##### Remarks

RFPreampPresent

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/11e56ad4-cecb-92fc-8803-416163163723.htm language=enus -->
## TOPIC 00014: rfmxinstrdotnet/html/11e56ad4-cecb-92fc-8803-416163163723.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/11e56ad4-cecb-92fc-8803-416163163723.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/11e56ad4-cecb-92fc-8803-416163163723.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.LOSourceOnboard Field

RFmxInstrMXConstantsLOSourceOnboard Field

PXIe-5831: This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage.

PXIe-5832: This configuration uses the onboard LO of the PXIe-3623, using the LO2 stage.

PXIe-5831 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.

PXIe-5832 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3623.

PXIe-5840 with PXIe-5653: If the center frequency is greater than or equal to 3.2 GHz, this configuration uses the PXIe-5653 LO source. For frequencies less than 3.2 GHz, this configuration uses the PXIe-5840 internal LO. If RFmx is operating in Spectrum mode, this configuration uses the PXIe-5840 internal LO irrespective of the frequency.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string LOSourceOnboard = "Onboard"
```

```text
Public Const LOSourceOnboard As String = "Onboard"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm language=enus -->
## TOPIC 00015: rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXRecommendedSpectralFftWindow Enumeration

RFmxInstrMXRecommendedSpectralFftWindow Enumeration

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXRecommendedSpectralFftWindow
```

```text
Public Enumeration RFmxInstrMXRecommendedSpectralFftWindow
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | Indicates that the measurement does not use FFT windowing to reduce spectral leakage. |
| FlatTop | 1 | Indicates a Flat Top FFT window type. |
| Hanning | 2 | Indicates a Hanning FFT window type. |
| Hamming | 3 | Indicates a Hamming FFT window type. |
| Gaussian | 4 | Indicates a Gaussian FFT window type. |
| Blackman | 5 | Indicates a Blackman FFT window type. |
| BlackmanHarris | 6 | Indicates a Blackman-Harris FFT window type. |
| KaiserBessel | 7 | Indicates a Kaiser-Bessel FFT window type. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm language=enus -->
## TOPIC 00016: rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeShort Method

RFmxInstrMXSetAttributeShort Method

Sets the value of a Short attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeShort(
	string channelName,
	int attributeIdentifier,
	short value
)
```

```text
Public Function SetAttributeShort ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Short
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int16**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm language=enus -->
## TOPIC 00017: rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetCommonModeLevel Method

RFmxInstrMXGetCommonModeLevel Method

Gets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCommonModeLevel(
	string channelName,
	out double value
)
```

```text
Public Function GetCommonModeLevel ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

###### Return Value

Int32

##### Remarks

CommonModeLevel

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm language=enus -->
## TOPIC 00018: rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.IsDisposed Property

RFmxInstrMXIsDisposed Property

Gets a value that indicates whether the signal has been disposed.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public bool IsDisposed { get; }
```

```text
Public ReadOnly Property IsDisposed As Boolean
	Get
```

###### Property Value

Boolean

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/18131141-6279-499d-60b6-6c38b4fc7cf8.htm language=enus -->
## TOPIC 00019: rfmxinstrdotnet/html/18131141-6279-499d-60b6-6c38b4fc7cf8.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/18131141-6279-499d-60b6-6c38b4fc7cf8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/18131141-6279-499d-60b6-6c38b4fc7cf8.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRFHighpassFilterFrequency Method

RFmxInstrMXGetRFHighpassFilterFrequency Method

Gets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRFHighpassFilterFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetRFHighpassFilterFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition.

###### Return Value

Int32

##### Remarks

RFHighpassFilterFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/1a20a249-279c-307e-2eae-b06bc9470b13.htm language=enus -->
## TOPIC 00020: rfmxinstrdotnet/html/1a20a249-279c-307e-2eae-b06bc9470b13.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/1a20a249-279c-307e-2eae-b06bc9470b13.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/1a20a249-279c-307e-2eae-b06bc9470b13.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetDoneEventTerminalName Method

RFmxInstrMXGetDoneEventTerminalName Method

Gets the fully qualified signal name as a string.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDoneEventTerminalName(
	string selectorString,
	out string value
)
```

```text
Public Function GetDoneEventTerminalName ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the fully qualified signal name as a string.

###### Return Value

Int32

##### Remarks

DoneEventTerminalName

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/1b91177f-c9fb-cf80-1493-01e031255ddf.htm language=enus -->
## TOPIC 00021: rfmxinstrdotnet/html/1b91177f-c9fb-cf80-1493-01e031255ddf.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/1b91177f-c9fb-cf80-1493-01e031255ddf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/1b91177f-c9fb-cf80-1493-01e031255ddf.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetLOExportEnabled Method

RFmxInstrMXGetLOExportEnabled Method

Gets whether to enable the LO OUT terminals on the installed devices.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLOExportEnabled(
	string channelName,
	out bool value
)
```

```text
Public Function GetLOExportEnabled ( 
	channelName As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the losource number and port number. Example: "port0" or "port0/ losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value Boolean**
  - Upon return, contains whether to enable the LO OUT terminals on the installed devices.

###### Return Value

Int32

##### Remarks

LOExportEnabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/22393ab3-455f-daca-5352-a9fdcfcb14d7.htm language=enus -->
## TOPIC 00022: rfmxinstrdotnet/html/22393ab3-455f-daca-5352-a9fdcfcb14d7.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/22393ab3-455f-daca-5352-a9fdcfcb14d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/22393ab3-455f-daca-5352-a9fdcfcb14d7.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetNumberOfLOSharingGroups Method

RFmxInstrMXGetNumberOfLOSharingGroups Method

Gets the RFmx session with the number of LO sharing groups.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfLOSharingGroups(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfLOSharingGroups ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Int32**
  - Upon return, contains the RFmx session with the number of LO sharing groups.

###### Return Value

Int32

##### Remarks

NumberOfLOSharingGroups

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/22dcfdc9-8608-9483-92a2-9fe7e9e46fe4.htm language=enus -->
## TOPIC 00023: rfmxinstrdotnet/html/22dcfdc9-8608-9483-92a2-9fe7e9e46fe4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/22dcfdc9-8608-9483-92a2-9fe7e9e46fe4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/22dcfdc9-8608-9483-92a2-9fe7e9e46fe4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAdvanceTriggerDigitalEdgeSource Method

RFmxInstrMXGetAdvanceTriggerDigitalEdgeSource Method

Gets the source terminal for the advance trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAdvanceTriggerDigitalEdgeSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetAdvanceTriggerDigitalEdgeSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the source terminal for the advance trigger.

###### Return Value

Int32

##### Remarks

AdvanceTriggerDigitalEdgeSource

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/234aef0f-53e9-fea4-84de-484feded69f4.htm language=enus -->
## TOPIC 00024: rfmxinstrdotnet/html/234aef0f-53e9-fea4-84de-484feded69f4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/234aef0f-53e9-fea4-84de-484feded69f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/234aef0f-53e9-fea4-84de-484feded69f4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXDigitizerDitherEnabled Enumeration

RFmxInstrMXDigitizerDitherEnabled Enumeration

Specifies whether dithering is enabled on the digitizer.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXDigitizerDitherEnabled
```

```text
Public Enumeration RFmxInstrMXDigitizerDitherEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the method. |
| Enabled | 1 | Enables the method. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/24e417c2-6e5d-09c2-4ea7-3555885717ac.htm language=enus -->
## TOPIC 00025: rfmxinstrdotnet/html/24e417c2-6e5d-09c2-4ea7-3555885717ac.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/24e417c2-6e5d-09c2-4ea7-3555885717ac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/24e417c2-6e5d-09c2-4ea7-3555885717ac.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.DeleteExternalAttenuationTable Method

RFmxInstrMXDeleteExternalAttenuationTable Method

tableName

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int DeleteExternalAttenuationTable(
	string selectorString,
	string tableName
)
```

```text
Public Function DeleteExternalAttenuationTable ( 
	selectorString As String,
	tableName As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session, the default "" (empty string) deletes the active external attenuation table for all the MIMO Ports. To delete an external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0"
- **tableName String**
  - Specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/25ebea27-821b-4ffd-21b9-68f4712990a7.htm language=enus -->
## TOPIC 00026: rfmxinstrdotnet/html/25ebea27-821b-4ffd-21b9-68f4712990a7.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/25ebea27-821b-4ffd-21b9-68f4712990a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/25ebea27-821b-4ffd-21b9-68f4712990a7.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ConfigureExternalAttenuationInterpolationSpline Method

RFmxInstrMXConfigureExternalAttenuationInterpolationSpline Method

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureExternalAttenuationInterpolationSpline(
	string selectorString,
	string tableName
)
```

```text
Public Function ConfigureExternalAttenuationInterpolationSpline ( 
	selectorString As String,
	tableName As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all"
- **tableName String**
  - Specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/25fe339d-eed7-a0ad-85d1-f824fc647924.htm language=enus -->
## TOPIC 00027: rfmxinstrdotnet/html/25fe339d-eed7-a0ad-85d1-f824fc647924.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/25fe339d-eed7-a0ad-85d1-f824fc647924.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/25fe339d-eed7-a0ad-85d1-f824fc647924.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeInt Method

RFmxInstrMXGetAttributeInt Method

Gets the value of an RFmx 32-bit integer (int32) attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeInt(
	string channelName,
	int attributeIdentifier,
	out int value
)
```

```text
Public Function GetAttributeInt ( 
	channelName As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/27616300-139d-ed9c-26cc-ee3fc895b249.htm language=enus -->
## TOPIC 00028: rfmxinstrdotnet/html/27616300-139d-ed9c-26cc-ee3fc895b249.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/27616300-139d-ed9c-26cc-ee3fc895b249.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/27616300-139d-ed9c-26cc-ee3fc895b249.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXStartTriggerType Enumeration

RFmxInstrMXStartTriggerType Enumeration

Specifies whether the start trigger is a digital edge or a software trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXStartTriggerType
```

```text
Public Enumeration RFmxInstrMXStartTriggerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | No start trigger is configured. |
| DigitalEdge | 1 | The start trigger is not asserted until a digital edge is detected. The source of the digital edge is specified by the SetStartTriggerDigitalEdgeSource(String, String) method. |
| Software | 3 | The start trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr_SendSoftwareEdgeTrigger function. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/278a3472-a60a-0c38-d6e9-a47bcc4d5a29.htm language=enus -->
## TOPIC 00029: rfmxinstrdotnet/html/278a3472-a60a-0c38-d6e9-a47bcc4d5a29.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/278a3472-a60a-0c38-d6e9-a47bcc4d5a29.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/278a3472-a60a-0c38-d6e9-a47bcc4d5a29.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX(IntPtr) Constructor

RFmxInstrMX(IntPtr) Constructor

Creates a new RFmx session from an existing RFmx instrument handle.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxInstrMX(
	IntPtr instrumentHandle
)
```

```text
Public Sub New ( 
	instrumentHandle As IntPtr
)
```

###### Parameters

- **instrumentHandle IntPtr**
  - Specifies the pre-existing instrument handle used to create a new RFmx session.

##### Remarks

When you use an existing instrument handle to create a session; calling the Dispose, Close, or ForceClose methods will only dispose the .NET resources associated with this session. The pre-existing instrument handle will NOT be released.

##### See Also

###### Reference

RFmxInstrMX Class

RFmxInstrMX Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/2850d745-c99e-2f81-8cea-1ac1b79a4233.htm language=enus -->
## TOPIC 00030: rfmxinstrdotnet/html/2850d745-c99e-2f81-8cea-1ac1b79a4233.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/2850d745-c99e-2f81-8cea-1ac1b79a4233.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/2850d745-c99e-2f81-8cea-1ac1b79a4233.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiTriggerLine6 Field

RFmxInstrMXConstantsPxiTriggerLine6 Field

The signal is exported to the PXI trigger line 6.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine6 = "PXI_Trig6"
```

```text
Public Const PxiTriggerLine6 As String = "PXI_Trig6"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm language=enus -->
## TOPIC 00031: rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ConfigureSParameterExternalAttenuationTable Method

RFmxInstrMXConfigureSParameterExternalAttenuationTable Method

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSParameterExternalAttenuationTable(
	string selectorString,
	string tableName,
	double[] frequency,
	ComplexDouble[,,] sParameters,
	RFmxInstrMXSParameterOrientation sParameterOrientation
)
```

```text
Public Function ConfigureSParameterExternalAttenuationTable ( 
	selectorString As String,
	tableName As String,
	frequency As Double(),
	sParameters As ComplexDouble(,,),
	sParameterOrientation As RFmxInstrMXSParameterOrientation
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::(calplaneName)/port::(deviceName)/(channelNumber)/(portName)". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all"
- **tableName String**
  - Specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table.
- **frequency Double**
  - Specifies an array of frequencies in the S-parameter table. This value is expressed in Hz.
- **sParameters ComplexDouble**
  - Specifies the S-parameters for each frequency. The first index indicates the corresponding frequency entry, the second index corresponds to the target port for the S-parameter, and the third index corresponds to the the source port. For example, to index the s21 parameter for the fourth frequency in the table, you would use {3, 1, 0} as the indexes since they are zero-based.
- **sParameterOrientation RFmxInstrMXSParameterOrientation**
  - Specifies the orientation of the data in the S-parameter table relative to the port you specify.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/2a53c036-1c38-c962-7041-c8f74cda4007.htm language=enus -->
## TOPIC 00032: rfmxinstrdotnet/html/2a53c036-1c38-c962-7041-c8f74cda4007.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/2a53c036-1c38-c962-7041-c8f74cda4007.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/2a53c036-1c38-c962-7041-c8f74cda4007.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAmplitudeSettling Method

RFmxInstrMXSetAmplitudeSettling Method

Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAmplitudeSettling(
	string channelName,
	double value
)
```

```text
Public Function SetAmplitudeSettling ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Identifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter.
- **value Double**
  - Specifies the the amplitude settling accuracy value. This value is expressed in decibels.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm language=enus -->
## TOPIC 00033: rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeSByteArray Method

RFmxInstrMXGetAttributeSByteArray Method

Gets the value of a sbyte array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeSByteArray(
	string channelName,
	int attributeIdentifier,
	ref sbyte[] value
)
```

```text
Public Function GetAttributeSByteArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As SByte()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value SByte**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/3750c58c-9f7b-4165-21ab-fe8dc3f77a32.htm language=enus -->
## TOPIC 00034: rfmxinstrdotnet/html/3750c58c-9f7b-4165-21ab-fe8dc3f77a32.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/3750c58c-9f7b-4165-21ab-fe8dc3f77a32.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/3750c58c-9f7b-4165-21ab-fe8dc3f77a32.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.ClockIn Field

RFmxInstrMXConstantsClockIn Field

PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the [SetFrequencyReferenceFrequency(String, Double)](606143ec-e637-e700-cf97-1b6e1e4076e1.htm) method to 100 MHz.

PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the [SetFrequencyReferenceFrequency(String, Double)](606143ec-e637-e700-cf97-1b6e1e4076e1.htm) method
 to 100 MHz.

PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840/5841/5842/5860 with PXIe-5653: This configuration does not apply.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string ClockIn = "ClkIn"
```

```text
Public Const ClockIn As String = "ClkIn"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm language=enus -->
## TOPIC 00035: rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFftWidth Method

RFmxInstrMXGetFftWidth Method

Gets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftWidth(
	string channelName,
	out double value
)
```

```text
Public Function GetFftWidth ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

###### Return Value

Int32

##### Remarks

FftWidth

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/37ad0021-e833-3d40-866f-2cfc6bbff712.htm language=enus -->
## TOPIC 00036: rfmxinstrdotnet/html/37ad0021-e833-3d40-866f-2cfc6bbff712.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/37ad0021-e833-3d40-866f-2cfc6bbff712.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/37ad0021-e833-3d40-866f-2cfc6bbff712.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetNumberOfRawIQRecords Method

RFmxInstrMXGetNumberOfRawIQRecords Method

Gets the number of raw IQ records to acquire to complete measurement averaging.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfRawIQRecords(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfRawIQRecords ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Int32**
  - Gets the number of raw IQ records to acquire to complete measurement averaging. This property returns a value of 0 when RFmx cannot provide I/Q data for the specified measurement configuration.

###### Return Value

Int32

##### Remarks

NumberOfRawIQRecords

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm language=enus -->
## TOPIC 00037: rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

IList.ListType Property

IListListType Property

Gets the type of the current list object.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
Type ListType { get; }
```

```text
ReadOnly Property ListType As Type
	Get
```

###### Property Value

Type

##### See Also

###### Reference

IList Interface

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm language=enus -->
## TOPIC 00038: rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetTuningSpeed Method

RFmxInstrMXSetTuningSpeed Method

Makes tradeoffs between tuning speed and phase noise.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTuningSpeed(
	string channelName,
	RFmxInstrMXTuningSpeed value
)
```

```text
Public Function SetTuningSpeed ( 
	channelName As String,
	value As RFmxInstrMXTuningSpeed
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value RFmxInstrMXTuningSpeed**
  - Makes tradeoffs between tuning speed and phase noise.

###### Return Value

Int32

##### Remarks

TuningSpeed

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm language=enus -->
## TOPIC 00039: rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeFloat Method

RFmxInstrMXGetAttributeFloat Method

Gets the value of a Float attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeFloat(
	string channelName,
	int attributeIdentifier,
	out float value
)
```

```text
Public Function GetAttributeFloat ( 
	channelName As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Single
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Single**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/44d8c1df-d59f-698b-7448-9907c404e486.htm language=enus -->
## TOPIC 00040: rfmxinstrdotnet/html/44d8c1df-d59f-698b-7448-9907c404e486.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/44d8c1df-d59f-698b-7448-9907c404e486.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/44d8c1df-d59f-698b-7448-9907c404e486.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXLoadOptions Enumeration

RFmxInstrMXLoadOptions Enumeration

LoadConfigurations(String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXLoadOptions
```

```text
Public Enumeration RFmxInstrMXLoadOptions
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| SkipNone | 0 | RFmx loads all the configurations to the session. |
| SkipRFInstr | 1 | RFmx skips loading the RFmxInstr configurations to the session. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/4cfafbd0-d2d4-603e-c793-3de7feb038a3.htm language=enus -->
## TOPIC 00041: rfmxinstrdotnet/html/4cfafbd0-d2d4-603e-c793-3de7feb038a3.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/4cfafbd0-d2d4-603e-c793-3de7feb038a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/4cfafbd0-d2d4-603e-c793-3de7feb038a3.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetCommonModeLevel Method

RFmxInstrMXSetCommonModeLevel Method

Sets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCommonModeLevel(
	string channelName,
	double value
)
```

```text
Public Function SetCommonModeLevel ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Specifies the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

###### Return Value

Int32

##### Remarks

CommonModeLevel

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/4d78dea5-fdb3-4c56-e8bc-6f03bdf888ed.htm language=enus -->
## TOPIC 00042: rfmxinstrdotnet/html/4d78dea5-fdb3-4c56-e8bc-6f03bdf888ed.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/4d78dea5-fdb3-4c56-e8bc-6f03bdf888ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/4d78dea5-fdb3-4c56-e8bc-6f03bdf888ed.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.CheckAcquisitionStatus Method

RFmxInstrMXCheckAcquisitionStatus Method

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int CheckAcquisitionStatus(
	out bool done
)
```

```text
Public Function CheckAcquisitionStatus ( 
	<OutAttribute> ByRef done As Boolean
) As Integer
```

###### Parameters

- **done Boolean**
  - Indicates whether the acquisition is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/4e32fd9b-7d12-3d27-1c6a-2980762699f8.htm language=enus -->
## TOPIC 00043: rfmxinstrdotnet/html/4e32fd9b-7d12-3d27-1c6a-2980762699f8.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/4e32fd9b-7d12-3d27-1c6a-2980762699f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/4e32fd9b-7d12-3d27-1c6a-2980762699f8.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX Class

RFmxInstrMX Class

Defines a root class which is used to identify and control Instr signal configuration.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxInstrMX : IDisposable
```

```text
Public NotInheritable Class RFmxInstrMX
	Implements IDisposable
```

The RFmxInstrMX type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | RFmxInstrMX(IntPtr) | Creates a new RFmx session from an existing RFmx instrument handle. |
|  | RFmxInstrMX(String, String) | Creates an RFmx session to the device you specify through the resourceName parameter. Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| Note |  |  |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |  |  |
|  | RFmxInstrMX(String, String) | Creates an RFmx session to the device you specify through the resourceName parameter. Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| Note |  |  |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |  |  |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | NumberOfLists | Gets the number of lists created in the current session. |
|  | NumberOfSignalConfigurations | Gets the number of signal configurations created in the current session. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BuildCalibrationPlaneString | Creates the selector string to use with External Attenuation Table methods. |
|  | BuildInstrumentString | Creates the instrument string to use as the Selector String for reading the recommended settings. |
|  | BuildLOString | Creates the LO string to use as the selector string for LO related methods. |
|  | BuildModuleString | Configures the Module string to use as the Selector String for reading temperature of specific modules of the device. |
|  | BuildPortString2 | Creates the port string to use as the selector string with External Attenuation Table methods. On a MIMO session, this method can be used to build port string to use as a selector string for configuring or reading port-specific methods and external attenuation table methods. |
|  | CheckAcquisitionStatus | Checks the status of the acquisition. Use this method to check for any errors that may occur during acquisition, or to check whether RFmx has completed the acquisition operation. |
|  | CheckIfListExists | Returns whether the list you specify in the listname parameter exists, and also returns the corresponding personality of the list, if the list exists. This method does not support an empty ("") list name. |
|  | CheckIfSignalExists | Returns whether the signal you specify in the signalname parameter exists, and also returns the corresponding personality of the signal, if the signal exists. This method does not support an empty ("") signal name. |
|  | Close | Closes the RFmx session. |
|  | ConfigureExternalAttenuationInterpolationLinear | Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this method performs a linear interpolation based on the entries above and below the row in the table. Currently interpolation is supported only for S-parameter tables. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | ConfigureExternalAttenuationInterpolationNearest | Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used. Currently interpolation is supported only for S-parameter tables. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5860 |
|  | ConfigureExternalAttenuationInterpolationSpline | Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this method performs a spline interpolation based on the entries above and below the row in the table. Currently interpolation is supported only for S-parameter tables. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | ConfigureExternalAttenuationTable | Stores the external attenuation table in the calibration plane specified by the selectorString parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. If there is only one table configured in any calibration plane, it is automatically selected as the active table.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | ConfigureFrequencyReference | Configures the Reference Clock and the frequency reference source. |
|  | ConfigureMechanicalAttenuation | Configures the mechanical attenuation and RFmx attenuation hardware settings.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668 |
|  | ConfigureRFAttenuation | Configures the nominal attenuation and RFmx setting. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668 |
|  | ConfigureSParameterExternalAttenuationTable | Stores the S-parameter table in the calibration plane specified by the selectorString parameter. On a MIMO session the S-parameter table is stored for each MIMO port in the specified calibration plane.supporteddevices: PXIe-5830/5831/5832/5840/5841/5842/5860 If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
|  | ConfigureSParameterExternalAttenuationType | Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. supporteddevices: PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | DangerousGetNIRfsaHandle | Returns the value of the underlying instrument handle. Note Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |
| Note |  |  |
| Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |  |  |
|  | DangerousGetNIRfsaHandleArray | Returns list of underlying instrument handles. Note Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |
| Note |  |  |
| Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |  |  |
|  | DeleteAllExternalAttenuationTables | Deletes all the external attenuation tables in the calibration plane specified by the selectorString parameter. On a MIMO session, this method deletes all the external attenuation tables for the specified MIMO port. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | DeleteExternalAttenuationTable | Deletes the external attenuation table set by the tableName parameter in the calibration plane specified by the selectorString parameter. On a MIMO session, this method selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | DisableCalibrationPlane | Disables the calibration plane specified by the selectorString parameter for amplitude correction.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | EnableCalibrationPlane | Enables the calibration plane specified by the selectorString parameter for amplitude correction.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | ExportSignal | Routes signals (triggers, clocks, and events) to the specified output terminal. This method is not supported on a MIMO session. |
|  | FetchRawIQData | Fetches I/Q data from a single record in an acquisition. |
|  | ForceClose | Closes all RFmx sessions. Calling this method once will destroy the session, irrespective of the many references obtained for the session for a particular resource name. |
|  | GetAdvanceTriggerDigitalEdgeSource | Gets the source terminal for the advance trigger. |
|  | GetAdvanceTriggerExportOutputTerminal | Gets the destination terminal for the exported advance trigger. |
|  | GetAdvanceTriggerTerminalName | Gets the fully qualified signal name as a string. |
|  | GetAdvanceTriggerType | Gets whether the advance trigger is a digital edge or a software trigger. |
|  | GetAmplitudeSettling | Gets the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate function. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeByte | Gets the value of a Byte attribute. |
|  | GetAttributeByteArray | Gets the value of a byte array attribute. |
|  | GetAttributeComplexDoubleArray | Gets the value of a ComplexDouble array attribute. |
|  | GetAttributeComplexSingleArray | Gets the value of a ComplexSingle array attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeDoubleArray | Gets the value of a double array attribute. |
|  | GetAttributeFloat | Gets the value of a Float attribute. |
|  | GetAttributeFloatArray | Gets the value of a float array attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeIntArray | Gets the value of a int array attribute. |
|  | GetAttributeLong | Gets the value of an RFmx 64-bit integer (int64) attribute. |
|  | GetAttributeLongArray | Gets the value of a long array attribute. |
|  | GetAttributeSByte | Gets the value of a SByte attribute. |
|  | GetAttributeSByteArray | Gets the value of a sbyte array attribute. |
|  | GetAttributeShort | Gets the value of a Short attribute. |
|  | GetAttributeString | Gets the value of a string attribute. |
|  | GetAttributeUInt | Gets the value of a uint attribute. |
|  | GetAttributeUIntArray | Gets the value of a uint array attribute. |
|  | GetAttributeULongArray | Gets the value of a ulong array attribute. |
|  | GetAttributeUShort | Gets the value of a UShort attribute. |
|  | GetAvailablePaths | Gets paths available for the session. On a MIMO session, this method fetches all the paths for the initialized MIMO paths. |
|  | GetAvailablePorts(String) | Obsolete. Gets the list of ports available for use based on your instrument configuration. |
|  | GetAvailablePorts(String, String) | Gets ports available for the session. On a MIMO session, this method fetches all the ports for the initialized MIMO ports. |
|  | GetChannelCoupling | Gets whether the RF IN connector is AC- or DC-coupled on the downconverter. |
|  | GetCleanerSpectrum | Gets how to obtain the lowest noise floor or faster measurement speed. |
|  | GetCommonModeLevel | Gets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. |
|  | GetDeviceTemperature | Gets the current temperature of the module. This value is expressed in degrees Celsius. |
|  | GetDigitalGain | Gets the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. |
|  | GetDigitizerDitherEnabled | Gets whether dithering is enabled on the digitizer. |
|  | GetDigitizerTemperature | Gets the current temperature of the digitizer module. This value is expressed in degrees Celsius. |
|  | GetDoneEventOutputTerminal | Gets the destination terminal for the Done event. |
|  | GetDoneEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetDownconverterCenterFrequency | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | GetDownconverterFrequencyOffset | Gets an offset from the center frequency value for the downconverter. Use this method to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this method to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. |
|  | GetDownconverterGain | Gets the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this method. |
|  | GetDownconverterPreselectorEnabled | Gets whether the tunable preselector is enabled on the downconverter. |
|  | GetEndOfRecordEventOutputTerminal | Gets the destination terminal for the End of Record event. |
|  | GetEndOfRecordEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetErrorString | Converts the status code returned by an RFmxInstr function into a string. |
|  | GetExternalAttenuationTableActualValue | Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane. |
|  | GetFftWidth | Gets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. |
|  | GetFrequencyReferenceExportedTerminal | Gets a comma-separated list of the terminals at which to export the frequency reference. |
|  | GetFrequencyReferenceFrequency | Gets the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz. |
|  | GetFrequencyReferenceSource | Gets the frequency reference source. |
|  | GetFrequencySettling | Gets the value used for LO frequency settling. |
|  | GetFrequencySettlingUnits | Gets the delay duration units and interpretation for LO settling. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIFFilterBandwidth | Gets the IF filter path bandwidth for your device configuration. |
|  | GetIFOutputPowerLevelOffset | Gets the power offset by which to adjust the default IF output power level. This value is expressed in dB. |
|  | GetInputIsolationEnabled | Gets whether input isolation is enabled. |
|  | GetInstrumentFirmwareRevision | Gets a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. |
|  | GetInstrumentHandle | Gets the SafeHandle to the RFmxInstrMX instrument session. |
|  | GetInstrumentModel | Gets a string that contains the model number or name of the RF device that you are currently using. |
|  | GetListNames | Returns the list names and the corresponding selected personality type from the personalityFilter parameter. When you set the personalityFilter parameter to all, this function returns the available list names for all supported personalities. |
|  | GetLO2ExportEnabled | Gets whether to enable the LO2 OUT terminals in the installed devices. |
|  | GetLoadOptions | Specifies the configurations to skip while loading from a file using the LoadConfigurations(String) method |
|  | GetLOExportEnabled | Gets whether to enable the LO OUT terminals on the installed devices. |
|  | GetLOFrequency | Gets the LO signal frequency for the configured center frequency. This value is expressed in Hz. |
|  | GetLOFrequencyStepSize | Gets the step size for tuning the LO phase-locked loop (PLL). |
|  | GetLOInjectionSide | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | GetLOInPower | Gets the power level expected at the LO IN terminal when the SetLOSource(String, String) method is set to RFMXINSTR_VAL_LO_SOURCE_LO_IN. This value is expressed in dBm. |
|  | GetLOLeakageAvoidanceEnabled | Gets whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. |
|  | GetLOOutPower | Gets the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(String, Boolean) method is set to TRUE. This value is expressed in dBm. |
|  | GetLOPllFractionalMode | Gets whether to use fractional mode for the LO phase-locked loop (PLL). |
|  | GetLOSharingMode | Gets the RFmx session with the respective LO sharing mode. |
|  | GetLOSource | Gets the LO signal source used to downconvert the RF input signal. |
|  | GetLOTemperature | Gets the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. |
|  | GetLOVcoFrequencyStepSize | Gets the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. |
|  | GetMechanicalAttenuationAuto | Gets whether RFmx chooses an attenuation setting based on the hardware settings. |
|  | GetMechanicalAttenuationValue | Gets the level of mechanical attenuation for the RF path. This value is expressed in dB. |
|  | GetMixerLevel | Gets the mixer level, in dBm. |
|  | GetMixerLevelOffset | Gets the number of dB by which to adjust the device mixer level. |
|  | GetModuleRevision | Gets the revision of the RF downconverter module. |
|  | GetNumberOfLOSharingGroups | Gets the RFmx session with the number of LO sharing groups. |
|  | GetNumberOfRawIQRecords | Gets the number of raw IQ records to acquire to complete measurement averaging. |
|  | GetOptimizePathForSignalBandwidth | Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. |
|  | GetOspDelayEnabled | Gets whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. |
|  | GetOverflowErrorReporting | Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. |
|  | GetPhaseOffset | Gets the offset to apply to the initial I and Q phases. |
|  | GetPreampEnabled | Gets whether the RF preamplifier is enabled in the system. |
|  | GetPreselectorPresent | Indicates whether a preselector is available on the RF downconverter module. |
|  | GetReadyForAdvanceEventOutputTerminal | Gets the destination terminal for the Ready for Advance event. |
|  | GetReadyForAdvanceEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetReadyForReferenceEventOutputTerminal | Gets the destination terminal for the Ready for Reference event. |
|  | GetReadyForReferenceEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetReadyForStartEventOutputTerminal | Gets the destination terminal for the Ready for Start event. |
|  | GetReadyForStartEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetRecommendedAcquisitionType | Gets the recommended acquisition type for the last committed measurement configuration. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedCenterFrequency | Gets the recommended center frequency of the RF signal. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedIQAcquisitionTime | Gets the recommended acquisition time for I/Q acquisition, in seconds. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedIQMinimumSampleRate | Gets the recommended minimum sample rate for I/Q acquisition, in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedIQPreTriggerTime | Gets the recommended pretrigger time for I/Q acquisition, in seconds. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedNumberOfRecords | Gets the recommended number of records to acquire to complete measurement averaging. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedSpectralAcquisitionSpan | Gets the recommended acquisition span for spectral acquisition, in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedSpectralFftWindow | Gets the recommended FFT window type for spectral acquisition. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedSpectralResolutionBandwidth | Gets the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedTriggerMinimumQuietTime | Gets the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRFAttenuationAuto | Gets whether RFmx computes the RF attenuation. |
|  | GetRFAttenuationStepSize | Gets the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. |
|  | GetRFAttenuationValue | Gets the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. |
|  | GetRFHighpassFilterFrequency | Gets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | GetRFPreampPresent | Indicates whether an RF preamplifier is available on the RF downconverter module. |
|  | GetSelfCalibrateLastDateAndTime | Gets the date and time of the last successful self-calibration. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Note For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |
| Note |  |  |
| For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |  |  |
|  | GetSelfCalibrateLastTemperature | Gets the temperature of the last successful self-calibration. This value is expresed in degree Celsius. On a MIMO session, use the selectorString parameter to get the last successful self-calibration temperature for a specific MIMO port. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860 Note For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |
| Note |  |  |
| For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |  |  |
|  | GetSelfCalibrationValidityCheck | Gets whether RFmx validates the self-calibration data. |
|  | GetSelfCalibrationValidityCheckTimeInterval | Gets the minimum time between two self calibration validity checks. This value is expressed in seconds. |
|  | GetSerialNumber | Gets the serial number of the RF downconverter module. |
|  | GetSession(String, String) | Gets a session, if it exists for given resource name; else, returns a new one. |
|  | GetSession(String, String) | Gets a session, if it exists for given set of resource name; else, returns a new one. |
|  | GetSession(String, String, Boolean) | Gets a session, if it exists for given resource name; else, returns a new one. |
|  | GetSession(String, String, Boolean) | Gets a session, if it exists for given set of resource name; else, returns a new one. |
|  | GetSessionFromNIRfsaHandle | Gets a session, if it exists for given NIRfsa instrument handle; else, returns a new one. Note1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |
| Note |  |  |
| 1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |  |  |
|  | GetSessionFromNIRfsaHandles | Gets a session, if it exists for given set of NIRfsa instrument handle; else, returns a new one. Note1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |
| Note |  |  |
| 1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |  |  |
|  | GetSignalConfigurationNames | Returns the signal names and corresponding personality type, for the personality type selected in the personalityFilter parameter. |
|  | GetSmuChannel | Gets the output channel to be used for noise figure (NF) measurement in RFmx. |
|  | GetSmuResourceName | Gets the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name. |
|  | GetSParameterExternalAttenuationType | Returns the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the selectorString input to specify the name of the Calplane and port to configure for s-parameter. Supported devices: PXIe-5830/5831/5832/5840 |
|  | GetStartTriggerDigitalEdge | Gets the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | GetStartTriggerDigitalEdgeSource | Gets the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | GetStartTriggerExportOutputTerminal | Gets the destination terminal for the exported start trigger. |
|  | GetStartTriggerTerminalName | Gets the fully qualified signal name as a string. |
|  | GetStartTriggerType | Gets whether the start trigger is a digital edge or a software trigger. |
|  | GetSubSpanOverlap | Gets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | GetTemperatureReadInterval | Gets the minimum time difference between temperature sensor readings. This value is expressed in seconds. |
|  | GetThermalCorrectionHeadroomRange | Gets the expected thermal operating range of the instrument from the self-calibration temperature returned from the GetDeviceTemperature(String, Double) method. This value is expressed in degree Celsius. |
|  | GetThermalCorrectionTemperatureResolution | Gets the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. |
|  | GetTriggerExportOutputTerminal | Gets the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. |
|  | GetTriggerTerminalName | Gets the fully-qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/RefTrigger, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/RefTrigger, where BasebandModule is the name of your device in MAX. PXIe-5860: /ModuleName/ai/ChannelNumber/RefTrigger,, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). All other devices: /DigitizerName/RefTrigger, where DigitizerName is the name of your associated digitizer module in MAX. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | GetTuningSpeed | Makes tradeoffs between tuning speed and phase noise. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetWarning | Gets the latest warning code and description. |
|  | IsSelfCalibrateValid | Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the validSteps parameter to the stepsToOmit parameter of the SelfCalibrate(String, RFmxInstrMXSelfCalibrateSteps) method. On a MIMO session use the selectorString parameter to get the self-calibration validity for a specific MIMO port.supporteddevices: PXIe-5663/5663E/5665/5668 |
|  | LoadConfigurations | Loads the methods of an RFmx session saved in a file. This file can be generated using SaveAllConfigurations(String) method or the RF Signal Analyzer panel in InstrumentStudio. You can specify the configurations to skip while loading from a file using the LoadOptions property. If the file contains a named signal configuration which is already present in the session, then this method will return an error. It is recommended to call the RFmxInstr Reset Entire Session method to delete all the named signal configurations in the session. |
|  | LoadSParameterExternalAttenuationTableFromS2pFile | Stores the S-parameter table from the S2P file in the calibration plane specified by the selectorString parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session the S-parameter table is stored for each MIMO port in the specified calibration plane.supporteddevices: PXIe-5830/5831/5832/5840/5841/5842/5860 If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetDriver | Restores the NI-RFSA driver state to a default state to avoid RFmx using any hardware or driver state that was set by the RF toolkits or other custom NI-RFSA code. Use this method when you switch back to using RFmx to perform measurements after you have used the NI-RFSA handle to perform measurements with RF toolkits or you have used other custom NI-RFSA code. Unlike the ResetToDefault method, the RfmxInstr Reset Driver method does not reset RFmx methods configured on the RFmx session. Hence, you do not need to set RFmx methods again when switching back to RFmx measurements. Refer to RFmx SpecAn CHP - WCDMA ModAcc - CHP Example (LabVIEW) on ni.com for more information about using RFmx to perform measurements. |
|  | ResetEntireSession | Deletes all the named signal configurations in the session and resets all methods for the default signal instances of already loaded personalities in the session. This method disables all the calibration planes. |
|  | ResetToDefault | Resets the RFmxInstr methods to their default values. This method disables all the calibration planes. |
|  | SaveAllConfigurations | Saves all the configured methods in the RFmx session to a file in the specified file path. Use this method to save the current state of the RFmx session. On a MIMO session, this method saves all the configured methods for the specified MIMO port. List configurations, reference waveforms and external attenuation tables are not saved by this method. |
|  | SelectActiveExternalAttenuationTable | Activates the external attenuation table set by the tableName parameter in the calibration plane specified by the selectorString parameter. On a MIMO session, this method selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | SelfCalibrate | Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this method self-calibrates all NI-RFSA devices and associated modules that support self-calibration. Refer to the specifications document for your device for more information about how often to self-calibrate. For more information about Self Calibrate, refer to the niRFSA Self Cal method topic for your device in the NI RF Vector Signal Analyzers Help. For PXIe-5644/5645/5646, RFmx internally closes the RFSA session, performs self-calibration and opens a new session for the same device. If the RFSA session has been accessed from RFmx, using the RFmxInstr Get NIRFSA Session method before calling the RFmxInstr Self Calibrate method, the RFSA session will become invalid upon calling the RFmxInstr Self Calibrate. supporteddevices: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SelfCalibrateRange | Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this method runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the niRFSA Self Calibrate Range method topic for your device in the NI RF Vector Signal Analyzers Help. On a MIMO session, this method self-calibrates all NI-RFSA devices and associated modules that support self-calibration.supporteddevices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 This method does not update self-calibration date and temperature. Self-calibration range data is not saved to your device if you restart the system. |
|  | SendSoftwareEdgeAdvanceTrigger | Sends a trigger to the waiting device when you choose a software version of the Advance trigger. You can also use this method to override a hardware trigger. This method returns an error if: You configure an invalid trigger. You have not previously called the RFmx Initiate method.supporteddevices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SendSoftwareEdgeStartTrigger | Sends a trigger to the waiting device when you choose a software version of Start trigger. You can also use this method to override a hardware trigger. This method returns an error if: You configure an invalid trigger. You have not previously called the RFmx Initiate method.supporteddevices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SetAdvanceTriggerDigitalEdgeSource | Sets the source terminal for the advance trigger. |
|  | SetAdvanceTriggerExportOutputTerminal | Sets the destination terminal for the exported advance trigger. |
|  | SetAdvanceTriggerType | Sets whether the advance trigger is a digital edge or a software trigger. |
|  | SetAmplitudeSettling | Sets the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate method. Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value. Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeByte | Sets the value of a Byte attribute. |
|  | SetAttributeByteArray | Sets the value of a byte array attribute. |
|  | SetAttributeComplexDoubleArray | Sets the value of a ComplexDouble array attribute. |
|  | SetAttributeComplexSingleArray | Sets the value of a ComplexSingle array attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeDoubleArray | Sets the value of a double array attribute. |
|  | SetAttributeFloat | Sets the value of a Float attribute. |
|  | SetAttributeFloatArray | Sets the value of a float array attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeIntArray | Sets the value of a int array attribute. |
|  | SetAttributeLong | Sets the value of a Long attribute. |
|  | SetAttributeLongArray | Sets the value of a long array attribute. |
|  | SetAttributeSByte | Sets the value of a SByte attribute. |
|  | SetAttributeSByteArray | Sets the value of a sbyte array attribute. |
|  | SetAttributeShort | Sets the value of a Short attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAttributeUInt | Sets the value of a UInt attribute. |
|  | SetAttributeUIntArray | Sets the value of a uint array attribute. |
|  | SetAttributeULongArray | Sets the value of a ulong array attribute. |
|  | SetAttributeUShort | Sets the value of a UShort attribute. |
|  | SetChannelCoupling | Sets whether the RF IN connector is AC- or DC-coupled on the downconverter. |
|  | SetCleanerSpectrum | Sets how to obtain the lowest noise floor or faster measurement speed. |
|  | SetCommonModeLevel | Sets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. |
|  | SetDigitalGain | Sets the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. |
|  | SetDigitizerDitherEnabled | Sets whether dithering is enabled on the digitizer. |
|  | SetDoneEventOutputTerminal | Sets the destination terminal for the Done event. |
|  | SetDownconverterCenterFrequency | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | SetDownconverterFrequencyOffset | Sets an offset from the center frequency value for the downconverter. Use this method to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this method to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. |
|  | SetDownconverterPreselectorEnabled | Sets whether the tunable preselector is enabled on the downconverter. |
|  | SetEndOfRecordEventOutputTerminal | Sets the destination terminal for the End of Record event. |
|  | SetFftWidth | Sets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. |
|  | SetFrequencyReferenceExportedTerminal | Sets a comma-separated list of the terminals at which to export the frequency reference. |
|  | SetFrequencyReferenceFrequency | Sets the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz. |
|  | SetFrequencyReferenceSource | Sets the frequency reference source. |
|  | SetFrequencySettling | Sets the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the SetFrequencySettlingUnits(String, RFmxInstrMXFrequencySettlingUnits) method. Note This method is not supported if you are using an external LO. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 |
| Note |  |  |
| This method is not supported if you are using an external LO. |  |  |
|  | SetFrequencySettlingUnits | Gets the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the SetFrequencySettlingUnits(String, RFmxInstrMXFrequencySettlingUnits) method. Note This method is not supported if you are using an external LO. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 |
| Note |  |  |
| This method is not supported if you are using an external LO. |  |  |
|  | SetIFFilterBandwidth | Sets the IF filter path bandwidth for your device configuration. |
|  | SetIFOutputPowerLevelOffset | Sets the power offset by which to adjust the default IF output power level. This value is expressed in dB. |
|  | SetInputIsolationEnabled | Sets whether input isolation is enabled. |
|  | SetLO2ExportEnabled | Sets whether to enable the LO2 OUT terminals in the installed devices. |
|  | SetLoadOptions | Specifies the configurations to skip while loading from a file using the LoadConfigurations(String) method |
|  | SetLOExportEnabled | Sets whether to enable the LO OUT terminals on the installed devices. |
|  | SetLOFrequency | Sets the LO signal frequency for the configured center frequency. This value is expressed in Hz. |
|  | SetLOFrequencyStepSize | Sets the step size for tuning the LO phase-locked loop (PLL). |
|  | SetLOInjectionSide | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | SetLOInPower | Sets the power level expected at the LO IN terminal when the SetLOSource(String, String) method is set to RFMXINSTR_VAL_LO_SOURCE_LO_IN. This value is expressed in dBm. |
|  | SetLOLeakageAvoidanceEnabled | Sets whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. |
|  | SetLOOutPower | Sets the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(String, Boolean) method is set to TRUE. This value is expressed in dBm. |
|  | SetLOPllFractionalMode | Sets whether to use fractional mode for the LO phase-locked loop (PLL). |
|  | SetLOSharingMode | Sets the RFmx session with the respective LO sharing mode. |
|  | SetLOSource | Sets the LO signal source used to downconvert the RF input signal. |
|  | SetLOVcoFrequencyStepSize | Sets the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. |
|  | SetMechanicalAttenuationAuto | Sets whether RFmx chooses an attenuation setting based on the hardware settings. |
|  | SetMechanicalAttenuationValue | Sets the level of mechanical attenuation for the RF path. This value is expressed in dB. |
|  | SetMixerLevel | Sets the mixer level, in dBm. |
|  | SetMixerLevelOffset | Sets the number of dB by which to adjust the device mixer level. |
|  | SetNumberOfLOSharingGroups | Sets the RFmx session with the number of LO sharing groups. |
|  | SetOptimizePathForSignalBandwidth | Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. |
|  | SetOspDelayEnabled | Sets whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. |
|  | SetOverflowErrorReporting | Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. |
|  | SetPhaseOffset | Sets the offset to apply to the initial I and Q phases. |
|  | SetPreampEnabled | Sets whether the RF preamplifier is enabled in the system. |
|  | SetReadyForAdvanceEventOutputTerminal | Sets the destination terminal for the Ready for Advance event. |
|  | SetReadyForReferenceEventOutputTerminal | Sets the destination terminal for the Ready for Reference event. |
|  | SetReadyForStartEventOutputTerminal | Sets the destination terminal for the Ready for Start event. |
|  | SetRFAttenuationAuto | Sets whether RFmx computes the RF attenuation. |
|  | SetRFAttenuationStepSize | Sets the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. |
|  | SetRFAttenuationValue | Sets the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. |
|  | SetRFHighpassFilterFrequency | Sets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | SetSelfCalibrationValidityCheck | Sets whether RFmx validates the self-calibration data. |
|  | SetSelfCalibrationValidityCheckTimeInterval | Sets the minimum time between two self calibration validity checks. This value is expressed in seconds. |
|  | SetSmuChannel | Sets the output channel to be used for noise figure (NF) measurement in RFmx. |
|  | SetSmuResourceName | Sets the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name. |
|  | SetStartTriggerDigitalEdge | Sets the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | SetStartTriggerDigitalEdgeSource | Sets the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | SetStartTriggerExportOutputTerminal | Sets the destination terminal for the exported start trigger. |
|  | SetStartTriggerType | Sets whether the start trigger is a digital edge or a software trigger. |
|  | SetSubSpanOverlap | Sets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | SetTemperatureReadInterval | Sets the minimum time difference between temperature sensor readings. This value is expressed in seconds. |
|  | SetThermalCorrectionHeadroomRange | Sets the expected thermal operating range of the instrument from the self-calibration temperature returned from the GetDeviceTemperature(String, Double) method. This value is expressed in degree Celsius. |
|  | SetThermalCorrectionTemperatureResolution | Sets the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. |
|  | SetTriggerExportOutputTerminal | Sets the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. |
|  | SetTuningSpeed | Makes tradeoffs between tuning speed and phase noise. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |
|  | WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is complete. This method is typically called after a specific initiate method. |

Top

##### Remarks

For more information about RFmx Instruments, refer to RFmx Instruments Help.

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/4e43a5cb-b69a-2965-81a4-c91f50c2cf2f.htm language=enus -->
## TOPIC 00044: rfmxinstrdotnet/html/4e43a5cb-b69a-2965-81a4-c91f50c2cf2f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/4e43a5cb-b69a-2965-81a4-c91f50c2cf2f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/4e43a5cb-b69a-2965-81a4-c91f50c2cf2f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetOverflowErrorReporting Method

RFmxInstrMXSetOverflowErrorReporting Method

Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOverflowErrorReporting(
	string channelName,
	RFmxInstrMXOverflowErrorReporting value
)
```

```text
Public Function SetOverflowErrorReporting ( 
	channelName As String,
	value As RFmxInstrMXOverflowErrorReporting
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXOverflowErrorReporting**
  - Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

###### Return Value

Int32

##### Remarks

OverflowErrorReporting

Warning

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/4f5a2ca4-3321-1e11-443b-3d1e0557fec7.htm language=enus -->
## TOPIC 00045: rfmxinstrdotnet/html/4f5a2ca4-3321-1e11-443b-3d1e0557fec7.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/4f5a2ca4-3321-1e11-443b-3d1e0557fec7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/4f5a2ca4-3321-1e11-443b-3d1e0557fec7.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.IsSelfCalibrateValid Method

RFmxInstrMXIsSelfCalibrateValid Method

validSteps

stepsToOmit

SelfCalibrate(String, RFmxInstrMXSelfCalibrateSteps)

supporteddevices:

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int IsSelfCalibrateValid(
	string selectorString,
	out bool selfCalibrateValid,
	out RFmxInstrMXSelfCalibrateSteps validSteps
)
```

```text
Public Function IsSelfCalibrateValid ( 
	selectorString As String,
	<OutAttribute> ByRef selfCalibrateValid As Boolean,
	<OutAttribute> ByRef validSteps As RFmxInstrMXSelfCalibrateSteps
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a Selector String comprising of a MIMO port on a MIMO session. Example:"""port::myrfsa1/0" You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **selfCalibrateValid Boolean**
  - Upon return, contains TRUE if all the calibration data is valid and FALSE if any of the calibration data is invalid.
- **validSteps RFmxInstrMXSelfCalibrateSteps**
  - Upon return, contains an array of valid steps. PreselectorAlignmentIndicates the Preselector Alignment calibration data is valid. This step generates coefficients to align the preselector across the frequency range for your device.GainReferenceIndicates the Gain Reference calibration data is valid. This step measures the changes in gain since the last external calibration was run. IFFlatnessIndicates the IF Flatness calibration data is valid. This step measures the IF response of the entire system for each of the supported IF filters.DigitizerSelfcalIndicates the Digitizer Self Cal calibration data is valid. This step calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.LOSelfCalIndicates the LO Self Cal calibration data is valid. This step calls for LO self-calibration, if the LO source module is associated with the RF downconverter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5078e3ce-893a-2293-6720-cfce0162e496.htm language=enus -->
## TOPIC 00046: rfmxinstrdotnet/html/5078e3ce-893a-2293-6720-cfce0162e496.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5078e3ce-893a-2293-6720-cfce0162e496.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5078e3ce-893a-2293-6720-cfce0162e496.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXPreampEnabled Enumeration

RFmxInstrMXPreampEnabled Enumeration

Specifies whether the RF preamplifier is enabled in the system.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXPreampEnabled
```

```text
Public Enumeration RFmxInstrMXPreampEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the RF preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668 |
| Enabled | 1 | Enables the RF preamplifier when it is in the signal path and disables it when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the GetRFPreampPresent(String, Boolean) method to determine whether the downconverter has a preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668 |
| Automatic | 3 | Automatically enables the RF preamplifier based on the value of the reference level. Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5112893d-57cb-5bce-0d16-3b6a268309d6.htm language=enus -->
## TOPIC 00047: rfmxinstrdotnet/html/5112893d-57cb-5bce-0d16-3b6a268309d6.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5112893d-57cb-5bce-0d16-3b6a268309d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5112893d-57cb-5bce-0d16-3b6a268309d6.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetFrequencySettling Method

RFmxInstrMXSetFrequencySettling Method

SetFrequencySettlingUnits(String, RFmxInstrMXFrequencySettlingUnits)

| Note |
| --- |
| This method is not supported if you are using an external LO. |

Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencySettling(
	string channelName,
	double value
)
```

```text
Public Function SetFrequencySettling ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Identifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter.
- **value Double**
  - Specifies the value used for LO frequency settling.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/51478d2d-5a06-1edc-53f2-0a1fb0d0fb73.htm language=enus -->
## TOPIC 00048: rfmxinstrdotnet/html/51478d2d-5a06-1edc-53f2-0a1fb0d0fb73.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/51478d2d-5a06-1edc-53f2-0a1fb0d0fb73.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/51478d2d-5a06-1edc-53f2-0a1fb0d0fb73.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLOFrequencyStepSize Method

RFmxInstrMXSetLOFrequencyStepSize Method

Sets the step size for tuning the LO phase-locked loop (PLL).

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLOFrequencyStepSize(
	string selectorString,
	double value
)
```

```text
Public Function SetLOFrequencyStepSize ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Specifies the step size for tuning the LO phase-locked loop (PLL).

###### Return Value

Int32

##### Remarks

LOFrequencyStepSize

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/517255a9-8178-599e-8482-1a245c1c65f3.htm language=enus -->
## TOPIC 00049: rfmxinstrdotnet/html/517255a9-8178-599e-8482-1a245c1c65f3.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/517255a9-8178-599e-8482-1a245c1c65f3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/517255a9-8178-599e-8482-1a245c1c65f3.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.LoadSParameterExternalAttenuationTableFromS2pFile Method

RFmxInstrMXLoadSParameterExternalAttenuationTableFromS2pFile Method

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int LoadSParameterExternalAttenuationTableFromS2pFile(
	string selectorString,
	string tableName,
	string s2pFilePath,
	RFmxInstrMXSParameterOrientation sParameterOrientation
)
```

```text
Public Function LoadSParameterExternalAttenuationTableFromS2pFile ( 
	selectorString As String,
	tableName As String,
	s2pFilePath As String,
	sParameterOrientation As RFmxInstrMXSParameterOrientation
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports method to get the valid port names. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all"
- **tableName String**
  - Specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table.
- **s2pFilePath String**
  - Specifies the path to the S2P file that contains S-parameter table information for the specified port.
- **sParameterOrientation RFmxInstrMXSParameterOrientation**
  - Specifies the orientation of the data in the S-parameter table relative to the port you specify.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/550378cf-b917-b5ee-58f4-2c68f5cf9aff.htm language=enus -->
## TOPIC 00050: rfmxinstrdotnet/html/550378cf-b917-b5ee-58f4-2c68f5cf9aff.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/550378cf-b917-b5ee-58f4-2c68f5cf9aff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/550378cf-b917-b5ee-58f4-2c68f5cf9aff.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetTriggerExportOutputTerminal Method

RFmxInstrMXSetTriggerExportOutputTerminal Method

Sets the destination terminal for the exported Reference Trigger. You can also choose not to export any signal.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerExportOutputTerminal(
	string channelName,
	string value
)
```

```text
Public Function SetTriggerExportOutputTerminal ( 
	channelName As String,
	value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value String**
  - Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal.

###### Return Value

Int32

##### Remarks

TriggerExportOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm language=enus -->
## TOPIC 00051: rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.LOSourceNone Field

RFmxInstrMXConstantsLOSourceNone Field

Specifies that no LO source is required to downconvert the RF input signal.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string LOSourceNone = "None"
```

```text
Public Const LOSourceNone As String = "None"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5a916224-5665-e0f6-9bde-ee82fc03d432.htm language=enus -->
## TOPIC 00052: rfmxinstrdotnet/html/5a916224-5665-e0f6-9bde-ee82fc03d432.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5a916224-5665-e0f6-9bde-ee82fc03d432.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5a916224-5665-e0f6-9bde-ee82fc03d432.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiTriggerLine5 Field

RFmxInstrMXConstantsPxiTriggerLine5 Field

The signal is exported to the PXI trigger line 5.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine5 = "PXI_Trig5"
```

```text
Public Const PxiTriggerLine5 As String = "PXI_Trig5"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5bc251b4-286f-ca9e-c525-2f10ee5ed8df.htm language=enus -->
## TOPIC 00053: rfmxinstrdotnet/html/5bc251b4-286f-ca9e-c525-2f10ee5ed8df.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5bc251b4-286f-ca9e-c525-2f10ee5ed8df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5bc251b4-286f-ca9e-c525-2f10ee5ed8df.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAdvanceTriggerDigitalEdgeSource Method

RFmxInstrMXSetAdvanceTriggerDigitalEdgeSource Method

Sets the source terminal for the advance trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAdvanceTriggerDigitalEdgeSource(
	string selectorString,
	string value
)
```

```text
Public Function SetAdvanceTriggerDigitalEdgeSource ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Specifies the source terminal for the advance trigger.

###### Return Value

Int32

##### Remarks

AdvanceTriggerDigitalEdgeSource

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5bf3e401-0d67-f22d-1d70-eaab5ff75139.htm language=enus -->
## TOPIC 00054: rfmxinstrdotnet/html/5bf3e401-0d67-f22d-1d70-eaab5ff75139.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5bf3e401-0d67-f22d-1d70-eaab5ff75139.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5bf3e401-0d67-f22d-1d70-eaab5ff75139.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.Pfi1 Field

RFmxInstrMXConstantsPfi1 Field

The signal is exported to the PXI 1.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string Pfi1 = "PFI1"
```

```text
Public Const Pfi1 As String = "PFI1"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5cc25af4-3f05-4f69-fba1-682c8df3c1ed.htm language=enus -->
## TOPIC 00055: rfmxinstrdotnet/html/5cc25af4-3f05-4f69-fba1-682c8df3c1ed.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5cc25af4-3f05-4f69-fba1-682c8df3c1ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5cc25af4-3f05-4f69-fba1-682c8df3c1ed.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiTriggerLine7 Field

RFmxInstrMXConstantsPxiTriggerLine7 Field

The signal is exported to the PXI trigger line 7.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine7 = "PXI_Trig7"
```

```text
Public Const PxiTriggerLine7 As String = "PXI_Trig7"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5d782514-9d7d-68f9-a6b1-7ac75a2e764a.htm language=enus -->
## TOPIC 00056: rfmxinstrdotnet/html/5d782514-9d7d-68f9-a6b1-7ac75a2e764a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5d782514-9d7d-68f9-a6b1-7ac75a2e764a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5d782514-9d7d-68f9-a6b1-7ac75a2e764a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLOExportEnabled Method

RFmxInstrMXSetLOExportEnabled Method

Sets whether to enable the LO OUT terminals on the installed devices.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLOExportEnabled(
	string channelName,
	bool value
)
```

```text
Public Function SetLOExportEnabled ( 
	channelName As String,
	value As Boolean
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the losource number and port number. Example: "port0" or "port0/losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value Boolean**
  - Specifies whether to enable the LO OUT terminals on the installed devices.

###### Return Value

Int32

##### Remarks

LOExportEnabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5dafaae7-c408-fdfe-2773-411df323d420.htm language=enus -->
## TOPIC 00057: rfmxinstrdotnet/html/5dafaae7-c408-fdfe-2773-411df323d420.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5dafaae7-c408-fdfe-2773-411df323d420.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5dafaae7-c408-fdfe-2773-411df323d420.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetEndOfRecordEventTerminalName Method

RFmxInstrMXGetEndOfRecordEventTerminalName Method

Gets the fully qualified signal name as a string.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEndOfRecordEventTerminalName(
	string selectorString,
	out string value
)
```

```text
Public Function GetEndOfRecordEventTerminalName ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the fully qualified signal name as a string.

###### Return Value

Int32

##### Remarks

EndOfRecordEventTerminalName

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm language=enus -->
## TOPIC 00058: rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX Constructor

RFmxInstrMX Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | RFmxInstrMX(IntPtr) | Creates a new RFmx session from an existing RFmx instrument handle. |
|  | RFmxInstrMX(String, String) | Creates an RFmx session to the device you specify through the resourceName parameter. Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| Note |  |  |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |  |  |
|  | RFmxInstrMX(String, String) | Creates an RFmx session to the device you specify through the resourceName parameter. Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| Note |  |  |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |  |  |

Top

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm language=enus -->
## TOPIC 00059: rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLO2ExportEnabled Method

RFmxInstrMXSetLO2ExportEnabled Method

Sets whether to enable the LO2 OUT terminals in the installed devices.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLO2ExportEnabled(
	string channelName,
	RFmxInstrMXLO2ExportEnabled value
)
```

```text
Public Function SetLO2ExportEnabled ( 
	channelName As String,
	value As RFmxInstrMXLO2ExportEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value RFmxInstrMXLO2ExportEnabled**
  - Specifies whether to enable the LO2 OUT terminals in the installed devices.

###### Return Value

Int32

##### Remarks

LO2ExportEnabled

Disabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/606143ec-e637-e700-cf97-1b6e1e4076e1.htm language=enus -->
## TOPIC 00060: rfmxinstrdotnet/html/606143ec-e637-e700-cf97-1b6e1e4076e1.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/606143ec-e637-e700-cf97-1b6e1e4076e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/606143ec-e637-e700-cf97-1b6e1e4076e1.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetFrequencyReferenceFrequency Method

RFmxInstrMXSetFrequencyReferenceFrequency Method

Sets the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyReferenceFrequency(
	string channelName,
	double value
)
```

```text
Public Function SetFrequencyReferenceFrequency ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Specifies the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

FrequencyReferenceFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/64850b64-c388-bb46-a1ca-6af3ceded53a.htm language=enus -->
## TOPIC 00061: rfmxinstrdotnet/html/64850b64-c388-bb46-a1ca-6af3ceded53a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/64850b64-c388-bb46-a1ca-6af3ceded53a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/64850b64-c388-bb46-a1ca-6af3ceded53a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetOspDelayEnabled Method

RFmxInstrMXSetOspDelayEnabled Method

Sets whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOspDelayEnabled(
	string channelName,
	RFmxInstrMXOspDelayEnabled value
)
```

```text
Public Function SetOspDelayEnabled ( 
	channelName As String,
	value As RFmxInstrMXOspDelayEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXOspDelayEnabled**
  - Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block.

###### Return Value

Int32

##### Remarks

OspDelayEnabled

Enabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6513f1b1-eee7-7db0-c533-17b7a6d2af51.htm language=enus -->
## TOPIC 00062: rfmxinstrdotnet/html/6513f1b1-eee7-7db0-c533-17b7a6d2af51.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6513f1b1-eee7-7db0-c533-17b7a6d2af51.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6513f1b1-eee7-7db0-c533-17b7a6d2af51.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFrequencySettlingUnits Method

RFmxInstrMXGetFrequencySettlingUnits Method

Gets the delay duration units and interpretation for LO settling.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencySettlingUnits(
	string channelName,
	out RFmxInstrMXFrequencySettlingUnits value
)
```

```text
Public Function GetFrequencySettlingUnits ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXFrequencySettlingUnits
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXFrequencySettlingUnits**
  - Upon return, contains the delay duration units and interpretation for LO settling.

###### Return Value

Int32

##### Remarks

FrequencySettlingUnits

Ppm

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6592ab73-7d3c-3b4f-903b-7d94c85260f2.htm language=enus -->
## TOPIC 00063: rfmxinstrdotnet/html/6592ab73-7d3c-3b4f-903b-7d94c85260f2.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6592ab73-7d3c-3b4f-903b-7d94c85260f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6592ab73-7d3c-3b4f-903b-7d94c85260f2.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXLO2ExportEnabled Enumeration

RFmxInstrMXLO2ExportEnabled Enumeration

Specifies whether to enable the LO2 OUT terminals in the installed devices.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXLO2ExportEnabled
```

```text
Public Enumeration RFmxInstrMXLO2ExportEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the LO2 OUT terminals. |
| Enabled | 1 | Enables the LO2 OUT terminals. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/66c08219-b810-dc87-fdec-604823e7b99e.htm language=enus -->
## TOPIC 00064: rfmxinstrdotnet/html/66c08219-b810-dc87-fdec-604823e7b99e.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/66c08219-b810-dc87-fdec-604823e7b99e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/66c08219-b810-dc87-fdec-604823e7b99e.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.LOSourceSecondary Field

RFmxInstrMXConstantsLOSourceSecondary Field

Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), PXIe-5832 with PXIe-5653 (LO1 stage only).

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string LOSourceSecondary = "Secondary"
```

```text
Public Const LOSourceSecondary As String = "Secondary"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/672cfe84-b068-2a34-7b27-1fda3510cd2a.htm language=enus -->
## TOPIC 00065: rfmxinstrdotnet/html/672cfe84-b068-2a34-7b27-1fda3510cd2a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/672cfe84-b068-2a34-7b27-1fda3510cd2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/672cfe84-b068-2a34-7b27-1fda3510cd2a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.NumberOfSignalConfigurations Property

RFmxInstrMXNumberOfSignalConfigurations Property

Gets the number of signal configurations created in the current session.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int NumberOfSignalConfigurations { get; }
```

```text
Public ReadOnly Property NumberOfSignalConfigurations As Integer
	Get
```

###### Property Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/675d4b81-099b-0de9-726f-8cfe32209f09.htm language=enus -->
## TOPIC 00066: rfmxinstrdotnet/html/675d4b81-099b-0de9-726f-8cfe32209f09.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/675d4b81-099b-0de9-726f-8cfe32209f09.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/675d4b81-099b-0de9-726f-8cfe32209f09.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetLOInjectionSide Method

RFmxInstrMXGetLOInjectionSide Method

Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLOInjectionSide(
	string channelName,
	out RFmxInstrMXLOInjectionSide value
)
```

```text
Public Function GetLOInjectionSide ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXLOInjectionSide
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXLOInjectionSide**
  - Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

LOInjectionSide

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/67908bde-b58a-aef5-a399-741fd77877cc.htm language=enus -->
## TOPIC 00067: rfmxinstrdotnet/html/67908bde-b58a-aef5-a399-741fd77877cc.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/67908bde-b58a-aef5-a399-741fd77877cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/67908bde-b58a-aef5-a399-741fd77877cc.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeString Method

RFmxInstrMXSetAttributeString Method

Sets the value of a String attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeString(
	string channelName,
	int attributeIdentifier,
	string value
)
```

```text
Public Function SetAttributeString ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value String**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/67c46214-7dd3-a8d1-7ab2-e8791a4c1594.htm language=enus -->
## TOPIC 00068: rfmxinstrdotnet/html/67c46214-7dd3-a8d1-7ab2-e8791a4c1594.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/67c46214-7dd3-a8d1-7ab2-e8791a4c1594.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/67c46214-7dd3-a8d1-7ab2-e8791a4c1594.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.BuildCalibrationPlaneString Method

RFmxInstrMXBuildCalibrationPlaneString Method

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildCalibrationPlaneString(
	string calibrationPlaneName
)
```

```text
Public Shared Function BuildCalibrationPlaneString ( 
	calibrationPlaneName As String
) As String
```

###### Parameters

- **calibrationPlaneName String**
  - Specifies the calibration plane name for building the selector string. This input accepts the calibration plane name with or without the "calplane::" prefix.

###### Return Value

String

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/69156124-1842-ba35-a693-5c4d20a388c1.htm language=enus -->
## TOPIC 00069: rfmxinstrdotnet/html/69156124-1842-ba35-a693-5c4d20a388c1.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/69156124-1842-ba35-a693-5c4d20a388c1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/69156124-1842-ba35-a693-5c4d20a388c1.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetStartTriggerType Method

RFmxInstrMXSetStartTriggerType Method

Sets whether the start trigger is a digital edge or a software trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStartTriggerType(
	string selectorString,
	RFmxInstrMXStartTriggerType value
)
```

```text
Public Function SetStartTriggerType ( 
	selectorString As String,
	value As RFmxInstrMXStartTriggerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value RFmxInstrMXStartTriggerType**
  - Specifies whether the start trigger is a digital edge or a software trigger.

###### Return Value

Int32

##### Remarks

StartTriggerType

None

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6978a661-7c69-3a1d-65aa-9841baf3728c.htm language=enus -->
## TOPIC 00070: rfmxinstrdotnet/html/6978a661-7c69-3a1d-65aa-9841baf3728c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6978a661-7c69-3a1d-65aa-9841baf3728c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6978a661-7c69-3a1d-65aa-9841baf3728c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

ISignalConfiguration.SignalConfigurationType Property

ISignalConfigurationSignalConfigurationType Property

Gets the type of the current signal configuration object.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
Type SignalConfigurationType { get; }
```

```text
ReadOnly Property SignalConfigurationType As Type
	Get
```

###### Property Value

Type

##### See Also

###### Reference

ISignalConfiguration Interface

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/699968c9-220b-6906-4b04-962bf9e99f75.htm language=enus -->
## TOPIC 00071: rfmxinstrdotnet/html/699968c9-220b-6906-4b04-962bf9e99f75.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/699968c9-220b-6906-4b04-962bf9e99f75.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/699968c9-220b-6906-4b04-962bf9e99f75.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXSParameterType Enumeration

RFmxInstrMXSParameterType Enumeration

Returns the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the selectorString input to specify the name of the Calplane and port to configure for s-parameter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXSParameterType
```

```text
Public Enumeration RFmxInstrMXSParameterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Scalar | 1 | De-embeds the measurement using the gain term. |
| Vector | 2 | De-embeds the measurement using the gain term and the reflection term. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6b503f98-6ceb-55d3-d78d-808309d1dba7.htm language=enus -->
## TOPIC 00072: rfmxinstrdotnet/html/6b503f98-6ceb-55d3-d78d-808309d1dba7.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6b503f98-6ceb-55d3-d78d-808309d1dba7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6b503f98-6ceb-55d3-d78d-808309d1dba7.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ConfigureMechanicalAttenuation Method

RFmxInstrMXConfigureMechanicalAttenuation Method

supporteddevices:

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMechanicalAttenuation(
	string channelName,
	RFmxInstrMXMechanicalAttenuationAuto mechanicalAttenuationAuto,
	double mechanicalAttenuationValue
)
```

```text
Public Function ConfigureMechanicalAttenuation ( 
	channelName As String,
	mechanicalAttenuationAuto As RFmxInstrMXMechanicalAttenuationAuto,
	mechanicalAttenuationValue As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Identifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter.
- **mechanicalAttenuationAuto RFmxInstrMXMechanicalAttenuationAuto**
  - Specifies whether RFmx automatically chooses an attenuation setting based on the hardware settings.
- **mechanicalAttenuationValue Double**
  - Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm language=enus -->
## TOPIC 00073: rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetInstrumentHandle Method

RFmxInstrMXGetInstrumentHandle Method

SafeHandle

RFmxInstrMX

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public SafeHandle GetInstrumentHandle()
```

```text
Public Function GetInstrumentHandle As SafeHandle
```

###### Return Value

SafeHandle

SafeHandle

RFmxInstrMX

##### Remarks

SafeHandle

IntPtr

IntPtr

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6ca4bdae-a97c-fc5f-bb86-9b335e0ea810.htm language=enus -->
## TOPIC 00074: rfmxinstrdotnet/html/6ca4bdae-a97c-fc5f-bb86-9b335e0ea810.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6ca4bdae-a97c-fc5f-bb86-9b335e0ea810.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6ca4bdae-a97c-fc5f-bb86-9b335e0ea810.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.ClockOut Field

RFmxInstrMXConstantsClockOut Field

Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string ClockOut = "ClkOut"
```

```text
Public Const ClockOut As String = "ClkOut"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm language=enus -->
## TOPIC 00075: rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLOOutPower Method

RFmxInstrMXSetLOOutPower Method

SetLOExportEnabled(String, Boolean)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLOOutPower(
	string channelName,
	double value
)
```

```text
Public Function SetLOOutPower ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(String, Boolean) method is set to TRUE. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

LOOutPower

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6d344bc4-da44-43e2-4cc7-aed1f96c41d8.htm language=enus -->
## TOPIC 00076: rfmxinstrdotnet/html/6d344bc4-da44-43e2-4cc7-aed1f96c41d8.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6d344bc4-da44-43e2-4cc7-aed1f96c41d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6d344bc4-da44-43e2-4cc7-aed1f96c41d8.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiStarLine Field

RFmxInstrMXConstantsPxiStarLine Field

The signal is exported to the PXI star trigger line.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiStarLine = "PXI_STAR"
```

```text
Public Const PxiStarLine As String = "PXI_STAR"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6d3c79db-4a78-b8fd-7060-b40e88928bb5.htm language=enus -->
## TOPIC 00077: rfmxinstrdotnet/html/6d3c79db-4a78-b8fd-7060-b40e88928bb5.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6d3c79db-4a78-b8fd-7060-b40e88928bb5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6d3c79db-4a78-b8fd-7060-b40e88928bb5.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetReadyForReferenceEventOutputTerminal Method

RFmxInstrMXGetReadyForReferenceEventOutputTerminal Method

Gets the destination terminal for the Ready for Reference event.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReadyForReferenceEventOutputTerminal(
	string selectorString,
	out string value
)
```

```text
Public Function GetReadyForReferenceEventOutputTerminal ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the destination terminal for the Ready for Reference event.

###### Return Value

Int32

##### Remarks

ReadyForReferenceEventOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6e7950d9-e98a-c2eb-688e-8bc7857f066b.htm language=enus -->
## TOPIC 00078: rfmxinstrdotnet/html/6e7950d9-e98a-c2eb-688e-8bc7857f066b.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6e7950d9-e98a-c2eb-688e-8bc7857f066b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6e7950d9-e98a-c2eb-688e-8bc7857f066b.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetDoneEventOutputTerminal Method

RFmxInstrMXGetDoneEventOutputTerminal Method

Gets the destination terminal for the Done event.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDoneEventOutputTerminal(
	string selectorString,
	out string value
)
```

```text
Public Function GetDoneEventOutputTerminal ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the destination terminal for the Done event.

###### Return Value

Int32

##### Remarks

DoneEventOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6ed29c47-42f1-16ee-3536-0ffe35fd3527.htm language=enus -->
## TOPIC 00079: rfmxinstrdotnet/html/6ed29c47-42f1-16ee-3536-0ffe35fd3527.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6ed29c47-42f1-16ee-3536-0ffe35fd3527.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6ed29c47-42f1-16ee-3536-0ffe35fd3527.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeDouble Method

RFmxInstrMXSetAttributeDouble Method

Sets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeDouble(
	string channelName,
	int attributeIdentifier,
	double value
)
```

```text
Public Function SetAttributeDouble ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Double**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6f897760-cc3f-a0ec-ed35-0699065189d8.htm language=enus -->
## TOPIC 00080: rfmxinstrdotnet/html/6f897760-cc3f-a0ec-ed35-0699065189d8.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6f897760-cc3f-a0ec-ed35-0699065189d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6f897760-cc3f-a0ec-ed35-0699065189d8.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeUShort Method

RFmxInstrMXSetAttributeUShort Method

Sets the value of a UShort attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeUShort(
	string channelName,
	int attributeIdentifier,
	ushort value
)
```

```text
Public Function SetAttributeUShort ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As UShort
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value UInt16**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6fc74f59-5abf-a4b2-2a68-41081268c940.htm language=enus -->
## TOPIC 00081: rfmxinstrdotnet/html/6fc74f59-5abf-a4b2-2a68-41081268c940.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6fc74f59-5abf-a4b2-2a68-41081268c940.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6fc74f59-5abf-a4b2-2a68-41081268c940.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSession(String, String) Method

RFmxInstrMXGetSession(String, String) Method

Gets a session, if it exists for given resource name; else, returns a new one.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxInstrMX GetSession(
	string resourceName,
	string optionString
)
```

```text
Public Shared Function GetSession ( 
	resourceName As String,
	optionString As String
) As RFmxInstrMX
```

###### Parameters

- **resourceName String**
  - Specifies the resource name of the device to initialize.
- **optionString String**
  - Sets the initial value of certain properties for the session.The following attributes are used in this parameter: RFmxSetup,Simulate,AnalysisOnly. To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1 You can set the Digitizerfield to 5622_25MHz_DDC only when using the NI 5665. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. To set multiple attributes, separate their assignments with a comma.

###### Return Value

RFmxInstrMX

##### See Also

###### Reference

RFmxInstrMX Class

GetSession Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/6fe7b90b-2e7b-ee7e-cd27-4ce26b2b3046.htm language=enus -->
## TOPIC 00082: rfmxinstrdotnet/html/6fe7b90b-2e7b-ee7e-cd27-4ce26b2b3046.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/6fe7b90b-2e7b-ee7e-cd27-4ce26b2b3046.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/6fe7b90b-2e7b-ee7e-cd27-4ce26b2b3046.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRecommendedIQPreTriggerTime Method

RFmxInstrMXGetRecommendedIQPreTriggerTime Method

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRecommendedIQPreTriggerTime(
	string channelName,
	out double value
)
```

```text
Public Function GetRecommendedIQPreTriggerTime ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the recommended pretrigger time for I/Q acquisition, in seconds.

###### Return Value

Int32

##### Remarks

RecommendedIQPreTriggerTime

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/71734aa2-2cf0-9e9c-7600-1b1e1435f9e3.htm language=enus -->
## TOPIC 00083: rfmxinstrdotnet/html/71734aa2-2cf0-9e9c-7600-1b1e1435f9e3.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/71734aa2-2cf0-9e9c-7600-1b1e1435f9e3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/71734aa2-2cf0-9e9c-7600-1b1e1435f9e3.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeUInt Method

RFmxInstrMXGetAttributeUInt Method

Gets the value of a uint attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeUInt(
	string channelName,
	int attributeIdentifier,
	out uint value
)
```

```text
Public Function GetAttributeUInt ( 
	channelName As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As UInteger
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value UInt32**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7175fe7c-eea8-64cf-5262-3540c245a199.htm language=enus -->
## TOPIC 00084: rfmxinstrdotnet/html/7175fe7c-eea8-64cf-5262-3540c245a199.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7175fe7c-eea8-64cf-5262-3540c245a199.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7175fe7c-eea8-64cf-5262-3540c245a199.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetDownconverterPreselectorEnabled Method

RFmxInstrMXGetDownconverterPreselectorEnabled Method

Gets whether the tunable preselector is enabled on the downconverter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDownconverterPreselectorEnabled(
	string channelName,
	out RFmxInstrMXDownconverterPreselectorEnabled value
)
```

```text
Public Function GetDownconverterPreselectorEnabled ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXDownconverterPreselectorEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXDownconverterPreselectorEnabled**
  - Upon return, contains whether the tunable preselector is enabled on the downconverter.

###### Return Value

Int32

##### Remarks

DownconverterPreselectorEnabled

Disabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/736c6476-e5c4-3b4c-e57f-54a758105689.htm language=enus -->
## TOPIC 00085: rfmxinstrdotnet/html/736c6476-e5c4-3b4c-e57f-54a758105689.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/736c6476-e5c4-3b4c-e57f-54a758105689.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/736c6476-e5c4-3b4c-e57f-54a758105689.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeBool Method

RFmxInstrMXSetAttributeBool Method

Sets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeBool(
	string channelName,
	int attributeIdentifier,
	bool value
)
```

```text
Public Function SetAttributeBool ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Boolean
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Boolean**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/745120f3-a387-8991-055e-39be283c3d78.htm language=enus -->
## TOPIC 00086: rfmxinstrdotnet/html/745120f3-a387-8991-055e-39be283c3d78.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/745120f3-a387-8991-055e-39be283c3d78.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/745120f3-a387-8991-055e-39be283c3d78.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX Methods

RFmxInstrMX Methods

The [RFmxInstrMX](4e32fd9b-7d12-3d27-1c6a-2980762699f8.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BuildCalibrationPlaneString | Creates the selector string to use with External Attenuation Table methods. |
|  | BuildInstrumentString | Creates the instrument string to use as the Selector String for reading the recommended settings. |
|  | BuildLOString | Creates the LO string to use as the selector string for LO related methods. |
|  | BuildModuleString | Configures the Module string to use as the Selector String for reading temperature of specific modules of the device. |
|  | BuildPortString2 | Creates the port string to use as the selector string with External Attenuation Table methods. On a MIMO session, this method can be used to build port string to use as a selector string for configuring or reading port-specific methods and external attenuation table methods. |
|  | CheckAcquisitionStatus | Checks the status of the acquisition. Use this method to check for any errors that may occur during acquisition, or to check whether RFmx has completed the acquisition operation. |
|  | CheckIfListExists | Returns whether the list you specify in the listname parameter exists, and also returns the corresponding personality of the list, if the list exists. This method does not support an empty ("") list name. |
|  | CheckIfSignalExists | Returns whether the signal you specify in the signalname parameter exists, and also returns the corresponding personality of the signal, if the signal exists. This method does not support an empty ("") signal name. |
|  | Close | Closes the RFmx session. |
|  | ConfigureExternalAttenuationInterpolationLinear | Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this method performs a linear interpolation based on the entries above and below the row in the table. Currently interpolation is supported only for S-parameter tables. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | ConfigureExternalAttenuationInterpolationNearest | Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used. Currently interpolation is supported only for S-parameter tables. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5860 |
|  | ConfigureExternalAttenuationInterpolationSpline | Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this method performs a spline interpolation based on the entries above and below the row in the table. Currently interpolation is supported only for S-parameter tables. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | ConfigureExternalAttenuationTable | Stores the external attenuation table in the calibration plane specified by the selectorString parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. If there is only one table configured in any calibration plane, it is automatically selected as the active table.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | ConfigureFrequencyReference | Configures the Reference Clock and the frequency reference source. |
|  | ConfigureMechanicalAttenuation | Configures the mechanical attenuation and RFmx attenuation hardware settings.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668 |
|  | ConfigureRFAttenuation | Configures the nominal attenuation and RFmx setting. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668 |
|  | ConfigureSParameterExternalAttenuationTable | Stores the S-parameter table in the calibration plane specified by the selectorString parameter. On a MIMO session the S-parameter table is stored for each MIMO port in the specified calibration plane.supporteddevices: PXIe-5830/5831/5832/5840/5841/5842/5860 If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
|  | ConfigureSParameterExternalAttenuationType | Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. supporteddevices: PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | DangerousGetNIRfsaHandle | Returns the value of the underlying instrument handle. Note Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |
| Note |  |  |
| Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |  |  |
|  | DangerousGetNIRfsaHandleArray | Returns list of underlying instrument handles. Note Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |
| Note |  |  |
| Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |  |  |
|  | DeleteAllExternalAttenuationTables | Deletes all the external attenuation tables in the calibration plane specified by the selectorString parameter. On a MIMO session, this method deletes all the external attenuation tables for the specified MIMO port. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | DeleteExternalAttenuationTable | Deletes the external attenuation table set by the tableName parameter in the calibration plane specified by the selectorString parameter. On a MIMO session, this method selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | DisableCalibrationPlane | Disables the calibration plane specified by the selectorString parameter for amplitude correction.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | EnableCalibrationPlane | Enables the calibration plane specified by the selectorString parameter for amplitude correction.supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | ExportSignal | Routes signals (triggers, clocks, and events) to the specified output terminal. This method is not supported on a MIMO session. |
|  | FetchRawIQData | Fetches I/Q data from a single record in an acquisition. |
|  | ForceClose | Closes all RFmx sessions. Calling this method once will destroy the session, irrespective of the many references obtained for the session for a particular resource name. |
|  | GetAdvanceTriggerDigitalEdgeSource | Gets the source terminal for the advance trigger. |
|  | GetAdvanceTriggerExportOutputTerminal | Gets the destination terminal for the exported advance trigger. |
|  | GetAdvanceTriggerTerminalName | Gets the fully qualified signal name as a string. |
|  | GetAdvanceTriggerType | Gets whether the advance trigger is a digital edge or a software trigger. |
|  | GetAmplitudeSettling | Gets the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate function. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeByte | Gets the value of a Byte attribute. |
|  | GetAttributeByteArray | Gets the value of a byte array attribute. |
|  | GetAttributeComplexDoubleArray | Gets the value of a ComplexDouble array attribute. |
|  | GetAttributeComplexSingleArray | Gets the value of a ComplexSingle array attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeDoubleArray | Gets the value of a double array attribute. |
|  | GetAttributeFloat | Gets the value of a Float attribute. |
|  | GetAttributeFloatArray | Gets the value of a float array attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeIntArray | Gets the value of a int array attribute. |
|  | GetAttributeLong | Gets the value of an RFmx 64-bit integer (int64) attribute. |
|  | GetAttributeLongArray | Gets the value of a long array attribute. |
|  | GetAttributeSByte | Gets the value of a SByte attribute. |
|  | GetAttributeSByteArray | Gets the value of a sbyte array attribute. |
|  | GetAttributeShort | Gets the value of a Short attribute. |
|  | GetAttributeString | Gets the value of a string attribute. |
|  | GetAttributeUInt | Gets the value of a uint attribute. |
|  | GetAttributeUIntArray | Gets the value of a uint array attribute. |
|  | GetAttributeULongArray | Gets the value of a ulong array attribute. |
|  | GetAttributeUShort | Gets the value of a UShort attribute. |
|  | GetAvailablePaths | Gets paths available for the session. On a MIMO session, this method fetches all the paths for the initialized MIMO paths. |
|  | GetAvailablePorts(String) | Obsolete. Gets the list of ports available for use based on your instrument configuration. |
|  | GetAvailablePorts(String, String) | Gets ports available for the session. On a MIMO session, this method fetches all the ports for the initialized MIMO ports. |
|  | GetChannelCoupling | Gets whether the RF IN connector is AC- or DC-coupled on the downconverter. |
|  | GetCleanerSpectrum | Gets how to obtain the lowest noise floor or faster measurement speed. |
|  | GetCommonModeLevel | Gets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. |
|  | GetDeviceTemperature | Gets the current temperature of the module. This value is expressed in degrees Celsius. |
|  | GetDigitalGain | Gets the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. |
|  | GetDigitizerDitherEnabled | Gets whether dithering is enabled on the digitizer. |
|  | GetDigitizerTemperature | Gets the current temperature of the digitizer module. This value is expressed in degrees Celsius. |
|  | GetDoneEventOutputTerminal | Gets the destination terminal for the Done event. |
|  | GetDoneEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetDownconverterCenterFrequency | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | GetDownconverterFrequencyOffset | Gets an offset from the center frequency value for the downconverter. Use this method to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this method to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. |
|  | GetDownconverterGain | Gets the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this method. |
|  | GetDownconverterPreselectorEnabled | Gets whether the tunable preselector is enabled on the downconverter. |
|  | GetEndOfRecordEventOutputTerminal | Gets the destination terminal for the End of Record event. |
|  | GetEndOfRecordEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetErrorString | Converts the status code returned by an RFmxInstr function into a string. |
|  | GetExternalAttenuationTableActualValue | Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane. |
|  | GetFftWidth | Gets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. |
|  | GetFrequencyReferenceExportedTerminal | Gets a comma-separated list of the terminals at which to export the frequency reference. |
|  | GetFrequencyReferenceFrequency | Gets the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz. |
|  | GetFrequencyReferenceSource | Gets the frequency reference source. |
|  | GetFrequencySettling | Gets the value used for LO frequency settling. |
|  | GetFrequencySettlingUnits | Gets the delay duration units and interpretation for LO settling. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIFFilterBandwidth | Gets the IF filter path bandwidth for your device configuration. |
|  | GetIFOutputPowerLevelOffset | Gets the power offset by which to adjust the default IF output power level. This value is expressed in dB. |
|  | GetInputIsolationEnabled | Gets whether input isolation is enabled. |
|  | GetInstrumentFirmwareRevision | Gets a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. |
|  | GetInstrumentHandle | Gets the SafeHandle to the RFmxInstrMX instrument session. |
|  | GetInstrumentModel | Gets a string that contains the model number or name of the RF device that you are currently using. |
|  | GetListNames | Returns the list names and the corresponding selected personality type from the personalityFilter parameter. When you set the personalityFilter parameter to all, this function returns the available list names for all supported personalities. |
|  | GetLO2ExportEnabled | Gets whether to enable the LO2 OUT terminals in the installed devices. |
|  | GetLoadOptions | Specifies the configurations to skip while loading from a file using the LoadConfigurations(String) method |
|  | GetLOExportEnabled | Gets whether to enable the LO OUT terminals on the installed devices. |
|  | GetLOFrequency | Gets the LO signal frequency for the configured center frequency. This value is expressed in Hz. |
|  | GetLOFrequencyStepSize | Gets the step size for tuning the LO phase-locked loop (PLL). |
|  | GetLOInjectionSide | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | GetLOInPower | Gets the power level expected at the LO IN terminal when the SetLOSource(String, String) method is set to RFMXINSTR_VAL_LO_SOURCE_LO_IN. This value is expressed in dBm. |
|  | GetLOLeakageAvoidanceEnabled | Gets whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. |
|  | GetLOOutPower | Gets the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(String, Boolean) method is set to TRUE. This value is expressed in dBm. |
|  | GetLOPllFractionalMode | Gets whether to use fractional mode for the LO phase-locked loop (PLL). |
|  | GetLOSharingMode | Gets the RFmx session with the respective LO sharing mode. |
|  | GetLOSource | Gets the LO signal source used to downconvert the RF input signal. |
|  | GetLOTemperature | Gets the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. |
|  | GetLOVcoFrequencyStepSize | Gets the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. |
|  | GetMechanicalAttenuationAuto | Gets whether RFmx chooses an attenuation setting based on the hardware settings. |
|  | GetMechanicalAttenuationValue | Gets the level of mechanical attenuation for the RF path. This value is expressed in dB. |
|  | GetMixerLevel | Gets the mixer level, in dBm. |
|  | GetMixerLevelOffset | Gets the number of dB by which to adjust the device mixer level. |
|  | GetModuleRevision | Gets the revision of the RF downconverter module. |
|  | GetNumberOfLOSharingGroups | Gets the RFmx session with the number of LO sharing groups. |
|  | GetNumberOfRawIQRecords | Gets the number of raw IQ records to acquire to complete measurement averaging. |
|  | GetOptimizePathForSignalBandwidth | Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. |
|  | GetOspDelayEnabled | Gets whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. |
|  | GetOverflowErrorReporting | Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. |
|  | GetPhaseOffset | Gets the offset to apply to the initial I and Q phases. |
|  | GetPreampEnabled | Gets whether the RF preamplifier is enabled in the system. |
|  | GetPreselectorPresent | Indicates whether a preselector is available on the RF downconverter module. |
|  | GetReadyForAdvanceEventOutputTerminal | Gets the destination terminal for the Ready for Advance event. |
|  | GetReadyForAdvanceEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetReadyForReferenceEventOutputTerminal | Gets the destination terminal for the Ready for Reference event. |
|  | GetReadyForReferenceEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetReadyForStartEventOutputTerminal | Gets the destination terminal for the Ready for Start event. |
|  | GetReadyForStartEventTerminalName | Gets the fully qualified signal name as a string. |
|  | GetRecommendedAcquisitionType | Gets the recommended acquisition type for the last committed measurement configuration. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedCenterFrequency | Gets the recommended center frequency of the RF signal. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedIQAcquisitionTime | Gets the recommended acquisition time for I/Q acquisition, in seconds. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedIQMinimumSampleRate | Gets the recommended minimum sample rate for I/Q acquisition, in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedIQPreTriggerTime | Gets the recommended pretrigger time for I/Q acquisition, in seconds. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedNumberOfRecords | Gets the recommended number of records to acquire to complete measurement averaging. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedSpectralAcquisitionSpan | Gets the recommended acquisition span for spectral acquisition, in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedSpectralFftWindow | Gets the recommended FFT window type for spectral acquisition. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedSpectralResolutionBandwidth | Gets the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRecommendedTriggerMinimumQuietTime | Gets the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds. This method is supported when 1. RFmxInstrMX(String, String) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(String, String) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this method. |
|  | GetRFAttenuationAuto | Gets whether RFmx computes the RF attenuation. |
|  | GetRFAttenuationStepSize | Gets the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. |
|  | GetRFAttenuationValue | Gets the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. |
|  | GetRFHighpassFilterFrequency | Gets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | GetRFPreampPresent | Indicates whether an RF preamplifier is available on the RF downconverter module. |
|  | GetSelfCalibrateLastDateAndTime | Gets the date and time of the last successful self-calibration. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Note For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |
| Note |  |  |
| For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |  |  |
|  | GetSelfCalibrateLastTemperature | Gets the temperature of the last successful self-calibration. This value is expresed in degree Celsius. On a MIMO session, use the selectorString parameter to get the last successful self-calibration temperature for a specific MIMO port. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860 Note For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |
| Note |  |  |
| For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |  |  |
|  | GetSelfCalibrationValidityCheck | Gets whether RFmx validates the self-calibration data. |
|  | GetSelfCalibrationValidityCheckTimeInterval | Gets the minimum time between two self calibration validity checks. This value is expressed in seconds. |
|  | GetSerialNumber | Gets the serial number of the RF downconverter module. |
|  | GetSession(String, String) | Gets a session, if it exists for given resource name; else, returns a new one. |
|  | GetSession(String, String) | Gets a session, if it exists for given set of resource name; else, returns a new one. |
|  | GetSession(String, String, Boolean) | Gets a session, if it exists for given resource name; else, returns a new one. |
|  | GetSession(String, String, Boolean) | Gets a session, if it exists for given set of resource name; else, returns a new one. |
|  | GetSessionFromNIRfsaHandle | Gets a session, if it exists for given NIRfsa instrument handle; else, returns a new one. Note1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |
| Note |  |  |
| 1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |  |  |
|  | GetSessionFromNIRfsaHandles | Gets a session, if it exists for given set of NIRfsa instrument handle; else, returns a new one. Note1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |
| Note |  |  |
| 1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |  |  |
|  | GetSignalConfigurationNames | Returns the signal names and corresponding personality type, for the personality type selected in the personalityFilter parameter. |
|  | GetSmuChannel | Gets the output channel to be used for noise figure (NF) measurement in RFmx. |
|  | GetSmuResourceName | Gets the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name. |
|  | GetSParameterExternalAttenuationType | Returns the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the selectorString input to specify the name of the Calplane and port to configure for s-parameter. Supported devices: PXIe-5830/5831/5832/5840 |
|  | GetStartTriggerDigitalEdge | Gets the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | GetStartTriggerDigitalEdgeSource | Gets the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | GetStartTriggerExportOutputTerminal | Gets the destination terminal for the exported start trigger. |
|  | GetStartTriggerTerminalName | Gets the fully qualified signal name as a string. |
|  | GetStartTriggerType | Gets whether the start trigger is a digital edge or a software trigger. |
|  | GetSubSpanOverlap | Gets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | GetTemperatureReadInterval | Gets the minimum time difference between temperature sensor readings. This value is expressed in seconds. |
|  | GetThermalCorrectionHeadroomRange | Gets the expected thermal operating range of the instrument from the self-calibration temperature returned from the GetDeviceTemperature(String, Double) method. This value is expressed in degree Celsius. |
|  | GetThermalCorrectionTemperatureResolution | Gets the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. |
|  | GetTriggerExportOutputTerminal | Gets the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. |
|  | GetTriggerTerminalName | Gets the fully-qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/RefTrigger, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/RefTrigger, where BasebandModule is the name of your device in MAX. PXIe-5860: /ModuleName/ai/ChannelNumber/RefTrigger,, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). All other devices: /DigitizerName/RefTrigger, where DigitizerName is the name of your associated digitizer module in MAX. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | GetTuningSpeed | Makes tradeoffs between tuning speed and phase noise. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetWarning | Gets the latest warning code and description. |
|  | IsSelfCalibrateValid | Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the validSteps parameter to the stepsToOmit parameter of the SelfCalibrate(String, RFmxInstrMXSelfCalibrateSteps) method. On a MIMO session use the selectorString parameter to get the self-calibration validity for a specific MIMO port.supporteddevices: PXIe-5663/5663E/5665/5668 |
|  | LoadConfigurations | Loads the methods of an RFmx session saved in a file. This file can be generated using SaveAllConfigurations(String) method or the RF Signal Analyzer panel in InstrumentStudio. You can specify the configurations to skip while loading from a file using the LoadOptions property. If the file contains a named signal configuration which is already present in the session, then this method will return an error. It is recommended to call the RFmxInstr Reset Entire Session method to delete all the named signal configurations in the session. |
|  | LoadSParameterExternalAttenuationTableFromS2pFile | Stores the S-parameter table from the S2P file in the calibration plane specified by the selectorString parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session the S-parameter table is stored for each MIMO port in the specified calibration plane.supporteddevices: PXIe-5830/5831/5832/5840/5841/5842/5860 If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetDriver | Restores the NI-RFSA driver state to a default state to avoid RFmx using any hardware or driver state that was set by the RF toolkits or other custom NI-RFSA code. Use this method when you switch back to using RFmx to perform measurements after you have used the NI-RFSA handle to perform measurements with RF toolkits or you have used other custom NI-RFSA code. Unlike the ResetToDefault method, the RfmxInstr Reset Driver method does not reset RFmx methods configured on the RFmx session. Hence, you do not need to set RFmx methods again when switching back to RFmx measurements. Refer to RFmx SpecAn CHP - WCDMA ModAcc - CHP Example (LabVIEW) on ni.com for more information about using RFmx to perform measurements. |
|  | ResetEntireSession | Deletes all the named signal configurations in the session and resets all methods for the default signal instances of already loaded personalities in the session. This method disables all the calibration planes. |
|  | ResetToDefault | Resets the RFmxInstr methods to their default values. This method disables all the calibration planes. |
|  | SaveAllConfigurations | Saves all the configured methods in the RFmx session to a file in the specified file path. Use this method to save the current state of the RFmx session. On a MIMO session, this method saves all the configured methods for the specified MIMO port. List configurations, reference waveforms and external attenuation tables are not saved by this method. |
|  | SelectActiveExternalAttenuationTable | Activates the external attenuation table set by the tableName parameter in the calibration plane specified by the selectorString parameter. On a MIMO session, this method selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement. supporteddevices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 |
|  | SelfCalibrate | Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this method self-calibrates all NI-RFSA devices and associated modules that support self-calibration. Refer to the specifications document for your device for more information about how often to self-calibrate. For more information about Self Calibrate, refer to the niRFSA Self Cal method topic for your device in the NI RF Vector Signal Analyzers Help. For PXIe-5644/5645/5646, RFmx internally closes the RFSA session, performs self-calibration and opens a new session for the same device. If the RFSA session has been accessed from RFmx, using the RFmxInstr Get NIRFSA Session method before calling the RFmxInstr Self Calibrate method, the RFSA session will become invalid upon calling the RFmxInstr Self Calibrate. supporteddevices: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SelfCalibrateRange | Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this method runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the niRFSA Self Calibrate Range method topic for your device in the NI RF Vector Signal Analyzers Help. On a MIMO session, this method self-calibrates all NI-RFSA devices and associated modules that support self-calibration.supporteddevices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 This method does not update self-calibration date and temperature. Self-calibration range data is not saved to your device if you restart the system. |
|  | SendSoftwareEdgeAdvanceTrigger | Sends a trigger to the waiting device when you choose a software version of the Advance trigger. You can also use this method to override a hardware trigger. This method returns an error if: You configure an invalid trigger. You have not previously called the RFmx Initiate method.supporteddevices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SendSoftwareEdgeStartTrigger | Sends a trigger to the waiting device when you choose a software version of Start trigger. You can also use this method to override a hardware trigger. This method returns an error if: You configure an invalid trigger. You have not previously called the RFmx Initiate method.supporteddevices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SetAdvanceTriggerDigitalEdgeSource | Sets the source terminal for the advance trigger. |
|  | SetAdvanceTriggerExportOutputTerminal | Sets the destination terminal for the exported advance trigger. |
|  | SetAdvanceTriggerType | Sets whether the advance trigger is a digital edge or a software trigger. |
|  | SetAmplitudeSettling | Sets the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate method. Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value. Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeByte | Sets the value of a Byte attribute. |
|  | SetAttributeByteArray | Sets the value of a byte array attribute. |
|  | SetAttributeComplexDoubleArray | Sets the value of a ComplexDouble array attribute. |
|  | SetAttributeComplexSingleArray | Sets the value of a ComplexSingle array attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeDoubleArray | Sets the value of a double array attribute. |
|  | SetAttributeFloat | Sets the value of a Float attribute. |
|  | SetAttributeFloatArray | Sets the value of a float array attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeIntArray | Sets the value of a int array attribute. |
|  | SetAttributeLong | Sets the value of a Long attribute. |
|  | SetAttributeLongArray | Sets the value of a long array attribute. |
|  | SetAttributeSByte | Sets the value of a SByte attribute. |
|  | SetAttributeSByteArray | Sets the value of a sbyte array attribute. |
|  | SetAttributeShort | Sets the value of a Short attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAttributeUInt | Sets the value of a UInt attribute. |
|  | SetAttributeUIntArray | Sets the value of a uint array attribute. |
|  | SetAttributeULongArray | Sets the value of a ulong array attribute. |
|  | SetAttributeUShort | Sets the value of a UShort attribute. |
|  | SetChannelCoupling | Sets whether the RF IN connector is AC- or DC-coupled on the downconverter. |
|  | SetCleanerSpectrum | Sets how to obtain the lowest noise floor or faster measurement speed. |
|  | SetCommonModeLevel | Sets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. |
|  | SetDigitalGain | Sets the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. |
|  | SetDigitizerDitherEnabled | Sets whether dithering is enabled on the digitizer. |
|  | SetDoneEventOutputTerminal | Sets the destination terminal for the Done event. |
|  | SetDownconverterCenterFrequency | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | SetDownconverterFrequencyOffset | Sets an offset from the center frequency value for the downconverter. Use this method to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this method to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. |
|  | SetDownconverterPreselectorEnabled | Sets whether the tunable preselector is enabled on the downconverter. |
|  | SetEndOfRecordEventOutputTerminal | Sets the destination terminal for the End of Record event. |
|  | SetFftWidth | Sets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. |
|  | SetFrequencyReferenceExportedTerminal | Sets a comma-separated list of the terminals at which to export the frequency reference. |
|  | SetFrequencyReferenceFrequency | Sets the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz. |
|  | SetFrequencyReferenceSource | Sets the frequency reference source. |
|  | SetFrequencySettling | Sets the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the SetFrequencySettlingUnits(String, RFmxInstrMXFrequencySettlingUnits) method. Note This method is not supported if you are using an external LO. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 |
| Note |  |  |
| This method is not supported if you are using an external LO. |  |  |
|  | SetFrequencySettlingUnits | Gets the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the SetFrequencySettlingUnits(String, RFmxInstrMXFrequencySettlingUnits) method. Note This method is not supported if you are using an external LO. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 |
| Note |  |  |
| This method is not supported if you are using an external LO. |  |  |
|  | SetIFFilterBandwidth | Sets the IF filter path bandwidth for your device configuration. |
|  | SetIFOutputPowerLevelOffset | Sets the power offset by which to adjust the default IF output power level. This value is expressed in dB. |
|  | SetInputIsolationEnabled | Sets whether input isolation is enabled. |
|  | SetLO2ExportEnabled | Sets whether to enable the LO2 OUT terminals in the installed devices. |
|  | SetLoadOptions | Specifies the configurations to skip while loading from a file using the LoadConfigurations(String) method |
|  | SetLOExportEnabled | Sets whether to enable the LO OUT terminals on the installed devices. |
|  | SetLOFrequency | Sets the LO signal frequency for the configured center frequency. This value is expressed in Hz. |
|  | SetLOFrequencyStepSize | Sets the step size for tuning the LO phase-locked loop (PLL). |
|  | SetLOInjectionSide | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
|  | SetLOInPower | Sets the power level expected at the LO IN terminal when the SetLOSource(String, String) method is set to RFMXINSTR_VAL_LO_SOURCE_LO_IN. This value is expressed in dBm. |
|  | SetLOLeakageAvoidanceEnabled | Sets whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. |
|  | SetLOOutPower | Sets the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(String, Boolean) method is set to TRUE. This value is expressed in dBm. |
|  | SetLOPllFractionalMode | Sets whether to use fractional mode for the LO phase-locked loop (PLL). |
|  | SetLOSharingMode | Sets the RFmx session with the respective LO sharing mode. |
|  | SetLOSource | Sets the LO signal source used to downconvert the RF input signal. |
|  | SetLOVcoFrequencyStepSize | Sets the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. |
|  | SetMechanicalAttenuationAuto | Sets whether RFmx chooses an attenuation setting based on the hardware settings. |
|  | SetMechanicalAttenuationValue | Sets the level of mechanical attenuation for the RF path. This value is expressed in dB. |
|  | SetMixerLevel | Sets the mixer level, in dBm. |
|  | SetMixerLevelOffset | Sets the number of dB by which to adjust the device mixer level. |
|  | SetNumberOfLOSharingGroups | Sets the RFmx session with the number of LO sharing groups. |
|  | SetOptimizePathForSignalBandwidth | Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. |
|  | SetOspDelayEnabled | Sets whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. |
|  | SetOverflowErrorReporting | Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. |
|  | SetPhaseOffset | Sets the offset to apply to the initial I and Q phases. |
|  | SetPreampEnabled | Sets whether the RF preamplifier is enabled in the system. |
|  | SetReadyForAdvanceEventOutputTerminal | Sets the destination terminal for the Ready for Advance event. |
|  | SetReadyForReferenceEventOutputTerminal | Sets the destination terminal for the Ready for Reference event. |
|  | SetReadyForStartEventOutputTerminal | Sets the destination terminal for the Ready for Start event. |
|  | SetRFAttenuationAuto | Sets whether RFmx computes the RF attenuation. |
|  | SetRFAttenuationStepSize | Sets the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. |
|  | SetRFAttenuationValue | Sets the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. |
|  | SetRFHighpassFilterFrequency | Sets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | SetSelfCalibrationValidityCheck | Sets whether RFmx validates the self-calibration data. |
|  | SetSelfCalibrationValidityCheckTimeInterval | Sets the minimum time between two self calibration validity checks. This value is expressed in seconds. |
|  | SetSmuChannel | Sets the output channel to be used for noise figure (NF) measurement in RFmx. |
|  | SetSmuResourceName | Sets the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name. |
|  | SetStartTriggerDigitalEdge | Sets the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | SetStartTriggerDigitalEdgeSource | Sets the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
|  | SetStartTriggerExportOutputTerminal | Sets the destination terminal for the exported start trigger. |
|  | SetStartTriggerType | Sets whether the start trigger is a digital edge or a software trigger. |
|  | SetSubSpanOverlap | Sets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
|  | SetTemperatureReadInterval | Sets the minimum time difference between temperature sensor readings. This value is expressed in seconds. |
|  | SetThermalCorrectionHeadroomRange | Sets the expected thermal operating range of the instrument from the self-calibration temperature returned from the GetDeviceTemperature(String, Double) method. This value is expressed in degree Celsius. |
|  | SetThermalCorrectionTemperatureResolution | Sets the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. |
|  | SetTriggerExportOutputTerminal | Sets the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. |
|  | SetTuningSpeed | Makes tradeoffs between tuning speed and phase noise. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |
|  | WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is complete. This method is typically called after a specific initiate method. |

Top

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/74d0d1b7-6fe4-be58-60b8-3c171bab62be.htm language=enus -->
## TOPIC 00087: rfmxinstrdotnet/html/74d0d1b7-6fe4-be58-60b8-3c171bab62be.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/74d0d1b7-6fe4-be58-60b8-3c171bab62be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/74d0d1b7-6fe4-be58-60b8-3c171bab62be.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetLoadOptions Method

RFmxInstrMXGetLoadOptions Method

LoadConfigurations(String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLoadOptions(
	string channelName,
	ref RFmxInstrMXLoadOptions[] value
)
```

```text
Public Function GetLoadOptions ( 
	channelName As String,
	ByRef value As RFmxInstrMXLoadOptions()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value RFmxInstrMXLoadOptions**
  - Specifies the configurations to skip while loading from a file using the LoadConfigurations(String) method

###### Return Value

Int32

##### Remarks

LoadOptions

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/75377430-e92d-d5fc-b10b-723253c083e1.htm language=enus -->
## TOPIC 00088: rfmxinstrdotnet/html/75377430-e92d-d5fc-b10b-723253c083e1.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/75377430-e92d-d5fc-b10b-723253c083e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/75377430-e92d-d5fc-b10b-723253c083e1.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeByte Method

RFmxInstrMXSetAttributeByte Method

Sets the value of a Byte attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeByte(
	string channelName,
	int attributeIdentifier,
	byte value
)
```

```text
Public Function SetAttributeByte ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Byte
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Byte**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm language=enus -->
## TOPIC 00089: rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeByteArray Method

RFmxInstrMXGetAttributeByteArray Method

Gets the value of a byte array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeByteArray(
	string channelName,
	int attributeIdentifier,
	ref byte[] value
)
```

```text
Public Function GetAttributeByteArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As Byte()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Byte**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/76deccc0-914f-1e60-a288-69903b0fc48f.htm language=enus -->
## TOPIC 00090: rfmxinstrdotnet/html/76deccc0-914f-1e60-a288-69903b0fc48f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/76deccc0-914f-1e60-a288-69903b0fc48f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/76deccc0-914f-1e60-a288-69903b0fc48f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSession(String, String, Boolean) Method

RFmxInstrMXGetSession(String, String, Boolean) Method

Gets a session, if it exists for given resource name; else, returns a new one.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxInstrMX GetSession(
	string resourceName,
	string optionString,
	out bool isNewSession
)
```

```text
Public Shared Function GetSession ( 
	resourceName As String,
	optionString As String,
	<OutAttribute> ByRef isNewSession As Boolean
) As RFmxInstrMX
```

###### Parameters

- **resourceName String**
  - Specifies the resource name of the device to initialize.
- **optionString String**
  - Sets the initial value of certain properties for the session.The following attributes are used in this parameter: RFmxSetup,Simulate,AnalysisOnly. To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1 You can set the Digitizerfield to 5622_25MHz_DDC only when using the NI 5665. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. To set multiple attributes, separate their assignments with a comma.
- **isNewSession Boolean**
  - if new session is created; otherwise .

###### Return Value

RFmxInstrMX

##### See Also

###### Reference

RFmxInstrMX Class

GetSession Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7751fa61-fe91-7ef7-7202-d3c745459728.htm language=enus -->
## TOPIC 00091: rfmxinstrdotnet/html/7751fa61-fe91-7ef7-7202-d3c745459728.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7751fa61-fe91-7ef7-7202-d3c745459728.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7751fa61-fe91-7ef7-7202-d3c745459728.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetLOFrequency Method

RFmxInstrMXGetLOFrequency Method

Gets the LO signal frequency for the configured center frequency. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLOFrequency(
	string channelName,
	out double value
)
```

```text
Public Function GetLOFrequency ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the LO signal frequency for the configured center frequency. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

LOFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/77f18286-1b49-6bfd-ee64-83150249cd35.htm language=enus -->
## TOPIC 00092: rfmxinstrdotnet/html/77f18286-1b49-6bfd-ee64-83150249cd35.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/77f18286-1b49-6bfd-ee64-83150249cd35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/77f18286-1b49-6bfd-ee64-83150249cd35.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.None Field

RFmxInstrMXConstantsNone Field

The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string None = ""
```

```text
Public Const None As String = ""
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7820ae4d-e419-adc5-0fac-9b7e5928dcae.htm language=enus -->
## TOPIC 00093: rfmxinstrdotnet/html/7820ae4d-e419-adc5-0fac-9b7e5928dcae.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7820ae4d-e419-adc5-0fac-9b7e5928dcae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7820ae4d-e419-adc5-0fac-9b7e5928dcae.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxException Properties

RFmxException Properties

The [RFmxException](18d5fcbe-05d4-882e-f44f-33468189c7b9.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Data | Gets a collection of key/value pairs that provide additional user-defined information about the exception.(Inherited from Exception) |
|  | HelpLink | Gets or sets a link to the help file associated with this exception.(Inherited from Exception) |
|  | HResult | Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception.(Inherited from Exception) |
|  | InnerException | Gets the Exception instance that caused the current exception.(Inherited from Exception) |
|  | Message | Gets a message that describes the current exception.(Inherited from Exception) |
|  | Source | Gets or sets the name of the application or the object that causes the error.(Inherited from Exception) |
|  | StackTrace | Gets a string representation of the immediate frames on the call stack.(Inherited from Exception) |
|  | TargetSite | Gets the method that throws the current exception.(Inherited from Exception) |

Top

##### See Also

###### Reference

RFmxException Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/788ff34f-6952-8158-4b61-82e5592e0604.htm language=enus -->
## TOPIC 00094: rfmxinstrdotnet/html/788ff34f-6952-8158-4b61-82e5592e0604.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/788ff34f-6952-8158-4b61-82e5592e0604.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/788ff34f-6952-8158-4b61-82e5592e0604.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.Close Method

RFmxInstrMXClose Method

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public void Close()
```

```text
Public Sub Close
```

###### Return Value

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm language=enus -->
## TOPIC 00095: rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFrequencyReferenceExportedTerminal Method

RFmxInstrMXGetFrequencyReferenceExportedTerminal Method

Gets a comma-separated list of the terminals at which to export the frequency reference.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyReferenceExportedTerminal(
	string channelName,
	out string value
)
```

```text
Public Function GetFrequencyReferenceExportedTerminal ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value String**
  - Upon return, contains a comma-separated list of the terminals at which to export the frequency reference.

###### Return Value

Int32

##### Remarks

FrequencyReferenceExportedTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm language=enus -->
## TOPIC 00096: rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.BuildModuleString Method

RFmxInstrMXBuildModuleString Method

Selector String

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildModuleString(
	string selectorString,
	string moduleName
)
```

```text
Public Shared Function BuildModuleString ( 
	selectorString As String,
	moduleName As String
) As String
```

###### Parameters

- **selectorString String**
  - specifies the selector string. The default value is "" (empty string).
- **moduleName String**
  - specifies the module for which you want the temperature to be read.

###### Return Value

String

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm language=enus -->
## TOPIC 00097: rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSignalConfigurationNames Method

RFmxInstrMXGetSignalConfigurationNames Method

Returns the signal names and corresponding personality type, for the personality type selected in the personalityFilter parameter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSignalConfigurationNames(
	string selectorString,
	RFmxInstrMXPersonalities personalityFilter,
	ref string[] signalNames,
	ref RFmxInstrMXPersonalities[] personality
)
```

```text
Public Function GetSignalConfigurationNames ( 
	selectorString As String,
	personalityFilter As RFmxInstrMXPersonalities,
	ByRef signalNames As String(),
	ByRef personality As RFmxInstrMXPersonalities()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string. Pass an empty string.
- **personalityFilter RFmxInstrMXPersonalities**
  - Specifies the personality filter to get the signal configuration names. You can specify one or more of the following personalities. The default value is All. To get all the signal names of SpecAn, personalityFilter parameter should be RFmxInstrMXPersonalities.SpecAn. To get the signal names of SpecAn and LTE, personalityFilter parameter should be RFmxInstrMXPersonalities.SpecAn and RFmxInstrMXPersonalities.Lte. To get the signal names of all personalities, personalityFilter parameter should be RFmxInstrMXPersonalities.All.
- **signalNames String**
  - Returns an array of the signal names.
- **personality RFmxInstrMXPersonalities**
  - Returns an array of personalities where each entry corresponds to the personality of each signal name in the signalNames array.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7a4a35ac-9180-f636-7cd3-17d3581645b4.htm language=enus -->
## TOPIC 00098: rfmxinstrdotnet/html/7a4a35ac-9180-f636-7cd3-17d3581645b4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7a4a35ac-9180-f636-7cd3-17d3581645b4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7a4a35ac-9180-f636-7cd3-17d3581645b4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXSParameterOrientation Enumeration

RFmxInstrMXSParameterOrientation Enumeration

Specifies the orientation of the data in the S2P file relative to the port you specify. The default value is Port2TowardsDut.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXSParameterOrientation
```

```text
Public Enumeration RFmxInstrMXSParameterOrientation
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Port1TowardsDut | 0 | Port 1 of the S2P is oriented towards the DUT. |
| Port2TowardsDut | 1 | Port 2 of the S2P is oriented towards the DUT. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7ac64e6f-3175-ad16-7f4d-12d312062e05.htm language=enus -->
## TOPIC 00099: rfmxinstrdotnet/html/7ac64e6f-3175-ad16-7f4d-12d312062e05.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7ac64e6f-3175-ad16-7f4d-12d312062e05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7ac64e6f-3175-ad16-7f4d-12d312062e05.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxieDStarBLine Field

RFmxInstrMXConstantsPxieDStarBLine Field

The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxieDStarBLine = "PXIe_DStarB"
```

```text
Public Const PxieDStarBLine As String = "PXIe_DStarB"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7af6b000-1a5f-025c-7110-4c42f7a0b9a5.htm language=enus -->
## TOPIC 00100: rfmxinstrdotnet/html/7af6b000-1a5f-025c-7110-4c42f7a0b9a5.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7af6b000-1a5f-025c-7110-4c42f7a0b9a5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7af6b000-1a5f-025c-7110-4c42f7a0b9a5.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSParameterExternalAttenuationType Method

RFmxInstrMXGetSParameterExternalAttenuationType Method

Returns the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the selectorString input to specify the name of the Calplane and port to configure for s-parameter.

Supported devices: PXIe-5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSParameterExternalAttenuationType(
	string selectorString,
	out RFmxInstrMXSParameterType sParameterType
)
```

```text
Public Function GetSParameterExternalAttenuationType ( 
	selectorString As String,
	<OutAttribute> ByRef sParameterType As RFmxInstrMXSParameterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". Hence, the valid selector string is "calplane::(calplaneName)/port::(deviceName)/(channelNumber)/(portName)". For a MIMO port, the valid selector string is "calplane::(calplaneName)/port::(deviceName)/(channelNumber)/(portName)". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0/if0"
- **sParameterType RFmxInstrMXSParameterType**
  - Returns the type of S-parameter which applies to measurements on the specified port for a Calplane.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7b30b76b-5f45-f2a7-05a6-d5e5ea8c8a92.htm language=enus -->
## TOPIC 00101: rfmxinstrdotnet/html/7b30b76b-5f45-f2a7-05a6-d5e5ea8c8a92.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7b30b76b-5f45-f2a7-05a6-d5e5ea8c8a92.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7b30b76b-5f45-f2a7-05a6-d5e5ea8c8a92.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetStartTriggerDigitalEdgeSource Method

RFmxInstrMXSetStartTriggerDigitalEdgeSource Method

SetStartTriggerType(String, RFmxInstrMXStartTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStartTriggerDigitalEdgeSource(
	string selectorString,
	string value
)
```

```text
Public Function SetStartTriggerDigitalEdgeSource ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Specifies the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

StartTriggerDigitalEdgeSource

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm language=enus -->
## TOPIC 00102: rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetIFOutputPowerLevelOffset Method

RFmxInstrMXGetIFOutputPowerLevelOffset Method

Gets the power offset by which to adjust the default IF output power level. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIFOutputPowerLevelOffset(
	string channelName,
	out double value
)
```

```text
Public Function GetIFOutputPowerLevelOffset ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the power offset by which to adjust the default IF output power level. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

IFOutputPowerLevelOffset

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7c61b5cc-aafd-70b4-aaf9-fcac4ad88f44.htm language=enus -->
## TOPIC 00103: rfmxinstrdotnet/html/7c61b5cc-aafd-70b4-aaf9-fcac4ad88f44.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7c61b5cc-aafd-70b4-aaf9-fcac4ad88f44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7c61b5cc-aafd-70b4-aaf9-fcac4ad88f44.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeULongArray Method

RFmxInstrMXSetAttributeULongArray Method

Sets the value of a ulong array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeULongArray(
	string channelName,
	int attributeIdentifier,
	ulong[] value
)
```

```text
Public Function SetAttributeULongArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As ULong()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value UInt64**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7cdd2046-fc87-1bc0-789c-34d3c7d9d979.htm language=enus -->
## TOPIC 00104: rfmxinstrdotnet/html/7cdd2046-fc87-1bc0-789c-34d3c7d9d979.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7cdd2046-fc87-1bc0-789c-34d3c7d9d979.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7cdd2046-fc87-1bc0-789c-34d3c7d9d979.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetExternalAttenuationTableActualValue Method

RFmxInstrMXGetExternalAttenuationTableActualValue Method

Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetExternalAttenuationTableActualValue(
	string selectorString,
	out double externalAttenuation
)
```

```text
Public Function GetExternalAttenuationTableActualValue ( 
	selectorString As String,
	<OutAttribute> ByRef externalAttenuation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a Selector String comprising of the signal name and calibration plane name. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, you must use "port::<deviceName>/<channelNumber>" as part of the selector string to read the external attenuation table actual value for the specified port. If you do not specify the signal name, the value is returned for the last committed signal instance. example: "" "signal::sig1" "calplane::plane0" "signal::sig1/calplane::plane0" "port::rfsa1/0" "signal::sig1/port::rfsa1/0" "calplane::plane0/port::rfsa1/0" "signal::sig1/calplane::plane0/port::rfsa1/0"
- **externalAttenuation Double**
  - Upon return, contains the external attenuation table actual value applied to the measurements for a specified signal and calibration plane. This further includes interpolation of the external attenuation table based on the specified signal. On a MIMO session, this value corresponds to a specified port. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7d47d1cf-00b3-32b6-973d-0e3879ced6da.htm language=enus -->
## TOPIC 00105: rfmxinstrdotnet/html/7d47d1cf-00b3-32b6-973d-0e3879ced6da.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7d47d1cf-00b3-32b6-973d-0e3879ced6da.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7d47d1cf-00b3-32b6-973d-0e3879ced6da.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.LOSourceSGSAShared Field

RFmxInstrMXConstantsLOSourceSGSAShared Field

Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on the PXIe-5830/5831/5832/5841/5842.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string LOSourceSGSAShared = "SG_SA_Shared"
```

```text
Public Const LOSourceSGSAShared As String = "SG_SA_Shared"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7e2e8094-d250-059b-5910-a9cc79126f0d.htm language=enus -->
## TOPIC 00106: rfmxinstrdotnet/html/7e2e8094-d250-059b-5910-a9cc79126f0d.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7e2e8094-d250-059b-5910-a9cc79126f0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7e2e8094-d250-059b-5910-a9cc79126f0d.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAvailablePaths Method

RFmxInstrMXGetAvailablePaths Method

Gets paths available for the session. On a MIMO session, this method fetches all the paths for the initialized MIMO paths.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAvailablePaths(
	string selectorString,
	ref string[] availablePaths
)
```

```text
Public Function GetAvailablePaths ( 
	selectorString As String,
	ByRef availablePaths As String()
) As Integer
```

###### Parameters

- **selectorString String**
  - Identifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter.
- **availablePaths String**
  - Returns an array of available paths.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7e3eec66-d138-177d-6b00-743af779d03d.htm language=enus -->
## TOPIC 00107: rfmxinstrdotnet/html/7e3eec66-d138-177d-6b00-743af779d03d.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7e3eec66-d138-177d-6b00-743af779d03d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7e3eec66-d138-177d-6b00-743af779d03d.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants Class

RFmxInstrMXConstants Class

Specifies constants for I/O terminals.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxInstrMXConstants
```

```text
Public NotInheritable Class RFmxInstrMXConstants
```

The RFmxInstrMXConstants type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | ClockIn | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the SetFrequencyReferenceFrequency(String, Double) method to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the SetFrequencyReferenceFrequency(String, Double) method to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840/5841/5842/5860 with PXIe-5653: This configuration does not apply. |
|  | ClockOut | Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | DoNotExportSignal | Specifies that the signal should not be exported. |
|  | LOSourceAutomaticSGSAShared | Specifies that RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings. configures instrument specific properties on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: Set LO Source property to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library). Set LO Source property to Automatic_SG_SA_Shared in RFmx. Configure any additional settings on RFSG and RFmx, including selecting waveforms. Initiate RFSG. Initiate RFmx. Note When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. |
| Note |  |  |
| When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. |  |  |
|  | LOSourceLOIn | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
|  | LOSourceNone | Specifies that no LO source is required to downconvert the RF input signal. |
|  | LOSourceOnboard | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. PXIe-5831: This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage. PXIe-5832: This configuration uses the onboard LO of the PXIe-3623, using the LO2 stage. PXIe-5831 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.PXIe-5832 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3623.PXIe-5840 with PXIe-5653: If the center frequency is greater than or equal to 3.2 GHz, this configuration uses the PXIe-5653 LO source. For frequencies less than 3.2 GHz, this configuration uses the PXIe-5840 internal LO. If RFmx is operating in Spectrum mode, this configuration uses the PXIe-5840 internal LO irrespective of the frequency. |
|  | LOSourceSecondary | Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), PXIe-5832 with PXIe-5653 (LO1 stage only). |
|  | LOSourceSGSAShared | Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on the PXIe-5830/5831/5832/5841/5842. |
|  | None | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. |
|  | OnboardClock | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5840 with PXIe-5653: Lock onto the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use ReferenceIn for PXIe-5840 or ReferenceIn2 for the PXIe-5840 with the PXIe-5653. PXIe-5860: Lock to the PXIe-5860 onboard clock. |
|  | Pfi0 | The signal is exported to the PFI 0. |
|  | Pfi1 | The signal is exported to the PXI 1. |
|  | PxiClock | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5860: The RFmx driver locks the device to the PXI backplane clock. PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842/5860: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
|  | PxiClockMaster | PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clock as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clock as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5840 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clock. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |
|  | PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | PxieDStarCLine | The signal is exported to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | PxiStarLine | The signal is exported to the PXI star trigger line. |
|  | PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
|  | PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
|  | PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
|  | PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
|  | PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
|  | PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
|  | PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
|  | PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
|  | ReferenceIn | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the SetFrequencyReferenceFrequency(String, Double) method according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the SetFrequencyReferenceFrequency(String, Double) method according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5840 with PXIe-5653: Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. |
|  | ReferenceIn2 | PXIe-5840 with PXIe-5653: RFmx locks the reference clock to the clock sourced at the PXIe-5840 REF IN terminal that is previously configured by an NI-RFSG session. Connect the NI-5840 REF OUT connector to the PXIe-5653 REF IN connector. Configure open NI-RFSG sessions to the device to use ReferenceIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. |
|  | ReferenceOut | Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | ReferenceOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
|  | TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7e553b93-9235-5f37-47b8-fe4431fb7238.htm language=enus -->
## TOPIC 00108: rfmxinstrdotnet/html/7e553b93-9235-5f37-47b8-fe4431fb7238.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7e553b93-9235-5f37-47b8-fe4431fb7238.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7e553b93-9235-5f37-47b8-fe4431fb7238.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAdvanceTriggerType Method

RFmxInstrMXGetAdvanceTriggerType Method

Gets whether the advance trigger is a digital edge or a software trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAdvanceTriggerType(
	string selectorString,
	out RFmxInstrMXAdvanceTriggerType value
)
```

```text
Public Function GetAdvanceTriggerType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxInstrMXAdvanceTriggerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value RFmxInstrMXAdvanceTriggerType**
  - Upon return, contains whether the advance trigger is a digital edge or a software trigger.

###### Return Value

Int32

##### Remarks

AdvanceTriggerType

None

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/7efcbd6e-4d01-7725-bdf1-f617afad68f3.htm language=enus -->
## TOPIC 00109: rfmxinstrdotnet/html/7efcbd6e-4d01-7725-bdf1-f617afad68f3.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/7efcbd6e-4d01-7725-bdf1-f617afad68f3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/7efcbd6e-4d01-7725-bdf1-f617afad68f3.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetThermalCorrectionHeadroomRange Method

RFmxInstrMXGetThermalCorrectionHeadroomRange Method

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetThermalCorrectionHeadroomRange(
	string selectorString,
	out double value
)
```

```text
Public Function GetThermalCorrectionHeadroomRange ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the expected thermal operating range of the instrument from the self-calibration temperature returned from the GetDeviceTemperature(String, Double) method. This value is expressed in degree Celsius.

###### Return Value

Int32

##### Remarks

ThermalCorrectionHeadroomRange

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/80110236-bb95-8e69-2065-f19a584faceb.htm language=enus -->
## TOPIC 00110: rfmxinstrdotnet/html/80110236-bb95-8e69-2065-f19a584faceb.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/80110236-bb95-8e69-2065-f19a584faceb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/80110236-bb95-8e69-2065-f19a584faceb.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetRFAttenuationValue Method

RFmxInstrMXSetRFAttenuationValue Method

Sets the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRFAttenuationValue(
	string channelName,
	double value
)
```

```text
Public Function SetRFAttenuationValue ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

RFAttenuationValue

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/80f61d15-127e-149e-07f3-e0cd72f5733f.htm language=enus -->
## TOPIC 00111: rfmxinstrdotnet/html/80f61d15-127e-149e-07f3-e0cd72f5733f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/80f61d15-127e-149e-07f3-e0cd72f5733f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/80f61d15-127e-149e-07f3-e0cd72f5733f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSession(String[], String) Method

RFmxInstrMXGetSession(String, String) Method

Gets a session, if it exists for given set of resource name; else, returns a new one.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxInstrMX GetSession(
	string[] resourceName,
	string optionString
)
```

```text
Public Shared Function GetSession ( 
	resourceName As String(),
	optionString As String
) As RFmxInstrMX
```

###### Parameters

- **resourceName String**
  - Specifies the resource name of the device to initialize.
- **optionString String**
  - Sets the initial value of certain properties for the session.The following attributes are used in this parameter: RFmxSetup,Simulate,AnalysisOnly. To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1 You can set the Digitizerfield to 5622_25MHz_DDC only when using the NI 5665. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. To set multiple attributes, separate their assignments with a comma.

###### Return Value

RFmxInstrMX

##### See Also

###### Reference

RFmxInstrMX Class

GetSession Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/810a102d-2e9b-6414-d12e-70b100e69f54.htm language=enus -->
## TOPIC 00112: rfmxinstrdotnet/html/810a102d-2e9b-6414-d12e-70b100e69f54.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/810a102d-2e9b-6414-d12e-70b100e69f54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/810a102d-2e9b-6414-d12e-70b100e69f54.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeComplexDoubleArray Method

RFmxInstrMXSetAttributeComplexDoubleArray Method

Sets the value of a ComplexDouble array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeComplexDoubleArray(
	string channelName,
	int attributeIdentifier,
	ComplexDouble[] value
)
```

```text
Public Function SetAttributeComplexDoubleArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As ComplexDouble()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value ComplexDouble**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/817cafcd-e8ed-ff4a-4ecc-8295970d3be9.htm language=enus -->
## TOPIC 00113: rfmxinstrdotnet/html/817cafcd-e8ed-ff4a-4ecc-8295970d3be9.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/817cafcd-e8ed-ff4a-4ecc-8295970d3be9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/817cafcd-e8ed-ff4a-4ecc-8295970d3be9.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.EnableCalibrationPlane Method

RFmxInstrMXEnableCalibrationPlane Method

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int EnableCalibrationPlane(
	string selectorString
)
```

```text
Public Function EnableCalibrationPlane ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which the external attenuation table or S-parameter is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. Example:"" "calplane::plane0" "calplane::all"

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/81e1ab38-c25e-c0ff-4197-562c5ee18422.htm language=enus -->
## TOPIC 00114: rfmxinstrdotnet/html/81e1ab38-c25e-c0ff-4197-562c5ee18422.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/81e1ab38-c25e-c0ff-4197-562c5ee18422.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/81e1ab38-c25e-c0ff-4197-562c5ee18422.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.ReferenceOut Field

RFmxInstrMXConstantsReferenceOut Field

Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string ReferenceOut = "RefOut"
```

```text
Public Const ReferenceOut As String = "RefOut"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8206e6c3-cf9f-2322-c748-37121cb2c37e.htm language=enus -->
## TOPIC 00115: rfmxinstrdotnet/html/8206e6c3-cf9f-2322-c748-37121cb2c37e.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8206e6c3-cf9f-2322-c748-37121cb2c37e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8206e6c3-cf9f-2322-c748-37121cb2c37e.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants Fields

RFmxInstrMXConstants Fields

The [RFmxInstrMXConstants](7e3eec66-d138-177d-6b00-743af779d03d.htm) type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | ClockIn | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the SetFrequencyReferenceFrequency(String, Double) method to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the SetFrequencyReferenceFrequency(String, Double) method to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840/5841/5842/5860 with PXIe-5653: This configuration does not apply. |
|  | ClockOut | Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | DoNotExportSignal | Specifies that the signal should not be exported. |
|  | LOSourceAutomaticSGSAShared | Specifies that RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings. configures instrument specific properties on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: Set LO Source property to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library). Set LO Source property to Automatic_SG_SA_Shared in RFmx. Configure any additional settings on RFSG and RFmx, including selecting waveforms. Initiate RFSG. Initiate RFmx. Note When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. |
| Note |  |  |
| When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. |  |  |
|  | LOSourceLOIn | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
|  | LOSourceNone | Specifies that no LO source is required to downconvert the RF input signal. |
|  | LOSourceOnboard | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. PXIe-5831: This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage. PXIe-5832: This configuration uses the onboard LO of the PXIe-3623, using the LO2 stage. PXIe-5831 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.PXIe-5832 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3623.PXIe-5840 with PXIe-5653: If the center frequency is greater than or equal to 3.2 GHz, this configuration uses the PXIe-5653 LO source. For frequencies less than 3.2 GHz, this configuration uses the PXIe-5840 internal LO. If RFmx is operating in Spectrum mode, this configuration uses the PXIe-5840 internal LO irrespective of the frequency. |
|  | LOSourceSecondary | Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), PXIe-5832 with PXIe-5653 (LO1 stage only). |
|  | LOSourceSGSAShared | Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on the PXIe-5830/5831/5832/5841/5842. |
|  | None | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. |
|  | OnboardClock | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5840 with PXIe-5653: Lock onto the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use ReferenceIn for PXIe-5840 or ReferenceIn2 for the PXIe-5840 with the PXIe-5653. PXIe-5860: Lock to the PXIe-5860 onboard clock. |
|  | Pfi0 | The signal is exported to the PFI 0. |
|  | Pfi1 | The signal is exported to the PXI 1. |
|  | PxiClock | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5860: The RFmx driver locks the device to the PXI backplane clock. PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842/5860: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
|  | PxiClockMaster | PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clock as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clock as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5840 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clock. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |
|  | PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | PxieDStarCLine | The signal is exported to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | PxiStarLine | The signal is exported to the PXI star trigger line. |
|  | PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
|  | PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
|  | PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
|  | PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
|  | PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
|  | PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
|  | PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
|  | PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
|  | ReferenceIn | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the SetFrequencyReferenceFrequency(String, Double) method according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the SetFrequencyReferenceFrequency(String, Double) method according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5840 with PXIe-5653: Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. |
|  | ReferenceIn2 | PXIe-5840 with PXIe-5653: RFmx locks the reference clock to the clock sourced at the PXIe-5840 REF IN terminal that is previously configured by an NI-RFSG session. Connect the NI-5840 REF OUT connector to the PXIe-5653 REF IN connector. Configure open NI-RFSG sessions to the device to use ReferenceIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. |
|  | ReferenceOut | Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
|  | ReferenceOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
|  | TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |

Top

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8217671e-92a9-a6d4-c035-d56e014507c0.htm language=enus -->
## TOPIC 00116: rfmxinstrdotnet/html/8217671e-92a9-a6d4-c035-d56e014507c0.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8217671e-92a9-a6d4-c035-d56e014507c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8217671e-92a9-a6d4-c035-d56e014507c0.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSession Method

RFmxInstrMXGetSession Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetSession(String, String) | Gets a session, if it exists for given resource name; else, returns a new one. |
|  | GetSession(String, String) | Gets a session, if it exists for given set of resource name; else, returns a new one. |
|  | GetSession(String, String, Boolean) | Gets a session, if it exists for given resource name; else, returns a new one. |
|  | GetSession(String, String, Boolean) | Gets a session, if it exists for given set of resource name; else, returns a new one. |

Top

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/846e6ce2-322b-e520-f066-593b6342452c.htm language=enus -->
## TOPIC 00117: rfmxinstrdotnet/html/846e6ce2-322b-e520-f066-593b6342452c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/846e6ce2-322b-e520-f066-593b6342452c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/846e6ce2-322b-e520-f066-593b6342452c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetSmuChannel Method

RFmxInstrMXSetSmuChannel Method

Sets the output channel to be used for noise figure (NF) measurement in RFmx.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSmuChannel(
	string channelName,
	string value
)
```

```text
Public Function SetSmuChannel ( 
	channelName As String,
	value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value String**
  - Specifies the output channel to be used for noise figure (NF) measurement in RFmx.

###### Return Value

Int32

##### Remarks

SmuChannel

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/849b7caa-4e82-2444-f6b2-d5f9450fd667.htm language=enus -->
## TOPIC 00118: rfmxinstrdotnet/html/849b7caa-4e82-2444-f6b2-d5f9450fd667.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/849b7caa-4e82-2444-f6b2-d5f9450fd667.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/849b7caa-4e82-2444-f6b2-d5f9450fd667.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetIFOutputPowerLevelOffset Method

RFmxInstrMXSetIFOutputPowerLevelOffset Method

Sets the power offset by which to adjust the default IF output power level. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIFOutputPowerLevelOffset(
	string channelName,
	double value
)
```

```text
Public Function SetIFOutputPowerLevelOffset ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Specifies the power offset by which to adjust the default IF output power level. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

IFOutputPowerLevelOffset

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8706d15a-95e3-132a-1c11-50c942cce57a.htm language=enus -->
## TOPIC 00119: rfmxinstrdotnet/html/8706d15a-95e3-132a-1c11-50c942cce57a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8706d15a-95e3-132a-1c11-50c942cce57a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8706d15a-95e3-132a-1c11-50c942cce57a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRecommendedSpectralAcquisitionSpan Method

RFmxInstrMXGetRecommendedSpectralAcquisitionSpan Method

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRecommendedSpectralAcquisitionSpan(
	string channelName,
	out double value
)
```

```text
Public Function GetRecommendedSpectralAcquisitionSpan ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the recommended acquisition span for spectral acquisition, in Hz.

###### Return Value

Int32

##### Remarks

RecommendedSpectralAcquisitionSpan

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8759f999-763d-61d6-6d59-8c1240883a10.htm language=enus -->
## TOPIC 00120: rfmxinstrdotnet/html/8759f999-763d-61d6-6d59-8c1240883a10.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8759f999-763d-61d6-6d59-8c1240883a10.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8759f999-763d-61d6-6d59-8c1240883a10.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXOptimizePathForSignalBandwidth Enumeration

RFmxInstrMXOptimizePathForSignalBandwidth Enumeration

Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXOptimizePathForSignalBandwidth
```

```text
Public Enumeration RFmxInstrMXOptimizePathForSignalBandwidth
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the optimized path for signal bandwidth. |
| Enabled | 1 | Enables the optimized path for signal bandwidth. |
| Automatic | 2 | Automatically enables the optimized path based on other configurations. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/87e8ee65-8b33-bee8-2380-745d6148ab10.htm language=enus -->
## TOPIC 00121: rfmxinstrdotnet/html/87e8ee65-8b33-bee8-2380-745d6148ab10.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/87e8ee65-8b33-bee8-2380-745d6148ab10.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/87e8ee65-8b33-bee8-2380-745d6148ab10.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetDigitizerTemperature Method

RFmxInstrMXGetDigitizerTemperature Method

Gets the current temperature of the digitizer module. This value is expressed in degrees Celsius.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDigitizerTemperature(
	string channelName,
	out double value
)
```

```text
Public Function GetDigitizerTemperature ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the current temperature of the digitizer module. This value is expressed in degrees Celsius.

###### Return Value

Int32

##### Remarks

DigitizerTemperature

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/88064bc3-7410-836f-2324-426878e94a2f.htm language=enus -->
## TOPIC 00122: rfmxinstrdotnet/html/88064bc3-7410-836f-2324-426878e94a2f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/88064bc3-7410-836f-2324-426878e94a2f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/88064bc3-7410-836f-2324-426878e94a2f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLOLeakageAvoidanceEnabled Method

RFmxInstrMXSetLOLeakageAvoidanceEnabled Method

Sets whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLOLeakageAvoidanceEnabled(
	string channelName,
	RFmxInstrMXLOLeakageAvoidanceEnabled value
)
```

```text
Public Function SetLOLeakageAvoidanceEnabled ( 
	channelName As String,
	value As RFmxInstrMXLOLeakageAvoidanceEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXLOLeakageAvoidanceEnabled**
  - Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition.

###### Return Value

Int32

##### Remarks

LOLeakageAvoidanceEnabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8b2c442c-4240-1cb6-10b1-e60e2b171f54.htm language=enus -->
## TOPIC 00123: rfmxinstrdotnet/html/8b2c442c-4240-1cb6-10b1-e60e2b171f54.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8b2c442c-4240-1cb6-10b1-e60e2b171f54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8b2c442c-4240-1cb6-10b1-e60e2b171f54.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSessionFromNIRfsaHandle Method

RFmxInstrMXGetSessionFromNIRfsaHandle Method

| Note |
| --- |
| 1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxInstrMX GetSessionFromNIRfsaHandle(
	IntPtr niRfsaHandle
)
```

```text
Public Shared Function GetSessionFromNIRfsaHandle ( 
	niRfsaHandle As IntPtr
) As RFmxInstrMX
```

###### Parameters

- **niRfsaHandle IntPtr**
  - Sets the initial value of certain properties for the session.The following attributes are used in this parameter: RFmxSetup,Simulate,AnalysisOnly. To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1 You can set the Digitizerfield to 5622_25MHz_DDC only when using the NI 5665. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. To set multiple attributes, separate their assignments with a comma.

###### Return Value

RFmxInstrMX

##### Remarks

Ensure to keep the NIRfsa .NET object that encapsulates the niRfsaHandle used to get the RFmxInstr .NET object from this function alive while using the RFmxInstrMX .NET object.
 In case the NIRfsa .NET object that encapsulates the niRfsaHandle used to get the RFmxInstr .NET object from this function is disposed or closed the corresponding RFmxInstrMX .NET object will stop working.

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8c5afbd3-8893-4e09-087e-e33e7714e850.htm language=enus -->
## TOPIC 00124: rfmxinstrdotnet/html/8c5afbd3-8893-4e09-087e-e33e7714e850.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8c5afbd3-8893-4e09-087e-e33e7714e850.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8c5afbd3-8893-4e09-087e-e33e7714e850.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetPreampEnabled Method

RFmxInstrMXSetPreampEnabled Method

Sets whether the RF preamplifier is enabled in the system.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPreampEnabled(
	string channelName,
	RFmxInstrMXPreampEnabled value
)
```

```text
Public Function SetPreampEnabled ( 
	channelName As String,
	value As RFmxInstrMXPreampEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value RFmxInstrMXPreampEnabled**
  - Specifies whether the RF preamplifier is enabled in the system.

###### Return Value

Int32

##### Remarks

PreampEnabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8d75638d-35a9-bfa2-b7f4-1493dd82beae.htm language=enus -->
## TOPIC 00125: rfmxinstrdotnet/html/8d75638d-35a9-bfa2-b7f4-1493dd82beae.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8d75638d-35a9-bfa2-b7f4-1493dd82beae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8d75638d-35a9-bfa2-b7f4-1493dd82beae.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ConfigureSParameterExternalAttenuationType Method

RFmxInstrMXConfigureSParameterExternalAttenuationType Method

Selector String

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSParameterExternalAttenuationType(
	string selectorString,
	RFmxInstrMXSParameterType sParameterType
)
```

```text
Public Function ConfigureSParameterExternalAttenuationType ( 
	selectorString As String,
	sParameterType As RFmxInstrMXSParameterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::(calplaneName)/port::(deviceName)/(channelNumber)/(portName)". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all"
- **sParameterType RFmxInstrMXSParameterType**
  - Specifies the type of S-parameter which applies to measurements on the specified port for a Calplane. If you set this parameter to Scalar or Vector, RFmx adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT. PXIe-5831/5832: Valid values for this parameter are Scalar and Vector. Vector is only supported for TRX Ports in a Semiconductor Test System (STS). PXIe-5840/5841/5842/5860: The only valid value for this parameter is Scalar. Scalar (1): De-embeds the measurement using the gain term. Vector (2): De-embeds the measurement using the gain term and the reflection term.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/8e26db60-0073-ac25-1ea5-2f284c8c8dfa.htm language=enus -->
## TOPIC 00126: rfmxinstrdotnet/html/8e26db60-0073-ac25-1ea5-2f284c8c8dfa.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/8e26db60-0073-ac25-1ea5-2f284c8c8dfa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/8e26db60-0073-ac25-1ea5-2f284c8c8dfa.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetInputIsolationEnabled Method

RFmxInstrMXGetInputIsolationEnabled Method

Gets whether input isolation is enabled.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetInputIsolationEnabled(
	string channelName,
	out RFmxInstrMXInputIsolationEnabled value
)
```

```text
Public Function GetInputIsolationEnabled ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXInputIsolationEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXInputIsolationEnabled**
  - Upon return, contains whether input isolation is enabled.

###### Return Value

Int32

##### Remarks

InputIsolationEnabled

Disabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/906c2ade-fa69-9049-f5e8-c191ebef558e.htm language=enus -->
## TOPIC 00127: rfmxinstrdotnet/html/906c2ade-fa69-9049-f5e8-c191ebef558e.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/906c2ade-fa69-9049-f5e8-c191ebef558e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/906c2ade-fa69-9049-f5e8-c191ebef558e.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSelfCalibrateLastTemperature Method

RFmxInstrMXGetSelfCalibrateLastTemperature Method

Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

| Note |
| --- |
| For PXIe-5644/5645/5646 devices, you must select ImageSuppression for the selfCalibrateStep parameter. |

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSelfCalibrateLastTemperature(
	string selectorString,
	RFmxInstrMXSelfCalibrateSteps selfCalibrateStep,
	out double temperature
)
```

```text
Public Function GetSelfCalibrateLastTemperature ( 
	selectorString As String,
	selfCalibrateStep As RFmxInstrMXSelfCalibrateSteps,
	<OutAttribute> ByRef temperature As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of a MIMO port on a MIMO session. Example:"""port::myrfsa1/0" You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **selfCalibrateStep RFmxInstrMXSelfCalibrateSteps**
  - Identifies the self-calibration step to query for the last successful self-calibration temperature data. The default value is PreselectorAlignment.
- **temperature Double**
  - Upon return, contains the value of temperature at the last self-calibration. This value is expresed in degree Celsius.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/909163c6-c505-e0c0-c8fc-a3c6ab6e7e4a.htm language=enus -->
## TOPIC 00128: rfmxinstrdotnet/html/909163c6-c505-e0c0-c8fc-a3c6ab6e7e4a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/909163c6-c505-e0c0-c8fc-a3c6ab6e7e4a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/909163c6-c505-e0c0-c8fc-a3c6ab6e7e4a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetMixerLevel Method

RFmxInstrMXSetMixerLevel Method

Sets the mixer level, in dBm.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMixerLevel(
	string channelName,
	double value
)
```

```text
Public Function SetMixerLevel ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Specifies the mixer level, in dBm.

###### Return Value

Int32

##### Remarks

MixerLevel

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/90e1849b-f7e8-cb36-05d4-766f592549c4.htm language=enus -->
## TOPIC 00129: rfmxinstrdotnet/html/90e1849b-f7e8-cb36-05d4-766f592549c4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/90e1849b-f7e8-cb36-05d4-766f592549c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/90e1849b-f7e8-cb36-05d4-766f592549c4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXStartTriggerDigitalEdge Enumeration

RFmxInstrMXStartTriggerDigitalEdge Enumeration

SetStartTriggerType(String, RFmxInstrMXStartTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXStartTriggerDigitalEdge
```

```text
Public Enumeration RFmxInstrMXStartTriggerDigitalEdge
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/959a21cf-ac6d-0d71-1ea7-e9d896ffec54.htm language=enus -->
## TOPIC 00130: rfmxinstrdotnet/html/959a21cf-ac6d-0d71-1ea7-e9d896ffec54.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/959a21cf-ac6d-0d71-1ea7-e9d896ffec54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/959a21cf-ac6d-0d71-1ea7-e9d896ffec54.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSessionFromNIRfsaHandles Method

RFmxInstrMXGetSessionFromNIRfsaHandles Method

| Note |
| --- |
| 1. Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. 2. Closing the RFmx session will not close the NI-RFSA driver session. |

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxInstrMX GetSessionFromNIRfsaHandles(
	IntPtr[] niRfsaHandles
)
```

```text
Public Shared Function GetSessionFromNIRfsaHandles ( 
	niRfsaHandles As IntPtr()
) As RFmxInstrMX
```

###### Parameters

- **niRfsaHandles IntPtr**
  - Sets the initial value of certain properties for the session.The following attributes are used in this parameter: RFmxSetup,Simulate,AnalysisOnly. To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1 You can set the Digitizerfield to 5622_25MHz_DDC only when using the NI 5665. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. To set multiple attributes, separate their assignments with a comma.

###### Return Value

RFmxInstrMX

##### Remarks

Ensure to keep the NIRfsa .NET object that encapsulates the niRfsaHandle used to get the RFmxInstr .NET object from this function alive while using the RFmxInstrMX .NET object.
 In case the NIRfsa .NET object that encapsulates the niRfsaHandle used to get the RFmxInstr .NET object from this function is disposed or closed the corresponding RFmxInstrMX .NET object will stop working.

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/9624dbb9-7a3b-036c-ac8f-8979b41dccef.htm language=enus -->
## TOPIC 00131: rfmxinstrdotnet/html/9624dbb9-7a3b-036c-ac8f-8979b41dccef.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/9624dbb9-7a3b-036c-ac8f-8979b41dccef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/9624dbb9-7a3b-036c-ac8f-8979b41dccef.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXLOPllFractionalMode Enumeration

RFmxInstrMXLOPllFractionalMode Enumeration

Specifies whether to use fractional mode for the LO phase-locked loop (PLL).

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXLOPllFractionalMode
```

```text
Public Enumeration RFmxInstrMXLOPllFractionalMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Indicates that the method is disabled. |
| Enabled | 1 | Indicates that the method is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/a80313ff-36af-26ef-fe27-a9fb878b785c.htm language=enus -->
## TOPIC 00132: rfmxinstrdotnet/html/a80313ff-36af-26ef-fe27-a9fb878b785c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/a80313ff-36af-26ef-fe27-a9fb878b785c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/a80313ff-36af-26ef-fe27-a9fb878b785c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetDigitalGain Method

RFmxInstrMXGetDigitalGain Method

Gets the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDigitalGain(
	string selectorString,
	out double value
)
```

```text
Public Function GetDigitalGain ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. RFmx does not compensate for the specified digital gain. You can use this property to account for external gain changes without changing the analog signal path. The PXIe-5644/5645/5646 applies this gain when the data is scaled. The raw data does not include this scaling on these devices.

###### Return Value

Int32

##### Remarks

DigitalGain

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/addb7e7c-6988-c5a6-9b38-071326ecc1bb.htm language=enus -->
## TOPIC 00133: rfmxinstrdotnet/html/addb7e7c-6988-c5a6-9b38-071326ecc1bb.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/addb7e7c-6988-c5a6-9b38-071326ecc1bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/addb7e7c-6988-c5a6-9b38-071326ecc1bb.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.ReferenceIn2 Field

RFmxInstrMXConstantsReferenceIn2 Field

PXIe-5840 with PXIe-5653: RFmx locks the reference clock to the clock sourced at the PXIe-5840 REF IN terminal that is previously configured by an NI-RFSG session. Connect the NI-5840 REF OUT connector to the PXIe-5653 REF IN connector.

Configure open NI-RFSG sessions to the device to use ReferenceIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653.

PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string ReferenceIn2 = "RefIn2"
```

```text
Public Const ReferenceIn2 As String = "RefIn2"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ae2421bc-1ad9-ed94-83fd-0eef75d9a1cd.htm language=enus -->
## TOPIC 00134: rfmxinstrdotnet/html/ae2421bc-1ad9-ed94-83fd-0eef75d9a1cd.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ae2421bc-1ad9-ed94-83fd-0eef75d9a1cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ae2421bc-1ad9-ed94-83fd-0eef75d9a1cd.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFrequencyReferenceSource Method

RFmxInstrMXGetFrequencyReferenceSource Method

Gets the frequency reference source.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyReferenceSource(
	string channelName,
	out string value
)
```

```text
Public Function GetFrequencyReferenceSource ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the frequency reference source.

###### Return Value

Int32

##### Remarks

FrequencyReferenceSource

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ae685dfe-5a2f-6cd6-ea73-f3aef34f1b00.htm language=enus -->
## TOPIC 00135: rfmxinstrdotnet/html/ae685dfe-5a2f-6cd6-ea73-f3aef34f1b00.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ae685dfe-5a2f-6cd6-ea73-f3aef34f1b00.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ae685dfe-5a2f-6cd6-ea73-f3aef34f1b00.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXChannelCoupling Enumeration

RFmxInstrMXChannelCoupling Enumeration

Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXChannelCoupling
```

```text
Public Enumeration RFmxInstrMXChannelCoupling
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| ACCoupled | 0 | Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter. |
| DCCoupled | 1 | Specifies that the RF input channel is DC-coupled. RFmx enforces a minimum RF attenuation for device protection. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm language=enus -->
## TOPIC 00136: rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSelfCalibrationValidityCheckTimeInterval Method

RFmxInstrMXGetSelfCalibrationValidityCheckTimeInterval Method

Gets the minimum time between two self calibration validity checks. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSelfCalibrationValidityCheckTimeInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetSelfCalibrationValidityCheckTimeInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the minimum time between two self calibration validity checks. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SelfCalibrationValidityCheckTimeInterval

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/b08c3315-3cbd-26fd-6c09-38f42daaaa29.htm language=enus -->
## TOPIC 00137: rfmxinstrdotnet/html/b08c3315-3cbd-26fd-6c09-38f42daaaa29.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/b08c3315-3cbd-26fd-6c09-38f42daaaa29.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/b08c3315-3cbd-26fd-6c09-38f42daaaa29.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeInt Method

RFmxInstrMXSetAttributeInt Method

Sets the value of a Int attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeInt(
	string channelName,
	int attributeIdentifier,
	int value
)
```

```text
Public Function SetAttributeInt ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Integer
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm language=enus -->
## TOPIC 00138: rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRecommendedCenterFrequency Method

RFmxInstrMXGetRecommendedCenterFrequency Method

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRecommendedCenterFrequency(
	string channelName,
	out double value
)
```

```text
Public Function GetRecommendedCenterFrequency ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the recommended center frequency of the RF signal. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

RecommendedCenterFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ba0f8d06-3e7b-8120-762d-b45771135da3.htm language=enus -->
## TOPIC 00139: rfmxinstrdotnet/html/ba0f8d06-3e7b-8120-762d-b45771135da3.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ba0f8d06-3e7b-8120-762d-b45771135da3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ba0f8d06-3e7b-8120-762d-b45771135da3.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeFloatArray Method

RFmxInstrMXGetAttributeFloatArray Method

Gets the value of a float array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeFloatArray(
	string channelName,
	int attributeIdentifier,
	ref float[] value
)
```

```text
Public Function GetAttributeFloatArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As Single()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Single**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/bbe1f187-e88b-7b6c-9492-be1ec50dd280.htm language=enus -->
## TOPIC 00140: rfmxinstrdotnet/html/bbe1f187-e88b-7b6c-9492-be1ec50dd280.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/bbe1f187-e88b-7b6c-9492-be1ec50dd280.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/bbe1f187-e88b-7b6c-9492-be1ec50dd280.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeByte Method

RFmxInstrMXGetAttributeByte Method

Gets the value of a Byte attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeByte(
	string channelName,
	int attributeIdentifier,
	out byte value
)
```

```text
Public Function GetAttributeByte ( 
	channelName As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Byte
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Byte**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/bbea26b3-28a9-756a-d337-11ee67403d76.htm language=enus -->
## TOPIC 00141: rfmxinstrdotnet/html/bbea26b3-28a9-756a-d337-11ee67403d76.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/bbea26b3-28a9-756a-d337-11ee67403d76.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/bbea26b3-28a9-756a-d337-11ee67403d76.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXDownconverterPreselectorEnabled Enumeration

RFmxInstrMXDownconverterPreselectorEnabled Enumeration

Specifies whether the tunable preselector is enabled on the downconverter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXDownconverterPreselectorEnabled
```

```text
Public Enumeration RFmxInstrMXDownconverterPreselectorEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the preselector. |
| Enabled | 1 | The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the GetPreselectorPresent(String, Boolean) method to determine if the downconverter has a preselector. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/bc772969-0ec6-181f-a0ed-5d6886fdf20e.htm language=enus -->
## TOPIC 00142: rfmxinstrdotnet/html/bc772969-0ec6-181f-a0ed-5d6886fdf20e.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/bc772969-0ec6-181f-a0ed-5d6886fdf20e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/bc772969-0ec6-181f-a0ed-5d6886fdf20e.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetTriggerTerminalName Method

RFmxInstrMXGetTriggerTerminalName Method

The standard format is as follows:

PXIe-5830/5831/5832: /BasebandModule/ai/0/RefTrigger, where BasebandModule is the name of your device in MAX.

PXIe-5860: /ModuleName/ai/ChannelNumber/RefTrigger,, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).

All other devices: /DigitizerName/RefTrigger, where DigitizerName is the name of your associated digitizer module in MAX.

Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerTerminalName(
	string channelName,
	out string value
)
```

```text
Public Function GetTriggerTerminalName ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value String**
  - Upon return, contains the fully qualified signal name as a string.

###### Return Value

Int32

##### Remarks

TriggerTerminalName

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/be338f59-ee67-2bac-43c1-9a7ec762b8b4.htm language=enus -->
## TOPIC 00143: rfmxinstrdotnet/html/be338f59-ee67-2bac-43c1-9a7ec762b8b4.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/be338f59-ee67-2bac-43c1-9a7ec762b8b4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/be338f59-ee67-2bac-43c1-9a7ec762b8b4.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetLOPllFractionalMode Method

RFmxInstrMXGetLOPllFractionalMode Method

Gets whether to use fractional mode for the LO phase-locked loop (PLL).

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLOPllFractionalMode(
	string channelName,
	out RFmxInstrMXLOPllFractionalMode value
)
```

```text
Public Function GetLOPllFractionalMode ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXLOPllFractionalMode
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value RFmxInstrMXLOPllFractionalMode**
  - Upon return, contains whether to use fractional mode for the LO phase-locked loop (PLL).

###### Return Value

Int32

##### Remarks

LOPllFractionalMode

Enabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/bef0d0a3-2544-d688-8ab3-f422abda9b00.htm language=enus -->
## TOPIC 00144: rfmxinstrdotnet/html/bef0d0a3-2544-d688-8ab3-f422abda9b00.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/bef0d0a3-2544-d688-8ab3-f422abda9b00.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/bef0d0a3-2544-d688-8ab3-f422abda9b00.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetDownconverterCenterFrequency Method

RFmxInstrMXGetDownconverterCenterFrequency Method

Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDownconverterCenterFrequency(
	string channelName,
	out double value
)
```

```text
Public Function GetDownconverterCenterFrequency ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value Double**
  - Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

DownconverterCenterFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/bf540408-42ab-abdd-bd08-11958914e135.htm language=enus -->
## TOPIC 00145: rfmxinstrdotnet/html/bf540408-42ab-abdd-bd08-11958914e135.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/bf540408-42ab-abdd-bd08-11958914e135.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/bf540408-42ab-abdd-bd08-11958914e135.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRecommendedSpectralFftWindow Method

RFmxInstrMXGetRecommendedSpectralFftWindow Method

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRecommendedSpectralFftWindow(
	string channelName,
	out RFmxInstrMXRecommendedSpectralFftWindow value
)
```

```text
Public Function GetRecommendedSpectralFftWindow ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXRecommendedSpectralFftWindow
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value RFmxInstrMXRecommendedSpectralFftWindow**
  - Upon return, contains the recommended FFT window type for spectral acquisition.

###### Return Value

Int32

##### Remarks

RecommendedSpectralFftWindow

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/bf6817b3-248c-953c-8ccc-d4bb2e2779ab.htm language=enus -->
## TOPIC 00146: rfmxinstrdotnet/html/bf6817b3-248c-953c-8ccc-d4bb2e2779ab.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/bf6817b3-248c-953c-8ccc-d4bb2e2779ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/bf6817b3-248c-953c-8ccc-d4bb2e2779ab.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.NumberOfLists Property

RFmxInstrMXNumberOfLists Property

Gets the number of lists created in the current session.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int NumberOfLists { get; }
```

```text
Public ReadOnly Property NumberOfLists As Integer
	Get
```

###### Property Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c284332e-461b-0e23-fc36-29821b801ae9.htm language=enus -->
## TOPIC 00147: rfmxinstrdotnet/html/c284332e-461b-0e23-fc36-29821b801ae9.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c284332e-461b-0e23-fc36-29821b801ae9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c284332e-461b-0e23-fc36-29821b801ae9.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ConfigureExternalAttenuationTable Method

RFmxInstrMXConfigureExternalAttenuationTable Method

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureExternalAttenuationTable(
	string selectorString,
	string tableName,
	double[] frequency,
	double[] externalAttenuation
)
```

```text
Public Function ConfigureExternalAttenuationTable ( 
	selectorString As String,
	tableName As String,
	frequency As Double(),
	externalAttenuation As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names. Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all"
- **tableName String**
  - Specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table.
- **frequency Double**
  - Specifies an array of frequencies in the external attenuation table. This value is expressed in Hz.
- **externalAttenuation Double**
  - Specifies an array of attenuations corresponding to the frequency specified by the frequency parameter. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c2feb480-a09a-f097-e273-ff46483826b1.htm language=enus -->
## TOPIC 00148: rfmxinstrdotnet/html/c2feb480-a09a-f097-e273-ff46483826b1.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c2feb480-a09a-f097-e273-ff46483826b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c2feb480-a09a-f097-e273-ff46483826b1.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXTuningSpeed Enumeration

RFmxInstrMXTuningSpeed Enumeration

Makes tradeoffs between tuning speed and phase noise.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXTuningSpeed
```

```text
Public Enumeration RFmxInstrMXTuningSpeed
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Normal | 0 | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an underdamped response. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a narrow loop bandwidth. |
| Medium | 1 | Specifies that the RF downconverter module uses a medium loop bandwidth. This value is not supported on PXIe-5663/5663E/5665/5668 devices. |
| Fast | 2 | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an overdamped response. Setting this method to Fast allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a wide loop bandwidth. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c3612b89-f04c-569e-537b-712476081537.htm language=enus -->
## TOPIC 00149: rfmxinstrdotnet/html/c3612b89-f04c-569e-537b-712476081537.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c3612b89-f04c-569e-537b-712476081537.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c3612b89-f04c-569e-537b-712476081537.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SelfCalibrate Method

RFmxInstrMXSelfCalibrate Method

niRFSA Self Cal method

NI RF Vector Signal Analyzers Help

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SelfCalibrate(
	string selectorString,
	RFmxInstrMXSelfCalibrateSteps stepsToOmit
)
```

```text
Public Function SelfCalibrate ( 
	selectorString As String,
	stepsToOmit As RFmxInstrMXSelfCalibrateSteps
) As Integer
```

###### Parameters

- **selectorString String**
  - Specify an empty string as the value of this parameter.
- **stepsToOmit RFmxInstrMXSelfCalibrateSteps**
  - Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that all calibration steps are performed. The only valid value for PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is an empty array. PreselectorAlignmentOmits the Preselector Alignment step. If you omit this step and the NI-RFSA IsSelfCalibrationValid method indicates the calibration data for this step is invalid, the preselector alignment specifications are not guaranteed. This step applies only to the PXIe-5605/5606.GainReferenceOmits the Gain Reference step. If you omit this step and the NI-RFSA IsSelfCalibrationValid method indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. IFFlatnessOmits the IF Flatness step. If you omit this step and the NI-RFSA IsSelfCalibrationValid method indicates the calibration data for this step is invalid, the IF flatness specifications are not guaranteed.DigitizerSelfcalOmits the Digitizer Self Cal step. If you omit this step and the NI-RFSA IsSelfCalibrationValid method indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed.LOSelfCalOmits the LO Self Cal step. If you omit this step and the NI-RFSA IsSelfCalibrationValid method indicates the calibration data for this step is invalid, the LO PLL may fail to lock.AmplitudeAccuracyNot used by this method.ResidualLOPowerNot used by this method.ImageSuppressionNot used by this method.SynthesizerAlignmentNot used by this method.DCOffsetNot used by this method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm language=enus -->
## TOPIC 00150: rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXMechanicalAttenuationAuto Enumeration

RFmxInstrMXMechanicalAttenuationAuto Enumeration

Specifies whether RFmx chooses an attenuation setting based on the hardware settings.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXMechanicalAttenuationAuto
```

```text
Public Enumeration RFmxInstrMXMechanicalAttenuationAuto
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that RFmx uses the value configured in the Mechanical Attenuation Value method. |
| True | 1 | Specifies that the measurement computes the mechanical attenuation. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c5fb5703-be31-9e23-12a7-b73733ed1c8f.htm language=enus -->
## TOPIC 00151: rfmxinstrdotnet/html/c5fb5703-be31-9e23-12a7-b73733ed1c8f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c5fb5703-be31-9e23-12a7-b73733ed1c8f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c5fb5703-be31-9e23-12a7-b73733ed1c8f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.FetchRawIQData Method

RFmxInstrMXFetchRawIQData Method

Fetches I/Q data from a single record in an acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRawIQData(
	string selectorString,
	double timeout,
	int recordsToFetch,
	long samplesToRead,
	ref ComplexWaveform<ComplexSingle> data
)
```

```text
Public Function FetchRawIQData ( 
	selectorString As String,
	timeout As Double,
	recordsToFetch As Integer,
	samplesToRead As Long,
	ByRef data As ComplexWaveform(Of ComplexSingle)
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the raw IQ data. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies the VI immediately returns available data. The default value is 10.
- **recordsToFetch Int32**
  - Specifies the record to retrieve. Record numbers are zero-based. The default value is 0.
- **samplesToRead Int64**
  - Specifies the number of samples to fetch. A value of -1 specifies that RFmx fetches all samples. The default value is -1.
- **data ComplexWaveformComplexSingle**
  - Returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I2 + Q2) / 2R, where R is the input impedance in ohms. For RFmx, R = 50 ohms.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c8386738-60fa-e822-f766-2f88f148b4db.htm language=enus -->
## TOPIC 00152: rfmxinstrdotnet/html/c8386738-60fa-e822-f766-2f88f148b4db.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c8386738-60fa-e822-f766-2f88f148b4db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c8386738-60fa-e822-f766-2f88f148b4db.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetReadyForReferenceEventTerminalName Method

RFmxInstrMXGetReadyForReferenceEventTerminalName Method

Gets the fully qualified signal name as a string.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReadyForReferenceEventTerminalName(
	string selectorString,
	out string value
)
```

```text
Public Function GetReadyForReferenceEventTerminalName ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the fully qualified signal name as a string.

###### Return Value

Int32

##### Remarks

ReadyForReferenceEventTerminalName

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm language=enus -->
## TOPIC 00153: rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetTemperatureReadInterval Method

RFmxInstrMXGetTemperatureReadInterval Method

Gets the minimum time difference between temperature sensor readings. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTemperatureReadInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetTemperatureReadInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the minimum time difference between temperature sensor readings. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TemperatureReadInterval

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/c8818c2b-79f8-a80e-4cf4-b5d3523c0a2c.htm language=enus -->
## TOPIC 00154: rfmxinstrdotnet/html/c8818c2b-79f8-a80e-4cf4-b5d3523c0a2c.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/c8818c2b-79f8-a80e-4cf4-b5d3523c0a2c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/c8818c2b-79f8-a80e-4cf4-b5d3523c0a2c.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXRecommendedAcquisitionType Enumeration

RFmxInstrMXRecommendedAcquisitionType Enumeration

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXRecommendedAcquisitionType
```

```text
Public Enumeration RFmxInstrMXRecommendedAcquisitionType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| IQ | 0 | Indicates that the recommended acquisition type is I/Q. Use the Analyze (IQ) function to perform the measurement. |
| Spectral | 1 | Indicates that the recommended acquisition type is Spectral. Use Analyze (Spectrum) function to perform the measurement. |
| IQOrSpectral | 2 | Indicates that the recommended acquisition type is I/Q or Spectral. Use either Analyze (IQ) or Analyze (Spectrum) function to perform the measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm language=enus -->
## TOPIC 00155: rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.Dispose Method

RFmxInstrMXDispose Method

Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any.

Namespace:

NationalInstruments.RFmx.InstrMX

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

##### Remarks

You can call this method safely more than once, even if the signal is already deleted.

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ceca86e7-d7aa-d81a-ddf5-e802578930bd.htm language=enus -->
## TOPIC 00156: rfmxinstrdotnet/html/ceca86e7-d7aa-d81a-ddf5-e802578930bd.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ceca86e7-d7aa-d81a-ddf5-e802578930bd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ceca86e7-d7aa-d81a-ddf5-e802578930bd.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SendSoftwareEdgeStartTrigger Method

RFmxInstrMXSendSoftwareEdgeStartTrigger Method

- You configure an invalid trigger.
- You have not previously called the RFmx Initiate method.

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SendSoftwareEdgeStartTrigger()
```

```text
Public Function SendSoftwareEdgeStartTrigger As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/cf5764a4-32e4-c882-982a-b0e0028eb095.htm language=enus -->
## TOPIC 00157: rfmxinstrdotnet/html/cf5764a4-32e4-c882-982a-b0e0028eb095.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/cf5764a4-32e4-c882-982a-b0e0028eb095.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/cf5764a4-32e4-c882-982a-b0e0028eb095.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetMechanicalAttenuationAuto Method

RFmxInstrMXSetMechanicalAttenuationAuto Method

Sets whether RFmx chooses an attenuation setting based on the hardware settings.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMechanicalAttenuationAuto(
	string channelName,
	RFmxInstrMXMechanicalAttenuationAuto value
)
```

```text
Public Function SetMechanicalAttenuationAuto ( 
	channelName As String,
	value As RFmxInstrMXMechanicalAttenuationAuto
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXMechanicalAttenuationAuto**
  - Specifies whether RFmx chooses an attenuation setting based on the hardware settings.

###### Return Value

Int32

##### Remarks

MechanicalAttenuationAuto

True

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/dd37302e-ec5c-e22f-dfb2-701a1d1dd83a.htm language=enus -->
## TOPIC 00158: rfmxinstrdotnet/html/dd37302e-ec5c-e22f-dfb2-701a1d1dd83a.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/dd37302e-ec5c-e22f-dfb2-701a1d1dd83a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/dd37302e-ec5c-e22f-dfb2-701a1d1dd83a.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRecommendedAcquisitionType Method

RFmxInstrMXGetRecommendedAcquisitionType Method

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRecommendedAcquisitionType(
	string channelName,
	out RFmxInstrMXRecommendedAcquisitionType value
)
```

```text
Public Function GetRecommendedAcquisitionType ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXRecommendedAcquisitionType
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value RFmxInstrMXRecommendedAcquisitionType**
  - Upon return, contains the recommended acquisition type for the last committed measurement configuration.

###### Return Value

Int32

##### Remarks

RecommendedAcquisitionType

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/df787e7b-b318-2f21-0b41-745e6fbc1949.htm language=enus -->
## TOPIC 00159: rfmxinstrdotnet/html/df787e7b-b318-2f21-0b41-745e6fbc1949.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/df787e7b-b318-2f21-0b41-745e6fbc1949.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/df787e7b-b318-2f21-0b41-745e6fbc1949.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetWarning Method

RFmxInstrMXGetWarning Method

Gets the latest warning code and description.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetWarning(
	out int warningCode,
	out string warningDescription
)
```

```text
Public Function GetWarning ( 
	<OutAttribute> ByRef warningCode As Integer,
	<OutAttribute> ByRef warningDescription As String
) As Integer
```

###### Parameters

- **warningCode Int32**
  - Upon return, contains the latest warning code.
- **warningDescription String**
  - Upon return, contains the latest warning description.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/e1e7045a-c552-a08d-ad4a-0b03fd445ba0.htm language=enus -->
## TOPIC 00160: rfmxinstrdotnet/html/e1e7045a-c552-a08d-ad4a-0b03fd445ba0.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/e1e7045a-c552-a08d-ad4a-0b03fd445ba0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/e1e7045a-c552-a08d-ad4a-0b03fd445ba0.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetOverflowErrorReporting Method

RFmxInstrMXGetOverflowErrorReporting Method

Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOverflowErrorReporting(
	string channelName,
	out RFmxInstrMXOverflowErrorReporting value
)
```

```text
Public Function GetOverflowErrorReporting ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXOverflowErrorReporting
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXOverflowErrorReporting**
  - Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

###### Return Value

Int32

##### Remarks

OverflowErrorReporting

Warning

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/e6403700-7ea1-0830-4149-571e94da247d.htm language=enus -->
## TOPIC 00161: rfmxinstrdotnet/html/e6403700-7ea1-0830-4149-571e94da247d.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/e6403700-7ea1-0830-4149-571e94da247d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/e6403700-7ea1-0830-4149-571e94da247d.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetSmuResourceName Method

RFmxInstrMXSetSmuResourceName Method

Sets the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSmuResourceName(
	string channelName,
	string value
)
```

```text
Public Function SetSmuResourceName ( 
	channelName As String,
	value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value String**
  - Specifies the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name.

###### Return Value

Int32

##### Remarks

SmuResourceName

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/e6b7baf7-4b3a-f67b-a57e-00a637960656.htm language=enus -->
## TOPIC 00162: rfmxinstrdotnet/html/e6b7baf7-4b3a-f67b-a57e-00a637960656.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/e6b7baf7-4b3a-f67b-a57e-00a637960656.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/e6b7baf7-4b3a-f67b-a57e-00a637960656.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetModuleRevision Method

RFmxInstrMXGetModuleRevision Method

Gets the revision of the RF downconverter module.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetModuleRevision(
	string channelName,
	out string value
)
```

```text
Public Function GetModuleRevision ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value String**
  - Upon return, contains the revision of the RF downconverter module.

###### Return Value

Int32

##### Remarks

ModuleRevision

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/e7959faf-2c12-134e-00c3-0da6bf73b599.htm language=enus -->
## TOPIC 00163: rfmxinstrdotnet/html/e7959faf-2c12-134e-00c3-0da6bf73b599.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/e7959faf-2c12-134e-00c3-0da6bf73b599.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/e7959faf-2c12-134e-00c3-0da6bf73b599.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAvailablePorts Method

RFmxInstrMXGetAvailablePorts Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetAvailablePorts(String) | Obsolete. Gets the list of ports available for use based on your instrument configuration. |
|  | GetAvailablePorts(String, String) | Gets ports available for the session. On a MIMO session, this method fetches all the ports for the initialized MIMO ports. |

Top

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/e8b45592-80de-6bb9-2463-20dd5c9f5138.htm language=enus -->
## TOPIC 00164: rfmxinstrdotnet/html/e8b45592-80de-6bb9-2463-20dd5c9f5138.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/e8b45592-80de-6bb9-2463-20dd5c9f5138.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/e8b45592-80de-6bb9-2463-20dd5c9f5138.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxException Methods

RFmxException Methods

The [RFmxException](18d5fcbe-05d4-882e-f44f-33468189c7b9.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection.(Inherited from Object) |
|  | GetBaseException | When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions.(Inherited from Exception) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetObjectData | Gets the SerializationInfo with information about the exception. (Overrides ExceptionGetObjectData(SerializationInfo, StreamingContext)) |
|  | GetType | Gets the runtime type of the current instance.(Inherited from Exception) |
|  | MemberwiseClone | Creates a shallow copy of the current Object.(Inherited from Object) |
|  | ToString | Creates and returns a string representation of the current exception.(Inherited from Exception) |

Top

##### See Also

###### Reference

RFmxException Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ea104c1b-81d3-1168-fd59-007dce3b095f.htm language=enus -->
## TOPIC 00165: rfmxinstrdotnet/html/ea104c1b-81d3-1168-fd59-007dce3b095f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ea104c1b-81d3-1168-fd59-007dce3b095f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ea104c1b-81d3-1168-fd59-007dce3b095f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeUIntArray Method

RFmxInstrMXSetAttributeUIntArray Method

Sets the value of a uint array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeUIntArray(
	string channelName,
	int attributeIdentifier,
	uint[] value
)
```

```text
Public Function SetAttributeUIntArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As UInteger()
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value UInt32**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/eb417975-e2e2-6f8d-22ec-0e2a9f80a6ed.htm language=enus -->
## TOPIC 00166: rfmxinstrdotnet/html/eb417975-e2e2-6f8d-22ec-0e2a9f80a6ed.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/eb417975-e2e2-6f8d-22ec-0e2a9f80a6ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/eb417975-e2e2-6f8d-22ec-0e2a9f80a6ed.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX(String, String) Constructor

RFmxInstrMX(String, String) Constructor

| Note |
| --- |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxInstrMX(
	string resourceName,
	string optionString
)
```

```text
Public Sub New ( 
	resourceName As String,
	optionString As String
)
```

###### Parameters

- **resourceName String**
  - Specifies the resource name of the device to initialize.
- **optionString String**
  - Sets the initial value of certain properties for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". While using this mode, you are responsible for waveform acquisition and RFmx will perform analysis on the I/Q waveform or Spectrum you specify. You must use personality specific Analyze functions to perform the measurements. To use external NI Source Measure Units (SMU) as the noise source power supply for the Noise Figure (NF) measurement, use "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx. RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs.

##### Remarks

To set multiple attributes, separate their assignments with a comma.

##### See Also

###### Reference

RFmxInstrMX Class

RFmxInstrMX Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ebcaaecc-1c87-3172-0a4b-e94178fd116f.htm language=enus -->
## TOPIC 00167: rfmxinstrdotnet/html/ebcaaecc-1c87-3172-0a4b-e94178fd116f.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ebcaaecc-1c87-3172-0a4b-e94178fd116f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ebcaaecc-1c87-3172-0a4b-e94178fd116f.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ExportSignal Method

RFmxInstrMXExportSignal Method

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ExportSignal(
	RFmxInstrMXExportSignalSource exportSignalSource,
	string exportSignalOutputTerminal
)
```

```text
Public Function ExportSignal ( 
	exportSignalSource As RFmxInstrMXExportSignalSource,
	exportSignalOutputTerminal As String
) As Integer
```

###### Parameters

- **exportSignalSource RFmxInstrMXExportSignalSource**
  - Controls the source to export signals.
- **exportSignalOutputTerminal String**
  - Specifies the terminal where the signal is exported. You can also choose not to export any signal.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/ebf9af0b-b53d-fff1-b5dd-91f10af516e7.htm language=enus -->
## TOPIC 00168: rfmxinstrdotnet/html/ebf9af0b-b53d-fff1-b5dd-91f10af516e7.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/ebf9af0b-b53d-fff1-b5dd-91f10af516e7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/ebf9af0b-b53d-fff1-b5dd-91f10af516e7.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

ISignalConfiguration.SignalConfigurationName Property

ISignalConfigurationSignalConfigurationName Property

Gets the name assigned to the current signal configuration object.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
string SignalConfigurationName { get; }
```

```text
ReadOnly Property SignalConfigurationName As String
	Get
```

###### Property Value

String

##### See Also

###### Reference

ISignalConfiguration Interface

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f1abec1d-7cad-89c3-cfd7-6fb52eaddc53.htm language=enus -->
## TOPIC 00169: rfmxinstrdotnet/html/f1abec1d-7cad-89c3-cfd7-6fb52eaddc53.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f1abec1d-7cad-89c3-cfd7-6fb52eaddc53.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f1abec1d-7cad-89c3-cfd7-6fb52eaddc53.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiClock Field

RFmxInstrMXConstantsPxiClock Field

PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624.

PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5860: The RFmx driver locks the device to the PXI backplane clock.

PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842/5860: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiClock = "PXI_Clk"
```

```text
Public Const PxiClock As String = "PXI_Clk"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f2205f04-5afe-795c-8a93-c5691f14c602.htm language=enus -->
## TOPIC 00170: rfmxinstrdotnet/html/f2205f04-5afe-795c-8a93-c5691f14c602.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f2205f04-5afe-795c-8a93-c5691f14c602.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f2205f04-5afe-795c-8a93-c5691f14c602.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAvailablePorts(String[]) Method

RFmxInstrMXGetAvailablePorts(String) Method

**Note: This API is now obsolete.**

Gets the list of ports available for use based on your instrument configuration.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use GetAvailablePorts(string selectorString, ref string[] availablePorts) overloaded method instead")]
public int GetAvailablePorts(
	out string[] availablePorts
)
```

```text
<ObsoleteAttribute("Use GetAvailablePorts(string selectorString, ref string[] availablePorts) overloaded method instead")>
Public Function GetAvailablePorts ( 
	<OutAttribute> ByRef availablePorts As String()
) As Integer
```

###### Parameters

- **availablePorts String**
  - Returns a list of available ports.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

GetAvailablePorts Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f2da7b2d-c5dd-8113-2348-89fcf9356622.htm language=enus -->
## TOPIC 00171: rfmxinstrdotnet/html/f2da7b2d-c5dd-8113-2348-89fcf9356622.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f2da7b2d-c5dd-8113-2348-89fcf9356622.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f2da7b2d-c5dd-8113-2348-89fcf9356622.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiTriggerLine1 Field

RFmxInstrMXConstantsPxiTriggerLine1 Field

The signal is exported to the PXI trigger line 1.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine1 = "PXI_Trig1"
```

```text
Public Const PxiTriggerLine1 As String = "PXI_Trig1"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f3f7be77-bbde-9311-1f6b-693b19805f74.htm language=enus -->
## TOPIC 00172: rfmxinstrdotnet/html/f3f7be77-bbde-9311-1f6b-693b19805f74.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f3f7be77-bbde-9311-1f6b-693b19805f74.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f3f7be77-bbde-9311-1f6b-693b19805f74.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetReadyForAdvanceEventOutputTerminal Method

RFmxInstrMXSetReadyForAdvanceEventOutputTerminal Method

Sets the destination terminal for the Ready for Advance event.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReadyForAdvanceEventOutputTerminal(
	string selectorString,
	string value
)
```

```text
Public Function SetReadyForAdvanceEventOutputTerminal ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Specifies the destination terminal for the Ready for Advance event.

###### Return Value

Int32

##### Remarks

ReadyForAdvanceEventOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f413ea98-d08b-a2b8-5cae-8d873a94acb9.htm language=enus -->
## TOPIC 00173: rfmxinstrdotnet/html/f413ea98-d08b-a2b8-5cae-8d873a94acb9.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f413ea98-d08b-a2b8-5cae-8d873a94acb9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f413ea98-d08b-a2b8-5cae-8d873a94acb9.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.LoadConfigurations Method

RFmxInstrMXLoadConfigurations Method

SaveAllConfigurations(String)

LoadOptions

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int LoadConfigurations(
	string filePath
)
```

```text
Public Function LoadConfigurations ( 
	filePath As String
) As Integer
```

###### Parameters

- **filePath String**
  - Specifies the complete path to the file from which the configurations are to be loaded. Default file extension: .rfmxconfig

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f528724f-a3f2-67bd-9726-bb5d63294273.htm language=enus -->
## TOPIC 00174: rfmxinstrdotnet/html/f528724f-a3f2-67bd-9726-bb5d63294273.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f528724f-a3f2-67bd-9726-bb5d63294273.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f528724f-a3f2-67bd-9726-bb5d63294273.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetDownconverterPreselectorEnabled Method

RFmxInstrMXSetDownconverterPreselectorEnabled Method

Sets whether the tunable preselector is enabled on the downconverter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDownconverterPreselectorEnabled(
	string channelName,
	RFmxInstrMXDownconverterPreselectorEnabled value
)
```

```text
Public Function SetDownconverterPreselectorEnabled ( 
	channelName As String,
	value As RFmxInstrMXDownconverterPreselectorEnabled
) As Integer
```

###### Parameters

- **channelName String**
  - Pass an empty string.
- **value RFmxInstrMXDownconverterPreselectorEnabled**
  - Specifies whether the tunable preselector is enabled on the downconverter.

###### Return Value

Int32

##### Remarks

DownconverterPreselectorEnabled

Disabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f58cb603-81a2-7d14-9383-0e1f832b47ce.htm language=enus -->
## TOPIC 00175: rfmxinstrdotnet/html/f58cb603-81a2-7d14-9383-0e1f832b47ce.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f58cb603-81a2-7d14-9383-0e1f832b47ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f58cb603-81a2-7d14-9383-0e1f832b47ce.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.LOSourceAutomaticSGSAShared Field

RFmxInstrMXConstantsLOSourceAutomaticSGSAShared Field

Specifies that RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements.

When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA).
 This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output.

This value automatically:
 determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings.
 configures instrument specific properties on SA to share the LO between the generator and analyzer, whenever possible.

To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order.

PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable.

PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required.

NI recommends the following order of steps:

| Note |
| --- |
| When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. |

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string LOSourceAutomaticSGSAShared = "Automatic_SG_SA_Shared"
```

```text
Public Const LOSourceAutomaticSGSAShared As String = "Automatic_SG_SA_Shared"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f6080e34-5220-b0bd-5057-a5568c11509d.htm language=enus -->
## TOPIC 00176: rfmxinstrdotnet/html/f6080e34-5220-b0bd-5057-a5568c11509d.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f6080e34-5220-b0bd-5057-a5568c11509d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f6080e34-5220-b0bd-5057-a5568c11509d.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetRFHighpassFilterFrequency Method

RFmxInstrMXSetRFHighpassFilterFrequency Method

Sets the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRFHighpassFilterFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetRFHighpassFilterFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition.

###### Return Value

Int32

##### Remarks

RFHighpassFilterFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/f7410bce-cab7-9808-17df-6c514096d384.htm language=enus -->
## TOPIC 00177: rfmxinstrdotnet/html/f7410bce-cab7-9808-17df-6c514096d384.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/f7410bce-cab7-9808-17df-6c514096d384.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/f7410bce-cab7-9808-17df-6c514096d384.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ResetAttribute Method

RFmxInstrMXResetAttribute Method

Resets the attribute to its default value.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ResetAttribute(
	string channelName,
	RFmxInstrMXPropertyId attributeId
)
```

```text
Public Function ResetAttribute ( 
	channelName As String,
	attributeId As RFmxInstrMXPropertyId
) As Integer
```

###### Parameters

- **channelName String**
  - Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeId RFmxInstrMXPropertyId**
  - Specifies an attribute identifier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/fa06ba80-1a06-fb4f-88d8-83dd9d02434d.htm language=enus -->
## TOPIC 00178: rfmxinstrdotnet/html/fa06ba80-1a06-fb4f-88d8-83dd9d02434d.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/fa06ba80-1a06-fb4f-88d8-83dd9d02434d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/fa06ba80-1a06-fb4f-88d8-83dd9d02434d.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetLOFrequencyStepSize Method

RFmxInstrMXGetLOFrequencyStepSize Method

Gets the step size for tuning the LO phase-locked loop (PLL).

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLOFrequencyStepSize(
	string selectorString,
	out double value
)
```

```text
Public Function GetLOFrequencyStepSize ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value Double**
  - Upon return, contains the step size for tuning the LO phase-locked loop (PLL).

###### Return Value

Int32

##### Remarks

LOFrequencyStepSize

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/facffb9a-2322-af31-7edd-06597da10e1e.htm language=enus -->
## TOPIC 00179: rfmxinstrdotnet/html/facffb9a-2322-af31-7edd-06597da10e1e.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/facffb9a-2322-af31-7edd-06597da10e1e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/facffb9a-2322-af31-7edd-06597da10e1e.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetEndOfRecordEventOutputTerminal Method

RFmxInstrMXSetEndOfRecordEventOutputTerminal Method

Sets the destination terminal for the End of Record event.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEndOfRecordEventOutputTerminal(
	string selectorString,
	string value
)
```

```text
Public Function SetEndOfRecordEventOutputTerminal ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Specifies the destination terminal for the End of Record event.

###### Return Value

Int32

##### Remarks

EndOfRecordEventOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/faf971ca-e599-1350-3296-05981f01f4ac.htm language=enus -->
## TOPIC 00180: rfmxinstrdotnet/html/faf971ca-e599-1350-3296-05981f01f4ac.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/faf971ca-e599-1350-3296-05981f01f4ac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/faf971ca-e599-1350-3296-05981f01f4ac.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetReadyForAdvanceEventTerminalName Method

RFmxInstrMXGetReadyForAdvanceEventTerminalName Method

Gets the fully qualified signal name as a string.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReadyForAdvanceEventTerminalName(
	string selectorString,
	out string value
)
```

```text
Public Function GetReadyForAdvanceEventTerminalName ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string.
- **value String**
  - Upon return, contains the fully qualified signal name as a string.

###### Return Value

Int32

##### Remarks

ReadyForAdvanceEventTerminalName

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr-dotnet path=rfmxinstrdotnet/html/fd352b0b-a546-dc86-ea04-6893ab42b5b2.htm language=enus -->
## TOPIC 00181: rfmxinstrdotnet/html/fd352b0b-a546-dc86-ea04-6893ab42b5b2.htm

- bundle_id: `rfmx-instr-dotnet`
- source_path: `rfmxinstrdotnet/html/fd352b0b-a546-dc86-ea04-6893ab42b5b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-dotnet/raw/resource/enus/rfmxinstrdotnet/html/fd352b0b-a546-dc86-ea04-6893ab42b5b2.htm
- document_id: `rfmx-instr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAvailablePorts(String, String[]) Method

RFmxInstrMXGetAvailablePorts(String, String) Method

Gets ports available for the session. On a MIMO session, this method fetches all the ports for the initialized MIMO ports.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAvailablePorts(
	string selectorString,
	ref string[] availablePorts
)
```

```text
Public Function GetAvailablePorts ( 
	selectorString As String,
	ByRef availablePorts As String()
) As Integer
```

###### Parameters

- **selectorString String**
  - Identifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter.
- **availablePorts String**
  - Returns an array of available ports.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

GetAvailablePorts Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
