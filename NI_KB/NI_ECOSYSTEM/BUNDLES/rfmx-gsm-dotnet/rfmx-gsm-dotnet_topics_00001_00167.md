# NI DOCUMENT BUNDLE: rfmx-gsm-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-gsm-dotnet start=1 end=167 -->
<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/0755017b-a8bc-08a5-e3df-7a44f577bcde.htm language=enus -->
## TOPIC 00001: rfmxgsmdotnet/html/0755017b-a8bc-08a5-e3df-7a44f577bcde.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/0755017b-a8bc-08a5-e3df-7a44f577bcde.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/0755017b-a8bc-08a5-e3df-7a44f577bcde.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMeanPeakEvm Method

RFmxGsmMXModAccResultsGetEvmMeanPeakEvm Method

Gets the mean of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanPeakEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanPeakEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMeanPeakEvm

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/08a64cb9-c46f-0006-ea42-3e5a549624c9.htm language=enus -->
## TOPIC 00002: rfmxgsmdotnet/html/08a64cb9-c46f-0006-ea42-3e5a549624c9.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/08a64cb9-c46f-0006-ea42-3e5a549624c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/08a64cb9-c46f-0006-ea42-3e5a549624c9.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetNoiseCompensationEnabled Method

RFmxGsmMXOrfsConfigurationGetNoiseCompensationEnabled Method

Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCompensationEnabled(
	string selectorString,
	out RFmxGsmMXOrfsNoiseCompensationEnabled value
)
```

```text
Public Function GetNoiseCompensationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXOrfsNoiseCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsNoiseCompensationEnabled**
  - Upon return, contains whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832

###### Return Value

Int32

##### Remarks

OrfsNoiseCompensationEnabled

False

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/0ffa8513-0d4c-1e7a-d960-56bfdfb97935.htm language=enus -->
## TOPIC 00003: rfmxgsmdotnet/html/0ffa8513-0d4c-1e7a-d960-56bfdfb97935.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/0ffa8513-0d4c-1e7a-d960-56bfdfb97935.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/0ffa8513-0d4c-1e7a-d960-56bfdfb97935.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ResetToDefault Method

RFmxGsmMXResetToDefault Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ResetToDefault(
	string selectorString
)
```

```text
Public Function ResetToDefault ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/15b84740-b467-db98-ba6c-eff2e7de6272.htm language=enus -->
## TOPIC 00004: rfmxgsmdotnet/html/15b84740-b467-db98-ba6c-eff2e7de6272.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/15b84740-b467-db98-ba6c-eff2e7de6272.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/15b84740-b467-db98-ba6c-eff2e7de6272.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetExternalAttenuation Method

RFmxGsmMXSetExternalAttenuation Method

NI RF Vector Signal Analyzers Help

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetExternalAttenuation(
	string selectorString,
	double value
)
```

```text
Public Function SetExternalAttenuation ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help.

###### Return Value

Int32

##### Remarks

ExternalAttenuation

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/162ce9ad-4ff9-e405-f131-addb3b38a4a3.htm language=enus -->
## TOPIC 00005: rfmxgsmdotnet/html/162ce9ad-4ff9-e405-f131-addb3b38a4a3.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/162ce9ad-4ff9-e405-f131-addb3b38a4a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/162ce9ad-4ff9-e405-f131-addb3b38a4a3.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.SetMeasurementEnabled Method

RFmxGsmMXPvtConfigurationSetMeasurementEnabled Method

Sets whether to enable the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementEnabled(
	string selectorString,
	bool value
)
```

```text
Public Function SetMeasurementEnabled ( 
	selectorString As String,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Specifies whether to enable the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtMeasurementEnabled

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/19196f05-c08a-1b27-f064-7c8f7be74ca7.htm language=enus -->
## TOPIC 00006: rfmxgsmdotnet/html/19196f05-c08a-1b27-f064-7c8f7be74ca7.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/19196f05-c08a-1b27-f064-7c8f7be74ca7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/19196f05-c08a-1b27-f064-7c8f7be74ca7.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetTimingAdvance Method

RFmxGsmMXGetTimingAdvance Method

Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimingAdvance(
	string selectorString,
	out int value
)
```

```text
Public Function GetTimingAdvance ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst.

###### Return Value

Int32

##### Remarks

TimingAdvance

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/1ba26dbb-047a-1b4f-b2e0-ae4b6186cd2d.htm language=enus -->
## TOPIC 00007: rfmxgsmdotnet/html/1ba26dbb-047a-1b4f-b2e0-ae4b6186cd2d.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/1ba26dbb-047a-1b4f-b2e0-ae4b6186cd2d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/1ba26dbb-047a-1b4f-b2e0-ae4b6186cd2d.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetModulationOffsetFrequency Method

RFmxGsmMXOrfsConfigurationSetModulationOffsetFrequency Method

Sets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetModulationOffsetFrequency(
	string selectorString,
	float value
)
```

```text
Public Function SetModulationOffsetFrequency ( 
	selectorString As String,
	value As Single
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the modoffset number. Example: "modoffset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Single**
  - Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

OrfsModulationOffsetFrequency

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/1d155578-1ae8-8c02-a14c-386eefda060b.htm language=enus -->
## TOPIC 00008: rfmxgsmdotnet/html/1d155578-1ae8-8c02-a14c-386eefda060b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/1d155578-1ae8-8c02-a14c-386eefda060b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/1d155578-1ae8-8c02-a14c-386eefda060b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetLimitedConfigurationChange Method

RFmxGsmMXGetLimitedConfigurationChange Method

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLimitedConfigurationChange(
	string selectorString,
	out RFmxGsmMXLimitedConfigurationChange value
)
```

```text
Public Function GetLimitedConfigurationChange ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXLimitedConfigurationChange**
  - Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

Disabled

Disabled

LimitedConfigurationChange

Disabled

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/209d448c-e1ca-01ca-7887-33baa697e9ab.htm language=enus -->
## TOPIC 00009: rfmxgsmdotnet/html/209d448c-e1ca-01ca-7887-33baa697e9ab.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/209d448c-e1ca-01ca-7887-33baa697e9ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/209d448c-e1ca-01ca-7887-33baa697e9ab.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtResults.FetchPowerTrace Method

RFmxGsmMXPvtResultsFetchPowerTrace Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPowerTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> upperMask,
	ref AnalogWaveform<float> signalPower,
	ref AnalogWaveform<float> lowerMask
)
```

```text
Public Function FetchPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef upperMask As AnalogWaveform(Of Single),
	ByRef signalPower As AnalogWaveform(Of Single),
	ByRef lowerMask As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **upperMask AnalogWaveformSingle**
  - Upon return, contains the upper mask trace, in dB.
- **signalPower AnalogWaveformSingle**
  - Upon return, contains the signal power trace. This value is expressed in dBm.
- **lowerMask AnalogWaveformSingle**
  - Upon return, contains the lower mask trace. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXPvtResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/21ae890a-6f28-741c-995a-08968a8e17a7.htm language=enus -->
## TOPIC 00010: rfmxgsmdotnet/html/21ae890a-6f28-741c-995a-08968a8e17a7.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/21ae890a-6f28-741c-995a-08968a8e17a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/21ae890a-6f28-741c-995a-08968a8e17a7.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.CloneSignalConfiguration Method

RFmxGsmMXCloneSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int CloneSignalConfiguration(
	string newSignalName,
	out RFmxGsmMX signalConfiguration
)
```

```text
Public Function CloneSignalConfiguration ( 
	newSignalName As String,
	<OutAttribute> ByRef signalConfiguration As RFmxGsmMX
) As Integer
```

###### Parameters

- **newSignalName String**
  - Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName"
- **signalConfiguration RFmxGsmMX**
  - Upon return, contains a new GSM signal instance.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/2365be82-9669-78b7-bf05-b28b2869ea20.htm language=enus -->
## TOPIC 00011: rfmxgsmdotnet/html/2365be82-9669-78b7-bf05-b28b2869ea20.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/2365be82-9669-78b7-bf05-b28b2869ea20.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/2365be82-9669-78b7-bf05-b28b2869ea20.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.GsmMX Namespace

NationalInstruments.RFmx.GsmMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxGsmMX | Defines a root class which is used to identify and control GSM signal configuration. |
|  | RFmxGsmMXConstants | Specifies constants for I/O terminals. |
|  | RFmxGsmMXModAcc | Represents the ModAcc measurement. |
|  | RFmxGsmMXModAccConfiguration | Provides methods to configure the ModAcc measurement |
|  | RFmxGsmMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
|  | RFmxGsmMXOrfs | Represents the ORFS measurement. |
|  | RFmxGsmMXOrfsConfiguration | Provides methods to configure the ORFS measurement |
|  | RFmxGsmMXOrfsResults | Provides methods to fetch and read the ORFS measurement results. |
|  | RFmxGsmMXPvt | Represents the PVT measurement. |
|  | RFmxGsmMXPvtConfiguration | Provides methods to configure the PVT measurement |
|  | RFmxGsmMXPvtResults | Provides methods to fetch and read the PVT measurement results. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | RFmxGsmMXAutoTscDetectionEnabled | Specifies whether the measurement automatically detects the training sequence code (TSC). |
|  | RFmxGsmMXBand | Specifies the operation band. |
|  | RFmxGsmMXBurstSynchronizationType | Specifies the method used to synchronize the burst. |
|  | RFmxGsmMXBurstType | Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method. |
|  | RFmxGsmMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge. |
|  | RFmxGsmMXHBFilterWidth | Specifies the filter width when you set the SetBurstType(String, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
|  | RFmxGsmMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | RFmxGsmMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(String, Double) method with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | RFmxGsmMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | RFmxGsmMXLinkDirection | Specifies the direction for which the frequency is calculated. Only Uplink is supported. |
|  | RFmxGsmMXMeasurementTypes | Specifies the type of measurement. |
|  | RFmxGsmMXModAccAveragingEnabled | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
|  | RFmxGsmMXModAccDetectedTsc | Returns the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. |
|  | RFmxGsmMXModAccDroopCompensationEnabled | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
|  | RFmxGsmMXModulationType | Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
|  | RFmxGsmMXOrfsAveragingEnabled | Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | RFmxGsmMXOrfsAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
|  | RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc | Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
|  | RFmxGsmMXOrfsEvaluationSymbolsScope |  |
|  | RFmxGsmMXOrfsMeasurementType | Specifies the type of spectral distortion to be measured. |
|  | RFmxGsmMXOrfsNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 |
|  | RFmxGsmMXOrfsOffsetFrequencyMode | Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | RFmxGsmMXPropertyId | Specifies all the attribute identifiers. |
|  | RFmxGsmMXPvtAveragingEnabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. |
|  | RFmxGsmMXPvtAveragingType | Specifies the averaging type for multiple acquisitions. |
|  | RFmxGsmMXPvtMeasurementStatus | Indicates the overall measurement status based on standard-defined limits. |
|  | RFmxGsmMXPvtSlotMeasurementStatus | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. |
|  | RFmxGsmMXSignalStructure | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(String, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
|  | RFmxGsmMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
|  | RFmxGsmMXTriggerType | Specifies the trigger type. |
|  | RFmxGsmMXTsc | Specifies the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(String, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/23fe9f76-3eda-4d59-47e1-88d5f5ffc0b2.htm language=enus -->
## TOPIC 00012: rfmxgsmdotnet/html/23fe9f76-3eda-4d59-47e1-88d5f5ffc0b2.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/23fe9f76-3eda-4d59-47e1-88d5f5ffc0b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/23fe9f76-3eda-4d59-47e1-88d5f5ffc0b2.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.AutoLevel Method

RFmxGsmMXAutoLevel Method

SetReferenceLevel(String, Double)

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int AutoLevel(
	string selectorString,
	double measurementInterval,
	out double referenceLevel
)
```

```text
Public Function AutoLevel ( 
	selectorString As String,
	measurementInterval As Double,
	<OutAttribute> ByRef referenceLevel As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementInterval Double**
  - Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal.
- **referenceLevel Double**
  - Upon return, contains the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/266a9c76-dbd2-42c5-58a5-ee059d0fcd77.htm language=enus -->
## TOPIC 00013: rfmxgsmdotnet/html/266a9c76-dbd2-42c5-58a5-ee059d0fcd77.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/266a9c76-dbd2-42c5-58a5-ee059d0fcd77.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/266a9c76-dbd2-42c5-58a5-ee059d0fcd77.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXExtension.GetGsmSignalConfiguration Method

RFmxGsmMXExtensionGetGsmSignalConfiguration Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetGsmSignalConfiguration(RFmxInstrMX) | Creates a new default GSM signal configuration if it doesn't exist; otherwise, it returns the existing default GSM signal configuration. |
|  | GetGsmSignalConfiguration(RFmxInstrMX, String) | Creates a GSM signal configuration for specified signal name. Existing GSM signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxGsmMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/2cbad542-52e0-c7c6-718c-e277550de9eb.htm language=enus -->
## TOPIC 00014: rfmxgsmdotnet/html/2cbad542-52e0-c7c6-718c-e277550de9eb.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/2cbad542-52e0-c7c6-718c-e277550de9eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/2cbad542-52e0-c7c6-718c-e277550de9eb.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ConfigureAutoTscDetectionEnabled Method

RFmxGsmMXConfigureAutoTscDetectionEnabled Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAutoTscDetectionEnabled(
	string selectorString,
	RFmxGsmMXAutoTscDetectionEnabled autoTscDetectionEnabled
)
```

```text
Public Function ConfigureAutoTscDetectionEnabled ( 
	selectorString As String,
	autoTscDetectionEnabled As RFmxGsmMXAutoTscDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **autoTscDetectionEnabled RFmxGsmMXAutoTscDetectionEnabled**
  - Specifies whether to auto detect the TSC.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/2dcba5f0-b597-116d-5a2e-980ba2718f3e.htm language=enus -->
## TOPIC 00015: rfmxgsmdotnet/html/2dcba5f0-b597-116d-5a2e-980ba2718f3e.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/2dcba5f0-b597-116d-5a2e-980ba2718f3e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/2dcba5f0-b597-116d-5a2e-980ba2718f3e.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetOffsetFrequencyMode Method

RFmxGsmMXOrfsConfigurationSetOffsetFrequencyMode Method

Sets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetFrequencyMode(
	string selectorString,
	RFmxGsmMXOrfsOffsetFrequencyMode value
)
```

```text
Public Function SetOffsetFrequencyMode ( 
	selectorString As String,
	value As RFmxGsmMXOrfsOffsetFrequencyMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsOffsetFrequencyMode**
  - Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

###### Return Value

Int32

##### Remarks

OrfsOffsetFrequencyMode

Standard

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/2e79eb45-5b2c-7ec1-3e09-8ac869254564.htm language=enus -->
## TOPIC 00016: rfmxgsmdotnet/html/2e79eb45-5b2c-7ec1-3e09-8ac869254564.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/2e79eb45-5b2c-7ec1-3e09-8ac869254564.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/2e79eb45-5b2c-7ec1-3e09-8ac869254564.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.Pvt Property

RFmxGsmMXPvt Property

RFmxGsmMXPvt

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxGsmMXPvt Pvt { get; }
```

```text
Public ReadOnly Property Pvt As RFmxGsmMXPvt
	Get
```

###### Property Value

RFmxGsmMXPvt

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/347ea766-4c71-1fb4-068f-e329832c0930.htm language=enus -->
## TOPIC 00017: rfmxgsmdotnet/html/347ea766-4c71-1fb4-068f-e329832c0930.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/347ea766-4c71-1fb4-068f-e329832c0930.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/347ea766-4c71-1fb4-068f-e329832c0930.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.ConfigureDroopCompensationEnabled Method

RFmxGsmMXModAccConfigurationConfigureDroopCompensationEnabled Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDroopCompensationEnabled(
	string selectorString,
	RFmxGsmMXModAccDroopCompensationEnabled droopCompensationEnabled
)
```

```text
Public Function ConfigureDroopCompensationEnabled ( 
	selectorString As String,
	droopCompensationEnabled As RFmxGsmMXModAccDroopCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **droopCompensationEnabled RFmxGsmMXModAccDroopCompensationEnabled**
  - Specifies whether to enable droop compensation for the ModAcc measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/34a017f1-595f-074f-b9fa-a4d189316a9b.htm language=enus -->
## TOPIC 00018: rfmxgsmdotnet/html/34a017f1-595f-074f-b9fa-a4d189316a9b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/34a017f1-595f-074f-b9fa-a4d189316a9b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/34a017f1-595f-074f-b9fa-a4d189316a9b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetIQPowerEdgeTriggerSource Method

RFmxGsmMXGetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetIQPowerEdgeTriggerSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Upon return, contains the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3573285f-d2aa-455e-27cd-ea951fa0af5b.htm language=enus -->
## TOPIC 00019: rfmxgsmdotnet/html/3573285f-d2aa-455e-27cd-ea951fa0af5b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3573285f-d2aa-455e-27cd-ea951fa0af5b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3573285f-d2aa-455e-27cd-ea951fa0af5b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ConfigureDigitalEdgeTrigger Method

RFmxGsmMXConfigureDigitalEdgeTrigger Method

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDigitalEdgeTrigger(
	string selectorString,
	string digitalEdgeTriggerSource,
	RFmxGsmMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge,
	double triggerDelay,
	bool enableTrigger
)
```

```text
Public Function ConfigureDigitalEdgeTrigger ( 
	selectorString As String,
	digitalEdgeTriggerSource As String,
	digitalEdgeTriggerEdge As RFmxGsmMXDigitalEdgeTriggerEdge,
	triggerDelay As Double,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **digitalEdgeTriggerSource String**
  - Specifies the source terminal for the digital-edge trigger. Use the string constants from the RFmxGsmMXConstants class or any other valid string to configure this parameter.
- **digitalEdgeTriggerEdge RFmxGsmMXDigitalEdgeTriggerEdge**
  - Specifies the trigger edge to detect.
- **triggerDelay Double**
  - Specifies the trigger delay time. This value is expressed in seconds.
- **enableTrigger Boolean**
  - Specifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/357c711d-596b-4c7e-c792-4a20207815ec.htm language=enus -->
## TOPIC 00020: rfmxgsmdotnet/html/357c711d-596b-4c7e-c792-4a20207815ec.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/357c711d-596b-4c7e-c792-4a20207815ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/357c711d-596b-4c7e-c792-4a20207815ec.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration Methods

RFmxGsmMXOrfsConfiguration Methods

The [RFmxGsmMXOrfsConfiguration](43f41871-dd8a-acab-b078-11ebd4435e12.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | ConfigureEvaluationSymbols | Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify which portion of the burst to measure for ORFS due to Modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average. |
|  | ConfigureMeasurementType | Configures the type of spectral distortion to be measured. |
|  | ConfigureModulationCustomOffsetFrequencyArray(String, Double) | Obsolete. Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureModulationCustomOffsetFrequencyArray(String, Single) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureNoiseCompensationEnabled | Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. supportedDevices: NI 5663/5665, NI 5668R |
|  | ConfigureOffsetFrequencyMode | Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | ConfigureSwitchingCustomOffsetFrequencyArray(String, Double) | Obsolete. Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureSwitchingCustomOffsetFrequencyArray(String, Single) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXOrfsAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
|  | GetEvaluationSymbolsIncludeTsc | Gets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
|  | GetEvaluationSymbolsScope |  |
|  | GetEvaluationSymbolsStart | Gets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | GetEvaluationSymbolsStop | Gets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the output radio frequency spectrum (ORFS) measurement. |
|  | GetMeasurementType | Gets the type of spectral distortion to be measured. |
|  | GetModulationCarrierRbw |  |
|  | GetModulationNumberOfOffsets | Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
|  | GetModulationOffsetFrequency | Gets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
|  | GetModulationOffsetRbw | Gets the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. |
|  | GetNoiseCompensationEnabled | Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetOffsetFrequencyMode | Gets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | GetSwitchingCarrierRbw |  |
|  | GetSwitchingNumberOfOffsets | Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
|  | GetSwitchingOffsetFrequency | Gets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
|  | GetSwitchingOffsetRbw | Gets the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXOrfsAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
|  | SetEvaluationSymbolsIncludeTsc | Sets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
|  | SetEvaluationSymbolsScope |  |
|  | SetEvaluationSymbolsStart | Sets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | SetEvaluationSymbolsStop | Sets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | SetMeasurementEnabled | Sets whether to enable the output radio frequency spectrum (ORFS) measurement. |
|  | SetMeasurementType | Sets the type of spectral distortion to be measured. |
|  | SetModulationCarrierRbw |  |
|  | SetModulationNumberOfOffsets | Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
|  | SetModulationOffsetFrequency | Sets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
|  | SetNoiseCompensationEnabled | Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetOffsetFrequencyMode | Sets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | SetSwitchingCarrierRbw |  |
|  | SetSwitchingNumberOfOffsets | Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
|  | SetSwitchingOffsetFrequency | Sets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3626b89f-f02b-0fd5-b66a-5f22e8a18ebc.htm language=enus -->
## TOPIC 00021: rfmxgsmdotnet/html/3626b89f-f02b-0fd5-b66a-5f22e8a18ebc.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3626b89f-f02b-0fd5-b66a-5f22e8a18ebc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3626b89f-f02b-0fd5-b66a-5f22e8a18ebc.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetOffsetFrequencyMode Method

RFmxGsmMXOrfsConfigurationGetOffsetFrequencyMode Method

Gets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetFrequencyMode(
	string selectorString,
	out RFmxGsmMXOrfsOffsetFrequencyMode value
)
```

```text
Public Function GetOffsetFrequencyMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXOrfsOffsetFrequencyMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsOffsetFrequencyMode**
  - Upon return, contains the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

###### Return Value

Int32

##### Remarks

OrfsOffsetFrequencyMode

Standard

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/36c35e42-9109-56a1-ce07-7513a25683f4.htm language=enus -->
## TOPIC 00022: rfmxgsmdotnet/html/36c35e42-9109-56a1-ce07-7513a25683f4.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/36c35e42-9109-56a1-ce07-7513a25683f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/36c35e42-9109-56a1-ce07-7513a25683f4.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ConfigureFrequencyArfcn Method

RFmxGsmMXConfigureFrequencyArfcn Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFrequencyArfcn(
	string selectorString,
	RFmxGsmMXLinkDirection linkDirection,
	RFmxGsmMXBand band,
	int arfcn
)
```

```text
Public Function ConfigureFrequencyArfcn ( 
	selectorString As String,
	linkDirection As RFmxGsmMXLinkDirection,
	band As RFmxGsmMXBand,
	arfcn As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **linkDirection RFmxGsmMXLinkDirection**
  - Specifies the source of the signal to be measured.
- **band RFmxGsmMXBand**
  - Specifies the band of operation.
- **arfcn Int32**
  - Specifies the ARFCN.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/38f478ee-8d0f-8c4c-f44e-f7986bd54bd9.htm language=enus -->
## TOPIC 00023: rfmxgsmdotnet/html/38f478ee-8d0f-8c4c-f44e-f7986bd54bd9.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/38f478ee-8d0f-8c4c-f44e-f7986bd54bd9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/38f478ee-8d0f-8c4c-f44e-f7986bd54bd9.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ConfigureBand Method

RFmxGsmMXConfigureBand Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureBand(
	string selectorString,
	RFmxGsmMXBand band
)
```

```text
Public Function ConfigureBand ( 
	selectorString As String,
	band As RFmxGsmMXBand
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **band RFmxGsmMXBand**
  - Specifies the band of operation.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3a3be45c-18ec-7998-7fa6-4c0bd0e28fee.htm language=enus -->
## TOPIC 00024: rfmxgsmdotnet/html/3a3be45c-18ec-7998-7fa6-4c0bd0e28fee.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3a3be45c-18ec-7998-7fa6-4c0bd0e28fee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3a3be45c-18ec-7998-7fa6-4c0bd0e28fee.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetMaximumIQOriginOffset Method

RFmxGsmMXModAccResultsGetMaximumIQOriginOffset Method

Gets the maximum of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumIQOriginOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumIQOriginOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsMaximumIQOriginOffset

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3c74b517-923d-0b6f-de70-f85457940d9f.htm language=enus -->
## TOPIC 00025: rfmxgsmdotnet/html/3c74b517-923d-0b6f-de70-f85457940d9f.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3c74b517-923d-0b6f-de70-f85457940d9f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3c74b517-923d-0b6f-de70-f85457940d9f.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMaximumPeakEvm Method

RFmxGsmMXModAccResultsGetEvmMaximumPeakEvm Method

Gets the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumPeakEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumPeakEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMaximumPeakEvm

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3cf0ce56-405b-c817-8f6f-cc3767b1aaa5.htm language=enus -->
## TOPIC 00026: rfmxgsmdotnet/html/3cf0ce56-405b-c817-8f6f-cc3767b1aaa5.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3cf0ce56-405b-c817-8f6f-cc3767b1aaa5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3cf0ce56-405b-c817-8f6f-cc3767b1aaa5.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetSignalStructure Method

RFmxGsmMXSetSignalStructure Method

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

None

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSignalStructure(
	string selectorString,
	RFmxGsmMXSignalStructure value
)
```

```text
Public Function SetSignalStructure ( 
	selectorString As String,
	value As RFmxGsmMXSignalStructure
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXSignalStructure**
  - Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(String, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively.

###### Return Value

Int32

##### Remarks

SignalStructure

Bursted

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3d77a024-51c3-7ae2-95ac-a2ccdb6ea138.htm language=enus -->
## TOPIC 00027: rfmxgsmdotnet/html/3d77a024-51c3-7ae2-95ac-a2ccdb6ea138.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3d77a024-51c3-7ae2-95ac-a2ccdb6ea138.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3d77a024-51c3-7ae2-95ac-a2ccdb6ea138.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.SetNumberOfAnalysisThreads Method

RFmxGsmMXPvtConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfAnalysisThreads(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfAnalysisThreads ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

PvtNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3ddd9f15-5067-7309-1541-aa6a2b1cbdd4.htm language=enus -->
## TOPIC 00028: rfmxgsmdotnet/html/3ddd9f15-5067-7309-1541-aa6a2b1cbdd4.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3ddd9f15-5067-7309-1541-aa6a2b1cbdd4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3ddd9f15-5067-7309-1541-aa6a2b1cbdd4.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.SetAveragingType Method

RFmxGsmMXPvtConfigurationSetAveragingType Method

Sets the averaging type for multiple acquisitions.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxGsmMXPvtAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxGsmMXPvtAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXPvtAveragingType**
  - Specifies the averaging type for multiple acquisitions.

###### Return Value

Int32

##### Remarks

PvtAveragingType

Rms

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3ea1d893-c891-4fe3-d050-e729f2d87b40.htm language=enus -->
## TOPIC 00029: rfmxgsmdotnet/html/3ea1d893-c891-4fe3-d050-e729f2d87b40.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3ea1d893-c891-4fe3-d050-e729f2d87b40.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3ea1d893-c891-4fe3-d050-e729f2d87b40.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsResults.FetchSwitchingPowerTrace Method

RFmxGsmMXOrfsResultsFetchSwitchingPowerTrace Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSwitchingPowerTrace(
	string selectorString,
	double timeout,
	ref float[] offsetFrequency,
	ref float[] absolutePower,
	ref float[] relativePower
)
```

```text
Public Function FetchSwitchingPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef offsetFrequency As Single(),
	ByRef absolutePower As Single(),
	ByRef relativePower As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **offsetFrequency Single**
  - Upon return, contains an array of switching offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz.
- **absolutePower Single**
  - Upon return, contains an array of absolute powers corresponding to the switching offset frequency list. This value is expressed in dBm.
- **relativePower Single**
  - Upon return, contains an array of relative powers corresponding to the switching offset frequencies. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXOrfsResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/3f8c21f4-bae2-39db-30ee-5b52c0eb8100.htm language=enus -->
## TOPIC 00030: rfmxgsmdotnet/html/3f8c21f4-bae2-39db-30ee-5b52c0eb8100.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/3f8c21f4-bae2-39db-30ee-5b52c0eb8100.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/3f8c21f4-bae2-39db-30ee-5b52c0eb8100.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ConfigureIQPowerEdgeTrigger Method

RFmxGsmMXConfigureIQPowerEdgeTrigger Method

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureIQPowerEdgeTrigger(
	string selectorString,
	string iqPowerEdgeTriggerSource,
	RFmxGsmMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope,
	double iqPowerEdgeTriggerLevel,
	double triggerDelay,
	RFmxGsmMXTriggerMinimumQuietTimeMode minimumQuietTimeMode,
	double minimumQuietTimeDuration,
	RFmxGsmMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType,
	bool enableTrigger
)
```

```text
Public Function ConfigureIQPowerEdgeTrigger ( 
	selectorString As String,
	iqPowerEdgeTriggerSource As String,
	iqPowerEdgeTriggerSlope As RFmxGsmMXIQPowerEdgeTriggerSlope,
	iqPowerEdgeTriggerLevel As Double,
	triggerDelay As Double,
	minimumQuietTimeMode As RFmxGsmMXTriggerMinimumQuietTimeMode,
	minimumQuietTimeDuration As Double,
	iqPowerEdgeTriggerLevelType As RFmxGsmMXIQPowerEdgeTriggerLevelType,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **iqPowerEdgeTriggerSource String**
  - Specifies the channel from which the device monitors the trigger.
- **iqPowerEdgeTriggerSlope RFmxGsmMXIQPowerEdgeTriggerSlope**
  - Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify.
- **iqPowerEdgeTriggerLevel Double**
  - Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute.
- **triggerDelay Double**
  - Specifies the trigger delay time. This value is expressed in seconds.
- **minimumQuietTimeMode RFmxGsmMXTriggerMinimumQuietTimeMode**
  - Specifies whether the measurement computes the minimum quiet time used for triggering.
- **minimumQuietTimeDuration Double**
  - Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(String, RFmxGsmMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level.
- **iqPowerEdgeTriggerLevelType RFmxGsmMXIQPowerEdgeTriggerLevelType**
  - Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute.
- **enableTrigger Boolean**
  - Specifies whether the trigger is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/405d2873-2727-e7c1-11ac-fa4345830bad.htm language=enus -->
## TOPIC 00031: rfmxgsmdotnet/html/405d2873-2727-e7c1-11ac-fa4345830bad.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/405d2873-2727-e7c1-11ac-fa4345830bad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/405d2873-2727-e7c1-11ac-fa4345830bad.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetAllTracesEnabled Method

RFmxGsmMXOrfsConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllTracesEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetAllTracesEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsAllTracesEnabled

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/416818a4-d286-2956-d2c3-688f02ef8cf0.htm language=enus -->
## TOPIC 00032: rfmxgsmdotnet/html/416818a4-d286-2956-d2c3-688f02ef8cf0.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/416818a4-d286-2956-d2c3-688f02ef8cf0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/416818a4-d286-2956-d2c3-688f02ef8cf0.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetDigitalEdgeTriggerSource Method

RFmxGsmMXGetDigitalEdgeTriggerSource Method

SetTriggerType(String, RFmxGsmMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDigitalEdgeTriggerSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetDigitalEdgeTriggerSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/418e388b-c1d5-52e0-d634-b76205d126ad.htm language=enus -->
## TOPIC 00033: rfmxgsmdotnet/html/418e388b-c1d5-52e0-d634-b76205d126ad.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/418e388b-c1d5-52e0-d634-b76205d126ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/418e388b-c1d5-52e0-d634-b76205d126ad.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAcc.Results Property

RFmxGsmMXModAccResults Property

RFmxGsmMXModAccResults

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxGsmMXModAccResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxGsmMXModAccResults
	Get
```

###### Property Value

RFmxGsmMXModAccResults

##### See Also

###### Reference

RFmxGsmMXModAcc Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/42a238ab-84e8-92ea-c895-9a023c5998a8.htm language=enus -->
## TOPIC 00034: rfmxgsmdotnet/html/42a238ab-84e8-92ea-c895-9a023c5998a8.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/42a238ab-84e8-92ea-c895-9a023c5998a8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/42a238ab-84e8-92ea-c895-9a023c5998a8.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.Orfs Property

RFmxGsmMXOrfs Property

RFmxGsmMXOrfs

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxGsmMXOrfs Orfs { get; }
```

```text
Public ReadOnly Property Orfs As RFmxGsmMXOrfs
	Get
```

###### Property Value

RFmxGsmMXOrfs

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/42aa2da8-4656-063a-0e4e-5d04fa773542.htm language=enus -->
## TOPIC 00035: rfmxgsmdotnet/html/42aa2da8-4656-063a-0e4e-5d04fa773542.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/42aa2da8-4656-063a-0e4e-5d04fa773542.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/42aa2da8-4656-063a-0e4e-5d04fa773542.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXExtension Methods

RFmxGsmMXExtension Methods

The [RFmxGsmMXExtension](327906a4-4794-11a5-1e21-fc47c93a7c04.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetGsmSignalConfiguration(RFmxInstrMX) | Creates a new default GSM signal configuration if it doesn't exist; otherwise, it returns the existing default GSM signal configuration. |
|  | GetGsmSignalConfiguration(RFmxInstrMX, String) | Creates a GSM signal configuration for specified signal name. Existing GSM signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxGsmMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/43598ee4-6f11-964e-7050-75c175c869f3.htm language=enus -->
## TOPIC 00036: rfmxgsmdotnet/html/43598ee4-6f11-964e-7050-75c175c869f3.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/43598ee4-6f11-964e-7050-75c175c869f3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/43598ee4-6f11-964e-7050-75c175c869f3.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetHBFilterWidth Method

RFmxGsmMXSetHBFilterWidth Method

SetBurstType(String, RFmxGsmMXBurstType)

HB

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetHBFilterWidth(
	string selectorString,
	RFmxGsmMXHBFilterWidth value
)
```

```text
Public Function SetHBFilterWidth ( 
	selectorString As String,
	value As RFmxGsmMXHBFilterWidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the slot number. Example: "slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value RFmxGsmMXHBFilterWidth**
  - Specifies the filter width when you set the SetBurstType(String, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

HBFilterWidth

Narrow

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/43f41871-dd8a-acab-b078-11ebd4435e12.htm language=enus -->
## TOPIC 00037: rfmxgsmdotnet/html/43f41871-dd8a-acab-b078-11ebd4435e12.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/43f41871-dd8a-acab-b078-11ebd4435e12.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/43f41871-dd8a-acab-b078-11ebd4435e12.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration Class

RFmxGsmMXOrfsConfiguration Class

Provides methods to configure the ORFS measurement

##### Inheritance Hierarchy

RFmxGsmMXSubObject

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxGsmMXOrfsConfiguration : RFmxGsmMXSubObject
```

```text
Public NotInheritable Class RFmxGsmMXOrfsConfiguration
	Inherits RFmxGsmMXSubObject
```

The RFmxGsmMXOrfsConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | ConfigureEvaluationSymbols | Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify which portion of the burst to measure for ORFS due to Modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average. |
|  | ConfigureMeasurementType | Configures the type of spectral distortion to be measured. |
|  | ConfigureModulationCustomOffsetFrequencyArray(String, Double) | Obsolete. Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureModulationCustomOffsetFrequencyArray(String, Single) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureNoiseCompensationEnabled | Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. supportedDevices: NI 5663/5665, NI 5668R |
|  | ConfigureOffsetFrequencyMode | Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | ConfigureSwitchingCustomOffsetFrequencyArray(String, Double) | Obsolete. Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureSwitchingCustomOffsetFrequencyArray(String, Single) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXOrfsAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
|  | GetEvaluationSymbolsIncludeTsc | Gets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
|  | GetEvaluationSymbolsScope |  |
|  | GetEvaluationSymbolsStart | Gets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | GetEvaluationSymbolsStop | Gets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the output radio frequency spectrum (ORFS) measurement. |
|  | GetMeasurementType | Gets the type of spectral distortion to be measured. |
|  | GetModulationCarrierRbw |  |
|  | GetModulationNumberOfOffsets | Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
|  | GetModulationOffsetFrequency | Gets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
|  | GetModulationOffsetRbw | Gets the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. |
|  | GetNoiseCompensationEnabled | Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetOffsetFrequencyMode | Gets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | GetSwitchingCarrierRbw |  |
|  | GetSwitchingNumberOfOffsets | Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
|  | GetSwitchingOffsetFrequency | Gets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
|  | GetSwitchingOffsetRbw | Gets the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXOrfsAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
|  | SetEvaluationSymbolsIncludeTsc | Sets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
|  | SetEvaluationSymbolsScope |  |
|  | SetEvaluationSymbolsStart | Sets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | SetEvaluationSymbolsStop | Sets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
|  | SetMeasurementEnabled | Sets whether to enable the output radio frequency spectrum (ORFS) measurement. |
|  | SetMeasurementType | Sets the type of spectral distortion to be measured. |
|  | SetModulationCarrierRbw |  |
|  | SetModulationNumberOfOffsets | Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
|  | SetModulationOffsetFrequency | Sets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
|  | SetNoiseCompensationEnabled | Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetOffsetFrequencyMode | Sets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
|  | SetSwitchingCarrierRbw |  |
|  | SetSwitchingNumberOfOffsets | Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
|  | SetSwitchingOffsetFrequency | Sets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/441d05b0-c238-928c-9c28-7048c70c5f81.htm language=enus -->
## TOPIC 00038: rfmxgsmdotnet/html/441d05b0-c238-928c-9c28-7048c70c5f81.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/441d05b0-c238-928c-9c28-7048c70c5f81.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/441d05b0-c238-928c-9c28-7048c70c5f81.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetWarning Method

RFmxGsmMXGetWarning Method

Gets the latest warning code and description.

Namespace:

NationalInstruments.RFmx.GsmMX

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

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/44ced980-aba6-3226-2f49-4f8ae60503bd.htm language=enus -->
## TOPIC 00039: rfmxgsmdotnet/html/44ced980-aba6-3226-2f49-4f8ae60503bd.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/44ced980-aba6-3226-2f49-4f8ae60503bd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/44ced980-aba6-3226-2f49-4f8ae60503bd.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvt.Results Property

RFmxGsmMXPvtResults Property

RFmxGsmMXPvtResults

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxGsmMXPvtResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxGsmMXPvtResults
	Get
```

###### Property Value

RFmxGsmMXPvtResults

##### See Also

###### Reference

RFmxGsmMXPvt Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4537f60c-f7aa-665b-0101-0b8824f9bdeb.htm language=enus -->
## TOPIC 00040: rfmxgsmdotnet/html/4537f60c-f7aa-665b-0101-0b8824f9bdeb.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4537f60c-f7aa-665b-0101-0b8824f9bdeb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4537f60c-f7aa-665b-0101-0b8824f9bdeb.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetAutoLevelInitialReferenceLevel Method

RFmxGsmMXSetAutoLevelInitialReferenceLevel Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoLevelInitialReferenceLevel(
	string selectorString,
	double value
)
```

```text
Public Function SetAutoLevelInitialReferenceLevel ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the initial reference level the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AutoLevelInitialReferenceLevel

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/45cd8a2c-6b80-e983-dd2a-b4c6ec6dedc2.htm language=enus -->
## TOPIC 00041: rfmxgsmdotnet/html/45cd8a2c-6b80-e983-dd2a-b4c6ec6dedc2.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/45cd8a2c-6b80-e983-dd2a-b4c6ec6dedc2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/45cd8a2c-6b80-e983-dd2a-b4c6ec6dedc2.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.GetMeasurementEnabled Method

RFmxGsmMXPvtConfigurationGetMeasurementEnabled Method

Gets whether to enable the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetMeasurementEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtMeasurementEnabled

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/45d7dd13-4df5-b65e-8676-f432615f0225.htm language=enus -->
## TOPIC 00042: rfmxgsmdotnet/html/45d7dd13-4df5-b65e-8676-f432615f0225.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/45d7dd13-4df5-b65e-8676-f432615f0225.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/45d7dd13-4df5-b65e-8676-f432615f0225.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMeanMagnitudeError Method

RFmxGsmMXModAccResultsGetEvmMeanMagnitudeError Method

Gets the mean of the RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanMagnitudeError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanMagnitudeError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the magnitude error values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMeanMagnitudeError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/469b49a7-487f-53b7-c4b7-68dea06036f6.htm language=enus -->
## TOPIC 00043: rfmxgsmdotnet/html/469b49a7-487f-53b7-c4b7-68dea06036f6.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/469b49a7-487f-53b7-c4b7-68dea06036f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/469b49a7-487f-53b7-c4b7-68dea06036f6.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetResultFetchTimeout Method

RFmxGsmMXSetResultFetchTimeout Method

Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetResultFetchTimeout(
	string selectorString,
	double value
)
```

```text
Public Function SetResultFetchTimeout ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/46bbe56b-dda0-f004-7d36-560c39083492.htm language=enus -->
## TOPIC 00044: rfmxgsmdotnet/html/46bbe56b-dda0-f004-7d36-560c39083492.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/46bbe56b-dda0-f004-7d36-560c39083492.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/46bbe56b-dda0-f004-7d36-560c39083492.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtResults Methods

RFmxGsmMXPvtResults Methods

The [RFmxGsmMXPvtResults](7ae4f1f1-fe93-cfc4-0875-277461bde504.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchMeasurementStatus | Fetches the overall PVT measurement status based on the standard defined measurement limits. |
|  | FetchPowerTrace | Fetches the upper mask, signal power, and lower mask trace. |
|  | FetchSlotMeasurement | Fetches the measurement results for a single-slot PVT measurement. Use "slot(n)" as the selector string to read results from this method. |
|  | FetchSlotMeasurementArray | Fetches the PVT measurement results for each slot. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementStatus | Indicates the overall measurement status based on standard-defined limits. |
|  | GetSlotAveragePower | Gets the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
|  | GetSlotBurstThreshold | Gets the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
|  | GetSlotBurstWidth | Gets the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot(n)" as the selector string to read this method. |
|  | GetSlotMaximumPower | Gets the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
|  | GetSlotMeasurementStatus | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. |
|  | GetSlotMinimumPower | Gets the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxGsmMXPvtResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/46cd44ae-85ff-7005-8201-556e29c8694b.htm language=enus -->
## TOPIC 00045: rfmxgsmdotnet/html/46cd44ae-85ff-7005-8201-556e29c8694b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/46cd44ae-85ff-7005-8201-556e29c8694b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/46cd44ae-85ff-7005-8201-556e29c8694b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetPfer95thPercentilePhaseError Method

RFmxGsmMXModAccResultsGetPfer95thPercentilePhaseError Method

Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPfer95thPercentilePhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetPfer95thPercentilePhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

###### Return Value

Int32

##### Remarks

ModAccResultsPfer95thPercentilePhaseError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/483bb462-01e5-1add-c50a-73bbea99b18c.htm language=enus -->
## TOPIC 00046: rfmxgsmdotnet/html/483bb462-01e5-1add-c50a-73bbea99b18c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/483bb462-01e5-1add-c50a-73bbea99b18c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/483bb462-01e5-1add-c50a-73bbea99b18c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetIQPowerEdgeTriggerLevelType Method

RFmxGsmMXSetIQPowerEdgeTriggerLevelType Method

SetIQPowerEdgeTriggerLevel(String, Double)

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerLevelType(
	string selectorString,
	RFmxGsmMXIQPowerEdgeTriggerLevelType value
)
```

```text
Public Function SetIQPowerEdgeTriggerLevelType ( 
	selectorString As String,
	value As RFmxGsmMXIQPowerEdgeTriggerLevelType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXIQPowerEdgeTriggerLevelType**
  - Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevelType

Relative

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4973c84d-7416-3925-3cd6-8a6a289856f6.htm language=enus -->
## TOPIC 00047: rfmxgsmdotnet/html/4973c84d-7416-3925-3cd6-8a6a289856f6.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4973c84d-7416-3925-3cd6-8a6a289856f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4973c84d-7416-3925-3cd6-8a6a289856f6.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.FetchPfer Method

RFmxGsmMXModAccResultsFetchPfer Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPfer(
	string selectorString,
	double timeout,
	out double meanRmsPhaseError,
	out double maximumRmsPhaseError,
	out double meanPeakPhaseError,
	out double maximumPeakPhaseError,
	out double meanFrequencyError,
	out int peakSymbol
)
```

```text
Public Function FetchPfer ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRmsPhaseError As Double,
	<OutAttribute> ByRef maximumRmsPhaseError As Double,
	<OutAttribute> ByRef meanPeakPhaseError As Double,
	<OutAttribute> ByRef maximumPeakPhaseError As Double,
	<OutAttribute> ByRef meanFrequencyError As Double,
	<OutAttribute> ByRef peakSymbol As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsPhaseError Double**
  - Upon return, contains the mean of RMS phase error values measured over all acquisition time slots. This value is expressed in degrees.
- **maximumRmsPhaseError Double**
  - Upon return, contains the maximum of RMS phase error values measured over all acquisition time slots. This value is expressed in degrees.
- **meanPeakPhaseError Double**
  - Upon return, contains the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees.
- **maximumPeakPhaseError Double**
  - Upon return, contains the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees.
- **meanFrequencyError Double**
  - Upon return, contains the mean of frequency error values measured over all acquisition time slots. This value is expressed in Hz.
- **peakSymbol Int32**
  - Upon return, contains the symbol number in the useful portion of the burst corresponding to phase error value in the maximumPeakPhaseError parameter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/497c5f86-b2d0-b742-336c-3339999d972a.htm language=enus -->
## TOPIC 00048: rfmxgsmdotnet/html/497c5f86-b2d0-b742-336c-3339999d972a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/497c5f86-b2d0-b742-336c-3339999d972a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/497c5f86-b2d0-b742-336c-3339999d972a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetPferMeanFrequencyError Method

RFmxGsmMXModAccResultsGetPferMeanFrequencyError Method

Gets the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPferMeanFrequencyError(
	string selectorString,
	out double value
)
```

```text
Public Function GetPferMeanFrequencyError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsPferMeanFrequencyError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/499e1e2e-aca8-e0ab-a50b-3d71aaece5e4.htm language=enus -->
## TOPIC 00049: rfmxgsmdotnet/html/499e1e2e-aca8-e0ab-a50b-3d71aaece5e4.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/499e1e2e-aca8-e0ab-a50b-3d71aaece5e4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/499e1e2e-aca8-e0ab-a50b-3d71aaece5e4.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsStart Method

RFmxGsmMXOrfsConfigurationSetEvaluationSymbolsStart Method

Sets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvaluationSymbolsStart(
	string selectorString,
	double value
)
```

```text
Public Function SetEvaluationSymbolsStart ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

OrfsEvaluationSymbolsStart

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4a0de894-0fc9-6474-ade3-700060d974c7.htm language=enus -->
## TOPIC 00050: rfmxgsmdotnet/html/4a0de894-0fc9-6474-ade3-700060d974c7.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4a0de894-0fc9-6474-ade3-700060d974c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4a0de894-0fc9-6474-ade3-700060d974c7.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXConstants Class

RFmxGsmMXConstants Class

Specifies constants for I/O terminals.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxGsmMXConstants
```

```text
Public NotInheritable Class RFmxGsmMXConstants
```

The RFmxGsmMXConstants type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622. |
|  | Pfi1 | The signal is exported to the PXI trigger line 0. |
|  | PxieDStarBLine | The trigger is received on the DStar B trigger line. |
|  | PxiStarLine | The signal is exported to the PXI star trigger line. |
|  | PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
|  | PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
|  | PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
|  | PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
|  | PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
|  | PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
|  | PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
|  | PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
|  | TimerEvent | The trigger is received from the timer event. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4a42cdc6-70c0-c551-1931-45cdfae052ae.htm language=enus -->
## TOPIC 00051: rfmxgsmdotnet/html/4a42cdc6-70c0-c551-1931-45cdfae052ae.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4a42cdc6-70c0-c551-1931-45cdfae052ae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4a42cdc6-70c0-c551-1931-45cdfae052ae.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetPowerControlLevel Method

RFmxGsmMXGetPowerControlLevel Method

3GPP TS 45.005 v8.0.0 specifications

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPowerControlLevel(
	string selectorString,
	out int value
)
```

```text
Public Function GetPowerControlLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the slot number. Example: "slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

PowerControlLevel

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4b646398-6ab4-4fe3-6d49-9f0d13a70226.htm language=enus -->
## TOPIC 00052: rfmxgsmdotnet/html/4b646398-6ab4-4fe3-6d49-9f0d13a70226.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4b646398-6ab4-4fe3-6d49-9f0d13a70226.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4b646398-6ab4-4fe3-6d49-9f0d13a70226.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetSelectedPorts Method

RFmxGsmMXSetSelectedPorts Method

Valid values

Default values

Supported devices: PXIe-5820/5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSelectedPorts(
	string selectorString,
	string value
)
```

```text
Public Function SetSelectedPorts ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the instrument port to be used by the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4d5d0c7c-4c4e-07f7-df04-b38da201bab8.htm language=enus -->
## TOPIC 00053: rfmxgsmdotnet/html/4d5d0c7c-4c4e-07f7-df04-b38da201bab8.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4d5d0c7c-4c4e-07f7-df04-b38da201bab8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4d5d0c7c-4c4e-07f7-df04-b38da201bab8.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModulationType Enumeration

RFmxGsmMXModulationType Enumeration

Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXModulationType
```

```text
Public Enumeration RFmxGsmMXModulationType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| ModulationTypeGmsk | 0 | The modulation type is Gaussian minimum shift keying. This value is valid only when you set the SetBurstType(String, RFmxGsmMXBurstType) method to NB. |
| ModulationType8Psk | 1 | The modulation type is 8-PSK. This value is valid only when you set the Burst Type method to NB. |
| ModulationTypeQpsk | 2 | The modulation type is QPSK. This value is valid only when you set the Burst Type method to HB. |
| ModulationType16Qam | 3 | The modulation type is 16-QAM. |
| ModulationType32Qam | 4 | The modulation type is 32-QAM. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4dfc8a9c-4501-0d7e-ca79-edd45abd5fc2.htm language=enus -->
## TOPIC 00054: rfmxgsmdotnet/html/4dfc8a9c-4501-0d7e-ca79-edd45abd5fc2.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4dfc8a9c-4501-0d7e-ca79-edd45abd5fc2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4dfc8a9c-4501-0d7e-ca79-edd45abd5fc2.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.ConfigureSwitchingCustomOffsetFrequencyArray Method

RFmxGsmMXOrfsConfigurationConfigureSwitchingCustomOffsetFrequencyArray Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureSwitchingCustomOffsetFrequencyArray(String, Double) | Obsolete. Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
|  | ConfigureSwitchingCustomOffsetFrequencyArray(String, Single) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |

Top

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4e291442-0f93-712c-87e4-b3eaac1b5b96.htm language=enus -->
## TOPIC 00055: rfmxgsmdotnet/html/4e291442-0f93-712c-87e4-b3eaac1b5b96.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4e291442-0f93-712c-87e4-b3eaac1b5b96.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4e291442-0f93-712c-87e4-b3eaac1b5b96.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetTriggerType Method

RFmxGsmMXGetTriggerType Method

Gets the trigger type.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerType(
	string selectorString,
	out RFmxGsmMXTriggerType value
)
```

```text
Public Function GetTriggerType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXTriggerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXTriggerType**
  - Upon return, contains the trigger type.

###### Return Value

Int32

##### Remarks

TriggerType

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4f1499ef-303a-721a-5c65-98f97c01b30c.htm language=enus -->
## TOPIC 00056: rfmxgsmdotnet/html/4f1499ef-303a-721a-5c65-98f97c01b30c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4f1499ef-303a-721a-5c65-98f97c01b30c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4f1499ef-303a-721a-5c65-98f97c01b30c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtMeasurementStatus Enumeration

RFmxGsmMXPvtMeasurementStatus Enumeration

Indicates the overall measurement status based on standard-defined limits.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXPvtMeasurementStatus
```

```text
Public Enumeration RFmxGsmMXPvtMeasurementStatus
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |
| Pass | 1 | The measurement passed because the average power of all slots is within the standard-defined limits. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/4f8ff948-3779-92ef-a2da-e8cbd6ae0557.htm language=enus -->
## TOPIC 00057: rfmxgsmdotnet/html/4f8ff948-3779-92ef-a2da-e8cbd6ae0557.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/4f8ff948-3779-92ef-a2da-e8cbd6ae0557.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/4f8ff948-3779-92ef-a2da-e8cbd6ae0557.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetPferMaximumPeakPhaseError Method

RFmxGsmMXModAccResultsGetPferMaximumPeakPhaseError Method

Gets the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPferMaximumPeakPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetPferMaximumPeakPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsPferMaximumPeakPhaseError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/504b7161-c93a-ac55-7363-a3eca646c639.htm language=enus -->
## TOPIC 00058: rfmxgsmdotnet/html/504b7161-c93a-ac55-7363-a3eca646c639.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/504b7161-c93a-ac55-7363-a3eca646c639.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/504b7161-c93a-ac55-7363-a3eca646c639.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetIQPowerEdgeTriggerLevel Method

RFmxGsmMXSetIQPowerEdgeTriggerLevel Method

SetIQPowerEdgeTriggerLevelType(String, RFmxGsmMXIQPowerEdgeTriggerLevelType)

Relative

Absolute

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerLevel(
	string selectorString,
	double value
)
```

```text
Public Function SetIQPowerEdgeTriggerLevel ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevel

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/508a89c4-e8b7-ed39-584d-3fe74acd6623.htm language=enus -->
## TOPIC 00059: rfmxgsmdotnet/html/508a89c4-e8b7-ed39-584d-3fe74acd6623.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/508a89c4-e8b7-ed39-584d-3fe74acd6623.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/508a89c4-e8b7-ed39-584d-3fe74acd6623.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ConfigureFrequency Method

RFmxGsmMXConfigureFrequency Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFrequency(
	string selectorString,
	double centerFrequency
)
```

```text
Public Function ConfigureFrequency ( 
	selectorString As String,
	centerFrequency As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **centerFrequency Double**
  - Specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/50d80122-23e0-0c43-74fb-da96c0fd7f70.htm language=enus -->
## TOPIC 00060: rfmxgsmdotnet/html/50d80122-23e0-0c43-74fb-da96c0fd7f70.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/50d80122-23e0-0c43-74fb-da96c0fd7f70.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/50d80122-23e0-0c43-74fb-da96c0fd7f70.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXSignalStructure Enumeration

RFmxGsmMXSignalStructure Enumeration

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

None

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXSignalStructure
```

```text
Public Enumeration RFmxGsmMXSignalStructure
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Bursted | 0 | The signal is bursted. |
| Continuous | 1 | The signal is continuous. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/513eba5b-0dde-5808-723d-1e36f797cf98.htm language=enus -->
## TOPIC 00061: rfmxgsmdotnet/html/513eba5b-0dde-5808-723d-1e36f797cf98.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/513eba5b-0dde-5808-723d-1e36f797cf98.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/513eba5b-0dde-5808-723d-1e36f797cf98.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsMeasurementType Enumeration

RFmxGsmMXOrfsMeasurementType Enumeration

Specifies the type of spectral distortion to be measured.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXOrfsMeasurementType
```

```text
Public Enumeration RFmxGsmMXOrfsMeasurementType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| ModulationAndSwitching | 0 | Measures the spectrum on the modulated part and the switching part of the waveform. |
| Modulation | 1 | Measures the spectrum on the modulated part of the waveform. |
| Switching | 2 | Measures the spectrum on the switching part of the waveform. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/51648bfe-2e3b-3629-c15e-df0690c14d30.htm language=enus -->
## TOPIC 00062: rfmxgsmdotnet/html/51648bfe-2e3b-3629-c15e-df0690c14d30.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/51648bfe-2e3b-3629-c15e-df0690c14d30.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/51648bfe-2e3b-3629-c15e-df0690c14d30.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.SetAveragingCount Method

RFmxGsmMXPvtConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxGsmMXPvtAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingCount(
	string selectorString,
	int value
)
```

```text
Public Function SetAveragingCount ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXPvtAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

PvtAveragingCount

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/52bca11d-a655-92b2-39c3-5a0ecd4de814.htm language=enus -->
## TOPIC 00063: rfmxgsmdotnet/html/52bca11d-a655-92b2-39c3-5a0ecd4de814.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/52bca11d-a655-92b2-39c3-5a0ecd4de814.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/52bca11d-a655-92b2-39c3-5a0ecd4de814.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXDigitalEdgeTriggerEdge Enumeration

RFmxGsmMXDigitalEdgeTriggerEdge Enumeration

SetTriggerType(String, RFmxGsmMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXDigitalEdgeTriggerEdge
```

```text
Public Enumeration RFmxGsmMXDigitalEdgeTriggerEdge
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/540ec1b9-c1bb-055e-c0f6-305824ebd344.htm language=enus -->
## TOPIC 00064: rfmxgsmdotnet/html/540ec1b9-c1bb-055e-c0f6-305824ebd344.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/540ec1b9-c1bb-055e-c0f6-305824ebd344.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/540ec1b9-c1bb-055e-c0f6-305824ebd344.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetModulationNumberOfOffsets Method

RFmxGsmMXOrfsConfigurationGetModulationNumberOfOffsets Method

Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetModulationNumberOfOffsets(
	string selectorString,
	out int value
)
```

```text
Public Function GetModulationNumberOfOffsets ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation.

###### Return Value

Int32

##### Remarks

OrfsModulationNumberOfOffsets

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/54d58a89-a54a-1401-5965-cf1daaac89e1.htm language=enus -->
## TOPIC 00065: rfmxgsmdotnet/html/54d58a89-a54a-1401-5965-cf1daaac89e1.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/54d58a89-a54a-1401-5965-cf1daaac89e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/54d58a89-a54a-1401-5965-cf1daaac89e1.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetMeasurementEnabled Method

RFmxGsmMXOrfsConfigurationSetMeasurementEnabled Method

Sets whether to enable the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementEnabled(
	string selectorString,
	bool value
)
```

```text
Public Function SetMeasurementEnabled ( 
	selectorString As String,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Specifies whether to enable the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsMeasurementEnabled

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/57abe92c-d8f3-87f7-9c9f-415815f4c716.htm language=enus -->
## TOPIC 00066: rfmxgsmdotnet/html/57abe92c-d8f3-87f7-9c9f-415815f4c716.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/57abe92c-d8f3-87f7-9c9f-415815f4c716.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/57abe92c-d8f3-87f7-9c9f-415815f4c716.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.SetAllTracesEnabled Method

RFmxGsmMXModAccConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAllTracesEnabled(
	string selectorString,
	bool value
)
```

```text
Public Function SetAllTracesEnabled ( 
	selectorString As String,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

###### Return Value

Int32

##### Remarks

ModAccAllTracesEnabled

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/58f3b1d6-5254-255c-f8bd-3a1f0a929c6d.htm language=enus -->
## TOPIC 00067: rfmxgsmdotnet/html/58f3b1d6-5254-255c-f8bd-3a1f0a929c6d.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/58f3b1d6-5254-255c-f8bd-3a1f0a929c6d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/58f3b1d6-5254-255c-f8bd-3a1f0a929c6d.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults Class

RFmxGsmMXModAccResults Class

Provides methods to fetch and read the ModAcc measurement results.

##### Inheritance Hierarchy

RFmxGsmMXSubObject

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxGsmMXModAccResults : RFmxGsmMXSubObject
```

```text
Public NotInheritable Class RFmxGsmMXModAccResults
	Inherits RFmxGsmMXSubObject
```

The RFmxGsmMXModAccResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchConstellationTrace | Fetches the constellation trace concatenated over all slots for the last acquistion. |
|  | FetchDemodulatedBits | Fetches the array of demodulated bits concatenated over all slots for the last acquisition. |
|  | FetchDetectedTsc | Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. Use "slot(n)" as the selector string to read results from this method. |
|  | FetchDetectedTscArray | Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. |
|  | FetchEvm | Fetches the EVM measurement results for EDGE/EGPRS. |
|  | FetchEvmAmplitudeDroop | Fetches the amplitude droop measurement results for EDGE/EGPRS. |
|  | FetchEvmMagnitudeError | Fetches the RMS values of the magnitude error measurement results for EDGE/EGPRS. |
|  | FetchEvmPhaseError | Fetches the phase error measurement results for EDGE/EGPRS. |
|  | FetchEvmTrace | Fetches the EDGE/EGPRS RMS EVM trace concatenated over all slots for the last acquisition. |
|  | FetchIQImpairments | Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS. |
|  | FetchMagnitudeErrorTrace | Fetches the EDGE/EGPRS magnitude error trace concatenated over all slots for the last acquisition. |
|  | FetchPfer | Fetches the phase and frequency error measurement results for GSM. |
|  | FetchPhaseErrorTrace | Fetches the phase error trace concatenated over all slots for the last acquisition. |
|  | GetDetectedTsc | Gets the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. |
|  | GetEvm95thPercentileEvm | Gets the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvm95thPercentileMagnitudeError | Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
|  | GetEvm95thPercentilePhaseError | Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
|  | GetEvmMaximumAmplitudeDroop | Gets the maximum of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumFrequencyError | Gets the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumMagnitudeError | Gets the maximum of the RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumPeakEvm | Gets the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumPeakMagnitudeError | Gets the maximum of peak magnitude error measured over all timeslots of all acquisitions. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
|  | GetEvmMaximumPeakPhaseError | Gets the maximum of peak phase error measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
|  | GetEvmMaximumPhaseError | Gets the maximum of the RMS values of phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumRmsEvm | Gets the maximum of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanAmplitudeDroop | Gets the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanFrequencyError | Gets the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanMagnitudeError | Gets the mean of the RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanPeakEvm | Gets the mean of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanPeakMagnitudeError | Returns the mean of peak magnitude error measured over all timeslots of all acquisitions. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
|  | GetEvmMeanPeakPhaseError | Gets the mean of peak phase error measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
|  | GetEvmMeanPhaseError | Gets the mean of the RMS values of phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanRmsEvm | Gets the mean of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmPeakEvmSymbol | Gets the symbol number in the burst measurement interval that corresponds to the EVM value returned by the GetEvmMaximumPeakEvm(String, Double) result. The method returns this result for EDGE/EGPRS measurements. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMaximumIQGainImbalance | Gets the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
|  | GetMaximumIQOriginOffset | Gets the maximum of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
|  | GetMeanIQGainImbalance | Gets the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
|  | GetMeanIQOriginOffset | Gets the mean of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
|  | GetPfer95thPercentilePhaseError | Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. |
|  | GetPferMaximumFrequencyError | Gets the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMaximumPeakPhaseError | Gets the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMaximumRmsPhaseError | Gets the maximum of the RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMeanFrequencyError | Gets the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMeanPeakPhaseError | Gets the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMeanRmsPhaseError | Gets the mean of the RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferPeakPhaseErrorSymbol | Gets the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(String, Double) result. The method returns this result for GSM ModAcc measurements. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5a182ffe-514e-42cb-eac6-e5c62ae3b5a6.htm language=enus -->
## TOPIC 00068: rfmxgsmdotnet/html/5a182ffe-514e-42cb-eac6-e5c62ae3b5a6.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5a182ffe-514e-42cb-eac6-e5c62ae3b5a6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5a182ffe-514e-42cb-eac6-e5c62ae3b5a6.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.DeleteSignalConfiguration Method

RFmxGsmMXDeleteSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int DeleteSignalConfiguration()
```

```text
Public Function DeleteSignalConfiguration As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5d03174a-f89a-d8d5-b3e5-914f8675642a.htm language=enus -->
## TOPIC 00069: rfmxgsmdotnet/html/5d03174a-f89a-d8d5-b3e5-914f8675642a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5d03174a-f89a-d8d5-b3e5-914f8675642a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5d03174a-f89a-d8d5-b3e5-914f8675642a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.FetchDetectedTsc Method

RFmxGsmMXModAccResultsFetchDetectedTsc Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDetectedTsc(
	string selectorString,
	double timeout,
	out RFmxGsmMXModAccDetectedTsc detectedTsc
)
```

```text
Public Function FetchDetectedTsc ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef detectedTsc As RFmxGsmMXModAccDetectedTsc
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and slot number. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"slot0""result::r1/slot0" You can use the BuildSlotString(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **detectedTsc RFmxGsmMXModAccDetectedTsc**
  - Upon return, contains the detected TSC when you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5e1f4117-4efb-8b5c-e8c2-7d8f7557772a.htm language=enus -->
## TOPIC 00070: rfmxgsmdotnet/html/5e1f4117-4efb-8b5c-e8c2-7d8f7557772a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5e1f4117-4efb-8b5c-e8c2-7d8f7557772a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5e1f4117-4efb-8b5c-e8c2-7d8f7557772a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXBurstSynchronizationType Enumeration

RFmxGsmMXBurstSynchronizationType Enumeration

Specifies the method used to synchronize the burst.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXBurstSynchronizationType
```

```text
Public Enumeration RFmxGsmMXBurstSynchronizationType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Tsc | 0 | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| Amplitude | 1 | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |
| None | 2 | Sets the T0 point to 273.23 microseconds after the trigger. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5ea50df3-ecc2-4916-4f85-b500516aeea2.htm language=enus -->
## TOPIC 00071: rfmxgsmdotnet/html/5ea50df3-ecc2-4916-4f85-b500516aeea2.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5ea50df3-ecc2-4916-4f85-b500516aeea2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5ea50df3-ecc2-4916-4f85-b500516aeea2.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsAveragingType Enumeration

RFmxGsmMXOrfsAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXOrfsAveragingType
```

```text
Public Enumeration RFmxGsmMXOrfsAveragingType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The measurement averages the power spectrum in a logarithmic scale. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5eaa62e6-aafa-7285-c676-1ea78648ede2.htm language=enus -->
## TOPIC 00072: rfmxgsmdotnet/html/5eaa62e6-aafa-7285-c676-1ea78648ede2.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5eaa62e6-aafa-7285-c676-1ea78648ede2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5eaa62e6-aafa-7285-c676-1ea78648ede2.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMeanAmplitudeDroop Method

RFmxGsmMXModAccResultsGetEvmMeanAmplitudeDroop Method

Gets the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanAmplitudeDroop(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanAmplitudeDroop ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMeanAmplitudeDroop

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5eeede94-4151-13f9-67da-38ec1f4c32ad.htm language=enus -->
## TOPIC 00073: rfmxgsmdotnet/html/5eeede94-4151-13f9-67da-38ec1f4c32ad.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5eeede94-4151-13f9-67da-38ec1f4c32ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5eeede94-4151-13f9-67da-38ec1f4c32ad.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.Initiate Method

RFmxGsmMXInitiate Method

WaitForMeasurementComplete(String, Double)

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int Initiate(
	string selectorString,
	string resultName
)
```

```text
Public Function Initiate ( 
	selectorString As String,
	resultName As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **resultName String**
  - Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1"

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5f2296bc-7567-cbea-a241-2752067c181c.htm language=enus -->
## TOPIC 00074: rfmxgsmdotnet/html/5f2296bc-7567-cbea-a241-2752067c181c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5f2296bc-7567-cbea-a241-2752067c181c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5f2296bc-7567-cbea-a241-2752067c181c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetAveragingType Method

RFmxGsmMXOrfsConfigurationSetAveragingType Method

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxGsmMXOrfsAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxGsmMXOrfsAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsAveragingType**
  - Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsAveragingType

Log

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/5fd47a84-8efb-b774-3ce4-a206ff60d85a.htm language=enus -->
## TOPIC 00075: rfmxgsmdotnet/html/5fd47a84-8efb-b774-3ce4-a206ff60d85a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/5fd47a84-8efb-b774-3ce4-a206ff60d85a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/5fd47a84-8efb-b774-3ce4-a206ff60d85a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtResults.FetchSlotMeasurementArray Method

RFmxGsmMXPvtResultsFetchSlotMeasurementArray Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSlotMeasurementArray(
	string selectorString,
	double timeout,
	ref double[] slotAveragePower,
	ref double[] slotBurstWidth,
	ref RFmxGsmMXPvtSlotMeasurementStatus[] slotMeasurementStatus,
	ref double[] slotMaximumPower,
	ref double[] slotMinimumPower,
	ref double[] slotBurstThreshold
)
```

```text
Public Function FetchSlotMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef slotAveragePower As Double(),
	ByRef slotBurstWidth As Double(),
	ByRef slotMeasurementStatus As RFmxGsmMXPvtSlotMeasurementStatus(),
	ByRef slotMaximumPower As Double(),
	ByRef slotMinimumPower As Double(),
	ByRef slotBurstThreshold As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **slotAveragePower Double**
  - Upon return, contains an array of mean powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm.
- **slotBurstWidth Double**
  - Upon return, contains an array of burst widths for the slots where the -3 dB transition points occur. This value is expressed in seconds.
- **slotMeasurementStatus RFmxGsmMXPvtSlotMeasurementStatus**
  - Indicates an array of PVT measurement statuses for multiple slots.
- **slotMaximumPower Double**
  - Upon return, contains an array of maximum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm.
- **slotMinimumPower Double**
  - Upon return, contains an array of minimum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm.
- **slotBurstThreshold Double**
  - Upon return, contains an array of thresholds that the PVT measurement uses to determine the burst validity. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXPvtResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/60781207-d382-d91e-70f9-2ef9c873a7f8.htm language=enus -->
## TOPIC 00076: rfmxgsmdotnet/html/60781207-d382-d91e-70f9-2ef9c873a7f8.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/60781207-d382-d91e-70f9-2ef9c873a7f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/60781207-d382-d91e-70f9-2ef9c873a7f8.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsIncludeTsc Method

RFmxGsmMXOrfsConfigurationSetEvaluationSymbolsIncludeTsc Method

Sets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvaluationSymbolsIncludeTsc(
	string selectorString,
	RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc value
)
```

```text
Public Function SetEvaluationSymbolsIncludeTsc ( 
	selectorString As String,
	value As RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc**
  - Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsEvaluationSymbolsIncludeTsc

False

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/61236fc3-f498-0f08-9f8e-a0b9f560c723.htm language=enus -->
## TOPIC 00077: rfmxgsmdotnet/html/61236fc3-f498-0f08-9f8e-a0b9f560c723.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/61236fc3-f498-0f08-9f8e-a0b9f560c723.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/61236fc3-f498-0f08-9f8e-a0b9f560c723.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetSwitchingOffsetFrequency Method

RFmxGsmMXOrfsConfigurationSetSwitchingOffsetFrequency Method

Sets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSwitchingOffsetFrequency(
	string selectorString,
	float value
)
```

```text
Public Function SetSwitchingOffsetFrequency ( 
	selectorString As String,
	value As Single
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Single**
  - Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

OrfsSwitchingOffsetFrequency

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/63510d2e-df24-1ffb-d171-0839fc019376.htm language=enus -->
## TOPIC 00078: rfmxgsmdotnet/html/63510d2e-df24-1ffb-d171-0839fc019376.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/63510d2e-df24-1ffb-d171-0839fc019376.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/63510d2e-df24-1ffb-d171-0839fc019376.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccDroopCompensationEnabled Enumeration

RFmxGsmMXModAccDroopCompensationEnabled Enumeration

Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXModAccDroopCompensationEnabled
```

```text
Public Enumeration RFmxGsmMXModAccDroopCompensationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables power droop compensation in the EVM measurement. |
| True | 1 | Enables power droop compensation in the EVM measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/64413534-b698-3858-ba25-09de7c2d530e.htm language=enus -->
## TOPIC 00079: rfmxgsmdotnet/html/64413534-b698-3858-ba25-09de7c2d530e.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/64413534-b698-3858-ba25-09de7c2d530e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/64413534-b698-3858-ba25-09de7c2d530e.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMaximumAmplitudeDroop Method

RFmxGsmMXModAccResultsGetEvmMaximumAmplitudeDroop Method

Gets the maximum of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumAmplitudeDroop(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumAmplitudeDroop ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMaximumAmplitudeDroop

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/64ecc8d8-b07e-89ae-bebc-5c3a9ca5f8db.htm language=enus -->
## TOPIC 00080: rfmxgsmdotnet/html/64ecc8d8-b07e-89ae-bebc-5c3a9ca5f8db.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/64ecc8d8-b07e-89ae-bebc-5c3a9ca5f8db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/64ecc8d8-b07e-89ae-bebc-5c3a9ca5f8db.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetTriggerDelay Method

RFmxGsmMXSetTriggerDelay Method

Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerDelay(
	string selectorString,
	double value
)
```

```text
Public Function SetTriggerDelay ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

###### Return Value

Int32

##### Remarks

TriggerDelay

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/7150ae0e-bd00-07c5-5b26-c5289c00c488.htm language=enus -->
## TOPIC 00081: rfmxgsmdotnet/html/7150ae0e-bd00-07c5-5b26-c5289c00c488.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/7150ae0e-bd00-07c5-5b26-c5289c00c488.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/7150ae0e-bd00-07c5-5b26-c5289c00c488.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMaximumPeakMagnitudeError Method

RFmxGsmMXModAccResultsGetEvmMaximumPeakMagnitudeError Method

Gets the maximum of peak magnitude error measured over all timeslots of all acquisitions. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumPeakMagnitudeError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumPeakMagnitudeError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMaximumPeakMagnitudeError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/71789870-0cb1-4a95-e92b-d0290e1139d2.htm language=enus -->
## TOPIC 00082: rfmxgsmdotnet/html/71789870-0cb1-4a95-e92b-d0290e1139d2.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/71789870-0cb1-4a95-e92b-d0290e1139d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/71789870-0cb1-4a95-e92b-d0290e1139d2.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetDetectedTsc Method

RFmxGsmMXModAccResultsGetDetectedTsc Method

SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType)

Tsc

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectedTsc(
	string selectorString,
	out RFmxGsmMXModAccDetectedTsc value
)
```

```text
Public Function GetDetectedTsc ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXModAccDetectedTsc
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value RFmxGsmMXModAccDetectedTsc**
  - Upon return, contains the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsDetectedTsc

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/74ee8811-3239-a3d5-cbb2-0ca061802472.htm language=enus -->
## TOPIC 00083: rfmxgsmdotnet/html/74ee8811-3239-a3d5-cbb2-0ca061802472.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/74ee8811-3239-a3d5-cbb2-0ca061802472.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/74ee8811-3239-a3d5-cbb2-0ca061802472.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetAttributeString Method

RFmxGsmMXGetAttributeString Method

Gets the value of a of an RFmx string.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeString(
	string selectorString,
	int attributeIdentifier,
	out string value
)
```

```text
Public Function GetAttributeString ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value String**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/75463a04-8048-cc13-41ed-76547d1a5398.htm language=enus -->
## TOPIC 00084: rfmxgsmdotnet/html/75463a04-8048-cc13-41ed-76547d1a5398.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/75463a04-8048-cc13-41ed-76547d1a5398.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/75463a04-8048-cc13-41ed-76547d1a5398.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAcc Properties

RFmxGsmMXModAcc Properties

The [RFmxGsmMXModAcc](555984ad-3f56-e845-0029-f7a5159e623f.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxGsmMXModAccConfiguration instance that provides methods to configure the ModAcc measurement |
|  | Results | Gets the RFmxGsmMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Top

##### See Also

###### Reference

RFmxGsmMXModAcc Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/771b02cc-213a-7b31-5906-330a337e1672.htm language=enus -->
## TOPIC 00085: rfmxgsmdotnet/html/771b02cc-213a-7b31-5906-330a337e1672.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/771b02cc-213a-7b31-5906-330a337e1672.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/771b02cc-213a-7b31-5906-330a337e1672.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ClearAllNamedResults Method

RFmxGsmMXClearAllNamedResults Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ClearAllNamedResults(
	string selectorString
)
```

```text
Public Function ClearAllNamedResults ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/8311fa4f-e91c-f8e5-a539-69768bbe61a3.htm language=enus -->
## TOPIC 00086: rfmxgsmdotnet/html/8311fa4f-e91c-f8e5-a539-69768bbe61a3.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/8311fa4f-e91c-f8e5-a539-69768bbe61a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/8311fa4f-e91c-f8e5-a539-69768bbe61a3.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetAttributeInt Method

RFmxGsmMXSetAttributeInt Method

Sets the value of a Int attribute.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeInt(
	string selectorString,
	int attributeIdentifier,
	int value
)
```

```text
Public Function SetAttributeInt ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/85bc9080-6d87-6475-677f-59d653fdf928.htm language=enus -->
## TOPIC 00087: rfmxgsmdotnet/html/85bc9080-6d87-6475-677f-59d653fdf928.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/85bc9080-6d87-6475-677f-59d653fdf928.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/85bc9080-6d87-6475-677f-59d653fdf928.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMaximumFrequencyError Method

RFmxGsmMXModAccResultsGetEvmMaximumFrequencyError Method

Gets the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumFrequencyError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumFrequencyError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMaximumFrequencyError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/865435a5-6982-53ef-f804-b0547a316526.htm language=enus -->
## TOPIC 00088: rfmxgsmdotnet/html/865435a5-6982-53ef-f804-b0547a316526.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/865435a5-6982-53ef-f804-b0547a316526.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/865435a5-6982-53ef-f804-b0547a316526.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXConstants.Pfi0 Field

RFmxGsmMXConstantsPfi0 Field

The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public const string Pfi0 = "PFI0"
```

```text
Public Const Pfi0 As String = "PFI0"
```

###### Field Value

String

##### See Also

###### Reference

RFmxGsmMXConstants Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/9105011f-38c9-1ed1-e609-37232759c07b.htm language=enus -->
## TOPIC 00089: rfmxgsmdotnet/html/9105011f-38c9-1ed1-e609-37232759c07b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/9105011f-38c9-1ed1-e609-37232759c07b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/9105011f-38c9-1ed1-e609-37232759c07b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetError Method

RFmxGsmMXGetError Method

Gets the latest error code and description.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetError(
	out int errorCode,
	out string errorDescription
)
```

```text
Public Function GetError ( 
	<OutAttribute> ByRef errorCode As Integer,
	<OutAttribute> ByRef errorDescription As String
) As Integer
```

###### Parameters

- **errorCode Int32**
  - Upon return, contains the latest error code.
- **errorDescription String**
  - Upon return, contains the latest error description.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/9529deac-4f8a-5781-80ad-d6c69c8c9096.htm language=enus -->
## TOPIC 00090: rfmxgsmdotnet/html/9529deac-4f8a-5781-80ad-d6c69c8c9096.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/9529deac-4f8a-5781-80ad-d6c69c8c9096.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/9529deac-4f8a-5781-80ad-d6c69c8c9096.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetEvaluationSymbolsStop Method

RFmxGsmMXOrfsConfigurationGetEvaluationSymbolsStop Method

Gets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvaluationSymbolsStop(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvaluationSymbolsStop ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

OrfsEvaluationSymbolsStop

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/95800c35-349a-cc55-4536-d6cc9ef2d872.htm language=enus -->
## TOPIC 00091: rfmxgsmdotnet/html/95800c35-349a-cc55-4536-d6cc9ef2d872.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/95800c35-349a-cc55-4536-d6cc9ef2d872.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/95800c35-349a-cc55-4536-d6cc9ef2d872.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetIQPowerEdgeTriggerLevel Method

RFmxGsmMXGetIQPowerEdgeTriggerLevel Method

SetIQPowerEdgeTriggerLevelType(String, RFmxGsmMXIQPowerEdgeTriggerLevelType)

Relative

Absolute

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQPowerEdgeTriggerLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevel

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/969f5d60-2332-3b9d-5b07-c2055adf65c0.htm language=enus -->
## TOPIC 00092: rfmxgsmdotnet/html/969f5d60-2332-3b9d-5b07-c2055adf65c0.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/969f5d60-2332-3b9d-5b07-c2055adf65c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/969f5d60-2332-3b9d-5b07-c2055adf65c0.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsStop Method

RFmxGsmMXOrfsConfigurationSetEvaluationSymbolsStop Method

Sets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvaluationSymbolsStop(
	string selectorString,
	double value
)
```

```text
Public Function SetEvaluationSymbolsStop ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

OrfsEvaluationSymbolsStop

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/9a9e407a-87b4-19ea-5b7e-d244b8f22d28.htm language=enus -->
## TOPIC 00093: rfmxgsmdotnet/html/9a9e407a-87b4-19ea-5b7e-d244b8f22d28.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/9a9e407a-87b4-19ea-5b7e-d244b8f22d28.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/9a9e407a-87b4-19ea-5b7e-d244b8f22d28.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetSwitchingOffsetFrequency Method

RFmxGsmMXOrfsConfigurationGetSwitchingOffsetFrequency Method

Gets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSwitchingOffsetFrequency(
	string selectorString,
	out float value
)
```

```text
Public Function GetSwitchingOffsetFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Single
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Single**
  - Upon return, contains the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

OrfsSwitchingOffsetFrequency

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/9b4805a9-4bea-9194-7b79-9e386b4ac950.htm language=enus -->
## TOPIC 00094: rfmxgsmdotnet/html/9b4805a9-4bea-9194-7b79-9e386b4ac950.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/9b4805a9-4bea-9194-7b79-9e386b4ac950.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/9b4805a9-4bea-9194-7b79-9e386b4ac950.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.ConfigureSwitchingCustomOffsetFrequencyArray(String, Single[]) Method

RFmxGsmMXOrfsConfigurationConfigureSwitchingCustomOffsetFrequencyArray(String, Single) Method

SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode)

Custom

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSwitchingCustomOffsetFrequencyArray(
	string selectorString,
	float[] switchingCustomOffsetFrequency
)
```

```text
Public Function ConfigureSwitchingCustomOffsetFrequencyArray ( 
	selectorString As String,
	switchingCustomOffsetFrequency As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **switchingCustomOffsetFrequency Single**
  - Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

ConfigureSwitchingCustomOffsetFrequencyArray Overload

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/9c4712f3-aa27-bc56-f33c-bfd5b19725c9.htm language=enus -->
## TOPIC 00095: rfmxgsmdotnet/html/9c4712f3-aa27-bc56-f33c-bfd5b19725c9.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/9c4712f3-aa27-bc56-f33c-bfd5b19725c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/9c4712f3-aa27-bc56-f33c-bfd5b19725c9.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetBand Method

RFmxGsmMXSetBand Method

Sets the operation band.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetBand(
	string selectorString,
	RFmxGsmMXBand value
)
```

```text
Public Function SetBand ( 
	selectorString As String,
	value As RFmxGsmMXBand
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXBand**
  - Specifies the operation band.

###### Return Value

Int32

##### Remarks

Band

Pgsm

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/9ec9c72e-64f2-e56a-bbd8-f6dc873d3c0c.htm language=enus -->
## TOPIC 00096: rfmxgsmdotnet/html/9ec9c72e-64f2-e56a-bbd8-f6dc873d3c0c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/9ec9c72e-64f2-e56a-bbd8-f6dc873d3c0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/9ec9c72e-64f2-e56a-bbd8-f6dc873d3c0c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetLimitedConfigurationChange Method

RFmxGsmMXSetLimitedConfigurationChange Method

Sets the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLimitedConfigurationChange(
	string selectorString,
	RFmxGsmMXLimitedConfigurationChange value
)
```

```text
Public Function SetLimitedConfigurationChange ( 
	selectorString As String,
	value As RFmxGsmMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXLimitedConfigurationChange**
  - Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

Disabled

Disabled

LimitedConfigurationChange

Disabled

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b13a5819-4ce9-82d2-71e5-0a0eff4c0277.htm language=enus -->
## TOPIC 00097: rfmxgsmdotnet/html/b13a5819-4ce9-82d2-71e5-0a0eff4c0277.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b13a5819-4ce9-82d2-71e5-0a0eff4c0277.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b13a5819-4ce9-82d2-71e5-0a0eff4c0277.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsResults.FetchModulationPowerTrace Method

RFmxGsmMXOrfsResultsFetchModulationPowerTrace Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchModulationPowerTrace(
	string selectorString,
	double timeout,
	ref float[] offsetFrequency,
	ref float[] absolutePower,
	ref float[] relativePower
)
```

```text
Public Function FetchModulationPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef offsetFrequency As Single(),
	ByRef absolutePower As Single(),
	ByRef relativePower As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **offsetFrequency Single**
  - Upon return, contains an array of modulation offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz.
- **absolutePower Single**
  - Upon return, contains an array of absolute powers corresponding to the modulation offset frequency list. This value is expressed in dBm.
- **relativePower Single**
  - Upon return, contains an array of relative powers corresponding to modulation offset frequency list. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXOrfsResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b3503930-4ae7-1e5d-c8ad-13f4dfcb6808.htm language=enus -->
## TOPIC 00098: rfmxgsmdotnet/html/b3503930-4ae7-1e5d-c8ad-13f4dfcb6808.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b3503930-4ae7-1e5d-c8ad-13f4dfcb6808.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b3503930-4ae7-1e5d-c8ad-13f4dfcb6808.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetBurstType Method

RFmxGsmMXGetBurstType Method

Gets the burst type. Use "slot(n)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstType(
	string selectorString,
	out RFmxGsmMXBurstType value
)
```

```text
Public Function GetBurstType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXBurstType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the slot number. Example: "slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value RFmxGsmMXBurstType**
  - Upon return, contains the burst type. Use "slot(n)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

BurstType

NB

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b3a26708-8c39-c507-f848-771b410dfa61.htm language=enus -->
## TOPIC 00099: rfmxgsmdotnet/html/b3a26708-8c39-c507-f848-771b410dfa61.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b3a26708-8c39-c507-f848-771b410dfa61.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b3a26708-8c39-c507-f848-771b410dfa61.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetPferMaximumRmsPhaseError Method

RFmxGsmMXModAccResultsGetPferMaximumRmsPhaseError Method

Gets the maximum of the RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPferMaximumRmsPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetPferMaximumRmsPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsPferMaximumRmsPhaseError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b43ce463-c60a-9649-b211-f0fba596ab8d.htm language=enus -->
## TOPIC 00100: rfmxgsmdotnet/html/b43ce463-c60a-9649-b211-f0fba596ab8d.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b43ce463-c60a-9649-b211-f0fba596ab8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b43ce463-c60a-9649-b211-f0fba596ab8d.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.FetchEvm Method

RFmxGsmMXModAccResultsFetchEvm Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEvm(
	string selectorString,
	double timeout,
	out double meanRmsEvm,
	out double maximumRmsEvm,
	out double meanPeakEvm,
	out double maximumPeakEvm,
	out double ninetyFifthPercentileEvm,
	out double meanFrequencyError,
	out int peakEvmSymbol
)
```

```text
Public Function FetchEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRmsEvm As Double,
	<OutAttribute> ByRef maximumRmsEvm As Double,
	<OutAttribute> ByRef meanPeakEvm As Double,
	<OutAttribute> ByRef maximumPeakEvm As Double,
	<OutAttribute> ByRef ninetyFifthPercentileEvm As Double,
	<OutAttribute> ByRef meanFrequencyError As Double,
	<OutAttribute> ByRef peakEvmSymbol As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsEvm Double**
  - Upon return, contains the mean of RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage.
- **maximumRmsEvm Double**
  - Upon return, contains the maximum of RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage.
- **meanPeakEvm Double**
  - Upon return, contains the mean of peak EVM values measured over all acquisition time slots. This value is expressed as a percentage.
- **maximumPeakEvm Double**
  - Upon return, contains the maximum of peak EVM values measured over all acquisition time slots. This value is expressed as a percentage.
- **ninetyFifthPercentileEvm Double**
  - Upon return, contains the EVM value, at which no more than 5 percent of the symbols have an EVM exceeding this value. This value is expressed as a percentage.
- **meanFrequencyError Double**
  - Upon return, contains the mean of frequency error values measured over all acquisition time slots. This value is expressed in Hz.
- **peakEvmSymbol Int32**
  - Upon return, contains the symbol number in the burst measurement interval corresponding to the EVM value returned by the maximumPeakEVM parameter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b56cb663-bda4-df2b-478e-ea472a9c9864.htm language=enus -->
## TOPIC 00101: rfmxgsmdotnet/html/b56cb663-bda4-df2b-478e-ea472a9c9864.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b56cb663-bda4-df2b-478e-ea472a9c9864.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b56cb663-bda4-df2b-478e-ea472a9c9864.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.GetAllTracesEnabled Method

RFmxGsmMXPvtConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllTracesEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetAllTracesEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtAllTracesEnabled

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b601c502-4963-aec9-91f0-fe103a27d25a.htm language=enus -->
## TOPIC 00102: rfmxgsmdotnet/html/b601c502-4963-aec9-91f0-fe103a27d25a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b601c502-4963-aec9-91f0-fe103a27d25a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b601c502-4963-aec9-91f0-fe103a27d25a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXBurstType Enumeration

RFmxGsmMXBurstType Enumeration

Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXBurstType
```

```text
Public Enumeration RFmxGsmMXBurstType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| NB | 0 | The burst type is Normal Burst. |
| HB | 1 | The burst type is Higher Symbol Rate Burst. |
| AB | 2 | The burst type is Access Burst. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/b63a6663-3f12-bc71-4f61-dd6ad203098d.htm language=enus -->
## TOPIC 00103: rfmxgsmdotnet/html/b63a6663-3f12-bc71-4f61-dd6ad203098d.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/b63a6663-3f12-bc71-4f61-dd6ad203098d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/b63a6663-3f12-bc71-4f61-dd6ad203098d.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetNumberOfTimeslots Method

RFmxGsmMXGetNumberOfTimeslots Method

Gets the number of time slots to be measured.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfTimeslots(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfTimeslots ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of time slots to be measured.

###### Return Value

Int32

##### Remarks

NumberOfTimeslots

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c1525e2a-a3cf-c6b1-72cf-70ac274e9ff7.htm language=enus -->
## TOPIC 00104: rfmxgsmdotnet/html/c1525e2a-a3cf-c6b1-72cf-70ac274e9ff7.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c1525e2a-a3cf-c6b1-72cf-70ac274e9ff7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c1525e2a-a3cf-c6b1-72cf-70ac274e9ff7.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetPferPeakPhaseErrorSymbol Method

RFmxGsmMXModAccResultsGetPferPeakPhaseErrorSymbol Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPferPeakPhaseErrorSymbol(
	string selectorString,
	out int value
)
```

```text
Public Function GetPferPeakPhaseErrorSymbol ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Int32**
  - Upon return, contains the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(String, Double) result. The method returns this result for GSM ModAcc measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsPferPeakPhaseErrorSymbol

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c215be01-c492-87ec-42b8-4873becfae3b.htm language=enus -->
## TOPIC 00105: rfmxgsmdotnet/html/c215be01-c492-87ec-42b8-4873becfae3b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c215be01-c492-87ec-42b8-4873becfae3b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c215be01-c492-87ec-42b8-4873becfae3b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration Methods

RFmxGsmMXModAccConfiguration Methods

The [RFmxGsmMXModAccConfiguration](e5d49e40-e3a8-7d6d-2fb8-ba785a1af023.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the modulation accuracy (ModAcc) measurement. |
|  | ConfigureDroopCompensationEnabled | Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXModAccAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
|  | GetDroopCompensationEnabled | Gets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXModAccAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
|  | SetDroopCompensationEnabled | Sets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
|  | SetMeasurementEnabled | Sets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c2baee89-16d3-10bc-fcd6-96deeb5bd517.htm language=enus -->
## TOPIC 00106: rfmxgsmdotnet/html/c2baee89-16d3-10bc-fcd6-96deeb5bd517.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c2baee89-16d3-10bc-fcd6-96deeb5bd517.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c2baee89-16d3-10bc-fcd6-96deeb5bd517.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtSlotMeasurementStatus Enumeration

RFmxGsmMXPvtSlotMeasurementStatus Enumeration

Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXPvtSlotMeasurementStatus
```

```text
Public Enumeration RFmxGsmMXPvtSlotMeasurementStatus
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The average power for at least one slot is outside the standard-defined limits. |
| Pass | 1 | The average power for each slot is within the standard-defined limits. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c4613179-4f72-7e8f-1399-6011a9d77932.htm language=enus -->
## TOPIC 00107: rfmxgsmdotnet/html/c4613179-4f72-7e8f-1399-6011a9d77932.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c4613179-4f72-7e8f-1399-6011a9d77932.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c4613179-4f72-7e8f-1399-6011a9d77932.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.ConfigureAveraging Method

RFmxGsmMXModAccConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxGsmMXModAccAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxGsmMXModAccAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxGsmMXModAccAveragingEnabled**
  - Specifies whether to enable averaging for the measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c4c9d59b-6351-9b84-3b1f-d261bad11b57.htm language=enus -->
## TOPIC 00108: rfmxgsmdotnet/html/c4c9d59b-6351-9b84-3b1f-d261bad11b57.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c4c9d59b-6351-9b84-3b1f-d261bad11b57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c4c9d59b-6351-9b84-3b1f-d261bad11b57.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMeanRmsEvm Method

RFmxGsmMXModAccResultsGetEvmMeanRmsEvm Method

Gets the mean of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanRmsEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanRmsEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMeanRmsEvm

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c6c2c13b-e965-2ebb-28b3-5b930df939d6.htm language=enus -->
## TOPIC 00109: rfmxgsmdotnet/html/c6c2c13b-e965-2ebb-28b3-5b930df939d6.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c6c2c13b-e965-2ebb-28b3-5b930df939d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c6c2c13b-e965-2ebb-28b3-5b930df939d6.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults Methods

RFmxGsmMXModAccResults Methods

The [RFmxGsmMXModAccResults](58f3b1d6-5254-255c-f8bd-3a1f0a929c6d.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchConstellationTrace | Fetches the constellation trace concatenated over all slots for the last acquistion. |
|  | FetchDemodulatedBits | Fetches the array of demodulated bits concatenated over all slots for the last acquisition. |
|  | FetchDetectedTsc | Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. Use "slot(n)" as the selector string to read results from this method. |
|  | FetchDetectedTscArray | Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. |
|  | FetchEvm | Fetches the EVM measurement results for EDGE/EGPRS. |
|  | FetchEvmAmplitudeDroop | Fetches the amplitude droop measurement results for EDGE/EGPRS. |
|  | FetchEvmMagnitudeError | Fetches the RMS values of the magnitude error measurement results for EDGE/EGPRS. |
|  | FetchEvmPhaseError | Fetches the phase error measurement results for EDGE/EGPRS. |
|  | FetchEvmTrace | Fetches the EDGE/EGPRS RMS EVM trace concatenated over all slots for the last acquisition. |
|  | FetchIQImpairments | Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS. |
|  | FetchMagnitudeErrorTrace | Fetches the EDGE/EGPRS magnitude error trace concatenated over all slots for the last acquisition. |
|  | FetchPfer | Fetches the phase and frequency error measurement results for GSM. |
|  | FetchPhaseErrorTrace | Fetches the phase error trace concatenated over all slots for the last acquisition. |
|  | GetDetectedTsc | Gets the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. |
|  | GetEvm95thPercentileEvm | Gets the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvm95thPercentileMagnitudeError | Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
|  | GetEvm95thPercentilePhaseError | Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
|  | GetEvmMaximumAmplitudeDroop | Gets the maximum of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumFrequencyError | Gets the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumMagnitudeError | Gets the maximum of the RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumPeakEvm | Gets the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumPeakMagnitudeError | Gets the maximum of peak magnitude error measured over all timeslots of all acquisitions. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
|  | GetEvmMaximumPeakPhaseError | Gets the maximum of peak phase error measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
|  | GetEvmMaximumPhaseError | Gets the maximum of the RMS values of phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMaximumRmsEvm | Gets the maximum of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanAmplitudeDroop | Gets the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanFrequencyError | Gets the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanMagnitudeError | Gets the mean of the RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanPeakEvm | Gets the mean of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanPeakMagnitudeError | Returns the mean of peak magnitude error measured over all timeslots of all acquisitions. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
|  | GetEvmMeanPeakPhaseError | Gets the mean of peak phase error measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
|  | GetEvmMeanPhaseError | Gets the mean of the RMS values of phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmMeanRmsEvm | Gets the mean of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
|  | GetEvmPeakEvmSymbol | Gets the symbol number in the burst measurement interval that corresponds to the EVM value returned by the GetEvmMaximumPeakEvm(String, Double) result. The method returns this result for EDGE/EGPRS measurements. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMaximumIQGainImbalance | Gets the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
|  | GetMaximumIQOriginOffset | Gets the maximum of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
|  | GetMeanIQGainImbalance | Gets the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
|  | GetMeanIQOriginOffset | Gets the mean of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
|  | GetPfer95thPercentilePhaseError | Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. |
|  | GetPferMaximumFrequencyError | Gets the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMaximumPeakPhaseError | Gets the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMaximumRmsPhaseError | Gets the maximum of the RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMeanFrequencyError | Gets the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMeanPeakPhaseError | Gets the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferMeanRmsPhaseError | Gets the mean of the RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
|  | GetPferPeakPhaseErrorSymbol | Gets the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(String, Double) result. The method returns this result for GSM ModAcc measurements. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c6ef218a-1be1-fb20-cde8-03070fa340f4.htm language=enus -->
## TOPIC 00110: rfmxgsmdotnet/html/c6ef218a-1be1-fb20-cde8-03070fa340f4.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c6ef218a-1be1-fb20-cde8-03070fa340f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c6ef218a-1be1-fb20-cde8-03070fa340f4.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetHBFilterWidth Method

RFmxGsmMXGetHBFilterWidth Method

SetBurstType(String, RFmxGsmMXBurstType)

HB

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHBFilterWidth(
	string selectorString,
	out RFmxGsmMXHBFilterWidth value
)
```

```text
Public Function GetHBFilterWidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXHBFilterWidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the slot number. Example: "slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value RFmxGsmMXHBFilterWidth**
  - Upon return, contains the filter width when you set the SetBurstType(String, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

HBFilterWidth

Narrow

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/c7f12dc5-4723-ddf2-9b71-d6fe35390767.htm language=enus -->
## TOPIC 00111: rfmxgsmdotnet/html/c7f12dc5-4723-ddf2-9b71-d6fe35390767.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/c7f12dc5-4723-ddf2-9b71-d6fe35390767.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/c7f12dc5-4723-ddf2-9b71-d6fe35390767.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.ResetAttribute Method

RFmxGsmMXResetAttribute Method

Resets the attribute to its default value.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ResetAttribute(
	string selectorString,
	RFmxGsmMXPropertyId attributeId
)
```

```text
Public Function ResetAttribute ( 
	selectorString As String,
	attributeId As RFmxGsmMXPropertyId
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2K Help for more information about configuring the selector string.
- **attributeId RFmxGsmMXPropertyId**
  - Specifies an attribute identifier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/ce9adb43-6481-4e2c-f1c5-4c66a1f29f06.htm language=enus -->
## TOPIC 00112: rfmxgsmdotnet/html/ce9adb43-6481-4e2c-f1c5-4c66a1f29f06.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/ce9adb43-6481-4e2c-f1c5-4c66a1f29f06.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/ce9adb43-6481-4e2c-f1c5-4c66a1f29f06.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsScope Method

RFmxGsmMXOrfsConfigurationSetEvaluationSymbolsScope Method

[Missing <summary> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsScope(System.String,NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsEvaluationSymbolsScope)"]

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvaluationSymbolsScope(
	string selectorString,
	RFmxGsmMXOrfsEvaluationSymbolsScope value
)
```

```text
Public Function SetEvaluationSymbolsScope ( 
	selectorString As String,
	value As RFmxGsmMXOrfsEvaluationSymbolsScope
) As Integer
```

###### Parameters

- **selectorString String**
  - [Missing <param name="selectorString"/> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsScope(System.String,NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsEvaluationSymbolsScope)"]
- **value RFmxGsmMXOrfsEvaluationSymbolsScope**
  - [Missing <param name="value"/> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsScope(System.String,NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsEvaluationSymbolsScope)"]

###### Return Value

Int32

[Missing <returns> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetEvaluationSymbolsScope(System.String,NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsEvaluationSymbolsScope)"]

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/cedf107c-0380-7200-d8a0-c4ef267999c4.htm language=enus -->
## TOPIC 00113: rfmxgsmdotnet/html/cedf107c-0380-7200-d8a0-c4ef267999c4.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/cedf107c-0380-7200-d8a0-c4ef267999c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/cedf107c-0380-7200-d8a0-c4ef267999c4.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtAveragingEnabled Enumeration

RFmxGsmMXPvtAveragingEnabled Enumeration

Specifies whether to enable averaging for the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXPvtAveragingEnabled
```

```text
Public Enumeration RFmxGsmMXPvtAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement is averaged over multiple acquisitions. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/cefe8047-ea16-4fea-b9e6-b798b97d5a21.htm language=enus -->
## TOPIC 00114: rfmxgsmdotnet/html/cefe8047-ea16-4fea-b9e6-b798b97d5a21.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/cefe8047-ea16-4fea-b9e6-b798b97d5a21.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/cefe8047-ea16-4fea-b9e6-b798b97d5a21.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetSwitchingNumberOfOffsets Method

RFmxGsmMXOrfsConfigurationGetSwitchingNumberOfOffsets Method

Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSwitchingNumberOfOffsets(
	string selectorString,
	out int value
)
```

```text
Public Function GetSwitchingNumberOfOffsets ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching.

###### Return Value

Int32

##### Remarks

OrfsSwitchingNumberOfOffsets

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/cf6d6290-17d0-5002-59d4-08a2b5d6d183.htm language=enus -->
## TOPIC 00115: rfmxgsmdotnet/html/cf6d6290-17d0-5002-59d4-08a2b5d6d183.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/cf6d6290-17d0-5002-59d4-08a2b5d6d183.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/cf6d6290-17d0-5002-59d4-08a2b5d6d183.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.GetAllTracesEnabled Method

RFmxGsmMXModAccConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllTracesEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetAllTracesEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

###### Return Value

Int32

##### Remarks

ModAccAllTracesEnabled

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d023d9d3-e04e-c3e9-822e-417b7f5fed99.htm language=enus -->
## TOPIC 00116: rfmxgsmdotnet/html/d023d9d3-e04e-c3e9-822e-417b7f5fed99.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d023d9d3-e04e-c3e9-822e-417b7f5fed99.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d023d9d3-e04e-c3e9-822e-417b7f5fed99.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetMeasurementType Method

RFmxGsmMXOrfsConfigurationSetMeasurementType Method

Sets the type of spectral distortion to be measured.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementType(
	string selectorString,
	RFmxGsmMXOrfsMeasurementType value
)
```

```text
Public Function SetMeasurementType ( 
	selectorString As String,
	value As RFmxGsmMXOrfsMeasurementType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsMeasurementType**
  - Specifies the type of spectral distortion to be measured.

###### Return Value

Int32

##### Remarks

OrfsMeasurementType

ModulationAndSwitching

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d15202ac-2575-a346-f1ab-170670429592.htm language=enus -->
## TOPIC 00117: rfmxgsmdotnet/html/d15202ac-2575-a346-f1ab-170670429592.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d15202ac-2575-a346-f1ab-170670429592.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d15202ac-2575-a346-f1ab-170670429592.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetLinkDirection Method

RFmxGsmMXGetLinkDirection Method

Gets the source of the signal to be measured.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLinkDirection(
	string selectorString,
	out RFmxGsmMXLinkDirection value
)
```

```text
Public Function GetLinkDirection ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXLinkDirection
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXLinkDirection**
  - Upon return, contains the source of the signal to be measured.

###### Return Value

Int32

##### Remarks

LinkDirection

Uplink

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d2e10fc1-0627-4aa9-d9ad-4b6bad10fc7c.htm language=enus -->
## TOPIC 00118: rfmxgsmdotnet/html/d2e10fc1-0627-4aa9-d9ad-4b6bad10fc7c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d2e10fc1-0627-4aa9-d9ad-4b6bad10fc7c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d2e10fc1-0627-4aa9-d9ad-4b6bad10fc7c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetAveragingEnabled Method

RFmxGsmMXOrfsConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxGsmMXOrfsAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXOrfsAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsAveragingEnabled**
  - Upon return, contains whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsAveragingEnabled

False

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d4dbdd09-22ad-3aa4-4de3-26b364a5c26a.htm language=enus -->
## TOPIC 00119: rfmxgsmdotnet/html/d4dbdd09-22ad-3aa4-4de3-26b364a5c26a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d4dbdd09-22ad-3aa4-4de3-26b364a5c26a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d4dbdd09-22ad-3aa4-4de3-26b364a5c26a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtResults.FetchMeasurementStatus Method

RFmxGsmMXPvtResultsFetchMeasurementStatus Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurementStatus(
	string selectorString,
	double timeout,
	out RFmxGsmMXPvtMeasurementStatus measurementStatus
)
```

```text
Public Function FetchMeasurementStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxGsmMXPvtMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus RFmxGsmMXPvtMeasurementStatus**
  - Indicates the overall measurement status based on standard-defined limits.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXPvtResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d595bdb5-d73f-061b-a3b4-d6480e4794b1.htm language=enus -->
## TOPIC 00120: rfmxgsmdotnet/html/d595bdb5-d73f-061b-a3b4-d6480e4794b1.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d595bdb5-d73f-061b-a3b4-d6480e4794b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d595bdb5-d73f-061b-a3b4-d6480e4794b1.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfs Methods

RFmxGsmMXOrfs Methods

The [RFmxGsmMXOrfs](91127f11-94f0-f934-9ba7-e2e45208e67b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxGsmMXOrfs Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d59e89ee-477b-e387-6929-410c13bf6bd9.htm language=enus -->
## TOPIC 00121: rfmxgsmdotnet/html/d59e89ee-477b-e387-6929-410c13bf6bd9.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d59e89ee-477b-e387-6929-410c13bf6bd9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d59e89ee-477b-e387-6929-410c13bf6bd9.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.ConfigureOffsetFrequencyMode Method

RFmxGsmMXOrfsConfigurationConfigureOffsetFrequencyMode Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetFrequencyMode(
	string selectorString,
	RFmxGsmMXOrfsOffsetFrequencyMode offsetFrequencyMode
)
```

```text
Public Function ConfigureOffsetFrequencyMode ( 
	selectorString As String,
	offsetFrequencyMode As RFmxGsmMXOrfsOffsetFrequencyMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetFrequencyMode RFmxGsmMXOrfsOffsetFrequencyMode**
  - Specifies the list of frequency offsets for which you can perform the ORFS measurements.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d5eed5ef-912e-4a9f-88f2-2959e6d959a3.htm language=enus -->
## TOPIC 00122: rfmxgsmdotnet/html/d5eed5ef-912e-4a9f-88f2-2959e6d959a3.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d5eed5ef-912e-4a9f-88f2-2959e6d959a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d5eed5ef-912e-4a9f-88f2-2959e6d959a3.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.ConfigureSwitchingCustomOffsetFrequencyArray(String, Double[]) Method

RFmxGsmMXOrfsConfigurationConfigureSwitchingCustomOffsetFrequencyArray(String, Double) Method

**Note: This API is now obsolete.**

SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode)

Custom

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use ConfigureSwitchingCustomOffsetFrequencyArray(string selectorString, float[] switchingCustomOffsetFrequency) method to configure")]
public int ConfigureSwitchingCustomOffsetFrequencyArray(
	string selectorString,
	double[] switchingCustomOffsetFrequency
)
```

```text
<ObsoleteAttribute("Use ConfigureSwitchingCustomOffsetFrequencyArray(string selectorString, float[] switchingCustomOffsetFrequency) method to configure")>
Public Function ConfigureSwitchingCustomOffsetFrequencyArray ( 
	selectorString As String,
	switchingCustomOffsetFrequency As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **switchingCustomOffsetFrequency Double**
  - Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(String, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement.

###### Return Value

Int32

##### Remarks

This method is obsoleted. Use ConfigureSwitchingCustomOffsetFrequencyArray(string selectorString, float[] switchingCustomOffsetFrequency) method to configure.

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

ConfigureSwitchingCustomOffsetFrequencyArray Overload

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d67c30c0-c065-5790-f5d6-d350b2e0c57e.htm language=enus -->
## TOPIC 00123: rfmxgsmdotnet/html/d67c30c0-c065-5790-f5d6-d350b2e0c57e.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d67c30c0-c065-5790-f5d6-d350b2e0c57e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d67c30c0-c065-5790-f5d6-d350b2e0c57e.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetMeasurementEnabled Method

RFmxGsmMXOrfsConfigurationGetMeasurementEnabled Method

Gets whether to enable the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetMeasurementEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsMeasurementEnabled

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d6fe613f-d847-49c1-7b6f-bff3f01587b7.htm language=enus -->
## TOPIC 00124: rfmxgsmdotnet/html/d6fe613f-d847-49c1-7b6f-bff3f01587b7.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d6fe613f-d847-49c1-7b6f-bff3f01587b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d6fe613f-d847-49c1-7b6f-bff3f01587b7.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsResults.FetchModulationResultsArray Method

RFmxGsmMXOrfsResultsFetchModulationResultsArray Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchModulationResultsArray(
	string selectorString,
	double timeout,
	out double modulationCarrierPower,
	ref double[] lowerRelativePower,
	ref double[] upperRelativePower,
	ref double[] lowerAbsolutePower,
	ref double[] upperAbsolutePower
)
```

```text
Public Function FetchModulationResultsArray ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef modulationCarrierPower As Double,
	ByRef lowerRelativePower As Double(),
	ByRef upperRelativePower As Double(),
	ByRef lowerAbsolutePower As Double(),
	ByRef upperAbsolutePower As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **modulationCarrierPower Double**
  - Upon return, contains the modulation carrier power. This value is expressed in dBm.
- **lowerRelativePower Double**
  - Upon return, contains an array of relative powers measured at the negative modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier.
- **upperRelativePower Double**
  - Upon return, contains an array of relative powers measured at the positive modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier.
- **lowerAbsolutePower Double**
  - Upon return, contains an array of absolute powers measured at the negative modulation offset frequencies. This value is expressed in dBm.
- **upperAbsolutePower Double**
  - Upon return, contains an array of absolute powers measured at the positive modulation offset frequencies. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXOrfsResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d77dd11e-de72-6fba-603e-e698f68c10eb.htm language=enus -->
## TOPIC 00125: rfmxgsmdotnet/html/d77dd11e-de72-6fba-603e-e698f68c10eb.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d77dd11e-de72-6fba-603e-e698f68c10eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d77dd11e-de72-6fba-603e-e698f68c10eb.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SelectMeasurements Method

RFmxGsmMXSelectMeasurements Method

Specifies the measurements that you want to enable.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SelectMeasurements(
	string selectorString,
	RFmxGsmMXMeasurementTypes measurement,
	bool enableAllTraces
)
```

```text
Public Function SelectMeasurements ( 
	selectorString As String,
	measurement As RFmxGsmMXMeasurementTypes,
	enableAllTraces As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurement RFmxGsmMXMeasurementTypes**
  - Specifies the measurement to perform.
- **enableAllTraces Boolean**
  - to enable all traces for the selected measurement; otherwise .

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d79dacfe-17d2-496e-e11b-cadc0a2a6480.htm language=enus -->
## TOPIC 00126: rfmxgsmdotnet/html/d79dacfe-17d2-496e-e11b-cadc0a2a6480.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d79dacfe-17d2-496e-e11b-cadc0a2a6480.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d79dacfe-17d2-496e-e11b-cadc0a2a6480.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXConstants Fields

RFmxGsmMXConstants Fields

The [RFmxGsmMXConstants](4a0de894-0fc9-6474-ade3-700060d974c7.htm) type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622. |
|  | Pfi1 | The signal is exported to the PXI trigger line 0. |
|  | PxieDStarBLine | The trigger is received on the DStar B trigger line. |
|  | PxiStarLine | The signal is exported to the PXI star trigger line. |
|  | PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
|  | PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
|  | PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
|  | PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
|  | PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
|  | PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
|  | PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
|  | PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
|  | TimerEvent | The trigger is received from the timer event. |

Top

##### See Also

###### Reference

RFmxGsmMXConstants Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d7fb9e1e-29b5-ea1b-ee7a-310d4c90e3c0.htm language=enus -->
## TOPIC 00127: rfmxgsmdotnet/html/d7fb9e1e-29b5-ea1b-ee7a-310d4c90e3c0.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d7fb9e1e-29b5-ea1b-ee7a-310d4c90e3c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d7fb9e1e-29b5-ea1b-ee7a-310d4c90e3c0.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetDigitalEdgeTriggerEdge Method

RFmxGsmMXSetDigitalEdgeTriggerEdge Method

SetTriggerType(String, RFmxGsmMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerEdge(
	string selectorString,
	RFmxGsmMXDigitalEdgeTriggerEdge value
)
```

```text
Public Function SetDigitalEdgeTriggerEdge ( 
	selectorString As String,
	value As RFmxGsmMXDigitalEdgeTriggerEdge
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXDigitalEdgeTriggerEdge**
  - Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerEdge

Rising

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d85231ff-33a8-eb25-bed1-48047275c231.htm language=enus -->
## TOPIC 00128: rfmxgsmdotnet/html/d85231ff-33a8-eb25-bed1-48047275c231.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d85231ff-33a8-eb25-bed1-48047275c231.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d85231ff-33a8-eb25-bed1-48047275c231.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.GetAveragingCount Method

RFmxGsmMXModAccConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxGsmMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingCount(
	string selectorString,
	out int value
)
```

```text
Public Function GetAveragingCount ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXModAccAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ModAccAveragingCount

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/d91efc8c-9007-160c-1b02-39652151ca97.htm language=enus -->
## TOPIC 00129: rfmxgsmdotnet/html/d91efc8c-9007-160c-1b02-39652151ca97.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/d91efc8c-9007-160c-1b02-39652151ca97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/d91efc8c-9007-160c-1b02-39652151ca97.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.SetDroopCompensationEnabled Method

RFmxGsmMXModAccConfigurationSetDroopCompensationEnabled Method

Sets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDroopCompensationEnabled(
	string selectorString,
	RFmxGsmMXModAccDroopCompensationEnabled value
)
```

```text
Public Function SetDroopCompensationEnabled ( 
	selectorString As String,
	value As RFmxGsmMXModAccDroopCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXModAccDroopCompensationEnabled**
  - Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

###### Return Value

Int32

##### Remarks

ModAccDroopCompensationEnabled

False

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/dac15084-8e99-2111-e335-77937840ee97.htm language=enus -->
## TOPIC 00130: rfmxgsmdotnet/html/dac15084-8e99-2111-e335-77937840ee97.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/dac15084-8e99-2111-e335-77937840ee97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/dac15084-8e99-2111-e335-77937840ee97.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.WaitForMeasurementComplete Method

RFmxGsmMXWaitForMeasurementComplete Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int WaitForMeasurementComplete(
	string selectorString,
	double timeout
)
```

```text
Public Function WaitForMeasurementComplete ( 
	selectorString As String,
	timeout As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/dbb394eb-09a5-4e48-ec22-79444a71a861.htm language=enus -->
## TOPIC 00131: rfmxgsmdotnet/html/dbb394eb-09a5-4e48-ec22-79444a71a861.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/dbb394eb-09a5-4e48-ec22-79444a71a861.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/dbb394eb-09a5-4e48-ec22-79444a71a861.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetModulationCarrierRbw Method

RFmxGsmMXOrfsConfigurationSetModulationCarrierRbw Method

[Missing <summary> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetModulationCarrierRbw(System.String,System.Double)"]

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetModulationCarrierRbw(
	string selectorString,
	double value
)
```

```text
Public Function SetModulationCarrierRbw ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - [Missing <param name="selectorString"/> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetModulationCarrierRbw(System.String,System.Double)"]
- **value Double**
  - [Missing <param name="value"/> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetModulationCarrierRbw(System.String,System.Double)"]

###### Return Value

Int32

[Missing <returns> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetModulationCarrierRbw(System.String,System.Double)"]

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/dd74c061-b11e-f14c-aa0a-b6952875a3cf.htm language=enus -->
## TOPIC 00132: rfmxgsmdotnet/html/dd74c061-b11e-f14c-aa0a-b6952875a3cf.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/dd74c061-b11e-f14c-aa0a-b6952875a3cf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/dd74c061-b11e-f14c-aa0a-b6952875a3cf.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetAttributeInt Method

RFmxGsmMXGetAttributeInt Method

Gets the value of an RFmx 32-bit integer (int32) attribute.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeInt(
	string selectorString,
	int attributeIdentifier,
	out int value
)
```

```text
Public Function GetAttributeInt ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e00d1e76-26db-b37f-4da9-23dc5a8afbe4.htm language=enus -->
## TOPIC 00133: rfmxgsmdotnet/html/e00d1e76-26db-b37f-4da9-23dc5a8afbe4.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e00d1e76-26db-b37f-4da9-23dc5a8afbe4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e00d1e76-26db-b37f-4da9-23dc5a8afbe4.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.FetchMagnitudeErrorTrace Method

RFmxGsmMXModAccResultsFetchMagnitudeErrorTrace Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMagnitudeErrorTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> magnitudeError
)
```

```text
Public Function FetchMagnitudeErrorTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef magnitudeError As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **magnitudeError AnalogWaveformSingle**
  - Upon return, contains the magnitude error trace. This value is expressed as a percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e07ffa13-8780-a50d-363e-d685e551831b.htm language=enus -->
## TOPIC 00134: rfmxgsmdotnet/html/e07ffa13-8780-a50d-363e-d685e551831b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e07ffa13-8780-a50d-363e-d685e551831b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e07ffa13-8780-a50d-363e-d685e551831b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.GetEvaluationSymbolsIncludeTsc Method

RFmxGsmMXOrfsConfigurationGetEvaluationSymbolsIncludeTsc Method

Gets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvaluationSymbolsIncludeTsc(
	string selectorString,
	out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc value
)
```

```text
Public Function GetEvaluationSymbolsIncludeTsc ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc**
  - Upon return, contains whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

###### Return Value

Int32

##### Remarks

OrfsEvaluationSymbolsIncludeTsc

False

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e20560f3-7ac9-8a39-d684-6b319e43a0f1.htm language=enus -->
## TOPIC 00135: rfmxgsmdotnet/html/e20560f3-7ac9-8a39-d684-6b319e43a0f1.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e20560f3-7ac9-8a39-d684-6b319e43a0f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e20560f3-7ac9-8a39-d684-6b319e43a0f1.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.FetchConstellationTrace Method

RFmxGsmMXModAccResultsFetchConstellationTrace Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] constellation
)
```

```text
Public Function FetchConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef constellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **constellation ComplexSingle**
  - Upon return, contains the constellation trace concatenated over all slots for the last acquisition.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e2559a67-dacd-e3cc-8793-7476dd95575b.htm language=enus -->
## TOPIC 00136: rfmxgsmdotnet/html/e2559a67-dacd-e3cc-8793-7476dd95575b.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e2559a67-dacd-e3cc-8793-7476dd95575b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e2559a67-dacd-e3cc-8793-7476dd95575b.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXOrfsConfiguration.SetSwitchingCarrierRbw Method

RFmxGsmMXOrfsConfigurationSetSwitchingCarrierRbw Method

[Missing <summary> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetSwitchingCarrierRbw(System.String,System.Double)"]

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSwitchingCarrierRbw(
	string selectorString,
	double value
)
```

```text
Public Function SetSwitchingCarrierRbw ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - [Missing <param name="selectorString"/> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetSwitchingCarrierRbw(System.String,System.Double)"]
- **value Double**
  - [Missing <param name="value"/> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetSwitchingCarrierRbw(System.String,System.Double)"]

###### Return Value

Int32

[Missing <returns> documentation for "M:NationalInstruments.RFmx.GsmMX.RFmxGsmMXOrfsConfiguration.SetSwitchingCarrierRbw(System.String,System.Double)"]

##### See Also

###### Reference

RFmxGsmMXOrfsConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e3161a6a-9e07-6d7d-18e9-5e62a234e708.htm language=enus -->
## TOPIC 00137: rfmxgsmdotnet/html/e3161a6a-9e07-6d7d-18e9-5e62a234e708.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e3161a6a-9e07-6d7d-18e9-5e62a234e708.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e3161a6a-9e07-6d7d-18e9-5e62a234e708.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXIQPowerEdgeTriggerLevelType Enumeration

RFmxGsmMXIQPowerEdgeTriggerLevelType Enumeration

SetIQPowerEdgeTriggerLevel(String, Double)

SetTriggerType(String, RFmxGsmMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXIQPowerEdgeTriggerLevelType
```

```text
Public Enumeration RFmxGsmMXIQPowerEdgeTriggerLevelType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The value of the IQ Power Edge Level method is relative to the value of the SetReferenceLevel(String, Double) method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e5801668-30bb-a8e1-68cd-635b4218b03f.htm language=enus -->
## TOPIC 00138: rfmxgsmdotnet/html/e5801668-30bb-a8e1-68cd-635b4218b03f.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e5801668-30bb-a8e1-68cd-635b4218b03f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e5801668-30bb-a8e1-68cd-635b4218b03f.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXConstants.TimerEvent Field

RFmxGsmMXConstantsTimerEvent Field

The trigger is received from the timer event.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public const string TimerEvent = "TimerEvent"
```

```text
Public Const TimerEvent As String = "TimerEvent"
```

###### Field Value

String

##### See Also

###### Reference

RFmxGsmMXConstants Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e5d49e40-e3a8-7d6d-2fb8-ba785a1af023.htm language=enus -->
## TOPIC 00139: rfmxgsmdotnet/html/e5d49e40-e3a8-7d6d-2fb8-ba785a1af023.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e5d49e40-e3a8-7d6d-2fb8-ba785a1af023.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e5d49e40-e3a8-7d6d-2fb8-ba785a1af023.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration Class

RFmxGsmMXModAccConfiguration Class

Provides methods to configure the ModAcc measurement

##### Inheritance Hierarchy

RFmxGsmMXSubObject

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxGsmMXModAccConfiguration : RFmxGsmMXSubObject
```

```text
Public NotInheritable Class RFmxGsmMXModAccConfiguration
	Inherits RFmxGsmMXSubObject
```

The RFmxGsmMXModAccConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the modulation accuracy (ModAcc) measurement. |
|  | ConfigureDroopCompensationEnabled | Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXModAccAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
|  | GetDroopCompensationEnabled | Gets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxGsmMXModAccAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
|  | SetDroopCompensationEnabled | Sets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
|  | SetMeasurementEnabled | Sets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e65c6fb4-9486-1471-5db6-aa822cb1917a.htm language=enus -->
## TOPIC 00140: rfmxgsmdotnet/html/e65c6fb4-9486-1471-5db6-aa822cb1917a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e65c6fb4-9486-1471-5db6-aa822cb1917a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e65c6fb4-9486-1471-5db6-aa822cb1917a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SignalConfigurationType Property

RFmxGsmMXSignalConfigurationType Property

Type

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public Type SignalConfigurationType { get; }
```

```text
Public ReadOnly Property SignalConfigurationType As Type
	Get
```

###### Property Value

Type

###### Implements

ISignalConfiguration.SignalConfigurationType

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e6cd188c-1375-f962-d2c2-1d87c388251c.htm language=enus -->
## TOPIC 00141: rfmxgsmdotnet/html/e6cd188c-1375-f962-d2c2-1d87c388251c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e6cd188c-1375-f962-d2c2-1d87c388251c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e6cd188c-1375-f962-d2c2-1d87c388251c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetDigitalEdgeTriggerSource Method

RFmxGsmMXSetDigitalEdgeTriggerSource Method

SetTriggerType(String, RFmxGsmMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerSource(
	string selectorString,
	string value
)
```

```text
Public Function SetDigitalEdgeTriggerSource ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the source terminal for the digital-edge trigger. Use the string constants from the RFmxGsmMXConstants class or any other valid string to configure this parameter. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e6fe174c-e55b-a83e-fdef-9918954e4194.htm language=enus -->
## TOPIC 00142: rfmxgsmdotnet/html/e6fe174c-e55b-a83e-fdef-9918954e4194.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e6fe174c-e55b-a83e-fdef-9918954e4194.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e6fe174c-e55b-a83e-fdef-9918954e4194.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.SetMeasurementEnabled Method

RFmxGsmMXModAccConfigurationSetMeasurementEnabled Method

Sets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementEnabled(
	string selectorString,
	bool value
)
```

```text
Public Function SetMeasurementEnabled ( 
	selectorString As String,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal.

###### Return Value

Int32

##### Remarks

ModAccMeasurementEnabled

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e9fa216b-4cea-d5ea-1251-5c4a631cf9cb.htm language=enus -->
## TOPIC 00143: rfmxgsmdotnet/html/e9fa216b-4cea-d5ea-1251-5c4a631cf9cb.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e9fa216b-4cea-d5ea-1251-5c4a631cf9cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e9fa216b-4cea-d5ea-1251-5c4a631cf9cb.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.SetNumberOfAnalysisThreads Method

RFmxGsmMXModAccConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfAnalysisThreads(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfAnalysisThreads ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

ModAccNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/e9fca695-803c-3e55-a7e4-2ebb10838025.htm language=enus -->
## TOPIC 00144: rfmxgsmdotnet/html/e9fca695-803c-3e55-a7e4-2ebb10838025.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/e9fca695-803c-3e55-a7e4-2ebb10838025.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/e9fca695-803c-3e55-a7e4-2ebb10838025.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX Methods

RFmxGsmMX Methods

The [RFmxGsmMX](8f27cc0e-cbd2-1847-43da-0d7a077b3912.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with the signal instance that you specify in the selectorString parameter. This acquisition and measurements were previously initiated by the Initiate(String, String) method. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is IQ. Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the Commit(String) method. |
|  | AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(String, Double) method. Use this method to help calculate an approximate setting for the reference level. The RFmxGSM Auto Level method performs the following tasks: Resets the mixer level, mixer level offset, and IF output power offset. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings. Iterates to adjust the reference level based on the input signal peak power. Uses immediate triggering and restores the trigger settings back to user setting after completing execution. You can also specify the starting reference level using the Auto Level Initial Reference Level method. Call this method after configuring all signal methods. When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx GSM Auto Level method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method, thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildOffsetString | Creates a offset string to use as the selector string with configuration or fetch methods and methods. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSlotString | Creates a slot string to use as the selector string with configuration or fetch methods and methods. |
|  | CalculateFrequencyFromArfcn | Obsolete. Configures the center frequency from absolute RF channel number (ARFCN), band, and link direction. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxGSM commits settings to the hardware when you call the Initiate(String, String) method. |
|  | ConfigureAutoTscDetectionEnabled | Configures whether to auto detect the training sequence code (TSC). |
|  | ConfigureBand | Configures the band of operation. |
|  | ConfigureBurstSynchronizationType | Configures the burst synchronization type. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureExternalAttenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
|  | ConfigureFrequency | Configures the center frequency of the RF signal to acquire. |
|  | ConfigureFrequencyArfcn | Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
|  | ConfigureLinkDirection | Configures the source of the signal to be measured. |
|  | ConfigureNumberOfTimeslots | Configures the number of timeslots to be measured. |
|  | ConfigurePowerControlLevel | Configures the power control level corresponding to the transmitted power. Use "slot(n)" as the selector string to configure this method. |
|  | ConfigureReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
|  | ConfigureRF | Configures the RF methods of the signal specified by the selector string. |
|  | ConfigureSignalType | Configures the signal type. Use "slot(n)" as the selector string to configure this method. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
|  | ConfigureTsc | Configures the training sequence code (TSC) in the burst. Use "slot(n)" as the selector string to configure this method. |
|  | DeleteSignalConfiguration | Deletes an instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllNamedResultNames | Returns all the named result names of the current signal instance. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | GetAutoTscDetectionEnabled | Gets whether the measurement automatically detects the training sequence code (TSC). |
|  | GetBand | Gets the operation band. |
|  | GetBurstSynchronizationType | Gets the method used to synchronize the burst. |
|  | GetBurstType | Gets the burst type. Use "slot(n)" as the selector string to configure or read this method. |
|  | GetCenterFrequency | Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
|  | GetDigitalEdgeTriggerEdge | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge. |
|  | GetDigitalEdgeTriggerSource | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge. |
|  | GetError | Gets the latest error code and description. |
|  | GetErrorString | Converts the status code returned by an RFmxGSM function into a string. |
|  | GetExternalAttenuation | Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetHBFilterWidth | Gets the filter width when you set the SetBurstType(String, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
|  | GetIQPowerEdgeTriggerLevel | Gets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(String, Double) method with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | GetLinkDirection | Gets the source of the signal to be measured. |
|  | GetModulationType | Gets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
|  | GetNumberOfTimeslots | Gets the number of time slots to be measured. |
|  | GetPowerControlLevel | Gets the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |
|  | GetReferenceLevel | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | GetResultFetchTimeout | Gets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | GetSignalStructure | Gets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(String, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
|  | GetTimingAdvance | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |
|  | GetTriggerDelay | Gets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
|  | GetTriggerMinimumQuietTimeDuration | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement computes the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the trigger type. |
|  | GetTsc | Gets the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(String, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetWarning | Gets the latest warning code and description. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. This method disables all the external attenuation tables in all calibration planes. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxGSM_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configure an invalid trigger. You have not previously called the RFmxGSM Initiate method. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SetAutoTscDetectionEnabled | Sets whether the measurement automatically detects the training sequence code (TSC). |
|  | SetBand | Sets the operation band. |
|  | SetBurstSynchronizationType | Sets the method used to synchronize the burst. |
|  | SetBurstType | Sets the burst type. Use "slot(n)" as the selector string to configure or read this method. |
|  | SetCenterFrequency | Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
|  | SetDigitalEdgeTriggerEdge | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the digital-edge trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to DigitalEdge. |
|  | SetExternalAttenuation | Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
|  | SetHBFilterWidth | Sets the filter width when you set the SetBurstType(String, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
|  | SetIQPowerEdgeTriggerLevel | Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(String, Double) method with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxGsmMXTriggerType) method to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | SetLinkDirection | Sets the source of the signal to be measured. |
|  | SetModulationType | Sets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
|  | SetNumberOfTimeslots | Sets the number of time slots to be measured. |
|  | SetPowerControlLevel | Sets the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |
|  | SetReferenceLevel | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | SetResultFetchTimeout | Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
|  | SetSelectedPorts | Sets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | SetSignalStructure | Sets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(String, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
|  | SetTimingAdvance | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |
|  | SetTriggerDelay | Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
|  | SetTriggerMinimumQuietTimeDuration | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement computes the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the trigger type. |
|  | SetTsc | Sets the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(String, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(String, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/ea49d1c7-8bf9-be3a-3470-1593c5e41139.htm language=enus -->
## TOPIC 00145: rfmxgsmdotnet/html/ea49d1c7-8bf9-be3a-3470-1593c5e41139.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/ea49d1c7-8bf9-be3a-3470-1593c5e41139.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/ea49d1c7-8bf9-be3a-3470-1593c5e41139.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.CheckMeasurementStatus Method

RFmxGsmMXCheckMeasurementStatus Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int CheckMeasurementStatus(
	string selectorString,
	out bool done
)
```

```text
Public Function CheckMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef done As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **done Boolean**
  - Indicates whether the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/eab942ce-b846-ab50-46a0-65648a19b3b1.htm language=enus -->
## TOPIC 00146: rfmxgsmdotnet/html/eab942ce-b846-ab50-46a0-65648a19b3b1.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/eab942ce-b846-ab50-46a0-65648a19b3b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/eab942ce-b846-ab50-46a0-65648a19b3b1.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXTriggerType Enumeration

RFmxGsmMXTriggerType Enumeration

Specifies the trigger type.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXTriggerType
```

```text
Public Enumeration RFmxGsmMXTriggerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(String, String) method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSlope(String, RFmxGsmMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/eabc4891-5531-e4a0-678a-81e9bda15fc0.htm language=enus -->
## TOPIC 00147: rfmxgsmdotnet/html/eabc4891-5531-e4a0-678a-81e9bda15fc0.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/eabc4891-5531-e4a0-678a-81e9bda15fc0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/eabc4891-5531-e4a0-678a-81e9bda15fc0.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetBurstSynchronizationType Method

RFmxGsmMXGetBurstSynchronizationType Method

Gets the method used to synchronize the burst.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstSynchronizationType(
	string selectorString,
	out RFmxGsmMXBurstSynchronizationType value
)
```

```text
Public Function GetBurstSynchronizationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXBurstSynchronizationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXBurstSynchronizationType**
  - Upon return, contains the method used to synchronize the burst.

###### Return Value

Int32

##### Remarks

BurstSynchronizationType

Tsc

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/eb124afe-b62b-9604-77a7-c9e4dd018391.htm language=enus -->
## TOPIC 00148: rfmxgsmdotnet/html/eb124afe-b62b-9604-77a7-c9e4dd018391.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/eb124afe-b62b-9604-77a7-c9e4dd018391.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/eb124afe-b62b-9604-77a7-c9e4dd018391.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.AbortMeasurements Method

RFmxGsmMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int AbortMeasurements(
	string selectorString
)
```

```text
Public Function AbortMeasurements ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/ee605824-c878-b66e-d822-7823993a40a8.htm language=enus -->
## TOPIC 00149: rfmxgsmdotnet/html/ee605824-c878-b66e-d822-7823993a40a8.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/ee605824-c878-b66e-d822-7823993a40a8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/ee605824-c878-b66e-d822-7823993a40a8.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMeanFrequencyError Method

RFmxGsmMXModAccResultsGetEvmMeanFrequencyError Method

Gets the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanFrequencyError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanFrequencyError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMeanFrequencyError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/ef7f799b-7bb8-da01-5306-e9d804f3962d.htm language=enus -->
## TOPIC 00150: rfmxgsmdotnet/html/ef7f799b-7bb8-da01-5306-e9d804f3962d.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/ef7f799b-7bb8-da01-5306-e9d804f3962d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/ef7f799b-7bb8-da01-5306-e9d804f3962d.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.GetAveragingEnabled Method

RFmxGsmMXPvtConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxGsmMXPvtAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxGsmMXPvtAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxGsmMXPvtAveragingEnabled**
  - Upon return, contains whether to enable averaging for the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtAveragingEnabled

False

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f1839750-7936-97f2-d563-60d4bd62f648.htm language=enus -->
## TOPIC 00151: rfmxgsmdotnet/html/f1839750-7936-97f2-d563-60d4bd62f648.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f1839750-7936-97f2-d563-60d4bd62f648.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f1839750-7936-97f2-d563-60d4bd62f648.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetPferMaximumFrequencyError Method

RFmxGsmMXModAccResultsGetPferMaximumFrequencyError Method

Gets the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPferMaximumFrequencyError(
	string selectorString,
	out double value
)
```

```text
Public Function GetPferMaximumFrequencyError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsPferMaximumFrequencyError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f18630f4-30d7-bd35-aeb2-49d218020c71.htm language=enus -->
## TOPIC 00152: rfmxgsmdotnet/html/f18630f4-30d7-bd35-aeb2-49d218020c71.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f18630f4-30d7-bd35-aeb2-49d218020c71.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f18630f4-30d7-bd35-aeb2-49d218020c71.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAcc.Configuration Property

RFmxGsmMXModAccConfiguration Property

RFmxGsmMXModAccConfiguration

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxGsmMXModAccConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxGsmMXModAccConfiguration
	Get
```

###### Property Value

RFmxGsmMXModAccConfiguration

##### See Also

###### Reference

RFmxGsmMXModAcc Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f28b25c1-401c-25f5-3104-d4f66e6eb669.htm language=enus -->
## TOPIC 00153: rfmxgsmdotnet/html/f28b25c1-401c-25f5-3104-d4f66e6eb669.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f28b25c1-401c-25f5-3104-d4f66e6eb669.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f28b25c1-401c-25f5-3104-d4f66e6eb669.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXMeasurementTypes Enumeration

RFmxGsmMXMeasurementTypes Enumeration

Specifies the type of measurement.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum RFmxGsmMXMeasurementTypes
```

```text
<FlagsAttribute>
Public Enumeration RFmxGsmMXMeasurementTypes
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| ModAcc | 1 | Selects ModAcc measurement. |
| Orfs | 2 | Selects ORFS measurement. |
| Pvt | 4 | Selects PVT measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f47f782d-1fb4-5784-d7bb-c91fc0a01dd1.htm language=enus -->
## TOPIC 00154: rfmxgsmdotnet/html/f47f782d-1fb4-5784-d7bb-c91fc0a01dd1.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f47f782d-1fb4-5784-d7bb-c91fc0a01dd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f47f782d-1fb4-5784-d7bb-c91fc0a01dd1.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMeanPeakMagnitudeError Method

RFmxGsmMXModAccResultsGetEvmMeanPeakMagnitudeError Method

Returns the mean of peak magnitude error measured over all timeslots of all acquisitions. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanPeakMagnitudeError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanPeakMagnitudeError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMeanPeakMagnitudeError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f4b6e532-42c1-3179-4a72-4f960689d4a8.htm language=enus -->
## TOPIC 00155: rfmxgsmdotnet/html/f4b6e532-42c1-3179-4a72-4f960689d4a8.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f4b6e532-42c1-3179-4a72-4f960689d4a8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f4b6e532-42c1-3179-4a72-4f960689d4a8.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtConfiguration.GetNumberOfAnalysisThreads Method

RFmxGsmMXPvtConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfAnalysisThreads(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfAnalysisThreads ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

PvtNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxGsmMXPvtConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f5864045-3309-039c-6010-12d08f46c5dc.htm language=enus -->
## TOPIC 00156: rfmxgsmdotnet/html/f5864045-3309-039c-6010-12d08f46c5dc.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f5864045-3309-039c-6010-12d08f46c5dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f5864045-3309-039c-6010-12d08f46c5dc.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.GetSelectedPorts Method

RFmxGsmMXGetSelectedPorts Method

Valid values

Default values

Supported devices: PXIe-5820/5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSelectedPorts(
	string selectorString,
	out string value
)
```

```text
Public Function GetSelectedPorts ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the instrument port to be used by the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f5a2f26c-58c4-6dd2-8687-b6125d6cf58d.htm language=enus -->
## TOPIC 00157: rfmxgsmdotnet/html/f5a2f26c-58c4-6dd2-8687-b6125d6cf58d.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f5a2f26c-58c4-6dd2-8687-b6125d6cf58d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f5a2f26c-58c4-6dd2-8687-b6125d6cf58d.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccConfiguration.GetNumberOfAnalysisThreads Method

RFmxGsmMXModAccConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfAnalysisThreads(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfAnalysisThreads ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

ModAccNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxGsmMXModAccConfiguration Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f605441a-ea5e-4ebe-7e8b-2af9a60b0792.htm language=enus -->
## TOPIC 00158: rfmxgsmdotnet/html/f605441a-ea5e-4ebe-7e8b-2af9a60b0792.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f605441a-ea5e-4ebe-7e8b-2af9a60b0792.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f605441a-ea5e-4ebe-7e8b-2af9a60b0792.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXExtension.GetGsmSignalConfiguration(RFmxInstrMX) Method

RFmxGsmMXExtensionGetGsmSignalConfiguration(RFmxInstrMX) Method

Creates a new default GSM signal configuration if it doesn't exist; otherwise, it returns the
 existing default GSM signal configuration.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxGsmMX GetGsmSignalConfiguration(
	this RFmxInstrMX instrSession
)
```

```text
<ExtensionAttribute>
Public Shared Function GetGsmSignalConfiguration ( 
	instrSession As RFmxInstrMX
) As RFmxGsmMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an instr session.

###### Return Value

RFmxGsmMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxGsmMXExtension Class

GetGsmSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f77de32e-b0b9-c644-ae7a-f24259083b0c.htm language=enus -->
## TOPIC 00159: rfmxgsmdotnet/html/f77de32e-b0b9-c644-ae7a-f24259083b0c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f77de32e-b0b9-c644-ae7a-f24259083b0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f77de32e-b0b9-c644-ae7a-f24259083b0c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXBand Enumeration

RFmxGsmMXBand Enumeration

Specifies the operation band.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxGsmMXBand
```

```text
Public Enumeration RFmxGsmMXBand
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Pgsm | 0 | The operation band is Primary GSM in the 900 MHz band. |
| Egsm | 1 | The operation band is Extended GSM in the 900 MHz band. |
| Rgsm | 2 | The operation band is Railway GSM in the 900 MHz band. |
| Dcs1800 | 3 | The operation band is GSM in the 1800 MHz band. |
| Pcs1900 | 4 | The operation band is GSM in the 1900 MHz band. |
| Gsm450 | 5 | The operation band is GSM in the 450 MHz band. |
| Gsm480 | 6 | The operation band is GSM in the 480 MHz band. |
| Gsm850 | 7 | The operation band is GSM in the 850 MHz band. |
| Gsm750 | 8 | The operation band is GSM in the 750 MHz band. |
| Tgsm810 | 9 | The operation band is terrestrial GSM in the 810 MHz band. |

##### See Also

###### Reference

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f933030a-287b-c588-38a5-f5cfb7bad2a7.htm language=enus -->
## TOPIC 00160: rfmxgsmdotnet/html/f933030a-287b-c588-38a5-f5cfb7bad2a7.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f933030a-287b-c588-38a5-f5cfb7bad2a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f933030a-287b-c588-38a5-f5cfb7bad2a7.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.SetAttributeDouble Method

RFmxGsmMXSetAttributeDouble Method

Sets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeDouble(
	string selectorString,
	int attributeIdentifier,
	double value
)
```

```text
Public Function SetAttributeDouble ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Double**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/f9f920bf-b78f-5a96-d678-774c672d5f9f.htm language=enus -->
## TOPIC 00161: rfmxgsmdotnet/html/f9f920bf-b78f-5a96-d678-774c672d5f9f.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/f9f920bf-b78f-5a96-d678-774c672d5f9f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/f9f920bf-b78f-5a96-d678-774c672d5f9f.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXExtension.GetGsmSignalConfiguration(RFmxInstrMX, String) Method

RFmxGsmMXExtensionGetGsmSignalConfiguration(RFmxInstrMX, String) Method

Creates a GSM signal configuration for specified signal name. Existing GSM signal configuration is
 returned if specified signal name exists.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxGsmMX GetGsmSignalConfiguration(
	this RFmxInstrMX instrSession,
	string signalName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetGsmSignalConfiguration ( 
	instrSession As RFmxInstrMX,
	signalName As String
) As RFmxGsmMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an RFmxInstr session.
- **signalName String**
  - Specifies a signal name.

###### Return Value

RFmxGsmMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxGsmMXExtension Class

GetGsmSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/fa036802-376a-926e-418b-f961c1163016.htm language=enus -->
## TOPIC 00162: rfmxgsmdotnet/html/fa036802-376a-926e-418b-f961c1163016.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/fa036802-376a-926e-418b-f961c1163016.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/fa036802-376a-926e-418b-f961c1163016.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMX.BuildResultString Method

RFmxGsmMXBuildResultString Method

Creates selector string for use with configuration or fetch.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildResultString(
	string resultName
)
```

```text
Public Shared Function BuildResultString ( 
	resultName As String
) As String
```

###### Parameters

- **resultName String**
  - Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1".

###### Return Value

String

##### See Also

###### Reference

RFmxGsmMX Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/fc3160b2-c1c7-1233-8759-58ce57751876.htm language=enus -->
## TOPIC 00163: rfmxgsmdotnet/html/fc3160b2-c1c7-1233-8759-58ce57751876.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/fc3160b2-c1c7-1233-8759-58ce57751876.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/fc3160b2-c1c7-1233-8759-58ce57751876.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.FetchIQImpairments Method

RFmxGsmMXModAccResultsFetchIQImpairments Method

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchIQImpairments(
	string selectorString,
	double timeout,
	out double meanIQGainImbalance,
	out double maximumIQGainImbalance,
	out double meanIQOriginOffset,
	out double maximumIQOriginOffset
)
```

```text
Public Function FetchIQImpairments ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanIQGainImbalance As Double,
	<OutAttribute> ByRef maximumIQGainImbalance As Double,
	<OutAttribute> ByRef meanIQOriginOffset As Double,
	<OutAttribute> ByRef maximumIQOriginOffset As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanIQGainImbalance Double**
  - Upon return, contains the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.
- **maximumIQGainImbalance Double**
  - Upon return, contains the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.
- **meanIQOriginOffset Double**
  - Upon return, contains the mean of I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS.
- **maximumIQOriginOffset Double**
  - Upon return, contains the maximum of I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS.

###### Return Value

Int32

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/fc53b034-bdc0-d42c-0731-048c5f0f664e.htm language=enus -->
## TOPIC 00164: rfmxgsmdotnet/html/fc53b034-bdc0-d42c-0731-048c5f0f664e.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/fc53b034-bdc0-d42c-0731-048c5f0f664e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/fc53b034-bdc0-d42c-0731-048c5f0f664e.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMaximumRmsEvm Method

RFmxGsmMXModAccResultsGetEvmMaximumRmsEvm Method

Gets the maximum of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumRmsEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumRmsEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMaximumRmsEvm

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/fcec93fe-b71c-2f2b-e49b-002cf756ac6c.htm language=enus -->
## TOPIC 00165: rfmxgsmdotnet/html/fcec93fe-b71c-2f2b-e49b-002cf756ac6c.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/fcec93fe-b71c-2f2b-e49b-002cf756ac6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/fcec93fe-b71c-2f2b-e49b-002cf756ac6c.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvmMaximumPeakPhaseError Method

RFmxGsmMXModAccResultsGetEvmMaximumPeakPhaseError Method

Gets the maximum of peak phase error measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumPeakPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumPeakPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

###### Return Value

Int32

##### Remarks

ModAccResultsEvmMaximumPeakPhaseError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/fe95cbd1-a216-8330-d6a8-858b256dda3a.htm language=enus -->
## TOPIC 00166: rfmxgsmdotnet/html/fe95cbd1-a216-8330-d6a8-858b256dda3a.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/fe95cbd1-a216-8330-d6a8-858b256dda3a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/fe95cbd1-a216-8330-d6a8-858b256dda3a.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXPvtResults.GetSlotMinimumPower Method

RFmxGsmMXPvtResultsGetSlotMinimumPower Method

Gets the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSlotMinimumPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetSlotMinimumPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method.

###### Return Value

Int32

##### Remarks

PvtResultsSlotMinimumPower

##### See Also

###### Reference

RFmxGsmMXPvtResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-gsm-dotnet path=rfmxgsmdotnet/html/fed5c8c7-f1b3-d7bf-ca71-9b29c83951f0.htm language=enus -->
## TOPIC 00167: rfmxgsmdotnet/html/fed5c8c7-f1b3-d7bf-ca71-9b29c83951f0.htm

- bundle_id: `rfmx-gsm-dotnet`
- source_path: `rfmxgsmdotnet/html/fed5c8c7-f1b3-d7bf-ca71-9b29c83951f0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-dotnet/raw/resource/enus/rfmxgsmdotnet/html/fed5c8c7-f1b3-d7bf-ca71-9b29c83951f0.htm
- document_id: `rfmx-gsm-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxGsmMXModAccResults.GetEvm95thPercentilePhaseError Method

RFmxGsmMXModAccResultsGetEvm95thPercentilePhaseError Method

Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

Namespace:

NationalInstruments.RFmx.GsmMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvm95thPercentilePhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvm95thPercentilePhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

###### Return Value

Int32

##### Remarks

ModAccResultsEvm95thPercentilePhaseError

##### See Also

###### Reference

RFmxGsmMXModAccResults Class

NationalInstruments.RFmx.GsmMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
