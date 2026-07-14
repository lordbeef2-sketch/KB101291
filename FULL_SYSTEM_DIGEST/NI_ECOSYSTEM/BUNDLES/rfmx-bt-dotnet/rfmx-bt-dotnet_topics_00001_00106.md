# NI DOCUMENT BUNDLE: rfmx-bt-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-bt-dotnet start=1 end=106 -->
<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/13d9cfe5-01f6-e90d-1647-ccea9134485a.htm language=enus -->
## TOPIC 00001: rfmxbtdotnet/html/13d9cfe5-01f6-e90d-1647-ccea9134485a.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/13d9cfe5-01f6-e90d-1647-ccea9134485a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/13d9cfe5-01f6-e90d-1647-ccea9134485a.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetAverageRmsMagnitudeErrorMean Method

RFmxBTMXModAccResultsGetAverageRmsMagnitudeErrorMean Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageRmsMagnitudeErrorMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageRmsMagnitudeErrorMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsAverageRmsMagnitudeErrorMean

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/14122ece-2cc0-377e-c7ac-a0363226878b.htm language=enus -->
## TOPIC 00002: rfmxbtdotnet/html/14122ece-2cc0-377e-c7ac-a0363226878b.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/14122ece-2cc0-377e-c7ac-a0363226878b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/14122ece-2cc0-377e-c7ac-a0363226878b.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetSelectedPorts Method

RFmxBTMXGetSelectedPorts Method

Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names.

###### Return Value

Int32

##### Remarks

SelectedPorts

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/141ff9f2-ecd9-b698-fd35-2ca3d97971c5.htm language=enus -->
## TOPIC 00003: rfmxbtdotnet/html/141ff9f2-ecd9-b698-fd35-2ca3d97971c5.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/141ff9f2-ecd9-b698-fd35-2ca3d97971c5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/141ff9f2-ecd9-b698-fd35-2ca3d97971c5.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXDigitalEdgeTriggerEdge Enumeration

RFmxBTMXDigitalEdgeTriggerEdge Enumeration

SetTriggerType(String, RFmxBTMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXDigitalEdgeTriggerEdge
```

```text
Public Enumeration RFmxBTMXDigitalEdgeTriggerEdge
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/15871096-1a09-bafe-b0d3-c031c37a2da1.htm language=enus -->
## TOPIC 00004: rfmxbtdotnet/html/15871096-1a09-bafe-b0d3-c031c37a2da1.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/15871096-1a09-bafe-b0d3-c031c37a2da1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/15871096-1a09-bafe-b0d3-c031c37a2da1.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetDirectionFindingMode Method

RFmxBTMXSetDirectionFindingMode Method

Sets the mode of direction finding.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDirectionFindingMode(
	string selectorString,
	RFmxBTMXDirectionFindingMode value
)
```

```text
Public Function SetDirectionFindingMode ( 
	selectorString As String,
	value As RFmxBTMXDirectionFindingMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXDirectionFindingMode**
  - Specifies the mode of direction finding.

###### Return Value

Int32

##### Remarks

DirectionFindingMode

Disabled

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm language=enus -->
## TOPIC 00005: rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeConfiguration.SetAveragingCount Method

RFmxBTMXFrequencyRangeConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

FrequencyRangeAveragingCount

##### See Also

###### Reference

RFmxBTMXFrequencyRangeConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/1d8a9a7e-95ba-4a9a-2ae6-92a2953d7b15.htm language=enus -->
## TOPIC 00006: rfmxbtdotnet/html/1d8a9a7e-95ba-4a9a-2ae6-92a2953d7b15.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/1d8a9a7e-95ba-4a9a-2ae6-92a2953d7b15.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/1d8a9a7e-95ba-4a9a-2ae6-92a2953d7b15.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXExtension Class

RFmxBTMXExtension Class

Provides extension methods to create BT signal configuration. These methods are added to RFmxInstrMX class.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxBTMXExtension
```

```text
<ExtensionAttribute>
Public NotInheritable Class RFmxBTMXExtension
```

The RFmxBTMXExtension type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetBTSignalConfiguration(RFmxInstrMX) | Creates a new default BT signal configuration if it doesn't exist; otherwise, it returns the existing default BT signal configuration. |
|  | GetBTSignalConfiguration(RFmxInstrMX, String) | Creates a BT signal configuration for specified signal name. Existing BT signal configuration is returned if specified signal name exists. |

Top

##### Remarks

For more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/1f8ffe71-0fe2-9ed8-0e7c-acd9078f3ce0.htm language=enus -->
## TOPIC 00007: rfmxbtdotnet/html/1f8ffe71-0fe2-9ed8-0e7c-acd9078f3ce0.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/1f8ffe71-0fe2-9ed8-0e7c-acd9078f3ce0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/1f8ffe71-0fe2-9ed8-0e7c-acd9078f3ce0.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchFrequencyErrorLE Method

RFmxBTMXModAccResultsFetchFrequencyErrorLE Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFrequencyErrorLE(
	string selectorString,
	double timeout,
	out double peakFrequencyErrorMaximum,
	out double initialFrequencyDriftMaximum,
	out double peakFrequencyDriftMaximum,
	out double peakFrequencyDriftRateMaximum
)
```

```text
Public Function FetchFrequencyErrorLE ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef peakFrequencyErrorMaximum As Double,
	<OutAttribute> ByRef initialFrequencyDriftMaximum As Double,
	<OutAttribute> ByRef peakFrequencyDriftMaximum As Double,
	<OutAttribute> ByRef peakFrequencyDriftRateMaximum As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **peakFrequencyErrorMaximum Double**
  - When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to Disabled, it returns the peak frequency error value computed on the preamble and payload portion of the LE packet. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz.
- **initialFrequencyDriftMaximum Double**
  - Upon return, contains the initial frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz.
- **peakFrequencyDriftMaximum Double**
  - Upon return, contains the peak frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz.
- **peakFrequencyDriftRateMaximum Double**
  - Upon return, contains the peak frequency drift rate value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/22030003-cf6f-0a48-d91d-424fc42ed63f.htm language=enus -->
## TOPIC 00008: rfmxbtdotnet/html/22030003-cf6f-0a48-d91d-424fc42ed63f.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/22030003-cf6f-0a48-d91d-424fc42ed63f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/22030003-cf6f-0a48-d91d-424fc42ed63f.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine3 Field

RFmxBTMXConstantsPxiTriggerLine3 Field

The signal is exported to the PXI trigger line 3.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/2257ed3d-cc95-534f-5989-8cd67fb17924.htm language=enus -->
## TOPIC 00009: rfmxbtdotnet/html/2257ed3d-cc95-534f-5989-8cd67fb17924.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/2257ed3d-cc95-534f-5989-8cd67fb17924.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/2257ed3d-cc95-534f-5989-8cd67fb17924.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.SetAveragingEnabled Method

RFmxBTMXTwentydBBandwidthConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for the 20dBBandwidth measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxBTMXTwentydBBandwidthAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxBTMXTwentydBBandwidthAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXTwentydBBandwidthAveragingEnabled**
  - Specifies whether to enable averaging for the 20dBBandwidth measurement.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthAveragingEnabled

False

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/23aa3333-9bea-5645-c7f1-a4d1d5d79e74.htm language=enus -->
## TOPIC 00010: rfmxbtdotnet/html/23aa3333-9bea-5645-c7f1-a4d1d5d79e74.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/23aa3333-9bea-5645-c7f1-a4d1d5d79e74.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/23aa3333-9bea-5645-c7f1-a4d1d5d79e74.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchDf1 Method

RFmxBTMXModAccResultsFetchDf1 Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDf1(
	string selectorString,
	double timeout,
	out double df1avgMaximum,
	out double df1avgMinimum
)
```

```text
Public Function FetchDf1 ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef df1avgMaximum As Double,
	<OutAttribute> ByRef df1avgMinimum As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **df1avgMaximum Double**
  - Upon return, contains the df1avg value computed on the signal. This value is expressed in Hz. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df1avg results computed for each averaging count.
- **df1avgMinimum Double**
  - Upon return, contains the df1avg value computed on the signal. This value is expressed in Hz. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/24de9fcc-905e-b7d2-fa86-d3efddc697d6.htm language=enus -->
## TOPIC 00011: rfmxbtdotnet/html/24de9fcc-905e-b7d2-fa86-d3efddc697d6.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/24de9fcc-905e-b7d2-fa86-d3efddc697d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/24de9fcc-905e-b7d2-fa86-d3efddc697d6.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXPowerRampConfiguration.SetNumberOfAnalysisThreads Method

RFmxBTMXPowerRampConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for PowerRamp measurement.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies the maximum number of threads used for parallelism for PowerRamp measurement.

###### Return Value

Int32

##### Remarks

PowerRampNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxBTMXPowerRampConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm language=enus -->
## TOPIC 00012: rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetCenterFrequency Method

RFmxBTMXSetCenterFrequency Method

Sets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCenterFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetCenterFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### Remarks

CenterFrequency

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/28b34b0a-bfdf-5500-5da0-df02fd613ff3.htm language=enus -->
## TOPIC 00013: rfmxbtdotnet/html/28b34b0a-bfdf-5500-5da0-df02fd613ff3.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/28b34b0a-bfdf-5500-5da0-df02fd613ff3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/28b34b0a-bfdf-5500-5da0-df02fd613ff3.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidth.Results Property

RFmxBTMXTwentydBBandwidthResults Property

RFmxBTMXTwentydBBandwidthResults

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXTwentydBBandwidthResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxBTMXTwentydBBandwidthResults
	Get
```

###### Property Value

RFmxBTMXTwentydBBandwidthResults

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidth Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/2c609219-d0df-ce11-76e5-eeba2c24470f.htm language=enus -->
## TOPIC 00014: rfmxbtdotnet/html/2c609219-d0df-ce11-76e5-eeba2c24470f.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/2c609219-d0df-ce11-76e5-eeba2c24470f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/2c609219-d0df-ce11-76e5-eeba2c24470f.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetRmsDevmMean Method

RFmxBTMXModAccResultsGetRmsDevmMean Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsDevmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsDevmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the RMS differential EVM (DEVM) value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsRmsDevmMean

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/2c76a139-f9eb-0a04-9591-cde92a754430.htm language=enus -->
## TOPIC 00015: rfmxbtdotnet/html/2c76a139-f9eb-0a04-9591-cde92a754430.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/2c76a139-f9eb-0a04-9591-cde92a754430.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/2c76a139-f9eb-0a04-9591-cde92a754430.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SendSoftwareEdgeTrigger Method

RFmxBTMXSendSoftwareEdgeTrigger Method

- You configure an invalid trigger.
- You have not previously called the Initiate(String, String) method.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/2df87ef9-eae7-0986-2dea-33463d13756a.htm language=enus -->
## TOPIC 00016: rfmxbtdotnet/html/2df87ef9-eae7-0986-2dea-33463d13756a.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/2df87ef9-eae7-0986-2dea-33463d13756a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/2df87ef9-eae7-0986-2dea-33463d13756a.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetBRPeakFrequencyDriftRateMaximum Method

RFmxBTMXModAccResultsGetBRPeakFrequencyDriftRateMaximum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBRPeakFrequencyDriftRateMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetBRPeakFrequencyDriftRateMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the peak frequency drift rate value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsBRPeakFrequencyDriftRateMaximum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/2e53d043-32ff-c360-efe6-c2c264eb61b5.htm language=enus -->
## TOPIC 00017: rfmxbtdotnet/html/2e53d043-32ff-c360-efe6-c2c264eb61b5.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/2e53d043-32ff-c360-efe6-c2c264eb61b5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/2e53d043-32ff-c360-efe6-c2c264eb61b5.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetEdrGfskAveragePowerMean Method

RFmxBTMXTxpResultsGetEdrGfskAveragePowerMean Method

Gets the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEdrGfskAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetEdrGfskAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsEdrGfskAveragePowerMean

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/3f81b6bf-292f-529f-83cb-474c47ebfd30.htm language=enus -->
## TOPIC 00018: rfmxbtdotnet/html/3f81b6bf-292f-529f-83cb-474c47ebfd30.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/3f81b6bf-292f-529f-83cb-474c47ebfd30.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/3f81b6bf-292f-529f-83cb-474c47ebfd30.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SignalConfigurationType Property

RFmxBTMXSignalConfigurationType Property

Type

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/40b4c707-b2ee-b24c-85cb-70ee1fab4b05.htm language=enus -->
## TOPIC 00019: rfmxbtdotnet/html/40b4c707-b2ee-b24c-85cb-70ee1fab4b05.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/40b4c707-b2ee-b24c-85cb-70ee1fab4b05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/40b4c707-b2ee-b24c-85cb-70ee1fab4b05.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccConfiguration.GetNumberOfAnalysisThreads Method

RFmxBTMXModAccConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXModAccConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/42f876e7-2c52-4373-b486-95eac93ef1b1.htm language=enus -->
## TOPIC 00020: rfmxbtdotnet/html/42f876e7-2c52-4373-b486-95eac93ef1b1.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/42f876e7-2c52-4373-b486-95eac93ef1b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/42f876e7-2c52-4373-b486-95eac93ef1b1.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumResults Class

RFmxBTMXModSpectrumResults Class

Provides methods to fetch and read the ModSpectrum measurement results.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXModSpectrumResults : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXModSpectrumResults
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXModSpectrumResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchSpectrum | Fetches the ModSpectrum spectrum trace. |
|  | GetBandwidth | Gets the 6 dB bandwidth of the received signal. It is computed as the difference between ModSpectrumResultsHighFrequency and ModSpectrumResultsLowFrequency . This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetHighFrequency | Gets the highest frequency above the center frequency at which the transmit power drops 6dB below the peak power. This value is expressed in Hz. |
|  | GetLowFrequency | Gets the lowest frequency below the center frequency at which the transmit power drops 6 dB below the peak power. This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/4a05584c-86a7-51b0-a79a-fbafd844fa71.htm language=enus -->
## TOPIC 00021: rfmxbtdotnet/html/4a05584c-86a7-51b0-a79a-fbafd844fa71.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/4a05584c-86a7-51b0-a79a-fbafd844fa71.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/4a05584c-86a7-51b0-a79a-fbafd844fa71.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration.GetAllTracesEnabled Method

RFmxBTMXTxpConfigurationGetAllTracesEnabled Method

Gets whether to enable all the traces used for transmit power (TxP) measurements.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains whether to enable all the traces used for transmit power (TxP) measurements.

###### Return Value

Int32

##### Remarks

TxpAllTracesEnabled

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/4a09bbd4-1f36-cbd6-d576-8b277b152ab1.htm language=enus -->
## TOPIC 00022: rfmxbtdotnet/html/4a09bbd4-1f36-cbd6-d576-8b277b152ab1.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/4a09bbd4-1f36-cbd6-d576-8b277b152ab1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/4a09bbd4-1f36-cbd6-d576-8b277b152ab1.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeResults Methods

RFmxBTMXFrequencyRangeResults Methods

The [RFmxBTMXFrequencyRangeResults](b41907f2-4290-5c77-98a0-e4b9943786ad.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchMeasurement | Fetches the FrequencyRange measurement results. |
|  | FetchSpectrum | Fetches the FrequencyRange spectrum trace. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetHighFrequency | Gets the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
|  | GetLowFrequency | Gets the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxBTMXFrequencyRangeResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/4ebcedb7-ef4a-c9e6-90cc-5f72cc35d755.htm language=enus -->
## TOPIC 00023: rfmxbtdotnet/html/4ebcedb7-ef4a-c9e6-90cc-5f72cc35d755.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/4ebcedb7-ef4a-c9e6-90cc-5f72cc35d755.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/4ebcedb7-ef4a-c9e6-90cc-5f72cc35d755.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine1 Field

RFmxBTMXConstantsPxiTriggerLine1 Field

The signal is exported to the PXI trigger line 1.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm language=enus -->
## TOPIC 00024: rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetIQPowerEdgeTriggerSource Method

RFmxBTMXGetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxBTMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/54e3a130-ed66-db5a-d29e-02997bc6f21a.htm language=enus -->
## TOPIC 00025: rfmxbtdotnet/html/54e3a130-ed66-db5a-d29e-02997bc6f21a.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/54e3a130-ed66-db5a-d29e-02997bc6f21a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/54e3a130-ed66-db5a-d29e-02997bc6f21a.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.FetchMeasurementStatus Method

RFmxBTMXAcpResultsFetchMeasurementStatus Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

Symmetric

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurementStatus(
	string selectorString,
	double timeout,
	out RFmxBTMXAcpResultsMeasurementStatus measurementStatus
)
```

```text
Public Function FetchMeasurementStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxBTMXAcpResultsMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus RFmxBTMXAcpResultsMeasurementStatus**
  - Upon return, contains the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. Refer to GetMeasurementStatus(String, RFmxBTMXAcpResultsMeasurementStatus) method for more information about measurement status.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/567f3bc6-59ee-b552-b136-e9704d612045.htm language=enus -->
## TOPIC 00026: rfmxbtdotnet/html/567f3bc6-59ee-b552-b136-e9704d612045.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/567f3bc6-59ee-b552-b136-e9704d612045.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/567f3bc6-59ee-b552-b136-e9704d612045.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrum Methods

RFmxBTMXModSpectrum Methods

The [RFmxBTMXModSpectrum](089ceb93-3542-926c-7a1a-1d5e3b9ddb5a.htm) type exposes the following members.

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

RFmxBTMXModSpectrum Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/585ea64c-fea9-dd19-2599-303187fec79e.htm language=enus -->
## TOPIC 00027: rfmxbtdotnet/html/585ea64c-fea9-dd19-2599-303187fec79e.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/585ea64c-fea9-dd19-2599-303187fec79e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/585ea64c-fea9-dd19-2599-303187fec79e.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumResults Methods

RFmxBTMXModSpectrumResults Methods

The [RFmxBTMXModSpectrumResults](42f876e7-2c52-4373-b486-95eac93ef1b1.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchSpectrum | Fetches the ModSpectrum spectrum trace. |
|  | GetBandwidth | Gets the 6 dB bandwidth of the received signal. It is computed as the difference between ModSpectrumResultsHighFrequency and ModSpectrumResultsLowFrequency . This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetHighFrequency | Gets the highest frequency above the center frequency at which the transmit power drops 6dB below the peak power. This value is expressed in Hz. |
|  | GetLowFrequency | Gets the lowest frequency below the center frequency at which the transmit power drops 6 dB below the peak power. This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxBTMXModSpectrumResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm language=enus -->
## TOPIC 00028: rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthResults.GetBandwidth Method

RFmxBTMXTwentydBBandwidthResultsGetBandwidth Method

Gets the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthResultsBandwidth

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm language=enus -->
## TOPIC 00029: rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXExtension.GetBTSignalConfiguration Method

RFmxBTMXExtensionGetBTSignalConfiguration Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetBTSignalConfiguration(RFmxInstrMX) | Creates a new default BT signal configuration if it doesn't exist; otherwise, it returns the existing default BT signal configuration. |
|  | GetBTSignalConfiguration(RFmxInstrMX, String) | Creates a BT signal configuration for specified signal name. Existing BT signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxBTMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm language=enus -->
## TOPIC 00030: rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.AbortMeasurements Method

RFmxBTMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm language=enus -->
## TOPIC 00031: rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.GetAveragingEnabled Method

RFmxBTMXAcpConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxBTMXAcpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXAcpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXAcpAveragingEnabled**
  - Upon return, contains whether to enable averaging for the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpAveragingEnabled

False

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5b373a64-c831-1067-a37d-35a900257173.htm language=enus -->
## TOPIC 00032: rfmxbtdotnet/html/5b373a64-c831-1067-a37d-35a900257173.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5b373a64-c831-1067-a37d-35a900257173.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5b373a64-c831-1067-a37d-35a900257173.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXPacketType Enumeration

RFmxBTMXPacketType Enumeration

Specifies the type of the Bluetooth packet to be measured.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXPacketType
```

```text
Public Enumeration RFmxBTMXPacketType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| PacketTypeDH1 | 0 | Specifies that the packet type is DH1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.2, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketTypeDH3 | 1 | Specifies that the packet type is DH3. The packet belongs to BR PHY. Refer to Section 6.5.4.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketTypeDH5 | 2 | Specifies that the packet type is DH5. The packet belongs to BR PHY. Refer to Section 6.5.4.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketTypeDM1 | 3 | Specifies that the packet type is DM1. The packet belongs to BR PHY. Refer to Sections 6.5.1.5 and 6.5.4.1, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketTypeDM3 | 4 | Specifies that the packet type is DM3. The packet belongs to BR PHY. Refer to Section 6.5.4.3, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketTypeDM5 | 5 | Specifies that the packet type is DM5. The packet belongs to BR PHY. Refer to Section 6.5.4.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType2DH1 | 6 | Specifies that the packet type is 2-DH1. The packet belongs to EDR PHY. Refer to Section 6.5.4.8, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType2DH3 | 7 | Specifies that the packet type is 2-DH3. The packet belongs to EDR PHY. Refer to Section 6.5.4.9, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType2DH5 | 8 | Specifies that the packet type is 2-DH5. The packet belongs to EDR PHY. Refer to Section 6.5.4.10, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType3DH1 | 9 | Specifies that the packet type is 3-DH1. The packet belongs to EDR PHY. Refer to Section 6.5.4.11, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| Unknown | -1 |  |
| PacketType3DH3 | 10 | Specifies that the packet type is 3-DH3. The packet belongs to EDR PHY. Refer to Section 6.5.4.12, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType3DH5 | 11 | Specifies that the packet type is 3-DH5. The packet belongs to EDR PHY. Refer to Section 6.5.4.13, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType2EV3 | 12 | Specifies that the packet type is 2-EV3. The packet belongs to EDR PHY. Refer to Section 6.5.3.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType2EV5 | 13 | Specifies that the packet type is 2-EV5. The packet belongs to EDR PHY. Refer to Section 6.5.3.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType3EV3 | 14 | Specifies that the packet type is 3-EV3. The packet belongs to EDR PHY. Refer to Section 6.5.3.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketType3EV5 | 15 | Specifies that the packet type is 3-EV5. The packet belongs to EDR PHY. Refer to Section 6.5.3.7, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| PacketTypeLE | 16 | Specifies that the packet belongs to LE PHY. Refer to Section 2.1 and 2.2, Part B, Volume 6 of the Bluetooth Specification v5.1 for more information about this packet. |
| PacketTypeLECS | 17 | Specifies that the packet type is LE-CS. The packet belongs to LE-CS PHY |
| PacketTypeLEHdt | 18 | Specifies that the packet type is LE-HDT. The packet belongs to LE-HDT PHY. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm language=enus -->
## TOPIC 00033: rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ConfigureDataRate Method

RFmxBTMXConfigureDataRate Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDataRate(
	string selectorString,
	int dataRate
)
```

```text
Public Function ConfigureDataRate ( 
	selectorString As String,
	dataRate As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **dataRate Int32**
  - Specifies the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This parameter is applicable to the LE/LE-CS packet types.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5c536354-20fd-e5af-b97e-8bfc089deb7f.htm language=enus -->
## TOPIC 00034: rfmxbtdotnet/html/5c536354-20fd-e5af-b97e-8bfc089deb7f.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5c536354-20fd-e5af-b97e-8bfc089deb7f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5c536354-20fd-e5af-b97e-8bfc089deb7f.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine5 Field

RFmxBTMXConstantsPxiTriggerLine5 Field

The signal is exported to the PXI trigger line 5.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5c84c7e5-6184-2da5-0c25-1fce9f7d4c78.htm language=enus -->
## TOPIC 00035: rfmxbtdotnet/html/5c84c7e5-6184-2da5-0c25-1fce9f7d4c78.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5c84c7e5-6184-2da5-0c25-1fce9f7d4c78.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5c84c7e5-6184-2da5-0c25-1fce9f7d4c78.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchFrequencyErrorEdr Method

RFmxBTMXModAccResultsFetchFrequencyErrorEdr Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFrequencyErrorEdr(
	string selectorString,
	double timeout,
	out double headerFrequencyErrorWiMaximum,
	out double peakFrequencyErrorWiPlusW0Maximum,
	out double peakFrequencyErrorW0Maximum
)
```

```text
Public Function FetchFrequencyErrorEdr ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef headerFrequencyErrorWiMaximum As Double,
	<OutAttribute> ByRef peakFrequencyErrorWiPlusW0Maximum As Double,
	<OutAttribute> ByRef peakFrequencyErrorW0Maximum As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **headerFrequencyErrorWiMaximum Double**
  - Upon return, contains the frequency error value computed on the header of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute header frequency error values computed for each averaging count. This value is expressed in Hz.
- **peakFrequencyErrorWiPlusW0Maximum Double**
  - Upon return, contains the peak frequency error value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz.
- **peakFrequencyErrorW0Maximum Double**
  - Upon return, contains the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5cb3463b-5de4-4d0d-e13b-d3f2c4a1ffb8.htm language=enus -->
## TOPIC 00036: rfmxbtdotnet/html/5cb3463b-5de4-4d0d-e13b-d3f2c4a1ffb8.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5cb3463b-5de4-4d0d-e13b-d3f2c4a1ffb8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5cb3463b-5de4-4d0d-e13b-d3f2c4a1ffb8.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults Class

RFmxBTMXModAccResults Class

Provides methods to fetch and read the ModAcc measurement results.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXModAccResults : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXModAccResults
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXModAccResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchConstellationTrace | Fetches the demodulated symbols from the enhanced data rate (EDR) portion of the EDR packet. This method is valid only for EDR packets. |
|  | FetchCSDetrendedPhaseTrace | Fetches the zero-mean Detrended Phase (deg) versus time trace. This method is valid only for low energy CS (LE-CS) packets. |
|  | FetchCSToneTrace | Fetches the CS Tone Amplitude (dBm) versus time and CS Tone Phase (deg) versus time traces. This method is valid only for low energy CS (LE-CS) packets. |
|  | FetchDemodulatedBitTrace | Fetches the ModAcc demodulated bit trace. |
|  | FetchDevm | Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets. |
|  | FetchDevmMagnitudeError | Fetches ModAcc RMS magnitude error results. These results are valid only for enhanced data rate (EDR) packets. |
|  | FetchDevmPerSymbolTrace | Fetches the DEVM values for symbols from the enhanced data rate (EDR) portion of the EDR packet. This method is valid only for EDR packets. |
|  | FetchDevmPhaseError | Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets. |
|  | FetchDf1 | Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf1maxTrace | Fetches the df1max versus the time trace. This method is applicable only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf2 | Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf2maxTrace | Fetches the df2max versus the time trace. This method is valid only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf4avgTrace | Fetches the df4avg versus the time trace. This function is valid only for LE-CS Packets. |
|  | FetchFrequencyErrorBR | Fetches the ModAcc frequency error trace for basic rate (BR) packets. |
|  | FetchFrequencyErrorEdr | Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets. |
|  | FetchFrequencyErrorLE | Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets. |
|  | FetchFrequencyErrorTraceBR | Fetches the ModAcc frequency error trace for basic rate (BR) packets. |
|  | FetchFrequencyErrorTraceLE | Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets. |
|  | FetchFrequencyErrorWiPlusW0TraceEdr | Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets. |
|  | FetchFrequencyTrace | Fetches the frequency versus time trace. This trace is valid only for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets. |
|  | FetchRmsDevmTrace | Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This method is valid only for enhanced data rate (EDR) packets. |
|  | Get99PercentDevm | Gets the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage. |
|  | GetAverageRmsMagnitudeErrorMean | Gets the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage. |
|  | GetAverageRmsPhaseErrorMean | Return the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
|  | GetBRInitialFrequencyErrorMaximum | Gets the initial frequency error value computed on the preamble portion of the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetBRPeakFrequencyDriftMaximum | Gets the peak frequency drift value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | GetBRPeakFrequencyDriftRateMaximum | Gets the peak frequency drift rate value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
|  | GetClockDriftMean | Gets the clock drift estimated over the LE-CS packet. This value is expressed in ppm. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the clock drift values computed for each averaging count. |
|  | GetDf1avgMaximum | Gets the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf1avgMean | Gets the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df1avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf1avgMinimum | Gets the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf2avgMaximum | Gets the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf2avgMean | Gets the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf2avgMinimum | Gets the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf3avgMean | Gets the df3avg value computed on the signal. When you set the ModAccAveragingEnabled method to True, it returns the mean of the df3avg results computed for each averaging count. This value is expressed in Hz. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
|  | GetEdrHeaderFrequencyErrorWiMaximum | Gets the frequency error value computed on the header of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetEdrPeakFrequencyErrorW0Maximum | Gets the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum absolute of the peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetEdrPeakFrequencyErrorWiPlusW0Maximum | Gets the peak frequency error value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQOriginOffsetMean | Gets the I/Q origin offset estimated over the EDR portion of the EDR packets. This value is expressed in dB. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the I/Q origin offset values computed for each averaging count. |
|  | GetLEInitialFrequencyDriftMaximum | Gets the initial frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEInitialFrequencyErrorMaximum | Gets the initial frequency error value computed on the preamble portion of the LE or LE-CS packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEPeakFrequencyDriftMaximum | Gets the peak frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEPeakFrequencyDriftRateMaximum | Gets the peak frequency drift rate value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEPeakFrequencyErrorMaximum | When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to Disabled, it returns the peak frequency error value computed on the LE/LE-CS packet. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetMinimumDf1maxMinimum | Gets the minimum df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df1max results computed for each averaging count. This value is expressed in Hz. |
|  | GetMinimumDf2maxMinimum | Gets the minimum df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df2max results computed for each averaging count. This value is expressed in Hz. |
|  | GetPeakDevmMaximum | Gets the peak of the differential EVM (DEVM) values computed on symbols in the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of peak symbol differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
|  | GetPeakDf1maxMaximum | Gets the peak df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df1max results computed for each averaging count. This value is expressed in Hz. |
|  | GetPeakDf2maxMaximum | Gets the peak df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df2max results computed for each averaging count. This value is expressed in Hz. |
|  | GetPeakRmsDevmMaximum | Gets the peak of the RMS differential EVM (DEVM) values computed on each 50us block of the EDR portion of the EDR packet. When you set SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns maximum of peak RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
|  | GetPeakRmsMagnitudeErrorMaximum | Gets the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.This value is expressed as a percentage. |
|  | GetPeakRmsPhaseErrorMaximum | Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |
|  | GetPercentageOfSymbolsAboveDf1maxThreshold | Gets the percentage of symbols with df1max values that are greater than the df1max threshold defined by the standard. This result is valid only for the LE packet with a data rate of 125 Kbps. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df1max values from all averaging counts. This value expressed as a percentage. |
|  | GetPercentageOfSymbolsAboveDf2maxThreshold | Gets the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. |
|  | GetPercentageOfSymbolsAboveDf4avgThreshold | Gets the percentage of symbols with df4avg values that are greater than the df4avg threshold defined by the standard. When you set the ModAccAveragingEnabled method to True, it computes this result using the df4avg values from all averaging counts. This value is expressed as a percentage. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
|  | GetPercentageOfSymbolsBelow99PercentDevmLimit | Gets the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification v5.1.0. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the symbol differential EVM (DEVM) values from all averaging counts. This value is expressed as a percentage. |
|  | GetPreambleStartTimeMean | Gets the start time of the preamble of LE-CS packet. This value is expressed in seconds. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the preamble start time values computed for each averaging count. |
|  | GetRmsDevmMean | Gets the RMS differential EVM (DEVM) value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm language=enus -->
## TOPIC 00037: rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetReferenceLevel Method

RFmxBTMXGetReferenceLevel Method

Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReferenceLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetReferenceLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

ReferenceLevel

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm language=enus -->
## TOPIC 00038: rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.ConfigureAveraging Method

RFmxBTMXTwentydBBandwidthConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxBTMXTwentydBBandwidthAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxBTMXTwentydBBandwidthAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxBTMXTwentydBBandwidthAveragingEnabled**
  - Specifies whether to enable averaging for 20dBBandwidth measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/601a9478-76c2-773f-4eaa-c41c80aebfe5.htm language=enus -->
## TOPIC 00039: rfmxbtdotnet/html/601a9478-76c2-773f-4eaa-c41c80aebfe5.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/601a9478-76c2-773f-4eaa-c41c80aebfe5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/601a9478-76c2-773f-4eaa-c41c80aebfe5.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumAveragingEnabled Enumeration

RFmxBTMXModSpectrumAveragingEnabled Enumeration

Specifies whether to enable averaging for ModSpectrum measurements.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXModSpectrumAveragingEnabled
```

```text
Public Enumeration RFmxBTMXModSpectrumAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement uses the ModSpectrumAveragingCount method as the number of acquisitions over which the ModSpectrum measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm language=enus -->
## TOPIC 00040: rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine0 Field

RFmxBTMXConstantsPxiTriggerLine0 Field

The signal is exported to the PXI trigger line 0.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine0 = "PXI_Trig0"
```

```text
Public Const PxiTriggerLine0 As String = "PXI_Trig0"
```

###### Field Value

String

##### See Also

###### Reference

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/613f25ed-e513-fe03-ba97-cf20c71147dc.htm language=enus -->
## TOPIC 00041: rfmxbtdotnet/html/613f25ed-e513-fe03-ba97-cf20c71147dc.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/613f25ed-e513-fe03-ba97-cf20c71147dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/613f25ed-e513-fe03-ba97-cf20c71147dc.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRange.Results Property

RFmxBTMXFrequencyRangeResults Property

RFmxBTMXFrequencyRangeResults

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXFrequencyRangeResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxBTMXFrequencyRangeResults
	Get
```

###### Property Value

RFmxBTMXFrequencyRangeResults

##### See Also

###### Reference

RFmxBTMXFrequencyRange Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/6346800e-0ece-5443-d1db-e9d59279d7d7.htm language=enus -->
## TOPIC 00042: rfmxbtdotnet/html/6346800e-0ece-5443-d1db-e9d59279d7d7.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/6346800e-0ece-5443-d1db-e9d59279d7d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/6346800e-0ece-5443-d1db-e9d59279d7d7.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumConfiguration.ConfigureAveraging Method

RFmxBTMXModSpectrumConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxBTMXModSpectrumAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxBTMXModSpectrumAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxBTMXModSpectrumAveragingEnabled**
  - Specifies whether to enable averaging for the ModSpectrum measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModSpectrumConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/6360e79d-23b8-9f63-f645-53edce99ec77.htm language=enus -->
## TOPIC 00043: rfmxbtdotnet/html/6360e79d-23b8-9f63-f645-53edce99ec77.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/6360e79d-23b8-9f63-f645-53edce99ec77.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/6360e79d-23b8-9f63-f645-53edce99ec77.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration.GetNumberOfAnalysisThreads Method

RFmxBTMXTxpConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

TxpNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/63f20f0a-2bdf-cc51-f878-ffd580e5a04e.htm language=enus -->
## TOPIC 00044: rfmxbtdotnet/html/63f20f0a-2bdf-cc51-f878-ffd580e5a04e.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/63f20f0a-2bdf-cc51-f878-ffd580e5a04e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/63f20f0a-2bdf-cc51-f878-ffd580e5a04e.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumResults.GetLowFrequency Method

RFmxBTMXModSpectrumResultsGetLowFrequency Method

Gets the lowest frequency below the center frequency at which the transmit power drops 6 dB below the peak power. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the lowest frequency below the center frequency at which the transmit power drops 6 dB below the peak power. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModSpectrumResultsLowFrequency

##### See Also

###### Reference

RFmxBTMXModSpectrumResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm language=enus -->
## TOPIC 00045: rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetChannelSoundingSyncSequence Method

RFmxBTMXSetChannelSoundingSyncSequence Method

SetPacketType(String, RFmxBTMXPacketType)

SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChannelSoundingSyncSequence(
	string selectorString,
	RFmxBTMXChannelSoundingSyncSequence value
)
```

```text
Public Function SetChannelSoundingSyncSequence ( 
	selectorString As String,
	value As RFmxBTMXChannelSoundingSyncSequence
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXChannelSoundingSyncSequence**
  - Specifies the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone.

###### Return Value

Int32

##### Remarks

ChannelSoundingSyncSequence

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/66bd52ed-5e4f-15f5-a1c4-a9e621a40c6c.htm language=enus -->
## TOPIC 00046: rfmxbtdotnet/html/66bd52ed-5e4f-15f5-a1c4-a9e621a40c6c.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/66bd52ed-5e4f-15f5-a1c4-a9e621a40c6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/66bd52ed-5e4f-15f5-a1c4-a9e621a40c6c.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.FetchPowers Method

RFmxBTMXTxpResultsFetchPowers Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPowers(
	string selectorString,
	double timeout,
	out double averagePowerMean,
	out double averagePowerMaximum,
	out double averagePowerMinimum,
	out double peakToAveragePowerRatioMaximum
)
```

```text
Public Function FetchPowers ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef averagePowerMean As Double,
	<OutAttribute> ByRef averagePowerMaximum As Double,
	<OutAttribute> ByRef averagePowerMinimum As Double,
	<OutAttribute> ByRef peakToAveragePowerRatioMaximum As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **averagePowerMean Double**
  - Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the SetAveragingEnabled(String, RFmxBTMXTxpAveragingEnabled) method to True, it returns the mean of the average power results computed for each averaging count. This value is expressed in dBm.
- **averagePowerMaximum Double**
  - Upon return, contains the average power computed over the measurement interval. When you set the Direction Finding Mode method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm.
- **averagePowerMinimum Double**
  - Upon return, contains the average power computed over the measurement interval. When you set the Direction Finding Mode method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm.
- **peakToAveragePowerRatioMaximum Double**
  - Upon return, contains the peak to average power ratio computed over the measurement interval. When you set the Direction Finding Mode method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/679ea7f5-67a0-5d96-1200-9883bcbb69af.htm language=enus -->
## TOPIC 00047: rfmxbtdotnet/html/679ea7f5-67a0-5d96-1200-9883bcbb69af.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/679ea7f5-67a0-5d96-1200-9883bcbb69af.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/679ea7f5-67a0-5d96-1200-9883bcbb69af.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetDf2avgMinimum Method

RFmxBTMXModAccResultsGetDf2avgMinimum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDf2avgMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetDf2avgMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsDf2avgMinimum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/691bc1f7-a46b-831e-4572-332697973576.htm language=enus -->
## TOPIC 00048: rfmxbtdotnet/html/691bc1f7-a46b-831e-4572-332697973576.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/691bc1f7-a46b-831e-4572-332697973576.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/691bc1f7-a46b-831e-4572-332697973576.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants Class

RFmxBTMXConstants Class

Specifies constants for I/O terminals.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxBTMXConstants
```

```text
Public NotInheritable Class RFmxBTMXConstants
```

The RFmxBTMXConstants type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 0. |
|  | Pfi1 | The signal is exported to the PXI 1. |
|  | PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. |
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

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/693dabda-d937-f63a-63ca-98a699d249d5.htm language=enus -->
## TOPIC 00049: rfmxbtdotnet/html/693dabda-d937-f63a-63ca-98a699d249d5.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/693dabda-d937-f63a-63ca-98a699d249d5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/693dabda-d937-f63a-63ca-98a699d249d5.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetIQPowerEdgeTriggerLevel Method

RFmxBTMXGetIQPowerEdgeTriggerLevel Method

Gets the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevel

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm language=enus -->
## TOPIC 00050: rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.Commit Method

RFmxBTMXCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int Commit(
	string selectorString
)
```

```text
Public Function Commit ( 
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

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/6b2e74b4-28c2-9c69-1391-3dcbe2d5eb89.htm language=enus -->
## TOPIC 00051: rfmxbtdotnet/html/6b2e74b4-28c2-9c69-1391-3dcbe2d5eb89.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/6b2e74b4-28c2-9c69-1391-3dcbe2d5eb89.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/6b2e74b4-28c2-9c69-1391-3dcbe2d5eb89.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetClockDriftMean Method

RFmxBTMXModAccResultsGetClockDriftMean Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetClockDriftMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetClockDriftMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the clock drift estimated over the LE-CS packet. This value is expressed in ppm. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the clock drift values computed for each averaging count.

###### Return Value

Int32

##### Remarks

ModAccResultsClockDriftMean

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/6ded1d5b-896f-982d-8f1b-d839e31d6f2b.htm language=enus -->
## TOPIC 00052: rfmxbtdotnet/html/6ded1d5b-896f-982d-8f1b-d839e31d6f2b.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/6ded1d5b-896f-982d-8f1b-d839e31d6f2b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/6ded1d5b-896f-982d-8f1b-d839e31d6f2b.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.FetchOffsetMeasurementArray Method

RFmxBTMXAcpResultsFetchOffsetMeasurementArray Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchOffsetMeasurementArray(
	string selectorString,
	double timeout,
	ref double[] lowerAbsolutePower,
	ref double[] upperAbsolutePower,
	ref double[] lowerRelativePower,
	ref double[] upperRelativePower,
	ref double[] lowerMargin,
	ref double[] upperMargin
)
```

```text
Public Function FetchOffsetMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef lowerAbsolutePower As Double(),
	ByRef upperAbsolutePower As Double(),
	ByRef lowerRelativePower As Double(),
	ByRef upperRelativePower As Double(),
	ByRef lowerMargin As Double(),
	ByRef upperMargin As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **lowerAbsolutePower Double**
  - Upon return, contains the array of absolute power measured in the lower offset channel. This value is expressed in dBm.
- **upperAbsolutePower Double**
  - Upon return, contains the array of absolute power measured in the upper offset channel. This value is expressed in dBm.
- **lowerRelativePower Double**
  - Upon return, contains the array of relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB.
- **upperRelativePower Double**
  - Upon return, contains array of the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB.
- **lowerMargin Double**
  - Upon return, contains the array of margin from the limit specified by the mask with Exception for lower offset channel. This value is expressed in dB. Margin is defined as the difference between the Offset Absolute Power and Mask with Exception. This parameter is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This parameter returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric.
- **upperMargin Double**
  - Upon return, contains the array of the margin from the limit specified by the mask with Exception for upper offset channel. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This parameter returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/70611a4a-07a0-9822-6d94-8f76307628f1.htm language=enus -->
## TOPIC 00053: rfmxbtdotnet/html/70611a4a-07a0-9822-6d94-8f76307628f1.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/70611a4a-07a0-9822-6d94-8f76307628f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/70611a4a-07a0-9822-6d94-8f76307628f1.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.SetAllTracesEnabled Method

RFmxBTMXAcpConfigurationSetAllTracesEnabled Method

Sets whether to enable all traces for the adjacent channel power (ACP) measurements.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies whether to enable all traces for the adjacent channel power (ACP) measurements.

###### Return Value

Int32

##### Remarks

AcpAllTracesEnabled

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm language=enus -->
## TOPIC 00054: rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidth Methods

RFmxBTMXTwentydBBandwidth Methods

The [RFmxBTMXTwentydBBandwidth](dcc38597-ee7c-66d2-d0b4-2a13b6dffb51.htm) type exposes the following members.

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

RFmxBTMXTwentydBBandwidth Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm language=enus -->
## TOPIC 00055: rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetAveragePowerMinimum Method

RFmxBTMXTxpResultsGetAveragePowerMinimum Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragePowerMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAveragePowerMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsAveragePowerMinimum

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm language=enus -->
## TOPIC 00056: rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcp Methods

RFmxBTMXAcp Methods

The [RFmxBTMXAcp](4a4c2240-0d07-6aae-387c-51eaa8015704.htm) type exposes the following members.

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

RFmxBTMXAcp Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/73bf35f5-cba5-b83f-b675-df59dd7aa315.htm language=enus -->
## TOPIC 00057: rfmxbtdotnet/html/73bf35f5-cba5-b83f-b675-df59dd7aa315.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/73bf35f5-cba5-b83f-b675-df59dd7aa315.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/73bf35f5-cba5-b83f-b675-df59dd7aa315.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumConfiguration Class

RFmxBTMXModSpectrumConfiguration Class

Provides methods to configure the ModSpectrum measurement.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXModSpectrumConfiguration : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXModSpectrumConfiguration
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXModSpectrumConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the ModSpectrum measurement. |
|  | ConfigureBurstSynchronizationType | Configures the burst synchronization type for ModSpectrum measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable all the traces used for ModSpectrum measurements. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the ModSpectrumAveragingEnabled method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for ModSpectrum measurements. |
|  | GetBurstSynchronizationType | Gets the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the ModSpectrum measurements.This measurement is valid only for channel sounding (CS) packets. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for ModSpectrum measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable all the traces used for ModSpectrum measurements. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the ModSpectrumAveragingEnabled method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for ModSpectrum measurements. |
|  | SetBurstSynchronizationType | Sets the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the ModSpectrum measurements.This measurement is valid only for channel sounding (CS) packets. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for ModSpectrum measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/74c53b07-4e14-2dbe-d1c3-aa3b162879cd.htm language=enus -->
## TOPIC 00058: rfmxbtdotnet/html/74c53b07-4e14-2dbe-d1c3-aa3b162879cd.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/74c53b07-4e14-2dbe-d1c3-aa3b162879cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/74c53b07-4e14-2dbe-d1c3-aa3b162879cd.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetMinimumDf1maxMinimum Method

RFmxBTMXModAccResultsGetMinimumDf1maxMinimum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMinimumDf1maxMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetMinimumDf1maxMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the minimum df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df1max results computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsMinimumDf1maxMinimum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/751cbd20-6328-396c-d970-d2ad45b8eccf.htm language=enus -->
## TOPIC 00059: rfmxbtdotnet/html/751cbd20-6328-396c-d970-d2ad45b8eccf.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/751cbd20-6328-396c-d970-d2ad45b8eccf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/751cbd20-6328-396c-d970-d2ad45b8eccf.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetCteSlotDuration Method

RFmxBTMXGetCteSlotDuration Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfArrival

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCteSlotDuration(
	string selectorString,
	out double value
)
```

```text
Public Function GetCteSlotDuration ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the length of the transmit slots and sampling slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature.

###### Return Value

Int32

##### Remarks

CteSlotDuration

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/7f10a051-d93c-c6b8-d312-9b5a9d08feb5.htm language=enus -->
## TOPIC 00060: rfmxbtdotnet/html/7f10a051-d93c-c6b8-d312-9b5a9d08feb5.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/7f10a051-d93c-c6b8-d312-9b5a9d08feb5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/7f10a051-d93c-c6b8-d312-9b5a9d08feb5.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeConfiguration.SetSpan Method

RFmxBTMXFrequencyRangeConfigurationSetSpan Method

Bluetooth Test Specification v5.1.0

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSpan(
	string selectorString,
	double value
)
```

```text
Public Function SetSpan ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz.

###### Return Value

Int32

##### Remarks

FrequencyRangeSpan

##### See Also

###### Reference

RFmxBTMXFrequencyRangeConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm language=enus -->
## TOPIC 00061: rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.FetchReferenceChannelPower Method

RFmxBTMXAcpResultsFetchReferenceChannelPower Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchReferenceChannelPower(
	string selectorString,
	double timeout,
	out double referenceChannelPower
)
```

```text
Public Function FetchReferenceChannelPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef referenceChannelPower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **referenceChannelPower Double**
  - Upon return, contains the measured power of the reference channel. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/840c6750-8530-4305-333b-546762a5fefd.htm language=enus -->
## TOPIC 00062: rfmxbtdotnet/html/840c6750-8530-4305-333b-546762a5fefd.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/840c6750-8530-4305-333b-546762a5fefd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/840c6750-8530-4305-333b-546762a5fefd.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ResetToDefault Method

RFmxBTMXResetToDefault Method

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/8db0a1bb-d4fe-d9da-1b2c-9cfdc3bff78e.htm language=enus -->
## TOPIC 00063: rfmxbtdotnet/html/8db0a1bb-d4fe-d9da-1b2c-9cfdc3bff78e.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/8db0a1bb-d4fe-d9da-1b2c-9cfdc3bff78e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/8db0a1bb-d4fe-d9da-1b2c-9cfdc3bff78e.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTriggerType Enumeration

RFmxBTMXTriggerType Enumeration

Specifies the type of trigger to be used for signal acquisition.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXTriggerType
```

```text
Public Enumeration RFmxBTMXTriggerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | No reference trigger is used for signal acquisition. |
| DigitalEdge | 1 | A digital-edge trigger is used for signal acquisition. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(String, String) method. |
| IQPowerEdge | 2 | An I/Q power-edge trigger is used for signal acquisition, which is configured using the SetIQPowerEdgeTriggerSlope(String, RFmxBTMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | A software trigger is used for signal acquisition. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/918ede3b-4101-c1b3-7eda-da6563a44809.htm language=enus -->
## TOPIC 00064: rfmxbtdotnet/html/918ede3b-4101-c1b3-7eda-da6563a44809.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/918ede3b-4101-c1b3-7eda-da6563a44809.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/918ede3b-4101-c1b3-7eda-da6563a44809.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.FetchLECteTransmitSlotPowersArray Method

RFmxBTMXTxpResultsFetchLECteTransmitSlotPowersArray Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLECteTransmitSlotPowersArray(
	string selectorString,
	double timeout,
	ref double[] transmitSlotAveragePowerMean,
	ref double[] transmitSlotPeakAbsolutePowerDeviationMaximum
)
```

```text
Public Function FetchLECteTransmitSlotPowersArray ( 
	selectorString As String,
	timeout As Double,
	ByRef transmitSlotAveragePowerMean As Double(),
	ByRef transmitSlotPeakAbsolutePowerDeviationMaximum As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **transmitSlotAveragePowerMean Double**
  - Upon return, contains an array of average powers computed over every transmit slot in CTE portion of the LE packet. When you set the TXP Averaging Enabled method to true, it returns an array of mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm.
- **transmitSlotPeakAbsolutePowerDeviationMaximum Double**
  - Upon return, contains an array of peak absolute power deviations computed over every transmit slot in CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. When you set the TXP Averaging Enabled method to true, it returns an array of maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/933114ad-f7d8-f7c9-d208-f3ead98a371c.htm language=enus -->
## TOPIC 00065: rfmxbtdotnet/html/933114ad-f7d8-f7c9-d208-f3ead98a371c.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/933114ad-f7d8-f7c9-d208-f3ead98a371c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/933114ad-f7d8-f7c9-d208-f3ead98a371c.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetPercentageOfSymbolsAboveDf4avgThreshold Method

RFmxBTMXModAccResultsGetPercentageOfSymbolsAboveDf4avgThreshold Method

ModAccAveragingEnabled

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPercentageOfSymbolsAboveDf4avgThreshold(
	string selectorString,
	out double value
)
```

```text
Public Function GetPercentageOfSymbolsAboveDf4avgThreshold ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the percentage of symbols with df4avg values that are greater than the df4avg threshold defined by the standard. When you set the ModAccAveragingEnabled method to True, it computes this result using the df4avg values from all averaging counts. This value is expressed as a percentage. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2.

###### Return Value

Int32

##### Remarks

ModAccResultsPercentageOfSymbolsAboveDf4avgThreshold

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/936d147c-77bb-4e1e-1924-d4d5acd021e8.htm language=enus -->
## TOPIC 00066: rfmxbtdotnet/html/936d147c-77bb-4e1e-1924-d4d5acd021e8.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/936d147c-77bb-4e1e-1924-d4d5acd021e8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/936d147c-77bb-4e1e-1924-d4d5acd021e8.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.GetNumberOfOffsets Method

RFmxBTMXAcpConfigurationGetNumberOfOffsets Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

Symmetric

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. This method also returns the actual number of offsets used in the ACP measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand.

###### Return Value

Int32

##### Remarks

AcpNumberOfOffsets

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9375d585-2b28-931a-6088-4b9923fa20e1.htm language=enus -->
## TOPIC 00067: rfmxbtdotnet/html/9375d585-2b28-931a-6088-4b9923fa20e1.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9375d585-2b28-931a-6088-4b9923fa20e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9375d585-2b28-931a-6088-4b9923fa20e1.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.SetNumberOfAnalysisThreads Method

RFmxBTMXTwentydBBandwidthConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the 20dB bandwidth measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies the maximum number of threads used for parallelism for the 20dB bandwidth measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/943cfd12-2ea4-52ea-4af5-6a64ccb6047b.htm language=enus -->
## TOPIC 00068: rfmxbtdotnet/html/943cfd12-2ea4-52ea-4af5-6a64ccb6047b.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/943cfd12-2ea4-52ea-4af5-6a64ccb6047b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/943cfd12-2ea4-52ea-4af5-6a64ccb6047b.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine7 Field

RFmxBTMXConstantsPxiTriggerLine7 Field

The signal is exported to the PXI trigger line 7.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/94d7a618-5ff0-4e4b-9643-e23222996ba0.htm language=enus -->
## TOPIC 00069: rfmxbtdotnet/html/94d7a618-5ff0-4e4b-9643-e23222996ba0.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/94d7a618-5ff0-4e4b-9643-e23222996ba0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/94d7a618-5ff0-4e4b-9643-e23222996ba0.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetReferenceLevelHeadroom Method

RFmxBTMXGetReferenceLevelHeadroom Method

SetReferenceLevel(String, Double)

Default values

Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReferenceLevelHeadroom(
	string selectorString,
	out double value
)
```

```text
Public Function GetReferenceLevelHeadroom ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

###### Return Value

Int32

##### Remarks

ReferenceLevelHeadroom

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/94f9600f-7b2d-aa40-9cce-76e6fc2800f6.htm language=enus -->
## TOPIC 00070: rfmxbtdotnet/html/94f9600f-7b2d-aa40-9cce-76e6fc2800f6.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/94f9600f-7b2d-aa40-9cce-76e6fc2800f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/94f9600f-7b2d-aa40-9cce-76e6fc2800f6.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetResultFetchTimeout Method

RFmxBTMXSetResultFetchTimeout Method

Sets the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/970b59ce-5228-196d-5ed4-3e456dae8e23.htm language=enus -->
## TOPIC 00071: rfmxbtdotnet/html/970b59ce-5228-196d-5ed4-3e456dae8e23.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/970b59ce-5228-196d-5ed4-3e456dae8e23.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/970b59ce-5228-196d-5ed4-3e456dae8e23.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.DisableTrigger Method

RFmxBTMXDisableTrigger Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int DisableTrigger(
	string selectorString
)
```

```text
Public Function DisableTrigger ( 
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

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm language=enus -->
## TOPIC 00072: rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.GetAllTracesEnabled Method

RFmxBTMXAcpConfigurationGetAllTracesEnabled Method

Gets whether to enable all traces for the adjacent channel power (ACP) measurements.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains whether to enable all traces for the adjacent channel power (ACP) measurements.

###### Return Value

Int32

##### Remarks

AcpAllTracesEnabled

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/976b03cb-6723-e2b6-8c75-201d7ac4ded4.htm language=enus -->
## TOPIC 00073: rfmxbtdotnet/html/976b03cb-6723-e2b6-8c75-201d7ac4ded4.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/976b03cb-6723-e2b6-8c75-201d7ac4ded4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/976b03cb-6723-e2b6-8c75-201d7ac4ded4.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.GetAveragingCount Method

RFmxBTMXTwentydBBandwidthConfigurationGetAveragingCount Method

TwentydBBandwidthAveragingEnabled

True

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the number of acquisitions used for averaging when you set the TwentydBBandwidthAveragingEnabled method to True.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthAveragingCount

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9784eb57-e8ee-dfe4-deed-e5f63f7d25d8.htm language=enus -->
## TOPIC 00074: rfmxbtdotnet/html/9784eb57-e8ee-dfe4-deed-e5f63f7d25d8.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9784eb57-e8ee-dfe4-deed-e5f63f7d25d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9784eb57-e8ee-dfe4-deed-e5f63f7d25d8.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrum.Configuration Property

RFmxBTMXModSpectrumConfiguration Property

RFmxBTMXModSpectrumConfiguration

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXModSpectrumConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxBTMXModSpectrumConfiguration
	Get
```

###### Property Value

RFmxBTMXModSpectrumConfiguration

##### See Also

###### Reference

RFmxBTMXModSpectrum Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/99f7ba72-5bc3-41da-3b96-af1e61f90c3d.htm language=enus -->
## TOPIC 00075: rfmxbtdotnet/html/99f7ba72-5bc3-41da-3b96-af1e61f90c3d.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/99f7ba72-5bc3-41da-3b96-af1e61f90c3d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/99f7ba72-5bc3-41da-3b96-af1e61f90c3d.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.SetMeasurementEnabled Method

RFmxBTMXTwentydBBandwidthConfigurationSetMeasurementEnabled Method

Bluetooth Test Specification v5.1.0

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies whether to enable the 20dBBandwidth measurement specified in section 4.5.5 of the Bluetooth Test Specification v5.1.0. The measurement uses a span of 3 MHz internally. This measurement is valid only for basic rate (BR) packets.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthMeasurementEnabled

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9a9a2f7e-9350-a1a1-2096-31361febcd60.htm language=enus -->
## TOPIC 00076: rfmxbtdotnet/html/9a9a2f7e-9350-a1a1-2096-31361febcd60.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9a9a2f7e-9350-a1a1-2096-31361febcd60.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9a9a2f7e-9350-a1a1-2096-31361febcd60.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.GetMeasurementStatus Method

RFmxBTMXAcpResultsGetMeasurementStatus Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxBTMXAcpResultsMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXAcpResultsMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value RFmxBTMXAcpResultsMeasurementStatus**
  - Indicates the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand.

###### Return Value

Int32

##### Remarks

AcpResultsMeasurementStatus

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm language=enus -->
## TOPIC 00077: rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetAttributeDouble Method

RFmxBTMXSetAttributeDouble Method

Sets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Double**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm language=enus -->
## TOPIC 00078: rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchFrequencyTrace Method

RFmxBTMXModAccResultsFetchFrequencyTrace Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFrequencyTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> frequency
)
```

```text
Public Function FetchFrequencyTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef frequency As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **frequency AnalogWaveformSingle**
  - Upon return, contains the frequency versus time trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9b8e3739-544d-29ad-dd8d-cae6061ce862.htm language=enus -->
## TOPIC 00079: rfmxbtdotnet/html/9b8e3739-544d-29ad-dd8d-cae6061ce862.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9b8e3739-544d-29ad-dd8d-cae6061ce862.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9b8e3739-544d-29ad-dd8d-cae6061ce862.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiStarLine Field

RFmxBTMXConstantsPxiStarLine Field

The signal is exported to the PXI star trigger line.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9b98ea2a-31a0-67e1-cdac-6b43bcbad02c.htm language=enus -->
## TOPIC 00080: rfmxbtdotnet/html/9b98ea2a-31a0-67e1-cdac-6b43bcbad02c.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9b98ea2a-31a0-67e1-cdac-6b43bcbad02c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9b98ea2a-31a0-67e1-cdac-6b43bcbad02c.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetIQPowerEdgeTriggerLevelType Method

RFmxBTMXSetIQPowerEdgeTriggerLevelType Method

SetIQPowerEdgeTriggerLevel(String, Double)

SetTriggerType(String, RFmxBTMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerLevelType(
	string selectorString,
	RFmxBTMXIQPowerEdgeTriggerLevelType value
)
```

```text
Public Function SetIQPowerEdgeTriggerLevelType ( 
	selectorString As String,
	value As RFmxBTMXIQPowerEdgeTriggerLevelType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXIQPowerEdgeTriggerLevelType**
  - Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevelType

Relative

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm language=enus -->
## TOPIC 00081: rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults Class

RFmxBTMXAcpResults Class

Provides methods to fetch and read the ACP measurement results.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXAcpResults : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXAcpResults
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXAcpResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchAbsolutePowerTrace | Fetches the absolute power trace for ACP measurement. |
|  | FetchMaskTrace | Fetches the limit with exception mask and limit without exception mask traces for ACP measurement. This method returns a valid trace only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | FetchMeasurementStatus | Fetches the overall ACP measurement status based on the measurement limits as defined by the standard if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method is not valid if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. |
|  | FetchOffsetMeasurement | Fetches the absolute powers, relative powers and margins measured in the offset channel. Use "offset(k)" as the selector string to read results from this method. |
|  | FetchOffsetMeasurementArray | Fetches the array of absolute powers, relative powers and margins measured in the offset channels. |
|  | FetchReferenceChannelPower | Returns the measured power of the reference channel. |
|  | FetchSpectrum | Fetches the spectrum used for ACP measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetLowerOffsetAbsolutePower | Gets the absolute power measured in the lower offset channel. This value is expressed in dBm. |
|  | GetLowerOffsetMargin | Gets the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. |
|  | GetLowerOffsetRelativePower | Gets the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | GetMeasurementStatus | Indicates the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | GetReferenceChannelPower | Gets the measured power of the reference channel. This value is expressed in dBm. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetUpperOffsetAbsolutePower | Gets the absolute power measured in the upper offset channel. This value is expressed in dBm. |
|  | GetUpperOffsetMargin | Gets the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. |
|  | GetUpperOffsetRelativePower | Gets the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm language=enus -->
## TOPIC 00082: rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpAveragingEnabled Enumeration

RFmxBTMXAcpAveragingEnabled Enumeration

Specifies whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXAcpAveragingEnabled
```

```text
Public Enumeration RFmxBTMXAcpAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement uses the SetAveragingCount(String, Int32) method as the number of acquisitions over which the ACP measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9c553cf4-fec9-51e2-8496-61401714b788.htm language=enus -->
## TOPIC 00083: rfmxbtdotnet/html/9c553cf4-fec9-51e2-8496-61401714b788.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9c553cf4-fec9-51e2-8496-61401714b788.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9c553cf4-fec9-51e2-8496-61401714b788.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXPropertyId Enumeration

RFmxBTMXPropertyId Enumeration

Specifies all the attribute identifiers.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXPropertyId
```

```text
Public Enumeration RFmxBTMXPropertyId
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| CenterFrequency | 11,534,337 | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| ReferenceLevel | 11,534,338 | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ExternalAttenuation | 11,534,339 | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
| TriggerType | 11,534,340 | Specifies the type of trigger to be used for signal acquisition. |
| DigitalEdgeTriggerSource | 11,534,341 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
| DigitalEdgeTriggerEdge | 11,534,342 | Specifies the active edge for the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
| IQPowerEdgeTriggerSource | 11,534,343 | Specifies the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerLevel | 11,534,344 | Specifies the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. |
| IQPowerEdgeTriggerSlope | 11,534,345 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
| TriggerDelay | 11,534,346 | Specifies the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
| TriggerMinimumQuietTimeMode | 11,534,347 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 11,534,348 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| PacketType | 11,534,349 | Specifies the type of the Bluetooth packet to be measured. |
| DataRate | 11,534,350 | Specifies the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types. |
| BDAddressLap | 11,534,351 | Specifies the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |
| AccessAddress | 11,534,353 | Specifies the 32-bit LE access address. |
| PayloadBitPattern | 11,534,354 | Specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. Refer to the Payload Bit Pattern property that lists the measurements that are applicable for different payload bit patterns. |
| PayloadLengthMode | 11,534,355 | Specifies the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(String, Int32) properties decide the length of the payload to be used for measurement. |
| PayloadLength | 11,534,356 | Specifies the payload length of the signal in bytes. This method is applicable only when you set the SetPayloadLengthMode(String, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length used for measurement if you set the Payload Length Mode method to Auto. |
| ChannelNumber | 11,534,359 | Specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
| DetectedPacketType | 11,534,361 | Returns the packet type detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| DetectedDataRate | 11,534,378 | Returns the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| DetectedPayloadLength | 11,534,379 | Returns the payload length detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| DirectionFindingMode | 11,534,380 | Specifies the mode of direction finding. |
| CteLength | 11,534,381 | Specifies the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |
| CteSlotDuration | 11,534,382 | Specifies the length of the transmit slots and sampling slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
| CteNumberOfTransmitSlots | 11,534,383 | Returns the number of transmit slots in the constant time extension portion of the generated LE packet. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
| ChannelSoundingPacketFormat | 11,534,384 | Specifies the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS. |
| ChannelSoundingSyncSequence | 11,534,385 | Specifies the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
| ChannelSoundingPhaseMeasurementPeriod | 11,534,386 | Specifies the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
| ChannelSoundingToneExtensionSlot | 11,534,387 | Specifies whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
| BandwidthBitPeriodProduct | 11,534,388 | Specifies the bandwidth bit period product of GFSK modulation for LE-CS packet type. |
| ChannelSoundingAntennaSwitchTime | 11,534,389 | Specifies the Channel Sounding Antenna Switch Time for the LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
| ChannelSoundingNumberOfAntennaPath | 11,534,390 | Specifies the number of antenna paths for the generated LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
| ReferenceLevelHeadroom | 11,538,428 | Specifies the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| SelectedPorts | 11,538,429 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| IQPowerEdgeTriggerLevelType | 11,538,431 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
| TxpMeasurementEnabled | 11,538,432 | Specifies whether to enable the transmit power (TxP) measurements. |
| TxpAveragingEnabled | 11,538,434 | Specifies whether to enable averaging for the transmit power (TxP) measurements. |
| TxpAveragingCount | 11,538,435 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXTxpAveragingEnabled) method to True. |
| TxpAllTracesEnabled | 11,538,436 | Specifies whether to enable all the traces used for transmit power (TxP) measurements. |
| TxpNumberOfAnalysisThreads | 11,538,437 | Specifies the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| TxpResultsAveragePowerMean | 11,538,439 | Returns the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count. |
| TxpResultsAveragePowerMaximum | 11,538,440 | Returns the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsAveragePowerMinimum | 11,538,441 | Returns the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsPeakPowerMaximum | 11,538,442 | Returns the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsPeakToAveragePowerRatioMaximum | 11,538,443 | Returns the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |
| TxpResultsEdrGfskAveragePowerMean | 11,538,444 | Returns the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsEdrDpskAveragePowerMean | 11,538,445 | Returns the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
| TxpBurstSynchronizationType | 11,538,448 | Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
| TxpResultsEdrDpskGfskAveragePowerRatioMean | 11,538,451 | Returns the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |
| TxpResultsLECteReferencePeriodAveragePowerMean | 11,538,452 | Returns the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsLECteReferencePeriodPeakAbsolutePowerDeviationMaximum | 11,538,453 | Returns the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
| TxpResultsLECteTransmitSlotAveragePowerMean | 11,538,454 | Returns the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsLECteTransmitSlotPeakAbsolutePowerDeviationMaximum | 11,538,455 | Returns the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
| TxpResultsLECSPhaseMeasurementPeriodAveragePowerMean | 11,538,456 | Returns the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. When you set the TxpAveragingEnabled method to True, it returns the mean of the phase measurement period average power results computed for each averaging count. This value is expressed in dBm. |
| TwentydBBandwidthMeasurementEnabled | 11,542,528 | Specifies whether to enable the 20dBBandwidth measurement specified in section 4.5.5 of the Bluetooth Test Specification v5.1.0. The measurement uses a span of 3 MHz internally. This measurement is valid only for basic rate (BR) packets. |
| TwentydBBandwidthAveragingEnabled | 11,542,530 | Specifies whether to enable averaging for the 20dBBandwidth measurement. |
| TwentydBBandwidthAveragingCount | 11,542,531 | Specifies the number of acquisitions used for averaging when you set the TwentydBBandwidthAveragingEnabled method to True. |
| TwentydBBandwidthAllTracesEnabled | 11,542,532 | Specifies whether to enable all the traces for the 20dBBandwidth measurement. |
| TwentydBBandwidthNumberOfAnalysisThreads | 11,542,533 | Specifies the maximum number of threads used for parallelism for the 20dB bandwidth measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| TwentydBBandwidthResultsPeakPower | 11,542,535 | Returns the peak power of the measured spectrum. This value is expressed in dBm. |
| TwentydBBandwidthResultsBandwidth | 11,542,536 | Returns the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz. |
| TwentydBBandwidthResultsHighFrequency | 11,542,537 | Returns the highest frequency above the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
| TwentydBBandwidthResultsLowFrequency | 11,542,538 | Returns the lowest frequency below the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
| FrequencyRangeMeasurementEnabled | 11,546,624 | Specifies whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification v5.1.0. This measurement is valid only for basic rate (BR) packets. |
| FrequencyRangeSpan | 11,546,626 | Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |
| FrequencyRangeAveragingEnabled | 11,546,627 | Specifies whether to enable averaging for the FrequencyRange measurement. |
| FrequencyRangeAveragingCount | 11,546,628 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |
| FrequencyRangeAllTracesEnabled | 11,546,629 | Specifies whether to enable all the traces for FrequencyRange measurement. |
| FrequencyRangeNumberOfAnalysisThreads | 11,546,630 | Specifies the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| FrequencyRangeResultsHighFrequency | 11,546,632 | Returns the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
| FrequencyRangeResultsLowFrequency | 11,546,633 | Returns the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
| ModAccMeasurementEnabled | 11,550,720 | Specifies whether to enable the ModAcc measurements. You can use this method to determine the modulation quality of the bluetooth transmitter. |
| ModAccIQOriginOffsetCorrectionEnabled | 11,550,723 | Specifies whether to enable the I/Q origin offset correction for EDR packets. If you set this method to True, the DEVM results are computed after correcting for the I/Q origin offset. |
| ModAccAveragingEnabled | 11,550,724 | Specifies whether to enable averaging for the ModAcc measurements. |
| ModAccAveragingCount | 11,550,725 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True. |
| ModAccAllTracesEnabled | 11,550,726 | Specifies whether to enable all the traces computed by ModAcc measurements. |
| ModAccNumberOfAnalysisThreads | 11,550,727 | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| ModAccResultsDf1avgMean | 11,550,729 | Returns the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df1avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf1avgMaximum | 11,550,730 | Returns the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf1avgMinimum | 11,550,731 | Returns the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPeakDf1maxMaximum | 11,550,732 | Returns the peak df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df1max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsMinimumDf1maxMinimum | 11,550,733 | Returns the minimum df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df1max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf2avgMean | 11,550,734 | Returns the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf2avgMaximum | 11,550,735 | Returns the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf2avgMinimum | 11,550,736 | Returns the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPeakDf2maxMaximum | 11,550,737 | Returns the peak df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df2max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsMinimumDf2maxMinimum | 11,550,738 | Returns the minimum df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df2max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPercentageOfSymbolsAboveDf2maxThreshold | 11,550,739 | Returns the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. |
| ModAccResultsBRInitialFrequencyErrorMaximum | 11,550,740 | Returns the initial frequency error value computed on the preamble portion of the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsBRPeakFrequencyDriftMaximum | 11,550,741 | Returns the peak frequency drift value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsBRPeakFrequencyDriftRateMaximum | 11,550,742 | Returns the peak frequency drift rate value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsEdrHeaderFrequencyErrorWiMaximum | 11,550,743 | Returns the frequency error value computed on the header of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsEdrPeakFrequencyErrorWiPlusW0Maximum | 11,550,744 | Returns the peak frequency error value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsEdrPeakFrequencyErrorW0Maximum | 11,550,745 | Returns the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum absolute of the peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEPeakFrequencyErrorMaximum | 11,550,746 | When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to Disabled, it returns the peak frequency error value computed on the LE/LE-CS packet. When you set the Direction Finding Mode method to AngleOfArrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute the peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEInitialFrequencyDriftMaximum | 11,550,747 | Returns the initial frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEPeakFrequencyDriftMaximum | 11,550,748 | Returns the peak frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEPeakFrequencyDriftRateMaximum | 11,550,749 | Returns the peak frequency drift rate value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPeakRmsDevmMaximum | 11,550,750 | Returns the peak of the RMS differential EVM (DEVM) values computed on each 50us block of the EDR portion of the EDR packet. When you set SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the aboslute peak RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
| ModAccResultsRmsDevmMean | 11,550,751 | Returns the RMS differential EVM (DEVM) value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the absolute mean of the RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
| ModAccResultsPeakDevmMaximum | 11,550,752 | Returns the peak of the differential EVM (DEVM) values computed on symbols in the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak symbol differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
| ModAccResults99PercentDevm | 11,550,753 | Returns the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage. |
| ModAccResultsPercentageOfSymbolsBelow99PercentDevmLimit | 11,550,754 | Returns the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification v5.1.0.. This value is expressed as a percentage. |
| ModAccResultsIQOriginOffsetMean | 11,550,755 | Returns the I/Q origin offset estimated over the EDR portion of the EDR packets. This value is expressed in dB. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the I/Q origin offset values computed for each averaging count. |
| ModAccBurstSynchronizationType | 11,550,763 | Specifies the type of synchronization used for detecting the start of packet in ModAcc measurement. |
| ModAccResultsPercentageOfSymbolsAboveDf1maxThreshold | 11,550,764 | Returns the percentage of symbols with df1max values that are greater than the df1max threshold defined by the standard. This result is valid only for the LE packet with a data rate of 125 Kbps. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df1max values from all averaging counts. This value expressed as a percentage. |
| ModAccResultsAverageRmsMagnitudeErrorMean | 11,550,765 | Returns the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage. |
| ModAccResultsPeakRmsMagnitudeErrorMaximum | 11,550,766 | Returns the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.This value is expressed as a percentage. |
| ModAccResultsAverageRmsPhaseErrorMean | 11,550,767 | Return the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
| ModAccResultsPeakRmsPhaseErrorMaximum | 11,550,768 | Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |
| ModAccResultsLEInitialFrequencyErrorMaximum | 11,550,769 | Returns the initial frequency error value computed on the preamble portion of the LE or LE-CS packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsClockDriftMean | 11,550,770 | Returns the clock drift estimated over the LE-CS packet. This value is expressed in ppm. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the clock drift values computed for each averaging count. |
| ModAccResultsPreambleStartTimeMean | 11,550,771 | Returns the start time of the preamble of LE-CS packet. This value is expressed in seconds. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the preamble start time values computed for each averaging count. |
| ModAccResultsDf3avgMean | 11,550,772 | Returns the df3avg value computed on the signal. When you set the ModAccAveragingEnabled method to True, it returns the mean of the df3avg results computed for each averaging count. This value is expressed in Hz. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
| ModAccResultsPercentageOfSymbolsAboveDf4avgThreshold | 11,550,773 | Returns the percentage of symbols with df4avg values that are greater than the df4avg threshold defined by the standard. When you set the ModAccAveragingEnabled method to True, it computes this result using the df4avg values from all averaging counts. This value is expressed as a percentage. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
| AcpMeasurementEnabled | 11,554,816 | Specifies whether to enable the ACP measurement. |
| AcpOffsetChannelMode | 11,554,818 | Specifies which offset channels are used for the measurement. |
| AcpNumberOfOffsets | 11,554,819 | Specifies the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. This method also returns the actual number of offsets used in the ACP measurement when you set the ACP Offset Channel Mode method to InBand. |
| AcpOffsetFrequency | 11,554,820 | Returns the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz. |
| AcpAveragingEnabled | 11,554,821 | Specifies whether to enable averaging for the ACP measurement. |
| AcpAveragingCount | 11,554,822 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXAcpAveragingEnabled) method to True. |
| AcpAllTracesEnabled | 11,554,823 | Specifies whether to enable all traces for the adjacent channel power (ACP) measurements. |
| AcpNumberOfAnalysisThreads | 11,554,824 | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
| AcpResultsMeasurementStatus | 11,554,826 | Indicates the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
| AcpResultsReferenceChannelPower | 11,554,827 | Returns the measured power of the reference channel. This value is expressed in dBm. |
| AcpResultsLowerOffsetAbsolutePower | 11,554,828 | Returns the absolute power measured in the lower offset channel. This value is expressed in dBm. |
| AcpResultsLowerOffsetRelativePower | 11,554,829 | Returns the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| AcpResultsLowerOffsetMargin | 11,554,830 | Returns the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the ACP Offset Channel Mode method to Symmetric. |
| AcpResultsUpperOffsetAbsolutePower | 11,554,831 | Returns the absolute power measured in the upper offset channel. This value is expressed in dBm. |
| AcpResultsUpperOffsetRelativePower | 11,554,832 | Returns the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| AcpResultsUpperOffsetMargin | 11,554,833 | Returns the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the ACP Offset Channel Mode method to Symmetric. |
| AcpBurstSynchronizationType | 11,554,834 | Specifies the type of synchronization used for detecting the start of the EDR packet in the adjacent channel power (ACP) measurement. |
| ResultFetchTimeout | 11,583,488 | Specifies the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete. |
| LimitedConfigurationChange | 11,587,584 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
| AutoLevelInitialReferenceLevel | 11,587,585 | Specifies the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| PowerRampMeasurementEnabled | 11,591,680 | Specifies whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. |
| PowerRampBurstSynchronizationType | 11,591,682 | Specifies the type of synchronization used for detecting the start of packet in the PowerRamp measurement. |
| PowerRampAveragingEnabled | 11,591,685 | Specifies whether to enable averaging for PowerRamp measurement. |
| PowerRampAveragingCount | 11,591,686 | Specifies the number of acquisitions used for averaging when you set the PowerRampAveragingEnabled method to True. |
| PowerRampNumberOfAnalysisThreads | 11,591,687 | Specifies the maximum number of threads used for parallelism for PowerRamp measurement. |
| PowerRampResultsRiseTimeMean | 11,591,689 | Rise Time returns the rise time of the acquired signal that is the amount of time taken for the power envelope to rise from a level of 10 percent to 90 percent. When you set the PowerRampAveragingEnabled method to True, this parameter returns the mean of the rise time computed for each averaging count. This value is expressed in seconds. |
| PowerRampResultsFallTimeMean | 11,591,690 | Fall Time returns the fall time of the acquired signal that is the amount of time taken for the power envelope to fall from a level of 90 percent to 10 percent. When you set the PowerRampAveragingEnabled method to True,this parameter returns the mean of the fall time computed for each averaging countt. This value is expressed in seconds. |
| PowerRampResults40dBFallTimeMean | 11,591,691 | 40dB Fall Time returns the fall time of the acquired signal at which transmit power drops 40 dB below average power. When you set the PowerRampAveragingEnabled method to True, this parameter returns the mean of the 40dB fall time computed for each averaging count. This value is expressed in seconds. |
| ModSpectrumMeasurementEnabled | 11,595,776 | Specifies whether to enable the ModSpectrum measurements.This measurement is valid only for channel sounding (CS) packets. |
| ModSpectrumBurstSynchronizationType | 11,595,778 | Specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. |
| ModSpectrumAveragingEnabled | 11,595,779 | Specifies whether to enable averaging for ModSpectrum measurements. |
| ModSpectrumAveragingCount | 11,595,780 | Specifies the number of acquisitions used for averaging when you set the ModSpectrumAveragingEnabled method to True. |
| ModSpectrumAllTracesEnabled | 11,595,781 | Specifies whether to enable all the traces used for ModSpectrum measurements. |
| ModSpectrumNumberOfAnalysisThreads | 11,595,782 | Specifies the maximum number of threads used for parallelism for ModSpectrum measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| ModSpectrumResultsBandwidth | 11,595,784 | Returns the 6 dB bandwidth of the received signal. It is computed as the difference between ModSpectrumResultsHighFrequency and ModSpectrumResultsLowFrequency . This value is expressed in Hz. |
| ModSpectrumResultsHighFrequency | 11,595,785 | Returns the highest frequency above the center frequency at which the transmit power drops 6dB below the peak power. This value is expressed in Hz. |
| ModSpectrumResultsLowFrequency | 11,595,786 | Returns the lowest frequency below the center frequency at which the transmit power drops 6 dB below the peak power. This value is expressed in Hz. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/9f9b010d-46a7-7228-5d5f-9279f8b77f3f.htm language=enus -->
## TOPIC 00084: rfmxbtdotnet/html/9f9b010d-46a7-7228-5d5f-9279f8b77f3f.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/9f9b010d-46a7-7228-5d5f-9279f8b77f3f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/9f9b010d-46a7-7228-5d5f-9279f8b77f3f.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.WaitForMeasurementComplete Method

RFmxBTMXWaitForMeasurementComplete Method

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm language=enus -->
## TOPIC 00085: rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine2 Field

RFmxBTMXConstantsPxiTriggerLine2 Field

The signal is exported to the PXI trigger line 2.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine2 = "PXI_Trig2"
```

```text
Public Const PxiTriggerLine2 As String = "PXI_Trig2"
```

###### Field Value

String

##### See Also

###### Reference

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm language=enus -->
## TOPIC 00086: rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetLECteReferencePeriodAveragePowerMean Method

RFmxBTMXTxpResultsGetLECteReferencePeriodAveragePowerMean Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLECteReferencePeriodAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetLECteReferencePeriodAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsLECteReferencePeriodAveragePowerMean

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm language=enus -->
## TOPIC 00087: rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.Txp Property

RFmxBTMXTxp Property

RFmxBTMXTxp

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXTxp Txp { get; }
```

```text
Public ReadOnly Property Txp As RFmxBTMXTxp
	Get
```

###### Property Value

RFmxBTMXTxp

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm language=enus -->
## TOPIC 00088: rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetAccessAddress Method

RFmxBTMXSetAccessAddress Method

Sets the 32-bit LE access address.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAccessAddress(
	string selectorString,
	int value
)
```

```text
Public Function SetAccessAddress ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the 32-bit LE access address.

###### Return Value

Int32

##### Remarks

AccessAddress

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm language=enus -->
## TOPIC 00089: rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeConfiguration Class

RFmxBTMXFrequencyRangeConfiguration Class

Provides methods to configure the FrequencyRange measurement.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXFrequencyRangeConfiguration : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXFrequencyRangeConfiguration
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXFrequencyRangeConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the FrequencyRange measurement. |
|  | ConfigureSpan | Configures the span for the FrequencyRange measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable all the traces for FrequencyRange measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the FrequencyRange measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification v5.1.0. This measurement is valid only for basic rate (BR) packets. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetSpan | Gets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable all the traces for FrequencyRange measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the FrequencyRange measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification v5.1.0. This measurement is valid only for basic rate (BR) packets. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetSpan | Sets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm language=enus -->
## TOPIC 00090: rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.GetUpperOffsetAbsolutePower Method

RFmxBTMXAcpResultsGetUpperOffsetAbsolutePower Method

Gets the absolute power measured in the upper offset channel. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the absolute power measured in the upper offset channel. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AcpResultsUpperOffsetAbsolutePower

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/b50dece9-36ac-8468-8983-84a519d9c0a9.htm language=enus -->
## TOPIC 00091: rfmxbtdotnet/html/b50dece9-36ac-8468-8983-84a519d9c0a9.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/b50dece9-36ac-8468-8983-84a519d9c0a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/b50dece9-36ac-8468-8983-84a519d9c0a9.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.AnalyzeIQ1Waveform Method

RFmxBTMXAnalyzeIQ1Waveform Method

IQ

IQ

IQorSpectral

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int AnalyzeIQ1Waveform(
	string selectorString,
	string resultName,
	ComplexWaveform<ComplexSingle> iq,
	bool reset,
	long reserved
)
```

```text
Public Function AnalyzeIQ1Waveform ( 
	selectorString As String,
	resultName As String,
	iq As ComplexWaveform(Of ComplexSingle),
	reset As Boolean,
	reserved As Long
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **resultName String**
  - Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1"
- **iq ComplexWaveformComplexSingle**
  - Specifies the data for a complex I/Q waveform including the start, delta, and actual values.
- **reset Boolean**
  - Resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records.
- **reserved Int64**
  - Reserved for future use. Any value passed to this parameter will be ignored.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/b514283d-823e-fe4c-f9d7-0c1396886227.htm language=enus -->
## TOPIC 00092: rfmxbtdotnet/html/b514283d-823e-fe4c-f9d7-0c1396886227.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/b514283d-823e-fe4c-f9d7-0c1396886227.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/b514283d-823e-fe4c-f9d7-0c1396886227.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpBurstSynchronizationType Enumeration

RFmxBTMXAcpBurstSynchronizationType Enumeration

Specifies the type of synchronization used for detecting the start of the EDR packet in the adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXAcpBurstSynchronizationType
```

```text
Public Enumeration RFmxBTMXAcpBurstSynchronizationType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble | 1 | Specifies that the measurement uses the preamble field bits to detect the start of the packet |
| SyncWord | 2 | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the SetBDAddressLap(String, Int32) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm language=enus -->
## TOPIC 00093: rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAcc.Configuration Property

RFmxBTMXModAccConfiguration Property

RFmxBTMXModAccConfiguration

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXModAccConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxBTMXModAccConfiguration
	Get
```

###### Property Value

RFmxBTMXModAccConfiguration

##### See Also

###### Reference

RFmxBTMXModAcc Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/b8be5588-01ab-36a6-aa5a-a9580375c825.htm language=enus -->
## TOPIC 00094: rfmxbtdotnet/html/b8be5588-01ab-36a6-aa5a-a9580375c825.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/b8be5588-01ab-36a6-aa5a-a9580375c825.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/b8be5588-01ab-36a6-aa5a-a9580375c825.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXPowerRampConfiguration Methods

RFmxBTMXPowerRampConfiguration Methods

The [RFmxBTMXPowerRampConfiguration](9cccdf35-bcc2-e87c-c4ee-78fa4a6c0ae9.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the PowerRamp measurement. |
|  | ConfigureBurstSynchronizationType | Configures the burst synchronization type for PowerRamp measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the PowerRampAveragingEnabled method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for PowerRamp measurement. |
|  | GetBurstSynchronizationType | Gets the type of synchronization used for detecting the start of packet in the PowerRamp measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for PowerRamp measurement. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the PowerRampAveragingEnabledmethod to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for PowerRamp measurement. |
|  | SetBurstSynchronizationType | Sets the type of synchronization used for detecting the start of packet in the PowerRamp measurement. |
|  | SetMeasurementEnabled | Sets whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for PowerRamp measurement. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxBTMXPowerRampConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm language=enus -->
## TOPIC 00095: rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX Class

RFmxBTMX Class

Defines a root class which is used to identify and control BT signal configuration.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMX : ISignalConfiguration, 
	IDisposable
```

```text
Public NotInheritable Class RFmxBTMX
	Implements ISignalConfiguration, IDisposable
```

The RFmxBTMX type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Acp | Gets the RFmxBTMXAcp instance that represents the ACP measurement. |
|  | FrequencyRange | Gets the RFmxBTMXFrequencyRange instance that represents the FrequencyRange measurement. |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | ModAcc | Gets the RFmxBTMXModAcc instance that represents the ModAcc measurement. |
|  | ModSpectrum | Gets the RFmxBTMXModSpectrum instance that represents the ModSpectrum measurement. |
|  | PowerRamp | Gets the RFmxBTMXPowerRamp instance that represents the PowerRamp measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxBTMX. |
|  | TwentydBBandwidth | Gets the RFmxBTMXTwentydBBandwidth instance that represents the 20dBBandwidth measurement. |
|  | Txp | Gets the RFmxBTMXTxp instance that represents the TXP measurement. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(String, String) or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either IQ or IQorSpectral. Query the Recommended Acquisition Type method after calling the RFmxBT Commit method. |
|  | AutoDetectSignal | Detects the Bluetooth packet and returns the detected packet type, data rate, and payload length. |
|  | AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(String, Double) method. Use this method to help calculate an approximate setting for the reference level. The RFmxBT Auto Level method does the following: Resets the mixer level, mixer level offset and IF output power offset. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings. Iterates to adjust the reference level based on the input signal peak power. Uses immediate triggering and restores the trigger settings back to user setting after completing execution. You can also specify the starting reference level using the Auto Level Initial Reference Level method.When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxBT Auto Level method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method, thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildOffsetString | Creates the offset string. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSlotString | Creates a selector string for use with the TXP configuration or fetch methods and methods. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxBT commits settings to the hardware when you call the Initiate(String, String) method or any of the measurement Read methods. |
|  | ConfigureChannelNumber | Configures the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification. |
|  | ConfigureDataRate | Configures the data rate of the low energy (LE) or low energy - channel sounding (LE-CS) packet to be measured. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureDirectionFinding | Obsolete. Configures the mode of direction finding and the length of Constant tone extension field in the generated signal. |
|  | ConfigureExternalAttenuation | Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
|  | ConfigureFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
|  | ConfigureLEDirectionFinding | Configures the mode of direction finding, length of the constant tone extension field, and the duration of the switching slot in the generated signal. |
|  | ConfigurePacketType | Configures the type of Bluetooth packet to be measured. |
|  | ConfigurePayloadBitPattern | Configures the bit pattern present in the payload of the packet. |
|  | ConfigurePayloadLength | Configures the payloadLengthMode and Auto parameters that decide the length of the payload to be used for the measurement. |
|  | ConfigureReferenceLevel | Configures the reference level which represents the maximum expected power of an RF input signal. |
|  | ConfigureRF | Configures the RF methods of the signal specified by the selector string. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
|  | DeleteSignalConfiguration | Deletes an instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAccessAddress | Gets the 32-bit LE access address. |
|  | GetAllNamedResultNames | Gets the named result names of the signal that you specify in the selectorString parameter. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | GetBandwidthBitPeriodProduct | Gets the bandwidth bit period product of GFSK modulation for LE-CS packet type. |
|  | GetBDAddressLap | Gets the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |
|  | GetCenterFrequency | Gets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
|  | GetChannelNumber | Gets the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | GetChannelSoundingAntennaSwitchTime | Gets the Channel Sounding Antenna Switch Time for the LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | GetChannelSoundingNumberOfAntennaPath | Gets the number of antenna paths for the generated LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | GetChannelSoundingPacketFormat | Gets the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS. |
|  | GetChannelSoundingPhaseMeasurementPeriod | Gets the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | GetChannelSoundingSyncSequence | Gets the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
|  | GetChannelSoundingToneExtensionSlot | Gets whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | GetCteLength | Gets the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |
|  | GetCteNumberOfTransmitSlots | Gets the number of transmit slots in the constant time extension portion of the generated LE packet. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
|  | GetCteSlotDuration | Gets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
|  | GetDataRate | Gets the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types. |
|  | GetDetectedDataRate | Gets the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
|  | GetDetectedPacketType | Gets the packet type detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
|  | GetDetectedPayloadLength | Gets the payload length detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
|  | GetDigitalEdgeTriggerEdge | Gets the active edge for the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | GetDigitalEdgeTriggerSource | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | GetDirectionFindingMode | Gets the mode of direction finding. |
|  | GetErrorString | Converts the status code returned by an RFmxBT function into a string. |
|  | GetExternalAttenuation | Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQPowerEdgeTriggerLevel | Gets the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
|  | GetPacketType | Gets the type of the Bluetooth packet to be measured. |
|  | GetPayloadBitPattern | Gets the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. |
|  | GetPayloadLength | Gets the payload length of the signal in bytes. This method is applicable only when you set the SetPayloadLengthMode(String, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length used for measurement if you set the Payload Length Mode method to Auto. |
|  | GetPayloadLengthMode | Gets the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(String, Int32) properties decide the length of the payload to be used for measurement. |
|  | GetReferenceLevel | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | GetResultFetchTimeout | Gets the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | GetTriggerDelay | Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | GetTriggerMinimumQuietTimeDuration | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement computes the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the type of trigger to be used for signal acquisition. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetWarning | Gets the latest warning code and description. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxBT_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configure an invalid trigger. You have not previously called the Initiate(String, String) method. |
|  | SetAccessAddress | Sets the 32-bit LE access address. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SetBandwidthBitPeriodProduct | Sets the bandwidth bit period product of GFSK modulation for LE-CS packet type. |
|  | SetBDAddressLap | Sets the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |
|  | SetCenterFrequency | Sets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
|  | SetChannelNumber | Sets the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | SetChannelSoundingAntennaSwitchTime | Sets the Channel Sounding Antenna Switch Time for the LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | SetChannelSoundingNumberOfAntennaPath | Sets the number of antenna paths for the generated LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | SetChannelSoundingPacketFormat | Sets the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS. |
|  | SetChannelSoundingPhaseMeasurementPeriod | Sets the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | SetChannelSoundingSyncSequence | Sets the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
|  | SetChannelSoundingToneExtensionSlot | Sets whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | SetCteLength | Sets the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |
|  | SetCteSlotDuration | Sets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
|  | SetDataRate | Sets the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types. |
|  | SetDigitalEdgeTriggerEdge | Sets the active edge for the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | SetDirectionFindingMode | Sets the mode of direction finding. |
|  | SetExternalAttenuation | Sets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
|  | SetIQPowerEdgeTriggerLevel | Sets the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
|  | SetPacketType | Sets the type of the Bluetooth packet to be measured. |
|  | SetPayloadBitPattern | Sets the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. |
|  | SetPayloadLength | Sets the payload length of the signal in bytes. This method is applicable only when you set the SetPayloadLengthMode(String, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length used for measurement if you set the Payload Length Mode method to Auto. |
|  | SetPayloadLengthMode | Sets the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(String, Int32) properties decide the length of the payload to be used for measurement. |
|  | SetReferenceLevel | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | SetResultFetchTimeout | Sets the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete. |
|  | SetSelectedPorts | Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | SetTriggerDelay | Sets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | SetTriggerMinimumQuietTimeDuration | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement computes the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the type of trigger to be used for signal acquisition. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/ba235315-9953-32a6-cba3-8004f1bcb9e2.htm language=enus -->
## TOPIC 00096: rfmxbtdotnet/html/ba235315-9953-32a6-cba3-8004f1bcb9e2.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/ba235315-9953-32a6-cba3-8004f1bcb9e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/ba235315-9953-32a6-cba3-8004f1bcb9e2.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXPowerRampConfiguration.GetBurstSynchronizationType Method

RFmxBTMXPowerRampConfigurationGetBurstSynchronizationType Method

Gets the type of synchronization used for detecting the start of packet in the PowerRamp measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstSynchronizationType(
	string selectorString,
	out RFmxBTMXPowerRampBurstSynchronizationType value
)
```

```text
Public Function GetBurstSynchronizationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXPowerRampBurstSynchronizationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXPowerRampBurstSynchronizationType**
  - Upon return, contains the type of synchronization used for detecting the start of packet in the PowerRamp measurement.

###### Return Value

Int32

##### Remarks

PowerRampBurstSynchronizationType

Preamble

##### See Also

###### Reference

RFmxBTMXPowerRampConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/bc9a7798-9611-99f8-7706-624b1d09b61d.htm language=enus -->
## TOPIC 00097: rfmxbtdotnet/html/bc9a7798-9611-99f8-7706-624b1d09b61d.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/bc9a7798-9611-99f8-7706-624b1d09b61d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/bc9a7798-9611-99f8-7706-624b1d09b61d.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccConfiguration.GetAveragingCount Method

RFmxBTMXModAccConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ModAccAveragingCount

##### See Also

###### Reference

RFmxBTMXModAccConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/be0986a2-a8e3-a34a-3a56-34547fec399c.htm language=enus -->
## TOPIC 00098: rfmxbtdotnet/html/be0986a2-a8e3-a34a-3a56-34547fec399c.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/be0986a2-a8e3-a34a-3a56-34547fec399c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/be0986a2-a8e3-a34a-3a56-34547fec399c.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetAttributeDouble Method

RFmxBTMXGetAttributeDouble Method

Gets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeDouble(
	string selectorString,
	int attributeIdentifier,
	out double value
)
```

```text
Public Function GetAttributeDouble ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Passes the ID of an attribute.
- **value Double**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/be5a30cf-785d-8bb6-96af-cdedf337dc0d.htm language=enus -->
## TOPIC 00099: rfmxbtdotnet/html/be5a30cf-785d-8bb6-96af-cdedf337dc0d.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/be5a30cf-785d-8bb6-96af-cdedf337dc0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/be5a30cf-785d-8bb6-96af-cdedf337dc0d.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetDf2avgMean Method

RFmxBTMXModAccResultsGetDf2avgMean Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDf2avgMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetDf2avgMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df2avg results computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsDf2avgMean

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/bf1cb972-d0c4-b3a3-9b71-18a1a179daef.htm language=enus -->
## TOPIC 00100: rfmxbtdotnet/html/bf1cb972-d0c4-b3a3-9b71-18a1a179daef.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/bf1cb972-d0c4-b3a3-9b71-18a1a179daef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/bf1cb972-d0c4-b3a3-9b71-18a1a179daef.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.FetchMaskTrace Method

RFmxBTMXAcpResultsFetchMaskTrace Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMaskTrace(
	string selectorString,
	double timeout,
	ref Spectrum<float> limitWithExceptionMask,
	ref Spectrum<float> limitWithoutExceptionMask
)
```

```text
Public Function FetchMaskTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef limitWithExceptionMask As Spectrum(Of Single),
	ByRef limitWithoutExceptionMask As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **limitWithExceptionMask SpectrumSingle**
  - Upon return, contains the limit with exception mask trace used for the measurement.
- **limitWithoutExceptionMask SpectrumSingle**
  - Upon return, contains the limit without exception mask trace used for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/c2f61915-8f49-c82d-7e7f-59bae951da97.htm language=enus -->
## TOPIC 00101: rfmxbtdotnet/html/c2f61915-8f49-c82d-7e7f-59bae951da97.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/c2f61915-8f49-c82d-7e7f-59bae951da97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/c2f61915-8f49-c82d-7e7f-59bae951da97.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeConfiguration.ConfigureAveraging Method

RFmxBTMXFrequencyRangeConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxBTMXFrequencyRangeAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxBTMXFrequencyRangeAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxBTMXFrequencyRangeAveragingEnabled**
  - Specifies whether to enable averaging for the FrequencyRange measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXFrequencyRangeConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/c326d9a1-a0c8-1183-5a09-9869ef5715b0.htm language=enus -->
## TOPIC 00102: rfmxbtdotnet/html/c326d9a1-a0c8-1183-5a09-9869ef5715b0.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/c326d9a1-a0c8-1183-5a09-9869ef5715b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/c326d9a1-a0c8-1183-5a09-9869ef5715b0.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModSpectrumConfiguration.SetMeasurementEnabled Method

RFmxBTMXModSpectrumConfigurationSetMeasurementEnabled Method

Sets whether to enable the ModSpectrum measurements.This measurement is valid only for channel sounding (CS) packets.

Namespace:

NationalInstruments.RFmx.BTMX

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
  - Specifies whether to enable the ModSpectrum measurements.This measurement is valid only for channel sounding (CS) packets.

###### Return Value

Int32

##### Remarks

ModSpectrumMeasurementEnabled

##### See Also

###### Reference

RFmxBTMXModSpectrumConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/c63be3d4-8a15-7e79-4dd8-ad5dce042d1c.htm language=enus -->
## TOPIC 00103: rfmxbtdotnet/html/c63be3d4-8a15-7e79-4dd8-ad5dce042d1c.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/c63be3d4-8a15-7e79-4dd8-ad5dce042d1c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/c63be3d4-8a15-7e79-4dd8-ad5dce042d1c.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpBurstSynchronizationType Enumeration

RFmxBTMXTxpBurstSynchronizationType Enumeration

Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXTxpBurstSynchronizationType
```

```text
Public Enumeration RFmxBTMXTxpBurstSynchronizationType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble | 1 | Specifies that the measurement uses the preamble field to detect the start of the packet. |
| SyncWord | 2 | Specifies that the measurement uses sync word for the BR/EDR packets and access address for LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the SetBDAddressLap(String, Int32) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/d2fabe1e-c1ab-2131-08df-8e71c65fe3ec.htm language=enus -->
## TOPIC 00104: rfmxbtdotnet/html/d2fabe1e-c1ab-2131-08df-8e71c65fe3ec.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/d2fabe1e-c1ab-2131-08df-8e71c65fe3ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/d2fabe1e-c1ab-2131-08df-8e71c65fe3ec.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthResults Methods

RFmxBTMXTwentydBBandwidthResults Methods

The [RFmxBTMXTwentydBBandwidthResults](e8cfb9c6-d03b-ac5f-84d3-42252a3cc2f1.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchMeasurement | Fetches the 20dBBandwidth measurement results. |
|  | FetchSpectrum | Fetches the 20dBBandwidth spectrum trace. |
|  | GetBandwidth | Gets the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetHighFrequency | Gets the highest frequency above the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
|  | GetLowFrequency | Gets the lowest frequency below the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
|  | GetPeakPower | Gets the peak power of the measured spectrum. This value is expressed in dBm. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/d3272410-289a-63ea-915b-0e979740c66b.htm language=enus -->
## TOPIC 00105: rfmxbtdotnet/html/d3272410-289a-63ea-915b-0e979740c66b.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/d3272410-289a-63ea-915b-0e979740c66b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/d3272410-289a-63ea-915b-0e979740c66b.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcp Properties

RFmxBTMXAcp Properties

The [RFmxBTMXAcp](4a4c2240-0d07-6aae-387c-51eaa8015704.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxBTMXAcpConfiguration instance that provides methods to configure the ACP measurement. |
|  | Results | Gets the RFmxBTMXAcpResults instance that provides methods to fetch and read the ACP measurement results. |

Top

##### See Also

###### Reference

RFmxBTMXAcp Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-bt-dotnet path=rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm language=enus -->
## TOPIC 00106: rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm

- bundle_id: `rfmx-bt-dotnet`
- source_path: `rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-dotnet/raw/resource/enus/rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm
- document_id: `rfmx-bt-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration.GetBurstSynchronizationType Method

RFmxBTMXTxpConfigurationGetBurstSynchronizationType Method

Gets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstSynchronizationType(
	string selectorString,
	out RFmxBTMXTxpBurstSynchronizationType value
)
```

```text
Public Function GetBurstSynchronizationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXTxpBurstSynchronizationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxBTMXTxpBurstSynchronizationType**
  - Upon return, contains the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

###### Return Value

Int32

##### Remarks

TxpBurstSynchronizationType

Preamble

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
