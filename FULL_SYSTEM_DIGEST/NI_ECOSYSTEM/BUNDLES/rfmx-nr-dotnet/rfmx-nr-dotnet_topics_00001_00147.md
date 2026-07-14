# NI DOCUMENT BUNDLE: rfmx-nr-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-nr-dotnet start=1 end=147 -->
<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/01973c0e-6c3f-1866-bd5a-974fe80ce859.htm language=enus -->
## TOPIC 00001: rfmxnrdotnet/html/01973c0e-6c3f-1866-bd5a-974fe80ce859.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/01973c0e-6c3f-1866-bd5a-974fe80ce859.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/01973c0e-6c3f-1866-bd5a-974fe80ce859.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemComponentCarrierResults.GetPeakFrequency Method

RFmxNRMXSemComponentCarrierResultsGetPeakFrequency Method

Gets the frequency at which peak power occurs in the component carrier. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the frequency at which peak power occurs in the component carrier. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemResultsComponentCarrierPeakFrequency

##### See Also

###### Reference

RFmxNRMXSemComponentCarrierResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/020be035-987b-cd21-7bc0-08670cd24648.htm language=enus -->
## TOPIC 00002: rfmxnrdotnet/html/020be035-987b-cd21-7bc0-08670cd24648.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/020be035-987b-cd21-7bc0-08670cd24648.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/020be035-987b-cd21-7bc0-08670cd24648.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPdschPtrsREOffset Method

RFmxNRMXComponentCarrierSetPdschPtrsREOffset Method

3GPP 38.211

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdschPtrsREOffset(
	string selectorString,
	int value
)
```

```text
Public Function SetPdschPtrsREOffset ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification.

###### Return Value

Int32

##### Remarks

PdschPtrsREOffset

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0251fc19-28d7-6870-3d7e-26d012158ad7.htm language=enus -->
## TOPIC 00003: rfmxnrdotnet/html/0251fc19-28d7-6870-3d7e-26d012158ad7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0251fc19-28d7-6870-3d7e-26d012158ad7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0251fc19-28d7-6870-3d7e-26d012158ad7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccShortFrameLengthUnit Enumeration

RFmxNRMXModAccShortFrameLengthUnit Enumeration

Specifies the units in which Short Frame Length is specified.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXModAccShortFrameLengthUnit
```

```text
Public Enumeration RFmxNRMXModAccShortFrameLengthUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Slot | 1 | Short frame length is specified in units of slots. |
|  | Subframe | 3 | Short frame length is specified in units of subframes. |
|  | Time | 6 | Short frame length is specified in units of time. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/02868c50-f8e9-e429-af05-ac516a76672b.htm language=enus -->
## TOPIC 00004: rfmxnrdotnet/html/02868c50-f8e9-e429-af05-ac516a76672b.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/02868c50-f8e9-e429-af05-ac516a76672b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/02868c50-f8e9-e429-af05-ac516a76672b.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.BuildPuschClusterString Method

RFmxNRMXBuildPuschClusterString Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildPuschClusterString(
	string selectorString,
	int puschClusterNumber
)
```

```text
Public Shared Function BuildPuschClusterString ( 
	selectorString As String,
	puschClusterNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, bandwidth part number, user number, and pusch number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/user0/pusch0""result::r1/subblock0/carrier0/bwp0/user0/pusch0" You can use the BuildPuschString(String, Int32) method to build the selector string.
- **puschClusterNumber**
  - Type: SystemInt32 Specifies the PUSCH cluster number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/02c1be80-87db-d326-b6f3-17bf82decde2.htm language=enus -->
## TOPIC 00005: rfmxnrdotnet/html/02c1be80-87db-d326-b6f3-17bf82decde2.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/02c1be80-87db-d326-b6f3-17bf82decde2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/02c1be80-87db-d326-b6f3-17bf82decde2.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.GetSubblockIntegrationBandwidth Method

RFmxNRMXSemConfigurationGetSubblockIntegrationBandwidth Method

Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSubblockIntegrationBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetSubblockIntegrationBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

###### Return Value

Int32

##### Remarks

SemSubblockIntegrationBandwidth

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/03166e8f-848c-752c-d596-cd8a9ce45bf3.htm language=enus -->
## TOPIC 00006: rfmxnrdotnet/html/03166e8f-848c-752c-d596-cd8a9ce45bf3.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/03166e8f-848c-752c-d596-cd8a9ce45bf3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/03166e8f-848c-752c-d596-cd8a9ce45bf3.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPuschDmrsNumberOfCdmGroups Method

RFmxNRMXComponentCarrierSetPuschDmrsNumberOfCdmGroups Method

SetPuschTransformPrecodingEnabled(String, RFmxNRMXPuschTransformPrecodingEnabled)

False

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschDmrsNumberOfCdmGroups(
	string selectorString,
	int value
)
```

```text
Public Function SetPuschDmrsNumberOfCdmGroups ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the number of CDM groups, when you set the SetPuschTransformPrecodingEnabled(String, RFmxNRMXPuschTransformPrecodingEnabled) method to False, otherwise it is coerced to 2.

###### Return Value

Int32

##### Remarks

PuschDmrsNumberOfCdmGroups

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/03cc735c-a199-1dce-33f5-e5138b9e1dfb.htm language=enus -->
## TOPIC 00007: rfmxnrdotnet/html/03cc735c-a199-1dce-33f5-e5138b9e1dfb.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/03cc735c-a199-1dce-33f5-e5138b9e1dfb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/03cc735c-a199-1dce-33f5-e5138b9e1dfb.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPdschNumberOfResourceBlocks Method

RFmxNRMXComponentCarrierGetPdschNumberOfResourceBlocks Method

Gets the number of consecutive resource blocks in a PDSCH cluster.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschNumberOfResourceBlocks(
	string selectorString,
	out int value
)
```

```text
Public Function GetPdschNumberOfResourceBlocks ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number, pdsch number and pdschcluster number. Example: "pdschcluster0" or "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0/pdschcluster0". You can use the BuildPdschClusterString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of consecutive resource blocks in a PDSCH cluster.

###### Return Value

Int32

##### Remarks

PdschNumberOfResourceBlocks

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/07ae82b3-b1a1-94a1-b455-5ec2b8e868e6.htm language=enus -->
## TOPIC 00008: rfmxnrdotnet/html/07ae82b3-b1a1-94a1-b455-5ec2b8e868e6.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/07ae82b3-b1a1-94a1-b455-5ec2b8e868e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/07ae82b3-b1a1-94a1-b455-5ec2b8e868e6.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPuschDmrsReleaseVersion Method

RFmxNRMXComponentCarrierGetPuschDmrsReleaseVersion Method

Gets the 3GGP release version for PUSCH DMRS.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschDmrsReleaseVersion(
	string selectorString,
	out RFmxNRMXPuschDmrsReleaseVersion value
)
```

```text
Public Function GetPuschDmrsReleaseVersion ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPuschDmrsReleaseVersion
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPuschDmrsReleaseVersionUpon return, contains the 3GGP release version for PUSCH DMRS.

###### Return Value

Int32

##### Remarks

PuschDmrsReleaseVersion

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/089e63db-5ab2-12e6-21ab-8e052b93e5f7.htm language=enus -->
## TOPIC 00009: rfmxnrdotnet/html/089e63db-5ab2-12e6-21ab-8e052b93e5f7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/089e63db-5ab2-12e6-21ab-8e052b93e5f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/089e63db-5ab2-12e6-21ab-8e052b93e5f7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXObwConfiguration.ConfigureAveraging Method

RFmxNRMXObwConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxNRMXObwAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxNRMXObwAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxNRMXObwAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxNRMXObwAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXObwAveragingEnabledSpecifies whether to enable averaging for the measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.
- **averagingType**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXObwAveragingTypeSpecifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXObwConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/093245b8-7cdf-d468-480c-ef8439de6c66.htm language=enus -->
## TOPIC 00010: rfmxnrdotnet/html/093245b8-7cdf-d468-480c-ef8439de6c66.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/093245b8-7cdf-d468-480c-ef8439de6c66.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/093245b8-7cdf-d468-480c-ef8439de6c66.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtConfiguration.SetMeasurementInterval Method

RFmxNRMXPvtConfigurationSetMeasurementInterval Method

Sets the measurement interval when the Measurement Interval Auto method is set to False. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementInterval(
	string selectorString,
	double value
)
```

```text
Public Function SetMeasurementInterval ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the measurement interval when the Measurement Interval Auto method is set to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PvtMeasurementInterval

##### See Also

###### Reference

RFmxNRMXPvtConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0a8f2fa7-2dba-2206-a39b-b3fd064dc56e.htm language=enus -->
## TOPIC 00011: rfmxnrdotnet/html/0a8f2fa7-2dba-2206-a39b-b3fd064dc56e.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0a8f2fa7-2dba-2206-a39b-b3fd064dc56e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0a8f2fa7-2dba-2206-a39b-b3fd064dc56e.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetTransmitAntennaToAnalyze Method

RFmxNRMXSetTransmitAntennaToAnalyze Method

Sets the physical antenna that is currently connected to the analyzer.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTransmitAntennaToAnalyze(
	string selectorString,
	int value
)
```

```text
Public Function SetTransmitAntennaToAnalyze ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the physical antenna that is currently connected to the analyzer.

###### Return Value

Int32

##### Remarks

TransmitAntennaToAnalyze

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0b961639-9abe-7973-599e-eedac72c8be4.htm language=enus -->
## TOPIC 00012: rfmxnrdotnet/html/0b961639-9abe-7973-599e-eedac72c8be4.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0b961639-9abe-7973-599e-eedac72c8be4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0b961639-9abe-7973-599e-eedac72c8be4.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetGridStart Method

RFmxNRMXComponentCarrierGetGridStart Method

Gets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetGridStart(
	string selectorString,
	out int value
)
```

```text
Public Function GetGridStart ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual.

###### Return Value

Int32

##### Remarks

GridStart

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0c00a192-e8b6-3b0c-9aee-38c117ad04a4.htm language=enus -->
## TOPIC 00013: rfmxnrdotnet/html/0c00a192-e8b6-3b0c-9aee-38c117ad04a4.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0c00a192-e8b6-3b0c-9aee-38c117ad04a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0c00a192-e8b6-3b0c-9aee-38c117ad04a4.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpOffsetSideband Enumeration

RFmxNRMXAcpOffsetSideband Enumeration

Specifies the sideband measured for the offset channel.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXAcpOffsetSideband
```

```text
Public Enumeration RFmxNRMXAcpOffsetSideband
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Negative | 0 | Configures a lower offset segment to the left of the leftmost carrier. |
|  | Positive | 1 | Configures an upper offset segment to the right of the rightmost carrier. |
|  | Both | 2 | Configures both the negative and the positive offset segments. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0d26d60d-01d2-5635-cf35-939fa2857493.htm language=enus -->
## TOPIC 00014: rfmxnrdotnet/html/0d26d60d-01d2-5635-cf35-939fa2857493.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0d26d60d-01d2-5635-cf35-939fa2857493.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0d26d60d-01d2-5635-cf35-939fa2857493.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtConfiguration.GetMeasurementIntervalAuto Method

RFmxNRMXPvtConfigurationGetMeasurementIntervalAuto Method

Gets whether the measurement interval is computed by the measurement or configured by the user through Measurement Interval method.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementIntervalAuto(
	string selectorString,
	out RFmxNRMXPvtMeasurementIntervalAuto value
)
```

```text
Public Function GetMeasurementIntervalAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPvtMeasurementIntervalAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPvtMeasurementIntervalAutoUpon return, contains whether the measurement interval is computed by the measurement or configured by the user through Measurement Interval method.

###### Return Value

Int32

##### Remarks

PvtMeasurementIntervalAuto

##### See Also

###### Reference

RFmxNRMXPvtConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0d5038ec-02dd-d25c-ffd1-da0706b8d2fc.htm language=enus -->
## TOPIC 00015: rfmxnrdotnet/html/0d5038ec-02dd-d25c-ffd1-da0706b8d2fc.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0d5038ec-02dd-d25c-ffd1-da0706b8d2fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0d5038ec-02dd-d25c-ffd1-da0706b8d2fc.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.SetRbwFilterType Method

RFmxNRMXAcpConfigurationSetRbwFilterType Method

Sets the shape of the RBW filter.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxNRMXAcpRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxNRMXAcpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXAcpRbwFilterTypeSpecifies the shape of the RBW filter.

###### Return Value

Int32

##### Remarks

AcpRbwFilterType

FftBased

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0efda717-09a2-578e-5c6f-e172f924faa7.htm language=enus -->
## TOPIC 00016: rfmxnrdotnet/html/0efda717-09a2-578e-5c6f-e172f924faa7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0efda717-09a2-578e-5c6f-e172f924faa7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0efda717-09a2-578e-5c6f-e172f924faa7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.GetIQOriginOffsetEstimationEnabled Method

RFmxNRMXModAccConfigurationGetIQOriginOffsetEstimationEnabled Method

Gets whether to estimate the IQ origin offset. If IQ origin offset is absent in the signal to be analyzed, you may disable IQ origin offset estimation to reduce measurement time or to avoid measurement inaccuracy due to error in IQ origin offset estimation.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOriginOffsetEstimationEnabled(
	string selectorString,
	out RFmxNRMXModAccIQOriginOffsetEstimationEnabled value
)
```

```text
Public Function GetIQOriginOffsetEstimationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXModAccIQOriginOffsetEstimationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccIQOriginOffsetEstimationEnabledUpon return, contains whether to estimate the IQ origin offset. If IQ origin offset is absent in the signal to be analyzed, you may disable IQ origin offset estimation to reduce measurement time or to avoid measurement inaccuracy due to error in IQ origin offset estimation.

###### Return Value

Int32

##### Remarks

ModAccIQOriginOffsetEstimationEnabled

True

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/0f652a2b-e74f-1f00-2bd7-0671c699df49.htm language=enus -->
## TOPIC 00017: rfmxnrdotnet/html/0f652a2b-e74f-1f00-2bd7-0671c699df49.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/0f652a2b-e74f-1f00-2bd7-0671c699df49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/0f652a2b-e74f-1f00-2bd7-0671c699df49.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.GetDeltaFMaximum Method

RFmxNRMXSemConfigurationGetDeltaFMaximum Method

SetDownlinkMaskType(String, RFmxNRMXSemDownlinkMaskType)

Standard

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDeltaFMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetDeltaFMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the stop frequency for 3rd offset segment to be used in the measurement. This method is valid only for downlink and when you set the SetDownlinkMaskType(String, RFmxNRMXSemDownlinkMaskType) method to Standard.

###### Return Value

Int32

##### Remarks

SemDeltaFMaximum

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/10775dd0-b5e4-d707-f4c3-8c798dee1c73.htm language=enus -->
## TOPIC 00018: rfmxnrdotnet/html/10775dd0-b5e4-d707-f4c3-8c798dee1c73.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/10775dd0-b5e4-d707-f4c3-8c798dee1c73.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/10775dd0-b5e4-d707-f4c3-8c798dee1c73.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPdsch1024QamConstellationTrace Method

RFmxNRMXModAccResultsFetchPdsch1024QamConstellationTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPdsch1024QamConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] qam1024Constellation
)
```

```text
Public Function FetchPdsch1024QamConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef qam1024Constellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **qam1024Constellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the 1024 QAM constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/10c3d693-1d96-05be-aba7-edaae59b35cc.htm language=enus -->
## TOPIC 00019: rfmxnrdotnet/html/10c3d693-1d96-05be-aba7-edaae59b35cc.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/10c3d693-1d96-05be-aba7-edaae59b35cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/10c3d693-1d96-05be-aba7-edaae59b35cc.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.GetMeasurementEnabled Method

RFmxNRMXChpConfigurationGetMeasurementEnabled Method

Gets whether to enable the channel power measurement.

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanUpon return, contains whether to enable the channel power measurement.

###### Return Value

Int32

##### Remarks

ChpMeasurementEnabled

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/111d8b3b-edd5-3669-dff0-4515880b098f.htm language=enus -->
## TOPIC 00020: rfmxnrdotnet/html/111d8b3b-edd5-3669-dff0-4515880b098f.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/111d8b3b-edd5-3669-dff0-4515880b098f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/111d8b3b-edd5-3669-dff0-4515880b098f.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetFrequency Method

RFmxNRMXComponentCarrierSetFrequency Method

Sets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ComponentCarrierFrequency

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/11340699-453a-905f-a22d-e890cb1b7999.htm language=enus -->
## TOPIC 00021: rfmxnrdotnet/html/11340699-453a-905f-a22d-e890cb1b7999.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/11340699-453a-905f-a22d-e890cb1b7999.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/11340699-453a-905f-a22d-e890cb1b7999.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpResults.FetchAbsolutePowersTrace Method

RFmxNRMXAcpResultsFetchAbsolutePowersTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **traceIndex**
  - Type: SystemInt32 Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets).
- **absolutePowersTrace**
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the trace of the measured integrated power in the channel specified by the traceIndex parameter. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXAcpResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/11bd80bc-3439-e41c-2923-bb31f5c4cdaa.htm language=enus -->
## TOPIC 00022: rfmxnrdotnet/html/11bd80bc-3439-e41c-2923-bb31f5c4cdaa.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/11bd80bc-3439-e41c-2923-bb31f5c4cdaa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/11bd80bc-3439-e41c-2923-bb31f5c4cdaa.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPbchDataRmsEvmPerSubcarrierMeanTrace Method

RFmxNRMXModAccResultsFetchPbchDataRmsEvmPerSubcarrierMeanTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPbchDataRmsEvmPerSubcarrierMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> pbchDataRmsEvmPerSubcarrierMean
)
```

```text
Public Function FetchPbchDataRmsEvmPerSubcarrierMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef pbchDataRmsEvmPerSubcarrierMean As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **pbchDataRmsEvmPerSubcarrierMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PBCH data within the Meas Length method. The unit of this EVM value is specified by the SetEvmUnit(String, RFmxNRMXModAccEvmUnit) method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/11e93cdd-45fe-29b2-300a-e937565dd74a.htm language=enus -->
## TOPIC 00023: rfmxnrdotnet/html/11e93cdd-45fe-29b2-300a-e937565dd74a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/11e93cdd-45fe-29b2-300a-e937565dd74a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/11e93cdd-45fe-29b2-300a-e937565dd74a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetDigitalEdgeTriggerEdge Method

RFmxNRMXSetDigitalEdgeTriggerEdge Method

SetTriggerType(String, RFmxNRMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerEdge(
	string selectorString,
	RFmxNRMXDigitalEdgeTriggerEdge value
)
```

```text
Public Function SetDigitalEdgeTriggerEdge ( 
	selectorString As String,
	value As RFmxNRMXDigitalEdgeTriggerEdge
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXDigitalEdgeTriggerEdge Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxNRMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerEdge

Rising

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/11e99740-25b2-6652-1e06-ffead921769c.htm language=enus -->
## TOPIC 00024: rfmxnrdotnet/html/11e99740-25b2-6652-1e06-ffead921769c.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/11e99740-25b2-6652-1e06-ffead921769c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/11e99740-25b2-6652-1e06-ffead921769c.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPuschDmrsDuration Method

RFmxNRMXComponentCarrierSetPuschDmrsDuration Method

Sets whether the DMRS is single-symbol or double-symbol.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschDmrsDuration(
	string selectorString,
	RFmxNRMXPuschDmrsDuration value
)
```

```text
Public Function SetPuschDmrsDuration ( 
	selectorString As String,
	value As RFmxNRMXPuschDmrsDuration
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPuschDmrsDurationSpecifies whether the DMRS is single-symbol or double-symbol.

###### Return Value

Int32

##### Remarks

PuschDmrsDuration

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/126b1650-762c-8f3a-f2d8-526921ce9ec3.htm language=enus -->
## TOPIC 00025: rfmxnrdotnet/html/126b1650-762c-8f3a-f2d8-526921ce9ec3.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/126b1650-762c-8f3a-f2d8-526921ce9ec3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/126b1650-762c-8f3a-f2d8-526921ce9ec3.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.AnalyzeIQ1Waveform Method

RFmxNRMXAnalyzeIQ1Waveform Method

IQ

IQ

IQorSpectral

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemString Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **resultName**
  - Type: SystemString Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1"
- **iq**
  - Type: NationalInstrumentsComplexWaveformComplexSingle Specifies the data for a complex waveform including the start, delta, and actual values.
- **reset**
  - Type: SystemBoolean Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records.
- **reserved**
  - Type: SystemInt64Reserved for future use. Any value passed to this parameter will be ignored.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/132e1dd9-9179-ab75-b86b-2839b03cc8ee.htm language=enus -->
## TOPIC 00026: rfmxnrdotnet/html/132e1dd9-9179-ab75-b86b-2839b03cc8ee.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/132e1dd9-9179-ab75-b86b-2839b03cc8ee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/132e1dd9-9179-ab75-b86b-2839b03cc8ee.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccCompositeResultsIncludePtrs Enumeration

RFmxNRMXModAccCompositeResultsIncludePtrs Enumeration

Specifies whether the PTRS resource elements are included for composite EVM and magnitude and phase error results and traces.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXModAccCompositeResultsIncludePtrs
```

```text
Public Enumeration RFmxNRMXModAccCompositeResultsIncludePtrs
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The PTRS resource elements are not included. |
|  | True | 1 | The PTRS resource elements are included. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/132ed675-6b09-b448-62b1-bb8ae72ce062.htm language=enus -->
## TOPIC 00027: rfmxnrdotnet/html/132ed675-6b09-b448-62b1-bb8ae72ce062.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/132ed675-6b09-b448-62b1-bb8ae72ce062.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/132ed675-6b09-b448-62b1-bb8ae72ce062.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtResults Methods

RFmxNRMXPvtResults Methods

The [RFmxNRMXPvtResults](04c182f9-b310-d62b-8cc8-636787377927.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Fetches PVT ON and OFF powers along with measurement status and burst width. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read from this method. |
|  | FetchMeasurementArray | Fetches an array of PVT ON and OFF powers along with measurement status and burst width. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSignalPowerTrace | Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | FetchWindowedSignalPowerTrace | Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetAbsoluteOffPowerAfter | Gets the OFF power in the segment after the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. |
|  | GetAbsoluteOffPowerBefore | Gets the OFF power in the segment before the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |
|  | GetAbsoluteONPower | Gets the power of the slots within the captured burst. This value is expressed in dBm. |
|  | GetBurstWidth | Gets the width of the captured burst. This value is expressed in seconds. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementStatus | Gets the measurement status indicating whether the off power before and after is within the standard defined limit. |
|  | GetPeakWindowedOffPower | Gets the NaN for the uplink direction, while it returns the peak power value of 70/N us windowed power during all OFF regions in the measurement interval. This value is expressed in dBm/MHz. |
|  | GetPeakWindowedOffPowerMargin | Gets the NaN for the uplink direction, while it returns the GetPeakWindowedOffPower(String, Double) to the 3GPP limit. This value is expressed in dB. |
|  | GetPeakWindowedOffPowerTime | Gets the NaN for the uplink direction, while it returns the time offset of the GetPeakWindowedOffPower(String, Double). This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxNRMXPvtResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1331b265-672d-daab-4bd6-e27037b34eaa.htm language=enus -->
## TOPIC 00028: rfmxnrdotnet/html/1331b265-672d-daab-4bd6-e27037b34eaa.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1331b265-672d-daab-4bd6-e27037b34eaa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1331b265-672d-daab-4bd6-e27037b34eaa.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.BuildPdcchString Method

RFmxNRMXBuildPdcchString Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildPdcchString(
	string selectorString,
	int pdcchNumber
)
```

```text
Public Shared Function BuildPdcchString ( 
	selectorString As String,
	pdcchNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, carrier number, bandwidth part number, and coreset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/coreset0""result::r1/subblock0/carrier0/bwp0/coreset0" You can use the BuildCoresetString(String, Int32) method to build the selector string.
- **pdcchNumber**
  - Type: SystemInt32 Specifies the PDCCH number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/13799633-f898-aa55-7218-648bf2fc47e0.htm language=enus -->
## TOPIC 00029: rfmxnrdotnet/html/13799633-f898-aa55-7218-648bf2fc47e0.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/13799633-f898-aa55-7218-648bf2fc47e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/13799633-f898-aa55-7218-648bf2fc47e0.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetBandwidthPartDCLocationKnown Method

RFmxNRMXComponentCarrierGetBandwidthPartDCLocationKnown Method

Gets whether Uplink Tx Direct Current location within the carrier is determined. If set to False, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only General In-Band Emission limits are applied. If set to True, DC location is determined within the carrier.
 This property is not supported when Link Direction property is set to Downlink.
 Use "bwp(m)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/bwp(m)" as the Selector Strings to configure or read this property.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBandwidthPartDCLocationKnown(
	string selectorString,
	out RFmxNRMXBandwidthPartDCLocationKnown value
)
```

```text
Public Function GetBandwidthPartDCLocationKnown ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXBandwidthPartDCLocationKnown
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXBandwidthPartDCLocationKnownUpon return, contains whether Uplink Tx Direct Current location within the carrier is determined. If set to False, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only General In-Band Emission limits are applied. If set to True, DC location is determined within the carrier.

###### Return Value

Int32

##### Remarks

BandwidthPartDCLocationKnown

True

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/14253f68-08aa-499f-b835-da913443f902.htm language=enus -->
## TOPIC 00030: rfmxnrdotnet/html/14253f68-08aa-499f-b835-da913443f902.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/14253f68-08aa-499f-b835-da913443f902.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/14253f68-08aa-499f-b835-da913443f902.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.SetOffsetRelativeLimitStart Method

RFmxNRMXSemConfigurationSetOffsetRelativeLimitStart Method

Sets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetRelativeLimitStart(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetRelativeLimitStart ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemOffsetRelativeLimitStart

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1440dd43-f111-aa67-086d-a772fea9abec.htm language=enus -->
## TOPIC 00031: rfmxnrdotnet/html/1440dd43-f111-aa67-086d-a772fea9abec.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1440dd43-f111-aa67-086d-a772fea9abec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1440dd43-f111-aa67-086d-a772fea9abec.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChp.Configuration Property

RFmxNRMXChpConfiguration Property

RFmxNRMXChpConfiguration

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxNRMXChpConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxNRMXChpConfiguration
	Get
```

###### Property Value

RFmxNRMXChpConfiguration

##### See Also

###### Reference

RFmxNRMXChp Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/16ef1aba-3626-1b29-ca0d-f139c5ddc192.htm language=enus -->
## TOPIC 00032: rfmxnrdotnet/html/16ef1aba-3626-1b29-ca0d-f139c5ddc192.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/16ef1aba-3626-1b29-ca0d-f139c5ddc192.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/16ef1aba-3626-1b29-ca0d-f139c5ddc192.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpAveragingEnabled Enumeration

RFmxNRMXAcpAveragingEnabled Enumeration

Specifies whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXAcpAveragingEnabled
```

```text
Public Enumeration RFmxNRMXAcpAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The ACP measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the ACP measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/16f28df6-17a0-a108-b1b0-6972f1b0c5ae.htm language=enus -->
## TOPIC 00033: rfmxnrdotnet/html/16f28df6-17a0-a108-b1b0-6972f1b0c5ae.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/16f28df6-17a0-a108-b1b0-6972f1b0c5ae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/16f28df6-17a0-a108-b1b0-6972f1b0c5ae.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.GetSynchronizationMode Method

RFmxNRMXModAccConfigurationGetSynchronizationMode Method

Gets whether the measurement is performed from slot or frame boundary.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSynchronizationMode(
	string selectorString,
	out RFmxNRMXModAccSynchronizationMode value
)
```

```text
Public Function GetSynchronizationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXModAccSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccSynchronizationModeUpon return, contains whether the measurement is performed from slot or frame boundary.

###### Return Value

Int32

##### Remarks

ModAccSynchronizationMode

Slot

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/175e64d3-6f29-400a-cd0b-883251fa0de4.htm language=enus -->
## TOPIC 00034: rfmxnrdotnet/html/175e64d3-6f29-400a-cd0b-883251fa0de4.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/175e64d3-6f29-400a-cd0b-883251fa0de4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/175e64d3-6f29-400a-cd0b-883251fa0de4.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpIntegrationBandwidthType Enumeration

RFmxNRMXChpIntegrationBandwidthType Enumeration

Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXChpIntegrationBandwidthType
```

```text
Public Enumeration RFmxNRMXChpIntegrationBandwidthType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SignalBandwidth | 0 | The IBW excludes the guard bands at the edges of the carrier or subblock. |
|  | ChannelBandwidth | 1 | The IBW includes the guard bands at the edges of the carrier or subblock. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1a284ffa-f1a1-ba4a-4199-cdb6b5d02428.htm language=enus -->
## TOPIC 00035: rfmxnrdotnet/html/1a284ffa-f1a1-ba4a-4199-cdb6b5d02428.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1a284ffa-f1a1-ba4a-4199-cdb6b5d02428.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1a284ffa-f1a1-ba4a-4199-cdb6b5d02428.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPuschDmrsAntennaPorts Method

RFmxNRMXComponentCarrierGetPuschDmrsAntennaPorts Method

Gets the antenna ports used for DMRS transmission.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschDmrsAntennaPorts(
	string selectorString,
	out string value
)
```

```text
Public Function GetPuschDmrsAntennaPorts ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemStringUpon return, contains the antenna ports used for DMRS transmission.

###### Return Value

Int32

##### Remarks

PuschDmrsAntennaPorts

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1abfb0fe-23e4-3fe6-3330-21e85dd02756.htm language=enus -->
## TOPIC 00036: rfmxnrdotnet/html/1abfb0fe-23e4-3fe6-3330-21e85dd02756.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1abfb0fe-23e4-3fe6-3330-21e85dd02756.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1abfb0fe-23e4-3fe6-3330-21e85dd02756.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXObwResults Class

RFmxNRMXObwResults Class

Provides methods to fetch and read the OBW measurement results.

##### Inheritance Hierarchy

RFmxNRMXSubObject

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxNRMXObwResults : RFmxNRMXSubObject
```

```text
Public NotInheritable Class RFmxNRMXObwResults
	Inherits RFmxNRMXSubObject
```

The RFmxNRMXObwResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSpectrum | Fetches the spectrum used for OBW measurements. |
|  | GetAbsolutePower | Gets the total power measured in the spectrum acquired by the measurement. This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetOccupiedBandwidth | Gets the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequency |
|  | GetStartFrequency | Gets the start frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequency |
|  | GetStopFrequency | Gets the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequency |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1b64fec2-6a4e-7a2f-00ea-397f9accdcf9.htm language=enus -->
## TOPIC 00037: rfmxnrdotnet/html/1b64fec2-6a4e-7a2f-00ea-397f9accdcf9.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1b64fec2-6a4e-7a2f-00ea-397f9accdcf9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1b64fec2-6a4e-7a2f-00ea-397f9accdcf9.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPdschDmrsTypeAPosition Method

RFmxNRMXComponentCarrierSetPdschDmrsTypeAPosition Method

Sets the position of first DMRS symbol in a slot for Type A configurations.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdschDmrsTypeAPosition(
	string selectorString,
	int value
)
```

```text
Public Function SetPdschDmrsTypeAPosition ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the position of first DMRS symbol in a slot for Type A configurations.

###### Return Value

Int32

##### Remarks

PdschDmrsTypeAPosition

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1bc1f905-f22a-5a23-b6b5-375119d3fac8.htm language=enus -->
## TOPIC 00038: rfmxnrdotnet/html/1bc1f905-f22a-5a23-b6b5-375119d3fac8.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1bc1f905-f22a-5a23-b6b5-375119d3fac8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1bc1f905-f22a-5a23-b6b5-375119d3fac8.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetIQTimingSkewCorrectionEnabled Method

RFmxNRMXModAccConfigurationSetIQTimingSkewCorrectionEnabled Method

Sets whether to enable IQ timing skew correction.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQTimingSkewCorrectionEnabled(
	string selectorString,
	RFmxNRMXModAccIQTimingSkewCorrectionEnabled value
)
```

```text
Public Function SetIQTimingSkewCorrectionEnabled ( 
	selectorString As String,
	value As RFmxNRMXModAccIQTimingSkewCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccIQTimingSkewCorrectionEnabledSpecifies whether to enable IQ timing skew correction.

###### Return Value

Int32

##### Remarks

ModAccIQTimingSkewCorrectionEnabled

False

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1cda6d56-71e4-d6be-8de0-2f54a2509219.htm language=enus -->
## TOPIC 00039: rfmxnrdotnet/html/1cda6d56-71e4-d6be-8de0-2f54a2509219.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1cda6d56-71e4-d6be-8de0-2f54a2509219.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1cda6d56-71e4-d6be-8de0-2f54a2509219.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPdschSymbolAllocation Method

RFmxNRMXComponentCarrierGetPdschSymbolAllocation Method

Gets the symbol allocation of each slot allocation.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschSymbolAllocation(
	string selectorString,
	out string value
)
```

```text
Public Function GetPdschSymbolAllocation ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemStringUpon return, contains the symbol allocation of each slot allocation.

###### Return Value

Int32

##### Remarks

PdschSymbolAllocation

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1ce60bda-e2b3-2078-159b-f68706a11423.htm language=enus -->
## TOPIC 00040: rfmxnrdotnet/html/1ce60bda-e2b3-2078-159b-f68706a11423.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1ce60bda-e2b3-2078-159b-f68706a11423.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1ce60bda-e2b3-2078-159b-f68706a11423.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemResults.GetUpperOffsetMargin Method

RFmxNRMXSemResultsGetUpperOffsetMargin Method

Gets the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetMargin(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetMargin ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMargin

##### See Also

###### Reference

RFmxNRMXSemResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1d0d08b3-e7c3-ef66-fdc4-627477d2fc40.htm language=enus -->
## TOPIC 00041: rfmxnrdotnet/html/1d0d08b3-e7c3-ef66-fdc4-627477d2fc40.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1d0d08b3-e7c3-ef66-fdc4-627477d2fc40.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1d0d08b3-e7c3-ef66-fdc4-627477d2fc40.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXDownlinkTestModel Enumeration

RFmxNRMXDownlinkTestModel Enumeration

3GPP 38.141

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXDownlinkTestModel
```

```text
Public Enumeration RFmxNRMXDownlinkTestModel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TM1_1 | 0 | Specifies a TM1.1 NR test model. |
|  | TM1_2 | 1 | Specifies a TM1.2 NR test model. |
|  | TM2 | 2 | Specifies a TM2 NR test model. |
|  | TM2a | 3 | Specifies a TM2a NR test model. |
|  | TM3_1 | 4 | Specifies a TM3.1 NR test model. |
|  | TM3_1a | 5 | Specifies a TM3.1a NR test model. |
|  | TM3_2 | 6 | Specifies a TM3.2 NR test model. |
|  | TM3_3 | 7 | Specifies a TM3.3 NR test model. |
|  | TM2b | 8 | Specifies a TM2b NR test model. |
|  | TM3_1b | 9 | Specifies a TM3.1b NR test model. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1dd4f02d-2d74-1f4f-9d00-8b74a016ad99.htm language=enus -->
## TOPIC 00042: rfmxnrdotnet/html/1dd4f02d-2d74-1f4f-9d00-8b74a016ad99.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1dd4f02d-2d74-1f4f-9d00-8b74a016ad99.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1dd4f02d-2d74-1f4f-9d00-8b74a016ad99.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPuschDmrsAdditionalPositions Method

RFmxNRMXComponentCarrierGetPuschDmrsAdditionalPositions Method

Gets the number of additional sets of consecutive DMRS symbols in a slot.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschDmrsAdditionalPositions(
	string selectorString,
	out int value
)
```

```text
Public Function GetPuschDmrsAdditionalPositions ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of additional sets of consecutive DMRS symbols in a slot.

###### Return Value

Int32

##### Remarks

PuschDmrsAdditionalPositions

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1e2d7066-5126-4317-a7ca-5a3d18f3b0d0.htm language=enus -->
## TOPIC 00043: rfmxnrdotnet/html/1e2d7066-5126-4317-a7ca-5a3d18f3b0d0.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1e2d7066-5126-4317-a7ca-5a3d18f3b0d0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1e2d7066-5126-4317-a7ca-5a3d18f3b0d0.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemDownlinkMaskType Enumeration

RFmxNRMXSemDownlinkMaskType Enumeration

Specifies the limits to be used in the measurement for Downlink.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXSemDownlinkMaskType
```

```text
Public Enumeration RFmxNRMXSemDownlinkMaskType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Standard | 0 | The measurement selects the offset frequencies and limits for SEM, as defined in Table 6.6.4.2.1-1, Table 6.6.4.2.1-2, Table 6.6.4.2.2.1-1, Table 6.6.4.2.2.1-2, Table 6.6.4.2.2.2-1, Table 6.6.4.2.3-1, Table 6.6.4.2.3-2, and Table 6.6.4.2.4-1 in section 6.6.4 and Table 9.7.4.3.2-1, 9.7.4.3.2-2, 9.7.4.3.3-1 and 9.7.4.3.3-2 in section 9.7.4 of the 3GPP TS 38.104 Specification. If the band value is set to 46 or 96 or 102, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.6.4.2.4A-1 and Table 6.6.4.2.4A-2 in section 6.6.4 of the 3GPP TS 38.104 Specification. If the band value is set to NTN bands 254, 255 or 256, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.6.4.2-1 in section 6.6.4 of the 3GPP 38.108 specification. The offset frequencies in Table 9.7.4.3.2-1, 9.7.4.3.2-2, 9.7.4.3.3-1 and 9.7.4.3.3-2 are relative to the contiguous transmission bandwidth edge. The measurement converts these offset frequencies to make them relative to the subblock edge before applying the masks. For range 1, the gNodeBCategory property can be set to any of the following values: Wide Area Base Station - Category A, Wide Area Base Station - Category B Option1, Wide Area Base Station - Category B Option2, Local Area Base Station, or Medium Range Base Station. Set the Band property for selecting limits table within a gNodeB category. For range 2, the gNodeB Category property can be set to any of the following values: FR2 Category A or FR2 Category B. Set the Band property for selecting limits table. |
|  | Custom | 2 | Specifies that limits are applied based on user-defined offset segments. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1e424517-6c97-e795-0b16-827863576264.htm language=enus -->
## TOPIC 00044: rfmxnrdotnet/html/1e424517-6c97-e795-0b16-827863576264.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1e424517-6c97-e795-0b16-827863576264.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1e424517-6c97-e795-0b16-827863576264.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXListStepTimerUnit Enumeration

RFmxNRMXListStepTimerUnit Enumeration

SetListStepTimerDuration(String, Double)

SetListStepTimerOffset(String, Double)

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXListStepTimerUnit
```

```text
Public Enumeration RFmxNRMXListStepTimerUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Slot | 1 | List Step Timer Duration and List Step Timer Offset are specified in units of slots. |
|  | Time | 6 | List Step Timer Duration and List Step Timer Offset are specified in seconds. Specify the List Step Timer Duration and List Step Timer Offset in multiples of 1 ms * (15 kHz/minimum subcarrier spacing of all carriers). All slots within this notional time duration are analysed. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1e8ca782-bdfc-b64f-fb74-05994a35e20c.htm language=enus -->
## TOPIC 00045: rfmxnrdotnet/html/1e8ca782-bdfc-b64f-fb74-05994a35e20c.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1e8ca782-bdfc-b64f-fb74-05994a35e20c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1e8ca782-bdfc-b64f-fb74-05994a35e20c.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPbchDmrsRmsEvmPerSubcarrierMeanTrace Method

RFmxNRMXModAccResultsFetchPbchDmrsRmsEvmPerSubcarrierMeanTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPbchDmrsRmsEvmPerSubcarrierMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> pbchDmrsRmsEvmPerSubcarrierMean
)
```

```text
Public Function FetchPbchDmrsRmsEvmPerSubcarrierMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef pbchDmrsRmsEvmPerSubcarrierMean As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **pbchDmrsRmsEvmPerSubcarrierMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PBCH DMRS within the Meas Length. The unit of this EVM value is specified by the SetEvmUnit(String, RFmxNRMXModAccEvmUnit) method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1f39233d-65cd-1edc-fef1-c5f15047b6a5.htm language=enus -->
## TOPIC 00046: rfmxnrdotnet/html/1f39233d-65cd-1edc-fef1-c5f15047b6a5.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1f39233d-65cd-1edc-fef1-c5f15047b6a5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1f39233d-65cd-1edc-fef1-c5f15047b6a5.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetPdschDataRmsEvmMean Method

RFmxNRMXModAccResultsGetPdschDataRmsEvmMean Method

Gets the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschDataRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPdschDataRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols.

###### Return Value

Int32

##### Remarks

ModAccResultsPdschDataRmsEvmMean

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/1f446753-a7e0-4617-81ac-6dd6a1c74d33.htm language=enus -->
## TOPIC 00047: rfmxnrdotnet/html/1f446753-a7e0-4617-81ac-6dd6a1c74d33.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/1f446753-a7e0-4617-81ac-6dd6a1c74d33.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/1f446753-a7e0-4617-81ac-6dd6a1c74d33.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPdschQpskConstellationTrace Method

RFmxNRMXModAccResultsFetchPdschQpskConstellationTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPdschQpskConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] qpskConstellation
)
```

```text
Public Function FetchPdschQpskConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef qpskConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **qpskConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the QPSK constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/20263ad6-d8f4-fd6f-058b-87b3fbb1b3b0.htm language=enus -->
## TOPIC 00048: rfmxnrdotnet/html/20263ad6-d8f4-fd6f-058b-87b3fbb1b3b0.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/20263ad6-d8f4-fd6f-058b-87b3fbb1b3b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/20263ad6-d8f4-fd6f-058b-87b3fbb1b3b0.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetTriggerType Method

RFmxNRMXSetTriggerType Method

Sets the type of trigger to be used for signal acquisition.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerType(
	string selectorString,
	RFmxNRMXTriggerType value
)
```

```text
Public Function SetTriggerType ( 
	selectorString As String,
	value As RFmxNRMXTriggerType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXTriggerTypeSpecifies the type of trigger to be used for signal acquisition.

###### Return Value

Int32

##### Remarks

TriggerType

None

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/210b8679-9a31-cd81-7e7e-af8b13e36db7.htm language=enus -->
## TOPIC 00049: rfmxnrdotnet/html/210b8679-9a31-cd81-7e7e-af8b13e36db7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/210b8679-9a31-cd81-7e7e-af8b13e36db7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/210b8679-9a31-cd81-7e7e-af8b13e36db7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.ValidateNoiseCalibrationData Method

RFmxNRMXAcpConfigurationValidateNoiseCalibrationData Method

selectorString

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int ValidateNoiseCalibrationData(
	string selectorString,
	out RFmxNRMXAcpNoiseCalibrationDataValid noiseCalibrationDataValid
)
```

```text
Public Function ValidateNoiseCalibrationData ( 
	selectorString As String,
	<OutAttribute> ByRef noiseCalibrationDataValid As RFmxNRMXAcpNoiseCalibrationDataValid
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **noiseCalibrationDataValid**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXAcpNoiseCalibrationDataValid Upon return, contains whether the calibration data is valid.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/21abe3d6-98c3-326e-0a2d-ffe7af417782.htm language=enus -->
## TOPIC 00050: rfmxnrdotnet/html/21abe3d6-98c3-326e-0a2d-ffe7af417782.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/21abe3d6-98c3-326e-0a2d-ffe7af417782.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/21abe3d6-98c3-326e-0a2d-ffe7af417782.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.SetAllTracesEnabled Method

RFmxNRMXChpConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the CHP measurement.

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanSpecifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.

###### Return Value

Int32

##### Remarks

ChpAllTracesEnabled

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/23811443-b6a1-5837-1ae1-8abbaf860640.htm language=enus -->
## TOPIC 00051: rfmxnrdotnet/html/23811443-b6a1-5837-1ae1-8abbaf860640.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/23811443-b6a1-5837-1ae1-8abbaf860640.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/23811443-b6a1-5837-1ae1-8abbaf860640.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpSweepTimeAuto Enumeration

RFmxNRMXAcpSweepTimeAuto Enumeration

Specifies whether the measurement sets the sweep time.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXAcpSweepTimeAuto
```

```text
Public Enumeration RFmxNRMXAcpSweepTimeAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(String, Double) method. |
|  | True | 1 | The measurement uses a sweep time of 1 ms. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/23cc2666-785e-bf89-993d-ef024a92b71f.htm language=enus -->
## TOPIC 00052: rfmxnrdotnet/html/23cc2666-785e-bf89-993d-ef024a92b71f.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/23cc2666-785e-bf89-993d-ef024a92b71f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/23cc2666-785e-bf89-993d-ef024a92b71f.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetSsbPattern Method

RFmxNRMXComponentCarrierSetSsbPattern Method

3GPP TS 38.213

CaseCUpTo3GHz

CaseC3GHzTo6GHz

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSsbPattern(
	string selectorString,
	RFmxNRMXSsbPattern value
)
```

```text
Public Function SetSsbPattern ( 
	selectorString As String,
	value As RFmxNRMXSsbPattern
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXSsbPattern Specifies the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to CaseC3GHzTo6GHz.

###### Return Value

Int32

##### Remarks

SsbPattern

CaseB3GHzTo6GHz

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/29a2aced-4287-5da1-9acf-0080919e9867.htm language=enus -->
## TOPIC 00053: rfmxnrdotnet/html/29a2aced-4287-5da1-9acf-0080919e9867.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/29a2aced-4287-5da1-9acf-0080919e9867.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/29a2aced-4287-5da1-9acf-0080919e9867.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.GetMeasurementOffset Method

RFmxNRMXModAccConfigurationGetMeasurementOffset Method

SetSynchronizationMode(String, RFmxNRMXModAccSynchronizationMode)

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeasurementOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxNRMXModAccSynchronizationMode) method. The unit for this is specified by ModAcc Measurement Length Unit.

###### Return Value

Int32

##### Remarks

ModAccMeasurementOffset

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2a132e58-d632-dead-c024-0092888275b2.htm language=enus -->
## TOPIC 00054: rfmxnrdotnet/html/2a132e58-d632-dead-c024-0092888275b2.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2a132e58-d632-dead-c024-0092888275b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2a132e58-d632-dead-c024-0092888275b2.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXList.DeleteList Method

RFmxNRMXListDeleteList Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int DeleteList()
```

```text
Public Function DeleteList As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXList Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2a3c87b8-fcc5-ca94-f252-659413da1d10.htm language=enus -->
## TOPIC 00055: rfmxnrdotnet/html/2a3c87b8-fcc5-ca94-f252-659413da1d10.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2a3c87b8-fcc5-ca94-f252-659413da1d10.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2a3c87b8-fcc5-ca94-f252-659413da1d10.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetDCSubcarrierRemovalEnabled Method

RFmxNRMXModAccConfigurationSetDCSubcarrierRemovalEnabled Method

Sets whether the DC subcarrier is removed from the EVM results.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDCSubcarrierRemovalEnabled(
	string selectorString,
	RFmxNRMXModAccDCSubcarrierRemovalEnabled value
)
```

```text
Public Function SetDCSubcarrierRemovalEnabled ( 
	selectorString As String,
	value As RFmxNRMXModAccDCSubcarrierRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccDCSubcarrierRemovalEnabledSpecifies whether the DC subcarrier is removed from the EVM results.

###### Return Value

Int32

##### Remarks

ModAccDCSubcarrierRemovalEnabled

True

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2a4b6fd5-ae1e-5161-7fd8-b78e01883aa9.htm language=enus -->
## TOPIC 00056: rfmxnrdotnet/html/2a4b6fd5-ae1e-5161-7fd8-b78e01883aa9.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2a4b6fd5-ae1e-5161-7fd8-b78e01883aa9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2a4b6fd5-ae1e-5161-7fd8-b78e01883aa9.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemResults.GetUpperOffsetMarginAbsolutePower Method

RFmxNRMXSemResultsGetUpperOffsetMarginAbsolutePower Method

Gets the power at which the Margin occurs in the upper (positive) offset segment. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power at which the Margin occurs in the upper (positive) offset segment. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMarginAbsolutePower

##### See Also

###### Reference

RFmxNRMXSemResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2bf61b2f-bc20-5ffc-3bf3-93b874e88473.htm language=enus -->
## TOPIC 00057: rfmxnrdotnet/html/2bf61b2f-bc20-5ffc-3bf3-93b874e88473.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2bf61b2f-bc20-5ffc-3bf3-93b874e88473.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2bf61b2f-bc20-5ffc-3bf3-93b874e88473.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPdcchCceAggregationLevel Method

RFmxNRMXComponentCarrierSetPdcchCceAggregationLevel Method

Sets the CCE aggregation level of PDCCH.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdcchCceAggregationLevel(
	string selectorString,
	int value
)
```

```text
Public Function SetPdcchCceAggregationLevel ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, coreset number and pdcch number. Example: "pdcch0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/pdcch0". You can use the BuildPdcchString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the CCE aggregation level of PDCCH.

###### Return Value

Int32

##### Remarks

PdcchCceAggregationLevel

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2cb1a09a-63b7-17df-8bfd-86fb974ed809.htm language=enus -->
## TOPIC 00058: rfmxnrdotnet/html/2cb1a09a-63b7-17df-8bfd-86fb974ed809.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2cb1a09a-63b7-17df-8bfd-86fb974ed809.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2cb1a09a-63b7-17df-8bfd-86fb974ed809.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetGridSizeMode Method

RFmxNRMXSetGridSizeMode Method

Sets whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetGridSizeMode(
	string selectorString,
	RFmxNRMXGridSizeMode value
)
```

```text
Public Function SetGridSizeMode ( 
	selectorString As String,
	value As RFmxNRMXGridSizeMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXGridSizeModeSpecifies whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually.

###### Return Value

Int32

##### Remarks

GridSizeMode

Auto

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2cefcf88-2c33-a394-6781-12d269ccb88c.htm language=enus -->
## TOPIC 00059: rfmxnrdotnet/html/2cefcf88-2c33-a394-6781-12d269ccb88c.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2cefcf88-2c33-a394-6781-12d269ccb88c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2cefcf88-2c33-a394-6781-12d269ccb88c.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetSubblockEndcNominalSpacingAdjustment Method

RFmxNRMXSetSubblockEndcNominalSpacingAdjustment Method

Sets the adjustment of the center frequency for adjacent E-UTRA and NR Channels in case of nominal spacing. The value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSubblockEndcNominalSpacingAdjustment(
	string selectorString,
	double value
)
```

```text
Public Function SetSubblockEndcNominalSpacingAdjustment ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the adjustment of the center frequency for adjacent E-UTRA and NR Channels in case of nominal spacing. The value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SubblockEndcNominalSpacingAdjustment

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2d769f02-ffcd-e00c-f29b-389915d7275c.htm language=enus -->
## TOPIC 00060: rfmxnrdotnet/html/2d769f02-ffcd-e00c-f29b-389915d7275c.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2d769f02-ffcd-e00c-f29b-389915d7275c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2d769f02-ffcd-e00c-f29b-389915d7275c.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXObwConfiguration.SetSpanAuto Method

RFmxNRMXObwConfigurationSetSpanAuto Method

Sets whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSpanAuto(
	string selectorString,
	RFmxNRMXObwSpanAuto value
)
```

```text
Public Function SetSpanAuto ( 
	selectorString As String,
	value As RFmxNRMXObwSpanAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXObwSpanAutoSpecifies whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user.

###### Return Value

Int32

##### Remarks

ObwSpanAuto

True

##### See Also

###### Reference

RFmxNRMXObwConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/2ec72cb8-669d-93af-e029-426e9c97bfbe.htm language=enus -->
## TOPIC 00061: rfmxnrdotnet/html/2ec72cb8-669d-93af-e029-426e9c97bfbe.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/2ec72cb8-669d-93af-e029-426e9c97bfbe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/2ec72cb8-669d-93af-e029-426e9c97bfbe.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.ComponentCarrier Property

RFmxNRMXSemConfigurationComponentCarrier Property

RFmxNRMXSemComponentCarrierConfiguration

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxNRMXSemComponentCarrierConfiguration ComponentCarrier { get; }
```

```text
Public ReadOnly Property ComponentCarrier As RFmxNRMXSemComponentCarrierConfiguration
	Get
```

###### Property Value

RFmxNRMXSemComponentCarrierConfiguration

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/32e0d4a2-01ce-4eec-be18-7f6bae19e8bd.htm language=enus -->
## TOPIC 00062: rfmxnrdotnet/html/32e0d4a2-01ce-4eec-be18-7f6bae19e8bd.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/32e0d4a2-01ce-4eec-be18-7f6bae19e8bd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/32e0d4a2-01ce-4eec-be18-7f6bae19e8bd.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtResults.GetMeasurementStatus Method

RFmxNRMXPvtResultsGetMeasurementStatus Method

Gets the measurement status indicating whether the off power before and after is within the standard defined limit.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxNRMXPvtMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPvtMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPvtMeasurementStatusUpon return, contains the measurement status indicating whether the off power before and after is within the standard defined limit.

###### Return Value

Int32

##### Remarks

PvtResultsMeasurementStatus

##### See Also

###### Reference

RFmxNRMXPvtResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/34a27a68-f5e1-791b-1843-b32ba82c0081.htm language=enus -->
## TOPIC 00063: rfmxnrdotnet/html/34a27a68-f5e1-791b-1843-b32ba82c0081.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/34a27a68-f5e1-791b-1843-b32ba82c0081.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/34a27a68-f5e1-791b-1843-b32ba82c0081.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.SetRbwFilterAutoBandwidth Method

RFmxNRMXChpConfigurationSetRbwFilterAutoBandwidth Method

Sets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAutoBandwidth(
	string selectorString,
	RFmxNRMXChpRbwAutoBandwidth value
)
```

```text
Public Function SetRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxNRMXChpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXChpRbwAutoBandwidthSpecifies whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

ChpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/34a81f3a-c70f-fe3c-3bdc-7a6c4012728a.htm language=enus -->
## TOPIC 00064: rfmxnrdotnet/html/34a81f3a-c70f-fe3c-3bdc-7a6c4012728a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/34a81f3a-c70f-fe3c-3bdc-7a6c4012728a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/34a81f3a-c70f-fe3c-3bdc-7a6c4012728a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.SetNumberOfAnalysisThreads Method

RFmxNRMXAcpConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the ACP measurement.

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the maximum number of threads used for parallelism for the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/34ae670c-9754-a525-3b15-5c6eab84f4c8.htm language=enus -->
## TOPIC 00065: rfmxnrdotnet/html/34ae670c-9754-a525-3b15-5c6eab84f4c8.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/34ae670c-9754-a525-3b15-5c6eab84f4c8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/34ae670c-9754-a525-3b15-5c6eab84f4c8.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXList.IsDisposed Property

RFmxNRMXListIsDisposed Property

Gets a value that indicates whether the list has been disposed.

Namespace:

NationalInstruments.RFmx.NRMX

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

RFmxNRMXList Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/34ebb6b8-396e-ec7b-62ba-524ef0f1fd00.htm language=enus -->
## TOPIC 00066: rfmxnrdotnet/html/34ebb6b8-396e-ec7b-62ba-524ef0f1fd00.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/34ebb6b8-396e-ec7b-62ba-524ef0f1fd00.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/34ebb6b8-396e-ec7b-62ba-524ef0f1fd00.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetSchDetectedModulationType Method

RFmxNRMXModAccResultsGetSchDetectedModulationType Method

SetAutoResourceBlockDetectionEnabled(String, RFmxNRMXAutoResourceBlockDetectionEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSchDetectedModulationType(
	string selectorString,
	out RFmxNRMXSchDetectedModulationType value
)
```

```text
Public Function GetSchDetectedModulationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXSchDetectedModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXSchDetectedModulationType Upon return, contains the modulation of the shared channel user data if you set the SetAutoResourceBlockDetectionEnabled(String, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True; otherwise, returns the configured modulation of the shared user data. In case of downlink test model, the modulation type specified by the 3GPP standard is returned.

###### Return Value

Int32

##### Remarks

ModAccResultsSchDetectedModulationType

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/39036e45-9970-73ed-d986-d1c067aab36f.htm language=enus -->
## TOPIC 00067: rfmxnrdotnet/html/39036e45-9970-73ed-d986-d1c067aab36f.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/39036e45-9970-73ed-d986-d1c067aab36f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/39036e45-9970-73ed-d986-d1c067aab36f.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetAutoIncrementCellIDEnabled Method

RFmxNRMXSetAutoIncrementCellIDEnabled Method

Sets whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoIncrementCellIDEnabled(
	string selectorString,
	RFmxNRMXAutoIncrementCellIDEnabled value
)
```

```text
Public Function SetAutoIncrementCellIDEnabled ( 
	selectorString As String,
	value As RFmxNRMXAutoIncrementCellIDEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXAutoIncrementCellIDEnabledSpecifies whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user.

###### Return Value

Int32

##### Remarks

AutoIncrementCellIDEnabled

False

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/397c1547-5616-ca26-be7a-e5b7d8e11c0d.htm language=enus -->
## TOPIC 00068: rfmxnrdotnet/html/397c1547-5616-ca26-be7a-e5b7d8e11c0d.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/397c1547-5616-ca26-be7a-e5b7d8e11c0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/397c1547-5616-ca26-be7a-e5b7d8e11c0d.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXTxp.Configuration Property

RFmxNRMXTxpConfiguration Property

RFmxNRMXTxpConfiguration

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxNRMXTxpConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxNRMXTxpConfiguration
	Get
```

###### Property Value

RFmxNRMXTxpConfiguration

##### See Also

###### Reference

RFmxNRMXTxp Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/40246202-7e41-2a45-428b-66ac808cf5f1.htm language=enus -->
## TOPIC 00069: rfmxnrdotnet/html/40246202-7e41-2a45-428b-66ac808cf5f1.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/40246202-7e41-2a45-428b-66ac808cf5f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/40246202-7e41-2a45-428b-66ac808cf5f1.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.LoadFromGenerationConfigurationFile Method

RFmxNRMXLoadFromGenerationConfigurationFile Method

Loads the attributes saved in an RFWS/TDMS file onto the RFmx session. This file can be saved using the NR Modulation Scheme in RFmx Waveform Creator. Make sure to select the 'store configuration' option while saving the TDMS file.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int LoadFromGenerationConfigurationFile(
	string selectorString,
	string filePath,
	int configurationIndex
)
```

```text
Public Function LoadFromGenerationConfigurationFile ( 
	selectorString As String,
	filePath As String,
	configurationIndex As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **filePath**
  - Type: SystemStringSpecifies the complete path to the RFWS/TDMS file from which the configurations are to be loaded.
- **configurationIndex**
  - Type: SystemInt32Specifies the index of the carrier set to be loaded from the RFWS/TDMS file.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/4049c1b5-6c37-6127-5138-3830aba5a328.htm language=enus -->
## TOPIC 00070: rfmxnrdotnet/html/4049c1b5-6c37-6127-5138-3830aba5a328.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/4049c1b5-6c37-6127-5138-3830aba5a328.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/4049c1b5-6c37-6127-5138-3830aba5a328.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXList.SetNumberOfSteps Method

RFmxNRMXListSetNumberOfSteps Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfSteps(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfSteps ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Pass an empty string. The list name that is passed when creating the list is used.
- **value**
  - Type: SystemInt32Upon return, contains the number of list step instances in a list.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXList Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/42406d6a-8ac3-41e6-b89c-8f3bd4c2c597.htm language=enus -->
## TOPIC 00071: rfmxnrdotnet/html/42406d6a-8ac3-41e6-b89c-8f3bd4c2c597.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/42406d6a-8ac3-41e6-b89c-8f3bd4c2c597.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/42406d6a-8ac3-41e6-b89c-8f3bd4c2c597.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPuschPtrsAntennaPorts Method

RFmxNRMXComponentCarrierSetPuschPtrsAntennaPorts Method

SetPuschPtrsEnabled(String, RFmxNRMXPuschPtrsEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschPtrsAntennaPorts(
	string selectorString,
	string value
)
```

```text
Public Function SetPuschPtrsAntennaPorts ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemString Specifies the DMRS antenna ports associated with PTRS transmission. This method is valid only if you set the SetPuschPtrsEnabled(String, RFmxNRMXPuschPtrsEnabled) method to True.

###### Return Value

Int32

##### Remarks

PuschPtrsAntennaPorts

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/425e212c-aee7-4bc7-23b3-11cd85b6c2aa.htm language=enus -->
## TOPIC 00072: rfmxnrdotnet/html/425e212c-aee7-4bc7-23b3-11cd85b6c2aa.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/425e212c-aee7-4bc7-23b3-11cd85b6c2aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/425e212c-aee7-4bc7-23b3-11cd85b6c2aa.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetNumberOfBandwidthParts Method

RFmxNRMXComponentCarrierGetNumberOfBandwidthParts Method

Gets the number of bandwidth parts present in the component carrier.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfBandwidthParts(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfBandwidthParts ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of bandwidth parts present in the component carrier.

###### Return Value

Int32

##### Remarks

NumberOfBandwidthParts

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/426b0c97-3ae4-6712-df24-ea9dd663a43d.htm language=enus -->
## TOPIC 00073: rfmxnrdotnet/html/426b0c97-3ae4-6712-df24-ea9dd663a43d.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/426b0c97-3ae4-6712-df24-ea9dd663a43d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/426b0c97-3ae4-6712-df24-ea9dd663a43d.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXList.ListType Property

RFmxNRMXListListType Property

Type

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public Type ListType { get; }
```

```text
Public ReadOnly Property ListType As Type
	Get
```

###### Property Value

Type

###### Implements

IList.ListType

##### See Also

###### Reference

RFmxNRMXList Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/429e96d4-973b-9a36-fcc5-1140b45c595c.htm language=enus -->
## TOPIC 00074: rfmxnrdotnet/html/429e96d4-973b-9a36-fcc5-1140b45c595c.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/429e96d4-973b-9a36-fcc5-1140b45c595c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/429e96d4-973b-9a36-fcc5-1140b45c595c.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetSpectralFlatnessRange2MinimumSubcarrierIndex Method

RFmxNRMXModAccResultsGetSpectralFlatnessRange2MinimumSubcarrierIndex Method

3GPP 38.101-1

3GPP 38.101-2

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectralFlatnessRange2MinimumSubcarrierIndex(
	string selectorString,
	out int value
)
```

```text
Public Function GetSpectralFlatnessRange2MinimumSubcarrierIndex ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the minimum subcarrier index magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification.

###### Return Value

Int32

##### Remarks

ModAccResultsSpectralFlatnessRange2MinimumSubcarrierIndex

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/42cab648-b7de-b357-ba88-7d5f5275aec7.htm language=enus -->
## TOPIC 00075: rfmxnrdotnet/html/42cab648-b7de-b357-ba88-7d5f5275aec7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/42cab648-b7de-b357-ba88-7d5f5275aec7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/42cab648-b7de-b357-ba88-7d5f5275aec7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.GetExternalAttenuation Method

RFmxNRMXGetExternalAttenuation Method

NI RF Vector Signal Analyzers Help

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetExternalAttenuation(
	string selectorString,
	out double value
)
```

```text
Public Function GetExternalAttenuation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help.

###### Return Value

Int32

##### Remarks

ExternalAttenuation

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/42d0169d-4e1e-1a79-e128-86aa12fd591f.htm language=enus -->
## TOPIC 00076: rfmxnrdotnet/html/42d0169d-4e1e-1a79-e128-86aa12fd591f.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/42d0169d-4e1e-1a79-e128-86aa12fd591f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/42d0169d-4e1e-1a79-e128-86aa12fd591f.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.GetIQPowerEdgeTriggerSlope Method

RFmxNRMXGetIQPowerEdgeTriggerSlope Method

Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerSlope(
	string selectorString,
	out RFmxNRMXIQPowerEdgeTriggerSlope value
)
```

```text
Public Function GetIQPowerEdgeTriggerSlope ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXIQPowerEdgeTriggerSlope
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXIQPowerEdgeTriggerSlopeUpon return, contains whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSlope

Rising

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/42f42249-2430-94a5-ea41-7d88087561ea.htm language=enus -->
## TOPIC 00077: rfmxnrdotnet/html/42f42249-2430-94a5-ea41-7d88087561ea.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/42f42249-2430-94a5-ea41-7d88087561ea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/42f42249-2430-94a5-ea41-7d88087561ea.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemResults.FetchUpperOffsetPower Method

RFmxNRMXSemResultsFetchUpperOffsetPower Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUpperOffsetPower(
	string selectorString,
	double timeout,
	out double totalAbsolutePower,
	out double totalRelativePower,
	out double peakAbsolutePower,
	out double peakFrequency,
	out double peakRelativePower
)
```

```text
Public Function FetchUpperOffsetPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef totalAbsolutePower As Double,
	<OutAttribute> ByRef totalRelativePower As Double,
	<OutAttribute> ByRef peakAbsolutePower As Double,
	<OutAttribute> ByRef peakFrequency As Double,
	<OutAttribute> ByRef peakRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, carrier number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **totalAbsolutePower**
  - Type: SystemDouble Upon return, contains the upper (positive) offset segment power. This value is expressed in dBm.
- **totalRelativePower**
  - Type: SystemDouble Upon return, contains the power in the upper offset segment relative to total aggregated power. This value is expressed in dB.
- **peakAbsolutePower**
  - Type: SystemDouble Upon return, contains the peak power in the upper offset segment. This value is expressed in dBm.
- **peakFrequency**
  - Type: SystemDouble Upon return, contains the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz.
- **peakRelativePower**
  - Type: SystemDouble Upon return, contains the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXSemResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/4427cc0c-1cc0-618b-11bc-8c8224067720.htm language=enus -->
## TOPIC 00078: rfmxnrdotnet/html/4427cc0c-1cc0-618b-11bc-8c8224067720.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/4427cc0c-1cc0-618b-11bc-8c8224067720.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/4427cc0c-1cc0-618b-11bc-8c8224067720.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetTransientPowerChangeThreshold Method

RFmxNRMXModAccConfigurationSetTransientPowerChangeThreshold Method

Sets transient period power change threshold level in dB.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTransientPowerChangeThreshold(
	string selectorString,
	double value
)
```

```text
Public Function SetTransientPowerChangeThreshold ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies transient period power change threshold level in dB.

###### Return Value

Int32

##### Remarks

ModAccTransientPowerChangeThreshold

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/448aa6b1-787a-5e37-199f-8f19c098fcde.htm language=enus -->
## TOPIC 00079: rfmxnrdotnet/html/448aa6b1-787a-5e37-199f-8f19c098fcde.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/448aa6b1-787a-5e37-199f-8f19c098fcde.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/448aa6b1-787a-5e37-199f-8f19c098fcde.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPuschPtrsPower Method

RFmxNRMXComponentCarrierSetPuschPtrsPower Method

SetPuschPtrsEnabled(String, RFmxNRMXPuschPtrsEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschPtrsPower(
	string selectorString,
	double value
)
```

```text
Public Function SetPuschPtrsPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Specifies the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This method is valid only if you set the SetPuschPtrsEnabled(String, RFmxNRMXPuschPtrsEnabled) method to True.

###### Return Value

Int32

##### Remarks

PuschPtrsPower

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/44dc4eb0-28a5-fb5c-5658-45d8e18e76c3.htm language=enus -->
## TOPIC 00080: rfmxnrdotnet/html/44dc4eb0-28a5-fb5c-5658-45d8e18e76c3.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/44dc4eb0-28a5-fb5c-5658-45d8e18e76c3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/44dc4eb0-28a5-fb5c-5658-45d8e18e76c3.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.GetAutoIncrementCellIDEnabled Method

RFmxNRMXGetAutoIncrementCellIDEnabled Method

Gets whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoIncrementCellIDEnabled(
	string selectorString,
	out RFmxNRMXAutoIncrementCellIDEnabled value
)
```

```text
Public Function GetAutoIncrementCellIDEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXAutoIncrementCellIDEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXAutoIncrementCellIDEnabledUpon return, contains whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user.

###### Return Value

Int32

##### Remarks

AutoIncrementCellIDEnabled

False

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/4657d2e5-c348-f069-f74e-3efcc629543d.htm language=enus -->
## TOPIC 00081: rfmxnrdotnet/html/4657d2e5-c348-f069-f74e-3efcc629543d.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/4657d2e5-c348-f069-f74e-3efcc629543d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/4657d2e5-c348-f069-f74e-3efcc629543d.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.BuildSubblockString Method

RFmxNRMXBuildSubblockString Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildSubblockString(
	string selectorString,
	int subblockNumber
)
```

```text
Public Shared Function BuildSubblockString ( 
	selectorString As String,
	subblockNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **subblockNumber**
  - Type: SystemInt32 Specifies the number of subblocks that are configured in the non-contiguous carrier aggregation. Set this parameter to 1, which is the default, for single carrier and intra-band contiguous carrier aggregation.

###### Return Value

String

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/48c286f9-ee2d-132a-309c-ac4432ea7281.htm language=enus -->
## TOPIC 00082: rfmxnrdotnet/html/48c286f9-ee2d-132a-309c-ac4432ea7281.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/48c286f9-ee2d-132a-309c-ac4432ea7281.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/48c286f9-ee2d-132a-309c-ac4432ea7281.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPuschMappingType Enumeration

RFmxNRMXPuschMappingType Enumeration

Specifies the mapping type of DMRS.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXPuschMappingType
```

```text
Public Enumeration RFmxNRMXPuschMappingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TypeA | 0 | The first DMRS symbol index in a slot is either 2 or 3 based on SetPuschDmrsTypeAPosition(String, Int32) method. |
|  | TypeB | 1 | The first DMRS symbol index in a slot is the first active PUSCH symbol. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/48cd9fa6-f84d-5c3b-37ea-f5135be5bfcc.htm language=enus -->
## TOPIC 00083: rfmxnrdotnet/html/48cd9fa6-f84d-5c3b-37ea-f5135be5bfcc.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/48cd9fa6-f84d-5c3b-37ea-f5135be5bfcc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/48cd9fa6-f84d-5c3b-37ea-f5135be5bfcc.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetAttributeSbyte Method

RFmxNRMXSetAttributeSbyte Method

Sets the value of a Sbyte attribute.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeSbyte(
	string selectorString,
	int attributeIdentifier,
	sbyte value
)
```

```text
Public Function SetAttributeSbyte ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As SByte
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx NR Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemSByteSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/49862278-b389-0ddf-759c-1186a842d5ff.htm language=enus -->
## TOPIC 00084: rfmxnrdotnet/html/49862278-b389-0ddf-759c-1186a842d5ff.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/49862278-b389-0ddf-759c-1186a842d5ff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/49862278-b389-0ddf-759c-1186a842d5ff.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.GetCenterFrequency Method

RFmxNRMXGetCenterFrequency Method

Gets the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute or relative to first subblock's center frequency. All component carrier frequencies within the subblock are defined with respect to this frequency.

Namespace:

NationalInstruments.RFmx.NRMX

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
  - Type: SystemString Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute or relative to first subblock's center frequency. All component carrier frequencies within the subblock are defined with respect to this frequency.

###### Return Value

Int32

##### Remarks

CenterFrequency

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/49a6006a-02d9-10df-1062-40b192c6d893.htm language=enus -->
## TOPIC 00085: rfmxnrdotnet/html/49a6006a-02d9-10df-1062-40b192c6d893.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/49a6006a-02d9-10df-1062-40b192c6d893.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/49a6006a-02d9-10df-1062-40b192c6d893.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPuschDmrsPuschIDMode Enumeration

RFmxNRMXPuschDmrsPuschIDMode Enumeration

SetCellID(String, Int32)

SetPuschTransformPrecodingEnabled(String, RFmxNRMXPuschTransformPrecodingEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXPuschDmrsPuschIDMode
```

```text
Public Enumeration RFmxNRMXPuschDmrsPuschIDMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | CellID | 0 | The value of PUSCH DMRS PUSCH ID is based on Cell ID method. |
|  | UserDefined | 1 | The value of PUSCH DMRS PUSCH ID is specified by you. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/4b17e881-8731-16c9-22ab-df5b413fff6a.htm language=enus -->
## TOPIC 00086: rfmxnrdotnet/html/4b17e881-8731-16c9-22ab-df5b413fff6a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/4b17e881-8731-16c9-22ab-df5b413fff6a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/4b17e881-8731-16c9-22ab-df5b413fff6a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.GetOffsetRbwFilterType Method

RFmxNRMXSemConfigurationGetOffsetRbwFilterType Method

Gets the shape of a digital RBW filter.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRbwFilterType(
	string selectorString,
	out RFmxNRMXSemOffsetRbwFilterType value
)
```

```text
Public Function GetOffsetRbwFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXSemOffsetRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXSemOffsetRbwFilterTypeUpon return, contains the shape of a digital RBW filter.

###### Return Value

Int32

##### Remarks

SemOffsetRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/4e3c772a-6756-5084-5b22-8430c5b97c11.htm language=enus -->
## TOPIC 00087: rfmxnrdotnet/html/4e3c772a-6756-5084-5b22-8430c5b97c11.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/4e3c772a-6756-5084-5b22-8430c5b97c11.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/4e3c772a-6756-5084-5b22-8430c5b97c11.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtConfiguration.GetAveragingType Method

RFmxNRMXPvtConfigurationGetAveragingType Method

Gets the measurement averaging type.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingType(
	string selectorString,
	out RFmxNRMXPvtAveragingType value
)
```

```text
Public Function GetAveragingType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPvtAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPvtAveragingTypeUpon return, contains the measurement averaging type.

###### Return Value

Int32

##### Remarks

PvtAveragingType

Rms

##### See Also

###### Reference

RFmxNRMXPvtConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/4ed387a7-51ed-388b-08e8-8c718c97d9f8.htm language=enus -->
## TOPIC 00088: rfmxnrdotnet/html/4ed387a7-51ed-388b-08e8-8c718c97d9f8.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/4ed387a7-51ed-388b-08e8-8c718c97d9f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/4ed387a7-51ed-388b-08e8-8c718c97d9f8.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPbchDataConstellationTrace Method

RFmxNRMXModAccResultsFetchPbchDataConstellationTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPbchDataConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] pbchDataConstellation
)
```

```text
Public Function FetchPbchDataConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef pbchDataConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **pbchDataConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the PBCH data trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/505af223-697f-d6fa-2c1c-b5d135042c6a.htm language=enus -->
## TOPIC 00089: rfmxnrdotnet/html/505af223-697f-d6fa-2c1c-b5d135042c6a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/505af223-697f-d6fa-2c1c-b5d135042c6a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/505af223-697f-d6fa-2c1c-b5d135042c6a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPdschPtrsPower Method

RFmxNRMXComponentCarrierSetPdschPtrsPower Method

SetPdschPtrsPowerMode(String, RFmxNRMXPdschPtrsPowerMode)

UserDefined

Standard

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdschPtrsPower(
	string selectorString,
	double value
)
```

```text
Public Function SetPdschPtrsPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Specifies the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this method is taken as an input when you set the SetPdschPtrsPowerMode(String, RFmxNRMXPdschPtrsPowerMode) method to UserDefined. If you set the PDSCH PTRS Pwr Mode method to Standard, the value is computed from other parameters.

###### Return Value

Int32

##### Remarks

PdschPtrsPower

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/520df076-954c-c0aa-e0ad-1538cdf85fb1.htm language=enus -->
## TOPIC 00090: rfmxnrdotnet/html/520df076-954c-c0aa-e0ad-1538cdf85fb1.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/520df076-954c-c0aa-e0ad-1538cdf85fb1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/520df076-954c-c0aa-e0ad-1538cdf85fb1.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPuschDmrsGroupHoppingEnabled Enumeration

RFmxNRMXPuschDmrsGroupHoppingEnabled Enumeration

SetPuschTransformPrecodingEnabled(String, RFmxNRMXPuschTransformPrecodingEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXPuschDmrsGroupHoppingEnabled
```

```text
Public Enumeration RFmxNRMXPuschDmrsGroupHoppingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Group hopping is disabled. |
|  | True | 1 | Group hopping is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/526a464d-6c4e-c9ac-d2e6-03c455f81245.htm language=enus -->
## TOPIC 00091: rfmxnrdotnet/html/526a464d-6c4e-c9ac-d2e6-03c455f81245.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/526a464d-6c4e-c9ac-d2e6-03c455f81245.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/526a464d-6c4e-c9ac-d2e6-03c455f81245.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.GetShortFrameLengthUnit Method

RFmxNRMXModAccConfigurationGetShortFrameLengthUnit Method

Gets the units in which Short Frame Length is specified.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetShortFrameLengthUnit(
	string selectorString,
	out RFmxNRMXModAccShortFrameLengthUnit value
)
```

```text
Public Function GetShortFrameLengthUnit ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXModAccShortFrameLengthUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccShortFrameLengthUnitUpon return, contains the units in which Short Frame Length is specified.

###### Return Value

Int32

##### Remarks

ModAccShortFrameLengthUnit

Time

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/5363066d-46a7-d90e-6b9c-0ca813664e1b.htm language=enus -->
## TOPIC 00092: rfmxnrdotnet/html/5363066d-46a7-d90e-6b9c-0ca813664e1b.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/5363066d-46a7-d90e-6b9c-0ca813664e1b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/5363066d-46a7-d90e-6b9c-0ca813664e1b.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpChannelConfigurationType Enumeration

RFmxNRMXAcpChannelConfigurationType Enumeration

Specifies the method to configure the carrier and the offset channel settings.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXAcpChannelConfigurationType
```

```text
Public Enumeration RFmxNRMXAcpChannelConfigurationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Standard | 0 | All settings will be 3GPP compliant. |
|  | Custom | 1 | The user can manually configure integration bandwidth and offset frequencies for the ACP measurement. |
|  | NS_29 | 2 | This is an additional requirement according to section 6.5F.2.4.2 of 3GPP 38.101-1 and is applicable only for uplink bandwidths of 20 MHz and 40 MHz. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/536b76f3-6c03-cdfb-222f-4b63740ea507.htm language=enus -->
## TOPIC 00093: rfmxnrdotnet/html/536b76f3-6c03-cdfb-222f-4b63740ea507.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/536b76f3-6c03-cdfb-222f-4b63740ea507.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/536b76f3-6c03-cdfb-222f-4b63740ea507.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.ComponentCarrier Property

RFmxNRMXChpConfigurationComponentCarrier Property

RFmxNRMXChpComponentCarrierConfiguration

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxNRMXChpComponentCarrierConfiguration ComponentCarrier { get; }
```

```text
Public ReadOnly Property ComponentCarrier As RFmxNRMXChpComponentCarrierConfiguration
	Get
```

###### Property Value

RFmxNRMXChpComponentCarrierConfiguration

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/53e03108-f445-4f6d-f1f0-3b06f0eb9c38.htm language=enus -->
## TOPIC 00094: rfmxnrdotnet/html/53e03108-f445-4f6d-f1f0-3b06f0eb9c38.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/53e03108-f445-4f6d-f1f0-3b06f0eb9c38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/53e03108-f445-4f6d-f1f0-3b06f0eb9c38.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccIQImpairmentsModel Enumeration

RFmxNRMXModAccIQImpairmentsModel Enumeration

Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXModAccIQImpairmentsModel
```

```text
Public Enumeration RFmxNRMXModAccIQImpairmentsModel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Tx | 0 | The measurement assumes that the I/Q impairments are introduced by a transmit DUT. |
|  | Rx | 1 | The measurement assumes that the I/Q impairments are introduced by a receive DUT. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/54021e3b-91e0-1816-d8bd-46f3ea6d66d1.htm language=enus -->
## TOPIC 00095: rfmxnrdotnet/html/54021e3b-91e0-1816-d8bd-46f3ea6d66d1.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/54021e3b-91e0-1816-d8bd-46f3ea6d66d1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/54021e3b-91e0-1816-d8bd-46f3ea6d66d1.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetDetectedCellID Method

RFmxNRMXModAccResultsGetDetectedCellID Method

SetAutoCellIDDetectionEnabled(String, RFmxNRMXAutoCellIDDetectionEnabled)

True

False

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectedCellID(
	string selectorString,
	out int value
)
```

```text
Public Function GetDetectedCellID ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the detected Cell ID, if the SetAutoCellIDDetectionEnabled(String, RFmxNRMXAutoCellIDDetectionEnabled) method is set to True. A value of -1 is returned, if the measurement fails to auto detect the Cell ID.Upon return, contains the user configured Cell ID, if the Auto Cell ID Detection Enabled method is set to False.

###### Return Value

Int32

##### Remarks

ModAccResultsDetectedCellID

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/54a73a51-c074-a8eb-d03f-9bb8dcd5c2ba.htm language=enus -->
## TOPIC 00096: rfmxnrdotnet/html/54a73a51-c074-a8eb-d03f-9bb8dcd5c2ba.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/54a73a51-c074-a8eb-d03f-9bb8dcd5c2ba.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/54a73a51-c074-a8eb-d03f-9bb8dcd5c2ba.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.SetAmplitudeCorrectionType Method

RFmxNRMXChpConfigurationSetAmplitudeCorrectionType Method

Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAmplitudeCorrectionType(
	string selectorString,
	RFmxNRMXChpAmplitudeCorrectionType value
)
```

```text
Public Function SetAmplitudeCorrectionType ( 
	selectorString As String,
	value As RFmxNRMXChpAmplitudeCorrectionType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXChpAmplitudeCorrectionTypeSpecifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

###### Return Value

Int32

##### Remarks

ChpAmplitudeCorrectionType

RFCenterFrequency

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/56a87ae1-4546-37c7-8aa7-c8edb93cd87c.htm language=enus -->
## TOPIC 00097: rfmxnrdotnet/html/56a87ae1-4546-37c7-8aa7-c8edb93cd87c.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/56a87ae1-4546-37c7-8aa7-c8edb93cd87c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/56a87ae1-4546-37c7-8aa7-c8edb93cd87c.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.GetNumberOfUtraOffsets Method

RFmxNRMXAcpConfigurationGetNumberOfUtraOffsets Method

Gets the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions. For uplink ACP measurement in frequency range 2, and for downlink ACP measurement, the ACP Num UTRA Offsets has to be 0.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfUtraOffsets(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfUtraOffsets ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions. For uplink ACP measurement in frequency range 2, and for downlink ACP measurement, the ACP Num UTRA Offsets has to be 0.

###### Return Value

Int32

##### Remarks

AcpNumberOfUtraOffsets

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/5c5859fb-e9aa-e2fd-f179-7bd2278ea981.htm language=enus -->
## TOPIC 00098: rfmxnrdotnet/html/5c5859fb-e9aa-e2fd-f179-7bd2278ea981.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/5c5859fb-e9aa-e2fd-f179-7bd2278ea981.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/5c5859fb-e9aa-e2fd-f179-7bd2278ea981.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemResults.GetLowerOffsetAbsolutePeakPower Method

RFmxNRMXSemResultsGetLowerOffsetAbsolutePeakPower Method

Gets the peak power in the lower (negative) offset segment. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power in the lower (negative) offset segment. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetAbsolutePeakPower

##### See Also

###### Reference

RFmxNRMXSemResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/5cb26b42-74b9-b1a3-9150-69d7fac2f345.htm language=enus -->
## TOPIC 00099: rfmxnrdotnet/html/5cb26b42-74b9-b1a3-9150-69d7fac2f345.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/5cb26b42-74b9-b1a3-9150-69d7fac2f345.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/5cb26b42-74b9-b1a3-9150-69d7fac2f345.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPuschDmrsConfigurationType Method

RFmxNRMXComponentCarrierGetPuschDmrsConfigurationType Method

Gets the configuration type of DMRS.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschDmrsConfigurationType(
	string selectorString,
	out RFmxNRMXPuschDmrsConfigurationType value
)
```

```text
Public Function GetPuschDmrsConfigurationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPuschDmrsConfigurationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPuschDmrsConfigurationTypeUpon return, contains the configuration type of DMRS.

###### Return Value

Int32

##### Remarks

PuschDmrsConfigurationType

Type1

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/5d18b2da-b793-1a88-fd3e-80c0eb9cc7eb.htm language=enus -->
## TOPIC 00100: rfmxnrdotnet/html/5d18b2da-b793-1a88-fd3e-80c0eb9cc7eb.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/5d18b2da-b793-1a88-fd3e-80c0eb9cc7eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/5d18b2da-b793-1a88-fd3e-80c0eb9cc7eb.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXObwConfiguration.GetFftWindow Method

RFmxNRMXObwConfigurationGetFftWindow Method

Gets the FFT window type to be used to reduce spectral leakage.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftWindow(
	string selectorString,
	out RFmxNRMXObwFftWindow value
)
```

```text
Public Function GetFftWindow ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXObwFftWindow
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXObwFftWindowUpon return, contains the FFT window type to be used to reduce spectral leakage.

###### Return Value

Int32

##### Remarks

ObwFftWindow

FlatTop

##### See Also

###### Reference

RFmxNRMXObwConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/5f699c77-9be8-1e3a-1b03-0dd8c6c9b2ec.htm language=enus -->
## TOPIC 00101: rfmxnrdotnet/html/5f699c77-9be8-1e3a-1b03-0dd8c6c9b2ec.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/5f699c77-9be8-1e3a-1b03-0dd8c6c9b2ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/5f699c77-9be8-1e3a-1b03-0dd8c6c9b2ec.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPdcchSlotAllocation Method

RFmxNRMXComponentCarrierSetPdcchSlotAllocation Method

Sets the slot allocation in NR frame. This defines the indices of the allocated slots.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdcchSlotAllocation(
	string selectorString,
	string value
)
```

```text
Public Function SetPdcchSlotAllocation ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, coreset number and pdcch number. Example: "pdcch0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/pdcch0". You can use the BuildPdcchString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemStringSpecifies the slot allocation in NR frame. This defines the indices of the allocated slots.

###### Return Value

Int32

##### Remarks

PdcchSlotAllocation

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/5f706773-8a1c-ad12-22ea-90d154335918.htm language=enus -->
## TOPIC 00102: rfmxnrdotnet/html/5f706773-8a1c-ad12-22ea-90d154335918.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/5f706773-8a1c-ad12-22ea-90d154335918.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/5f706773-8a1c-ad12-22ea-90d154335918.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.GetNoiseCompensationType Method

RFmxNRMXAcpConfigurationGetNoiseCompensationType Method

Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCompensationType(
	string selectorString,
	out RFmxNRMXAcpNoiseCompensationType value
)
```

```text
Public Function GetNoiseCompensationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXAcpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXAcpNoiseCompensationTypeUpon return, contains the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

AcpNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/6042bfd2-ca94-2cc3-60cb-a9af96ac6d6e.htm language=enus -->
## TOPIC 00103: rfmxnrdotnet/html/6042bfd2-ca94-2cc3-60cb-a9af96ac6d6e.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/6042bfd2-ca94-2cc3-60cb-a9af96ac6d6e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/6042bfd2-ca94-2cc3-60cb-a9af96ac6d6e.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPdschPtrsEnabled Enumeration

RFmxNRMXPdschPtrsEnabled Enumeration

Specifies whether PT-RS is present in the transmitted signal.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXPdschPtrsEnabled
```

```text
Public Enumeration RFmxNRMXPdschPtrsEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Detection of PTRS in the transmitted signal is disabled. |
|  | True | 1 | Detection of PTRS in the transmitted signal is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/60bc8f30-6e32-a4f2-e244-0c36343b7582.htm language=enus -->
## TOPIC 00104: rfmxnrdotnet/html/60bc8f30-6e32-a4f2-e244-0c36343b7582.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/60bc8f30-6e32-a4f2-e244-0c36343b7582.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/60bc8f30-6e32-a4f2-e244-0c36343b7582.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetRatedTrp Method

RFmxNRMXComponentCarrierSetRatedTrp Method

Sets the rated carrier TRP output power. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRatedTrp(
	string selectorString,
	double value
)
```

```text
Public Function SetRatedTrp ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the rated carrier TRP output power. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

RatedTrp

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/62fbdf9d-c002-95a2-3363-05ee656296b2.htm language=enus -->
## TOPIC 00105: rfmxnrdotnet/html/62fbdf9d-c002-95a2-3363-05ee656296b2.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/62fbdf9d-c002-95a2-3363-05ee656296b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/62fbdf9d-c002-95a2-3363-05ee656296b2.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPdschDmrsReleaseVersion Method

RFmxNRMXComponentCarrierGetPdschDmrsReleaseVersion Method

Gets the 3GGP release version for PDSCH DMRS.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschDmrsReleaseVersion(
	string selectorString,
	out RFmxNRMXPdschDmrsReleaseVersion value
)
```

```text
Public Function GetPdschDmrsReleaseVersion ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPdschDmrsReleaseVersion
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPdschDmrsReleaseVersionUpon return, contains the 3GGP release version for PDSCH DMRS.

###### Return Value

Int32

##### Remarks

PdschDmrsReleaseVersion

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/6308ae4b-69c5-4d87-84e7-6a4c77184283.htm language=enus -->
## TOPIC 00106: rfmxnrdotnet/html/6308ae4b-69c5-4d87-84e7-6a4c77184283.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/6308ae4b-69c5-4d87-84e7-6a4c77184283.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/6308ae4b-69c5-4d87-84e7-6a4c77184283.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.SetAveragingType Method

RFmxNRMXChpConfigurationSetAveragingType Method

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxNRMXChpAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxNRMXChpAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXChpAveragingTypeSpecifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

###### Return Value

Int32

##### Remarks

ChpAveragingType

Rms

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/630d2e60-9eb6-22d2-692a-95356e694bbc.htm language=enus -->
## TOPIC 00107: rfmxnrdotnet/html/630d2e60-9eb6-22d2-692a-95356e694bbc.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/630d2e60-9eb6-22d2-692a-95356e694bbc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/630d2e60-9eb6-22d2-692a-95356e694bbc.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXExtension.GetNRSignalConfiguration Method (RFmxInstrMX)

RFmxNRMXExtensionGetNRSignalConfiguration Method (RFmxInstrMX)

Creates a new default NR signal configuration if it doesn't exist; otherwise, it returns the
 existing default NR signal configuration.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxNRMX GetNRSignalConfiguration(
	this RFmxInstrMX instrSession
)
```

```text
<ExtensionAttribute>
Public Shared Function GetNRSignalConfiguration ( 
	instrSession As RFmxInstrMX
) As RFmxNRMX
```

###### Parameters

- **instrSession**
  - Type: RFmxInstrMXSpecifies an instr session.

###### Return Value

RFmxNRMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxNRMXExtension Class

GetNRSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/632f707f-7219-454e-96f5-29330bc08661.htm language=enus -->
## TOPIC 00108: rfmxnrdotnet/html/632f707f-7219-454e-96f5-29330bc08661.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/632f707f-7219-454e-96f5-29330bc08661.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/632f707f-7219-454e-96f5-29330bc08661.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetPuschNumberOfResourceBlocks Method

RFmxNRMXComponentCarrierGetPuschNumberOfResourceBlocks Method

SetAutoResourceBlockDetectionEnabled(String, RFmxNRMXAutoResourceBlockDetectionEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschNumberOfResourceBlocks(
	string selectorString,
	out int value
)
```

```text
Public Function GetPuschNumberOfResourceBlocks ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number, pusch number and puschcluster number. Example: "puschcluster0" or "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0/puschcluster0". You can use the BuildPuschClusterString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(String, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True.

###### Return Value

Int32

##### Remarks

PuschNumberOfResourceBlocks

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/63496d41-9a28-7b2f-d0d8-576005196317.htm language=enus -->
## TOPIC 00109: rfmxnrdotnet/html/63496d41-9a28-7b2f-d0d8-576005196317.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/63496d41-9a28-7b2f-d0d8-576005196317.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/63496d41-9a28-7b2f-d0d8-576005196317.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpConfiguration.SetAveragingCount Method

RFmxNRMXChpConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxNRMXChpAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxNRMXChpAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ChpAveragingCount

##### See Also

###### Reference

RFmxNRMXChpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/7840922e-c69f-c1b1-1b5f-7f2c0304f18e.htm language=enus -->
## TOPIC 00110: rfmxnrdotnet/html/7840922e-c69f-c1b1-1b5f-7f2c0304f18e.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/7840922e-c69f-c1b1-1b5f-7f2c0304f18e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/7840922e-c69f-c1b1-1b5f-7f2c0304f18e.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetCoresetResourceBlockOffset Method

RFmxNRMXComponentCarrierSetCoresetResourceBlockOffset Method

Sets the starting resource block of a CORESET cluster.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCoresetResourceBlockOffset(
	string selectorString,
	int value
)
```

```text
Public Function SetCoresetResourceBlockOffset ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, coreset number and coresetcluster number. Example: "coresetcluster0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/coresetcluster0". You can use the BuildCoresetClusterString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the starting resource block of a CORESET cluster.

###### Return Value

Int32

##### Remarks

CoresetResourceBlockOffset

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/7b729eb7-92ad-12c2-7bfe-3f49321d9ebe.htm language=enus -->
## TOPIC 00111: rfmxnrdotnet/html/7b729eb7-92ad-12c2-7bfe-3f49321d9ebe.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/7b729eb7-92ad-12c2-7bfe-3f49321d9ebe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/7b729eb7-92ad-12c2-7bfe-3f49321d9ebe.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.GetNoiseCalibrationMode Method

RFmxNRMXAcpConfigurationGetNoiseCalibrationMode Method

Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCalibrationMode(
	string selectorString,
	out RFmxNRMXAcpNoiseCalibrationMode value
)
```

```text
Public Function GetNoiseCalibrationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXAcpNoiseCalibrationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXAcpNoiseCalibrationModeUpon return, contains whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

AcpNoiseCalibrationMode

Auto

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/7e405cdf-0bc5-5a7d-b7c8-2493f0a62f6b.htm language=enus -->
## TOPIC 00112: rfmxnrdotnet/html/7e405cdf-0bc5-5a7d-b7c8-2493f0a62f6b.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/7e405cdf-0bc5-5a7d-b7c8-2493f0a62f6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/7e405cdf-0bc5-5a7d-b7c8-2493f0a62f6b.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtConfiguration.GetAveragingCount Method

RFmxNRMXPvtConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxNRMXPvtAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxNRMXPvtAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

PvtAveragingCount

##### See Also

###### Reference

RFmxNRMXPvtConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/7fb6ca40-a94e-d98b-6bff-bd08028c743d.htm language=enus -->
## TOPIC 00113: rfmxnrdotnet/html/7fb6ca40-a94e-d98b-6bff-bd08028c743d.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/7fb6ca40-a94e-d98b-6bff-bd08028c743d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/7fb6ca40-a94e-d98b-6bff-bd08028c743d.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetEpreRatioPort Method

RFmxNRMXComponentCarrierGetEpreRatioPort Method

3GPP TS 38.214

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEpreRatioPort(
	string selectorString,
	out int value
)
```

```text
Public Function GetEpreRatioPort ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode method to Standard.

###### Return Value

Int32

##### Remarks

EpreRatioPort

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/7fe3579a-f901-9498-2efd-cfc733f5cce1.htm language=enus -->
## TOPIC 00114: rfmxnrdotnet/html/7fe3579a-f901-9498-2efd-cfc733f5cce1.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/7fe3579a-f901-9498-2efd-cfc733f5cce1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/7fe3579a-f901-9498-2efd-cfc733f5cce1.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetMeasurementEnabled Method

RFmxNRMXModAccConfigurationSetMeasurementEnabled Method

Sets whether to enable the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.NRMX

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
  - Type: SystemBooleanSpecifies whether to enable the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccMeasurementEnabled

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/803ca5e4-0911-7a79-e5a1-9ab76f3af342.htm language=enus -->
## TOPIC 00115: rfmxnrdotnet/html/803ca5e4-0911-7a79-e5a1-9ab76f3af342.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/803ca5e4-0911-7a79-e5a1-9ab76f3af342.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/803ca5e4-0911-7a79-e5a1-9ab76f3af342.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.GetAveragingEnabled Method

RFmxNRMXSemConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the SEM measurement.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxNRMXSemAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXSemAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXSemAveragingEnabledUpon return, contains whether to enable averaging for the SEM measurement.

###### Return Value

Int32

##### Remarks

SemAveragingEnabled

False

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/819d884e-2184-d77d-0ba4-ac8bb7ea09a7.htm language=enus -->
## TOPIC 00116: rfmxnrdotnet/html/819d884e-2184-d77d-0ba4-ac8bb7ea09a7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/819d884e-2184-d77d-0ba4-ac8bb7ea09a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/819d884e-2184-d77d-0ba4-ac8bb7ea09a7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetPdschDmrsConfigurationType Method

RFmxNRMXComponentCarrierSetPdschDmrsConfigurationType Method

Sets the configuration type of DMRS.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdschDmrsConfigurationType(
	string selectorString,
	RFmxNRMXPdschDmrsConfigurationType value
)
```

```text
Public Function SetPdschDmrsConfigurationType ( 
	selectorString As String,
	value As RFmxNRMXPdschDmrsConfigurationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPdschDmrsConfigurationTypeSpecifies the configuration type of DMRS.

###### Return Value

Int32

##### Remarks

PdschDmrsConfigurationType

Type1

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/81b50df3-8534-6e78-3202-fab618caa47a.htm language=enus -->
## TOPIC 00117: rfmxnrdotnet/html/81b50df3-8534-6e78-3202-fab618caa47a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/81b50df3-8534-6e78-3202-fab618caa47a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/81b50df3-8534-6e78-3202-fab618caa47a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXConstants.PxiTriggerLine4 Field

RFmxNRMXConstantsPxiTriggerLine4 Field

The signal is exported to the PXI trigger line 4.

Namespace:

NationalInstruments.RFmx.NRMX

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

RFmxNRMXConstants Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/8387dd72-549a-071d-8c73-f1c40dce1d58.htm language=enus -->
## TOPIC 00118: rfmxnrdotnet/html/8387dd72-549a-071d-8c73-f1c40dce1d58.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/8387dd72-549a-071d-8c73-f1c40dce1d58.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/8387dd72-549a-071d-8c73-f1c40dce1d58.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetFftWindowType Method

RFmxNRMXModAccConfigurationSetFftWindowType Method

Sets the FFT window type used for EVM calculation.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftWindowType(
	string selectorString,
	RFmxNRMXModAccFftWindowType value
)
```

```text
Public Function SetFftWindowType ( 
	selectorString As String,
	value As RFmxNRMXModAccFftWindowType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccFftWindowTypeSpecifies the FFT window type used for EVM calculation.

###### Return Value

Int32

##### Remarks

ModAccFftWindowType

TypeCustom

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/83e48c14-3788-0a9c-77ae-793a0cece401.htm language=enus -->
## TOPIC 00119: rfmxnrdotnet/html/83e48c14-3788-0a9c-77ae-793a0cece401.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/83e48c14-3788-0a9c-77ae-793a0cece401.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/83e48c14-3788-0a9c-77ae-793a0cece401.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetNumberOfPtrsGroups Method

RFmxNRMXComponentCarrierGetNumberOfPtrsGroups Method

SetPuschPtrsEnabled(String, RFmxNRMXPuschPtrsEnabled)

True

SetPuschTransformPrecodingEnabled(String, RFmxNRMXPuschTransformPrecodingEnabled)

True

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfPtrsGroups(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfPtrsGroups ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the number of PTRS groups per OFDM symbol. This method is valid only if you set the SetPuschPtrsEnabled(String, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(String, RFmxNRMXPuschTransformPrecodingEnabled) method to True.

###### Return Value

Int32

##### Remarks

NumberOfPtrsGroups

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/856b3a01-3b95-2fe5-2a33-accdeb82c1cf.htm language=enus -->
## TOPIC 00120: rfmxnrdotnet/html/856b3a01-3b95-2fe5-2a33-accdeb82c1cf.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/856b3a01-3b95-2fe5-2a33-accdeb82c1cf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/856b3a01-3b95-2fe5-2a33-accdeb82c1cf.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.CloneSignalConfiguration Method

RFmxNRMXCloneSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int CloneSignalConfiguration(
	string newSignalName,
	out RFmxNRMX signalConfiguration
)
```

```text
Public Function CloneSignalConfiguration ( 
	newSignalName As String,
	<OutAttribute> ByRef signalConfiguration As RFmxNRMX
) As Integer
```

###### Parameters

- **newSignalName**
  - Type: SystemString Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName"
- **signalConfiguration**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXUpon return, contains a new NR signal instance.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/85a74fb9-8f32-25e9-91a1-0b28151d5783.htm language=enus -->
## TOPIC 00121: rfmxnrdotnet/html/85a74fb9-8f32-25e9-91a1-0b28151d5783.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/85a74fb9-8f32-25e9-91a1-0b28151d5783.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/85a74fb9-8f32-25e9-91a1-0b28151d5783.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetSssRmsEvmMean Method

RFmxNRMXModAccResultsGetSssRmsEvmMean Method

SetEvmUnit(String, RFmxNRMXModAccEvmUnit)

Percentage

dB

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSssRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetSssRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs computed over measurement length on SSS symbols. When you set the SetEvmUnit(String, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsSssRmsEvmMean

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/8637503b-7496-6f8f-6ae7-c8cf125865a8.htm language=enus -->
## TOPIC 00122: rfmxnrdotnet/html/8637503b-7496-6f8f-6ae7-c8cf125865a8.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/8637503b-7496-6f8f-6ae7-c8cf125865a8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/8637503b-7496-6f8f-6ae7-c8cf125865a8.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXObwSpanAuto Enumeration

RFmxNRMXObwSpanAuto Enumeration

Specifies whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXObwSpanAuto
```

```text
Public Enumeration RFmxNRMXObwSpanAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Indicates that the user-configured span is used. |
|  | True | 1 | Indicates that the measurement will auto compute the span based on the configuration. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/86849623-41ca-f615-c672-8392cc3fcd33.htm language=enus -->
## TOPIC 00123: rfmxnrdotnet/html/86849623-41ca-f615-c672-8392cc3fcd33.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/86849623-41ca-f615-c672-8392cc3fcd33.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/86849623-41ca-f615-c672-8392cc3fcd33.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccTimingTrackingMode Enumeration

RFmxNRMXModAccTimingTrackingMode Enumeration

Specifies the method used for timing tracking.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXModAccTimingTrackingMode
```

```text
Public Enumeration RFmxNRMXModAccTimingTrackingMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Disabled | 0 | Disables the timing tracking. |
|  | ReferenceAndData | 1 | All reference and data symbols are used for timing tracking. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/89454427-b208-17b3-1f6c-f09c1417c03a.htm language=enus -->
## TOPIC 00124: rfmxnrdotnet/html/89454427-b208-17b3-1f6c-f09c1417c03a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/89454427-b208-17b3-1f6c-f09c1417c03a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/89454427-b208-17b3-1f6c-f09c1417c03a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.GetSubblockAggregatedChannelBandwidth Method

RFmxNRMXSemConfigurationGetSubblockAggregatedChannelBandwidth Method

Gets the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSubblockAggregatedChannelBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetSubblockAggregatedChannelBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth.

###### Return Value

Int32

##### Remarks

SemSubblockAggregatedChannelBandwidth

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/896edbae-21d2-8100-711b-883bdaa49b0a.htm language=enus -->
## TOPIC 00125: rfmxnrdotnet/html/896edbae-21d2-8100-711b-883bdaa49b0a.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/896edbae-21d2-8100-711b-883bdaa49b0a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/896edbae-21d2-8100-711b-883bdaa49b0a.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpComponentCarrierResults.GetAbsolutePower Method

RFmxNRMXChpComponentCarrierResultsGetAbsolutePower Method

Gets the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

ChpResultsComponentCarrierAbsolutePower

##### See Also

###### Reference

RFmxNRMXChpComponentCarrierResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/8982f186-3467-9596-0e56-7703467f7c0d.htm language=enus -->
## TOPIC 00126: rfmxnrdotnet/html/8982f186-3467-9596-0e56-7703467f7c0d.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/8982f186-3467-9596-0e56-7703467f7c0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/8982f186-3467-9596-0e56-7703467f7c0d.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXIQPowerEdgeTriggerSlope Enumeration

RFmxNRMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXIQPowerEdgeTriggerSlope
```

```text
Public Enumeration RFmxNRMXIQPowerEdgeTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 0 | The trigger asserts when the signal power is rising. |
|  | Falling | 1 | The trigger asserts when the signal power is falling. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/95acf39b-c114-3335-38b6-77a72a46ebde.htm language=enus -->
## TOPIC 00127: rfmxnrdotnet/html/95acf39b-c114-3335-38b6-77a72a46ebde.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/95acf39b-c114-3335-38b6-77a72a46ebde.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/95acf39b-c114-3335-38b6-77a72a46ebde.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.SetFrequencyRange Method

RFmxNRMXSetFrequencyRange Method

Sets whether to use channel bandwidth and subcarrier spacing configuration supported in the frequency range 1 (sub 6 GHz) or the frequency range 2 (above 24 GHz).

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyRange(
	string selectorString,
	RFmxNRMXFrequencyRange value
)
```

```text
Public Function SetFrequencyRange ( 
	selectorString As String,
	value As RFmxNRMXFrequencyRange
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXFrequencyRangeSpecifies whether to use channel bandwidth and subcarrier spacing configuration supported in the frequency range 1 (sub 6 GHz) or the frequency range 2 (above 24 GHz).

###### Return Value

Int32

##### Remarks

FrequencyRange

Range1

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/95be7fa6-e392-2b50-fe24-7fb15533cd08.htm language=enus -->
## TOPIC 00128: rfmxnrdotnet/html/95be7fa6-e392-2b50-fe24-7fb15533cd08.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/95be7fa6-e392-2b50-fe24-7fb15533cd08.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/95be7fa6-e392-2b50-fe24-7fb15533cd08.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPbchDmrsConstellationTrace Method

RFmxNRMXModAccResultsFetchPbchDmrsConstellationTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPbchDmrsConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] pbchDmrsConstellation
)
```

```text
Public Function FetchPbchDmrsConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef pbchDmrsConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **pbchDmrsConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the PBCH DMRS trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/96198c0b-076d-03b9-2363-d4b868ad3172.htm language=enus -->
## TOPIC 00129: rfmxnrdotnet/html/96198c0b-076d-03b9-2363-d4b868ad3172.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/96198c0b-076d-03b9-2363-d4b868ad3172.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/96198c0b-076d-03b9-2363-d4b868ad3172.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAcc Properties

RFmxNRMXModAcc Properties

The [RFmxNRMXModAcc](675c4588-4ba4-1bf4-b8d8-7787d1bdaf84.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxNRMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
|  | Results | Gets the RFmxNRMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Top

##### See Also

###### Reference

RFmxNRMXModAcc Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/99851dca-2c40-6c9c-34a8-a8520ddad697.htm language=enus -->
## TOPIC 00130: rfmxnrdotnet/html/99851dca-2c40-6c9c-34a8-a8520ddad697.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/99851dca-2c40-6c9c-34a8-a8520ddad697.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/99851dca-2c40-6c9c-34a8-a8520ddad697.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemConfiguration.GetNumberOfOffsets Method

RFmxNRMXSemConfigurationGetNumberOfOffsets Method

Gets the number of SEM offset segments.

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of SEM offset segments.

###### Return Value

Int32

##### Remarks

SemNumberOfOffsets

##### See Also

###### Reference

RFmxNRMXSemConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/99c91d5c-be44-6d21-7ff3-b80d9e6d33f7.htm language=enus -->
## TOPIC 00131: rfmxnrdotnet/html/99c91d5c-be44-6d21-7ff3-b80d9e6d33f7.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/99c91d5c-be44-6d21-7ff3-b80d9e6d33f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/99c91d5c-be44-6d21-7ff3-b80d9e6d33f7.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.Chp Property

RFmxNRMXChp Property

RFmxNRMXChp

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxNRMXChp Chp { get; }
```

```text
Public ReadOnly Property Chp As RFmxNRMXChp
	Get
```

###### Property Value

RFmxNRMXChp

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/9b4b4e0e-d0e5-b912-a936-4c0db5c1c84f.htm language=enus -->
## TOPIC 00132: rfmxnrdotnet/html/9b4b4e0e-d0e5-b912-a936-4c0db5c1c84f.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/9b4b4e0e-d0e5-b912-a936-4c0db5c1c84f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/9b4b4e0e-d0e5-b912-a936-4c0db5c1c84f.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.GetRbwFilterBandwidth Method

RFmxNRMXAcpConfigurationGetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxNRMXAcpRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.NRMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxNRMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpRbwFilterBandwidth

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/9b668100-1fc5-16dd-7729-1906029abe32.htm language=enus -->
## TOPIC 00133: rfmxnrdotnet/html/9b668100-1fc5-16dd-7729-1906029abe32.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/9b668100-1fc5-16dd-7729-1906029abe32.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/9b668100-1fc5-16dd-7729-1906029abe32.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetShortFrameLength Method

RFmxNRMXModAccConfigurationSetShortFrameLength Method

Sets the short frame periodicity in unit specified by Short Frame Length Unit.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetShortFrameLength(
	string selectorString,
	double value
)
```

```text
Public Function SetShortFrameLength ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the short frame periodicity in unit specified by Short Frame Length Unit.

###### Return Value

Int32

##### Remarks

ModAccShortFrameLength

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/a67a08e3-5911-db83-a276-89d80515354b.htm language=enus -->
## TOPIC 00134: rfmxnrdotnet/html/a67a08e3-5911-db83-a276-89d80515354b.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/a67a08e3-5911-db83-a276-89d80515354b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/a67a08e3-5911-db83-a276-89d80515354b.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXSemComponentCarrierResults.GetRelativeIntegratedPower Method

RFmxNRMXSemComponentCarrierResultsGetRelativeIntegratedPower Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRelativeIntegratedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetRelativeIntegratedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the component carrier power relative to GetSubblockPower(String, Double). This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsComponentCarrierRelativeIntegratedPower

##### See Also

###### Reference

RFmxNRMXSemComponentCarrierResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/a6db925b-036e-4bce-19d1-7dcf7f160dbb.htm language=enus -->
## TOPIC 00135: rfmxnrdotnet/html/a6db925b-036e-4bce-19d1-7dcf7f160dbb.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/a6db925b-036e-4bce-19d1-7dcf7f160dbb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/a6db925b-036e-4bce-19d1-7dcf7f160dbb.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXTriggerMinimumQuietTimeMode Enumeration

RFmxNRMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXTriggerMinimumQuietTimeMode
```

```text
Public Enumeration RFmxNRMXTriggerMinimumQuietTimeMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(String, Double) method. |
|  | Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/a77ac951-48af-dc69-ba3e-f7bb7e35fcda.htm language=enus -->
## TOPIC 00136: rfmxnrdotnet/html/a77ac951-48af-dc69-ba3e-f7bb7e35fcda.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/a77ac951-48af-dc69-ba3e-f7bb7e35fcda.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/a77ac951-48af-dc69-ba3e-f7bb7e35fcda.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXAcpConfiguration.SetOffsetIntegrationBandwidth Method

RFmxNRMXAcpConfigurationSetOffsetIntegrationBandwidth Method

Sets the integration bandwidth of an offset channel. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetIntegrationBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetIntegrationBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the integration bandwidth of an offset channel. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpOffsetIntegrationBandwidth

##### See Also

###### Reference

RFmxNRMXAcpConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/a781c821-47b3-41aa-0617-a70a9f7a0f53.htm language=enus -->
## TOPIC 00137: rfmxnrdotnet/html/a781c821-47b3-41aa-0617-a70a9f7a0f53.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/a781c821-47b3-41aa-0617-a70a9f7a0f53.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/a781c821-47b3-41aa-0617-a70a9f7a0f53.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXChpSweepTimeAuto Enumeration

RFmxNRMXChpSweepTimeAuto Enumeration

Specifies whether the measurement sets the sweep time.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxNRMXChpSweepTimeAuto
```

```text
Public Enumeration RFmxNRMXChpSweepTimeAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the sweep time that you specify in the Sweep Time Interval method. |
|  | True | 1 | The measurement uses the sweep time based on the resolution bandwidth. |

##### See Also

###### Reference

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/a855b561-45a4-ddb3-a846-6d7fd530aa68.htm language=enus -->
## TOPIC 00138: rfmxnrdotnet/html/a855b561-45a4-ddb3-a846-6d7fd530aa68.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/a855b561-45a4-ddb3-a846-6d7fd530aa68.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/a855b561-45a4-ddb3-a846-6d7fd530aa68.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.SetBandwidthPartCyclicPrefixMode Method

RFmxNRMXComponentCarrierSetBandwidthPartCyclicPrefixMode Method

Sets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetBandwidthPartCyclicPrefixMode(
	string selectorString,
	RFmxNRMXBandwidthPartCyclicPrefixMode value
)
```

```text
Public Function SetBandwidthPartCyclicPrefixMode ( 
	selectorString As String,
	value As RFmxNRMXBandwidthPartCyclicPrefixMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXBandwidthPartCyclicPrefixModeSpecifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

###### Return Value

Int32

##### Remarks

BandwidthPartCyclicPrefixMode

Normal

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/a954e4b3-07a7-36ec-c5e8-ac42e9bf782d.htm language=enus -->
## TOPIC 00139: rfmxnrdotnet/html/a954e4b3-07a7-36ec-c5e8-ac42e9bf782d.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/a954e4b3-07a7-36ec-c5e8-ac42e9bf782d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/a954e4b3-07a7-36ec-c5e8-ac42e9bf782d.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXExtension.GetNRList Method

RFmxNRMXExtensionGetNRList Method

Creates a new NR list if it doesn't exist; otherwise, it returns the
 existing NR list.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxNRMXList GetNRList(
	this RFmxInstrMX instrSession,
	string listName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetNRList ( 
	instrSession As RFmxInstrMX,
	listName As String
) As RFmxNRMXList
```

###### Parameters

- **instrSession**
  - Type: RFmxInstrMXSpecifies an instr session.
- **listName**
  - Type: SystemString Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::list1" "list1"

###### Return Value

RFmxNRMXList

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxNRMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/aaa31716-5616-6b5e-47ea-0fb6a24ff111.htm language=enus -->
## TOPIC 00140: rfmxnrdotnet/html/aaa31716-5616-6b5e-47ea-0fb6a24ff111.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/aaa31716-5616-6b5e-47ea-0fb6a24ff111.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/aaa31716-5616-6b5e-47ea-0fb6a24ff111.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXComponentCarrier.GetSsbGridSize Method

RFmxNRMXComponentCarrierGetSsbGridSize Method

SetGridSizeMode(String, RFmxNRMXGridSizeMode)

Manual

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSsbGridSize(
	string selectorString,
	out int value
)
```

```text
Public Function GetSsbGridSize ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the SSB resource grid size when you set the SetGridSizeMode(String, RFmxNRMXGridSizeMode) method to Manual.

###### Return Value

Int32

##### Remarks

SsbGridSize

##### See Also

###### Reference

RFmxNRMXComponentCarrier Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/aad5d1b5-8ef5-4276-6e95-18f1e54f62c3.htm language=enus -->
## TOPIC 00141: rfmxnrdotnet/html/aad5d1b5-8ef5-4276-6e95-18f1e54f62c3.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/aad5d1b5-8ef5-4276-6e95-18f1e54f62c3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/aad5d1b5-8ef5-4276-6e95-18f1e54f62c3.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetSpectralFlatnessRange1Minimum Method

RFmxNRMXModAccResultsGetSpectralFlatnessRange1Minimum Method

3GPP 38.101-1

3GPP 38.101-2

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectralFlatnessRange1Minimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpectralFlatnessRange1Minimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsSpectralFlatnessRange1Minimum

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/aaf653f1-ff38-7ef4-9a15-a3644caa3d40.htm language=enus -->
## TOPIC 00142: rfmxnrdotnet/html/aaf653f1-ff38-7ef4-9a15-a3644caa3d40.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/aaf653f1-ff38-7ef4-9a15-a3644caa3d40.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/aaf653f1-ff38-7ef4-9a15-a3644caa3d40.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.GetWarning Method

RFmxNRMXGetWarning Method

Gets the latest warning code and description.

Namespace:

NationalInstruments.RFmx.NRMX

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

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/b6244f94-9cba-58ca-02f5-58daf0ebeb03.htm language=enus -->
## TOPIC 00143: rfmxnrdotnet/html/b6244f94-9cba-58ca-02f5-58daf0ebeb03.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/b6244f94-9cba-58ca-02f5-58daf0ebeb03.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/b6244f94-9cba-58ca-02f5-58daf0ebeb03.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccConfiguration.SetIQImpairmentsPerSubcarrierEnabled Method

RFmxNRMXModAccConfigurationSetIQImpairmentsPerSubcarrierEnabled Method

Sets whether to return I/Q impairments independently for each subcarrier.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQImpairmentsPerSubcarrierEnabled(
	string selectorString,
	RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled value
)
```

```text
Public Function SetIQImpairmentsPerSubcarrierEnabled ( 
	selectorString As String,
	value As RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXModAccIQImpairmentsPerSubcarrierEnabledSpecifies whether to return I/Q impairments independently for each subcarrier.

###### Return Value

Int32

##### Remarks

ModAccIQImpairmentsPerSubcarrierEnabled

False

##### See Also

###### Reference

RFmxNRMXModAccConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/b64946eb-7ad7-ed49-40d1-a692b90976cf.htm language=enus -->
## TOPIC 00144: rfmxnrdotnet/html/b64946eb-7ad7-ed49-40d1-a692b90976cf.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/b64946eb-7ad7-ed49-40d1-a692b90976cf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/b64946eb-7ad7-ed49-40d1-a692b90976cf.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXPvtConfiguration.GetMeasurementMethod Method

RFmxNRMXPvtConfigurationGetMeasurementMethod Method

Gets the PVT measurement method.

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementMethod(
	string selectorString,
	out RFmxNRMXPvtMeasurementMethod value
)
```

```text
Public Function GetMeasurementMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxNRMXPvtMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.NRMXRFmxNRMXPvtMeasurementMethodUpon return, contains the PVT measurement method.

###### Return Value

Int32

##### Remarks

PvtMeasurementMethod

Normal

##### See Also

###### Reference

RFmxNRMXPvtConfiguration Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/b7c926e3-c14a-e9be-71b4-d17b81bbc496.htm language=enus -->
## TOPIC 00145: rfmxnrdotnet/html/b7c926e3-c14a-e9be-71b4-d17b81bbc496.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/b7c926e3-c14a-e9be-71b4-d17b81bbc496.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/b7c926e3-c14a-e9be-71b4-d17b81bbc496.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.GetSpectralFlatnessRange1MaximumToRange2Minimum Method

RFmxNRMXModAccResultsGetSpectralFlatnessRange1MaximumToRange2Minimum Method

3GPP 38.101-1

3GPP 38.101-2

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectralFlatnessRange1MaximumToRange2Minimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpectralFlatnessRange1MaximumToRange2Minimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from maximum in Range1 to minimum in Range2 for the Measurement unit that has the worst ripple margin among all four ripple results defined in 3section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsSpectralFlatnessRange1MaximumToRange2Minimum

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/b7df448b-5085-fdda-8d21-1efc1582aa41.htm language=enus -->
## TOPIC 00146: rfmxnrdotnet/html/b7df448b-5085-fdda-8d21-1efc1582aa41.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/b7df448b-5085-fdda-8d21-1efc1582aa41.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/b7df448b-5085-fdda-8d21-1efc1582aa41.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMX.ConfigureSoftwareEdgeTrigger Method

RFmxNRMXConfigureSoftwareEdgeTrigger Method

Namespace:

NationalInstruments.RFmx.NRMX

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
  - Type: SystemDoubleSpecifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.
- **enableTrigger**
  - Type: SystemBooleanSpecifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMX Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-nr-dotnet path=rfmxnrdotnet/html/ba1c6bd4-14ea-77b4-dd83-08c1f4834703.htm language=enus -->
## TOPIC 00147: rfmxnrdotnet/html/ba1c6bd4-14ea-77b4-dd83-08c1f4834703.htm

- bundle_id: `rfmx-nr-dotnet`
- source_path: `rfmxnrdotnet/html/ba1c6bd4-14ea-77b4-dd83-08c1f4834703.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-dotnet/raw/resource/enus/rfmxnrdotnet/html/ba1c6bd4-14ea-77b4-dd83-08c1f4834703.htm
- document_id: `rfmx-nr-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxNRMXModAccResults.FetchPeakEvmPerSubcarrierMaximumTrace Method

RFmxNRMXModAccResultsFetchPeakEvmPerSubcarrierMaximumTrace Method

Namespace:

NationalInstruments.RFmx.NRMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPeakEvmPerSubcarrierMaximumTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> peakEvmPerSubcarrierMaximum
)
```

```text
Public Function FetchPeakEvmPerSubcarrierMaximumTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef peakEvmPerSubcarrierMaximum As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **peakEvmPerSubcarrierMaximum**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. .

###### Return Value

Int32

##### See Also

###### Reference

RFmxNRMXModAccResults Class

NationalInstruments.RFmx.NRMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
