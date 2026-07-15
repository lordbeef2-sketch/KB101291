# NI DOCUMENT BUNDLE: rfmx-pulse-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-pulse-dotnet start=1 end=117 -->
<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/014d2b5b-c4ca-a02d-1e6e-e0540a91c5a9.htm language=enus -->
## TOPIC 00001: rfmxpulsedotnet/html/014d2b5b-c4ca-a02d-1e6e-e0540a91c5a9.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/014d2b5b-c4ca-a02d-1e6e-e0540a91c5a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/014d2b5b-c4ca-a02d-1e6e-e0540a91c5a9.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetTriggerDelay Method

RFmxPulseMXGetTriggerDelay Method

Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerDelay(
	string selectorString,
	out double value
)
```

```text
Public Function GetTriggerDelay ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

###### Return Value

Int32

##### Remarks

TriggerDelay

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/01630b54-6c7e-0973-ff48-284cbbdee085.htm language=enus -->
## TOPIC 00002: rfmxpulsedotnet/html/01630b54-6c7e-0973-ff48-284cbbdee085.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/01630b54-6c7e-0973-ff48-284cbbdee085.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/01630b54-6c7e-0973-ff48-284cbbdee085.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulse.Results Property

RFmxPulseMXPulseResults Property

RFmxPulseMXPulseResults

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxPulseMXPulseResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxPulseMXPulseResults
	Get
```

###### Property Value

RFmxPulseMXPulseResults

##### See Also

###### Reference

RFmxPulseMXPulse Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/025c8c1f-a2d8-6324-02d9-399b4f5270d2.htm language=enus -->
## TOPIC 00003: rfmxpulsedotnet/html/025c8c1f-a2d8-6324-02d9-399b4f5270d2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/025c8c1f-a2d8-6324-02d9-399b4f5270d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/025c8c1f-a2d8-6324-02d9-399b4f5270d2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetDroopMaximum Method

RFmxPulseMXPulseResultsGetDroopMaximum Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDroopMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetDroopMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsDroopMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/05422d7e-9c7f-c638-5aba-ca8f1454d46a.htm language=enus -->
## TOPIC 00004: rfmxpulsedotnet/html/05422d7e-9c7f-c638-5aba-ca8f1454d46a.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/05422d7e-9c7f-c638-5aba-ca8f1454d46a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/05422d7e-9c7f-c638-5aba-ca8f1454d46a.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTimeSidelobePeakCorrelationMinimum Method

RFmxPulseMXPulseResultsGetTimeSidelobePeakCorrelationMinimum Method

Gets the minimum peak correlation across the measured pulses.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobePeakCorrelationMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetTimeSidelobePeakCorrelationMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum peak correlation across the measured pulses.

###### Return Value

Int32

##### Remarks

PulseResultsTimeSidelobePeakCorrelationMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/06e8e651-0e6c-8150-9cef-1271f78af4f2.htm language=enus -->
## TOPIC 00005: rfmxpulsedotnet/html/06e8e651-0e6c-8150-9cef-1271f78af4f2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/06e8e651-0e6c-8150-9cef-1271f78af4f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/06e8e651-0e6c-8150-9cef-1271f78af4f2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetMultipleMeasurementPointsWindowStart Method

RFmxPulseMXPulseConfigurationSetMultipleMeasurementPointsWindowStart Method

Sets the start of the measurement window used for multiple measurement points selection over pulse ON duration.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMultipleMeasurementPointsWindowStart(
	string selectorString,
	double value
)
```

```text
Public Function SetMultipleMeasurementPointsWindowStart ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the start of the measurement window used for multiple measurement points selection over pulse ON duration.

###### Return Value

Int32

##### Remarks

PulseMultipleMeasurementPointsWindowStart

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/076bdd73-0a69-96a0-4a0b-588c68300cc7.htm language=enus -->
## TOPIC 00006: rfmxpulsedotnet/html/076bdd73-0a69-96a0-4a0b-588c68300cc7.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/076bdd73-0a69-96a0-4a0b-588c68300cc7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/076bdd73-0a69-96a0-4a0b-588c68300cc7.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseDetectionReference Enumeration

RFmxPulseMXPulseDetectionReference Enumeration

SetDetectionThreshold(String, Double)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseDetectionReference
```

```text
Public Enumeration RFmxPulseMXPulseDetectionReference
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ReferenceLevel | 0 | The threshold is relative to the reference level of the samples. |
|  | Absolute | 1 | The threshold is the absolute power, in dBm. |
|  | Peak | 2 | The threshold is relative to the peak level of the samples. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/07bc15fc-f37a-55f1-2865-1f862603476c.htm language=enus -->
## TOPIC 00007: rfmxpulsedotnet/html/07bc15fc-f37a-55f1-2865-1f862603476c.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/07bc15fc-f37a-55f1-2865-1f862603476c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/07bc15fc-f37a-55f1-2865-1f862603476c.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseAmplitudeTraceUnit Enumeration

RFmxPulseMXPulseAmplitudeTraceUnit Enumeration

Specifies the unit of the amplitude level. This method is applicable only for the amplitude trace.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseAmplitudeTraceUnit
```

```text
Public Enumeration RFmxPulseMXPulseAmplitudeTraceUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | dBm | 0 | Amplitude trace is expressed in dBm. |
|  | Volts | 1 | Amplitude trace is expressed in Volts. |
|  | Watts | 2 | Amplitude trace is expressed in Watts. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/091a11b4-83b5-9cfa-b84b-82294cff4335.htm language=enus -->
## TOPIC 00008: rfmxpulsedotnet/html/091a11b4-83b5-9cfa-b84b-82294cff4335.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/091a11b4-83b5-9cfa-b84b-82294cff4335.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/091a11b4-83b5-9cfa-b84b-82294cff4335.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTimeSidelobeMainlobeWidthMinimum Method

RFmxPulseMXPulseResultsGetTimeSidelobeMainlobeWidthMinimum Method

Gets the minimum mainlobe width across the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobeMainlobeWidthMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetTimeSidelobeMainlobeWidthMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum mainlobe width across the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsTimeSidelobeMainlobeWidthMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/09a06c76-c357-1977-4527-7103f8efd622.htm language=enus -->
## TOPIC 00009: rfmxpulsedotnet/html/09a06c76-c357-1977-4527-7103f8efd622.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/09a06c76-c357-1977-4527-7103f8efd622.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/09a06c76-c357-1977-4527-7103f8efd622.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetStabilityEnabled Method

RFmxPulseMXPulseConfigurationSetStabilityEnabled Method

Sets whether to enable pulse stability results computation.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStabilityEnabled(
	string selectorString,
	RFmxPulseMXPulseStabilityEnabled value
)
```

```text
Public Function SetStabilityEnabled ( 
	selectorString As String,
	value As RFmxPulseMXPulseStabilityEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXPulseStabilityEnabledSpecifies whether to enable pulse stability results computation.

###### Return Value

Int32

##### Remarks

PulseStabilityEnabled

True

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/0c616be5-e276-3c6d-3bbd-6f93f4a4f252.htm language=enus -->
## TOPIC 00010: rfmxpulsedotnet/html/0c616be5-e276-3c6d-3bbd-6f93f4a4f252.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/0c616be5-e276-3c6d-3bbd-6f93f4a4f252.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/0c616be5-e276-3c6d-3bbd-6f93f4a4f252.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFMChirpRate2Mean Method

RFmxPulseMXPulseResultsGetFMChirpRate2Mean Method

Gets the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMChirpRate2Mean(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMChirpRate2Mean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

###### Return Value

Int32

##### Remarks

PulseResultsFMChirpRate2Mean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/0cbccc6b-86db-1ccf-85d6-8272c23103e5.htm language=enus -->
## TOPIC 00011: rfmxpulsedotnet/html/0cbccc6b-86db-1ccf-85d6-8272c23103e5.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/0cbccc6b-86db-1ccf-85d6-8272c23103e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/0cbccc6b-86db-1ccf-85d6-8272c23103e5.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTimeSidelobePeakSidelobeLevelStandardDeviation Method

RFmxPulseMXPulseResultsGetTimeSidelobePeakSidelobeLevelStandardDeviation Method

Gets the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobePeakSidelobeLevelStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetTimeSidelobePeakSidelobeLevelStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsTimeSidelobePeakSidelobeLevelStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/0cee9445-9d1b-085c-ccf1-e24644917eb4.htm language=enus -->
## TOPIC 00012: rfmxpulsedotnet/html/0cee9445-9d1b-085c-ccf1-e24644917eb4.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/0cee9445-9d1b-085c-ccf1-e24644917eb4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/0cee9445-9d1b-085c-ccf1-e24644917eb4.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetIQPowerEdgeTriggerSource Method

RFmxPulseMXSetIQPowerEdgeTriggerSource Method

TriggerType

IQPowerEdge

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerSource(
	string selectorString,
	string value
)
```

```text
Public Function SetIQPowerEdgeTriggerSource ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringSpecifies the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/0e1cc1e6-7687-013e-900c-b55229136e8d.htm language=enus -->
## TOPIC 00013: rfmxpulsedotnet/html/0e1cc1e6-7687-013e-900c-b55229136e8d.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/0e1cc1e6-7687-013e-900c-b55229136e8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/0e1cc1e6-7687-013e-900c-b55229136e8d.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetMeasurementEnabled Method

RFmxPulseMXPulseConfigurationSetMeasurementEnabled Method

Sets whether pulse measurements are enabled..

Namespace:

NationalInstruments.RFmx.PulseMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanSpecifies whether pulse measurements are enabled..

###### Return Value

Int32

##### Remarks

PulseMeasurementEnabled

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/0e9a78f4-d2f3-8518-0177-606ec5720a91.htm language=enus -->
## TOPIC 00014: rfmxpulsedotnet/html/0e9a78f4-d2f3-8518-0177-606ec5720a91.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/0e9a78f4-d2f3-8518-0177-606ec5720a91.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/0e9a78f4-d2f3-8518-0177-606ec5720a91.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPhaseErrorPeakMaximum Method

RFmxPulseMXPulseResultsGetPhaseErrorPeakMaximum Method

Gets the maximum peak phase error across the measured pulses. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseErrorPeakMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseErrorPeakMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum peak phase error across the measured pulses. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PulseResultsPhaseErrorPeakMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/0fa14394-028f-fbca-6471-163b4d59b61b.htm language=enus -->
## TOPIC 00015: rfmxpulsedotnet/html/0fa14394-028f-fbca-6471-163b4d59b61b.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/0fa14394-028f-fbca-6471-163b4d59b61b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/0fa14394-028f-fbca-6471-163b4d59b61b.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAmplitudeStabilityMinimum Method

RFmxPulseMXPulseResultsGetAmplitudeStabilityMinimum Method

Gets the minimum amplitude stability across the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeStabilityMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAmplitudeStabilityMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum amplitude stability across the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsAmplitudeStabilityMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/1019fb9a-ef1e-7c64-2fa6-cc16a0577d16.htm language=enus -->
## TOPIC 00016: rfmxpulsedotnet/html/1019fb9a-ef1e-7c64-2fa6-cc16a0577d16.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/1019fb9a-ef1e-7c64-2fa6-cc16a0577d16.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/1019fb9a-ef1e-7c64-2fa6-cc16a0577d16.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAverageLevelMaximum Method

RFmxPulseMXPulseResultsGetAverageLevelMaximum Method

Gets the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageLevelMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageLevelMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsAverageLevelMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/10c641f5-6c09-e73e-fa1b-0a8b71dde61c.htm language=enus -->
## TOPIC 00017: rfmxpulsedotnet/html/10c641f5-6c09-e73e-fa1b-0a8b71dde61c.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/10c641f5-6c09-e73e-fa1b-0a8b71dde61c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/10c641f5-6c09-e73e-fa1b-0a8b71dde61c.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetMeasurementPointAveragingDuration Method

RFmxPulseMXPulseConfigurationSetMeasurementPointAveragingDuration Method

Sets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementPointAveragingDuration(
	string selectorString,
	double value
)
```

```text
Public Function SetMeasurementPointAveragingDuration ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.

###### Return Value

Int32

##### Remarks

PulseMeasurementPointAveragingDuration

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/12c697e8-5b3c-557c-c48f-29d08cf5b9bf.htm language=enus -->
## TOPIC 00018: rfmxpulsedotnet/html/12c697e8-5b3c-557c-c48f-29d08cf5b9bf.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/12c697e8-5b3c-557c-c48f-29d08cf5b9bf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/12c697e8-5b3c-557c-c48f-29d08cf5b9bf.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTimeSidelobeDelay Method

RFmxPulseMXPulseResultsGetTimeSidelobeDelay Method

Gets the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobeDelay(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetTimeSidelobeDelay ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsTimeSidelobeDelay

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/16361eca-9007-42ea-d68a-75c69d1fc52e.htm language=enus -->
## TOPIC 00019: rfmxpulsedotnet/html/16361eca-9007-42ea-d68a-75c69d1fc52e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/16361eca-9007-42ea-d68a-75c69d1fc52e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/16361eca-9007-42ea-d68a-75c69d1fc52e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.FetchTimeSidelobeTrace Method

RFmxPulseMXPulseResultsFetchTimeSidelobeTrace Method

Fetches the time sidelobe trace for the selected pulse.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchTimeSidelobeTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> timeSidelobe
)
```

```text
Public Function FetchTimeSidelobeTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef timeSidelobe As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1"
- **timeout**
  - Type: SystemDoubleSpecifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **timeSidelobe**
  - Type: NationalInstrumentsAnalogWaveformSingleUpon return, contains the trace of correlated magnitude, in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/167c745c-a871-83e5-827a-90072d638ec2.htm language=enus -->
## TOPIC 00020: rfmxpulsedotnet/html/167c745c-a871-83e5-827a-90072d638ec2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/167c745c-a871-83e5-827a-90072d638ec2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/167c745c-a871-83e5-827a-90072d638ec2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetReferenceLevel Method

RFmxPulseMXSetReferenceLevel Method

Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReferenceLevel(
	string selectorString,
	double value
)
```

```text
Public Function SetReferenceLevel ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

ReferenceLevel

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/16826759-ef57-0719-634e-31686fe9f569.htm language=enus -->
## TOPIC 00021: rfmxpulsedotnet/html/16826759-ef57-0719-634e-31686fe9f569.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/16826759-ef57-0719-634e-31686fe9f569.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/16826759-ef57-0719-634e-31686fe9f569.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.GetTimeSidelobeMinimumCorrelation Method

RFmxPulseMXPulseConfigurationGetTimeSidelobeMinimumCorrelation Method

Gets the minimum peak correlation value for the time sidelobe measurements.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobeMinimumCorrelation(
	string selectorString,
	out double value
)
```

```text
Public Function GetTimeSidelobeMinimumCorrelation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum peak correlation value for the time sidelobe measurements.

###### Return Value

Int32

##### Remarks

PulseTimeSidelobeMinimumCorrelation

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/1a5e3f8c-f9c1-62ba-6455-8e2088fcc621.htm language=enus -->
## TOPIC 00022: rfmxpulsedotnet/html/1a5e3f8c-f9c1-62ba-6455-8e2088fcc621.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/1a5e3f8c-f9c1-62ba-6455-8e2088fcc621.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/1a5e3f8c-f9c1-62ba-6455-8e2088fcc621.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTimeSidelobeCompressionRatioStandardDeviation Method

RFmxPulseMXPulseResultsGetTimeSidelobeCompressionRatioStandardDeviation Method

Gets the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobeCompressionRatioStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetTimeSidelobeCompressionRatioStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

PulseResultsTimeSidelobeCompressionRatioStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/1d5cfed6-4a4c-d766-e914-534aa8eb9d93.htm language=enus -->
## TOPIC 00023: rfmxpulsedotnet/html/1d5cfed6-4a4c-d766-e914-534aa8eb9d93.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/1d5cfed6-4a4c-d766-e914-534aa8eb9d93.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/1d5cfed6-4a4c-d766-e914-534aa8eb9d93.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTimeSidelobeDelayMinimum Method

RFmxPulseMXPulseResultsGetTimeSidelobeDelayMinimum Method

Gets the minimum sidelobe delay across the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimeSidelobeDelayMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetTimeSidelobeDelayMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum sidelobe delay across the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsTimeSidelobeDelayMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/273a6932-096e-a3f0-4a69-e80caa01e4e5.htm language=enus -->
## TOPIC 00024: rfmxpulsedotnet/html/273a6932-096e-a3f0-4a69-e80caa01e4e5.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/273a6932-096e-a3f0-4a69-e80caa01e4e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/273a6932-096e-a3f0-4a69-e80caa01e4e5.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.GetFrequencyAndPhaseDeviationRangeEdgeStart Method

RFmxPulseMXPulseConfigurationGetFrequencyAndPhaseDeviationRangeEdgeStart Method

SetFrequencyAndPhaseDeviationRangeReference(String, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)

Edge

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyAndPhaseDeviationRangeEdgeStart(
	string selectorString,
	out double value
)
```

```text
Public Function GetFrequencyAndPhaseDeviationRangeEdgeStart ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(String, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge.

###### Return Value

Int32

##### Remarks

PulseFrequencyAndPhaseDeviationRangeEdgeStart

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/280b6397-0643-bd47-9109-0c20c3fe8115.htm language=enus -->
## TOPIC 00025: rfmxpulsedotnet/html/280b6397-0643-bd47-9109-0c20c3fe8115.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/280b6397-0643-bd47-9109-0c20c3fe8115.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/280b6397-0643-bd47-9109-0c20c3fe8115.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.PxiTriggerLine3 Field

RFmxPulseMXConstantsPxiTriggerLine3 Field

The signal is exported to the PXI trigger line 3.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine3 = "PXI_Trig3"
```

```text
Public Const PxiTriggerLine3 As String = "PXI_Trig3"
```

###### Field Value

String

##### See Also

###### Reference

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/292cd33b-0b27-819a-fcce-12559504e8f2.htm language=enus -->
## TOPIC 00026: rfmxpulsedotnet/html/292cd33b-0b27-819a-fcce-12559504e8f2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/292cd33b-0b27-819a-fcce-12559504e8f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/292cd33b-0b27-819a-fcce-12559504e8f2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.GetStabilityReferenceOffset Method

RFmxPulseMXPulseConfigurationGetStabilityReferenceOffset Method

Gets the offset in number of pulses used for pulse stability reference computation.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStabilityReferenceOffset(
	string selectorString,
	out int value
)
```

```text
Public Function GetStabilityReferenceOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the offset in number of pulses used for pulse stability reference computation.

###### Return Value

Int32

##### Remarks

PulseStabilityReferenceOffset

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/29544448-986a-013b-c2db-61e583eb62fe.htm language=enus -->
## TOPIC 00027: rfmxpulsedotnet/html/29544448-986a-013b-c2db-61e583eb62fe.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/29544448-986a-013b-c2db-61e583eb62fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/29544448-986a-013b-c2db-61e583eb62fe.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetSegmentAcquisitionLength Method

RFmxPulseMXGetSegmentAcquisitionLength Method

SegmentedAcquisitionEnabled

True

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentAcquisitionLength(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentAcquisitionLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SegmentAcquisitionLength

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/2a816bf4-8489-5608-e162-8d398dd7d6e6.htm language=enus -->
## TOPIC 00028: rfmxpulsedotnet/html/2a816bf4-8489-5608-e162-8d398dd7d6e6.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/2a816bf4-8489-5608-e162-8d398dd7d6e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/2a816bf4-8489-5608-e162-8d398dd7d6e6.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.Dispose Method

RFmxPulseMXDispose Method

Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/2c0fe911-899b-ddff-7af2-8c94d51ce28e.htm language=enus -->
## TOPIC 00029: rfmxpulsedotnet/html/2c0fe911-899b-ddff-7af2-8c94d51ce28e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/2c0fe911-899b-ddff-7af2-8c94d51ce28e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/2c0fe911-899b-ddff-7af2-8c94d51ce28e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseStabilityFrequencyErrorCompensation Enumeration

RFmxPulseMXPulseStabilityFrequencyErrorCompensation Enumeration

Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseStabilityFrequencyErrorCompensation
```

```text
Public Enumeration RFmxPulseMXPulseStabilityFrequencyErrorCompensation
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Off | 0 | Frequency error compensation is disabled. |
|  | On | 1 | Frequency error compensation is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/2caa3643-3665-7599-7874-5dda613a591f.htm language=enus -->
## TOPIC 00030: rfmxpulsedotnet/html/2caa3643-3665-7599-7874-5dda613a591f.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/2caa3643-3665-7599-7874-5dda613a591f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/2caa3643-3665-7599-7874-5dda613a591f.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAveragePhaseMean Method

RFmxPulseMXPulseResultsGetAveragePhaseMean Method

Gets the mean of the average phase across the measured pulses. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragePhaseMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetAveragePhaseMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the average phase across the measured pulses. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PulseResultsAveragePhaseMean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/343f7fb4-0f0d-fd21-123b-80f335368192.htm language=enus -->
## TOPIC 00031: rfmxpulsedotnet/html/343f7fb4-0f0d-fd21-123b-80f335368192.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/343f7fb4-0f0d-fd21-123b-80f335368192.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/343f7fb4-0f0d-fd21-123b-80f335368192.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFrequencyErrorRmsMinimum Method

RFmxPulseMXPulseResultsGetFrequencyErrorRmsMinimum Method

Gets the minimum RMS frequency error across the measured pulses. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyErrorRmsMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetFrequencyErrorRmsMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum RMS frequency error across the measured pulses. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

PulseResultsFrequencyErrorRmsMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/374dfae8-5379-8d4c-cc6e-1acf7382bdce.htm language=enus -->
## TOPIC 00032: rfmxpulsedotnet/html/374dfae8-5379-8d4c-cc6e-1acf7382bdce.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/374dfae8-5379-8d4c-cc6e-1acf7382bdce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/374dfae8-5379-8d4c-cc6e-1acf7382bdce.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.ConfigureSoftwareEdgeTrigger Method

RFmxPulseMXConfigureSoftwareEdgeTrigger Method

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSoftwareEdgeTrigger(
	string selectorString,
	double triggerDelay,
	bool enableTrigger
)
```

```text
Public Function ConfigureSoftwareEdgeTrigger ( 
	selectorString As String,
	triggerDelay As Double,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **triggerDelay**
  - Type: SystemDoubleSpecifies the trigger delay time, in seconds.
- **enableTrigger**
  - Type: SystemBooleanSpecifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/38c4aefb-7f9c-94a8-bc51-5330115b4cd1.htm language=enus -->
## TOPIC 00033: rfmxpulsedotnet/html/38c4aefb-7f9c-94a8-bc51-5330115b4cd1.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/38c4aefb-7f9c-94a8-bc51-5330115b4cd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/38c4aefb-7f9c-94a8-bc51-5330115b4cd1.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetNumberOfSegments Method

RFmxPulseMXSetNumberOfSegments Method

SegmentedAcquisitionEnabled

True

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfSegments(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfSegments ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True.

###### Return Value

Int32

##### Remarks

NumberOfSegments

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/3a440936-1e05-6475-465e-f1d5539c0778.htm language=enus -->
## TOPIC 00034: rfmxpulsedotnet/html/3a440936-1e05-6475-465e-f1d5539c0778.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/3a440936-1e05-6475-465e-f1d5539c0778.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/3a440936-1e05-6475-465e-f1d5539c0778.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXMeasurementFilterType Enumeration

RFmxPulseMXMeasurementFilterType Enumeration

Specifies the demodulation filter type to be used in the measurements.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXMeasurementFilterType
```

```text
Public Enumeration RFmxPulseMXMeasurementFilterType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rectangular | 0 | The Rectangular filter is applied. |
|  | Gaussian | 1 | The Gaussian filter is applied. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/431447d1-5a56-8ae7-326c-81390bd03067.htm language=enus -->
## TOPIC 00035: rfmxpulsedotnet/html/431447d1-5a56-8ae7-326c-81390bd03067.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/431447d1-5a56-8ae7-326c-81390bd03067.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/431447d1-5a56-8ae7-326c-81390bd03067.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAverageLevel Method

RFmxPulseMXPulseResultsGetAverageLevel Method

Gets the average power levels during the pulse period for all measured pulses. The values are expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageLevel(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetAverageLevel ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power levels during the pulse period for all measured pulses. The values are expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsAverageLevel

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/4396fdc4-f6a2-b5a4-ae45-0ba6787e40dd.htm language=enus -->
## TOPIC 00036: rfmxpulsedotnet/html/4396fdc4-f6a2-b5a4-ae45-0ba6787e40dd.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/4396fdc4-f6a2-b5a4-ae45-0ba6787e40dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/4396fdc4-f6a2-b5a4-ae45-0ba6787e40dd.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPhaseDeviationMean Method

RFmxPulseMXPulseResultsGetPhaseDeviationMean Method

Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseDeviationMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseDeviationMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PulseResultsPhaseDeviationMean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/456602a1-54d3-2d83-b892-eb845dc35f4e.htm language=enus -->
## TOPIC 00037: rfmxpulsedotnet/html/456602a1-54d3-2d83-b892-eb845dc35f4e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/456602a1-54d3-2d83-b892-eb845dc35f4e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/456602a1-54d3-2d83-b892-eb845dc35f4e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFrequencyErrorPeakLocation Method

RFmxPulseMXPulseResultsGetFrequencyErrorPeakLocation Method

Gets the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyErrorPeakLocation(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetFrequencyErrorPeakLocation ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsFrequencyErrorPeakLocation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/463c4dfa-7f7e-6bf5-dc4a-56738471e5af.htm language=enus -->
## TOPIC 00038: rfmxpulsedotnet/html/463c4dfa-7f7e-6bf5-dc4a-56738471e5af.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/463c4dfa-7f7e-6bf5-dc4a-56738471e5af.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/463c4dfa-7f7e-6bf5-dc4a-56738471e5af.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.PxieDStarBLine Field

RFmxPulseMXConstantsPxieDStarBLine Field

The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/47b32b11-b54c-2b97-cca1-90ffabec598d.htm language=enus -->
## TOPIC 00039: rfmxpulsedotnet/html/47b32b11-b54c-2b97-cca1-90ffabec598d.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/47b32b11-b54c-2b97-cca1-90ffabec598d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/47b32b11-b54c-2b97-cca1-90ffabec598d.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXSegmentedAcquisitionEnabled Enumeration

RFmxPulseMXSegmentedAcquisitionEnabled Enumeration

Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXSegmentedAcquisitionEnabled
```

```text
Public Enumeration RFmxPulseMXSegmentedAcquisitionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Segmented acquisition is disabled. |
|  | True | 1 | Segmented acquisition is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/499eb561-e21e-6265-4a50-55e135f5962a.htm language=enus -->
## TOPIC 00040: rfmxpulsedotnet/html/499eb561-e21e-6265-4a50-55e135f5962a.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/499eb561-e21e-6265-4a50-55e135f5962a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/499eb561-e21e-6265-4a50-55e135f5962a.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetDroopCompensationEnabled Method

RFmxPulseMXPulseConfigurationSetDroopCompensationEnabled Method

Sets whether to compensate the droop detected in pulse level when applying thresholds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDroopCompensationEnabled(
	string selectorString,
	RFmxPulseMXPulseDroopCompensationEnabled value
)
```

```text
Public Function SetDroopCompensationEnabled ( 
	selectorString As String,
	value As RFmxPulseMXPulseDroopCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXPulseDroopCompensationEnabledSpecifies whether to compensate the droop detected in pulse level when applying thresholds.

###### Return Value

Int32

##### Remarks

PulseDroopCompensationEnabled

False

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/4b824da0-a819-d603-f2f3-d63cba7a8f33.htm language=enus -->
## TOPIC 00041: rfmxpulsedotnet/html/4b824da0-a819-d603-f2f3-d63cba7a8f33.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/4b824da0-a819-d603-f2f3-d63cba7a8f33.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/4b824da0-a819-d603-f2f3-d63cba7a8f33.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetMultiburstEnabled Method

RFmxPulseMXPulseConfigurationSetMultiburstEnabled Method

Sets whether to enable pulse measurements on the multiple burst transmission.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMultiburstEnabled(
	string selectorString,
	RFmxPulseMXMultiburstEnabled value
)
```

```text
Public Function SetMultiburstEnabled ( 
	selectorString As String,
	value As RFmxPulseMXMultiburstEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXMultiburstEnabledSpecifies whether to enable pulse measurements on the multiple burst transmission.

###### Return Value

Int32

##### Remarks

PulseMultiburstEnabled

False

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/4b9b6ec6-cf14-d579-50b3-be9762dfc7f4.htm language=enus -->
## TOPIC 00042: rfmxpulsedotnet/html/4b9b6ec6-cf14-d579-50b3-be9762dfc7f4.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/4b9b6ec6-cf14-d579-50b3-be9762dfc7f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/4b9b6ec6-cf14-d579-50b3-be9762dfc7f4.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAmplitudeStability Method

RFmxPulseMXPulseResultsGetAmplitudeStability Method

Gets the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeStability(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetAmplitudeStability ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference.

###### Return Value

Int32

##### Remarks

PulseResultsAmplitudeStability

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/4f9b7509-2f8b-0739-f56c-43bcd0322b21.htm language=enus -->
## TOPIC 00043: rfmxpulsedotnet/html/4f9b7509-2f8b-0739-f56c-43bcd0322b21.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/4f9b7509-2f8b-0739-f56c-43bcd0322b21.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/4f9b7509-2f8b-0739-f56c-43bcd0322b21.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFrequencyDeviationMinimum Method

RFmxPulseMXPulseResultsGetFrequencyDeviationMinimum Method

Gets the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyDeviationMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetFrequencyDeviationMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

PulseResultsFrequencyDeviationMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/50618f8b-8413-7d7f-0621-1288ebf7bf52.htm language=enus -->
## TOPIC 00044: rfmxpulsedotnet/html/50618f8b-8413-7d7f-0621-1288ebf7bf52.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/50618f8b-8413-7d7f-0621-1288ebf7bf52.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/50618f8b-8413-7d7f-0621-1288ebf7bf52.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.ConfigureRF Method

RFmxPulseMXConfigureRF Method

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRF(
	string selectorString,
	double centerFrequency,
	double referenceLevel,
	double externalAttenuation
)
```

```text
Public Function ConfigureRF ( 
	selectorString As String,
	centerFrequency As Double,
	referenceLevel As Double,
	externalAttenuation As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **centerFrequency**
  - Type: SystemDoubleSpecifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this method is hardware dependent.
- **referenceLevel**
  - Type: SystemDoubleSpecifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this method is hardware dependent.
- **externalAttenuation**
  - Type: SystemDoubleSpecifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/51a9c565-3374-4fd5-c499-1ea001b306df.htm language=enus -->
## TOPIC 00045: rfmxpulsedotnet/html/51a9c565-3374-4fd5-c499-1ea001b306df.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/51a9c565-3374-4fd5-c499-1ea001b306df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/51a9c565-3374-4fd5-c499-1ea001b306df.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseToPulsePhaseDifferenceMinimum Method

RFmxPulseMXPulseResultsGetPulseToPulsePhaseDifferenceMinimum Method

Gets the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseToPulsePhaseDifferenceMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseToPulsePhaseDifferenceMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PulseResultsPulseToPulsePhaseDifferenceMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/51ffbb69-f576-b870-ae0e-76babd3ff7d2.htm language=enus -->
## TOPIC 00046: rfmxpulsedotnet/html/51ffbb69-f576-b870-ae0e-76babd3ff7d2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/51ffbb69-f576-b870-ae0e-76babd3ff7d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/51ffbb69-f576-b870-ae0e-76babd3ff7d2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPeakLevelMinimum Method

RFmxPulseMXPulseResultsGetPeakLevelMinimum Method

Gets the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakLevelMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakLevelMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsPeakLevelMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/537fb741-1349-c0fe-5956-35bd35696f5e.htm language=enus -->
## TOPIC 00047: rfmxpulsedotnet/html/537fb741-1349-c0fe-5956-35bd35696f5e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/537fb741-1349-c0fe-5956-35bd35696f5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/537fb741-1349-c0fe-5956-35bd35696f5e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPhaseErrorPeakLocation Method

RFmxPulseMXPulseResultsGetPhaseErrorPeakLocation Method

Gets the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseErrorPeakLocation(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetPhaseErrorPeakLocation ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsPhaseErrorPeakLocation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/56e07407-c31b-3512-bb01-7554ba93cc6d.htm language=enus -->
## TOPIC 00048: rfmxpulsedotnet/html/56e07407-c31b-3512-bb01-7554ba93cc6d.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/56e07407-c31b-3512-bb01-7554ba93cc6d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/56e07407-c31b-3512-bb01-7554ba93cc6d.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetAttributeInt Method

RFmxPulseMXSetAttributeInt Method

Sets the value of a Int attribute.

Namespace:

NationalInstruments.RFmx.PulseMX

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

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt32Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/56e635c9-9231-f994-16a8-cebe7a660497.htm language=enus -->
## TOPIC 00049: rfmxpulsedotnet/html/56e635c9-9231-f994-16a8-cebe7a660497.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/56e635c9-9231-f994-16a8-cebe7a660497.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/56e635c9-9231-f994-16a8-cebe7a660497.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetErrorString Method

RFmxPulseMXGetErrorString Method

Converts the status code returned by an RFmxPULSE function into a string.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetErrorString(
	int errorCode,
	out string errorDescription
)
```

```text
Public Function GetErrorString ( 
	errorCode As Integer,
	<OutAttribute> ByRef errorDescription As String
) As Integer
```

###### Parameters

- **errorCode**
  - Type: SystemInt32Specifies an error or warning code.
- **errorDescription**
  - Type: SystemStringUpon return, contains the error description.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/578e9557-a81c-fdce-313e-06f8190da241.htm language=enus -->
## TOPIC 00050: rfmxpulsedotnet/html/578e9557-a81c-fdce-313e-06f8190da241.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/578e9557-a81c-fdce-313e-06f8190da241.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/578e9557-a81c-fdce-313e-06f8190da241.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetRipple Method

RFmxPulseMXPulseResultsGetRipple Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRipple(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetRipple ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsRipple

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/58f72cc2-67d4-9448-cd58-3d9d180d2ecc.htm language=enus -->
## TOPIC 00051: rfmxpulsedotnet/html/58f72cc2-67d4-9448-cd58-3d9d180d2ecc.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/58f72cc2-67d4-9448-cd58-3d9d180d2ecc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/58f72cc2-67d4-9448-cd58-3d9d180d2ecc.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFMChirpRateMinimum Method

RFmxPulseMXPulseResultsGetFMChirpRateMinimum Method

Gets the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMChirpRateMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMChirpRateMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

###### Return Value

Int32

##### Remarks

PulseResultsFMChirpRateMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/59320cba-9d18-d1af-7d70-4b027e1d065d.htm language=enus -->
## TOPIC 00052: rfmxpulsedotnet/html/59320cba-9d18-d1af-7d70-4b027e1d065d.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/59320cba-9d18-d1af-7d70-4b027e1d065d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/59320cba-9d18-d1af-7d70-4b027e1d065d.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetIQPowerEdgeTriggerLevelType Method

RFmxPulseMXGetIQPowerEdgeTriggerLevelType Method

IQPowerEdgeTriggerLevel

TriggerType

IQPowerEdge

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerLevelType(
	string selectorString,
	out RFmxPulseMXIQPowerEdgeTriggerLevelType value
)
```

```text
Public Function GetIQPowerEdgeTriggerLevelType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxPulseMXIQPowerEdgeTriggerLevelType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXIQPowerEdgeTriggerLevelTypeUpon return, contains the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevelType

Absolute

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/594ad676-8da4-f494-8058-dc8231561998.htm language=enus -->
## TOPIC 00053: rfmxpulsedotnet/html/594ad676-8da4-f494-8058-dc8231561998.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/594ad676-8da4-f494-8058-dc8231561998.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/594ad676-8da4-f494-8058-dc8231561998.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetRippleMaximum Method

RFmxPulseMXPulseResultsGetRippleMaximum Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRippleMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetRippleMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsRippleMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/59b88a8d-0a07-117d-0dde-0a3262b229a8.htm language=enus -->
## TOPIC 00054: rfmxpulsedotnet/html/59b88a8d-0a07-117d-0dde-0a3262b229a8.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/59b88a8d-0a07-117d-0dde-0a3262b229a8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/59b88a8d-0a07-117d-0dde-0a3262b229a8.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseLevelComputationMethod Enumeration

RFmxPulseMXPulseLevelComputationMethod Enumeration

IEEE Std 181-2011

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseLevelComputationMethod
```

```text
Public Enumeration RFmxPulseMXPulseLevelComputationMethod
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Mean | 0 | The levels derived as the pulse sub-histogram mean levels. |
|  | Median | 1 | The levels derived as the pulse sub-histogram median levels. |
|  | Mode | 2 | The levels derived as the pulse sub-histogram mode levels. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/5f1e54f6-e820-8569-859e-1b87f623c986.htm language=enus -->
## TOPIC 00055: rfmxpulsedotnet/html/5f1e54f6-e820-8569-859e-1b87f623c986.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/5f1e54f6-e820-8569-859e-1b87f623c986.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/5f1e54f6-e820-8569-859e-1b87f623c986.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseRepetitionIntervalStandardDeviation Method

RFmxPulseMXPulseResultsGetPulseRepetitionIntervalStandardDeviation Method

Gets the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseRepetitionIntervalStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseRepetitionIntervalStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsPulseRepetitionIntervalStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/60e449c3-c94c-fdcc-2a69-dd1447c3d8a3.htm language=enus -->
## TOPIC 00056: rfmxpulsedotnet/html/60e449c3-c94c-fdcc-2a69-dd1447c3d8a3.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/60e449c3-c94c-fdcc-2a69-dd1447c3d8a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/60e449c3-c94c-fdcc-2a69-dd1447c3d8a3.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.Pfi0 Field

RFmxPulseMXConstantsPfi0 Field

The signal is exported to the PFI 0.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/611bf097-c10d-b2eb-e716-0272d3970521.htm language=enus -->
## TOPIC 00057: rfmxpulsedotnet/html/611bf097-c10d-b2eb-e716-0272d3970521.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/611bf097-c10d-b2eb-e716-0272d3970521.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/611bf097-c10d-b2eb-e716-0272d3970521.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.PulseMX Namespace

NationalInstruments.RFmx.PulseMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxPulseMX | Defines a root class which is used to identify and control PULSE signal configuration. |
|  | RFmxPulseMXConstants | Specifies constants for I/O terminals. |
|  | RFmxPulseMXPulse | Represents the Pulse measurement. |
|  | RFmxPulseMXPulseConfiguration | Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you. Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. Specifies the time offset in seconds from the reference point to position the trace range. Specifies the length in seconds of the trace range centered at the reference point. Provides methods to configure the Pulse measurement. |
|  | RFmxPulseMXPulseResults | Provides methods to fetch and read the Pulse measurement results. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | RFmxPulseMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
|  | RFmxPulseMXIQPowerEdgeTriggerLevelType | Specifies the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |
|  | RFmxPulseMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |
|  | RFmxPulseMXMaximumPulseCountEnabled | Specifies whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |
|  | RFmxPulseMXMeasurementFilterType | Specifies the demodulation filter type to be used in the measurements. |
|  | RFmxPulseMXMeasurementTypes | Specifies the type of measurement. |
|  | RFmxPulseMXMultiburstEnabled | Specifies whether to enable pulse measurements on the multiple burst transmission. |
|  | RFmxPulseMXPropertyId | Specifies all the attribute identifiers. |
|  | RFmxPulseMXPulseAmplitudeLevelDomain | Specifies whether voltage or power to be used as domain for pulse measurements. |
|  | RFmxPulseMXPulseAmplitudeTraceUnit | Specifies the unit of the amplitude level. This method is applicable only for the amplitude trace. |
|  | RFmxPulseMXPulseCWFrequencyOffsetAuto | Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(String, RFmxPulseMXPulseModulationType) method to CW. |
|  | RFmxPulseMXPulseDetectionReference | Specifies the reference used for SetDetectionThreshold(String, Double) method. |
|  | RFmxPulseMXPulseDroopCompensationEnabled | Specifies whether to compensate the droop detected in pulse level when applying thresholds. |
|  | RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference | Specifies the reference used for the measurement range in phase/frequency deviation and error measurements. |
|  | RFmxPulseMXPulseLevelComputationMethod | Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |
|  | RFmxPulseMXPulseMeasurementPointReference | Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |
|  | RFmxPulseMXPulseMetricsAmplitudeDeviationUnit | Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |
|  | RFmxPulseMXPulseMetricsEnabled | Specifies whether to enable pulse metrics results computation. |
|  | RFmxPulseMXPulseModulationType | Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |
|  | RFmxPulseMXPulseMultipleMeasurementPointsEnabled | Specifies whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |
|  | RFmxPulseMXPulseStabilityEnabled | Specifies whether to enable pulse stability results computation. |
|  | RFmxPulseMXPulseStabilityFrequencyErrorCompensation | Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |
|  | RFmxPulseMXPulseTimeSidelobeEnabled | Specifies whether to enable pulse time sidelobe results computation. |
|  | RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto | Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual. |
|  | RFmxPulseMXPulseTimeSidelobeReferenceWindowType | Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |
|  | RFmxPulseMXPulseTraceRangeAuto | Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you. |
|  | RFmxPulseMXPulseTraceRangeReference | Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |
|  | RFmxPulseMXSegmentedAcquisitionEnabled | Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |
|  | RFmxPulseMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
|  | RFmxPulseMXTriggerType | Specifies the trigger type. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/64725590-23c9-e738-59f6-b88876d6327a.htm language=enus -->
## TOPIC 00058: rfmxpulsedotnet/html/64725590-23c9-e738-59f6-b88876d6327a.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/64725590-23c9-e738-59f6-b88876d6327a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/64725590-23c9-e738-59f6-b88876d6327a.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseOffDurationMaximum Method

RFmxPulseMXPulseResultsGetPulseOffDurationMaximum Method

Gets the maximum OFF duration across the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseOffDurationMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseOffDurationMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum OFF duration across the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsPulseOffDurationMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/651372a7-23e8-818b-34a0-5dab4f897230.htm language=enus -->
## TOPIC 00059: rfmxpulsedotnet/html/651372a7-23e8-818b-34a0-5dab4f897230.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/651372a7-23e8-818b-34a0-5dab4f897230.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/651372a7-23e8-818b-34a0-5dab4f897230.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetFrequencyAndPhaseCWFrequencyOffsetAuto Method

RFmxPulseMXPulseConfigurationSetFrequencyAndPhaseCWFrequencyOffsetAuto Method

SetFrequencyAndPhaseModulationType(String, RFmxPulseMXPulseModulationType)

CW

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyAndPhaseCWFrequencyOffsetAuto(
	string selectorString,
	RFmxPulseMXPulseCWFrequencyOffsetAuto value
)
```

```text
Public Function SetFrequencyAndPhaseCWFrequencyOffsetAuto ( 
	selectorString As String,
	value As RFmxPulseMXPulseCWFrequencyOffsetAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXPulseCWFrequencyOffsetAutoSpecifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(String, RFmxPulseMXPulseModulationType) method to CW.

###### Return Value

Int32

##### Remarks

PulseFrequencyAndPhaseCWFrequencyOffsetAuto

True

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6853682d-a5ab-eea6-c670-8940dc0235e1.htm language=enus -->
## TOPIC 00060: rfmxpulsedotnet/html/6853682d-a5ab-eea6-c670-8940dc0235e1.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6853682d-a5ab-eea6-c670-8940dc0235e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6853682d-a5ab-eea6-c670-8940dc0235e1.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFallTimeMinimum Method

RFmxPulseMXPulseResultsGetFallTimeMinimum Method

Gets the minimum fall time across the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFallTimeMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetFallTimeMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum fall time across the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsFallTimeMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/690eea4d-56c6-fc6c-37e7-2e6c26fe7ea2.htm language=enus -->
## TOPIC 00061: rfmxpulsedotnet/html/690eea4d-56c6-fc6c-37e7-2e6c26fe7ea2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/690eea4d-56c6-fc6c-37e7-2e6c26fe7ea2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/690eea4d-56c6-fc6c-37e7-2e6c26fe7ea2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseCWFrequencyOffsetAuto Enumeration

RFmxPulseMXPulseCWFrequencyOffsetAuto Enumeration

SetFrequencyAndPhaseModulationType(String, RFmxPulseMXPulseModulationType)

CW

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseCWFrequencyOffsetAuto
```

```text
Public Enumeration RFmxPulseMXPulseCWFrequencyOffsetAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | CW frequency offset computation is set to manual. |
|  | True | 1 | CW frequency offset computation is set to automatic. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6a5a3e84-0499-606f-b867-45501d450611.htm language=enus -->
## TOPIC 00062: rfmxpulsedotnet/html/6a5a3e84-0499-606f-b867-45501d450611.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6a5a3e84-0499-606f-b867-45501d450611.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6a5a3e84-0499-606f-b867-45501d450611.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseRepetitionInterval Method

RFmxPulseMXPulseResultsGetPulseRepetitionInterval Method

Gets the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseRepetitionInterval(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetPulseRepetitionInterval ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsPulseRepetitionInterval

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6acd3f50-0566-0859-00c6-9575feda0115.htm language=enus -->
## TOPIC 00063: rfmxpulsedotnet/html/6acd3f50-0566-0859-00c6-9575feda0115.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6acd3f50-0566-0859-00c6-9575feda0115.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6acd3f50-0566-0859-00c6-9575feda0115.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAmplitudeStabilityMaximum Method

RFmxPulseMXPulseResultsGetAmplitudeStabilityMaximum Method

Gets the maximum amplitude stability across the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeStabilityMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAmplitudeStabilityMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum amplitude stability across the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsAmplitudeStabilityMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6c229a8d-cd03-80ec-9781-09da894dc7c4.htm language=enus -->
## TOPIC 00064: rfmxpulsedotnet/html/6c229a8d-cd03-80ec-9781-09da894dc7c4.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6c229a8d-cd03-80ec-9781-09da894dc7c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6c229a8d-cd03-80ec-9781-09da894dc7c4.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulse.Configuration Property

RFmxPulseMXPulseConfiguration Property

RFmxPulseMXPulseConfiguration

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxPulseMXPulseConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxPulseMXPulseConfiguration
	Get
```

###### Property Value

RFmxPulseMXPulseConfiguration

##### See Also

###### Reference

RFmxPulseMXPulse Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6cb0fe36-d5dd-da89-fd76-83926adb9fee.htm language=enus -->
## TOPIC 00065: rfmxpulsedotnet/html/6cb0fe36-d5dd-da89-fd76-83926adb9fee.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6cb0fe36-d5dd-da89-fd76-83926adb9fee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6cb0fe36-d5dd-da89-fd76-83926adb9fee.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPhaseDeviationMaximum Method

RFmxPulseMXPulseResultsGetPhaseDeviationMaximum Method

Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseDeviationMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseDeviationMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PulseResultsPhaseDeviationMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6d715d2d-6069-22a7-388e-f7c68da48a27.htm language=enus -->
## TOPIC 00066: rfmxpulsedotnet/html/6d715d2d-6069-22a7-388e-f7c68da48a27.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6d715d2d-6069-22a7-388e-f7c68da48a27.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6d715d2d-6069-22a7-388e-f7c68da48a27.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetCenterFrequency Method

RFmxPulseMXGetCenterFrequency Method

Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCenterFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetCenterFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### Remarks

CenterFrequency

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6da365ac-100a-faea-b084-60dd29f2f326.htm language=enus -->
## TOPIC 00067: rfmxpulsedotnet/html/6da365ac-100a-faea-b084-60dd29f2f326.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6da365ac-100a-faea-b084-60dd29f2f326.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6da365ac-100a-faea-b084-60dd29f2f326.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseToPulseFrequencyDifferenceStandardDeviation Method

RFmxPulseMXPulseResultsGetPulseToPulseFrequencyDifferenceStandardDeviation Method

Gets the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseToPulseFrequencyDifferenceStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseToPulseFrequencyDifferenceStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

PulseResultsPulseToPulseFrequencyDifferenceStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6ddd03a3-0456-9446-4425-1d43b5baca05.htm language=enus -->
## TOPIC 00068: rfmxpulsedotnet/html/6ddd03a3-0456-9446-4425-1d43b5baca05.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6ddd03a3-0456-9446-4425-1d43b5baca05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6ddd03a3-0456-9446-4425-1d43b5baca05.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseMetricsAmplitudeDeviationUnit Enumeration

RFmxPulseMXPulseMetricsAmplitudeDeviationUnit Enumeration

Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseMetricsAmplitudeDeviationUnit
```

```text
Public Enumeration RFmxPulseMXPulseMetricsAmplitudeDeviationUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Percentage | 0 | Amplitude deviation results are returned as a percentage. |
|  | dB | 1 | Amplitude deviation results are returned in dB. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/6ee3907c-5c26-3e8f-d9a1-c6bbbb376ce4.htm language=enus -->
## TOPIC 00069: rfmxpulsedotnet/html/6ee3907c-5c26-3e8f-d9a1-c6bbbb376ce4.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/6ee3907c-5c26-3e8f-d9a1-c6bbbb376ce4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/6ee3907c-5c26-3e8f-d9a1-c6bbbb376ce4.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.GetFrequencyAndPhaseDeviationRangeLength Method

RFmxPulseMXPulseConfigurationGetFrequencyAndPhaseDeviationRangeLength Method

SetFrequencyAndPhaseDeviationRangeReference(String, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)

Center

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyAndPhaseDeviationRangeLength(
	string selectorString,
	out double value
)
```

```text
Public Function GetFrequencyAndPhaseDeviationRangeLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(String, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center.

###### Return Value

Int32

##### Remarks

PulseFrequencyAndPhaseDeviationRangeLength

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/71c11d12-6f5f-8e76-2389-c0a10688a800.htm language=enus -->
## TOPIC 00070: rfmxpulsedotnet/html/71c11d12-6f5f-8e76-2389-c0a10688a800.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/71c11d12-6f5f-8e76-2389-c0a10688a800.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/71c11d12-6f5f-8e76-2389-c0a10688a800.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetMeasurementBandwidth Method

RFmxPulseMXGetMeasurementBandwidth Method

Gets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeasurementBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the bandwidth of the filter used for the required sample rate. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

MeasurementBandwidth

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/72c344d7-af65-54ff-0869-9407ad5b411f.htm language=enus -->
## TOPIC 00071: rfmxpulsedotnet/html/72c344d7-af65-54ff-0869-9407ad5b411f.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/72c344d7-af65-54ff-0869-9407ad5b411f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/72c344d7-af65-54ff-0869-9407ad5b411f.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetDutyCycle Method

RFmxPulseMXPulseResultsGetDutyCycle Method

Gets the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDutyCycle(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetDutyCycle ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

PulseResultsDutyCycle

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/738bdaf3-b31f-1d18-fded-9700be699211.htm language=enus -->
## TOPIC 00072: rfmxpulsedotnet/html/738bdaf3-b31f-1d18-fded-9700be699211.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/738bdaf3-b31f-1d18-fded-9700be699211.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/738bdaf3-b31f-1d18-fded-9700be699211.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXExtension Methods

RFmxPulseMXExtension Methods

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetPulseSignalConfiguration(RFmxInstrMX) | Creates a new default PULSE signal configuration if it doesn't exist; otherwise, it returns the existing default PULSE signal configuration. |
|  | GetPulseSignalConfiguration(RFmxInstrMX, String) | Creates a PULSE signal configuration for specified signal name. Existing PULSE signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxPulseMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/74863b9b-b429-14aa-0c8c-7bd52e2e63e5.htm language=enus -->
## TOPIC 00073: rfmxpulsedotnet/html/74863b9b-b429-14aa-0c8c-7bd52e2e63e5.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/74863b9b-b429-14aa-0c8c-7bd52e2e63e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/74863b9b-b429-14aa-0c8c-7bd52e2e63e5.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetAttributeBool Method

RFmxPulseMXSetAttributeBool Method

Sets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.PulseMX

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

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemBooleanSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/853c3a70-1858-cabe-d60b-872202547a57.htm language=enus -->
## TOPIC 00074: rfmxpulsedotnet/html/853c3a70-1858-cabe-d60b-872202547a57.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/853c3a70-1858-cabe-d60b-872202547a57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/853c3a70-1858-cabe-d60b-872202547a57.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetFrequencyAndPhaseCWFrequencyOffset Method

RFmxPulseMXPulseConfigurationSetFrequencyAndPhaseCWFrequencyOffset Method

SetFrequencyAndPhaseModulationType(String, RFmxPulseMXPulseModulationType)

CW

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyAndPhaseCWFrequencyOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetFrequencyAndPhaseCWFrequencyOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(String, RFmxPulseMXPulseModulationType) method to CW.

###### Return Value

Int32

##### Remarks

PulseFrequencyAndPhaseCWFrequencyOffset

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/8547daef-8fa6-aad3-5963-db681ac67d20.htm language=enus -->
## TOPIC 00075: rfmxpulsedotnet/html/8547daef-8fa6-aad3-5963-db681ac67d20.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/8547daef-8fa6-aad3-5963-db681ac67d20.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/8547daef-8fa6-aad3-5963-db681ac67d20.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetFrequencyAndPhaseDeviationRangeReference Method

RFmxPulseMXPulseConfigurationSetFrequencyAndPhaseDeviationRangeReference Method

Sets the reference used for the measurement range in phase/frequency deviation and error measurements.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyAndPhaseDeviationRangeReference(
	string selectorString,
	RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference value
)
```

```text
Public Function SetFrequencyAndPhaseDeviationRangeReference ( 
	selectorString As String,
	value As RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReferenceSpecifies the reference used for the measurement range in phase/frequency deviation and error measurements.

###### Return Value

Int32

##### Remarks

PulseFrequencyAndPhaseDeviationRangeReference

Center

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/860d2770-b0d4-6f6f-843a-e7de4313312c.htm language=enus -->
## TOPIC 00076: rfmxpulsedotnet/html/860d2770-b0d4-6f6f-843a-e7de4313312c.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/860d2770-b0d4-6f6f-843a-e7de4313312c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/860d2770-b0d4-6f6f-843a-e7de4313312c.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTopLevel Method

RFmxPulseMXPulseResultsGetTopLevel Method

Gets the top levels for all measured pulses. The values are expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTopLevel(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetTopLevel ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the top levels for all measured pulses. The values are expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsTopLevel

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/8843314a-0830-421f-07f8-915f2f469413.htm language=enus -->
## TOPIC 00077: rfmxpulsedotnet/html/8843314a-0830-421f-07f8-915f2f469413.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/8843314a-0830-421f-07f8-915f2f469413.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/8843314a-0830-421f-07f8-915f2f469413.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFMChirpRateStandardDeviation Method

RFmxPulseMXPulseResultsGetFMChirpRateStandardDeviation Method

Gets the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMChirpRateStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMChirpRateStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

###### Return Value

Int32

##### Remarks

PulseResultsFMChirpRateStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/886552a1-96d8-0d22-c3c3-a286b430160e.htm language=enus -->
## TOPIC 00078: rfmxpulsedotnet/html/886552a1-96d8-0d22-c3c3-a286b430160e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/886552a1-96d8-0d22-c3c3-a286b430160e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/886552a1-96d8-0d22-c3c3-a286b430160e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetDetectionMinimumOffDuration Method

RFmxPulseMXPulseConfigurationSetDetectionMinimumOffDuration Method

Sets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDetectionMinimumOffDuration(
	string selectorString,
	double value
)
```

```text
Public Function SetDetectionMinimumOffDuration ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseDetectionMinimumOffDuration

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/8dee0005-cfb5-99e6-cc55-a4b835989371.htm language=enus -->
## TOPIC 00079: rfmxpulsedotnet/html/8dee0005-cfb5-99e6-cc55-a4b835989371.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/8dee0005-cfb5-99e6-cc55-a4b835989371.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/8dee0005-cfb5-99e6-cc55-a4b835989371.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetDroop Method

RFmxPulseMXPulseResultsGetDroop Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDroop(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetDroop ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsDroop

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/905e45e8-d82e-790d-af24-8735ddf97ee5.htm language=enus -->
## TOPIC 00080: rfmxpulsedotnet/html/905e45e8-d82e-790d-af24-8735ddf97ee5.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/905e45e8-d82e-790d-af24-8735ddf97ee5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/905e45e8-d82e-790d-af24-8735ddf97ee5.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPhaseStabilityMaximum Method

RFmxPulseMXPulseResultsGetPhaseStabilityMaximum Method

Gets the maximum phase stability across the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseStabilityMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseStabilityMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum phase stability across the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsPhaseStabilityMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/90cdbd0c-b7ad-a6df-76f5-a47ea6f49be8.htm language=enus -->
## TOPIC 00081: rfmxpulsedotnet/html/90cdbd0c-b7ad-a6df-76f5-a47ea6f49be8.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/90cdbd0c-b7ad-a6df-76f5-a47ea6f49be8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/90cdbd0c-b7ad-a6df-76f5-a47ea6f49be8.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAverageFrequencyMaximum Method

RFmxPulseMXPulseResultsGetAverageFrequencyMaximum Method

Gets the maximum average frequency across the measured pulses. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageFrequencyMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageFrequencyMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum average frequency across the measured pulses. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

PulseResultsAverageFrequencyMaximum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/925ca1eb-741b-bac4-5d41-4148c15265ef.htm language=enus -->
## TOPIC 00082: rfmxpulsedotnet/html/925ca1eb-741b-bac4-5d41-4148c15265ef.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/925ca1eb-741b-bac4-5d41-4148c15265ef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/925ca1eb-741b-bac4-5d41-4148c15265ef.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetAmplitudeTraceUnit Method

RFmxPulseMXPulseConfigurationSetAmplitudeTraceUnit Method

Sets the unit of the amplitude level. This method is applicable only for the amplitude trace.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAmplitudeTraceUnit(
	string selectorString,
	RFmxPulseMXPulseAmplitudeTraceUnit value
)
```

```text
Public Function SetAmplitudeTraceUnit ( 
	selectorString As String,
	value As RFmxPulseMXPulseAmplitudeTraceUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXPulseAmplitudeTraceUnitSpecifies the unit of the amplitude level. This method is applicable only for the amplitude trace.

###### Return Value

Int32

##### Remarks

PulseAmplitudeTraceUnit

dBm

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/92e8a488-5b4a-7e71-1d9f-05a6fb997767.htm language=enus -->
## TOPIC 00083: rfmxpulsedotnet/html/92e8a488-5b4a-7e71-1d9f-05a6fb997767.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/92e8a488-5b4a-7e71-1d9f-05a6fb997767.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/92e8a488-5b4a-7e71-1d9f-05a6fb997767.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetStabilityPulseToPulseOffset Method

RFmxPulseMXPulseConfigurationSetStabilityPulseToPulseOffset Method

Sets the offset in number of pulses used for pulse-to-pulse stability measurement trace.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStabilityPulseToPulseOffset(
	string selectorString,
	int value
)
```

```text
Public Function SetStabilityPulseToPulseOffset ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the offset in number of pulses used for pulse-to-pulse stability measurement trace.

###### Return Value

Int32

##### Remarks

PulseStabilityPulseToPulseOffset

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9b040fb7-75bf-ac08-f176-314debe843d0.htm language=enus -->
## TOPIC 00084: rfmxpulsedotnet/html/9b040fb7-75bf-ac08-f176-314debe843d0.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9b040fb7-75bf-ac08-f176-314debe843d0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9b040fb7-75bf-ac08-f176-314debe843d0.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetMaximumPulseCount Method

RFmxPulseMXGetMaximumPulseCount Method

MaximumPulseCountEnabled

True

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumPulseCount(
	string selectorString,
	out int value
)
```

```text
Public Function GetMaximumPulseCount ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True.

###### Return Value

Int32

##### Remarks

MaximumPulseCount

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9b488192-a42f-1196-ae74-88c62ebbac8b.htm language=enus -->
## TOPIC 00085: rfmxpulsedotnet/html/9b488192-a42f-1196-ae74-88c62ebbac8b.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9b488192-a42f-1196-ae74-88c62ebbac8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9b488192-a42f-1196-ae74-88c62ebbac8b.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetDroopMean Method

RFmxPulseMXPulseResultsGetDroopMean Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDroopMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetDroopMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsDroopMean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9b74d359-11a2-8552-6f85-1cf5907c8fea.htm language=enus -->
## TOPIC 00086: rfmxpulsedotnet/html/9b74d359-11a2-8552-6f85-1cf5907c8fea.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9b74d359-11a2-8552-6f85-1cf5907c8fea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9b74d359-11a2-8552-6f85-1cf5907c8fea.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.ConfigureDigitalEdgeTrigger Method

RFmxPulseMXConfigureDigitalEdgeTrigger Method

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDigitalEdgeTrigger(
	string selectorString,
	string digitalEdgeTriggerSource,
	RFmxPulseMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge,
	double triggerDelay,
	bool enableTrigger
)
```

```text
Public Function ConfigureDigitalEdgeTrigger ( 
	selectorString As String,
	digitalEdgeTriggerSource As String,
	digitalEdgeTriggerEdge As RFmxPulseMXDigitalEdgeTriggerEdge,
	triggerDelay As Double,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **digitalEdgeTriggerSource**
  - Type: SystemString Specifies the source terminal for the RFmxPulseMXConstants.
- **digitalEdgeTriggerEdge**
  - Type: NationalInstruments.RFmx.PulseMXRFmxPulseMXDigitalEdgeTriggerEdgeSpecifies the trigger edge to detect.
- **triggerDelay**
  - Type: SystemDouble Specifies the trigger delay time. This value is expressed in seconds.
- **enableTrigger**
  - Type: SystemBoolean Specifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9c43a3c4-7134-623f-7e27-3793e5b06dcd.htm language=enus -->
## TOPIC 00087: rfmxpulsedotnet/html/9c43a3c4-7134-623f-7e27-3793e5b06dcd.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9c43a3c4-7134-623f-7e27-3793e5b06dcd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9c43a3c4-7134-623f-7e27-3793e5b06dcd.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetOvershootStandardDeviation Method

RFmxPulseMXPulseResultsGetOvershootStandardDeviation Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOvershootStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetOvershootStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsOvershootStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9ca92ee8-a3d2-8c59-3d69-369bae3b09e4.htm language=enus -->
## TOPIC 00088: rfmxpulsedotnet/html/9ca92ee8-a3d2-8c59-3d69-369bae3b09e4.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9ca92ee8-a3d2-8c59-3d69-369bae3b09e4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9ca92ee8-a3d2-8c59-3d69-369bae3b09e4.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetLowerThresholdLevel Method

RFmxPulseMXPulseConfigurationSetLowerThresholdLevel Method

Sets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLowerThresholdLevel(
	string selectorString,
	double value
)
```

```text
Public Function SetLowerThresholdLevel ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

###### Return Value

Int32

##### Remarks

PulseLowerThresholdLevel

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9e7fbf69-8ae4-3550-e275-f36d25524e58.htm language=enus -->
## TOPIC 00089: rfmxpulsedotnet/html/9e7fbf69-8ae4-3550-e275-f36d25524e58.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9e7fbf69-8ae4-3550-e275-f36d25524e58.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9e7fbf69-8ae4-3550-e275-f36d25524e58.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.SetMultipleMeasurementPointsWindowStepSize Method

RFmxPulseMXPulseConfigurationSetMultipleMeasurementPointsWindowStepSize Method

Sets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMultipleMeasurementPointsWindowStepSize(
	string selectorString,
	double value
)
```

```text
Public Function SetMultipleMeasurementPointsWindowStepSize ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally.

###### Return Value

Int32

##### Remarks

PulseMultipleMeasurementPointsWindowStepSize

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9ef7a22b-5878-16c1-c404-f09857e7a0ab.htm language=enus -->
## TOPIC 00090: rfmxpulsedotnet/html/9ef7a22b-5878-16c1-c404-f09857e7a0ab.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9ef7a22b-5878-16c1-c404-f09857e7a0ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9ef7a22b-5878-16c1-c404-f09857e7a0ab.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX Properties

RFmxPulseMX Properties

The [RFmxPulseMX](dcbec4dc-b667-b630-ece9-b470445bc249.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | Pulse | Gets the RFmxPulseMXPulse instance that represents the Pulse measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxPulseMX. |

Top

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/9f15e1a3-bd5a-612d-a531-555377bb55e4.htm language=enus -->
## TOPIC 00091: rfmxpulsedotnet/html/9f15e1a3-bd5a-612d-a531-555377bb55e4.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/9f15e1a3-bd5a-612d-a531-555377bb55e4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/9f15e1a3-bd5a-612d-a531-555377bb55e4.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetFrequencyErrorPeak Method

RFmxPulseMXPulseResultsGetFrequencyErrorPeak Method

Gets the peak frequency error for all measured pulses. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyErrorPeak(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetFrequencyErrorPeak ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak frequency error for all measured pulses. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

PulseResultsFrequencyErrorPeak

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/a1b5a328-3485-b846-4d4f-06f162b869bc.htm language=enus -->
## TOPIC 00092: rfmxpulsedotnet/html/a1b5a328-3485-b846-4d4f-06f162b869bc.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/a1b5a328-3485-b846-4d4f-06f162b869bc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/a1b5a328-3485-b846-4d4f-06f162b869bc.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetRippleMean Method

RFmxPulseMXPulseResultsGetRippleMean Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRippleMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetRippleMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsRippleMean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/a30e33a5-1750-4b54-9a33-730360e40994.htm language=enus -->
## TOPIC 00093: rfmxpulsedotnet/html/a30e33a5-1750-4b54-9a33-730360e40994.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/a30e33a5-1750-4b54-9a33-730360e40994.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/a30e33a5-1750-4b54-9a33-730360e40994.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SendSoftwareEdgeTrigger Method

RFmxPulseMXSendSoftwareEdgeTrigger Method

ConfigureSoftwareEdgeTrigger(String, Double, Boolean)

- You configure an invalid trigger.
- You have not previously called the Initiate(String, String) method.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SendSoftwareEdgeTrigger()
```

```text
Public Function SendSoftwareEdgeTrigger As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/a4dcbabe-2b0e-98ce-b272-75806a11b217.htm language=enus -->
## TOPIC 00094: rfmxpulsedotnet/html/a4dcbabe-2b0e-98ce-b272-75806a11b217.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/a4dcbabe-2b0e-98ce-b272-75806a11b217.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/a4dcbabe-2b0e-98ce-b272-75806a11b217.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.PxiTriggerLine6 Field

RFmxPulseMXConstantsPxiTriggerLine6 Field

The signal is exported to the PXI trigger line 6.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/a6fc3858-1a88-49fe-f3e0-de6fbe509a4c.htm language=enus -->
## TOPIC 00095: rfmxpulsedotnet/html/a6fc3858-1a88-49fe-f3e0-de6fbe509a4c.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/a6fc3858-1a88-49fe-f3e0-de6fbe509a4c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/a6fc3858-1a88-49fe-f3e0-de6fbe509a4c.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetAttributeIntArray Method

RFmxPulseMXSetAttributeIntArray Method

Set the value of a integer array attribute.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeIntArray(
	string selectorString,
	int attributeIdentifier,
	int[] value
)
```

```text
Public Function SetAttributeIntArray ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Integer()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt32Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/a988de59-670c-b833-f366-9d48253cc222.htm language=enus -->
## TOPIC 00096: rfmxpulsedotnet/html/a988de59-670c-b833-f366-9d48253cc222.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/a988de59-670c-b833-f366-9d48253cc222.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/a988de59-670c-b833-f366-9d48253cc222.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetRippleMinimum Method

RFmxPulseMXPulseResultsGetRippleMinimum Method

SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRippleMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetRippleMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(String, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method.

###### Return Value

Int32

##### Remarks

PulseResultsRippleMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/b64c1880-b719-be5d-9b26-75c26f775410.htm language=enus -->
## TOPIC 00097: rfmxpulsedotnet/html/b64c1880-b719-be5d-9b26-75c26f775410.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/b64c1880-b719-be5d-9b26-75c26f775410.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/b64c1880-b719-be5d-9b26-75c26f775410.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants Fields

RFmxPulseMXConstants Fields

The [RFmxPulseMXConstants](61693e07-044a-1e6e-28dc-7041e2f47082.htm) type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 0. |
|  | Pfi1 | The signal is exported to the PXI 1. |
|  | PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. |
|  | PxiStarLine | The signal is exported to the PXI star trigger line. |
|  | PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
|  | PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
|  | PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
|  | PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
|  | PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
|  | PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
|  | PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
|  | PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
|  | TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665. |

Top

##### See Also

###### Reference

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/bfa0ed73-c845-ff82-ec54-7d9f049204ce.htm language=enus -->
## TOPIC 00098: rfmxpulsedotnet/html/bfa0ed73-c845-ff82-ec54-7d9f049204ce.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/bfa0ed73-c845-ff82-ec54-7d9f049204ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/bfa0ed73-c845-ff82-ec54-7d9f049204ce.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.TimerEvent Field

RFmxPulseMXConstantsTimerEvent Field

The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/c0056d47-0180-8257-a25b-2366967bd22e.htm language=enus -->
## TOPIC 00099: rfmxpulsedotnet/html/c0056d47-0180-8257-a25b-2366967bd22e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/c0056d47-0180-8257-a25b-2366967bd22e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/c0056d47-0180-8257-a25b-2366967bd22e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.PxiStarLine Field

RFmxPulseMXConstantsPxiStarLine Field

The signal is exported to the PXI star trigger line.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/c5229993-4aed-cb41-0bfd-4c51fd0d139e.htm language=enus -->
## TOPIC 00100: rfmxpulsedotnet/html/c5229993-4aed-cb41-0bfd-4c51fd0d139e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/c5229993-4aed-cb41-0bfd-4c51fd0d139e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/c5229993-4aed-cb41-0bfd-4c51fd0d139e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.GetNumberOfAnalysisThreads Method

RFmxPulseMXPulseConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the pulse measurement.

Namespace:

NationalInstruments.RFmx.PulseMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism for the pulse measurement.

###### Return Value

Int32

##### Remarks

PulseNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/c68e0d75-8030-5802-0245-5187a0765627.htm language=enus -->
## TOPIC 00101: rfmxpulsedotnet/html/c68e0d75-8030-5802-0245-5187a0765627.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/c68e0d75-8030-5802-0245-5187a0765627.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/c68e0d75-8030-5802-0245-5187a0765627.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAverageFrequencyMinimum Method

RFmxPulseMXPulseResultsGetAverageFrequencyMinimum Method

Gets the minimum average frequency across the measured pulses. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageFrequencyMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageFrequencyMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum average frequency across the measured pulses. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

PulseResultsAverageFrequencyMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/c7e27e79-a078-2af5-d328-66751cbfe44e.htm language=enus -->
## TOPIC 00102: rfmxpulsedotnet/html/c7e27e79-a078-2af5-d328-66751cbfe44e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/c7e27e79-a078-2af5-d328-66751cbfe44e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/c7e27e79-a078-2af5-d328-66751cbfe44e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetAverageLevelMean Method

RFmxPulseMXPulseResultsGetAverageLevelMean Method

Gets the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageLevelMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageLevelMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsAverageLevelMean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/cc6df9ed-2891-1814-6d4b-43b54f67e156.htm language=enus -->
## TOPIC 00103: rfmxpulsedotnet/html/cc6df9ed-2891-1814-6d4b-43b54f67e156.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/cc6df9ed-2891-1814-6d4b-43b54f67e156.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/cc6df9ed-2891-1814-6d4b-43b54f67e156.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseMeasurementPointReference Enumeration

RFmxPulseMXPulseMeasurementPointReference Enumeration

Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxPulseMXPulseMeasurementPointReference
```

```text
Public Enumeration RFmxPulseMXPulseMeasurementPointReference
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rise | 0 | The measurement point is defined in reference to the rising edge. |
|  | Center | 1 | The measurement point is defined in reference to the center of the pulse. |
|  | Fall | 2 | The measurement point is defined in reference to the falling edge. |

##### See Also

###### Reference

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/cd1bc094-fff1-a544-a1a0-a5f7663f6ff7.htm language=enus -->
## TOPIC 00104: rfmxpulsedotnet/html/cd1bc094-fff1-a544-a1a0-a5f7663f6ff7.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/cd1bc094-fff1-a544-a1a0-a5f7663f6ff7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/cd1bc094-fff1-a544-a1a0-a5f7663f6ff7.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseOffDurationMean Method

RFmxPulseMXPulseResultsGetPulseOffDurationMean Method

Gets the mean of the OFF duration values across the measured pulses. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseOffDurationMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseOffDurationMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean of the OFF duration values across the measured pulses. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseResultsPulseOffDurationMean

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/cfcdaebf-4a6b-27c9-6a58-59fcc2fdff18.htm language=enus -->
## TOPIC 00105: rfmxpulsedotnet/html/cfcdaebf-4a6b-27c9-6a58-59fcc2fdff18.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/cfcdaebf-4a6b-27c9-6a58-59fcc2fdff18.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/cfcdaebf-4a6b-27c9-6a58-59fcc2fdff18.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.PxiTriggerLine1 Field

RFmxPulseMXConstantsPxiTriggerLine1 Field

The signal is exported to the PXI trigger line 1.

Namespace:

NationalInstruments.RFmx.PulseMX

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

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/d956ea8e-4781-4a12-698d-c399172c4eaf.htm language=enus -->
## TOPIC 00106: rfmxpulsedotnet/html/d956ea8e-4781-4a12-698d-c399172c4eaf.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/d956ea8e-4781-4a12-698d-c399172c4eaf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/d956ea8e-4781-4a12-698d-c399172c4eaf.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetWarning Method

RFmxPulseMXGetWarning Method

Gets the latest warning code and description.

Namespace:

NationalInstruments.RFmx.PulseMX

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

- **warningCode**
  - Type: SystemInt32Upon return, contains the latest warning code.
- **warningDescription**
  - Type: SystemStringUpon return, contains the latest warning description.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/e3917932-4d4f-5ef7-24ad-bfd37cd4d460.htm language=enus -->
## TOPIC 00107: rfmxpulsedotnet/html/e3917932-4d4f-5ef7-24ad-bfd37cd4d460.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/e3917932-4d4f-5ef7-24ad-bfd37cd4d460.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/e3917932-4d4f-5ef7-24ad-bfd37cd4d460.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetDutyCycleStandardDeviation Method

RFmxPulseMXPulseResultsGetDutyCycleStandardDeviation Method

Gets the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDutyCycleStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetDutyCycleStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

PulseResultsDutyCycleStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/e66ee343-8f08-f043-f6b0-e00d2b8b3a8c.htm language=enus -->
## TOPIC 00108: rfmxpulsedotnet/html/e66ee343-8f08-f043-f6b0-e00d2b8b3a8c.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/e66ee343-8f08-f043-f6b0-e00d2b8b3a8c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/e66ee343-8f08-f043-f6b0-e00d2b8b3a8c.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPulseToPulsePhaseDifference Method

RFmxPulseMXPulseResultsGetPulseToPulsePhaseDifference Method

Gets the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseToPulsePhaseDifference(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetPulseToPulsePhaseDifference ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PulseResultsPulseToPulsePhaseDifference

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/f73cb5c6-9815-e289-cbd5-e5453f10b61d.htm language=enus -->
## TOPIC 00109: rfmxpulsedotnet/html/f73cb5c6-9815-e289-cbd5-e5453f10b61d.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/f73cb5c6-9815-e289-cbd5-e5453f10b61d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/f73cb5c6-9815-e289-cbd5-e5453f10b61d.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPeakLevel Method

RFmxPulseMXPulseResultsGetPeakLevel Method

Gets the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakLevel(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetPeakLevel ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsPeakLevel

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/f81ea334-225b-5a5a-246e-9e46eb0b0c8d.htm language=enus -->
## TOPIC 00110: rfmxpulsedotnet/html/f81ea334-225b-5a5a-246e-9e46eb0b0c8d.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/f81ea334-225b-5a5a-246e-9e46eb0b0c8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/f81ea334-225b-5a5a-246e-9e46eb0b0c8d.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseConfiguration.GetMultiburstLength Method

RFmxPulseMXPulseConfigurationGetMultiburstLength Method

Gets the number of pulses assigned to a single burst.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMultiburstLength(
	string selectorString,
	out int value
)
```

```text
Public Function GetMultiburstLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the number of pulses assigned to a single burst.

###### Return Value

Int32

##### Remarks

PulseMultiburstLength

##### See Also

###### Reference

RFmxPulseMXPulseConfiguration Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fb5c3d96-e8be-ada4-7e25-b0fce5a71b33.htm language=enus -->
## TOPIC 00111: rfmxpulsedotnet/html/fb5c3d96-e8be-ada4-7e25-b0fce5a71b33.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fb5c3d96-e8be-ada4-7e25-b0fce5a71b33.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fb5c3d96-e8be-ada4-7e25-b0fce5a71b33.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTotalStabilityMinimum Method

RFmxPulseMXPulseResultsGetTotalStabilityMinimum Method

Gets the minimum total stability across the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTotalStabilityMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetTotalStabilityMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum total stability across the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsTotalStabilityMinimum

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fd4509b9-b521-4062-9354-b310643e526f.htm language=enus -->
## TOPIC 00112: rfmxpulsedotnet/html/fd4509b9-b521-4062-9354-b310643e526f.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fd4509b9-b521-4062-9354-b310643e526f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fd4509b9-b521-4062-9354-b310643e526f.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetTotalStability Method

RFmxPulseMXPulseResultsGetTotalStability Method

Gets the total stability of the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTotalStability(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetTotalStability ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the total stability of the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsTotalStability

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fd8ea58d-4b62-9856-4d50-be9c0ac879f9.htm language=enus -->
## TOPIC 00113: rfmxpulsedotnet/html/fd8ea58d-4b62-9856-4d50-be9c0ac879f9.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fd8ea58d-4b62-9856-4d50-be9c0ac879f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fd8ea58d-4b62-9856-4d50-be9c0ac879f9.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.SetMaximumPulseCount Method

RFmxPulseMXSetMaximumPulseCount Method

MaximumPulseCountEnabled

True

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMaximumPulseCount(
	string selectorString,
	int value
)
```

```text
Public Function SetMaximumPulseCount ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True.

###### Return Value

Int32

##### Remarks

MaximumPulseCount

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fda2a1d5-4fe6-27cc-2571-a1d68b80ffc5.htm language=enus -->
## TOPIC 00114: rfmxpulsedotnet/html/fda2a1d5-4fe6-27cc-2571-a1d68b80ffc5.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fda2a1d5-4fe6-27cc-2571-a1d68b80ffc5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fda2a1d5-4fe6-27cc-2571-a1d68b80ffc5.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetBaseLevelStandardDeviation Method

RFmxPulseMXPulseResultsGetBaseLevelStandardDeviation Method

Gets the standard deviation of the base levels across the measured pulses. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBaseLevelStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetBaseLevelStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the standard deviation of the base levels across the measured pulses. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

PulseResultsBaseLevelStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fecce110-8376-1f45-f451-00bdd578e0e2.htm language=enus -->
## TOPIC 00115: rfmxpulsedotnet/html/fecce110-8376-1f45-f451-00bdd578e0e2.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fecce110-8376-1f45-f451-00bdd578e0e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fecce110-8376-1f45-f451-00bdd578e0e2.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXConstants.PxiTriggerLine4 Field

RFmxPulseMXConstantsPxiTriggerLine4 Field

The signal is exported to the PXI trigger line 4.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine4 = "PXI_Trig4"
```

```text
Public Const PxiTriggerLine4 As String = "PXI_Trig4"
```

###### Field Value

String

##### See Also

###### Reference

RFmxPulseMXConstants Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fedf0cde-e096-c763-6d4f-d41face263ab.htm language=enus -->
## TOPIC 00116: rfmxpulsedotnet/html/fedf0cde-e096-c763-6d4f-d41face263ab.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fedf0cde-e096-c763-6d4f-d41face263ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fedf0cde-e096-c763-6d4f-d41face263ab.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMX.GetAttributeInt Method

RFmxPulseMXGetAttributeInt Method

Gets the value of an RFmx 32-bit integer (int32) attribute.

Namespace:

NationalInstruments.RFmx.PulseMX

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

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt32Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxPulseMX Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-pulse-dotnet path=rfmxpulsedotnet/html/fffae704-a00a-f6f9-66d0-5cbb8fc02d1e.htm language=enus -->
## TOPIC 00117: rfmxpulsedotnet/html/fffae704-a00a-f6f9-66d0-5cbb8fc02d1e.htm

- bundle_id: `rfmx-pulse-dotnet`
- source_path: `rfmxpulsedotnet/html/fffae704-a00a-f6f9-66d0-5cbb8fc02d1e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-dotnet/raw/resource/enus/rfmxpulsedotnet/html/fffae704-a00a-f6f9-66d0-5cbb8fc02d1e.htm
- document_id: `rfmx-pulse-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxPulseMXPulseResults.GetPhaseStabilityStandardDeviation Method

RFmxPulseMXPulseResultsGetPhaseStabilityStandardDeviation Method

Gets the phase stability standard deviation across the measured pulses. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.PulseMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseStabilityStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseStabilityStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the phase stability standard deviation across the measured pulses. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PulseResultsPhaseStabilityStandardDeviation

##### See Also

###### Reference

RFmxPulseMXPulseResults Class

NationalInstruments.RFmx.PulseMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
