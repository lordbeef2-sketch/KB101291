# NI DOCUMENT BUNDLE: rfmx-wcdma-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-wcdma-dotnet start=1 end=101 -->
<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/02a13c3a-476f-e632-84a9-8214c82e0e49.htm language=enus -->
## TOPIC 00001: rfmxwcdmadotnet/html/02a13c3a-476f-e632-84a9-8214c82e0e49.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/02a13c3a-476f-e632-84a9-8214c82e0e49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/02a13c3a-476f-e632-84a9-8214c82e0e49.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpConfiguration.ConfigureAveraging Method

RFmxWcdmaMXChpConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxWcdmaMXChpAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxWcdmaMXChpAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxWcdmaMXChpAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxWcdmaMXChpAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxWcdmaMXChpAveragingEnabled**
  - Specifies whether to enable averaging of the spectrum for the measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.
- **averagingType RFmxWcdmaMXChpAveragingType**
  - Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXChpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/02d6c390-f684-017c-5ac3-cc1d7fb9c198.htm language=enus -->
## TOPIC 00002: rfmxwcdmadotnet/html/02d6c390-f684-017c-5ac3-cc1d7fb9c198.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/02d6c390-f684-017c-5ac3-cc1d7fb9c198.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/02d6c390-f684-017c-5ac3-cc1d7fb9c198.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccResults.FetchEvm Method

RFmxWcdmaMXModAccResultsFetchEvm Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEvm(
	string selectorString,
	double timeout,
	out double rmsEvm,
	out double peakEvm,
	out double rho,
	out double frequencyError,
	out double chipRateError,
	out double rmsMagnitudeError,
	out double rmsPhaseError
)
```

```text
Public Function FetchEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef rmsEvm As Double,
	<OutAttribute> ByRef peakEvm As Double,
	<OutAttribute> ByRef rho As Double,
	<OutAttribute> ByRef frequencyError As Double,
	<OutAttribute> ByRef chipRateError As Double,
	<OutAttribute> ByRef rmsMagnitudeError As Double,
	<OutAttribute> ByRef rmsPhaseError As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and carrier number. If you do not specify the result name, the default result instance is used. Example:"carrier0""result::r1/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **rmsEvm Double**
  - Upon return, contains the RMS EVM of the composite signal for a carrier. This value is expressed as a percentage.
- **peakEvm Double**
  - Upon return, contains the peak EVM of the composite signal for a carrier. This value is expressed as a percentage.
- **rho Double**
  - Upon return, contains the correlation of the received signal with the reference signal normalized by the signal power for a carrier.
- **frequencyError Double**
  - Upon return, contains the frequency offset of the composite signal for a carrier. This value is expressed in Hz.
- **chipRateError Double**
  - Upon return, contains the chip rate error of the composite signal for a carrier. This value is expressed in ppm.
- **rmsMagnitudeError Double**
  - Upon return, contains the RMS magnitude error of the composite signal for a carrier. This value is expressed in percentage.
- **rmsPhaseError Double**
  - Upon return, contains the RMS phase error of the composite signal for a carrier. This value is expressed in degrees.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXModAccResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0389eb6f-46ba-96ed-9814-352e81c5a3e6.htm language=enus -->
## TOPIC 00003: rfmxwcdmadotnet/html/0389eb6f-46ba-96ed-9814-352e81c5a3e6.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0389eb6f-46ba-96ed-9814-352e81c5a3e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0389eb6f-46ba-96ed-9814-352e81c5a3e6.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemConfiguration.SetMeasurementEnabled Method

RFmxWcdmaMXSemConfigurationSetMeasurementEnabled Method

Sets whether to enable the SEM measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Specifies whether to enable the SEM measurement.

###### Return Value

Int32

##### Remarks

SemMeasurementEnabled

##### See Also

###### Reference

RFmxWcdmaMXSemConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/04423d53-af71-36db-70e2-c1635cd2bf17.htm language=enus -->
## TOPIC 00004: rfmxwcdmadotnet/html/04423d53-af71-36db-70e2-c1635cd2bf17.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/04423d53-af71-36db-70e2-c1635cd2bf17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/04423d53-af71-36db-70e2-c1635cd2bf17.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpRbwFilterType Enumeration

RFmxWcdmaMXChpRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXChpRbwFilterType
```

```text
Public Enumeration RFmxWcdmaMXChpRbwFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is applied. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/07953c58-3b10-3ab6-5f19-9df031a36768.htm language=enus -->
## TOPIC 00005: rfmxwcdmadotnet/html/07953c58-3b10-3ab6-5f19-9df031a36768.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/07953c58-3b10-3ab6-5f19-9df031a36768.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/07953c58-3b10-3ab6-5f19-9df031a36768.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpResults.FetchTotalCarrierPower Method

RFmxWcdmaMXAcpResultsFetchTotalCarrierPower Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchTotalCarrierPower(
	string selectorString,
	double timeout,
	out double totalCarrierPower
)
```

```text
Public Function FetchTotalCarrierPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef totalCarrierPower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **totalCarrierPower Double**
  - Upon return, contains the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(String, Double) method. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXAcpResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/07cd1c9c-9b7c-545b-5237-1489da354aed.htm language=enus -->
## TOPIC 00006: rfmxwcdmadotnet/html/07cd1c9c-9b7c-545b-5237-1489da354aed.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/07cd1c9c-9b7c-545b-5237-1489da354aed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/07cd1c9c-9b7c-545b-5237-1489da354aed.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemConfiguration.SetNumberOfAnalysisThreads Method

RFmxWcdmaMXSemConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the SEM measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Specifies the maximum number of threads used for parallelism for the SEM measurement.

###### Return Value

Int32

##### Remarks

SemNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxWcdmaMXSemConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/08716a29-394e-c24d-b8f1-c3c4bd47051e.htm language=enus -->
## TOPIC 00007: rfmxwcdmadotnet/html/08716a29-394e-c24d-b8f1-c3c4bd47051e.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/08716a29-394e-c24d-b8f1-c3c4bd47051e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/08716a29-394e-c24d-b8f1-c3c4bd47051e.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpRbwFilterType Enumeration

RFmxWcdmaMXAcpRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXAcpRbwFilterType
```

```text
Public Enumeration RFmxWcdmaMXAcpRbwFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is used. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/08b21fd7-74ef-2545-8102-b01e1f38bbb0.htm language=enus -->
## TOPIC 00008: rfmxwcdmadotnet/html/08b21fd7-74ef-2545-8102-b01e1f38bbb0.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/08b21fd7-74ef-2545-8102-b01e1f38bbb0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/08b21fd7-74ef-2545-8102-b01e1f38bbb0.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.BuildOffsetString Method

RFmxWcdmaMXBuildOffsetString Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildOffsetString(
	string selectorString,
	int offsetNumber
)
```

```text
Public Shared Function BuildOffsetString ( 
	selectorString As String,
	offsetNumber As Integer
) As String
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **offsetNumber Int32**
  - Specifies the offset number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0b2f104d-b625-1005-9f3f-b7b10cf20e14.htm language=enus -->
## TOPIC 00009: rfmxwcdmadotnet/html/0b2f104d-b625-1005-9f3f-b7b10cf20e14.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0b2f104d-b625-1005-9f3f-b7b10cf20e14.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0b2f104d-b625-1005-9f3f-b7b10cf20e14.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwResults.GetStopFrequency Method

RFmxWcdmaMXObwResultsGetStopFrequency Method

Gets the stop frequency of the occupied bandwidth.This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStopFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetStopFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the stop frequency of the occupied bandwidth.This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ObwResultsStopFrequency

##### See Also

###### Reference

RFmxWcdmaMXObwResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0c228dfa-58d9-9a03-edf8-ee86c665c640.htm language=enus -->
## TOPIC 00010: rfmxwcdmadotnet/html/0c228dfa-58d9-9a03-edf8-ee86c665c640.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0c228dfa-58d9-9a03-edf8-ee86c665c640.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0c228dfa-58d9-9a03-edf8-ee86c665c640.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemConfiguration.SetAveragingCount Method

RFmxWcdmaMXSemConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxWcdmaMXSemAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWcdmaMXSemAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

SemAveragingCount

##### See Also

###### Reference

RFmxWcdmaMXSemConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0c845c56-55d6-f94f-06d7-0ed227f8bd3c.htm language=enus -->
## TOPIC 00011: rfmxwcdmadotnet/html/0c845c56-55d6-f94f-06d7-0ed227f8bd3c.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0c845c56-55d6-f94f-06d7-0ed227f8bd3c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0c845c56-55d6-f94f-06d7-0ed227f8bd3c.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemConfiguration.GetAllTracesEnabled Method

RFmxWcdmaMXSemConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Upon return, contains whether to enable the traces to be stored and retrieved after performing the SEM measurement.

###### Return Value

Int32

##### Remarks

SemAllTracesEnabled

##### See Also

###### Reference

RFmxWcdmaMXSemConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0d118341-cbff-c673-3c89-891324db3fd4.htm language=enus -->
## TOPIC 00012: rfmxwcdmadotnet/html/0d118341-cbff-c673-3c89-891324db3fd4.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0d118341-cbff-c673-3c89-891324db3fd4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0d118341-cbff-c673-3c89-891324db3fd4.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.ConfigureBand Method

RFmxWcdmaMXConfigureBand Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureBand(
	string selectorString,
	int band
)
```

```text
Public Function ConfigureBand ( 
	selectorString As String,
	band As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **band Int32**
  - Specifies the UMTS operation band.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0e0e64b9-f079-d239-bc4d-80d6e6100afa.htm language=enus -->
## TOPIC 00013: rfmxwcdmadotnet/html/0e0e64b9-f079-d239-bc4d-80d6e6100afa.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0e0e64b9-f079-d239-bc4d-80d6e6100afa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0e0e64b9-f079-d239-bc4d-80d6e6100afa.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwResults.FetchSpectrum Method

RFmxWcdmaMXObwResultsFetchSpectrum Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSpectrum(
	string selectorString,
	double timeout,
	ref Spectrum<float> spectrum
)
```

```text
Public Function FetchSpectrum ( 
	selectorString As String,
	timeout As Double,
	ByRef spectrum As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **spectrum SpectrumSingle**
  - Upon return, contains the trace of power levels in the spectral domain. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXObwResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0ee73a5d-fd6a-a154-bbe1-44997485c58c.htm language=enus -->
## TOPIC 00014: rfmxwcdmadotnet/html/0ee73a5d-fd6a-a154-bbe1-44997485c58c.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0ee73a5d-fd6a-a154-bbe1-44997485c58c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0ee73a5d-fd6a-a154-bbe1-44997485c58c.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.GetIQOffsetRemovalEnabled Method

RFmxWcdmaMXCdaConfigurationGetIQOffsetRemovalEnabled Method

Gets whether to remove the I/Q offset before the CDA measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOffsetRemovalEnabled(
	string selectorString,
	out RFmxWcdmaMXCdaIQOffsetRemovalEnabled value
)
```

```text
Public Function GetIQOffsetRemovalEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXCdaIQOffsetRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXCdaIQOffsetRemovalEnabled**
  - Upon return, contains whether to remove the I/Q offset before the CDA measurement.

###### Return Value

Int32

##### Remarks

CdaIQOffsetRemovalEnabled

False

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0ef78d36-ab5a-cc3e-d152-797344c82306.htm language=enus -->
## TOPIC 00015: rfmxwcdmadotnet/html/0ef78d36-ab5a-cc3e-d152-797344c82306.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0ef78d36-ab5a-cc3e-d152-797344c82306.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0ef78d36-ab5a-cc3e-d152-797344c82306.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.SetMeasurementLength Method

RFmxWcdmaMXCdaConfigurationSetMeasurementLength Method

Sets the duration of the code domain measurement. This value is expressed in slots.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementLength(
	string selectorString,
	int value
)
```

```text
Public Function SetMeasurementLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the duration of the code domain measurement. This value is expressed in slots.

###### Return Value

Int32

##### Remarks

CdaMeasurementLength

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/0fabfa1b-f764-b254-d62a-a4d7538f8af1.htm language=enus -->
## TOPIC 00016: rfmxwcdmadotnet/html/0fabfa1b-f764-b254-d62a-a4d7538f8af1.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/0fabfa1b-f764-b254-d62a-a4d7538f8af1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/0fabfa1b-f764-b254-d62a-a4d7538f8af1.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccResults.GetPeakActiveCde Method

RFmxWcdmaMXModAccResultsGetPeakActiveCde Method

Gets the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakActiveCde(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakActiveCde ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakActiveCde

##### See Also

###### Reference

RFmxWcdmaMXModAccResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/101affe2-63ee-0447-8bb9-35e425ad6898.htm language=enus -->
## TOPIC 00017: rfmxwcdmadotnet/html/101affe2-63ee-0447-8bb9-35e425ad6898.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/101affe2-63ee-0447-8bb9-35e425ad6898.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/101affe2-63ee-0447-8bb9-35e425ad6898.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwResults.GetOccupiedBandwidth Method

RFmxWcdmaMXObwResultsGetOccupiedBandwidth Method

Gets the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers.This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOccupiedBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetOccupiedBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers.This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ObwResultsOccupiedBandwidth

##### See Also

###### Reference

RFmxWcdmaMXObwResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/1230ece2-3059-c2c7-7da0-947b5ecb567b.htm language=enus -->
## TOPIC 00018: rfmxwcdmadotnet/html/1230ece2-3059-c2c7-7da0-947b5ecb567b.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/1230ece2-3059-c2c7-7da0-947b5ecb567b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/1230ece2-3059-c2c7-7da0-947b5ecb567b.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.SetUplinkScramblingCode Method

RFmxWcdmaMXSetUplinkScramblingCode Method

Sets the scrambling code for the uplink channel.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUplinkScramblingCode(
	string selectorString,
	int value
)
```

```text
Public Function SetUplinkScramblingCode ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value Int32**
  - Specifies the scrambling code for the uplink channel.

###### Return Value

Int32

##### Remarks

UplinkScramblingCode

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/124c16ee-beae-7698-c901-e173ec70e2a3.htm language=enus -->
## TOPIC 00019: rfmxwcdmadotnet/html/124c16ee-beae-7698-c901-e173ec70e2a3.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/124c16ee-beae-7698-c901-e173ec70e2a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/124c16ee-beae-7698-c901-e173ec70e2a3.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.GetSweepTimeAuto Method

RFmxWcdmaMXAcpConfigurationGetSweepTimeAuto Method

Gets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxWcdmaMXAcpSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXAcpSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXAcpSweepTimeAuto**
  - Upon return, contains whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

AcpSweepTimeAuto

True

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/19f84eaf-e863-173b-7ed7-a9d2f5b111d6.htm language=enus -->
## TOPIC 00020: rfmxwcdmadotnet/html/19f84eaf-e863-173b-7ed7-a9d2f5b111d6.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/19f84eaf-e863-173b-7ed7-a9d2f5b111d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/19f84eaf-e863-173b-7ed7-a9d2f5b111d6.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwConfiguration.GetAveragingCount Method

RFmxWcdmaMXObwConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxWcdmaMXObwAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWcdmaMXObwAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ObwAveragingCount

##### See Also

###### Reference

RFmxWcdmaMXObwConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/1c9cb8c1-2aef-a271-47a2-c669722641c0.htm language=enus -->
## TOPIC 00021: rfmxwcdmadotnet/html/1c9cb8c1-2aef-a271-47a2-c669722641c0.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/1c9cb8c1-2aef-a271-47a2-c669722641c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/1c9cb8c1-2aef-a271-47a2-c669722641c0.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemSweepTimeAuto Enumeration

RFmxWcdmaMXSemSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXSemSweepTimeAuto
```

```text
Public Enumeration RFmxWcdmaMXSemSweepTimeAuto
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(String, Double) method. |
| True | 1 | The measurement uses a sweep time value of one slot duration. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/1d29b673-46f2-f500-84d5-40cce0018cba.htm language=enus -->
## TOPIC 00022: rfmxwcdmadotnet/html/1d29b673-46f2-f500-84d5-40cce0018cba.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/1d29b673-46f2-f500-84d5-40cce0018cba.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/1d29b673-46f2-f500-84d5-40cce0018cba.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChp.Results Property

RFmxWcdmaMXChpResults Property

RFmxWcdmaMXChpResults

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWcdmaMXChpResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxWcdmaMXChpResults
	Get
```

###### Property Value

RFmxWcdmaMXChpResults

##### See Also

###### Reference

RFmxWcdmaMXChp Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/201066c4-e42b-fb32-9f1e-d0443e1c22d4.htm language=enus -->
## TOPIC 00023: rfmxwcdmadotnet/html/201066c4-e42b-fb32-9f1e-d0443e1c22d4.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/201066c4-e42b-fb32-9f1e-d0443e1c22d4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/201066c4-e42b-fb32-9f1e-d0443e1c22d4.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccResults.GetRmsEvm Method

RFmxWcdmaMXModAccResultsGetRmsEvm Method

Gets the RMS EVM of the composite signal.This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the RMS EVM of the composite signal.This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsRmsEvm

##### See Also

###### Reference

RFmxWcdmaMXModAccResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/22ac4640-e488-49a7-4005-ed7044f6f0c2.htm language=enus -->
## TOPIC 00024: rfmxwcdmadotnet/html/22ac4640-e488-49a7-4005-ed7044f6f0c2.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/22ac4640-e488-49a7-4005-ed7044f6f0c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/22ac4640-e488-49a7-4005-ed7044f6f0c2.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.WcdmaMX Namespace

NationalInstruments.RFmx.WcdmaMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxWcdmaMX | Defines a root class which is used to identify and control WCDMA signal configuration. |
|  | RFmxWcdmaMXAcp | Represents the ACP measurement. |
|  | RFmxWcdmaMXAcpConfiguration | Provides methods to configure the ACP measurement |
|  | RFmxWcdmaMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
|  | RFmxWcdmaMXCda | Represents the CDA measurement. |
|  | RFmxWcdmaMXCdaConfiguration | Provides methods to configure the CDA measurement |
|  | RFmxWcdmaMXCdaResults | Provides methods to fetch and read the CDA measurement results. |
|  | RFmxWcdmaMXChp | Represents the CHP measurement. |
|  | RFmxWcdmaMXChpConfiguration | Provides methods to configure the CHP measurement |
|  | RFmxWcdmaMXChpResults | Provides methods to fetch and read the CHP measurement results. |
|  | RFmxWcdmaMXConstants | Specifies constants for I/O terminals. |
|  | RFmxWcdmaMXModAcc | Represents the ModAcc measurement. |
|  | RFmxWcdmaMXModAccConfiguration | Provides methods to configure the ModAcc measurement |
|  | RFmxWcdmaMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
|  | RFmxWcdmaMXObw | Represents the OBW measurement. |
|  | RFmxWcdmaMXObwConfiguration | Provides methods to configure the OBW measurement |
|  | RFmxWcdmaMXObwResults | Provides methods to fetch and read the OBW measurement results. |
|  | RFmxWcdmaMXQevm | Represents the QEVM measurement. |
|  | RFmxWcdmaMXQevmConfiguration | Provides methods to configure the QEVM measurement |
|  | RFmxWcdmaMXQevmResults | Provides methods to fetch and read the QEVM measurement results. |
|  | RFmxWcdmaMXSem | Represents the SEM measurement. |
|  | RFmxWcdmaMXSemConfiguration | Provides methods to configure the SEM measurement |
|  | RFmxWcdmaMXSemResults | Provides methods to fetch and read the SEM measurement results. |
|  | RFmxWcdmaMXSlotPhase | Represents the SlotPhase measurement. |
|  | RFmxWcdmaMXSlotPhaseConfiguration | Provides methods to configure the SlotPhase measurement |
|  | RFmxWcdmaMXSlotPhaseResults | Provides methods to fetch and read the SlotPhase measurement results. |
|  | RFmxWcdmaMXSlotPower | Represents the SlotPower measurement. |
|  | RFmxWcdmaMXSlotPowerConfiguration | Provides methods to configure the SlotPower measurement |
|  | RFmxWcdmaMXSlotPowerResults | Provides methods to fetch and read the SlotPower measurement results. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | RFmxWcdmaMXAcpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
|  | RFmxWcdmaMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
|  | RFmxWcdmaMXAcpAveragingType | Specifies the averaging type for averaging the spectrum of multiple acquisitions. The averaged spectrum is used for ACP measurement. |
|  | RFmxWcdmaMXAcpFftOverlapMode | Specifies how overlapping is applied when computing the FFT of the acquired samples. The default value is Disabled. |
|  | RFmxWcdmaMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |
|  | RFmxWcdmaMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |
|  | RFmxWcdmaMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
|  | RFmxWcdmaMXAcpOffsetPowerReferenceCarrier | Specifies the carrier used as the power reference to measure the offset channel relative power. |
|  | RFmxWcdmaMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
|  | RFmxWcdmaMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |
|  | RFmxWcdmaMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
|  | RFmxWcdmaMXBranch | Specifies the branch on which the data is modulated in the channel. |
|  | RFmxWcdmaMXCdaIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the CDA measurement. |
|  | RFmxWcdmaMXCdaMeasurementChannelBranch | Specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
|  | RFmxWcdmaMXCdaMeasurementChannelModulationType | Specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
|  | RFmxWcdmaMXCdaPowerUnit | Specifies the measurement unit of all power results, except GetTotalPower(String, Double). |
|  | RFmxWcdmaMXCdaRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | RFmxWcdmaMXCdaSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxWcdmaMXCdaSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | RFmxWcdmaMXChannelConfigurationMode | Specifies the channel configuration mode. |
|  | RFmxWcdmaMXChpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
|  | RFmxWcdmaMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |
|  | RFmxWcdmaMXChpAveragingType | Specifies the averaging type for averaging the spectrum of multiple acquisitions. |
|  | RFmxWcdmaMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
|  | RFmxWcdmaMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |
|  | RFmxWcdmaMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
|  | RFmxWcdmaMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. |
|  | RFmxWcdmaMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. |
|  | RFmxWcdmaMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. |
|  | RFmxWcdmaMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | RFmxWcdmaMXLinkDirection | Specifies the direction for which the frequency is calculated. |
|  | RFmxWcdmaMXMeasurementTypes | Specifies the type of measurement. |
|  | RFmxWcdmaMXModAccDetectedBranch | Returns the branch of the detected channel. |
|  | RFmxWcdmaMXModAccDetectedModulationType | Returns the modulation type of the detected channel. |
|  | RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled | Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. |
|  | RFmxWcdmaMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the ModAcc measurement. |
|  | RFmxWcdmaMXModAccIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. |
|  | RFmxWcdmaMXModAccPeakActiveCdeBranch | Returns the branch of the channel corresponding to the value of the GetPeakActiveCde(String, Double) method for a carrier. |
|  | RFmxWcdmaMXModAccPeakCdeBranch | Returns the branch corresponding to the value of the GetPeakCde(String, Double) method. |
|  | RFmxWcdmaMXModAccPeakRcdeBranch | Returns the branch of the channel corresponding to the value of the GetPeakRcde(String, Double) method for a carrier. |
|  | RFmxWcdmaMXModAccRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | RFmxWcdmaMXModAccSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxWcdmaMXModAccSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | RFmxWcdmaMXModAccTransientRemovalEnabled | Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |
|  | RFmxWcdmaMXModulationType | Specifies the modulation type for the channel. |
|  | RFmxWcdmaMXObwAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
|  | RFmxWcdmaMXObwAveragingEnabled | Specifies whether to enable averaging for the OBW measurement. |
|  | RFmxWcdmaMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
|  | RFmxWcdmaMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
|  | RFmxWcdmaMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |
|  | RFmxWcdmaMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
|  | RFmxWcdmaMXPropertyId | Specifies all the attribute identifiers. |
|  | RFmxWcdmaMXQevmAveragingEnabled | Specifies whether to enable averaging for the QEVM measurement. |
|  | RFmxWcdmaMXQevmIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the QEVM measurement. |
|  | RFmxWcdmaMXQevmRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | RFmxWcdmaMXQevmSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxWcdmaMXSemAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
|  | RFmxWcdmaMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |
|  | RFmxWcdmaMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. |
|  | RFmxWcdmaMXSemLowerOffsetMeasurementStatus | Indicates the measurement status based on the GetLowerOffsetMargin(String, Double) method. |
|  | RFmxWcdmaMXSemMeasurementStatus | Indicates the overall SEM measurement status, based on the value of the GetLowerOffsetMeasurementStatus(String, RFmxWcdmaMXSemLowerOffsetMeasurementStatus) and the GetUpperOffsetMeasurementStatus(String, RFmxWcdmaMXSemUpperOffsetMeasurementStatus) properties. |
|  | RFmxWcdmaMXSemOffsetRbwFilterType | Returns the shape of the digital RBW filter. |
|  | RFmxWcdmaMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
|  | RFmxWcdmaMXSemUpperOffsetMeasurementStatus | Indicates the measurement status based on the GetUpperOffsetMargin(String, Double) method. |
|  | RFmxWcdmaMXSlotPhaseRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | RFmxWcdmaMXSlotPhaseSpectrumInverted | Specifies whether the signal spectrum is inverted. |
|  | RFmxWcdmaMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
|  | RFmxWcdmaMXSlotPhaseTransientRemovalEnabled | Specifies whether the SlotPhase measurement excludes 25 microseconds from the start and end of each slot while computing the linear-fit chip phase error, which is used to compute phase discontinuities at the slot boundaries. |
|  | RFmxWcdmaMXSlotPowerRrcFilterEnabled | Specifies whether to enable the RRC filter. |
|  | RFmxWcdmaMXSlotPowerSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxWcdmaMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |
|  | RFmxWcdmaMXTransmitterArchitecture | Specifies the RF architecture at the transmitter for a multicarrier signal. |
|  | RFmxWcdmaMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
|  | RFmxWcdmaMXTriggerType | Specifies the trigger type. |
|  | RFmxWcdmaMXUplinkScramblingType | Specifies the type of scrambling to use for the measurement. |
|  | RFmxWcdmaMXUplinkTestModel | Specifies the uplink test model when the user sets the SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/2319019f-a4a7-25fa-8909-805bb2e4d0ce.htm language=enus -->
## TOPIC 00025: rfmxwcdmadotnet/html/2319019f-a4a7-25fa-8909-805bb2e4d0ce.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/2319019f-a4a7-25fa-8909-805bb2e4d0ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/2319019f-a4a7-25fa-8909-805bb2e4d0ce.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXQevmResults.GetMaximumPhaseError Method

RFmxWcdmaMXQevmResultsGetMaximumPhaseError Method

SetAveragingCount(String, Int32)

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(String, Int32) method.The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval.

###### Return Value

Int32

##### Remarks

QevmResultsMaximumPhaseError

##### See Also

###### Reference

RFmxWcdmaMXQevmResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/245a029f-3abd-acfc-e0c5-2519f6fc3cbb.htm language=enus -->
## TOPIC 00026: rfmxwcdmadotnet/html/245a029f-3abd-acfc-e0c5-2519f6fc3cbb.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/245a029f-3abd-acfc-e0c5-2519f6fc3cbb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/245a029f-3abd-acfc-e0c5-2519f6fc3cbb.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpAmplitudeCorrectionType Enumeration

RFmxWcdmaMXAcpAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXAcpAmplitudeCorrectionType
```

```text
Public Enumeration RFmxWcdmaMXAcpAmplitudeCorrectionType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/24aa3e91-62ff-0725-f847-547a8cf48707.htm language=enus -->
## TOPIC 00027: rfmxwcdmadotnet/html/24aa3e91-62ff-0725-f847-547a8cf48707.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/24aa3e91-62ff-0725-f847-547a8cf48707.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/24aa3e91-62ff-0725-f847-547a8cf48707.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.GetChannelConfigurationMode Method

RFmxWcdmaMXGetChannelConfigurationMode Method

Gets the channel configuration mode.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChannelConfigurationMode(
	string selectorString,
	out RFmxWcdmaMXChannelConfigurationMode value
)
```

```text
Public Function GetChannelConfigurationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXChannelConfigurationMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXChannelConfigurationMode**
  - Upon return, contains the channel configuration mode.

###### Return Value

Int32

##### Remarks

ChannelConfigurationMode

AutoDetect

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/24adc5cf-f45a-5a25-4536-3066fe2a5c57.htm language=enus -->
## TOPIC 00028: rfmxwcdmadotnet/html/24adc5cf-f45a-5a25-4536-3066fe2a5c57.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/24adc5cf-f45a-5a25-4536-3066fe2a5c57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/24adc5cf-f45a-5a25-4536-3066fe2a5c57.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpMeasurementMethod Enumeration

RFmxWcdmaMXAcpMeasurementMethod Enumeration

Specifies the method for performing the ACP measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXAcpMeasurementMethod
```

```text
Public Enumeration RFmxWcdmaMXAcpMeasurementMethod
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| DynamicRange | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range.Supported Devices: PXIe-5665/5668R |
| SequentialFft | 2 | The ACP measurement acquires I/Q samples specified by the SetSweepTimeInterval(String, Double) method. These samples are divided into smaller chunks. The size of each chunk is defined by the SetSequentialFftSize(String, Int32) method, and FFT is computed for each of these chunks. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Use this method to optimize for speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed.The following methods have limited support when you set the RFmxWcdmaMXAcpConfiguration.ConfigureMeasurementMethod method to SequentialFft.The RFmxWcdmaMXAcpConfiguration.SetRbwFilterAutoBandwidth method will only support True value. The RFmxWcdmaMXAcpConfiguration.SetRbwFilterType method will only support FftBased value. The RFmxWcdmaMXAcpConfiguration.SetSweepTimeAuto method will only support False value. The RFmxWcdmaMXAcpConfiguration.SetAveragingCount method will only support a value of greater than or equal to 1. The RFmxWcdmaMXAcpConfiguration.SetNumberOfAnalysisThreads method will only support a value of 1. The RFmxWcdmaMXAcpConfiguration.SetAmplitudeCorrectionType Method will only support a value of RFCenterFrequency. Note: For multi-span FFT, the averaging count should be 1. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/2521a3fe-ea29-a8cd-c7e4-b9ce87366a86.htm language=enus -->
## TOPIC 00029: rfmxwcdmadotnet/html/2521a3fe-ea29-a8cd-c7e4-b9ce87366a86.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/2521a3fe-ea29-a8cd-c7e4-b9ce87366a86.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/2521a3fe-ea29-a8cd-c7e4-b9ce87366a86.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccConfiguration.GetMeasurementOffset Method

RFmxWcdmaMXModAccConfigurationGetMeasurementOffset Method

SetSynchronizationMode(String, RFmxWcdmaMXModAccSynchronizationMode)

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementOffset(
	string selectorString,
	out int value
)
```

```text
Public Function GetMeasurementOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxWcdmaMXModAccSynchronizationMode) method.

###### Return Value

Int32

##### Remarks

ModAccMeasurementOffset

##### See Also

###### Reference

RFmxWcdmaMXModAccConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/25ff74b8-1b14-9573-845e-0420dafd63e6.htm language=enus -->
## TOPIC 00030: rfmxwcdmadotnet/html/25ff74b8-1b14-9573-845e-0420dafd63e6.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/25ff74b8-1b14-9573-845e-0420dafd63e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/25ff74b8-1b14-9573-845e-0420dafd63e6.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.GetNumberOfOffsets Method

RFmxWcdmaMXAcpConfigurationGetNumberOfOffsets Method

Gets the number of offset channels.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfOffsets(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfOffsets ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of offset channels.

###### Return Value

Int32

##### Remarks

AcpNumberOfOffsets

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/2b52d47b-4763-d1d5-d0fd-767cbe6f6a3c.htm language=enus -->
## TOPIC 00031: rfmxwcdmadotnet/html/2b52d47b-4763-d1d5-d0fd-767cbe6f6a3c.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/2b52d47b-4763-d1d5-d0fd-767cbe6f6a3c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/2b52d47b-4763-d1d5-d0fd-767cbe6f6a3c.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.BuildResultString Method

RFmxWcdmaMXBuildResultString Method

Creates selector string for use with configuration or fetch.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/301c8bff-4cb3-b0bc-cb28-ef2846280e6c.htm language=enus -->
## TOPIC 00032: rfmxwcdmadotnet/html/301c8bff-4cb3-b0bc-cb28-ef2846280e6c.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/301c8bff-4cb3-b0bc-cb28-ef2846280e6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/301c8bff-4cb3-b0bc-cb28-ef2846280e6c.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcp Methods

RFmxWcdmaMXAcp Methods

The [RFmxWcdmaMXAcp](ab05a21f-7995-fd41-4fb6-24e14ab2c671.htm) type exposes the following members.

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

RFmxWcdmaMXAcp Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/30a13e5f-da46-cc4d-7263-91e580f6f604.htm language=enus -->
## TOPIC 00033: rfmxwcdmadotnet/html/30a13e5f-da46-cc4d-7263-91e580f6f604.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/30a13e5f-da46-cc4d-7263-91e580f6f604.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/30a13e5f-da46-cc4d-7263-91e580f6f604.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSlotPhaseResults.FetchMeasurement Method

RFmxWcdmaMXSlotPhaseResultsFetchMeasurement Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurement(
	string selectorString,
	double timeout,
	out double maximumPhaseDiscontinuity,
	out int discontinuityCountGreaterThanLimit1,
	out int discontinuityCountGreaterThanLimit2,
	out int discontinuityMinimumDistance
)
```

```text
Public Function FetchMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef maximumPhaseDiscontinuity As Double,
	<OutAttribute> ByRef discontinuityCountGreaterThanLimit1 As Integer,
	<OutAttribute> ByRef discontinuityCountGreaterThanLimit2 As Integer,
	<OutAttribute> ByRef discontinuityMinimumDistance As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **maximumPhaseDiscontinuity Double**
  - Upon return, contains the maximum of all the measured phase discontinuity values at the slot boundaries. This value is expressed in degrees.
- **discontinuityCountGreaterThanLimit1 Int32**
  - Upon return, contains the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees.
- **discontinuityCountGreaterThanLimit2 Int32**
  - Upon return, contains the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees.
- **discontinuityMinimumDistance Int32**
  - Upon return, contains the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. If there are no phase discontinuity values greater than Limit 1, or if there is only one phase discontinuity value greater than Limit 1, this result is not valid. In such a case, -1 is reported as the result.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXSlotPhaseResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/30d596e4-91a4-f417-ee21-16ab4649ba7d.htm language=enus -->
## TOPIC 00034: rfmxwcdmadotnet/html/30d596e4-91a4-f417-ee21-16ab4649ba7d.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/30d596e4-91a4-f417-ee21-16ab4649ba7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/30d596e4-91a4-f417-ee21-16ab4649ba7d.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.SetSequentialFftSize Method

RFmxWcdmaMXAcpConfigurationSetSequentialFftSize Method

SetMeasurementMethod(String, RFmxWcdmaMXAcpMeasurementMethod)

SequentialFft

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSequentialFftSize(
	string selectorString,
	int value
)
```

```text
Public Function SetSequentialFftSize ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of bins to use for FFT computation when the SetMeasurementMethod(String, RFmxWcdmaMXAcpMeasurementMethod) method is set to SequentialFft.

###### Return Value

Int32

##### Remarks

AcpSequentialFftSize

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/3215830b-d768-a5e4-6525-75e988be87a2.htm language=enus -->
## TOPIC 00035: rfmxwcdmadotnet/html/3215830b-d768-a5e4-6525-75e988be87a2.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/3215830b-d768-a5e4-6525-75e988be87a2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/3215830b-d768-a5e4-6525-75e988be87a2.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXUplinkTestModel Enumeration

RFmxWcdmaMXUplinkTestModel Enumeration

SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode)

TestModel

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXUplinkTestModel
```

```text
Public Enumeration RFmxWcdmaMXUplinkTestModel
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| R6C_2_1 | 0 | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_2 | 1 | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_3 | 2 | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_4 | 3 | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_5 | 4 | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_10_1_4_Subtest1 | 5 | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest2 | 6 | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest3 | 7 | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest4 | 8 | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest5 | 9 | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest6 | 10 | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7C_10_1_4_Subtest1 | 11 | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_10_1_4_Subtest2 | 12 | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_10_1_4_Subtest3 | 13 | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_10_1_4_Subtest4 | 14 | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest1 | 15 | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest2 | 16 | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest3 | 17 | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest4 | 18 | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest5 | 19 | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8C_11_1_3_Subtest1 | 20 | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R8C_11_1_3_Subtest2 | 21 | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_3_Subtest3 | 22 | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_3_Subtest4 | 23 | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_3_Subtest5 | 24 | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_4_Subtest1 | 25 | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/321dcb81-9e42-9aa2-c61a-2b695ed33346.htm language=enus -->
## TOPIC 00036: rfmxwcdmadotnet/html/321dcb81-9e42-9aa2-c61a-2b695ed33346.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/321dcb81-9e42-9aa2-c61a-2b695ed33346.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/321dcb81-9e42-9aa2-c61a-2b695ed33346.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled Enumeration

RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled Enumeration

Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled
```

```text
Public Enumeration RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The I/Q gain imbalance is not removed before the ModAcc measurement. |
| True | 1 | The I/Q gain imbalance is removed before the ModAcc measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4a2e9195-bb87-1ea1-b2ce-69399fd3686e.htm language=enus -->
## TOPIC 00037: rfmxwcdmadotnet/html/4a2e9195-bb87-1ea1-b2ce-69399fd3686e.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4a2e9195-bb87-1ea1-b2ce-69399fd3686e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4a2e9195-bb87-1ea1-b2ce-69399fd3686e.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccResults.GetDetectedSpreadingCode Method

RFmxWcdmaMXModAccResultsGetDetectedSpreadingCode Method

Gets the spreading code of the detected channel.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectedSpreadingCode(
	string selectorString,
	out int value
)
```

```text
Public Function GetDetectedSpreadingCode ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name, Channel number and Carrier number. Example: "Carrier0", "result::r1/Carrier0" or "result::r1/Carrier0/Channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the spreading code of the detected channel.

###### Return Value

Int32

##### Remarks

ModAccResultsDetectedSpreadingCode

##### See Also

###### Reference

RFmxWcdmaMXModAccResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4c4c5785-dfc1-ce24-6935-d76084e30e93.htm language=enus -->
## TOPIC 00038: rfmxwcdmadotnet/html/4c4c5785-dfc1-ce24-6935-d76084e30e93.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4c4c5785-dfc1-ce24-6935-d76084e30e93.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4c4c5785-dfc1-ce24-6935-d76084e30e93.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemResults.GetUpperOffsetAbsolutePeakPower Method

RFmxWcdmaMXSemResultsGetUpperOffsetAbsolutePeakPower Method

Gets the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetAbsolutePeakPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetAbsolutePeakPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetAbsolutePeakPower

##### See Also

###### Reference

RFmxWcdmaMXSemResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4ca9da2a-798e-5b5b-477b-1971560ced90.htm language=enus -->
## TOPIC 00039: rfmxwcdmadotnet/html/4ca9da2a-798e-5b5b-477b-1971560ced90.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4ca9da2a-798e-5b5b-477b-1971560ced90.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4ca9da2a-798e-5b5b-477b-1971560ced90.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwConfiguration.GetNumberOfAnalysisThreads Method

RFmxWcdmaMXObwConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the OBW measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Upon return, contains the maximum number of threads used for parallelism for the OBW measurement.

###### Return Value

Int32

##### Remarks

ObwNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxWcdmaMXObwConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4d10b26c-7053-8806-bfd0-8150d033a709.htm language=enus -->
## TOPIC 00040: rfmxwcdmadotnet/html/4d10b26c-7053-8806-bfd0-8150d033a709.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4d10b26c-7053-8806-bfd0-8150d033a709.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4d10b26c-7053-8806-bfd0-8150d033a709.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.SetUplinkTestModel Method

RFmxWcdmaMXSetUplinkTestModel Method

SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode)

TestModel

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUplinkTestModel(
	string selectorString,
	RFmxWcdmaMXUplinkTestModel value
)
```

```text
Public Function SetUplinkTestModel ( 
	selectorString As String,
	value As RFmxWcdmaMXUplinkTestModel
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value RFmxWcdmaMXUplinkTestModel**
  - Specifies the uplink test model when the user sets the SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode) method to TestModel.

###### Return Value

Int32

##### Remarks

UplinkTestModel

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4d162d0a-0872-53a8-1551-177f38996519.htm language=enus -->
## TOPIC 00041: rfmxwcdmadotnet/html/4d162d0a-0872-53a8-1551-177f38996519.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4d162d0a-0872-53a8-1551-177f38996519.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4d162d0a-0872-53a8-1551-177f38996519.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpRbwAutoBandwidth Enumeration

RFmxWcdmaMXChpRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXChpRbwAutoBandwidth
```

```text
Public Enumeration RFmxWcdmaMXChpRbwAutoBandwidth
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(String, Double) method. |
| True | 1 | The measurement computes the RBW. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4d1fb8d6-cc9a-66c6-9482-d54412598380.htm language=enus -->
## TOPIC 00042: rfmxwcdmadotnet/html/4d1fb8d6-cc9a-66c6-9482-d54412598380.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4d1fb8d6-cc9a-66c6-9482-d54412598380.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4d1fb8d6-cc9a-66c6-9482-d54412598380.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemAmplitudeCorrectionType Enumeration

RFmxWcdmaMXSemAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXSemAmplitudeCorrectionType
```

```text
Public Enumeration RFmxWcdmaMXSemAmplitudeCorrectionType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4d45e88e-d368-a075-2d9f-20d455e98876.htm language=enus -->
## TOPIC 00043: rfmxwcdmadotnet/html/4d45e88e-d368-a075-2d9f-20d455e98876.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4d45e88e-d368-a075-2d9f-20d455e98876.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4d45e88e-d368-a075-2d9f-20d455e98876.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpConfiguration.SetAveragingType Method

RFmxWcdmaMXChpConfigurationSetAveragingType Method

Sets the averaging type for averaging the spectrum of multiple acquisitions.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxWcdmaMXChpAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxWcdmaMXChpAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXChpAveragingType**
  - Specifies the averaging type for averaging the spectrum of multiple acquisitions.

###### Return Value

Int32

##### Remarks

ChpAveragingType

##### See Also

###### Reference

RFmxWcdmaMXChpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4e5e55b5-7037-6dbc-8c0f-840d5c2b7b66.htm language=enus -->
## TOPIC 00044: rfmxwcdmadotnet/html/4e5e55b5-7037-6dbc-8c0f-840d5c2b7b66.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4e5e55b5-7037-6dbc-8c0f-840d5c2b7b66.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4e5e55b5-7037-6dbc-8c0f-840d5c2b7b66.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpResults.FetchCarrierMeasurementArray Method

RFmxWcdmaMXChpResultsFetchCarrierMeasurementArray Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurementArray(
	string selectorString,
	double timeout,
	ref double[] absolutePower,
	ref double[] relativePower
)
```

```text
Public Function FetchCarrierMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef absolutePower As Double(),
	ByRef relativePower As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **absolutePower Double**
  - Upon return, contains an array of carrier powers integrated over a bandwidth of 5 MHz. This value is expressed in dBm.
- **relativePower Double**
  - Upon return, contains an array of carrier powers relative to the GetTotalCarrierPower(String, Double) method. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXChpResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/4fa172d8-26ef-3ff3-92a1-b6f9422d0ad3.htm language=enus -->
## TOPIC 00045: rfmxwcdmadotnet/html/4fa172d8-26ef-3ff3-92a1-b6f9422d0ad3.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/4fa172d8-26ef-3ff3-92a1-b6f9422d0ad3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/4fa172d8-26ef-3ff3-92a1-b6f9422d0ad3.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXQevmConfiguration.GetAveragingCount Method

RFmxWcdmaMXQevmConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxWcdmaMXQevmAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWcdmaMXQevmAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

QevmAveragingCount

##### See Also

###### Reference

RFmxWcdmaMXQevmConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/505fac73-e1d5-7577-e90f-d5ff874d967b.htm language=enus -->
## TOPIC 00046: rfmxwcdmadotnet/html/505fac73-e1d5-7577-e90f-d5ff874d967b.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/505fac73-e1d5-7577-e90f-d5ff874d967b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/505fac73-e1d5-7577-e90f-d5ff874d967b.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.SetResultFetchTimeout Method

RFmxWcdmaMXSetResultFetchTimeout Method

Sets the time to wait before results are available in the RFmxWCDMA_PropertyNode.This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Specifies the time to wait before results are available in the RFmxWCDMA_PropertyNode.This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/507a7ca0-e145-cf49-7c33-60e5e6f4ca4f.htm language=enus -->
## TOPIC 00047: rfmxwcdmadotnet/html/507a7ca0-e145-cf49-7c33-60e5e6f4ca4f.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/507a7ca0-e145-cf49-7c33-60e5e6f4ca4f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/507a7ca0-e145-cf49-7c33-60e5e6f4ca4f.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpConfiguration.ConfigureSweepTime Method

RFmxWcdmaMXChpConfigurationConfigureSweepTime Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSweepTime(
	string selectorString,
	RFmxWcdmaMXChpSweepTimeAuto sweepTimeAuto,
	double sweepTimeInterval
)
```

```text
Public Function ConfigureSweepTime ( 
	selectorString As String,
	sweepTimeAuto As RFmxWcdmaMXChpSweepTimeAuto,
	sweepTimeInterval As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sweepTimeAuto RFmxWcdmaMXChpSweepTimeAuto**
  - Specifies whether the measurement computes the sweep time.
- **sweepTimeInterval Double**
  - Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXChpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/50d61bca-9ab3-4300-45f4-d4304710ecf4.htm language=enus -->
## TOPIC 00048: rfmxwcdmadotnet/html/50d61bca-9ab3-4300-45f4-d4304710ecf4.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/50d61bca-9ab3-4300-45f4-d4304710ecf4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/50d61bca-9ab3-4300-45f4-d4304710ecf4.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSlotPowerConfiguration.GetSynchronizationMode Method

RFmxWcdmaMXSlotPowerConfigurationGetSynchronizationMode Method

Gets whether the measurement is performed from the frame or slot boundary.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSynchronizationMode(
	string selectorString,
	out RFmxWcdmaMXSlotPowerSynchronizationMode value
)
```

```text
Public Function GetSynchronizationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXSlotPowerSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXSlotPowerSynchronizationMode**
  - Upon return, contains whether the measurement is performed from the frame or slot boundary.

###### Return Value

Int32

##### Remarks

SlotPowerSynchronizationMode

Frame

##### See Also

###### Reference

RFmxWcdmaMXSlotPowerConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5618a025-c88f-f0c9-251e-4dbfb74eadca.htm language=enus -->
## TOPIC 00049: rfmxwcdmadotnet/html/5618a025-c88f-f0c9-251e-4dbfb74eadca.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5618a025-c88f-f0c9-251e-4dbfb74eadca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5618a025-c88f-f0c9-251e-4dbfb74eadca.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaIQOffsetRemovalEnabled Enumeration

RFmxWcdmaMXCdaIQOffsetRemovalEnabled Enumeration

Specifies whether to remove the I/Q offset before the CDA measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXCdaIQOffsetRemovalEnabled
```

```text
Public Enumeration RFmxWcdmaMXCdaIQOffsetRemovalEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The I/Q offset is not removed before the CDA measurement. |
| True | 1 | the I/Q offset is removed before the CDA measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/585bd451-0056-bb39-d447-c2b8114a7183.htm language=enus -->
## TOPIC 00050: rfmxwcdmadotnet/html/585bd451-0056-bb39-d447-c2b8114a7183.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/585bd451-0056-bb39-d447-c2b8114a7183.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/585bd451-0056-bb39-d447-c2b8114a7183.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwConfiguration.SetAveragingEnabled Method

RFmxWcdmaMXObwConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for the OBW measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxWcdmaMXObwAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxWcdmaMXObwAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXObwAveragingEnabled**
  - Specifies whether to enable averaging for the OBW measurement.

###### Return Value

Int32

##### Remarks

ObwAveragingEnabled

False

##### See Also

###### Reference

RFmxWcdmaMXObwConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5a2655c6-180e-242b-65d4-e83e9016b25f.htm language=enus -->
## TOPIC 00051: rfmxwcdmadotnet/html/5a2655c6-180e-242b-65d4-e83e9016b25f.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5a2655c6-180e-242b-65d4-e83e9016b25f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5a2655c6-180e-242b-65d4-e83e9016b25f.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccDetectedBranch Enumeration

RFmxWcdmaMXModAccDetectedBranch Enumeration

Returns the branch of the detected channel.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXModAccDetectedBranch
```

```text
Public Enumeration RFmxWcdmaMXModAccDetectedBranch
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| I | 0 | The signal is modulated on the in-phase branch. |
| Q | 1 | The signal is modulated on the quadrature-phase branch. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5a3d5215-7adb-f53e-7bb4-2d2432771c08.htm language=enus -->
## TOPIC 00052: rfmxwcdmadotnet/html/5a3d5215-7adb-f53e-7bb4-2d2432771c08.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5a3d5215-7adb-f53e-7bb4-2d2432771c08.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5a3d5215-7adb-f53e-7bb4-2d2432771c08.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSlotPhaseResults Class

RFmxWcdmaMXSlotPhaseResults Class

Provides methods to fetch and read the SlotPhase measurement results.

##### Inheritance Hierarchy

RFmxWcdmaMXSubObject

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxWcdmaMXSlotPhaseResults : RFmxWcdmaMXSubObject
```

```text
Public NotInheritable Class RFmxWcdmaMXSlotPhaseResults
	Inherits RFmxWcdmaMXSubObject
```

The RFmxWcdmaMXSlotPhaseResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchChipPhaseErrorLinearFitTrace | Fetches the chip phase error linear fit trace for the SlotPhase measurement. |
|  | FetchChipPhaseErrorTrace | Fetches the chip phase error trace for the SlotPhase measurement. |
|  | FetchMeasurement | Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results. |
|  | FetchPhaseDiscontinuities | Fetches the phase discontinuity values for the slot phase measurement. |
|  | GetDiscontinuityCountGreaterThanLimit1 | Gets the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |
|  | GetDiscontinuityCountGreaterThanLimit2 | Gets the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |
|  | GetDiscontinuityMinimumDistance | Gets the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMaximumPhaseDiscontinuity | Gets the maximum of all the measured phase discontinuity values at the slot boundaries. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5a6422ba-7b63-ac63-1a1e-ff2d08092a15.htm language=enus -->
## TOPIC 00053: rfmxwcdmadotnet/html/5a6422ba-7b63-ac63-1a1e-ff2d08092a15.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5a6422ba-7b63-ac63-1a1e-ff2d08092a15.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5a6422ba-7b63-ac63-1a1e-ff2d08092a15.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.GetLimitedConfigurationChange Method

RFmxWcdmaMXGetLimitedConfigurationChange Method

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLimitedConfigurationChange(
	string selectorString,
	out RFmxWcdmaMXLimitedConfigurationChange value
)
```

```text
Public Function GetLimitedConfigurationChange ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXLimitedConfigurationChange**
  - Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

LimitedConfigurationChange

Disabled

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5b2975d1-e462-119f-36bf-db9ecaa8dd24.htm language=enus -->
## TOPIC 00054: rfmxwcdmadotnet/html/5b2975d1-e462-119f-36bf-db9ecaa8dd24.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5b2975d1-e462-119f-36bf-db9ecaa8dd24.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5b2975d1-e462-119f-36bf-db9ecaa8dd24.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXObwConfiguration.GetRbwFilterBandwidth Method

RFmxWcdmaMXObwConfigurationGetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxWcdmaMXObwRbwAutoBandwidth)

False

SetRbwFilterType(String, RFmxWcdmaMXObwRbwFilterType)

Gaussian

Flat

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetRbwFilterBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxWcdmaMXObwRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(String, RFmxWcdmaMXObwRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ObwRbwFilterBandwidth

##### See Also

###### Reference

RFmxWcdmaMXObwConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5bb14835-490f-6d97-c8ac-7c502e0bad85.htm language=enus -->
## TOPIC 00055: rfmxwcdmadotnet/html/5bb14835-490f-6d97-c8ac-7c502e0bad85.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5bb14835-490f-6d97-c8ac-7c502e0bad85.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5bb14835-490f-6d97-c8ac-7c502e0bad85.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.ResetToDefault Method

RFmxWcdmaMXResetToDefault Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

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

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5c6fc6ae-e161-1631-0d42-a303505cfbfe.htm language=enus -->
## TOPIC 00056: rfmxwcdmadotnet/html/5c6fc6ae-e161-1631-0d42-a303505cfbfe.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5c6fc6ae-e161-1631-0d42-a303505cfbfe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5c6fc6ae-e161-1631-0d42-a303505cfbfe.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpSweepTimeAuto Enumeration

RFmxWcdmaMXAcpSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXAcpSweepTimeAuto
```

```text
Public Enumeration RFmxWcdmaMXAcpSweepTimeAuto
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(String, Double) method |
| True | 1 | The measurement uses a sweep time value of one slot duration. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5da03314-de81-4eac-c0ae-fda8f7bd9abf.htm language=enus -->
## TOPIC 00057: rfmxwcdmadotnet/html/5da03314-de81-4eac-c0ae-fda8f7bd9abf.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5da03314-de81-4eac-c0ae-fda8f7bd9abf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5da03314-de81-4eac-c0ae-fda8f7bd9abf.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpResults.FetchAbsolutePowersTrace Method

RFmxWcdmaMXAcpResultsFetchAbsolutePowersTrace Method

Fetches the absolute powers trace for the ACP measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAbsolutePowersTrace(
	string selectorString,
	double timeout,
	int traceIndex,
	ref Spectrum<float> absolutePowersTrace
)
```

```text
Public Function FetchAbsolutePowersTrace ( 
	selectorString As String,
	timeout As Double,
	traceIndex As Integer,
	ByRef absolutePowersTrace As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **traceIndex Int32**
  - Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets).
- **absolutePowersTrace SpectrumSingle**
  - Returns the trace of measured integrated power in the channel specified by the traceIndex parameter. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXAcpResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5dbefbca-065f-a91b-8a48-8b9126f2f28f.htm language=enus -->
## TOPIC 00058: rfmxwcdmadotnet/html/5dbefbca-065f-a91b-8a48-8b9126f2f28f.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5dbefbca-065f-a91b-8a48-8b9126f2f28f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5dbefbca-065f-a91b-8a48-8b9126f2f28f.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSlotPowerConfiguration.GetMeasurementLength Method

RFmxWcdmaMXSlotPowerConfigurationGetMeasurementLength Method

Gets the duration of the SlotPower measurement. This value is expressed in slots.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementLength(
	string selectorString,
	out int value
)
```

```text
Public Function GetMeasurementLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the duration of the SlotPower measurement. This value is expressed in slots.

###### Return Value

Int32

##### Remarks

SlotPowerMeasurementLength

##### See Also

###### Reference

RFmxWcdmaMXSlotPowerConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5de115af-153c-6239-2e6c-3d17a0efd702.htm language=enus -->
## TOPIC 00059: rfmxwcdmadotnet/html/5de115af-153c-6239-2e6c-3d17a0efd702.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5de115af-153c-6239-2e6c-3d17a0efd702.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5de115af-153c-6239-2e6c-3d17a0efd702.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXQevmConfiguration.SetAveragingCount Method

RFmxWcdmaMXQevmConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxWcdmaMXQevmAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWcdmaMXQevmAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

QevmAveragingCount

##### See Also

###### Reference

RFmxWcdmaMXQevmConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5f7de32c-2a45-4ba3-049c-e38dd50c40c1.htm language=enus -->
## TOPIC 00060: rfmxwcdmadotnet/html/5f7de32c-2a45-4ba3-049c-e38dd50c40c1.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5f7de32c-2a45-4ba3-049c-e38dd50c40c1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5f7de32c-2a45-4ba3-049c-e38dd50c40c1.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.GetUplinkTestModel Method

RFmxWcdmaMXGetUplinkTestModel Method

SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode)

TestModel

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkTestModel(
	string selectorString,
	out RFmxWcdmaMXUplinkTestModel value
)
```

```text
Public Function GetUplinkTestModel ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXUplinkTestModel
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value RFmxWcdmaMXUplinkTestModel**
  - Upon return, contains the uplink test model when the user sets the SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode) method to TestModel.

###### Return Value

Int32

##### Remarks

UplinkTestModel

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5f9b4807-5523-a42b-1610-f16b75d87556.htm language=enus -->
## TOPIC 00061: rfmxwcdmadotnet/html/5f9b4807-5523-a42b-1610-f16b75d87556.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5f9b4807-5523-a42b-1610-f16b75d87556.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5f9b4807-5523-a42b-1610-f16b75d87556.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.AbortMeasurements Method

RFmxWcdmaMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.WcdmaMX

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

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/5fdd72c7-3c0e-5cb5-db7e-4a52255530dd.htm language=enus -->
## TOPIC 00062: rfmxwcdmadotnet/html/5fdd72c7-3c0e-5cb5-db7e-4a52255530dd.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/5fdd72c7-3c0e-5cb5-db7e-4a52255530dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/5fdd72c7-3c0e-5cb5-db7e-4a52255530dd.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXExtension.GetWcdmaSignalConfiguration Method

RFmxWcdmaMXExtensionGetWcdmaSignalConfiguration Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetWcdmaSignalConfiguration(RFmxInstrMX) | Creates a new default WCDMA signal configuration if it doesn't exist; otherwise, it returns the existing default WCDMA signal configuration. |
|  | GetWcdmaSignalConfiguration(RFmxInstrMX, String) | Creates a WCDMA signal configuration for specified signal name. Existing WCDMA signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxWcdmaMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/60861b9c-1fda-787e-a8e5-656ecf73a837.htm language=enus -->
## TOPIC 00063: rfmxwcdmadotnet/html/60861b9c-1fda-787e-a8e5-656ecf73a837.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/60861b9c-1fda-787e-a8e5-656ecf73a837.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/60861b9c-1fda-787e-a8e5-656ecf73a837.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemResults.GetUpperOffsetMarginAbsolutePower Method

RFmxWcdmaMXSemResultsGetUpperOffsetMarginAbsolutePower Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetMarginAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetMarginAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the power at the frequency corresponding to the GetUpperOffsetMargin(String, Double) method.This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMarginAbsolutePower

##### See Also

###### Reference

RFmxWcdmaMXSemResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/60edb0a1-e60f-72b0-6516-1008c5823cea.htm language=enus -->
## TOPIC 00064: rfmxwcdmadotnet/html/60edb0a1-e60f-72b0-6516-1008c5823cea.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/60edb0a1-e60f-72b0-6516-1008c5823cea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/60edb0a1-e60f-72b0-6516-1008c5823cea.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.GetPowerUnit Method

RFmxWcdmaMXCdaConfigurationGetPowerUnit Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPowerUnit(
	string selectorString,
	out RFmxWcdmaMXCdaPowerUnit value
)
```

```text
Public Function GetPowerUnit ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXCdaPowerUnit
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXCdaPowerUnit**
  - Upon return, contains the measurement unit of all power results, except GetTotalPower(String, Double).

###### Return Value

Int32

##### Remarks

CdaPowerUnit

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/60f8ab71-032c-7057-8d25-0c79a31c8c69.htm language=enus -->
## TOPIC 00065: rfmxwcdmadotnet/html/60f8ab71-032c-7057-8d25-0c79a31c8c69.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/60f8ab71-032c-7057-8d25-0c79a31c8c69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/60f8ab71-032c-7057-8d25-0c79a31c8c69.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemConfiguration.SetSweepTimeAuto Method

RFmxWcdmaMXSemConfigurationSetSweepTimeAuto Method

Sets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSweepTimeAuto(
	string selectorString,
	RFmxWcdmaMXSemSweepTimeAuto value
)
```

```text
Public Function SetSweepTimeAuto ( 
	selectorString As String,
	value As RFmxWcdmaMXSemSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXSemSweepTimeAuto**
  - Specifies whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

SemSweepTimeAuto

True

##### See Also

###### Reference

RFmxWcdmaMXSemConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/61f90b17-88c1-e32e-0dd9-5467a2d89752.htm language=enus -->
## TOPIC 00066: rfmxwcdmadotnet/html/61f90b17-88c1-e32e-0dd9-5467a2d89752.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/61f90b17-88c1-e32e-0dd9-5467a2d89752.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/61f90b17-88c1-e32e-0dd9-5467a2d89752.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.GetMeasurementChannelModulationType Method

RFmxWcdmaMXCdaConfigurationGetMeasurementChannelModulationType Method

Gets the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementChannelModulationType(
	string selectorString,
	out RFmxWcdmaMXCdaMeasurementChannelModulationType value
)
```

```text
Public Function GetMeasurementChannelModulationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXCdaMeasurementChannelModulationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXCdaMeasurementChannelModulationType**
  - Upon return, contains the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

###### Return Value

Int32

##### Remarks

CdaMeasurementChannelModulationType

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/64a48889-abcb-7b72-aad1-d4f82392d13e.htm language=enus -->
## TOPIC 00067: rfmxwcdmadotnet/html/64a48889-abcb-7b72-aad1-d4f82392d13e.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/64a48889-abcb-7b72-aad1-d4f82392d13e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/64a48889-abcb-7b72-aad1-d4f82392d13e.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXQevm.Results Property

RFmxWcdmaMXQevmResults Property

RFmxWcdmaMXQevmResults

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWcdmaMXQevmResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxWcdmaMXQevmResults
	Get
```

###### Property Value

RFmxWcdmaMXQevmResults

##### See Also

###### Reference

RFmxWcdmaMXQevm Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/66087d34-e26a-56d2-a865-2183f4127766.htm language=enus -->
## TOPIC 00068: rfmxwcdmadotnet/html/66087d34-e26a-56d2-a865-2183f4127766.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/66087d34-e26a-56d2-a865-2183f4127766.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/66087d34-e26a-56d2-a865-2183f4127766.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.ConfigureUplinkTestModelArray Method

RFmxWcdmaMXConfigureUplinkTestModelArray Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUplinkTestModelArray(
	string selectorString,
	RFmxWcdmaMXUplinkTestModel[] uplinkTestModel
)
```

```text
Public Function ConfigureUplinkTestModelArray ( 
	selectorString As String,
	uplinkTestModel As RFmxWcdmaMXUplinkTestModel()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **uplinkTestModel RFmxWcdmaMXUplinkTestModel**
  - Specifies the array of the uplink test model when the user sets the SetChannelConfigurationMode(String, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R(n), where n is the oldest release number with a given set of channel configurations.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/677b213c-64fc-0e22-9366-b91768ad35cd.htm language=enus -->
## TOPIC 00069: rfmxwcdmadotnet/html/677b213c-64fc-0e22-9366-b91768ad35cd.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/677b213c-64fc-0e22-9366-b91768ad35cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/677b213c-64fc-0e22-9366-b91768ad35cd.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXIQPowerEdgeTriggerSlope Enumeration

RFmxWcdmaMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXIQPowerEdgeTriggerSlope
```

```text
Public Enumeration RFmxWcdmaMXIQPowerEdgeTriggerSlope
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6a45c600-0e14-e1e0-ec9e-4e54628d50da.htm language=enus -->
## TOPIC 00070: rfmxwcdmadotnet/html/6a45c600-0e14-e1e0-ec9e-4e54628d50da.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6a45c600-0e14-e1e0-ec9e-4e54628d50da.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6a45c600-0e14-e1e0-ec9e-4e54628d50da.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXQevmConfiguration.GetSpectrumInverted Method

RFmxWcdmaMXQevmConfigurationGetSpectrumInverted Method

Gets whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectrumInverted(
	string selectorString,
	out RFmxWcdmaMXQevmSpectrumInverted value
)
```

```text
Public Function GetSpectrumInverted ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXQevmSpectrumInverted
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXQevmSpectrumInverted**
  - Upon return, contains whether the spectrum of the signal is inverted.

###### Return Value

Int32

##### Remarks

QevmSpectrumInverted

False

##### See Also

###### Reference

RFmxWcdmaMXQevmConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6ce8c6f4-7128-570c-0719-ff4c001a1e47.htm language=enus -->
## TOPIC 00071: rfmxwcdmadotnet/html/6ce8c6f4-7128-570c-0719-ff4c001a1e47.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6ce8c6f4-7128-570c-0719-ff4c001a1e47.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6ce8c6f4-7128-570c-0719-ff4c001a1e47.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpResults Class

RFmxWcdmaMXAcpResults Class

Provides methods to fetch and read the ACP measurement results.

##### Inheritance Hierarchy

RFmxWcdmaMXSubObject

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxWcdmaMXAcpResults : RFmxWcdmaMXSubObject
```

```text
Public NotInheritable Class RFmxWcdmaMXAcpResults
	Inherits RFmxWcdmaMXSubObject
```

The RFmxWcdmaMXAcpResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchAbsolutePowersTrace | Fetches the absolute powers trace for the ACP measurement. |
|  | FetchCarrierMeasurement | Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power. Use "carrier(n)" as the selector string to configure this method. |
|  | FetchCarrierMeasurementArray | Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the GetTotalCarrierPower(String, Double) method. |
|  | FetchOffsetMeasurement | Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. Use "offset(n)" as the selector string to configure this method. |
|  | FetchOffsetMeasurementArray | Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the SetOffsetPowerReferenceCarrier(String, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method. |
|  | FetchRelativePowersTrace | Fetches the relative powers trace for the ACP measurement. |
|  | FetchSpectrum | Fetches the spectrum used for the ACP measurement. |
|  | FetchTotalCarrierPower | Fetches the total carrier power for the ACP measurement. |
|  | GetCarrierAbsolutePower | Gets the carrier power.This value is expressed in dBm. |
|  | GetCarrierRelativePower | Gets the carrier power relative to the GetTotalCarrierPower(String, Double).This value is expressed in dB. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetLowerOffsetAbsolutePower | Gets the lower offset channel power. This value is expressed in dBm. |
|  | GetLowerOffsetRelativePower | Gets the lower offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(String, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |
|  | GetTotalCarrierPower | Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(String, Double) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetUpperOffsetAbsolutePower | Gets the upper offset channel power.This value is expressed in dBm. |
|  | GetUpperOffsetRelativePower | Gets the upper offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(String, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6e00d2b4-b072-10e0-b276-10a880471018.htm language=enus -->
## TOPIC 00072: rfmxwcdmadotnet/html/6e00d2b4-b072-10e0-b276-10a880471018.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6e00d2b4-b072-10e0-b276-10a880471018.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6e00d2b4-b072-10e0-b276-10a880471018.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.SetAttributeBool Method

RFmxWcdmaMXSetAttributeBool Method

Sets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeBool(
	string selectorString,
	int attributeIdentifier,
	bool value
)
```

```text
Public Function SetAttributeBool ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx WCDMA Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Boolean**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6eb10bc5-e437-7e6f-1e12-8d566a736a34.htm language=enus -->
## TOPIC 00073: rfmxwcdmadotnet/html/6eb10bc5-e437-7e6f-1e12-8d566a736a34.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6eb10bc5-e437-7e6f-1e12-8d566a736a34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6eb10bc5-e437-7e6f-1e12-8d566a736a34.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpResults.GetLowerOffsetRelativePower Method

RFmxWcdmaMXAcpResultsGetLowerOffsetRelativePower Method

SetOffsetPowerReferenceCarrier(String, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier)

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetRelativePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetRelativePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the lower offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(String, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB.

###### Return Value

Int32

##### Remarks

AcpResultsLowerOffsetRelativePower

##### See Also

###### Reference

RFmxWcdmaMXAcpResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6eb4eea8-8c59-fa3d-5a11-4492f90436a5.htm language=enus -->
## TOPIC 00074: rfmxwcdmadotnet/html/6eb4eea8-8c59-fa3d-5a11-4492f90436a5.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6eb4eea8-8c59-fa3d-5a11-4492f90436a5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6eb4eea8-8c59-fa3d-5a11-4492f90436a5.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.ConfigureRbwFilter Method

RFmxWcdmaMXAcpConfigurationConfigureRbwFilter Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRbwFilter(
	string selectorString,
	RFmxWcdmaMXAcpRbwAutoBandwidth rbwAuto,
	double rbw,
	RFmxWcdmaMXAcpRbwFilterType rbwFilterType
)
```

```text
Public Function ConfigureRbwFilter ( 
	selectorString As String,
	rbwAuto As RFmxWcdmaMXAcpRbwAutoBandwidth,
	rbw As Double,
	rbwFilterType As RFmxWcdmaMXAcpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rbwAuto RFmxWcdmaMXAcpRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW.
- **rbw Double**
  - Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the rbwAuto parameter to False. This parameter is valid only if you set the rbwFilterType parameter to Gaussian or Flat. This value is expressed in Hz.
- **rbwFilterType RFmxWcdmaMXAcpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6ee4c2af-77a6-29ab-38ca-40ec986b3d0b.htm language=enus -->
## TOPIC 00075: rfmxwcdmadotnet/html/6ee4c2af-77a6-29ab-38ca-40ec986b3d0b.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6ee4c2af-77a6-29ab-38ca-40ec986b3d0b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6ee4c2af-77a6-29ab-38ca-40ec986b3d0b.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.Chp Property

RFmxWcdmaMXChp Property

RFmxWcdmaMXChp

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWcdmaMXChp Chp { get; }
```

```text
Public ReadOnly Property Chp As RFmxWcdmaMXChp
	Get
```

###### Property Value

RFmxWcdmaMXChp

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6f49b291-90a5-9f04-4a37-f499c05a3146.htm language=enus -->
## TOPIC 00076: rfmxwcdmadotnet/html/6f49b291-90a5-9f04-4a37-f499c05a3146.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6f49b291-90a5-9f04-4a37-f499c05a3146.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6f49b291-90a5-9f04-4a37-f499c05a3146.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.GetMeasurementEnabled Method

RFmxWcdmaMXCdaConfigurationGetMeasurementEnabled Method

Gets whether to enable the CDA measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Upon return, contains whether to enable the CDA measurement.

###### Return Value

Int32

##### Remarks

CdaMeasurementEnabled

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6fba2a07-2d62-baf9-a105-edafb8107f7f.htm language=enus -->
## TOPIC 00077: rfmxwcdmadotnet/html/6fba2a07-2d62-baf9-a105-edafb8107f7f.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6fba2a07-2d62-baf9-a105-edafb8107f7f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6fba2a07-2d62-baf9-a105-edafb8107f7f.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.GetMeasurementOffset Method

RFmxWcdmaMXCdaConfigurationGetMeasurementOffset Method

SetSynchronizationMode(String, RFmxWcdmaMXCdaSynchronizationMode)

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementOffset(
	string selectorString,
	out int value
)
```

```text
Public Function GetMeasurementOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxWcdmaMXCdaSynchronizationMode) method.

###### Return Value

Int32

##### Remarks

CdaMeasurementOffset

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/6feea389-ff6d-ee6d-dc41-a510453d5b7c.htm language=enus -->
## TOPIC 00078: rfmxwcdmadotnet/html/6feea389-ff6d-ee6d-dc41-a510453d5b7c.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/6feea389-ff6d-ee6d-dc41-a510453d5b7c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/6feea389-ff6d-ee6d-dc41-a510453d5b7c.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.ConfigureUserDefinedChannel Method

RFmxWcdmaMXConfigureUserDefinedChannel Method

SetNumberOfChannels(String, Int32)

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUserDefinedChannel(
	string selectorString,
	int spreadingFactor,
	int spreadingCode,
	RFmxWcdmaMXModulationType modulationType,
	RFmxWcdmaMXBranch branch
)
```

```text
Public Function ConfigureUserDefinedChannel ( 
	selectorString As String,
	spreadingFactor As Integer,
	spreadingCode As Integer,
	modulationType As RFmxWcdmaMXModulationType,
	branch As RFmxWcdmaMXBranch
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the signal name, carrier number, and channel number. Example:"carrier0/channel0" You can use the BuildChannelString(String, Int32) method to build the selector string.
- **spreadingFactor Int32**
  - Specifies the spreading factor of the channel.
- **spreadingCode Int32**
  - Specifies the spreading code of the channel.
- **modulationType RFmxWcdmaMXModulationType**
  - Specifies the modulation type of the channel.
- **branch RFmxWcdmaMXBranch**
  - Specifies the branch on which the data is modulated.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/70ef9389-9a2e-1f57-64d8-2ed5d8e3bf0f.htm language=enus -->
## TOPIC 00079: rfmxwcdmadotnet/html/70ef9389-9a2e-1f57-64d8-2ed5d8e3bf0f.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/70ef9389-9a2e-1f57-64d8-2ed5d8e3bf0f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/70ef9389-9a2e-1f57-64d8-2ed5d8e3bf0f.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.GetNumberOfAnalysisThreads Method

RFmxWcdmaMXAcpConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the ACP measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Upon return, contains the maximum number of threads used for parallelism for the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/715384a3-bb78-bd82-1726-6870c06591b4.htm language=enus -->
## TOPIC 00080: rfmxwcdmadotnet/html/715384a3-bb78-bd82-1726-6870c06591b4.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/715384a3-bb78-bd82-1726-6870c06591b4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/715384a3-bb78-bd82-1726-6870c06591b4.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.GetOffsetPowerReferenceSpecific Method

RFmxWcdmaMXAcpConfigurationGetOffsetPowerReferenceSpecific Method

Gets the index of the reference carrier.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetPowerReferenceSpecific(
	string selectorString,
	out int value
)
```

```text
Public Function GetOffsetPowerReferenceSpecific ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the index of the reference carrier.

###### Return Value

Int32

##### Remarks

AcpOffsetPowerReferenceSpecific

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/725acdd3-2402-8256-6b71-4d49b236cbe9.htm language=enus -->
## TOPIC 00081: rfmxwcdmadotnet/html/725acdd3-2402-8256-6b71-4d49b236cbe9.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/725acdd3-2402-8256-6b71-4d49b236cbe9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/725acdd3-2402-8256-6b71-4d49b236cbe9.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccConfiguration.SetIQGainImbalanceRemovalEnabled Method

RFmxWcdmaMXModAccConfigurationSetIQGainImbalanceRemovalEnabled Method

Sets whether to remove I/Q gain imbalance before the ModAcc Measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQGainImbalanceRemovalEnabled(
	string selectorString,
	RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled value
)
```

```text
Public Function SetIQGainImbalanceRemovalEnabled ( 
	selectorString As String,
	value As RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled**
  - Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement.

###### Return Value

Int32

##### Remarks

ModAccIQGainImbalanceRemovalEnabled

False

##### See Also

###### Reference

RFmxWcdmaMXModAccConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/73a5668e-57e8-22cd-2c40-4616fba85b8f.htm language=enus -->
## TOPIC 00082: rfmxwcdmadotnet/html/73a5668e-57e8-22cd-2c40-4616fba85b8f.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/73a5668e-57e8-22cd-2c40-4616fba85b8f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/73a5668e-57e8-22cd-2c40-4616fba85b8f.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.ConfigureUserDefinedChannelArray Method

RFmxWcdmaMXConfigureUserDefinedChannelArray Method

SetNumberOfChannels(String, Int32)

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUserDefinedChannelArray(
	string selectorString,
	int[] spreadingFactor,
	int[] spreadingCode,
	RFmxWcdmaMXModulationType[] modulationType,
	RFmxWcdmaMXBranch[] branch
)
```

```text
Public Function ConfigureUserDefinedChannelArray ( 
	selectorString As String,
	spreadingFactor As Integer(),
	spreadingCode As Integer(),
	modulationType As RFmxWcdmaMXModulationType(),
	branch As RFmxWcdmaMXBranch()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of carrier number. Example:"carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **spreadingFactor Int32**
  - Specifies an array of spreading factor of the channels.
- **spreadingCode Int32**
  - Specifies an array of spreading code of the channels.
- **modulationType RFmxWcdmaMXModulationType**
  - Specifies an array of modulation types of the channels.
- **branch RFmxWcdmaMXBranch**
  - Specifies an array of branches on which the data is modulated in the channel.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/743d3025-a2fa-b59e-ced3-b0ae798d5eb6.htm language=enus -->
## TOPIC 00083: rfmxwcdmadotnet/html/743d3025-a2fa-b59e-ced3-b0ae798d5eb6.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/743d3025-a2fa-b59e-ced3-b0ae798d5eb6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/743d3025-a2fa-b59e-ced3-b0ae798d5eb6.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccResults.GetPeakRcdeCode Method

RFmxWcdmaMXModAccResultsGetPeakRcdeCode Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakRcdeCode(
	string selectorString,
	out int value
)
```

```text
Public Function GetPeakRcdeCode ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the spreading code of the channel corresponding to the value of the GetPeakRcde(String, Double) method for a carrier.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakRcdeCode

##### See Also

###### Reference

RFmxWcdmaMXModAccResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/7a1b3dda-09b8-93aa-c44d-66d7284ccef0.htm language=enus -->
## TOPIC 00084: rfmxwcdmadotnet/html/7a1b3dda-09b8-93aa-c44d-66d7284ccef0.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/7a1b3dda-09b8-93aa-c44d-66d7284ccef0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/7a1b3dda-09b8-93aa-c44d-66d7284ccef0.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.GetIQPowerEdgeTriggerSlope Method

RFmxWcdmaMXGetIQPowerEdgeTriggerSlope Method

Gets whether the device asserts the trigger when the signal power is rising or when it is falling.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerSlope(
	string selectorString,
	out RFmxWcdmaMXIQPowerEdgeTriggerSlope value
)
```

```text
Public Function GetIQPowerEdgeTriggerSlope ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWcdmaMXIQPowerEdgeTriggerSlope
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXIQPowerEdgeTriggerSlope**
  - Upon return, contains whether the device asserts the trigger when the signal power is rising or when it is falling.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSlope

Rising

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/7c769329-608f-bdfe-d50f-03ae99dc1619.htm language=enus -->
## TOPIC 00085: rfmxwcdmadotnet/html/7c769329-608f-bdfe-d50f-03ae99dc1619.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/7c769329-608f-bdfe-d50f-03ae99dc1619.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/7c769329-608f-bdfe-d50f-03ae99dc1619.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.SetBranch Method

RFmxWcdmaMXSetBranch Method

Sets the branch on which the data is modulated in the channel.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetBranch(
	string selectorString,
	RFmxWcdmaMXBranch value
)
```

```text
Public Function SetBranch ( 
	selectorString As String,
	value As RFmxWcdmaMXBranch
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the channel number and carrier number. Example: "carrier0" or "carrier0/channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value RFmxWcdmaMXBranch**
  - Specifies the branch on which the data is modulated in the channel.

###### Return Value

Int32

##### Remarks

SetBranch(String, RFmxWcdmaMXBranch)

I

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/80abb7f3-ae58-8b38-1c68-e9d66408e1f2.htm language=enus -->
## TOPIC 00086: rfmxwcdmadotnet/html/80abb7f3-ae58-8b38-1c68-e9d66408e1f2.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/80abb7f3-ae58-8b38-1c68-e9d66408e1f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/80abb7f3-ae58-8b38-1c68-e9d66408e1f2.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemConfiguration.GetOffsetBandwidthIntegral Method

RFmxWcdmaMXSemConfigurationGetOffsetBandwidthIntegral Method

Gets the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetBandwidthIntegral(
	string selectorString,
	out int value
)
```

```text
Public Function GetOffsetBandwidthIntegral ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW.

###### Return Value

Int32

##### Remarks

SemOffsetBandwidthIntegral

##### See Also

###### Reference

RFmxWcdmaMXSemConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/827cda3a-10ae-e825-3a94-3db5f4f2e8e5.htm language=enus -->
## TOPIC 00087: rfmxwcdmadotnet/html/827cda3a-10ae-e825-3a94-3db5f4f2e8e5.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/827cda3a-10ae-e825-3a94-3db5f4f2e8e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/827cda3a-10ae-e825-3a94-3db5f4f2e8e5.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXChpConfiguration.SetRbwFilterAutoBandwidth Method

RFmxWcdmaMXChpConfigurationSetRbwFilterAutoBandwidth Method

Sets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAutoBandwidth(
	string selectorString,
	RFmxWcdmaMXChpRbwAutoBandwidth value
)
```

```text
Public Function SetRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxWcdmaMXChpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxWcdmaMXChpRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

ChpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxWcdmaMXChpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/8d866059-e147-a7de-7ab8-60293a2757be.htm language=enus -->
## TOPIC 00088: rfmxwcdmadotnet/html/8d866059-e147-a7de-7ab8-60293a2757be.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/8d866059-e147-a7de-7ab8-60293a2757be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/8d866059-e147-a7de-7ab8-60293a2757be.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaConfiguration.GetMeasurementChannelSpreadingFactor Method

RFmxWcdmaMXCdaConfigurationGetMeasurementChannelSpreadingFactor Method

Gets the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementChannelSpreadingFactor(
	string selectorString,
	out int value
)
```

```text
Public Function GetMeasurementChannelSpreadingFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

###### Return Value

Int32

##### Remarks

CdaMeasurementChannelSpreadingFactor

##### See Also

###### Reference

RFmxWcdmaMXCdaConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/8e130986-1863-6bdb-4e8d-b9b1facd6f6b.htm language=enus -->
## TOPIC 00089: rfmxwcdmadotnet/html/8e130986-1863-6bdb-4e8d-b9b1facd6f6b.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/8e130986-1863-6bdb-4e8d-b9b1facd6f6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/8e130986-1863-6bdb-4e8d-b9b1facd6f6b.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.ConfigureOffsetPowerReference Method

RFmxWcdmaMXAcpConfigurationConfigureOffsetPowerReference Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetPowerReference(
	string selectorString,
	RFmxWcdmaMXAcpOffsetPowerReferenceCarrier offsetPowerReferenceCarrier,
	int offsetPowerReferenceSpecific
)
```

```text
Public Function ConfigureOffsetPowerReference ( 
	selectorString As String,
	offsetPowerReferenceCarrier As RFmxWcdmaMXAcpOffsetPowerReferenceCarrier,
	offsetPowerReferenceSpecific As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetPowerReferenceCarrier RFmxWcdmaMXAcpOffsetPowerReferenceCarrier**
  - Specifies the carrier to use as the power reference to measure offset channel relative power.
- **offsetPowerReferenceSpecific Int32**
  - Specifies the index of the carrier to be used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the offsetPowerReferenceCarrier parameter to Specific.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/8fbd59d4-d8a3-cca9-2dd8-d98ecdc2adcd.htm language=enus -->
## TOPIC 00090: rfmxwcdmadotnet/html/8fbd59d4-d8a3-cca9-2dd8-d98ecdc2adcd.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/8fbd59d4-d8a3-cca9-2dd8-d98ecdc2adcd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/8fbd59d4-d8a3-cca9-2dd8-d98ecdc2adcd.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemResults.GetLowerOffsetAbsolutePeakPower Method

RFmxWcdmaMXSemResultsGetLowerOffsetAbsolutePeakPower Method

Gets the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetAbsolutePeakPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetAbsolutePeakPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetAbsolutePeakPower

##### See Also

###### Reference

RFmxWcdmaMXSemResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/9336f554-6706-7944-3249-a590963d8ff2.htm language=enus -->
## TOPIC 00091: rfmxwcdmadotnet/html/9336f554-6706-7944-3249-a590963d8ff2.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/9336f554-6706-7944-3249-a590963d8ff2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/9336f554-6706-7944-3249-a590963d8ff2.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemResults.GetLowerOffsetMarginRelativePower Method

RFmxWcdmaMXSemResultsGetLowerOffsetMarginRelativePower Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetMarginRelativePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetMarginRelativePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the power at the frequency corresponding to the value of the GetLowerOffsetMargin(String, Double) method and relative to the GetTotalCarrierPower(String, Double) method. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetMarginRelativePower

##### See Also

###### Reference

RFmxWcdmaMXSemResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/938ba05a-7717-6741-86bc-bd0d78e65c7e.htm language=enus -->
## TOPIC 00092: rfmxwcdmadotnet/html/938ba05a-7717-6741-86bc-bd0d78e65c7e.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/938ba05a-7717-6741-86bc-bd0d78e65c7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/938ba05a-7717-6741-86bc-bd0d78e65c7e.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemResults.GetUpperOffsetAbsoluteIntegratedPower Method

RFmxWcdmaMXSemResultsGetUpperOffsetAbsoluteIntegratedPower Method

Gets the power measured in the upper, or positive, offset segment.This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetAbsoluteIntegratedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetAbsoluteIntegratedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the power measured in the upper, or positive, offset segment.This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetAbsoluteIntegratedPower

##### See Also

###### Reference

RFmxWcdmaMXSemResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/9bbbf8f1-2592-8ccf-bde8-ac08b30eba4d.htm language=enus -->
## TOPIC 00093: rfmxwcdmadotnet/html/9bbbf8f1-2592-8ccf-bde8-ac08b30eba4d.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/9bbbf8f1-2592-8ccf-bde8-ac08b30eba4d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/9bbbf8f1-2592-8ccf-bde8-ac08b30eba4d.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSlotPhaseConfiguration.GetMeasurementLength Method

RFmxWcdmaMXSlotPhaseConfigurationGetMeasurementLength Method

Gets the duration of the SlotPhase measurement. This value is expressed in slots.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementLength(
	string selectorString,
	out int value
)
```

```text
Public Function GetMeasurementLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the duration of the SlotPhase measurement. This value is expressed in slots.

###### Return Value

Int32

##### Remarks

SlotPhaseMeasurementLength

##### See Also

###### Reference

RFmxWcdmaMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/9c1c008c-cffb-5b84-4e0c-4043695ddc0c.htm language=enus -->
## TOPIC 00094: rfmxwcdmadotnet/html/9c1c008c-cffb-5b84-4e0c-4043695ddc0c.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/9c1c008c-cffb-5b84-4e0c-4043695ddc0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/9c1c008c-cffb-5b84-4e0c-4043695ddc0c.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXSemResults.GetUpperOffsetRelativePeakPower Method

RFmxWcdmaMXSemResultsGetUpperOffsetRelativePeakPower Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetRelativePeakPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetRelativePeakPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the peak power measured in the upper, or positive, offset segment relative to the value of the GetTotalCarrierPower(String, Double) method.This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetRelativePeakPower

##### See Also

###### Reference

RFmxWcdmaMXSemResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/9ca145a6-83dc-5079-04a8-6edc6a50216b.htm language=enus -->
## TOPIC 00095: rfmxwcdmadotnet/html/9ca145a6-83dc-5079-04a8-6edc6a50216b.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/9ca145a6-83dc-5079-04a8-6edc6a50216b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/9ca145a6-83dc-5079-04a8-6edc6a50216b.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpConfiguration.GetFftOverlap Method

RFmxWcdmaMXAcpConfigurationGetFftOverlap Method

Gets the number of samples to overlap between consecutive chunks while performing FFT. This value is expressed as a percentage of the Sequential FFT Size when you set the RFmxWcdmaMXAcpMeasurementMethod method to Sequential FFT.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftOverlap(
	string selectorString,
	out double value
)
```

```text
Public Function GetFftOverlap ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, gets the number of samples to overlap between consecutive chunks while performing FFT.

###### Return Value

Int32

##### Remarks

AcpFftOverlap

##### See Also

###### Reference

RFmxWcdmaMXAcpConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/9daeeb65-980f-b8e8-d5d8-c6e10d0d5493.htm language=enus -->
## TOPIC 00096: rfmxwcdmadotnet/html/9daeeb65-980f-b8e8-d5d8-c6e10d0d5493.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/9daeeb65-980f-b8e8-d5d8-c6e10d0d5493.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/9daeeb65-980f-b8e8-d5d8-c6e10d0d5493.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXCdaResults.FetchCodeDomainPower Method

RFmxWcdmaMXCdaResultsFetchCodeDomainPower Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCodeDomainPower(
	string selectorString,
	double timeout,
	out double totalPower,
	out double totalActivePower,
	out double meanActivePower,
	out double peakActivePower,
	out double meanInactivePower,
	out double peakInactivePower
)
```

```text
Public Function FetchCodeDomainPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef totalPower As Double,
	<OutAttribute> ByRef totalActivePower As Double,
	<OutAttribute> ByRef meanActivePower As Double,
	<OutAttribute> ByRef peakActivePower As Double,
	<OutAttribute> ByRef meanInactivePower As Double,
	<OutAttribute> ByRef peakInactivePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **totalPower Double**
  - Upon return, contains the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm.
- **totalActivePower Double**
  - Upon return, contains the sum of all the active channel powers. If you set the SetPowerUnit(String, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(String, Double) method. This value is expressed in dB or dBm.
- **meanActivePower Double**
  - Upon return, contains the average of all the active channel powers. If you set the CDA Pwr Unit method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr method. This value is expressed in dB or dBm.
- **peakActivePower Double**
  - Upon return, contains the largest code power among the set of active channels in the code domain. If you set the CDA Pwr Unit method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr method. This value is expressed in dB or dBm.
- **meanInactivePower Double**
  - Upon return, contains the average code power among the set of inactive channels in the code domain. If you set the CDA Pwr Unit method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr method. This value is expressed in dB or dBm.
- **peakInactivePower Double**
  - Upon return, contains the largest code power among the set of inactive channels in the code domain. If you set the CDA Pwr Unit method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr method. This value is expressed in dB or dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXCdaResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/a38b199c-c8b4-22ea-d7e7-6b742b0d87cc.htm language=enus -->
## TOPIC 00097: rfmxwcdmadotnet/html/a38b199c-c8b4-22ea-d7e7-6b742b0d87cc.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/a38b199c-c8b4-22ea-d7e7-6b742b0d87cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/a38b199c-c8b4-22ea-d7e7-6b742b0d87cc.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccConfiguration Methods

RFmxWcdmaMXModAccConfiguration Methods

The [RFmxWcdmaMXModAccConfiguration](e6c1f884-f447-0bf5-2184-7ab8fd6606ec.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureReferenceWaveform | Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements.This method is used only when you set the SetSynchronizationMode(String, RFmxWcdmaMXModAccSynchronizationMode) method to Marker. |
|  | ConfigureSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQGainImbalanceRemovalEnabled | Gets whether to remove I/Q gain imbalance before the ModAcc Measurement. |
|  | GetIQOffsetRemovalEnabled | Gets whether to remove the I/Q offset before the ModAcc measurement. |
|  | GetIQQuadratureErrorRemovalEnabled | Gets whether to remove the I/Q quadrature error before the ModAcc measurement. |
|  | GetMeasurementEnabled | Gets whether to enable the ModAcc measurement. |
|  | GetMeasurementLength | Gets the duration of the ModAcc measurement. This value is expressed in slots. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxWcdmaMXModAccSynchronizationMode) method. |
|  | GetRrcFilterEnabled | Gets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | GetSpectrumInverted | Gets whether the spectrum of the signal is inverted. |
|  | GetSynchronizationMode | Gets whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | GetTransientRemovalEnabled | Gets whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. |
|  | SetIQGainImbalanceRemovalEnabled | Sets whether to remove I/Q gain imbalance before the ModAcc Measurement. |
|  | SetIQOffsetRemovalEnabled | Sets whether to remove the I/Q offset before the ModAcc measurement. |
|  | SetIQQuadratureErrorRemovalEnabled | Sets whether to remove the I/Q quadrature error before the ModAcc measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the ModAcc measurement. |
|  | SetMeasurementLength | Sets the duration of the ModAcc measurement. This value is expressed in slots. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxWcdmaMXModAccSynchronizationMode) method. |
|  | SetRrcFilterEnabled | Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | SetSpectrumInverted | Sets whether the spectrum of the signal is inverted. |
|  | SetSynchronizationMode | Sets whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | SetTransientRemovalEnabled | Sets whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxWcdmaMXModAccConfiguration Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/a3a73827-180c-46f2-1466-5343d36c7ae7.htm language=enus -->
## TOPIC 00098: rfmxwcdmadotnet/html/a3a73827-180c-46f2-1466-5343d36c7ae7.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/a3a73827-180c-46f2-1466-5343d36c7ae7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/a3a73827-180c-46f2-1466-5343d36c7ae7.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAccResults.FetchConstellationTrace Method

RFmxWcdmaMXModAccResultsFetchConstellationTrace Method

Namespace:

NationalInstruments.RFmx.WcdmaMX

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
  - Specifies a selector string comprising of the result name, and carrier number. If you do not specify the result name, the default result instance is used. Example:"carrier0""result::r1/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.
- **constellation ComplexSingle**
  - Upon return, contains an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWcdmaMXModAccResults Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/a46eabf8-584e-30ca-9c22-f9d8dee89277.htm language=enus -->
## TOPIC 00099: rfmxwcdmadotnet/html/a46eabf8-584e-30ca-9c22-f9d8dee89277.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/a46eabf8-584e-30ca-9c22-f9d8dee89277.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/a46eabf8-584e-30ca-9c22-f9d8dee89277.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMX.GetTriggerMinimumQuietTimeDuration Method

RFmxWcdmaMXGetTriggerMinimumQuietTimeDuration Method

Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerMinimumQuietTimeDuration(
	string selectorString,
	out double value
)
```

```text
Public Function GetTriggerMinimumQuietTimeDuration ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TriggerMinimumQuietTimeDuration

##### See Also

###### Reference

RFmxWcdmaMX Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/ae629e2c-4bb2-0ca8-95e3-3e3035d91bfb.htm language=enus -->
## TOPIC 00100: rfmxwcdmadotnet/html/ae629e2c-4bb2-0ca8-95e3-3e3035d91bfb.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/ae629e2c-4bb2-0ca8-95e3-3e3035d91bfb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/ae629e2c-4bb2-0ca8-95e3-3e3035d91bfb.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXAcpFftOverlapMode Enumeration

RFmxWcdmaMXAcpFftOverlapMode Enumeration

Specifies how overlapping is applied when computing the FFT of the acquired samples. The default value is Disabled.

Namespace:

NationalInstruments.RFmx.WcdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWcdmaMXAcpFftOverlapMode
```

```text
Public Enumeration RFmxWcdmaMXAcpFftOverlapMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Indicates that overlapping is not applied to the acquired samples. |
| Automatic | 1 | Indicates that the RFmx driver automatically chooses optimal values of the ACP FFT Overlap method based on the measurement configuration. |

##### See Also

###### Reference

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wcdma-dotnet path=rfmxwcdmadotnet/html/aed9b50e-ce60-ea5f-366a-1850945c3593.htm language=enus -->
## TOPIC 00101: rfmxwcdmadotnet/html/aed9b50e-ce60-ea5f-366a-1850945c3593.htm

- bundle_id: `rfmx-wcdma-dotnet`
- source_path: `rfmxwcdmadotnet/html/aed9b50e-ce60-ea5f-366a-1850945c3593.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-dotnet/raw/resource/enus/rfmxwcdmadotnet/html/aed9b50e-ce60-ea5f-366a-1850945c3593.htm
- document_id: `rfmx-wcdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWcdmaMXModAcc Methods

RFmxWcdmaMXModAcc Methods

The [RFmxWcdmaMXModAcc](f9727a80-b4a8-eb2f-e87a-841fc9df5bc0.htm) type exposes the following members.

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

RFmxWcdmaMXModAcc Class

NationalInstruments.RFmx.WcdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
