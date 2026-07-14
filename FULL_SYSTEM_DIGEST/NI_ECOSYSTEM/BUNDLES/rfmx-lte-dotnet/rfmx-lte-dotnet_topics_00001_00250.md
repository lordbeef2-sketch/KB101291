# NI DOCUMENT BUNDLE: rfmx-lte-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-lte-dotnet start=1 end=250 -->
<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/03f86b4e-d907-41d0-6a01-47f880cf3163.htm language=enus -->
## TOPIC 00001: rfmxltedotnet/html/03f86b4e-d907-41d0-6a01-47f880cf3163.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/03f86b4e-d907-41d0-6a01-47f880cf3163.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/03f86b4e-d907-41d0-6a01-47f880cf3163.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPsschMaximumPeakDataEvm Method

RFmxLteMXModAccResultsGetPsschMaximumPeakDataEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPsschMaximumPeakDataEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetPsschMaximumPeakDataEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsPsschMaximumPeakDataEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/044a750a-af9f-3a2b-ce4e-a18a8dc125e5.htm language=enus -->
## TOPIC 00002: rfmxltedotnet/html/044a750a-af9f-3a2b-ce4e-a18a8dc125e5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/044a750a-af9f-3a2b-ce4e-a18a8dc125e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/044a750a-af9f-3a2b-ce4e-a18a8dc125e5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPeakCompositeEvmSubcarrierIndex Method

RFmxLteMXModAccResultsGetPeakCompositeEvmSubcarrierIndex Method

Gets the subcarrier index where the maximum peak composite EVM for ModAcc occurs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakCompositeEvmSubcarrierIndex(
	string selectorString,
	out int value
)
```

```text
Public Function GetPeakCompositeEvmSubcarrierIndex ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the subcarrier index where the maximum peak composite EVM for ModAcc occurs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakCompositeEvmSubcarrierIndex

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/04f0e127-09a4-9374-94dd-2df29f8616b7.htm language=enus -->
## TOPIC 00003: rfmxltedotnet/html/04f0e127-09a4-9374-94dd-2df29f8616b7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/04f0e127-09a4-9374-94dd-2df29f8616b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/04f0e127-09a4-9374-94dd-2df29f8616b7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.ConfigureNumberOfEutraOffsets Method

RFmxLteMXAcpConfigurationConfigureNumberOfEutraOffsets Method

true

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfEutraOffsets(
	string selectorString,
	int numberOfEutraOffsets
)
```

```text
Public Function ConfigureNumberOfEutraOffsets ( 
	selectorString As String,
	numberOfEutraOffsets As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **numberOfEutraOffsets**
  - Type: SystemInt32 Specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to true.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/060885d5-a394-07d7-4a6f-6093cf3731c2.htm language=enus -->
## TOPIC 00004: rfmxltedotnet/html/060885d5-a394-07d7-4a6f-6093cf3731c2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/060885d5-a394-07d7-4a6f-6093cf3731c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/060885d5-a394-07d7-4a6f-6093cf3731c2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAcc.Configuration Property

RFmxLteMXModAccConfiguration Property

RFmxLteMXModAccConfiguration

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXModAccConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxLteMXModAccConfiguration
	Get
```

###### Property Value

RFmxLteMXModAccConfiguration

##### See Also

###### Reference

RFmxLteMXModAcc Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0652affb-9a7e-8ca3-5012-32fa4f6ee69d.htm language=enus -->
## TOPIC 00005: rfmxltedotnet/html/0652affb-9a7e-8ca3-5012-32fa4f6ee69d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0652affb-9a7e-8ca3-5012-32fa4f6ee69d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0652affb-9a7e-8ca3-5012-32fa4f6ee69d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpComponentCarrierResults Class

RFmxLteMXAcpComponentCarrierResults Class

Provides methods to fetch and read the ACP Component Carrier results.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXAcpComponentCarrierResults : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXAcpComponentCarrierResults
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXAcpComponentCarrierResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Fetches the ACP component carrier measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMeasurementArray | Returns an array of the absolute and relative powers of the component carriers. The relative power is relative to the subblock power. Use "subblock(n)" as the selector string to read results from this method. |
|  | GetAbsolutePower | Gets the power measured over the integration bandwidth of the carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetRelativePower | Gets the component carrier power relative to its subblock power. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/066add4b-66ab-5944-6ea8-733d9556cade.htm language=enus -->
## TOPIC 00006: rfmxltedotnet/html/066add4b-66ab-5944-6ea8-733d9556cade.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/066add4b-66ab-5944-6ea8-733d9556cade.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/066add4b-66ab-5944-6ea8-733d9556cade.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetLaaNumberOfSubframes Method

RFmxLteMXComponentCarrierGetLaaNumberOfSubframes Method

Gets the number of subframes in an LAA burst including the starting subframe.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLaaNumberOfSubframes(
	string selectorString,
	out int value
)
```

```text
Public Function GetLaaNumberOfSubframes ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of subframes in an LAA burst including the starting subframe.

###### Return Value

Int32

##### Remarks

LaaNumberOfSubframes

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/06b146f9-a638-0d49-9b9c-fd3ed325e81f.htm language=enus -->
## TOPIC 00007: rfmxltedotnet/html/06b146f9-a638-0d49-9b9c-fd3ed325e81f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/06b146f9-a638-0d49-9b9c-fd3ed325e81f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/06b146f9-a638-0d49-9b9c-fd3ed325e81f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.GetAveragingType Method

RFmxLteMXObwConfigurationGetAveragingType Method

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingType(
	string selectorString,
	out RFmxLteMXObwAveragingType value
)
```

```text
Public Function GetAveragingType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXObwAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwAveragingTypeUpon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

###### Return Value

Int32

##### Remarks

ObwAveragingType

Rms

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/07c7333b-82e5-0e13-fa7b-b1661259db69.htm language=enus -->
## TOPIC 00008: rfmxltedotnet/html/07c7333b-82e5-0e13-fa7b-b1661259db69.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/07c7333b-82e5-0e13-fa7b-b1661259db69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/07c7333b-82e5-0e13-fa7b-b1661259db69.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPhaseResults.FetchMaximumPhaseDiscontinuityArray Method

RFmxLteMXSlotPhaseResultsFetchMaximumPhaseDiscontinuityArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMaximumPhaseDiscontinuityArray(
	string selectorString,
	double timeout,
	ref double[] maximumPhaseDiscontinuity
)
```

```text
Public Function FetchMaximumPhaseDiscontinuityArray ( 
	selectorString As String,
	timeout As Double,
	ByRef maximumPhaseDiscontinuity As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **maximumPhaseDiscontinuity**
  - Type: SystemDouble Upon return, contains the array of maximum values of phase difference at the slot boundaries within the SetMeasurementLength(String, Int32).

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSlotPhaseResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/07e93da1-24a2-bc73-4191-ca65099958d7.htm language=enus -->
## TOPIC 00009: rfmxltedotnet/html/07e93da1-24a2-bc73-4191-ca65099958d7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/07e93da1-24a2-bc73-4191-ca65099958d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/07e93da1-24a2-bc73-4191-ca65099958d7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetAmplitudeCorrectionType Method

RFmxLteMXAcpConfigurationGetAmplitudeCorrectionType Method

Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeCorrectionType(
	string selectorString,
	out RFmxLteMXAcpAmplitudeCorrectionType value
)
```

```text
Public Function GetAmplitudeCorrectionType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAcpAmplitudeCorrectionType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpAmplitudeCorrectionTypeUpon return, contains whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

###### Return Value

Int32

##### Remarks

AcpAmplitudeCorrectionType

RFCenterFrequency

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/083d71fd-aa66-09ca-294a-e87450678d64.htm language=enus -->
## TOPIC 00010: rfmxltedotnet/html/083d71fd-aa66-09ca-294a-e87450678d64.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/083d71fd-aa66-09ca-294a-e87450678d64.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/083d71fd-aa66-09ca-294a-e87450678d64.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvt Properties

RFmxLteMXPvt Properties

The [RFmxLteMXPvt](9b826aeb-c280-6928-f60c-9690bea33825.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXPvtConfiguration instance that provides methods to configure the PVT measurement. |
|  | Results | Gets the RFmxLteMXPvtResults instance that provides methods to fetch and read the PVT measurement results. |

Top

##### See Also

###### Reference

RFmxLteMXPvt Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/08eacb28-5514-e2fa-1c82-d66e8d283327.htm language=enus -->
## TOPIC 00011: rfmxltedotnet/html/08eacb28-5514-e2fa-1c82-d66e8d283327.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/08eacb28-5514-e2fa-1c82-d66e8d283327.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/08eacb28-5514-e2fa-1c82-d66e8d283327.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.GetNumberOfAnalysisThreads Method

RFmxLteMXObwConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

ObwNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/092653e6-c3bd-3b26-5b6d-1925b03b6e4c.htm language=enus -->
## TOPIC 00012: rfmxltedotnet/html/092653e6-c3bd-3b26-5b6d-1925b03b6e4c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/092653e6-c3bd-3b26-5b6d-1925b03b6e4c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/092653e6-c3bd-3b26-5b6d-1925b03b6e4c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetDigitalEdgeTriggerSource Method

RFmxLteMXGetDigitalEdgeTriggerSource Method

SetTriggerType(String, RFmxLteMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemString Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/094828ac-c047-02fd-25b0-cfec381a03cc.htm language=enus -->
## TOPIC 00013: rfmxltedotnet/html/094828ac-c047-02fd-25b0-cfec381a03cc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/094828ac-c047-02fd-25b0-cfec381a03cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/094828ac-c047-02fd-25b0-cfec381a03cc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchDownlinkPbchConstellation Method

RFmxLteMXModAccResultsFetchDownlinkPbchConstellation Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDownlinkPbchConstellation(
	string selectorString,
	double timeout,
	ref ComplexSingle[] pbchConstellation
)
```

```text
Public Function FetchDownlinkPbchConstellation ( 
	selectorString As String,
	timeout As Double,
	ByRef pbchConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **pbchConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the PBCH constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0963ea03-b588-439c-e12f-024bbd99c5f7.htm language=enus -->
## TOPIC 00014: rfmxltedotnet/html/0963ea03-b588-439c-e12f-024bbd99c5f7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0963ea03-b588-439c-e12f-024bbd99c5f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0963ea03-b588-439c-e12f-024bbd99c5f7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults Methods

RFmxLteMXSemResults Methods

The [RFmxLteMXSemResults](a544db38-7b92-5e15-3f5e-3db1718872c0.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchLowerOffsetMargin | Returns the measurement status, margin, frequency at margin, and the absolute and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchLowerOffsetMarginArray | Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchLowerOffsetPower | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchLowerOffsetPowerArray | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchMeasurementStatus | Returns the overall measurement status based on the standard mask type that you configure. |
|  | FetchSpectrum | Fetches the spectrum used for the SEM measurement. |
|  | FetchSubblockMeasurement | Returns the power, integration bandwidth and center frequency of the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchTotalAggregatedPower | Returns the sum of powers of all subblocks. |
|  | FetchUpperOffsetMargin | Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchUpperOffsetMarginArray | Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchUpperOffsetPower | Returns the total absolute and relative powers, peak, absolute, and relative powers, and frequency at peak absolute power of upper offset segment. The relative power is relative to total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | FetchUpperOffsetPowerArray | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLowerOffsetAbsoluteIntegratedPower | Gets the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetAbsolutePeakPower | Gets the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetMargin | Gets the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetMarginAbsolutePower | Gets the power at which the margin occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetMarginFrequency | Gets the frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetMarginRelativePower | Gets the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetMeasurementStatus | Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type method. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetPeakFrequency | Gets the frequency at which the peak power occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetRelativeIntegratedPower | Gets the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetLowerOffsetRelativePeakPower | Gets the peak power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetMeasurementStatus | Gets the overall measurement status based on the standard mask type that you configure in the SEM Standard Mask Type method. |
|  | GetSubblockCenterFrequency | Gets the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. |
|  | GetSubblockIntegrationBandwidth | Gets the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. |
|  | GetSubblockPower | Gets the power measured over the integration bandwidth of the subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
|  | GetTotalAggregatedPower | Gets the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUpperOffsetAbsoluteIntegratedPower | Gets the upper (positive) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetAbsolutePeakPower | Gets the power in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetMargin | Gets the margin from the absolute limit mask for the upper (positive) offset. The Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetMarginAbsolutePower | Gets the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetMarginFrequency | Gets the frequency at which the margin occurs in the upper (positive) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetMarginRelativePower | Gets the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetMeasurementStatus | Gets the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetPeakFrequency | Gets the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | GetUpperOffsetRelativeIntegratedPower | Gets the power in the upper (positive) offset segment relative to the total aggregated power. |
|  | GetUpperOffsetRelativePeakPower | Gets the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/096d095a-cbe4-0268-4e2d-7f6913db3e56.htm language=enus -->
## TOPIC 00015: rfmxltedotnet/html/096d095a-cbe4-0268-4e2d-7f6913db3e56.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/096d095a-cbe4-0268-4e2d-7f6913db3e56.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/096d095a-cbe4-0268-4e2d-7f6913db3e56.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpResults Methods

RFmxLteMXTxpResults Methods

The [RFmxLteMXTxpResults](270bce9b-cc89-16a1-957e-be43e8a93a2a.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Fetches the average power and peak power of the the signal over which power measurments are performed. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPowerTrace | Fetches power versus time trace. |
|  | GetAveragePowerMean | Gets the average power of the acquired signal. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPeakPowerMaximum | Gets the peak power of the acquired signal. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXTxpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0af475a6-bc15-80f2-e8ae-e6ed99c07cf4.htm language=enus -->
## TOPIC 00016: rfmxltedotnet/html/0af475a6-bc15-80f2-e8ae-e6ed99c07cf4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0af475a6-bc15-80f2-e8ae-e6ed99c07cf4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0af475a6-bc15-80f2-e8ae-e6ed99c07cf4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetAllTracesEnabled Method

RFmxLteMXModAccConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanSpecifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccAllTracesEnabled

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0bdc1bf5-8f2e-2500-6edc-f7e890021938.htm language=enus -->
## TOPIC 00017: rfmxltedotnet/html/0bdc1bf5-8f2e-2500-6edc-f7e890021938.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0bdc1bf5-8f2e-2500-6edc-f7e890021938.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0bdc1bf5-8f2e-2500-6edc-f7e890021938.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXDownlinkTestModel Enumeration

RFmxLteMXDownlinkTestModel Enumeration

SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode)

TestModel

3GPP 36.141

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXDownlinkTestModel
```

```text
Public Enumeration RFmxLteMXDownlinkTestModel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TM1_1 | 0 | Specifies an E-UTRA Test Model 1.1. |
|  | TM1_2 | 1 | Specifies an E-UTRA Test Model 1.2. |
|  | TM2 | 2 | Specifies an E-UTRA Test Model 2. |
|  | TM2A | 3 | Specifies an E-UTRA Test Model 2a. |
|  | TM3_1 | 4 | Specifies an E-UTRA Test Model 3.1. |
|  | TM3_2 | 5 | Specifies an E-UTRA Test Model 3.2. |
|  | TM3_3 | 6 | Specifies an E-UTRA Test Model 3.3. |
|  | TM3_1A | 7 | Specifies an E-UTRA Test Model 3.1a. |
|  | TM2B | 8 | Specifies an E-UTRA Test Model 2b. |
|  | TM3_1B | 9 | Specifies an E-UTRA Test Model 3.1b. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0bfa04fe-cd70-06ef-21be-120f079dfd51.htm language=enus -->
## TOPIC 00018: rfmxltedotnet/html/0bfa04fe-cd70-06ef-21be-120f079dfd51.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0bfa04fe-cd70-06ef-21be-120f079dfd51.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0bfa04fe-cd70-06ef-21be-120f079dfd51.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtAveragingType Enumeration

RFmxLteMXPvtAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXPvtAveragingType
```

```text
Public Enumeration RFmxLteMXPvtAveragingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
|  | Log | 1 | The power spectrum is averaged in a logarithmic scale. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0c63ca18-2bcd-5a7a-3753-92e65c593277.htm language=enus -->
## TOPIC 00019: rfmxltedotnet/html/0c63ca18-2bcd-5a7a-3753-92e65c593277.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0c63ca18-2bcd-5a7a-3753-92e65c593277.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0c63ca18-2bcd-5a7a-3753-92e65c593277.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxp Properties

RFmxLteMXTxp Properties

The [RFmxLteMXTxp](3793912c-7b60-55bb-130f-60b983c112f9.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXTxpConfiguration instance that provides methods to configure the TXP measurement. |
|  | Results | Gets the RFmxLteMXTxpResults instance that provides methods to fetch and read the TXP measurement results. |

Top

##### See Also

###### Reference

RFmxLteMXTxp Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0ec19ff1-6eba-d732-7d9f-7b9a42d5ae8b.htm language=enus -->
## TOPIC 00020: rfmxltedotnet/html/0ec19ff1-6eba-d732-7d9f-7b9a42d5ae8b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0ec19ff1-6eba-d732-7d9f-7b9a42d5ae8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0ec19ff1-6eba-d732-7d9f-7b9a42d5ae8b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetNoiseCompensationType Method

RFmxLteMXChpConfigurationSetNoiseCompensationType Method

Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCompensationType(
	string selectorString,
	RFmxLteMXChpNoiseCompensationType value
)
```

```text
Public Function SetNoiseCompensationType ( 
	selectorString As String,
	value As RFmxLteMXChpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpNoiseCompensationTypeSpecifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

ChpNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0ed7711a-30bb-bc3c-b41e-10eb3af3d2e3.htm language=enus -->
## TOPIC 00021: rfmxltedotnet/html/0ed7711a-30bb-bc3c-b41e-10eb3af3d2e3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0ed7711a-30bb-bc3c-b41e-10eb3af3d2e3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0ed7711a-30bb-bc3c-b41e-10eb3af3d2e3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXLinkDirection Enumeration

RFmxLteMXLinkDirection Enumeration

Specifies the direction for which the frequency is calculated. Only Uplink is supported.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXLinkDirection
```

```text
Public Enumeration RFmxLteMXLinkDirection
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Downlink | 0 | The measurement uses 3GPP LTE downlink specification to measure the received signal. |
|  | Uplink | 1 | The frequency is calculated in the reverse link direction, also know as the uplink direction. |
|  | Sidelink | 2 | The measurement uses 3GPP LTE sidelink specifications to measure the received signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0edb8768-aff1-7f49-3955-6716515d8f48.htm language=enus -->
## TOPIC 00022: rfmxltedotnet/html/0edb8768-aff1-7f49-3955-6716515d8f48.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0edb8768-aff1-7f49-3955-6716515d8f48.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0edb8768-aff1-7f49-3955-6716515d8f48.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.AbortMeasurements Method

RFmxLteMXListAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The list name that is passed when creating the list is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0efc3c0b-cea8-9ada-f657-8782285e86b7.htm language=enus -->
## TOPIC 00023: rfmxltedotnet/html/0efc3c0b-cea8-9ada-f657-8782285e86b7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0efc3c0b-cea8-9ada-f657-8782285e86b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0efc3c0b-cea8-9ada-f657-8782285e86b7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchInBandEmissionMargin Method

RFmxLteMXModAccResultsFetchInBandEmissionMargin Method

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchInBandEmissionMargin(
	string selectorString,
	double timeout,
	out double inBandEmissionMargin
)
```

```text
Public Function FetchInBandEmissionMargin ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef inBandEmissionMargin As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **inBandEmissionMargin**
  - Type: SystemDouble Upon return, contains the in-band emission margin. The margin is the least difference between the in-band emission measurement trace and limit trace. The limit is defined in section 6.5.2.3.5 of the 3GPP TS 36.521 specification. The in-band emissions are a measure of the interference falling into the non-allocated resources blocks.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0f0a76d8-1b11-95dc-c0ba-2b179fdc1ecc.htm language=enus -->
## TOPIC 00024: rfmxltedotnet/html/0f0a76d8-1b11-95dc-c0ba-2b179fdc1ecc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0f0a76d8-1b11-95dc-c0ba-2b179fdc1ecc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0f0a76d8-1b11-95dc-c0ba-2b179fdc1ecc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXConstants.PxiTriggerLine3 Field

RFmxLteMXConstantsPxiTriggerLine3 Field

The signal is exported to the PXI trigger line 3.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXConstants Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0f3d95c3-86ed-6d8b-9648-51beee3f6667.htm language=enus -->
## TOPIC 00025: rfmxltedotnet/html/0f3d95c3-86ed-6d8b-9648-51beee3f6667.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0f3d95c3-86ed-6d8b-9648-51beee3f6667.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0f3d95c3-86ed-6d8b-9648-51beee3f6667.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchInBandEmissionMarginArray Method

RFmxLteMXModAccResultsFetchInBandEmissionMarginArray Method

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchInBandEmissionMarginArray(
	string selectorString,
	double timeout,
	ref double[] inBandEmissionMargin
)
```

```text
Public Function FetchInBandEmissionMarginArray ( 
	selectorString As String,
	timeout As Double,
	ByRef inBandEmissionMargin As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **inBandEmissionMargin**
  - Type: SystemDouble Upon return, contains the array of the in-band emission margins. The margin is the least difference between the in-band emission measurement trace and limit trace. The limit is defined in section 6.5.2.3.5 of the 3GPP TS 36.521 specification. The in-band emissions are a measure of the interference falling into the non-allocated resources blocks.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0f4a7d51-a680-8514-cd70-0055c93f537e.htm language=enus -->
## TOPIC 00026: rfmxltedotnet/html/0f4a7d51-a680-8514-cd70-0055c93f537e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0f4a7d51-a680-8514-cd70-0055c93f537e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0f4a7d51-a680-8514-cd70-0055c93f537e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.SetOffPowerExclusionAfter Method

RFmxLteMXPvtConfigurationSetOffPowerExclusionAfter Method

Sets the time excluded from the Off region after the burst. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffPowerExclusionAfter(
	string selectorString,
	double value
)
```

```text
Public Function SetOffPowerExclusionAfter ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the time excluded from the Off region after the burst. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PvtOffPowerExclusionAfter

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0f547461-7cfe-e370-b468-75648fbeb0d7.htm language=enus -->
## TOPIC 00027: rfmxltedotnet/html/0f547461-7cfe-e370-b468-75648fbeb0d7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0f547461-7cfe-e370-b468-75648fbeb0d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0f547461-7cfe-e370-b468-75648fbeb0d7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetLaaStartingSubframe Method

RFmxLteMXComponentCarrierGetLaaStartingSubframe Method

Gets the starting subframe of an LAA burst.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLaaStartingSubframe(
	string selectorString,
	out int value
)
```

```text
Public Function GetLaaStartingSubframe ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the starting subframe of an LAA burst.

###### Return Value

Int32

##### Remarks

LaaStartingSubframe

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0fa486c7-5464-4740-11b7-081f943c01f7.htm language=enus -->
## TOPIC 00028: rfmxltedotnet/html/0fa486c7-5464-4740-11b7-081f943c01f7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0fa486c7-5464-4740-11b7-081f943c01f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0fa486c7-5464-4740-11b7-081f943c01f7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtResults.GetMeasurementStatus Method

RFmxLteMXPvtResultsGetMeasurementStatus Method

Gets the measurement status indicating whether the power before and after the burst is within the standard defined limit. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxLteMXPvtMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXPvtMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPvtMeasurementStatusUpon return, contains the measurement status indicating whether the power before and after the burst is within the standard defined limit. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

PvtResultsMeasurementStatus

##### See Also

###### Reference

RFmxLteMXPvtResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0fb80b2f-f36d-62c6-9b03-7ac77e91d4bc.htm language=enus -->
## TOPIC 00029: rfmxltedotnet/html/0fb80b2f-f36d-62c6-9b03-7ac77e91d4bc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0fb80b2f-f36d-62c6-9b03-7ac77e91d4bc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0fb80b2f-f36d-62c6-9b03-7ac77e91d4bc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetSequentialFftSize Method

RFmxLteMXAcpConfigurationSetSequentialFftSize Method

SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod)

SequentialFft

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Specifies the FFT size, when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft.

###### Return Value

Int32

##### Remarks

AcpSequentialFftSize

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/0fdf1804-7ea2-e0b4-574b-c3c56ebcff21.htm language=enus -->
## TOPIC 00030: rfmxltedotnet/html/0fdf1804-7ea2-e0b4-574b-c3c56ebcff21.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/0fdf1804-7ea2-e0b4-574b-c3c56ebcff21.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/0fdf1804-7ea2-e0b4-574b-c3c56ebcff21.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObw.Configuration Property

RFmxLteMXObwConfiguration Property

RFmxLteMXObwConfiguration

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXObwConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxLteMXObwConfiguration
	Get
```

###### Property Value

RFmxLteMXObwConfiguration

##### See Also

###### Reference

RFmxLteMXObw Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/1036f1f4-305b-5bc7-fb25-9b2832fb2cb6.htm language=enus -->
## TOPIC 00031: rfmxltedotnet/html/1036f1f4-305b-5bc7-fb25-9b2832fb2cb6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/1036f1f4-305b-5bc7-fb25-9b2832fb2cb6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/1036f1f4-305b-5bc7-fb25-9b2832fb2cb6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetInBandEmissionMargin Method

RFmxLteMXModAccResultsGetInBandEmissionMargin Method

Gets the in-band emission margin. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetInBandEmissionMargin(
	string selectorString,
	out double value
)
```

```text
Public Function GetInBandEmissionMargin ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the in-band emission margin. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsInBandEmissionMargin

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/104bc655-2fc8-6f2f-cc52-6fa34b0498f2.htm language=enus -->
## TOPIC 00032: rfmxltedotnet/html/104bc655-2fc8-6f2f-cc52-6fa34b0498f2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/104bc655-2fc8-6f2f-cc52-6fa34b0498f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/104bc655-2fc8-6f2f-cc52-6fa34b0498f2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.ValidateNoiseCalibrationData Method

RFmxLteMXChpConfigurationValidateNoiseCalibrationData Method

Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorString parameter.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ValidateNoiseCalibrationData(
	string selectorString,
	out RFmxLteMXChpNoiseCalibrationDataValid noiseCalibrationDataValid
)
```

```text
Public Function ValidateNoiseCalibrationData ( 
	selectorString As String,
	<OutAttribute> ByRef noiseCalibrationDataValid As RFmxLteMXChpNoiseCalibrationDataValid
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **noiseCalibrationDataValid**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpNoiseCalibrationDataValid Returns whether the calibration data is valid.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/10719605-472d-ae68-b714-ec901b602af1.htm language=enus -->
## TOPIC 00033: rfmxltedotnet/html/10719605-472d-ae68-b714-ec901b602af1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/10719605-472d-ae68-b714-ec901b602af1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/10719605-472d-ae68-b714-ec901b602af1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAcc Class

RFmxLteMXModAcc Class

Represents the ModAcc measurement.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXModAcc : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXModAcc
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXModAcc type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
|  | Results | Gets the RFmxLteMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Top

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

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/1091a146-d354-a854-b44c-c7b55ba92bc6.htm language=enus -->
## TOPIC 00034: rfmxltedotnet/html/1091a146-d354-a854-b44c-c7b55ba92bc6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/1091a146-d354-a854-b44c-c7b55ba92bc6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/1091a146-d354-a854-b44c-c7b55ba92bc6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetMeasurementEnabled Method

RFmxLteMXModAccConfigurationGetMeasurementEnabled Method

Gets whether to enable the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/114ccb9f-2eb1-9189-aa2f-6d836072c41d.htm language=enus -->
## TOPIC 00035: rfmxltedotnet/html/114ccb9f-2eb1-9189-aa2f-6d836072c41d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/114ccb9f-2eb1-9189-aa2f-6d836072c41d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/114ccb9f-2eb1-9189-aa2f-6d836072c41d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXDownlinkAutoCellIDDetectionEnabled Enumeration

RFmxLteMXDownlinkAutoCellIDDetectionEnabled Enumeration

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXDownlinkAutoCellIDDetectionEnabled
```

```text
Public Enumeration RFmxLteMXDownlinkAutoCellIDDetectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the cell ID you configure. |
|  | True | 1 | The measurement autodetects the cell ID. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/1175fb3c-e176-0514-d398-c54f79fa61df.htm language=enus -->
## TOPIC 00036: rfmxltedotnet/html/1175fb3c-e176-0514-d398-c54f79fa61df.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/1175fb3c-e176-0514-d398-c54f79fa61df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/1175fb3c-e176-0514-d398-c54f79fa61df.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetResultFetchTimeout Method

RFmxLteMXGetResultFetchTimeout Method

Gets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetResultFetchTimeout(
	string selectorString,
	out double value
)
```

```text
Public Function GetResultFetchTimeout ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/11bdb333-f3d1-bfb4-56c7-66a81bb9e5da.htm language=enus -->
## TOPIC 00037: rfmxltedotnet/html/11bdb333-f3d1-bfb4-56c7-66a81bb9e5da.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/11bdb333-f3d1-bfb4-56c7-66a81bb9e5da.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/11bdb333-f3d1-bfb4-56c7-66a81bb9e5da.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChp Methods

RFmxLteMXChp Methods

The [RFmxLteMXChp](d6a0fb9d-e6dc-14a7-dce2-20fd0b1c58a1.htm) type exposes the following members.

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

RFmxLteMXChp Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/11d3757a-1802-0e7b-0499-7ebb8b6420fa.htm language=enus -->
## TOPIC 00038: rfmxltedotnet/html/11d3757a-1802-0e7b-0499-7ebb8b6420fa.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/11d3757a-1802-0e7b-0499-7ebb8b6420fa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/11d3757a-1802-0e7b-0499-7ebb8b6420fa.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPsschConstellationTrace Method

RFmxLteMXModAccResultsFetchPsschConstellationTrace Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPsschConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] dataConstellation,
	ref ComplexSingle[] dmrsConstellation
)
```

```text
Public Function FetchPsschConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef dataConstellation As ComplexSingle(),
	ByRef dmrsConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **dataConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the PSSCH data constellation trace.
- **dmrsConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the PSSCH demodulation reference signal (DMRS) constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/12ba9d97-a072-fcd1-739f-25f5e19a1e36.htm language=enus -->
## TOPIC 00039: rfmxltedotnet/html/12ba9d97-a072-fcd1-739f-25f5e19a1e36.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/12ba9d97-a072-fcd1-739f-25f5e19a1e36.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/12ba9d97-a072-fcd1-739f-25f5e19a1e36.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPuschMaximumPeakDmrsEvm Method

RFmxLteMXModAccResultsGetPuschMaximumPeakDmrsEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschMaximumPeakDmrsEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetPuschMaximumPeakDmrsEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the maximum value of the peak EVMs calculated on PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsPuschMaximumPeakDmrsEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/12ed6e3e-b772-ee0e-4f9f-7956c667b9ac.htm language=enus -->
## TOPIC 00040: rfmxltedotnet/html/12ed6e3e-b772-ee0e-4f9f-7956c667b9ac.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/12ed6e3e-b772-ee0e-4f9f-7956c667b9ac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/12ed6e3e-b772-ee0e-4f9f-7956c667b9ac.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpResults.GetPeakPowerMaximum Method

RFmxLteMXTxpResultsGetPeakPowerMaximum Method

Gets the peak power of the acquired signal.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the acquired signal.

###### Return Value

Int32

##### Remarks

TxpResultsPeakPowerMaximum

##### See Also

###### Reference

RFmxLteMXTxpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/13f6a3c1-8b5a-ab88-f628-b1989dbb6abe.htm language=enus -->
## TOPIC 00041: rfmxltedotnet/html/13f6a3c1-8b5a-ab88-f628-b1989dbb6abe.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/13f6a3c1-8b5a-ab88-f628-b1989dbb6abe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/13f6a3c1-8b5a-ab88-f628-b1989dbb6abe.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetAveragingCount Method

RFmxLteMXTxpConfigurationSetAveragingCount Method

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Specifies the number of acquisitions used for averaging when Averaging Enabled is True.

###### Return Value

Int32

##### Remarks

TxpAveragingCount

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/14498156-387a-c2e8-bd46-c321cbb6a564.htm language=enus -->
## TOPIC 00042: rfmxltedotnet/html/14498156-387a-c2e8-bd46-c321cbb6a564.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/14498156-387a-c2e8-bd46-c321cbb6a564.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/14498156-387a-c2e8-bd46-c321cbb6a564.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetMeasurementOffset Method

RFmxLteMXTxpConfigurationGetMeasurementOffset Method

Gets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDoubleUpon return, contains the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TxpMeasurementOffset

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/1957b0c0-55ba-0b67-3190-879cc5b492b8.htm language=enus -->
## TOPIC 00043: rfmxltedotnet/html/1957b0c0-55ba-0b67-3190-879cc5b492b8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/1957b0c0-55ba-0b67-3190-879cc5b492b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/1957b0c0-55ba-0b67-3190-879cc5b492b8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetMeasurementOffset Method

RFmxLteMXTxpConfigurationSetMeasurementOffset Method

Sets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetMeasurementOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TxpMeasurementOffset

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/1bca98d4-455d-65fb-0491-80b8af5e5e67.htm language=enus -->
## TOPIC 00044: rfmxltedotnet/html/1bca98d4-455d-65fb-0491-80b8af5e5e67.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/1bca98d4-455d-65fb-0491-80b8af5e5e67.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/1bca98d4-455d-65fb-0491-80b8af5e5e67.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList Class

RFmxLteMXList Class

Defines a root class which is used to identify and control Lte list.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXList : IList, 
	IDisposable
```

```text
Public NotInheritable Class RFmxLteMXList
	Implements IList, IDisposable
```

The RFmxLteMXList type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsDisposed | Gets a value that indicates whether the list has been disposed. |
|  | ListName | Gets the list name. |
|  | ListType | Gets the Type object for RFmxLteMXList. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with list instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(String, String) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current list instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxLTE commits settings to the hardware when you call the Initiate(String, String) method. |
|  | CreateListStep | Creates a new list step instance in a list. |
|  | DeleteList | Deletes an instance of a list. |
|  | Dispose | Deletes the list and clears any trace of the current list, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetListStep | Returns a list step instance in a list. |
|  | GetListStepAll | Returns all list step instances in a list. |
|  | GetListStepRange | Returns a range of list step instances in a list. |
|  | GetNumberOfSteps | Returns number of list step instances in a list. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the list and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetToDefault | Resets a list to the default values. |
|  | SetNumberOfSteps | Sets number of list step instances in a list. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/201be21c-393d-40ea-9da3-9e2eca3ac3d8.htm language=enus -->
## TOPIC 00045: rfmxltedotnet/html/201be21c-393d-40ea-9da3-9e2eca3ac3d8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/201be21c-393d-40ea-9da3-9e2eca3ac3d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/201be21c-393d-40ea-9da3-9e2eca3ac3d8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.WaitForMeasurementComplete Method

RFmxLteMXListWaitForMeasurementComplete Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDouble Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/23e69356-bbd7-3de9-62d6-fba0ab7ba3da.htm language=enus -->
## TOPIC 00046: rfmxltedotnet/html/23e69356-bbd7-3de9-62d6-fba0ab7ba3da.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/23e69356-bbd7-3de9-62d6-fba0ab7ba3da.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/23e69356-bbd7-3de9-62d6-fba0ab7ba3da.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetMeasurementMode Method

RFmxLteMXChpConfigurationSetMeasurementMode Method

Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementMode(
	string selectorString,
	RFmxLteMXChpMeasurementMode value
)
```

```text
Public Function SetMeasurementMode ( 
	selectorString As String,
	value As RFmxLteMXChpMeasurementMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpMeasurementModeSpecifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

ChpMeasurementMode

Measure

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/23f026b9-73c7-9dab-994a-547a07f56bb0.htm language=enus -->
## TOPIC 00047: rfmxltedotnet/html/23f026b9-73c7-9dab-994a-547a07f56bb0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/23f026b9-73c7-9dab-994a-547a07f56bb0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/23f026b9-73c7-9dab-994a-547a07f56bb0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPsschNumberOfResourceBlocks Method

RFmxLteMXComponentCarrierSetPsschNumberOfResourceBlocks Method

Sets the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPsschNumberOfResourceBlocks(
	string selectorString,
	int value
)
```

```text
Public Function SetPsschNumberOfResourceBlocks ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation.

###### Return Value

Int32

##### Remarks

PsschNumberOfResourceBlocks

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/243db204-643b-424d-7045-c4677d9c81c2.htm language=enus -->
## TOPIC 00048: rfmxltedotnet/html/243db204-643b-424d-7045-c4677d9c81c2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/243db204-643b-424d-7045-c4677d9c81c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/243db204-643b-424d-7045-c4677d9c81c2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.ClearNamedResult Method

RFmxLteMXListClearNamedResult Method

selectorString

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ClearNamedResult(
	string selectorString
)
```

```text
Public Function ClearNamedResult ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/25da387e-e15d-c9e3-3ed2-b940bd31a86e.htm language=enus -->
## TOPIC 00049: rfmxltedotnet/html/25da387e-e15d-c9e3-3ed2-b940bd31a86e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/25da387e-e15d-c9e3-3ed2-b940bd31a86e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/25da387e-e15d-c9e3-3ed2-b940bd31a86e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetRbwFilterAutoBandwidth Method

RFmxLteMXAcpConfigurationGetRbwFilterAutoBandwidth Method

Gets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterAutoBandwidth(
	string selectorString,
	out RFmxLteMXAcpRbwAutoBandwidth value
)
```

```text
Public Function GetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAcpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpRbwAutoBandwidthUpon return, contains whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

AcpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/270bce9b-cc89-16a1-957e-be43e8a93a2a.htm language=enus -->
## TOPIC 00050: rfmxltedotnet/html/270bce9b-cc89-16a1-957e-be43e8a93a2a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/270bce9b-cc89-16a1-957e-be43e8a93a2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/270bce9b-cc89-16a1-957e-be43e8a93a2a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpResults Class

RFmxLteMXTxpResults Class

Provides methods to fetch and read the TXP measurement results.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXTxpResults : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXTxpResults
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXTxpResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Fetches the average power and peak power of the the signal over which power measurments are performed. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPowerTrace | Fetches power versus time trace. |
|  | GetAveragePowerMean | Gets the average power of the acquired signal. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPeakPowerMaximum | Gets the peak power of the acquired signal. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/279a459c-0061-9d31-6753-05b7a400986c.htm language=enus -->
## TOPIC 00051: rfmxltedotnet/html/279a459c-0061-9d31-6753-05b7a400986c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/279a459c-0061-9d31-6753-05b7a400986c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/279a459c-0061-9d31-6753-05b7a400986c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList Properties

RFmxLteMXList Properties

The [RFmxLteMXList](1bca98d4-455d-65fb-0491-80b8af5e5e67.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsDisposed | Gets a value that indicates whether the list has been disposed. |
|  | ListName | Gets the list name. |
|  | ListType | Gets the Type object for RFmxLteMXList. |

Top

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/27d674d3-af5e-0485-c0b7-bb0385f3c0f2.htm language=enus -->
## TOPIC 00052: rfmxltedotnet/html/27d674d3-af5e-0485-c0b7-bb0385f3c0f2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/27d674d3-af5e-0485-c0b7-bb0385f3c0f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/27d674d3-af5e-0485-c0b7-bb0385f3c0f2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpResults.GetTotalAggregatedPower Method

RFmxLteMXAcpResultsGetTotalAggregatedPower Method

Gets the total power of all the frequency bins over the integration bandwidths of all subblocks. The total power includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTotalAggregatedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetTotalAggregatedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the sum of powers of all the frequency bins over the integration bandwidth of subblock. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps. When you set the RFmxLteMXAcpPowerUnits method to dBm, the method returns the total integrated power in dBm of all the active carriers measured. When you set the RFmxLteMXAcpPowerUnits method to dBm/Hz, the method returns the power spectral density in dBm/Hz based on the power in all the active carriers measured.

###### Return Value

Int32

##### Remarks

AcpResultsTotalAggregatedPower

##### See Also

###### Reference

RFmxLteMXAcpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/27d74351-3c79-61a0-b932-98fd206d5e7d.htm language=enus -->
## TOPIC 00053: rfmxltedotnet/html/27d74351-3c79-61a0-b932-98fd206d5e7d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/27d74351-3c79-61a0-b932-98fd206d5e7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/27d74351-3c79-61a0-b932-98fd206d5e7d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpNoiseCalibrationMode Enumeration

RFmxLteMXAcpNoiseCalibrationMode Enumeration

Specifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAcpNoiseCalibrationMode
```

```text
Public Enumeration RFmxLteMXAcpNoiseCalibrationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Manual | 0 | When you set the SetMeasurementMode(String, RFmxLteMXAcpMeasurementMode) method to Calibrate Noise Floor, you can initiate instrument noise calibration for ACP manually. When you set the ACP Meas Mode method to Measure, you can initiate the ACP measurement manually. |
|  | Auto | 1 | When you set the SetNoiseCompensationEnabled(String, RFmxLteMXAcpNoiseCompensationEnabled) method to True, the RFmx driver sets the Input Isolation Enabled method to Enabled and calibrates the instrument noise in the current state of the instrument. After that, the RFmx driver resets Input Isolation Enabled method and performs the ACP measurement including compensation for the noise contribution of the instrument. The RFmx driver skips noise calibration in this mode if valid noise calibration data is already cached. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2a75511a-8f4d-5f51-cb57-bd0b04426c34.htm language=enus -->
## TOPIC 00054: rfmxltedotnet/html/2a75511a-8f4d-5f51-cb57-bd0b04426c34.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2a75511a-8f4d-5f51-cb57-bd0b04426c34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2a75511a-8f4d-5f51-cb57-bd0b04426c34.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.ListType Property

RFmxLteMXListListType Property

Type

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2e444181-72da-a84f-7adc-cbaa4256f325.htm language=enus -->
## TOPIC 00055: rfmxltedotnet/html/2e444181-72da-a84f-7adc-cbaa4256f325.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2e444181-72da-a84f-7adc-cbaa4256f325.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2e444181-72da-a84f-7adc-cbaa4256f325.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetMeasurementEnabled Method

RFmxLteMXTxpConfigurationSetMeasurementEnabled Method

Sets whether to enable the Transmit Power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanSpecifies whether to enable the Transmit Power (TXP) measurement.

###### Return Value

Int32

##### Remarks

TxpMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2eca0a6c-3c45-adb6-a266-c85d34ab168a.htm language=enus -->
## TOPIC 00056: rfmxltedotnet/html/2eca0a6c-3c45-adb6-a266-c85d34ab168a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2eca0a6c-3c45-adb6-a266-c85d34ab168a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2eca0a6c-3c45-adb6-a266-c85d34ab168a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.SetNumberOfSteps Method

RFmxLteMXListSetNumberOfSteps Method

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2ed11f31-dec9-11b1-2cf6-e838cba94cf7.htm language=enus -->
## TOPIC 00057: rfmxltedotnet/html/2ed11f31-dec9-11b1-2cf6-e838cba94cf7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2ed11f31-dec9-11b1-2cf6-e838cba94cf7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2ed11f31-dec9-11b1-2cf6-e838cba94cf7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchMaximumEvmPerSlotTrace Method

RFmxLteMXModAccResultsFetchMaximumEvmPerSlotTrace Method

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMaximumEvmPerSlotTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> maximumEvmPerSlot
)
```

```text
Public Function FetchMaximumEvmPerSlotTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef maximumEvmPerSlot As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **maximumEvmPerSlot**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the peak value of an EVM for each slot computed across all the symbols and all the allocated subcarriers.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2efb7126-d9b9-3b2a-9120-404a9e61a0c6.htm language=enus -->
## TOPIC 00058: rfmxltedotnet/html/2efb7126-d9b9-3b2a-9120-404a9e61a0c6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2efb7126-d9b9-3b2a-9120-404a9e61a0c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2efb7126-d9b9-3b2a-9120-404a9e61a0c6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSrsMaximumUpPtsEnabled Enumeration

RFmxLteMXSrsMaximumUpPtsEnabled Enumeration

3GPP 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXSrsMaximumUpPtsEnabled
```

```text
Public Enumeration RFmxLteMXSrsMaximumUpPtsEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | In special subframe, SRS is transmitted in RBs specified by SRS bandwidth configurations. |
|  | True | 1 | In special subframe, SRS is transmitted in all possible RBs. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2f97b71b-99c0-add0-1def-05dbb31eddaa.htm language=enus -->
## TOPIC 00059: rfmxltedotnet/html/2f97b71b-99c0-add0-1def-05dbb31eddaa.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2f97b71b-99c0-add0-1def-05dbb31eddaa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2f97b71b-99c0-add0-1def-05dbb31eddaa.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetSelectedPorts Method

RFmxLteMXGetSelectedPorts Method

Valid values

Default values

Supported devices: PXIe-5820/5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringUpon return, contains the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names.

###### Return Value

Int32

##### Remarks

SelectedPorts

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/2febab45-9c2a-4244-239c-142ac5b3303c.htm language=enus -->
## TOPIC 00060: rfmxltedotnet/html/2febab45-9c2a-4244-239c-142ac5b3303c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/2febab45-9c2a-4244-239c-142ac5b3303c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/2febab45-9c2a-4244-239c-142ac5b3303c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.GetSweepTimeAuto Method

RFmxLteMXObwConfigurationGetSweepTimeAuto Method

Gets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxLteMXObwSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXObwSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwSweepTimeAutoUpon return, contains whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

ObwSweepTimeAuto

True

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/30c2c826-39e1-eb17-6b9c-15412802831d.htm language=enus -->
## TOPIC 00061: rfmxltedotnet/html/30c2c826-39e1-eb17-6b9c-15412802831d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/30c2c826-39e1-eb17-6b9c-15412802831d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/30c2c826-39e1-eb17-6b9c-15412802831d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetUplinkDownlinkConfiguration Method

RFmxLteMXGetUplinkDownlinkConfiguration Method

3GPP TS 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkDownlinkConfiguration(
	string selectorString,
	out RFmxLteMXUplinkDownlinkConfiguration value
)
```

```text
Public Function GetUplinkDownlinkConfiguration ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXUplinkDownlinkConfiguration
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXUplinkDownlinkConfiguration Upon return, contains the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame.

###### Return Value

Int32

##### Remarks

UplinkDownlinkConfiguration

Configuration0

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/31d2b8cf-63c5-ff86-81f2-5091b80e055c.htm language=enus -->
## TOPIC 00062: rfmxltedotnet/html/31d2b8cf-63c5-ff86-81f2-5091b80e055c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/31d2b8cf-63c5-ff86-81f2-5091b80e055c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/31d2b8cf-63c5-ff86-81f2-5091b80e055c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetSrsEnabled Method

RFmxLteMXComponentCarrierGetSrsEnabled Method

Gets whether the LTE signal getting measured contains SRS transmission.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSrsEnabled(
	string selectorString,
	out RFmxLteMXSrsEnabled value
)
```

```text
Public Function GetSrsEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSrsEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSrsEnabledUpon return, contains whether the LTE signal getting measured contains SRS transmission.

###### Return Value

Int32

##### Remarks

SrsEnabled

False

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/31e8cdeb-6227-02c4-08b7-24433fb20c52.htm language=enus -->
## TOPIC 00063: rfmxltedotnet/html/31e8cdeb-6227-02c4-08b7-24433fb20c52.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/31e8cdeb-6227-02c4-08b7-24433fb20c52.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/31e8cdeb-6227-02c4-08b7-24433fb20c52.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwResults.FetchSpectrum Method

RFmxLteMXObwResultsFetchSpectrum Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **spectrum**
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the spectrum.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXObwResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/334f39be-803f-97b6-4d5d-880ba2aa1425.htm language=enus -->
## TOPIC 00064: rfmxltedotnet/html/334f39be-803f-97b6-4d5d-880ba2aa1425.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/334f39be-803f-97b6-4d5d-880ba2aa1425.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/334f39be-803f-97b6-4d5d-880ba2aa1425.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetBandwidth Method

RFmxLteMXComponentCarrierSetBandwidth Method

Sets the channel bandwidth of the signal being measured. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the channel bandwidth of the signal being measured. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SetBandwidth(String, Double)

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/34051873-b5f7-e129-57cf-232df58d5b4e.htm language=enus -->
## TOPIC 00065: rfmxltedotnet/html/34051873-b5f7-e129-57cf-232df58d5b4e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/34051873-b5f7-e129-57cf-232df58d5b4e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/34051873-b5f7-e129-57cf-232df58d5b4e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.FetchUpperOffsetMargin Method

RFmxLteMXSemResultsFetchUpperOffsetMargin Method

LTE Uplink Spectral Emission Mask

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUpperOffsetMargin(
	string selectorString,
	double timeout,
	out RFmxLteMXSemUpperOffsetMeasurementStatus measurementStatus,
	out double margin,
	out double marginFrequency,
	out double marginAbsolutePower,
	out double marginRelativePower
)
```

```text
Public Function FetchUpperOffsetMargin ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxLteMXSemUpperOffsetMeasurementStatus,
	<OutAttribute> ByRef margin As Double,
	<OutAttribute> ByRef marginFrequency As Double,
	<OutAttribute> ByRef marginAbsolutePower As Double,
	<OutAttribute> ByRef marginRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemUpperOffsetMeasurementStatus Upon return, contains the measurement status indicating whether the power before and after the burst is within the standard defined limit.
- **margin**
  - Type: SystemDouble Upon return, contains the margin from the standard defined absolute limit mask for upper offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginFrequency**
  - Type: SystemDouble Upon return, contains the frequency at which the margin occurs in the upper offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginAbsolutePower**
  - Type: SystemDouble Upon return, contains the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginRelativePower**
  - Type: SystemDouble Upon return, contains the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the GetTotalAggregatedPower(String, Double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/34195b8c-f97f-ab1b-67bf-124f110307a3.htm language=enus -->
## TOPIC 00066: rfmxltedotnet/html/34195b8c-f97f-ab1b-67bf-124f110307a3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/34195b8c-f97f-ab1b-67bf-124f110307a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/34195b8c-f97f-ab1b-67bf-124f110307a3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpResults Methods

RFmxLteMXChpResults Methods

The [RFmxLteMXChpResults](568020b6-fc99-6341-5a2c-0c6397caa366.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchSpectrum | Fetches the spectrum used for CHP measurements. |
|  | FetchSubblockMeasurement | Returns the power, integration bandwidth and center frequency of the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchTotalAggregatedPower | Fetches the sum of powers in all the subblocks. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetSubblockFrequency | Gets the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
|  | GetSubblockIntegrationBandwidth | Gets the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
|  | GetSubblockPower | Gets the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
|  | GetTotalAggregatedPower | Gets the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXChpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/352a564d-d8e5-d364-9f02-0e2dce9ad8c2.htm language=enus -->
## TOPIC 00067: rfmxltedotnet/html/352a564d-d8e5-d364-9f02-0e2dce9ad8c2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/352a564d-d8e5-d364-9f02-0e2dce9ad8c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/352a564d-d8e5-d364-9f02-0e2dce9ad8c2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.GetAveragingEnabled Method

RFmxLteMXChpConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the CHP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxLteMXChpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXChpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpAveragingEnabledUpon return, contains whether to enable averaging for the CHP measurement.

###### Return Value

Int32

##### Remarks

ChpAveragingEnabled

False

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/35ff25e6-e858-18a5-1afe-9eb96c5b3484.htm language=enus -->
## TOPIC 00068: rfmxltedotnet/html/35ff25e6-e858-18a5-1afe-9eb96c5b3484.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/35ff25e6-e858-18a5-1afe-9eb96c5b3484.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/35ff25e6-e858-18a5-1afe-9eb96c5b3484.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchSpectralFlatness Method

RFmxLteMXModAccResultsFetchSpectralFlatness Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSpectralFlatness(
	string selectorString,
	double timeout,
	out double range1MaximumToRange1Minimum,
	out double range2MaximumToRange2Minimum,
	out double range1MaximumToRange2Minimum,
	out double range2MaximumToRange1Minimum
)
```

```text
Public Function FetchSpectralFlatness ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef range1MaximumToRange1Minimum As Double,
	<OutAttribute> ByRef range2MaximumToRange2Minimum As Double,
	<OutAttribute> ByRef range1MaximumToRange2Minimum As Double,
	<OutAttribute> ByRef range2MaximumToRange1Minimum As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **range1MaximumToRange1Minimum**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. The frequency Range1 is as defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification.
- **range2MaximumToRange2Minimum**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range2. The frequency Range2 is defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification.
- **range1MaximumToRange2Minimum**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Range2. The frequency Range1 and 2 are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification.
- **range2MaximumToRange1Minimum**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from frequency Range2 to frequency Range1. The frequency Range1 and 2 are defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/376f56ba-5207-f7d2-283e-c297134fd221.htm language=enus -->
## TOPIC 00069: rfmxltedotnet/html/376f56ba-5207-f7d2-283e-c297134fd221.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/376f56ba-5207-f7d2-283e-c297134fd221.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/376f56ba-5207-f7d2-283e-c297134fd221.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpResults.FetchPowerTrace Method

RFmxLteMXTxpResultsFetchPowerTrace Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPowerTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> power
)
```

```text
Public Function FetchPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef power As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the RFmxLTE Build Signal String method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **power**
  - Type: NationalInstrumentsAnalogWaveformSingleUpon return, contains power versus time trace. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXTxpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3793912c-7b60-55bb-130f-60b983c112f9.htm language=enus -->
## TOPIC 00070: rfmxltedotnet/html/3793912c-7b60-55bb-130f-60b983c112f9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3793912c-7b60-55bb-130f-60b983c112f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3793912c-7b60-55bb-130f-60b983c112f9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxp Class

RFmxLteMXTxp Class

Represents the TXP measurement.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXTxp : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXTxp
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXTxp type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXTxpConfiguration instance that provides methods to configure the TXP measurement. |
|  | Results | Gets the RFmxLteMXTxpResults instance that provides methods to fetch and read the TXP measurement results. |

Top

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

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/39b01fbc-c7a2-ab7e-c4cd-95cf2255a55b.htm language=enus -->
## TOPIC 00071: rfmxltedotnet/html/39b01fbc-c7a2-ab7e-c4cd-95cf2255a55b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/39b01fbc-c7a2-ab7e-c4cd-95cf2255a55b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/39b01fbc-c7a2-ab7e-c4cd-95cf2255a55b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetAllTracesEnabled Method

RFmxLteMXTxpConfigurationGetAllTracesEnabled Method

Enables the traces to be stored and retrieved after the TXP measurement is performed.

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanEnables the traces to be stored and retrieved after the TXP measurement is performed.

###### Return Value

Int32

##### Remarks

TxpAllTracesEnabled

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3a4896cf-7a1c-b941-52c3-b5691f27f269.htm language=enus -->
## TOPIC 00072: rfmxltedotnet/html/3a4896cf-7a1c-b941-52c3-b5691f27f269.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3a4896cf-7a1c-b941-52c3-b5691f27f269.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3a4896cf-7a1c-b941-52c3-b5691f27f269.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.ConfigureOffsetAbsoluteLimitArray Method

RFmxLteMXSemConfigurationConfigureOffsetAbsoluteLimitArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetAbsoluteLimitArray(
	string selectorString,
	double[] offsetAbsoluteLimitStart,
	double[] offsetAbsoluteLimitStop
)
```

```text
Public Function ConfigureOffsetAbsoluteLimitArray ( 
	selectorString As String,
	offsetAbsoluteLimitStart As Double(),
	offsetAbsoluteLimitStop As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **offsetAbsoluteLimitStart**
  - Type: SystemDoubleSpecifies the array of the absolute power limits corresponding to the beginning of an offset segment. This value is expressed in dBm.
- **offsetAbsoluteLimitStop**
  - Type: SystemDoubleSpecifies the array of the absolute power limits corresponding to the end of an offset segment. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3a809648-c5d7-13af-5947-b7d8497ced0c.htm language=enus -->
## TOPIC 00073: rfmxltedotnet/html/3a809648-c5d7-13af-5947-b7d8497ced0c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3a809648-c5d7-13af-5947-b7d8497ced0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3a809648-c5d7-13af-5947-b7d8497ced0c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.SetDownlinkMaskType Method

RFmxLteMXSemConfigurationSetDownlinkMaskType Method

3GPP 36.141

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDownlinkMaskType(
	string selectorString,
	RFmxLteMXSemDownlinkMaskType value
)
```

```text
Public Function SetDownlinkMaskType ( 
	selectorString As String,
	value As RFmxLteMXSemDownlinkMaskType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemDownlinkMaskType Specifies the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types.

###### Return Value

Int32

##### Remarks

SemDownlinkMaskType

ENodeBCategoryBased

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3b41d0f9-7291-eb80-dbd2-f2a80865514b.htm language=enus -->
## TOPIC 00074: rfmxltedotnet/html/3b41d0f9-7291-eb80-dbd2-f2a80865514b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3b41d0f9-7291-eb80-dbd2-f2a80865514b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3b41d0f9-7291-eb80-dbd2-f2a80865514b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetNPuschFormat Method

RFmxLteMXComponentCarrierSetNPuschFormat Method

Sets the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNPuschFormat(
	string selectorString,
	int value
)
```

```text
Public Function SetNPuschFormat ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information.

###### Return Value

Int32

##### Remarks

NPuschFormat

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3b476ffa-a07b-21dc-1b40-655dcd55e62f.htm language=enus -->
## TOPIC 00075: rfmxltedotnet/html/3b476ffa-a07b-21dc-1b40-655dcd55e62f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3b476ffa-a07b-21dc-1b40-655dcd55e62f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3b476ffa-a07b-21dc-1b40-655dcd55e62f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetMeasurementEnabled Method

RFmxLteMXSemConfigurationGetMeasurementEnabled Method

Gets whether to enable the SEM measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the SEM measurement.

###### Return Value

Int32

##### Remarks

SemMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3b4e20e5-d301-d018-f398-133c172e5a6b.htm language=enus -->
## TOPIC 00076: rfmxltedotnet/html/3b4e20e5-d301-d018-f398-133c172e5a6b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3b4e20e5-d301-d018-f398-133c172e5a6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3b4e20e5-d301-d018-f398-133c172e5a6b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAutoControlChannelPowerDetectionEnabled Enumeration

RFmxLteMXAutoControlChannelPowerDetectionEnabled Enumeration

Specifies whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAutoControlChannelPowerDetectionEnabled
```

```text
Public Enumeration RFmxLteMXAutoControlChannelPowerDetectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, PHICH Power, and PCFICH Power properties that you specify are used for the measurement. |
|  | True | 1 | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, and PCFICH Power properties are auto-detected and used for the measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3b56e1cc-d055-c441-b36f-b2abd20154dc.htm language=enus -->
## TOPIC 00077: rfmxltedotnet/html/3b56e1cc-d055-c441-b36f-b2abd20154dc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3b56e1cc-d055-c441-b36f-b2abd20154dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3b56e1cc-d055-c441-b36f-b2abd20154dc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPowerConfiguration Methods

RFmxLteMXSlotPowerConfiguration Methods

The [RFmxLteMXSlotPowerConfiguration](9f7a39fe-76c3-3c8a-a752-f8d0c2ee85f8.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureMeasurementInterval | Configures the measurementOffset and measurementLength parameters of SlotPower measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. |
|  | GetCommonClockSourceEnabled | Gets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the SlotPower measurement. |
|  | GetMeasurementLength | Gets the number of subframes to be measured. This value is expressed in subframe. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. |
|  | GetSpectrumInverted | Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. |
|  | SetCommonClockSourceEnabled | Sets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
|  | SetMeasurementEnabled | Sets whether to enable the SlotPower measurement. |
|  | SetMeasurementLength | Sets the number of subframes to be measured. This value is expressed in subframe. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. |
|  | SetSpectrumInverted | Sets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXSlotPowerConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3b5c7f75-d2f9-de44-fd10-a690f99c4fa2.htm language=enus -->
## TOPIC 00078: rfmxltedotnet/html/3b5c7f75-d2f9-de44-fd10-a690f99c4fa2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3b5c7f75-d2f9-de44-fd10-a690f99c4fa2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3b5c7f75-d2f9-de44-fd10-a690f99c4fa2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpResults.GetTotalAggregatedPower Method

RFmxLteMXChpResultsGetTotalAggregatedPower Method

Gets the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTotalAggregatedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetTotalAggregatedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps.

###### Return Value

Int32

##### Remarks

ChpResultsTotalAggregatedPower

##### See Also

###### Reference

RFmxLteMXChpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3c9ba511-e112-c39a-20f2-f2433bd4ff3d.htm language=enus -->
## TOPIC 00079: rfmxltedotnet/html/3c9ba511-e112-c39a-20f2-f2433bd4ff3d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3c9ba511-e112-c39a-20f2-f2433bd4ff3d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3c9ba511-e112-c39a-20f2-f2433bd4ff3d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.ComponentCarrier Property

RFmxLteMXSemResultsComponentCarrier Property

RFmxLteMXSemComponentCarrierResults

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXSemComponentCarrierResults ComponentCarrier { get; }
```

```text
Public ReadOnly Property ComponentCarrier As RFmxLteMXSemComponentCarrierResults
	Get
```

###### Property Value

RFmxLteMXSemComponentCarrierResults

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3cd79100-e0a1-f65a-def5-89520741db44.htm language=enus -->
## TOPIC 00080: rfmxltedotnet/html/3cd79100-e0a1-f65a-def5-89520741db44.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3cd79100-e0a1-f65a-def5-89520741db44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3cd79100-e0a1-f65a-def5-89520741db44.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.SetMeasurementEnabled Method

RFmxLteMXSemConfigurationSetMeasurementEnabled Method

Sets whether to enable the SEM measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanSpecifies whether to enable the SEM measurement.

###### Return Value

Int32

##### Remarks

SemMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3ceedf00-9ac0-4fd7-36e5-26e8e7c31350.htm language=enus -->
## TOPIC 00081: rfmxltedotnet/html/3ceedf00-9ac0-4fd7-36e5-26e8e7c31350.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3ceedf00-9ac0-4fd7-36e5-26e8e7c31350.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3ceedf00-9ac0-4fd7-36e5-26e8e7c31350.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetAttributeDouble Method

RFmxLteMXSetAttributeDouble Method

Sets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx LTE Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemDoubleSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3d0ac3cf-3ec1-efea-32a7-5b81bfc634ec.htm language=enus -->
## TOPIC 00082: rfmxltedotnet/html/3d0ac3cf-3ec1-efea-32a7-5b81bfc634ec.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3d0ac3cf-3ec1-efea-32a7-5b81bfc634ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3d0ac3cf-3ec1-efea-32a7-5b81bfc634ec.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetNPuschDmrsDeltaSequenceShift Method

RFmxLteMXComponentCarrierSetNPuschDmrsDeltaSequenceShift Method

3GPP TS 36.211

SetNPuschDmrsGroupHoppingEnabled(String, RFmxLteMXNPuschDmrsGroupHoppingEnabled)

True

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNPuschDmrsDeltaSequenceShift(
	string selectorString,
	int value
)
```

```text
Public Function SetNPuschDmrsDeltaSequenceShift ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This method is valid when you set the SetNPuschDmrsGroupHoppingEnabled(String, RFmxLteMXNPuschDmrsGroupHoppingEnabled) method to True.

###### Return Value

Int32

##### Remarks

NPuschDmrsDeltaSequenceShift

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3d21ccbf-4f09-c15b-81d4-ed64faa30bfd.htm language=enus -->
## TOPIC 00083: rfmxltedotnet/html/3d21ccbf-4f09-c15b-81d4-ed64faa30bfd.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3d21ccbf-4f09-c15b-81d4-ed64faa30bfd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3d21ccbf-4f09-c15b-81d4-ed64faa30bfd.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccSynchronizationMode Enumeration

RFmxLteMXModAccSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or the slot boundary.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccSynchronizationMode
```

```text
Public Enumeration RFmxLteMXModAccSynchronizationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Frame | 0 | The frame boundary is detected, and the measurement is performed over the SetMeasurementLength(String, Int32) method, starting at the SetMeasurementOffset(String, Int32) method from the frame boundary. When you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge, the measurement expects a trigger at the frame boundary. |
|  | Slot | 1 | The slot boundary is detected, and the measurement is performed over the ModAcc Meas Length method starting at the ModAcc Meas Offset method from the slot boundary. When you set the Trigger Type method to DigitalEdge, the measurement expects a trigger at any slot boundary. |
|  | Marker | 2 | The measurement expects a marker (trigger) at the frame boundary from the user. The measurement takes advantage of triggered acquisitions to reduce processing resulting in faster measurement time. Measurement is performed over the ModAcc Meas Length method starting at ModAcc Meas Offset method from the frame boundary. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3d31a6f0-6175-85d7-d4b7-b479a5c775cc.htm language=enus -->
## TOPIC 00084: rfmxltedotnet/html/3d31a6f0-6175-85d7-d4b7-b479a5c775cc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3d31a6f0-6175-85d7-d4b7-b479a5c775cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3d31a6f0-6175-85d7-d4b7-b479a5c775cc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetCenterFrequencyForLimits Method

RFmxLteMXGetCenterFrequencyForLimits Method

Gets the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCenterFrequencyForLimits(
	string selectorString,
	out double value
)
```

```text
Public Function GetCenterFrequencyForLimits ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges of a given subblock. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

CenterFrequencyForLimits

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3d3cb56f-da67-c37d-14a3-0e8c131c111b.htm language=enus -->
## TOPIC 00085: rfmxltedotnet/html/3d3cb56f-da67-c37d-14a3-0e8c131c111b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3d3cb56f-da67-c37d-14a3-0e8c131c111b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3d3cb56f-da67-c37d-14a3-0e8c131c111b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.GetListStepRange Method

RFmxLteMXListGetListStepRange Method

Returns a range of list step instances in a list.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMX GetListStepRange(
	int stepStartIndex,
	int stepStopIndex
)
```

```text
Public Function GetListStepRange ( 
	stepStartIndex As Integer,
	stepStopIndex As Integer
) As RFmxLteMX
```

###### Parameters

- **stepStartIndex**
  - Type: SystemInt32 Pass the starting index of the range of list step.
- **stepStopIndex**
  - Type: SystemInt32 Pass the last index of the range of list step.

###### Return Value

RFmxLteMX

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3d8c6d87-a984-1c90-0160-16e92875fdcf.htm language=enus -->
## TOPIC 00086: rfmxltedotnet/html/3d8c6d87-a984-1c90-0160-16e92875fdcf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3d8c6d87-a984-1c90-0160-16e92875fdcf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3d8c6d87-a984-1c90-0160-16e92875fdcf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXDmrsOccEnabled Enumeration

RFmxLteMXDmrsOccEnabled Enumeration

Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXDmrsOccEnabled
```

```text
Public Enumeration RFmxLteMXDmrsOccEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement ignores the SetPuschCyclicShiftField(String, Int32) and uses the SetPuschNDmrs2(String, Int32) field for DMRS calculations. |
|  | True | 1 | The measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the value of PUSCH n_DMRS_2 and [w(0) w(1)] for DMRS signal based on the values you set for the Cyclic Shift Field and SetTransmitAntennaToAnalyze(String, Int32). |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3dad0b36-27ec-22d4-42f7-895190501ae8.htm language=enus -->
## TOPIC 00087: rfmxltedotnet/html/3dad0b36-27ec-22d4-42f7-895190501ae8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3dad0b36-27ec-22d4-42f7-895190501ae8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3dad0b36-27ec-22d4-42f7-895190501ae8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.ResetToDefault Method

RFmxLteMXResetToDefault Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3dccb52a-d2a2-bece-b63f-115652bac2d2.htm language=enus -->
## TOPIC 00088: rfmxltedotnet/html/3dccb52a-d2a2-bece-b63f-115652bac2d2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3dccb52a-d2a2-bece-b63f-115652bac2d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3dccb52a-d2a2-bece-b63f-115652bac2d2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPhaseConfiguration.GetExclusionPeriodEnabled Method

RFmxLteMXSlotPhaseConfigurationGetExclusionPeriodEnabled Method

3GPP 36.521-1

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetExclusionPeriodEnabled(
	string selectorString,
	out RFmxLteMXSlotPhaseExclusionPeriodEnabled value
)
```

```text
Public Function GetExclusionPeriodEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSlotPhaseExclusionPeriodEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSlotPhaseExclusionPeriodEnabled Upon return, contains whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion.

###### Return Value

Int32

##### Remarks

SlotPhaseExclusionPeriodEnabled

True

##### See Also

###### Reference

RFmxLteMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3dd99fab-0afd-8dbf-2aac-78f4cf4fd985.htm language=enus -->
## TOPIC 00089: rfmxltedotnet/html/3dd99fab-0afd-8dbf-2aac-78f4cf4fd985.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3dd99fab-0afd-8dbf-2aac-78f4cf4fd985.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3dd99fab-0afd-8dbf-2aac-78f4cf4fd985.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetSymbolClockErrorEstimationEnabled Method

RFmxLteMXModAccConfigurationGetSymbolClockErrorEstimationEnabled Method

Gets whether to estimate symbol clock error.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSymbolClockErrorEstimationEnabled(
	string selectorString,
	out RFmxLteMXModAccSymbolClockErrorEstimationEnabled value
)
```

```text
Public Function GetSymbolClockErrorEstimationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccSymbolClockErrorEstimationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccSymbolClockErrorEstimationEnabledUpon return, contains whether to estimate symbol clock error.

###### Return Value

Int32

##### Remarks

ModAccSymbolClockErrorEstimationEnabled

True

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3df92084-55b5-accb-f435-f9ebcf749d1a.htm language=enus -->
## TOPIC 00090: rfmxltedotnet/html/3df92084-55b5-accb-f435-f9ebcf749d1a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3df92084-55b5-accb-f435-f9ebcf749d1a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3df92084-55b5-accb-f435-f9ebcf749d1a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetFftWindowType Method

RFmxLteMXModAccConfigurationSetFftWindowType Method

Sets the FFT window type used for the EVM calculation for the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftWindowType(
	string selectorString,
	RFmxLteMXModAccFftWindowType value
)
```

```text
Public Function SetFftWindowType ( 
	selectorString As String,
	value As RFmxLteMXModAccFftWindowType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccFftWindowTypeSpecifies the FFT window type used for the EVM calculation for the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccFftWindowType

TypeCustom

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/3e7848b9-e4b8-a80a-6d19-08e877caf1a5.htm language=enus -->
## TOPIC 00091: rfmxltedotnet/html/3e7848b9-e4b8-a80a-6d19-08e877caf1a5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/3e7848b9-e4b8-a80a-6d19-08e877caf1a5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/3e7848b9-e4b8-a80a-6d19-08e877caf1a5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetExternalAttenuation Method

RFmxLteMXGetExternalAttenuation Method

NI RF Vector Signal Analyzers Help

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation.

###### Return Value

Int32

##### Remarks

ExternalAttenuation

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/41db6057-6c9a-ed58-fcf6-01cfaafab93f.htm language=enus -->
## TOPIC 00092: rfmxltedotnet/html/41db6057-6c9a-ed58-fcf6-01cfaafab93f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/41db6057-6c9a-ed58-fcf6-01cfaafab93f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/41db6057-6c9a-ed58-fcf6-01cfaafab93f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemOffsetRbwFilterType Enumeration

RFmxLteMXSemOffsetRbwFilterType Enumeration

Specifies the shape of a digital RBW filter.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXSemOffsetRbwFilterType
```

```text
Public Enumeration RFmxLteMXSemOffsetRbwFilterType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FftBased | 0 | No RBW filtering is performed. |
|  | Gaussian | 1 | The RBW filter has a Gaussian response. |
|  | Flat | 2 | The RBW filter has a flat response. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4233f407-cc24-c488-fce5-4ac01040d6de.htm language=enus -->
## TOPIC 00093: rfmxltedotnet/html/4233f407-cc24-c488-fce5-4ac01040d6de.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4233f407-cc24-c488-fce5-4ac01040d6de.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4233f407-cc24-c488-fce5-4ac01040d6de.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.ConfigureCommonClockSourceEnabled Method

RFmxLteMXModAccConfigurationConfigureCommonClockSourceEnabled Method

SetLinkDirection(String, RFmxLteMXLinkDirection)

Downlink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCommonClockSourceEnabled(
	string selectorString,
	RFmxLteMXModAccCommonClockSourceEnabled commonClockSourceEnabled
)
```

```text
Public Function ConfigureCommonClockSourceEnabled ( 
	selectorString As String,
	commonClockSourceEnabled As RFmxLteMXModAccCommonClockSourceEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **commonClockSourceEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccCommonClockSourceEnabledSpecifies whether the same Reference Clock is used for the local oscillator and the D/A converter. When the same Reference Clock is used, the carrier frequency offset is proportional to the Sample Clock error.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4239cc5f-f737-a2f2-a9d6-d5635e555c8f.htm language=enus -->
## TOPIC 00094: rfmxltedotnet/html/4239cc5f-f737-a2f2-a9d6-d5635e555c8f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4239cc5f-f737-a2f2-a9d6-d5635e555c8f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4239cc5f-f737-a2f2-a9d6-d5635e555c8f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetNumberOfAnalysisThreads Method

RFmxLteMXTxpConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism inside TXP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism inside TXP measurement.

###### Return Value

Int32

##### Remarks

TxpNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4259ca8b-d1d6-d413-7fe6-0b049e6c7f19.htm language=enus -->
## TOPIC 00095: rfmxltedotnet/html/4259ca8b-d1d6-d413-7fe6-0b049e6c7f19.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4259ca8b-d1d6-d413-7fe6-0b049e6c7f19.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4259ca8b-d1d6-d413-7fe6-0b049e6c7f19.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPowerResults Class

RFmxLteMXSlotPowerResults Class

Provides methods to fetch and read the SlotPower measurement results.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXSlotPowerResults : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXSlotPowerResults
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXSlotPowerResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchPowers | Fetches the array of Subframe Power and the Subframe Power Delta parameters over the measurement interval. A NaN is returned as subframe power delta, when the preceding slot is not occupied. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/426c68df-0b5a-0f36-4db9-c466dc87afc6.htm language=enus -->
## TOPIC 00096: rfmxltedotnet/html/426c68df-0b5a-0f36-4db9-c466dc87afc6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/426c68df-0b5a-0f36-4db9-c466dc87afc6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/426c68df-0b5a-0f36-4db9-c466dc87afc6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPdsch1024QamEvmArray Method

RFmxLteMXModAccResultsFetchPdsch1024QamEvmArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPdsch1024QamEvmArray(
	string selectorString,
	double timeout,
	ref double[] meanRms1024QamEvm
)
```

```text
Public Function FetchPdsch1024QamEvmArray ( 
	selectorString As String,
	timeout As Double,
	ByRef meanRms1024QamEvm As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRms1024QamEvm**
  - Type: SystemDouble Upon return, contains an array of mean values of the calculated RMS EVMs on all 1024QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the result is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4275d7b0-ec84-c838-42a8-9636564a297f.htm language=enus -->
## TOPIC 00097: rfmxltedotnet/html/4275d7b0-ec84-c838-42a8-9636564a297f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4275d7b0-ec84-c838-42a8-9636564a297f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4275d7b0-ec84-c838-42a8-9636564a297f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.SetAllTracesEnabled Method

RFmxLteMXObwConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the OBW measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanSpecifies whether to enable the traces to be stored and retrieved after performing the OBW measurement.

###### Return Value

Int32

##### Remarks

ObwAllTracesEnabled

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/432bc31f-e77e-36d6-0098-ad03906c60c9.htm language=enus -->
## TOPIC 00098: rfmxltedotnet/html/432bc31f-e77e-36d6-0098-ad03906c60c9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/432bc31f-e77e-36d6-0098-ad03906c60c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/432bc31f-e77e-36d6-0098-ad03906c60c9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.BuildListStepString Method

RFmxLteMXBuildListStepString Method

Creates the list step string.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildListStepString(
	string selectorString,
	string resultName,
	int listStepNumber
)
```

```text
Public Shared Function BuildListStepString ( 
	selectorString As String,
	resultName As String,
	listStepNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the list name. This input accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1"
- **resultName**
  - Type: SystemString Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1"
- **listStepNumber**
  - Type: SystemInt32 Specifies the list step number.

###### Return Value

String

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/45cdf90a-95ca-50e0-3ca0-559245e48b29.htm language=enus -->
## TOPIC 00099: rfmxltedotnet/html/45cdf90a-95ca-50e0-3ca0-559245e48b29.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/45cdf90a-95ca-50e0-3ca0-559245e48b29.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/45cdf90a-95ca-50e0-3ca0-559245e48b29.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetMeasurementInterval Method

RFmxLteMXTxpConfigurationSetMeasurementInterval Method

Sets the measurement interval. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDoubleSpecifies the measurement interval. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TxpMeasurementInterval

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4654f403-6b0e-843c-38ae-7ce7398712e5.htm language=enus -->
## TOPIC 00100: rfmxltedotnet/html/4654f403-6b0e-843c-38ae-7ce7398712e5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4654f403-6b0e-843c-38ae-7ce7398712e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4654f403-6b0e-843c-38ae-7ce7398712e5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXListStepTimerUnit Enumeration

RFmxLteMXListStepTimerUnit Enumeration

SetListStepTimerDuration(String, Double)

SetListStepTimerOffset(String, Double)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXListStepTimerUnit
```

```text
Public Enumeration RFmxLteMXListStepTimerUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Slot | 1 | List Step Timer Duration and List Step Timer Offset are specified in units of slots. |
|  | Time | 6 | List Step Timer Duration and List Step Timer Offset are specified in seconds. Specify the List Step Timer Duration and List Step Timer Offset in multiples of 1 ms * (15 kHz/minimum subcarrier spacing of all carriers). All slots within this notional time duration are analysed. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/480d4e82-7a5c-ad00-2bff-e7ef4e7560ac.htm language=enus -->
## TOPIC 00101: rfmxltedotnet/html/480d4e82-7a5c-ad00-2bff-e7ef4e7560ac.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/480d4e82-7a5c-ad00-2bff-e7ef4e7560ac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/480d4e82-7a5c-ad00-2bff-e7ef4e7560ac.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetSrsISrs Method

RFmxLteMXComponentCarrierGetSrsISrs Method

ISRS

3GPP 36.213

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSrsISrs(
	string selectorString,
	out int value
)
```

```text
Public Function GetSrsISrs ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the SRS configuration index ISRS. It is used to determine the SRS periodicity and SRS subframe offset. It is a UE specific method which defines whether the SRS is transmitted in the subframe reserved for SRS by SRS subframe configuration. Refer to 3GPP 36.213 specification for more details.

###### Return Value

Int32

##### Remarks

SrsISrs

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/483fb55a-20da-845e-63d7-a3343d979c58.htm language=enus -->
## TOPIC 00102: rfmxltedotnet/html/483fb55a-20da-845e-63d7-a3343d979c58.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/483fb55a-20da-845e-63d7-a3343d979c58.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/483fb55a-20da-845e-63d7-a3343d979c58.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAcc Methods

RFmxLteMXModAcc Methods

The [RFmxLteMXModAcc](10719605-472d-ae68-b714-ec901b602af1.htm) type exposes the following members.

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

RFmxLteMXModAcc Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4ab7441a-374b-7eae-30f6-784efad5630a.htm language=enus -->
## TOPIC 00103: rfmxltedotnet/html/4ab7441a-374b-7eae-30f6-784efad5630a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4ab7441a-374b-7eae-30f6-784efad5630a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4ab7441a-374b-7eae-30f6-784efad5630a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccFftWindowType Enumeration

RFmxLteMXModAccFftWindowType Enumeration

Specifies the FFT window type used for the EVM calculation for the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccFftWindowType
```

```text
Public Enumeration RFmxLteMXModAccFftWindowType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Type3GPP | 0 | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The FFT window positions are specified by the method. Refer to the Annexe E.3.2 of 3GPP TS 36.521 specification for more information on the FFT window. |
|  | TypeCustom | 1 | Only one FFT window position is used for the EVM calculation. FFT window position is specified by SetFftWindowOffset(String, Double) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4f5c8ec3-9e62-06da-16d9-92716f54a608.htm language=enus -->
## TOPIC 00104: rfmxltedotnet/html/4f5c8ec3-9e62-06da-16d9-92716f54a608.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4f5c8ec3-9e62-06da-16d9-92716f54a608.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4f5c8ec3-9e62-06da-16d9-92716f54a608.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.SetRbwFilterAutoBandwidth Method

RFmxLteMXObwConfigurationSetRbwFilterAutoBandwidth Method

Sets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAutoBandwidth(
	string selectorString,
	RFmxLteMXObwRbwAutoBandwidth value
)
```

```text
Public Function SetRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxLteMXObwRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwRbwAutoBandwidthSpecifies whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

ObwRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4fc01c5a-4cf7-d66e-b0d6-955e6d2daaf8.htm language=enus -->
## TOPIC 00105: rfmxltedotnet/html/4fc01c5a-4cf7-d66e-b0d6-955e6d2daaf8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4fc01c5a-4cf7-d66e-b0d6-955e6d2daaf8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4fc01c5a-4cf7-d66e-b0d6-955e6d2daaf8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetSpectralFlatnessRange2MaximumToRange2Minimum Method

RFmxLteMXModAccResultsGetSpectralFlatnessRange2MaximumToRange2Minimum Method

Measurement Offset

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectralFlatnessRange2MaximumToRange2Minimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpectralFlatnessRange2MaximumToRange2Minimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Measurement Offset parameter. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsSpectralFlatnessRange2MaximumToRange2Minimum

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/4fe4c060-106f-68e3-e73f-ee055813a628.htm language=enus -->
## TOPIC 00106: rfmxltedotnet/html/4fe4c060-106f-68e3-e73f-ee055813a628.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/4fe4c060-106f-68e3-e73f-ee055813a628.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/4fe4c060-106f-68e3-e73f-ee055813a628.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchMaximumMagnitudeErrorPerSymbolTrace Method

RFmxLteMXModAccResultsFetchMaximumMagnitudeErrorPerSymbolTrace Method

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMaximumMagnitudeErrorPerSymbolTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> maximumMagnitudeErrorPerSymbol
)
```

```text
Public Function FetchMaximumMagnitudeErrorPerSymbolTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef maximumMagnitudeErrorPerSymbol As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **maximumMagnitudeErrorPerSymbol**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the peak value of the magnitude error for each symbol computed across all the allocated subcarriers.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/517e7307-d3b6-3871-3a1a-5818abc74723.htm language=enus -->
## TOPIC 00107: rfmxltedotnet/html/517e7307-d3b6-3871-3a1a-5818abc74723.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/517e7307-d3b6-3871-3a1a-5818abc74723.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/517e7307-d3b6-3871-3a1a-5818abc74723.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetDownlinkMaskType Method

RFmxLteMXSemConfigurationGetDownlinkMaskType Method

3GPP 36.141

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDownlinkMaskType(
	string selectorString,
	out RFmxLteMXSemDownlinkMaskType value
)
```

```text
Public Function GetDownlinkMaskType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSemDownlinkMaskType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemDownlinkMaskType Upon return, contains the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types.

###### Return Value

Int32

##### Remarks

SemDownlinkMaskType

ENodeBCategoryBased

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/526585f1-95ab-2bb8-ae7c-772d51438b8f.htm language=enus -->
## TOPIC 00108: rfmxltedotnet/html/526585f1-95ab-2bb8-ae7c-772d51438b8f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/526585f1-95ab-2bb8-ae7c-772d51438b8f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/526585f1-95ab-2bb8-ae7c-772d51438b8f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpAveragingEnabled Enumeration

RFmxLteMXTxpAveragingEnabled Enumeration

Specifies whether to enable averaging for TXP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXTxpAveragingEnabled
```

```text
Public Enumeration RFmxLteMXTxpAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The number of acquisitions is 1. |
|  | True | 1 | The measurement uses the Averaging Count for the number of acquisitions over which the measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/53897175-0591-20d1-cb0f-46a456f54496.htm language=enus -->
## TOPIC 00109: rfmxltedotnet/html/53897175-0591-20d1-cb0f-46a456f54496.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/53897175-0591-20d1-cb0f-46a456f54496.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/53897175-0591-20d1-cb0f-46a456f54496.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.CheckMeasurementStatus Method

RFmxLteMXListCheckMeasurementStatus Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int CheckMeasurementStatus(
	string selectorString,
	out bool isDone
)
```

```text
Public Function CheckMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef isDone As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **isDone**
  - Type: SystemBoolean Indicates whether the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/53a2c9a6-681f-8e77-db56-f0b12c4433b9.htm language=enus -->
## TOPIC 00110: rfmxltedotnet/html/53a2c9a6-681f-8e77-db56-f0b12c4433b9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/53a2c9a6-681f-8e77-db56-f0b12c4433b9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/53a2c9a6-681f-8e77-db56-f0b12c4433b9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPsschDmrsEvm Method

RFmxLteMXModAccResultsFetchPsschDmrsEvm Method

SetEvmUnit(String, RFmxLteMXModAccEvmUnit)

Percentage

dB

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPsschDmrsEvm(
	string selectorString,
	double timeout,
	out double psschMeanRmsDmrsEvm,
	out double psschMaximumPeakDmrsEvm
)
```

```text
Public Function FetchPsschDmrsEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef psschMeanRmsDmrsEvm As Double,
	<OutAttribute> ByRef psschMaximumPeakDmrsEvm As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **psschMeanRmsDmrsEvm**
  - Type: SystemDouble Upon return, contains the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method.
- **psschMaximumPeakDmrsEvm**
  - Type: SystemDouble Upon return, contains the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/541c6904-3951-ebe6-d790-0465534682ca.htm language=enus -->
## TOPIC 00111: rfmxltedotnet/html/541c6904-3951-ebe6-d790-0465534682ca.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/541c6904-3951-ebe6-d790-0465534682ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/541c6904-3951-ebe6-d790-0465534682ca.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetMulticarrierTimeSynchronizationMode Method

RFmxLteMXModAccConfigurationSetMulticarrierTimeSynchronizationMode Method

Sets the time synchronization mode used in uplink in the case of carrier aggregation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMulticarrierTimeSynchronizationMode(
	string selectorString,
	RFmxLteMXModAccMulticarrierTimeSynchronizationMode value
)
```

```text
Public Function SetMulticarrierTimeSynchronizationMode ( 
	selectorString As String,
	value As RFmxLteMXModAccMulticarrierTimeSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccMulticarrierTimeSynchronizationModeSpecifies the time synchronization mode used in uplink in the case of carrier aggregation.

###### Return Value

Int32

##### Remarks

ModAccMulticarrierTimeSynchronizationMode

Common

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/543fd4e0-15e8-2a9e-2968-4bf5fa0a4d8e.htm language=enus -->
## TOPIC 00112: rfmxltedotnet/html/543fd4e0-15e8-2a9e-2968-4bf5fa0a4d8e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/543fd4e0-15e8-2a9e-2968-4bf5fa0a4d8e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/543fd4e0-15e8-2a9e-2968-4bf5fa0a4d8e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.ConfigureSweepTime Method

RFmxLteMXObwConfigurationConfigureSweepTime Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSweepTime(
	string selectorString,
	RFmxLteMXObwSweepTimeAuto sweepTimeAuto,
	double sweepTimeInterval
)
```

```text
Public Function ConfigureSweepTime ( 
	selectorString As String,
	sweepTimeAuto As RFmxLteMXObwSweepTimeAuto,
	sweepTimeInterval As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sweepTimeAuto**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwSweepTimeAutoSpecifies whether the measurement computes the sweep time.
- **sweepTimeInterval**
  - Type: SystemDouble Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/57fcca3f-a2ec-2429-6df2-18be3bb55299.htm language=enus -->
## TOPIC 00113: rfmxltedotnet/html/57fcca3f-a2ec-2429-6df2-18be3bb55299.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/57fcca3f-a2ec-2429-6df2-18be3bb55299.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/57fcca3f-a2ec-2429-6df2-18be3bb55299.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.FetchLowerOffsetMarginArray Method

RFmxLteMXSemResultsFetchLowerOffsetMarginArray Method

LTE Uplink Spectral Emission Mask

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLowerOffsetMarginArray(
	string selectorString,
	double timeout,
	ref RFmxLteMXSemLowerOffsetMeasurementStatus[] measurementStatus,
	ref double[] margin,
	ref double[] marginFrequency,
	ref double[] marginAbsolutePower,
	ref double[] marginRelativePower
)
```

```text
Public Function FetchLowerOffsetMarginArray ( 
	selectorString As String,
	timeout As Double,
	ByRef measurementStatus As RFmxLteMXSemLowerOffsetMeasurementStatus(),
	ByRef margin As Double(),
	ByRef marginFrequency As Double(),
	ByRef marginAbsolutePower As Double(),
	ByRef marginRelativePower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemLowerOffsetMeasurementStatus Upon return, contains the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit.
- **margin**
  - Type: SystemDouble Upon return, contains the array of margins from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginFrequency**
  - Type: SystemDouble Upon return, contains the array of frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginAbsolutePower**
  - Type: SystemDouble Upon return, contains the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginRelativePower**
  - Type: SystemDouble Upon return, contains the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the GetTotalAggregatedPower(String, Double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/58b64462-a1a4-f9a9-c901-665fc6a28ab5.htm language=enus -->
## TOPIC 00114: rfmxltedotnet/html/58b64462-a1a4-f9a9-c901-665fc6a28ab5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/58b64462-a1a4-f9a9-c901-665fc6a28ab5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/58b64462-a1a4-f9a9-c901-665fc6a28ab5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.ConfigureTransmitAntennaToAnalyze Method

RFmxLteMXConfigureTransmitAntennaToAnalyze Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureTransmitAntennaToAnalyze(
	string selectorString,
	int transmitAntennaToAnalyze
)
```

```text
Public Function ConfigureTransmitAntennaToAnalyze ( 
	selectorString As String,
	transmitAntennaToAnalyze As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **transmitAntennaToAnalyze**
  - Type: SystemInt32Specifies the physical antenna connected to the analyzer.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/58bc376a-01f2-7feb-76d3-d70af4168763.htm language=enus -->
## TOPIC 00115: rfmxltedotnet/html/58bc376a-01f2-7feb-76d3-d70af4168763.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/58bc376a-01f2-7feb-76d3-d70af4168763.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/58bc376a-01f2-7feb-76d3-d70af4168763.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetMulticarrierTimeSynchronizationMode Method

RFmxLteMXModAccConfigurationGetMulticarrierTimeSynchronizationMode Method

Gets the time synchronization mode used in uplink in the case of carrier aggregation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMulticarrierTimeSynchronizationMode(
	string selectorString,
	out RFmxLteMXModAccMulticarrierTimeSynchronizationMode value
)
```

```text
Public Function GetMulticarrierTimeSynchronizationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccMulticarrierTimeSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccMulticarrierTimeSynchronizationMode Upon retrun, the time synchronization mode used in uplink in the case of carrier aggregation.

###### Return Value

Int32

##### Remarks

ModAccMulticarrierTimeSynchronizationMode

Common

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5b9bde39-264d-6867-8ff6-c72c8530232d.htm language=enus -->
## TOPIC 00116: rfmxltedotnet/html/5b9bde39-264d-6867-8ff6-c72c8530232d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5b9bde39-264d-6867-8ff6-c72c8530232d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5b9bde39-264d-6867-8ff6-c72c8530232d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetNPuschNumberOfTones Method

RFmxLteMXComponentCarrierSetNPuschNumberOfTones Method

Sets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH).

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNPuschNumberOfTones(
	string selectorString,
	int value
)
```

```text
Public Function SetNPuschNumberOfTones ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH).

###### Return Value

Int32

##### Remarks

NPuschNumberOfTones

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5d053d97-0df8-9d23-5771-29b3aac72dff.htm language=enus -->
## TOPIC 00117: rfmxltedotnet/html/5d053d97-0df8-9d23-5771-29b3aac72dff.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5d053d97-0df8-9d23-5771-29b3aac72dff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5d053d97-0df8-9d23-5771-29b3aac72dff.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.Commit Method

RFmxLteMXListCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The list name that is passed when creating the list is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5d2bd386-b4e3-4502-68a7-a532e91c96c0.htm language=enus -->
## TOPIC 00118: rfmxltedotnet/html/5d2bd386-b4e3-4502-68a7-a532e91c96c0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5d2bd386-b4e3-4502-68a7-a532e91c96c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5d2bd386-b4e3-4502-68a7-a532e91c96c0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemComponentCarrierResults.GetAbsoluteIntegratedPower Method

RFmxLteMXSemComponentCarrierResultsGetAbsoluteIntegratedPower Method

Gets the sum of powers of all the frequency bins over the integration bandwidth of the carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAbsoluteIntegratedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetAbsoluteIntegratedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the sum of powers of all the frequency bins over the integration bandwidth of the carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

RFmxLteMXSemComponentCarrierResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5d73d4e3-892e-6522-eacc-81315d5fa301.htm language=enus -->
## TOPIC 00119: rfmxltedotnet/html/5d73d4e3-892e-6522-eacc-81315d5fa301.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5d73d4e3-892e-6522-eacc-81315d5fa301.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5d73d4e3-892e-6522-eacc-81315d5fa301.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.BuildSubblockString Method

RFmxLteMXBuildSubblockString Method

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32 Specifies the number of subblocks that are configured in the intra-band non-contiguous carrier aggregation. Set this parameter to 1, which is the default, for single carrier and intra-band contiguous carrier aggregation.

###### Return Value

String

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5ddb973b-894a-bff4-8405-88a292d05595.htm language=enus -->
## TOPIC 00120: rfmxltedotnet/html/5ddb973b-894a-bff4-8405-88a292d05595.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5ddb973b-894a-bff4-8405-88a292d05595.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5ddb973b-894a-bff4-8405-88a292d05595.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPowerConfiguration.SetCommonClockSourceEnabled Method

RFmxLteMXSlotPowerConfigurationSetCommonClockSourceEnabled Method

Sets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCommonClockSourceEnabled(
	string selectorString,
	RFmxLteMXSlotPowerCommonClockSourceEnabled value
)
```

```text
Public Function SetCommonClockSourceEnabled ( 
	selectorString As String,
	value As RFmxLteMXSlotPowerCommonClockSourceEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSlotPowerCommonClockSourceEnabledSpecifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

###### Return Value

Int32

##### Remarks

SlotPowerCommonClockSourceEnabled

True

##### See Also

###### Reference

RFmxLteMXSlotPowerConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5ddfb906-f391-7fd4-8228-519f322424ed.htm language=enus -->
## TOPIC 00121: rfmxltedotnet/html/5ddfb906-f391-7fd4-8228-519f322424ed.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5ddfb906-f391-7fd4-8228-519f322424ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5ddfb906-f391-7fd4-8228-519f322424ed.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetNoiseCompensationType Method

RFmxLteMXAcpConfigurationSetNoiseCompensationType Method

Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCompensationType(
	string selectorString,
	RFmxLteMXAcpNoiseCompensationType value
)
```

```text
Public Function SetNoiseCompensationType ( 
	selectorString As String,
	value As RFmxLteMXAcpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpNoiseCompensationTypeSpecifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

AcpNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5e557c5f-78b5-95ab-f60a-02d528c5a6fe.htm language=enus -->
## TOPIC 00122: rfmxltedotnet/html/5e557c5f-78b5-95ab-f60a-02d528c5a6fe.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5e557c5f-78b5-95ab-f60a-02d528c5a6fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5e557c5f-78b5-95ab-f60a-02d528c5a6fe.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXNPuschModulationType Enumeration

RFmxLteMXNPuschModulationType Enumeration

Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH).

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXNPuschModulationType
```

```text
Public Enumeration RFmxLteMXNPuschModulationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bpsk | 0 | Specifies a BPSK modulation scheme. |
|  | Qpsk | 1 | Specifies a QPSK modulation scheme. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/5e57d625-c455-d5b6-9e6c-5d9f923566d5.htm language=enus -->
## TOPIC 00123: rfmxltedotnet/html/5e57d625-c455-d5b6-9e6c-5d9f923566d5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/5e57d625-c455-d5b6-9e6c-5d9f923566d5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/5e57d625-c455-d5b6-9e6c-5d9f923566d5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXExtension.GetLteSignalConfiguration Method (RFmxInstrMX, String)

RFmxLteMXExtensionGetLteSignalConfiguration Method (RFmxInstrMX, String)

Creates a LTE signal configuration for specified signal name. Existing LTE signal configuration is
 returned if specified signal name exists.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxLteMX GetLteSignalConfiguration(
	this RFmxInstrMX instrSession,
	string signalName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetLteSignalConfiguration ( 
	instrSession As RFmxInstrMX,
	signalName As String
) As RFmxLteMX
```

###### Parameters

- **instrSession**
  - Type: RFmxInstrMXSpecifies an RFmxInstr session.
- **signalName**
  - Type: SystemStringSpecifies a signal name.

###### Return Value

RFmxLteMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxLteMXExtension Class

GetLteSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6130eab5-c110-61b6-2339-f679bd25bccf.htm language=enus -->
## TOPIC 00124: rfmxltedotnet/html/6130eab5-c110-61b6-2339-f679bd25bccf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6130eab5-c110-61b6-2339-f679bd25bccf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6130eab5-c110-61b6-2339-f679bd25bccf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetDuplexScheme Method

RFmxLteMXSetDuplexScheme Method

Sets the duplexing technique of the signal being measured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDuplexScheme(
	string selectorString,
	RFmxLteMXDuplexScheme value
)
```

```text
Public Function SetDuplexScheme ( 
	selectorString As String,
	value As RFmxLteMXDuplexScheme
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXDuplexSchemeSpecifies the duplexing technique of the signal being measured.

###### Return Value

Int32

##### Remarks

DuplexScheme

Fdd

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6323ce88-5493-fd3a-34de-77a134d5a66d.htm language=enus -->
## TOPIC 00125: rfmxltedotnet/html/6323ce88-5493-fd3a-34de-77a134d5a66d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6323ce88-5493-fd3a-34de-77a134d5a66d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6323ce88-5493-fd3a-34de-77a134d5a66d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.DeleteList Method

RFmxLteMXListDeleteList Method

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6377293b-f7e6-d69c-4b53-b77ddd96e851.htm language=enus -->
## TOPIC 00126: rfmxltedotnet/html/6377293b-f7e6-d69c-4b53-b77ddd96e851.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6377293b-f7e6-d69c-4b53-b77ddd96e851.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6377293b-f7e6-d69c-4b53-b77ddd96e851.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.GetListStepAll Method

RFmxLteMXListGetListStepAll Method

Returns all list step instances in a list.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMX GetListStepAll()
```

```text
Public Function GetListStepAll As RFmxLteMX
```

###### Return Value

RFmxLteMX

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/63bf3642-3c67-56f0-fadd-4dff3d7714a7.htm language=enus -->
## TOPIC 00127: rfmxltedotnet/html/63bf3642-3c67-56f0-fadd-4dff3d7714a7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/63bf3642-3c67-56f0-fadd-4dff3d7714a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/63bf3642-3c67-56f0-fadd-4dff3d7714a7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwResults Methods

RFmxLteMXObwResults Methods

The [RFmxLteMXObwResults](6e3cd618-3c59-80fa-5517-65f00a746e1d.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Occupied Bandwidth topic for more information about OBW measurements. |
|  | FetchSpectrum | Fetches the spectrum used for OBW measurements. |
|  | GetAbsolutePower | Gets the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetOccupiedBandwidth | Gets the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
|  | GetStartFrequency | Gets the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Stop frequency - Start frequency = Occupied bandwidthUse "subblock(n)" as the selector string to read this result. |
|  | GetStopFrequency | Gets the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequencyUse "subblock(n)" as the selector string to read this result. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXObwResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/63d6f761-665e-3d87-cd8b-9ea604f6a9e4.htm language=enus -->
## TOPIC 00128: rfmxltedotnet/html/63d6f761-665e-3d87-cd8b-9ea604f6a9e4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/63d6f761-665e-3d87-cd8b-9ea604f6a9e4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/63d6f761-665e-3d87-cd8b-9ea604f6a9e4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetFrequency Method

RFmxLteMXComponentCarrierGetFrequency Method

ComponentCarrierSpacingType

User

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. This method is applicable only if you set the ComponentCarrierSpacingType method to User.

###### Return Value

Int32

##### Remarks

SetFrequency(String, Double)

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/64f7df1a-3fa8-005b-d573-2b370ff18aa0.htm language=enus -->
## TOPIC 00129: rfmxltedotnet/html/64f7df1a-3fa8-005b-d573-2b370ff18aa0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/64f7df1a-3fa8-005b-d573-2b370ff18aa0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/64f7df1a-3fa8-005b-d573-2b370ff18aa0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.Initiate Method

RFmxLteMXListInitiate Method

WaitForMeasurementComplete(String, Double)

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **resultName**
  - Type: SystemString Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1"

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/662cd4e9-6807-0119-128c-a37a901a57d5.htm language=enus -->
## TOPIC 00130: rfmxltedotnet/html/662cd4e9-6807-0119-128c-a37a901a57d5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/662cd4e9-6807-0119-128c-a37a901a57d5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/662cd4e9-6807-0119-128c-a37a901a57d5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetEvmUnit Method

RFmxLteMXModAccConfigurationGetEvmUnit Method

Gets the units of the EVM results.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmUnit(
	string selectorString,
	out RFmxLteMXModAccEvmUnit value
)
```

```text
Public Function GetEvmUnit ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccEvmUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccEvmUnitUpon return, contains the units of the EVM results.

###### Return Value

Int32

##### Remarks

ModAccEvmUnit

Percentage

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6724ce0a-e35f-a7eb-331a-df1dc054026c.htm language=enus -->
## TOPIC 00131: rfmxltedotnet/html/6724ce0a-e35f-a7eb-331a-df1dc054026c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6724ce0a-e35f-a7eb-331a-df1dc054026c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6724ce0a-e35f-a7eb-331a-df1dc054026c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchEvmPerSubcarrierTrace Method

RFmxLteMXModAccResultsFetchEvmPerSubcarrierTrace Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEvmPerSubcarrierTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> meanRmsEvmPerSubcarrier
)
```

```text
Public Function FetchEvmPerSubcarrierTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef meanRmsEvmPerSubcarrier As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsEvmPerSubcarrier**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the mean value of the RMS EVMs calculated on all configured channels over the slots specified by the ModAcc Meas Length method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/67256126-b609-631e-17bf-a180c59f8df3.htm language=enus -->
## TOPIC 00132: rfmxltedotnet/html/67256126-b609-631e-17bf-a180c59f8df3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/67256126-b609-631e-17bf-a180c59f8df3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/67256126-b609-631e-17bf-a180c59f8df3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetFftWindowLength Method

RFmxLteMXModAccConfigurationGetFftWindowLength Method

SetFftWindowType(String, RFmxLteMXModAccFftWindowType)

Type3GPP

3GPP 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftWindowLength(
	string selectorString,
	out double value
)
```

```text
Public Function GetFftWindowLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(String, RFmxLteMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of 3GPP 36.521 specification for more information.

###### Return Value

Int32

##### Remarks

ModAccFftWindowLength

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6b8f416a-745f-3115-7b13-ca7f1d7b1626.htm language=enus -->
## TOPIC 00133: rfmxltedotnet/html/6b8f416a-745f-3115-7b13-ca7f1d7b1626.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6b8f416a-745f-3115-7b13-ca7f1d7b1626.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6b8f416a-745f-3115-7b13-ca7f1d7b1626.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetListStepTimerUnit Method

RFmxLteMXGetListStepTimerUnit Method

SetListStepTimerDuration(String, Double)

SetListStepTimerOffset(String, Double)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetListStepTimerUnit(
	string selectorString,
	out RFmxLteMXListStepTimerUnit value
)
```

```text
Public Function GetListStepTimerUnit ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXListStepTimerUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXListStepTimerUnit Upon return, contains the units in which SetListStepTimerDuration(String, Double) and SetListStepTimerOffset(String, Double) are specified.

###### Return Value

Int32

##### Remarks

ListStepTimerUnit

Slot

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6de95e9b-832a-3479-1e38-81956be25926.htm language=enus -->
## TOPIC 00134: rfmxltedotnet/html/6de95e9b-832a-3479-1e38-81956be25926.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6de95e9b-832a-3479-1e38-81956be25926.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6de95e9b-832a-3479-1e38-81956be25926.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXLimitedConfigurationChange Enumeration

RFmxLteMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by RFmx driver in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXLimitedConfigurationChange
```

```text
Public Enumeration RFmxLteMXLimitedConfigurationChange
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Disabled | 0 | This is the normal mode of the RFmx driver operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
|  | NoChange | 1 | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
|  | Frequency | 2 | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and SetExternalAttenuation(String, Double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
|  | ReferenceLevel | 3 | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the SetReferenceLevel(String, Double) method value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the SetIQPowerEdgeTriggerLevelType(String, RFmxLteMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
|  | FrequencyAndReferenceLevel | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type method to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
|  | SelectedPortsFrequencyAndReferenceLevel | 5 | Signal configuration, other than Selected Ports, Center frequency, Reference level, External attenuation, and RFmxInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type method to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6e3cd618-3c59-80fa-5517-65f00a746e1d.htm language=enus -->
## TOPIC 00135: rfmxltedotnet/html/6e3cd618-3c59-80fa-5517-65f00a746e1d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6e3cd618-3c59-80fa-5517-65f00a746e1d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6e3cd618-3c59-80fa-5517-65f00a746e1d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwResults Class

RFmxLteMXObwResults Class

Provides methods to fetch and read the OBW measurement results.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXObwResults : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXObwResults
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXObwResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Occupied Bandwidth topic for more information about OBW measurements. |
|  | FetchSpectrum | Fetches the spectrum used for OBW measurements. |
|  | GetAbsolutePower | Gets the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetOccupiedBandwidth | Gets the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
|  | GetStartFrequency | Gets the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Stop frequency - Start frequency = Occupied bandwidthUse "subblock(n)" as the selector string to read this result. |
|  | GetStopFrequency | Gets the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequencyUse "subblock(n)" as the selector string to read this result. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6e6b4e05-03ee-e914-8b4d-3b676a646e05.htm language=enus -->
## TOPIC 00136: rfmxltedotnet/html/6e6b4e05-03ee-e914-8b4d-3b676a646e05.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6e6b4e05-03ee-e914-8b4d-3b676a646e05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6e6b4e05-03ee-e914-8b4d-3b676a646e05.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemLowerOffsetMeasurementStatus Enumeration

RFmxLteMXSemLowerOffsetMeasurementStatus Enumeration

Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type method. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXSemLowerOffsetMeasurementStatus
```

```text
Public Enumeration RFmxLteMXSemLowerOffsetMeasurementStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 | Indicates that the measurement has failed. |
|  | Pass | 1 | Indicates that the measurement has passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6efbc649-9c36-79b4-7505-b1d8de060732.htm language=enus -->
## TOPIC 00137: rfmxltedotnet/html/6efbc649-9c36-79b4-7505-b1d8de060732.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6efbc649-9c36-79b4-7505-b1d8de060732.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6efbc649-9c36-79b4-7505-b1d8de060732.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAutoNPuschChannelDetectionEnabled Enumeration

RFmxLteMXAutoNPuschChannelDetectionEnabled Enumeration

SetNPuschToneOffset(String, Int32)

SetNPuschModulationType(String, RFmxLteMXNPuschModulationType)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAutoNPuschChannelDetectionEnabled
```

```text
Public Enumeration RFmxLteMXAutoNPuschChannelDetectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the values that you specify for the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties. |
|  | True | 1 | The measurement uses the values of the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties that are auto-detected. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6f1dfdad-5726-294c-f5ea-670dc96ffbd2.htm language=enus -->
## TOPIC 00138: rfmxltedotnet/html/6f1dfdad-5726-294c-f5ea-670dc96ffbd2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6f1dfdad-5726-294c-f5ea-670dc96ffbd2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6f1dfdad-5726-294c-f5ea-670dc96ffbd2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchEvmPerSlotTrace Method

RFmxLteMXModAccResultsFetchEvmPerSlotTrace Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEvmPerSlotTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> rmsEvmPerSlot
)
```

```text
Public Function FetchEvmPerSlotTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef rmsEvmPerSlot As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **rmsEvmPerSlot**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the EVM measured per slot.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6f634923-007d-3562-2252-4568e58e6085.htm language=enus -->
## TOPIC 00139: rfmxltedotnet/html/6f634923-007d-3562-2252-4568e58e6085.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6f634923-007d-3562-2252-4568e58e6085.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6f634923-007d-3562-2252-4568e58e6085.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetResultFetchTimeout Method

RFmxLteMXSetResultFetchTimeout Method

Sets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6f7860db-b7de-dad0-21b2-67add17d7be2.htm language=enus -->
## TOPIC 00140: rfmxltedotnet/html/6f7860db-b7de-dad0-21b2-67add17d7be2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6f7860db-b7de-dad0-21b2-67add17d7be2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6f7860db-b7de-dad0-21b2-67add17d7be2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.ConfigureFftWindowOffset Method

RFmxLteMXModAccConfigurationConfigureFftWindowOffset Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFftWindowOffset(
	string selectorString,
	double fftWindowOffset
)
```

```text
Public Function ConfigureFftWindowOffset ( 
	selectorString As String,
	fftWindowOffset As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **fftWindowOffset**
  - Type: SystemDoubleSpecifies the position of the FFT window that is used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6fa4ec92-2bfc-a2d2-b229-80f557e64a39.htm language=enus -->
## TOPIC 00141: rfmxltedotnet/html/6fa4ec92-2bfc-a2d2-b229-80f557e64a39.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6fa4ec92-2bfc-a2d2-b229-80f557e64a39.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6fa4ec92-2bfc-a2d2-b229-80f557e64a39.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrierSpacingType Enumeration

RFmxLteMXComponentCarrierSpacingType Enumeration

Specifies the spacing between two adjacent component carriers within a subblock.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXComponentCarrierSpacingType
```

```text
Public Enumeration RFmxLteMXComponentCarrierSpacingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Nominal | 0 | Calculates the frequency spacing between component carriers, as defined in section 5.4.1A in the 3GPP TS 36.521 specification, and sets the SetFrequency(String, Double) method. |
|  | Minimum | 1 | Calculates the frequency spacing between component carriers, as defined in section 5.4.1A of the 3GPP TS 36.521 specification, and sets the CC Freq method. |
|  | User | 2 | The CC frequency that you configure in the CC Freq method is used. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/6fa5e39c-0483-b6e0-6b0b-da2bb4391b5e.htm language=enus -->
## TOPIC 00142: rfmxltedotnet/html/6fa5e39c-0483-b6e0-6b0b-da2bb4391b5e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/6fa5e39c-0483-b6e0-6b0b-da2bb4391b5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/6fa5e39c-0483-b6e0-6b0b-da2bb4391b5e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetNumberOfAnalysisThreads Method

RFmxLteMXTxpConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism inside TXP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Specifies the maximum number of threads used for parallelism inside TXP measurement.

###### Return Value

Int32

##### Remarks

TxpNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7023b782-7c2e-d851-b987-cd965e92b88d.htm language=enus -->
## TOPIC 00143: rfmxltedotnet/html/7023b782-7c2e-d851-b987-cd965e92b88d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7023b782-7c2e-d851-b987-cd965e92b88d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7023b782-7c2e-d851-b987-cd965e92b88d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetTransmitterArchitecture Method

RFmxLteMXGetTransmitterArchitecture Method

Gets the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTransmitterArchitecture(
	string selectorString,
	out RFmxLteMXTransmitterArchitecture value
)
```

```text
Public Function GetTransmitterArchitecture ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXTransmitterArchitecture
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTransmitterArchitectureUpon return, contains the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

###### Return Value

Int32

##### Remarks

TransmitterArchitecture

LOPerComponentCarrier

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/70253329-456e-0136-3ebd-327ce6d19bce.htm language=enus -->
## TOPIC 00144: rfmxltedotnet/html/70253329-456e-0136-3ebd-327ce6d19bce.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/70253329-456e-0136-3ebd-327ce6d19bce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/70253329-456e-0136-3ebd-327ce6d19bce.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.SetRbwFilterType Method

RFmxLteMXObwConfigurationSetRbwFilterType Method

Sets the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxLteMXObwRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxLteMXObwRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwRbwFilterTypeSpecifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

ObwRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/705ac004-3e93-22f6-5994-28642ddcaa3e.htm language=enus -->
## TOPIC 00145: rfmxltedotnet/html/705ac004-3e93-22f6-5994-28642ddcaa3e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/705ac004-3e93-22f6-5994-28642ddcaa3e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/705ac004-3e93-22f6-5994-28642ddcaa3e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetTriggerMinimumQuietTimeDuration Method

RFmxLteMXSetTriggerMinimumQuietTimeDuration Method

Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerMinimumQuietTimeDuration(
	string selectorString,
	double value
)
```

```text
Public Function SetTriggerMinimumQuietTimeDuration ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TriggerMinimumQuietTimeDuration

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/705fa319-ab8b-444c-a786-e374d61e6776.htm language=enus -->
## TOPIC 00146: rfmxltedotnet/html/705fa319-ab8b-444c-a786-e374d61e6776.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/705fa319-ab8b-444c-a786-e374d61e6776.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/705fa319-ab8b-444c-a786-e374d61e6776.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetReferenceLevel Method

RFmxLteMXSetReferenceLevel Method

Sets the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDoubleSpecifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

ReferenceLevel

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/708db61e-6a1e-62ef-3f27-ce3f4b3ab233.htm language=enus -->
## TOPIC 00147: rfmxltedotnet/html/708db61e-6a1e-62ef-3f27-ce3f4b3ab233.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/708db61e-6a1e-62ef-3f27-ce3f4b3ab233.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/708db61e-6a1e-62ef-3f27-ce3f4b3ab233.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX Class

RFmxLteMX Class

Defines a root class which is used to identify and control LTE signal configuration.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMX : ISignalConfiguration, 
	IDisposable
```

```text
Public NotInheritable Class RFmxLteMX
	Implements ISignalConfiguration, IDisposable
```

The RFmxLteMX type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Acp | Gets the RFmxLteMXAcp instance that represents the ACP measurement. |
|  | Chp | Gets the RFmxLteMXChp instance that represents the CHP measurement. |
|  | ComponentCarrier | Gets the RFmxLteMXComponentCarrier instance. |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | ModAcc | Gets the RFmxLteMXModAcc instance that represents the ModAcc measurement. |
|  | Obw | Gets the RFmxLteMXObw instance that represents the OBW measurement. |
|  | Pvt | Gets the RFmxLteMXPvt instance that represents the PVT measurement. |
|  | Sem | Gets the RFmxLteMXSem instance that represents the SEM measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxLteMX. |
|  | SlotPhase | Gets the RFmxLteMXSlotPhase instance that represents the SlotPhase measurement. |
|  | SlotPower | Gets the RFmxLteMXSlotPower instance that represents the SlotPower measurement. |
|  | Txp | Gets the RFmxLteMXTxp instance that represents the TXP measurement. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(String, String) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either IQ or IQorSpectral. When using the Analysis-Only mode in RFmxLTE, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx LTE Commit method. |
|  | AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum waveform that you specify in spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either spectral or IQorSpectral. When using the Analysis-Only mode in RFmxLTE, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx LTE Commit method. |
|  | AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(String, Double) method. Use this method to calculate an approximate setting for the reference level. The RFmxLTE Auto Level method completes the following tasks: Resets the mixer level, mixer level offset, and IF output power offset. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings. Iterates to adjust the reference level based on the input signal peak power. Uses immediate triggering and restores the trigger settings back to user setting after the execution. You can also specify the starting reference level using SetAutoLevelInitialReferenceLevel(String, Double) method. When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxLTE Auto Level method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method; thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildCarrierString | Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch methods and methods. |
|  | BuildClusterString | Creates a cluster string to use as a selector string with the ModAcc cluster configuration or fetch methods and methods. |
|  | BuildListStepString | Creates the list step string. |
|  | BuildListString | Creates the list string. |
|  | BuildOffsetString | Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch methods and methods. |
|  | BuildPdschString | Creates a PDSCH string to use as a selector string with the configuration or fetch methods and methods. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSubblockString | Creates a subblock string to use as a selector string with the subblock configuration or fetch methods and methods. |
|  | BuildSubframeString | Creates a subframe string to use as a selector string with the configuration or fetch methods and methods. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxLTE commits settings to the hardware when you call the Initiate(String, String) method. |
|  | ConfigureAutoDmrsDetectionEnabled | Configures whether the demodulation reference signal (DMRS) parameters are configured by a user or automatically detected by a measurement. |
|  | ConfigureBand | Configures the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureDuplexScheme | Configures the duplexing technique of the signal being measured. |
|  | ConfigureeNodeBCategory | Configures the eNodeB category of the signal being measured. |
|  | ConfigureExternalAttenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
|  | ConfigureFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureFrequencyEarfcn | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
|  | ConfigureLinkDirection | Configures the link direction of the signal being measured. |
|  | ConfigureNumberOfComponentCarriers | Configures the number of component carriers within a subblock. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureNumberOfDutAntennas | Configures the number of physical antennas used for transmission by the DUT in a MIMO setup. |
|  | ConfigureNumberOfSubblocks | Configures the number of subblocks. |
|  | ConfigureReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
|  | ConfigureRF | Configures the RF methods of the signal specified by the selector string. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
|  | ConfigureTransmitAntennaToAnalyze | Configures the current physical antenna of the DUT in the MIMO setup being tested. |
|  | DeleteSignalConfiguration | Deletes an instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAcquisitionBandwidthOptimizationEnabled | Gets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |
|  | GetAllNamedResultNames | Gets the named result names of the signal that you specify in the selectorString parameter. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoDmrsDetectionEnabled | Gets whether you configure the values of the demodulation reference signal (DMRS) parameters, such as SetUplinkGroupHoppingEnabled(String, RFmxLteMXUplinkGroupHoppingEnabled), SetUplinkSequenceHoppingEnabled(String, RFmxLteMXUplinkSequenceHoppingEnabled), SetCellId(String, Int32), SetPuschNDmrs1(String, Int32), SetPuschNDmrs2(String, Int32), and SetPuschDeltaSequenceShift(String, Int32) properties, or if the values of these properties are auto-detected by the measurement. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | GetBand | Gets the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock, as defined in section 5.2 of the 3GPP TS 36.521 specification. |
|  | GetCenterFrequency | For a single carrier, this method specifies the center frequency of the acquired RF signal. |
|  | GetCenterFrequencyForLimits | Gets the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. |
|  | GetDigitalEdgeTriggerEdge | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | GetDigitalEdgeTriggerSource | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | GetDuplexScheme | Gets the duplexing technique of the signal being measured. |
|  | GeteNodeBCategory | Gets the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. |
|  | GetErrorString | Converts the status code returned by an RFmxLTE function into a string. |
|  | GetExternalAttenuation | Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIQPowerEdgeTriggerLevel | Gets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxLteMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx driver in the locked signal configuration state. |
|  | GetLinkDirection | Gets the link direction of the received signal. |
|  | GetListStepTimerDuration | Gets the duration of a given list step in units specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). |
|  | GetListStepTimerOffset | Gets the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent |
|  | GetListStepTimerUnit | Gets the units in which SetListStepTimerDuration(String, Double) and SetListStepTimerOffset(String, Double) are specified. |
|  | GetMiConfiguration | Gets whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the SetDuplexScheme(String, RFmxLteMXDuplexScheme) method to Tdd. |
|  | GetNumberOfDutAntennas | Gets the number of physical antennas available at the DUT for transmission in a MIMO setup. |
|  | GetNumberOfSubblocks | Gets the number of subblocks that are configured in intra-band non-contiguous carrier aggregation. |
|  | GetPuschPower | Obsolete. Gets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | GetReferenceLevel | Gets the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx driver adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | GetResultFetchTimeout | Gets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | GetSpecialSubframeConfiguration | Gets the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. |
|  | GetSubblockFrequency | Gets the offset of the subblock from the center frequency. This value is expressed in Hz. |
|  | GetTransmitAntennaToAnalyze | Gets the physical antenna connected to the analyzer. |
|  | GetTransmitterArchitecture | Gets the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. |
|  | GetTriggerDelay | Gets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre trigger samples. If the delay is positive, the measurement acquires post trigger samples. |
|  | GetTriggerMinimumQuietTimeDuration | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement computes the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the trigger type. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUplinkDownlinkConfiguration | Gets the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. |
|  | GetWarning | Gets the latest warning code and description. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxLTE_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configure an invalid trigger. You have not previously called the Initiate(String, String) method. |
|  | SetAcquisitionBandwidthOptimizationEnabled | Sets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoDmrsDetectionEnabled | Sets whether you configure the values of the demodulation reference signal (DMRS) parameters, such as SetUplinkGroupHoppingEnabled(String, RFmxLteMXUplinkGroupHoppingEnabled), SetUplinkSequenceHoppingEnabled(String, RFmxLteMXUplinkSequenceHoppingEnabled), SetCellId(String, Int32), SetPuschNDmrs1(String, Int32), SetPuschNDmrs2(String, Int32), and SetPuschDeltaSequenceShift(String, Int32) properties, or if the values of these properties are auto-detected by the measurement. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SetBand | Sets the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock, as defined in section 5.2 of the 3GPP TS 36.521 specification. |
|  | SetCenterFrequency | For a single carrier, this method specifies the center frequency of the acquired RF signal. |
|  | SetCenterFrequencyForLimits | Sets the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this method, the measurement internally uses RFmxLteMX.SetCenterFrequency for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. |
|  | SetDigitalEdgeTriggerEdge | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | SetDuplexScheme | Sets the duplexing technique of the signal being measured. |
|  | SeteNodeBCategory | Sets the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. |
|  | SetExternalAttenuation | Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation. |
|  | SetIQPowerEdgeTriggerLevel | Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxLteMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx driver in the locked signal configuration state. |
|  | SetLinkDirection | Sets the link direction of the received signal. |
|  | SetListStepTimerDuration | Sets the duration of a given list step in units specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). |
|  | SetListStepTimerOffset | Sets the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent. |
|  | SetListStepTimerUnit | Sets the units in which SetListStepTimerDuration(String, Double) and SetListStepTimerOffset(String, Double) are specified. |
|  | SetMiConfiguration | Sets whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the SetDuplexScheme(String, RFmxLteMXDuplexScheme) method to Tdd. |
|  | SetNumberOfDutAntennas | Sets the number of physical antennas available at the DUT for transmission in a MIMO setup. |
|  | SetNumberOfSubblocks | Sets the number of subblocks that are configured in intra-band non-contiguous carrier aggregation. |
|  | SetPuschPower | Obsolete. Sets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | SetReferenceLevel | Sets the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx driver adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | SetResultFetchTimeout | Sets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. |
|  | SetSelectedPorts | Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | SetSpecialSubframeConfiguration | Sets the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. |
|  | SetSubblockFrequency | Sets the offset of the subblock from the center frequency. This value is expressed in Hz. |
|  | SetTransmitAntennaToAnalyze | Sets the physical antenna connected to the analyzer. |
|  | SetTransmitterArchitecture | Sets the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. |
|  | SetTriggerDelay | Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre trigger samples. If the delay is positive, the measurement acquires post trigger samples. |
|  | SetTriggerMinimumQuietTimeDuration | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement computes the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the trigger type. |
|  | SetUplinkDownlinkConfiguration | Sets the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/70a54fb5-f332-46b1-0b25-cc80259eb02f.htm language=enus -->
## TOPIC 00148: rfmxltedotnet/html/70a54fb5-f332-46b1-0b25-cc80259eb02f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/70a54fb5-f332-46b1-0b25-cc80259eb02f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/70a54fb5-f332-46b1-0b25-cc80259eb02f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.Obw Property

RFmxLteMXObw Property

RFmxLteMXObw

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXObw Obw { get; }
```

```text
Public ReadOnly Property Obw As RFmxLteMXObw
	Get
```

###### Property Value

RFmxLteMXObw

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/70b7df16-c68c-cf2b-3f96-61f9e6043491.htm language=enus -->
## TOPIC 00149: rfmxltedotnet/html/70b7df16-c68c-cf2b-3f96-61f9e6043491.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/70b7df16-c68c-cf2b-3f96-61f9e6043491.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/70b7df16-c68c-cf2b-3f96-61f9e6043491.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPdschEvm Method

RFmxLteMXModAccResultsFetchPdschEvm Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPdschEvm(
	string selectorString,
	double timeout,
	out double meanRmsEvm,
	out double meanRmsQpskEvm,
	out double meanRms16QamEvm,
	out double meanRms64QamEvm,
	out double meanRms256QamEvm
)
```

```text
Public Function FetchPdschEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRmsEvm As Double,
	<OutAttribute> ByRef meanRmsQpskEvm As Double,
	<OutAttribute> ByRef meanRms16QamEvm As Double,
	<OutAttribute> ByRef meanRms64QamEvm As Double,
	<OutAttribute> ByRef meanRms256QamEvm As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsEvm**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.
- **meanRmsQpskEvm**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.
- **meanRms16QamEvm**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.
- **meanRms64QamEvm**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on all 64QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.
- **meanRms256QamEvm**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on all 256QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/70b914ae-70c9-e5b8-668d-96533f1865c2.htm language=enus -->
## TOPIC 00150: rfmxltedotnet/html/70b914ae-70c9-e5b8-668d-96533f1865c2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/70b914ae-70c9-e5b8-668d-96533f1865c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/70b914ae-70c9-e5b8-668d-96533f1865c2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXConstants.Pfi0 Field

RFmxLteMXConstantsPfi0 Field

The signal is exported to the PFI 0.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXConstants Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/70b9c37f-437b-d988-156a-c3b782d90ec2.htm language=enus -->
## TOPIC 00151: rfmxltedotnet/html/70b9c37f-437b-d988-156a-c3b782d90ec2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/70b9c37f-437b-d988-156a-c3b782d90ec2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/70b9c37f-437b-d988-156a-c3b782d90ec2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetTriggerMinimumQuietTimeMode Method

RFmxLteMXSetTriggerMinimumQuietTimeMode Method

Sets whether the measurement computes the minimum quiet time used for triggering.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerMinimumQuietTimeMode(
	string selectorString,
	RFmxLteMXTriggerMinimumQuietTimeMode value
)
```

```text
Public Function SetTriggerMinimumQuietTimeMode ( 
	selectorString As String,
	value As RFmxLteMXTriggerMinimumQuietTimeMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTriggerMinimumQuietTimeModeSpecifies whether the measurement computes the minimum quiet time used for triggering.

###### Return Value

Int32

##### Remarks

TriggerMinimumQuietTimeMode

Auto

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/70c302d5-be50-4678-2f8e-8e42c497a4f6.htm language=enus -->
## TOPIC 00152: rfmxltedotnet/html/70c302d5-be50-4678-2f8e-8e42c497a4f6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/70c302d5-be50-4678-2f8e-8e42c497a4f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/70c302d5-be50-4678-2f8e-8e42c497a4f6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwAveragingEnabled Enumeration

RFmxLteMXObwAveragingEnabled Enumeration

Specifies whether to enable averaging for the OBW measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXObwAveragingEnabled
```

```text
Public Enumeration RFmxLteMXObwAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The OBW measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the OBW measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/716784ad-80bf-c3dc-1c5f-0f76806353c0.htm language=enus -->
## TOPIC 00153: rfmxltedotnet/html/716784ad-80bf-c3dc-1c5f-0f76806353c0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/716784ad-80bf-c3dc-1c5f-0f76806353c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/716784ad-80bf-c3dc-1c5f-0f76806353c0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration Methods

RFmxLteMXAcpConfiguration Methods

The [RFmxLteMXAcpConfiguration](4b29983c-6540-3897-e4be-9ed2e22b6e51.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the ACP measurement. |
|  | ConfigureConfigurableNumberOfOffsetsEnabled | Configures whether the number of offsets will be computed by the measurement or configured by the user. |
|  | ConfigureMeasurementMethod | Configures the method for performing the ACP measurement. |
|  | ConfigureNoiseCompensationEnabled | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
|  | ConfigureNumberOfEutraOffsets | Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureNumberOfGsmOffsets | Configures the number of GSM adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureNumberOfUtraOffsets | Configures the number of universal terrestrial radio access (UTRA) adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigurePowerUnits | Configures the units for the absolute power. |
|  | ConfigureRbwFilter | Configures the RBW filter. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | ConfigureUtraAndEutraOffsets | Configures the number of universal terrestrial radio access (UTRA) and evolved universal terrestrial radio access (E-UTRA) adjacent channels of the subblock. This method is valid only for uplink single carrier, and contiguous carrier aggregation. In case of uplink non-contiguous multi-carrier and downlink, the number of UTRA/EUTRA offsets are determined from the 3GPP specification. Use "subblock(n)" as the selector string to configure this method. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXAcpAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the ACP measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
|  | GetComponentCarrierIntegrationBandwidth | Gets the integration bandwidth of the component carrier (CC). This value is expressed in Hz. |
|  | GetConfigurableNumberOfOffsetsEnabled | Gets whether the number of offsets is computed by measurement or configured by you. |
|  | GetEutraOffsetDefinition | Gets the evolved universal terrestrial radio access (E-UTRA) offset channel definition. |
|  | GetFarIFOutputPowerOffset | Gets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
|  | GetFftOverlap | Gets the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(String, RFmxLteMXAcpFftOverlapMode) method to UserDefined. |
|  | GetFftOverlapMode | Gets the overlap mode when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIFOutputPowerOffsetAuto | Gets whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
|  | GetMeasurementEnabled | Gets whether to enable the ACP measurement. |
|  | GetMeasurementMethod | Gets the method for performing the ACP measurement. |
|  | GetMeasurementMode | Gets whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNearIFOutputPowerOffset | Gets the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
|  | GetNoiseCalibrationAveragingAuto | Gets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |
|  | GetNoiseCalibrationAveragingCount | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxLteMXAcpNoiseCalibrationAveragingAuto) method to False. |
|  | GetNoiseCalibrationMode | Gets whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCompensationEnabled | Gets whether RFmx driver compensates for the instrument noise while performing the measurement when you set the SetNoiseCalibrationMode(String, RFmxLteMXAcpNoiseCalibrationMode) method to Auto, or when you set the ACP Noise Cal Mode method to Manual and the SetMeasurementMode(String, RFmxLteMXAcpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCompensationType | Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetNumberOfEutraOffsets | Gets the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
|  | GetNumberOfGsmOffsets | Gets the number of GSM adjacent channel offsets to be configured when you set the SetBandwidth(String, Double) to 200.0 k and the ACP Configurable Number of Offset Enabled method to True. |
|  | GetNumberOfUtraOffsets | Gets the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
|  | GetOffsetFrequency | Gets the offset frequency of an offset channel. This value is expressed in Hz. When you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink, the offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel. When you set the Link Direction method to Downlink, the offset frequency is computed from the center of the closest component carrier to the center of the nearest RBW filter of the offset channel. |
|  | GetOffsetIntegrationBandwidth | Gets the integration bandwidth of an offset carrier. This value is expressed in Hz. |
|  | GetPowerUnits | Gets the units for the absolute power. |
|  | GetRbwFilterAutoBandwidth | Gets whether the measurement computes the RBW. |
|  | GetRbwFilterBandwidth | Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | GetRbwFilterType | Gets the shape of the RBW filter. |
|  | GetSequentialFftSize | Gets the FFT size, when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. |
|  | GetSubblockIntegrationBandwidth | Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXAcpAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the ACP measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
|  | SetConfigurableNumberOfOffsetsEnabled | Sets whether the number of offsets is computed by measurement or configured by you. |
|  | SetEutraOffsetDefinition | Sets the evolved universal terrestrial radio access (E-UTRA) offset channel definition. |
|  | SetFarIFOutputPowerOffset | Sets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
|  | SetFftOverlap | Sets the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(String, RFmxLteMXAcpFftOverlapMode) method to UserDefined. |
|  | SetFftOverlapMode | Sets the overlap mode when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |
|  | SetIFOutputPowerOffsetAuto | Sets whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
|  | SetMeasurementEnabled | Sets whether to enable the ACP measurement. |
|  | SetMeasurementMethod | Sets the method for performing the ACP measurement. |
|  | SetMeasurementMode | Sets whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNearIFOutputPowerOffset | Sets the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
|  | SetNoiseCalibrationAveragingAuto | Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |
|  | SetNoiseCalibrationAveragingCount | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxLteMXAcpNoiseCalibrationAveragingAuto) method to False. |
|  | SetNoiseCalibrationMode | Sets whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCompensationEnabled | Sets whether RFmx driver compensates for the instrument noise while performing the measurement when you set the SetNoiseCalibrationMode(String, RFmxLteMXAcpNoiseCalibrationMode) method to Auto, or when you set the ACP Noise Cal Mode method to Manual and the SetMeasurementMode(String, RFmxLteMXAcpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCompensationType | Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetNumberOfEutraOffsets | Sets the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
|  | SetNumberOfGsmOffsets | Sets the number of GSM adjacent channel offsets to be configured when you set the SetBandwidth(String, Double) to 200.0 k and the ACP Configurable Number of Offset Enabled method to True. |
|  | SetNumberOfUtraOffsets | Sets the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
|  | SetPowerUnits | Sets the units for the absolute power. |
|  | SetRbwFilterAutoBandwidth | Sets whether the measurement computes the RBW. |
|  | SetRbwFilterBandwidth | Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | SetRbwFilterType | Sets the shape of the RBW filter. |
|  | SetSequentialFftSize | Sets the FFT size, when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | ValidateNoiseCalibrationData | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorString parameter. |

Top

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/71a0a3e7-d9e5-71e7-eb14-4e501d6a27e0.htm language=enus -->
## TOPIC 00154: rfmxltedotnet/html/71a0a3e7-d9e5-71e7-eb14-4e501d6a27e0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/71a0a3e7-d9e5-71e7-eb14-4e501d6a27e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/71a0a3e7-d9e5-71e7-eb14-4e501d6a27e0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.GetNumberOfAnalysisThreads Method

RFmxLteMXPvtConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

PvtNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/71b2c2b5-5b69-1bba-7676-5ab701b87826.htm language=enus -->
## TOPIC 00155: rfmxltedotnet/html/71b2c2b5-5b69-1bba-7676-5ab701b87826.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/71b2c2b5-5b69-1bba-7676-5ab701b87826.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/71b2c2b5-5b69-1bba-7676-5ab701b87826.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpMeasurementMode Enumeration

RFmxLteMXChpMeasurementMode Enumeration

Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXChpMeasurementMode
```

```text
Public Enumeration RFmxLteMXChpMeasurementMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Measure | 0 | CHP measurement is performed on the acquired signal. |
|  | CalibrateNoiseFloor | 1 | Manual noise calibration of the signal analyzer is performed for the CHP measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/71b38a3b-8bf4-a19d-8042-74751a4083cd.htm language=enus -->
## TOPIC 00156: rfmxltedotnet/html/71b38a3b-8bf4-a19d-8042-74751a4083cd.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/71b38a3b-8bf4-a19d-8042-74751a4083cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/71b38a3b-8bf4-a19d-8042-74751a4083cd.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchSubblockIQImpairments Method

RFmxLteMXModAccResultsFetchSubblockIQImpairments Method

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture)

LOPerSubblock

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSubblockIQImpairments(
	string selectorString,
	double timeout,
	out double subblockMeanIQOriginOffset,
	out double subblockMeanIQGainImbalance,
	out double subblockMeanIQQuadratureError
)
```

```text
Public Function FetchSubblockIQImpairments ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef subblockMeanIQOriginOffset As Double,
	<OutAttribute> ByRef subblockMeanIQGainImbalance As Double,
	<OutAttribute> ByRef subblockMeanIQQuadratureError As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **subblockMeanIQOriginOffset**
  - Type: SystemDouble Upon return, contains the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method in a subblock. This value is expressed in dBc.
- **subblockMeanIQGainImbalance**
  - Type: SystemDouble Upon return, contains the estimated I/Q gain imbalance averaged over the slots specified by the ModAcc Meas Length method. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock.
- **subblockMeanIQQuadratureError**
  - Type: SystemDouble Upon return, contains the estimated quadrature error averaged over the slots specified by the ModAcc Meas Length method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/723db5f9-f89f-8837-c87d-037ecb4f783c.htm language=enus -->
## TOPIC 00157: rfmxltedotnet/html/723db5f9-f89f-8837-c87d-037ecb4f783c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/723db5f9-f89f-8837-c87d-037ecb4f783c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/723db5f9-f89f-8837-c87d-037ecb4f783c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPdsch1024QamConstellation Method

RFmxLteMXModAccResultsFetchPdsch1024QamConstellation Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPdsch1024QamConstellation(
	string selectorString,
	double timeout,
	ref ComplexSingle[] qam1024Constellation
)
```

```text
Public Function FetchPdsch1024QamConstellation ( 
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

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7244eff5-f99d-8c1b-a8cf-b6d3e8008f7a.htm language=enus -->
## TOPIC 00158: rfmxltedotnet/html/7244eff5-f99d-8c1b-a8cf-b6d3e8008f7a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7244eff5-f99d-8c1b-a8cf-b6d3e8008f7a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7244eff5-f99d-8c1b-a8cf-b6d3e8008f7a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetRbwFilterType Method

RFmxLteMXAcpConfigurationGetRbwFilterType Method

Gets the shape of the RBW filter.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterType(
	string selectorString,
	out RFmxLteMXAcpRbwFilterType value
)
```

```text
Public Function GetRbwFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAcpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpRbwFilterTypeUpon return, contains the shape of the RBW filter.

###### Return Value

Int32

##### Remarks

AcpRbwFilterType

FftBased

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7249a726-9269-2836-c16e-e942e7d79e3f.htm language=enus -->
## TOPIC 00159: rfmxltedotnet/html/7249a726-9269-2836-c16e-e942e7d79e3f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7249a726-9269-2836-c16e-e942e7d79e3f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7249a726-9269-2836-c16e-e942e7d79e3f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpResults.FetchRelativePowersTrace Method

RFmxLteMXAcpResultsFetchRelativePowersTrace Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRelativePowersTrace(
	string selectorString,
	double timeout,
	int traceIndex,
	ref Spectrum<float> relativePowersTrace
)
```

```text
Public Function FetchRelativePowersTrace ( 
	selectorString As String,
	timeout As Double,
	traceIndex As Integer,
	ByRef relativePowersTrace As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **traceIndex**
  - Type: SystemInt32 Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets).
- **relativePowersTrace**
  - Type: NationalInstrumentsSpectrumSingle Returns the trace of relative powers measured relative to total aggregated power in the channel specified by the traceIndex parameter. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7272438e-53ae-1d69-2aaa-622d16f54ee2.htm language=enus -->
## TOPIC 00160: rfmxltedotnet/html/7272438e-53ae-1d69-2aaa-622d16f54ee2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7272438e-53ae-1d69-2aaa-622d16f54ee2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7272438e-53ae-1d69-2aaa-622d16f54ee2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetNPuschMeanDataPower Method

RFmxLteMXModAccResultsGetNPuschMeanDataPower Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNPuschMeanDataPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetNPuschMeanDataPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

ModAccResultsNPuschMeanDataPower

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/72725cc6-0b99-c88f-3e3f-e129dca2244d.htm language=enus -->
## TOPIC 00161: rfmxltedotnet/html/72725cc6-0b99-c88f-3e3f-e129dca2244d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/72725cc6-0b99-c88f-3e3f-e129dca2244d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/72725cc6-0b99-c88f-3e3f-e129dca2244d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetSpectralFlatnessRange2MaximumToRange1Minimum Method

RFmxLteMXModAccResultsGetSpectralFlatnessRange2MaximumToRange1Minimum Method

Measurement Offset

Range1

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectralFlatnessRange2MaximumToRange1Minimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpectralFlatnessRange2MaximumToRange1Minimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from frequency Measurement Offset parameter to frequency Range1. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsSpectralFlatnessRange2MaximumToRange1Minimum

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/72829ba6-4aa4-59cb-1efd-cb2eeeeaeba9.htm language=enus -->
## TOPIC 00162: rfmxltedotnet/html/72829ba6-4aa4-59cb-1efd-cb2eeeeaeba9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/72829ba6-4aa4-59cb-1efd-cb2eeeeaeba9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/72829ba6-4aa4-59cb-1efd-cb2eeeeaeba9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetRbwFilterAutoBandwidth Method

RFmxLteMXAcpConfigurationSetRbwFilterAutoBandwidth Method

Sets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAutoBandwidth(
	string selectorString,
	RFmxLteMXAcpRbwAutoBandwidth value
)
```

```text
Public Function SetRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxLteMXAcpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpRbwAutoBandwidthSpecifies whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

AcpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7322f202-6bb1-f630-70aa-0db4f36073d7.htm language=enus -->
## TOPIC 00163: rfmxltedotnet/html/7322f202-6bb1-f630-70aa-0db4f36073d7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7322f202-6bb1-f630-70aa-0db4f36073d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7322f202-6bb1-f630-70aa-0db4f36073d7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetNumberOfAnalysisThreads Method

RFmxLteMXAcpConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

AcpNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/733ba155-5681-875d-ee85-f67e3b3870dd.htm language=enus -->
## TOPIC 00164: rfmxltedotnet/html/733ba155-5681-875d-ee85-f67e3b3870dd.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/733ba155-5681-875d-ee85-f67e3b3870dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/733ba155-5681-875d-ee85-f67e3b3870dd.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPuschDeltaSequenceShift Method

RFmxLteMXComponentCarrierGetPuschDeltaSequenceShift Method

3GPP TS 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschDeltaSequenceShift(
	string selectorString,
	out int value
)
```

```text
Public Function GetPuschDeltaSequenceShift ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift.

###### Return Value

Int32

##### Remarks

PuschDeltaSequenceShift

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/73c3d9fb-789d-df2a-8b61-b6fe56cb7f49.htm language=enus -->
## TOPIC 00165: rfmxltedotnet/html/73c3d9fb-789d-df2a-8b61-b6fe56cb7f49.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/73c3d9fb-789d-df2a-8b61-b6fe56cb7f49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/73c3d9fb-789d-df2a-8b61-b6fe56cb7f49.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetAveragingEnabled Method

RFmxLteMXTxpConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for TXP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxLteMXTxpAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxLteMXTxpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTxpAveragingEnabledSpecifies whether to enable averaging for TXP measurement.

###### Return Value

Int32

##### Remarks

TxpAveragingEnabled

False

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/748a72ea-221c-339b-4871-44163ea01823.htm language=enus -->
## TOPIC 00166: rfmxltedotnet/html/748a72ea-221c-339b-4871-44163ea01823.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/748a72ea-221c-339b-4871-44163ea01823.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/748a72ea-221c-339b-4871-44163ea01823.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.SetAllTracesEnabled Method

RFmxLteMXTxpConfigurationSetAllTracesEnabled Method

Enables the traces to be stored and retrieved after the TXP measurement is performed.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanEnables the traces to be stored and retrieved after the TXP measurement is performed.

###### Return Value

Int32

##### Remarks

TxpAllTracesEnabled

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/74b28213-b5be-65e1-b82a-2e1932c6326c.htm language=enus -->
## TOPIC 00167: rfmxltedotnet/html/74b28213-b5be-65e1-b82a-2e1932c6326c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/74b28213-b5be-65e1-b82a-2e1932c6326c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/74b28213-b5be-65e1-b82a-2e1932c6326c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetUpperOffsetMargin Method

RFmxLteMXSemResultsGetUpperOffsetMargin Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the margin from the absolute limit mask for the upper (positive) offset. The Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMargin

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/752c1df5-4ac6-ed22-17d8-68b0ea1d137e.htm language=enus -->
## TOPIC 00168: rfmxltedotnet/html/752c1df5-4ac6-ed22-17d8-68b0ea1d137e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/752c1df5-4ac6-ed22-17d8-68b0ea1d137e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/752c1df5-4ac6-ed22-17d8-68b0ea1d137e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetInBandEmissionMaskType Method

RFmxLteMXModAccConfigurationSetInBandEmissionMaskType Method

Sets the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetInBandEmissionMaskType(
	string selectorString,
	RFmxLteMXModAccInBandEmissionMaskType value
)
```

```text
Public Function SetInBandEmissionMaskType ( 
	selectorString As String,
	value As RFmxLteMXModAccInBandEmissionMaskType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccInBandEmissionMaskTypeSpecifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results.

###### Return Value

Int32

##### Remarks

ModAccInBandEmissionMaskType

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7532bf6c-7b3d-ef44-0f78-f5e5ed9f3f5b.htm language=enus -->
## TOPIC 00169: rfmxltedotnet/html/7532bf6c-7b3d-ef44-0f78-f5e5ed9f3f5b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7532bf6c-7b3d-ef44-0f78-f5e5ed9f3f5b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7532bf6c-7b3d-ef44-0f78-f5e5ed9f3f5b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.IsDisposed Property

RFmxLteMXIsDisposed Property

Gets a value that indicates whether the signal has been disposed.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/75b928cf-cc13-5741-2b5c-574e3bff5bf4.htm language=enus -->
## TOPIC 00170: rfmxltedotnet/html/75b928cf-cc13-5741-2b5c-574e3bff5bf4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/75b928cf-cc13-5741-2b5c-574e3bff5bf4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/75b928cf-cc13-5741-2b5c-574e3bff5bf4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.ConfigureMeasurementMethod Method

RFmxLteMXPvtConfigurationConfigureMeasurementMethod Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementMethod(
	string selectorString,
	RFmxLteMXPvtMeasurementMethod measurementMethod
)
```

```text
Public Function ConfigureMeasurementMethod ( 
	selectorString As String,
	measurementMethod As RFmxLteMXPvtMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementMethod**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPvtMeasurementMethodSpecifies the method for performing the PVT measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/75c71552-2455-13d9-05f2-718733e990f7.htm language=enus -->
## TOPIC 00171: rfmxltedotnet/html/75c71552-2455-13d9-05f2-718733e990f7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/75c71552-2455-13d9-05f2-718733e990f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/75c71552-2455-13d9-05f2-718733e990f7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetMeanRmsPdcchEvm Method

RFmxLteMXModAccResultsGetMeanRmsPdcchEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanRmsPdcchEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanRmsPdcchEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on PDCCH channel over the slots specified by the SetMeasurementLength(String, Int32) method.

###### Return Value

Int32

##### Remarks

ModAccResultsMeanRmsPdcchEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/75c92f49-36ef-4372-31d6-f64639c64b02.htm language=enus -->
## TOPIC 00172: rfmxltedotnet/html/75c92f49-36ef-4372-31d6-f64639c64b02.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/75c92f49-36ef-4372-31d6-f64639c64b02.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/75c92f49-36ef-4372-31d6-f64639c64b02.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.ConfigureNumberOfComponentCarriers Method

RFmxLteMXConfigureNumberOfComponentCarriers Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfComponentCarriers(
	string selectorString,
	int numberOfComponentCarriers
)
```

```text
Public Function ConfigureNumberOfComponentCarriers ( 
	selectorString As String,
	numberOfComponentCarriers As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **numberOfComponentCarriers**
  - Type: SystemInt32Specifies the number of component carriers configured within a subblock.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/75e4e15e-3eea-5b75-5fe6-2eaeb849f456.htm language=enus -->
## TOPIC 00173: rfmxltedotnet/html/75e4e15e-3eea-5b75-5fe6-2eaeb849f456.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/75e4e15e-3eea-5b75-5fe6-2eaeb849f456.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/75e4e15e-3eea-5b75-5fe6-2eaeb849f456.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPuschModulationType Enumeration

RFmxLteMXPuschModulationType Enumeration

Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXPuschModulationType
```

```text
Public Enumeration RFmxLteMXPuschModulationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ModulationTypeQpsk | 0 | Specifies a QPSK modulation scheme. |
|  | ModulationType16Qam | 1 | Specifies a 16-QAM modulation scheme. |
|  | ModulationType64Qam | 2 | Specifies a 64-QAM modulation scheme. |
|  | ModulationType256Qam | 3 | Specifies a 256-QAM modulation scheme. |
|  | ModulationType1024Qam | 4 | Specifies a 1024-QAM modulation scheme. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/763ced2f-c360-4562-0688-e1cf5bcc0fb5.htm language=enus -->
## TOPIC 00174: rfmxltedotnet/html/763ced2f-c360-4562-0688-e1cf5bcc0fb5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/763ced2f-c360-4562-0688-e1cf5bcc0fb5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/763ced2f-c360-4562-0688-e1cf5bcc0fb5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.ConfigureNPuschTones Method

RFmxLteMXComponentCarrierConfigureNPuschTones Method

toneOffset

numberOfTones

modulationType

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNPuschTones(
	string selectorString,
	int toneOffset,
	int numberOfTones,
	RFmxLteMXNPuschModulationType modulationType
)
```

```text
Public Function ConfigureNPuschTones ( 
	selectorString As String,
	toneOffset As Integer,
	numberOfTones As Integer,
	modulationType As RFmxLteMXNPuschModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **toneOffset**
  - Type: SystemInt32Specifies the location of the starting subcarrier (tone) within the 200 kHz bandwidth that is allocated to the NPUSCH channel.
- **numberOfTones**
  - Type: SystemInt32 Specifies the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the NPUSCH channel.
- **modulationType**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXNPuschModulationType Specifies the modulation type that is used by the NPUSCH channel. This parameter is valid when numberOfTones is equal to 1 and SetNPuschFormat(String, Int32) is equal to 1. The modulation type for other configurations is defined in Table 10.1.3.2-1 of the 3GPP TS 36.211 specification.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/76cda149-0ce7-5935-7658-519aaf37f229.htm language=enus -->
## TOPIC 00175: rfmxltedotnet/html/76cda149-0ce7-5935-7658-519aaf37f229.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/76cda149-0ce7-5935-7658-519aaf37f229.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/76cda149-0ce7-5935-7658-519aaf37f229.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcquisitionBandwidthOptimizationEnabled Enumeration

RFmxLteMXAcquisitionBandwidthOptimizationEnabled Enumeration

Specifies whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAcquisitionBandwidthOptimizationEnabled
```

```text
Public Enumeration RFmxLteMXAcquisitionBandwidthOptimizationEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The RFmx driver does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the Center Frequency that you configure. |
|  | True | 1 | The RFmx driver positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this method disabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/76e98b39-75bb-82a8-1dad-59393735fbfa.htm language=enus -->
## TOPIC 00176: rfmxltedotnet/html/76e98b39-75bb-82a8-1dad-59393735fbfa.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/76e98b39-75bb-82a8-1dad-59393735fbfa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/76e98b39-75bb-82a8-1dad-59393735fbfa.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPuschNDmrs1 Method

RFmxLteMXComponentCarrierSetPuschNDmrs1 Method

3GPP TS 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschNDmrs1(
	string selectorString,
	int value
)
```

```text
Public Function SetPuschNDmrs1 ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification.

###### Return Value

Int32

##### Remarks

PuschNDmrs1

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/76f95832-70bd-7c70-c8b0-2303a33428c7.htm language=enus -->
## TOPIC 00177: rfmxltedotnet/html/76f95832-70bd-7c70-c8b0-2303a33428c7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/76f95832-70bd-7c70-c8b0-2303a33428c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/76f95832-70bd-7c70-c8b0-2303a33428c7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.BuildOffsetString Method

RFmxLteMXBuildOffsetString Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildResultString(String) method to build the selector string.
- **offsetNumber**
  - Type: SystemInt32 Specifies the offset number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/77ae9dc1-4363-45e5-28f8-84fb33c7ac38.htm language=enus -->
## TOPIC 00178: rfmxltedotnet/html/77ae9dc1-4363-45e5-28f8-84fb33c7ac38.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/77ae9dc1-4363-45e5-28f8-84fb33c7ac38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/77ae9dc1-4363-45e5-28f8-84fb33c7ac38.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetAutoLevelInitialReferenceLevel Method

RFmxLteMXSetAutoLevelInitialReferenceLevel Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AutoLevelInitialReferenceLevel

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/780dbeff-8336-7b24-c4c4-220c490d40aa.htm language=enus -->
## TOPIC 00179: rfmxltedotnet/html/780dbeff-8336-7b24-c4c4-220c490d40aa.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/780dbeff-8336-7b24-c4c4-220c490d40aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/780dbeff-8336-7b24-c4c4-220c490d40aa.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.SetAveragingEnabled Method

RFmxLteMXPvtConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxLteMXPvtAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxLteMXPvtAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPvtAveragingEnabledSpecifies whether to enable averaging for the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtAveragingEnabled

False

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/785e80c2-93ca-3c48-d0d8-86b5d5d56660.htm language=enus -->
## TOPIC 00180: rfmxltedotnet/html/785e80c2-93ca-3c48-d0d8-86b5d5d56660.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/785e80c2-93ca-3c48-d0d8-86b5d5d56660.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/785e80c2-93ca-3c48-d0d8-86b5d5d56660.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetSssPower Method

RFmxLteMXComponentCarrierSetSssPower Method

Sets the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSssPower(
	string selectorString,
	double value
)
```

```text
Public Function SetSssPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SssPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/78c16c60-314c-eff4-b2b2-ddb778e44163.htm language=enus -->
## TOPIC 00181: rfmxltedotnet/html/78c16c60-314c-eff4-b2b2-ddb778e44163.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/78c16c60-314c-eff4-b2b2-ddb778e44163.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/78c16c60-314c-eff4-b2b2-ddb778e44163.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPuschNDmrs1 Method

RFmxLteMXComponentCarrierGetPuschNDmrs1 Method

3GPP TS 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschNDmrs1(
	string selectorString,
	out int value
)
```

```text
Public Function GetPuschNDmrs1 ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification.

###### Return Value

Int32

##### Remarks

PuschNDmrs1

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/78f6e596-aa0e-70fe-4ae4-c62a1368346f.htm language=enus -->
## TOPIC 00182: rfmxltedotnet/html/78f6e596-aa0e-70fe-4ae4-c62a1368346f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/78f6e596-aa0e-70fe-4ae4-c62a1368346f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/78f6e596-aa0e-70fe-4ae4-c62a1368346f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetSubblockMeanQuadratureError Method

RFmxLteMXModAccResultsGetSubblockMeanQuadratureError Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSubblockMeanQuadratureError(
	string selectorString,
	out double value
)
```

```text
Public Function GetSubblockMeanQuadratureError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock.

###### Return Value

Int32

##### Remarks

ModAccResultsSubblockMeanQuadratureError

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/793c2c5e-a222-a5b8-9c20-567401f75003.htm language=enus -->
## TOPIC 00183: rfmxltedotnet/html/793c2c5e-a222-a5b8-9c20-567401f75003.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/793c2c5e-a222-a5b8-9c20-567401f75003.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/793c2c5e-a222-a5b8-9c20-567401f75003.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetPreFftErrorEstimationInterval Method

RFmxLteMXModAccConfigurationSetPreFftErrorEstimationInterval Method

Sets the interval used for Pre-FFT Error Estimation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPreFftErrorEstimationInterval(
	string selectorString,
	RFmxLteMXModAccPreFftErrorEstimationInterval value
)
```

```text
Public Function SetPreFftErrorEstimationInterval ( 
	selectorString As String,
	value As RFmxLteMXModAccPreFftErrorEstimationInterval
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccPreFftErrorEstimationIntervalSpecifies the interval used for Pre-FFT Error Estimation.

###### Return Value

Int32

##### Remarks

ModAccPreFftErrorEstimationInterval

MeasurementLength

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7976528d-a04b-5e63-a199-06193e392f35.htm language=enus -->
## TOPIC 00184: rfmxltedotnet/html/7976528d-a04b-5e63-a199-06193e392f35.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7976528d-a04b-5e63-a199-06193e392f35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7976528d-a04b-5e63-a199-06193e392f35.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetTransmitterArchitecture Method

RFmxLteMXSetTransmitterArchitecture Method

Sets the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTransmitterArchitecture(
	string selectorString,
	RFmxLteMXTransmitterArchitecture value
)
```

```text
Public Function SetTransmitterArchitecture ( 
	selectorString As String,
	value As RFmxLteMXTransmitterArchitecture
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTransmitterArchitectureSpecifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

###### Return Value

Int32

##### Remarks

TransmitterArchitecture

LOPerComponentCarrier

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/797bce41-0ec1-ec46-e894-95165fa661a7.htm language=enus -->
## TOPIC 00185: rfmxltedotnet/html/797bce41-0ec1-ec46-e894-95165fa661a7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/797bce41-0ec1-ec46-e894-95165fa661a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/797bce41-0ec1-ec46-e894-95165fa661a7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration Class

RFmxLteMXChpConfiguration Class

Provides methods to configure the CHP measurement.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXChpConfiguration : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXChpConfiguration
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXChpConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the CHP measurement. |
|  | ConfigureIntegrationBandwidthType | Configures the type of integration bandwidth (IBW), which selects one of the frequency ranges over which the CHP is measured. Refer to the LTE Channel Power (CHP) topic for more information. |
|  | ConfigureRbwFilter | Configures the RBW filter. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXChpAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the CHP measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |
|  | GetComponentCarrierIntegrationBandwidth | Gets the integration bandwidth of a component carrier (CC). This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIntegrationBandwidthType | Gets the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
|  | GetMeasurementEnabled | Gets whether to enable the channel power measurement. |
|  | GetMeasurementMode | Gets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCalibrationAveragingAuto | Gets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |
|  | GetNoiseCalibrationAveragingCount | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxLteMXChpNoiseCalibrationAveragingAuto) method to False. |
|  | GetNoiseCalibrationMode | Gets whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCompensationEnabled | Gets whether the RFmx driver compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(String, RFmxLteMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and the SetMeasurementMode(String, RFmxLteMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCompensationType | Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetRbwFilterAutoBandwidth | Gets whether the CHP measurement computes the RBW. |
|  | GetRbwFilterBandwidth | Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | GetRbwFilterType | Gets the shape of the digital RBW filter. |
|  | GetSubblockIntegrationBandwidth | Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXChpAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the CHP measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |
|  | SetIntegrationBandwidthType | Sets the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
|  | SetMeasurementEnabled | Sets whether to enable the channel power measurement. |
|  | SetMeasurementMode | Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCalibrationAveragingAuto | Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |
|  | SetNoiseCalibrationAveragingCount | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxLteMXChpNoiseCalibrationAveragingAuto) method to False. |
|  | SetNoiseCalibrationMode | Sets whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCompensationEnabled | Sets whether the RFmx driver compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(String, RFmxLteMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and the SetMeasurementMode(String, RFmxLteMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCompensationType | Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetRbwFilterAutoBandwidth | Sets whether the CHP measurement computes the RBW. |
|  | SetRbwFilterBandwidth | Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | SetRbwFilterType | Sets the shape of the digital RBW filter. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | ValidateNoiseCalibrationData | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorString parameter. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/79db997e-6d55-96ba-4f81-1337e6dc854b.htm language=enus -->
## TOPIC 00186: rfmxltedotnet/html/79db997e-6d55-96ba-4f81-1337e6dc854b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/79db997e-6d55-96ba-4f81-1337e6dc854b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/79db997e-6d55-96ba-4f81-1337e6dc854b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetLowerOffsetPeakFrequency Method

RFmxLteMXSemResultsGetLowerOffsetPeakFrequency Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetPeakFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetPeakFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the frequency at which the peak power occurs in the lower (negative) offset segment. For the type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetPeakFrequency

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/79f3eb45-4f70-9f7a-9b13-01689f7e1e6e.htm language=enus -->
## TOPIC 00187: rfmxltedotnet/html/79f3eb45-4f70-9f7a-9b13-01689f7e1e6e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/79f3eb45-4f70-9f7a-9b13-01689f7e1e6e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/79f3eb45-4f70-9f7a-9b13-01689f7e1e6e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetNPuschMeanRmsDmrsEvm Method

RFmxLteMXModAccResultsGetNPuschMeanRmsDmrsEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNPuschMeanRmsDmrsEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetNPuschMeanRmsDmrsEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(String, Int32) method.

###### Return Value

Int32

##### Remarks

ModAccResultsNPuschMeanRmsDmrsEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7a13cc26-4413-d329-c8f0-fa07e564a5be.htm language=enus -->
## TOPIC 00188: rfmxltedotnet/html/7a13cc26-4413-d329-c8f0-fa07e564a5be.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7a13cc26-4413-d329-c8f0-fa07e564a5be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7a13cc26-4413-d329-c8f0-fa07e564a5be.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPhaseConfiguration.GetSynchronizationMode Method

RFmxLteMXSlotPhaseConfigurationGetSynchronizationMode Method

Gets whether the measurement is performed from the frame or the slot boundary.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSynchronizationMode(
	string selectorString,
	out RFmxLteMXSlotPhaseSynchronizationMode value
)
```

```text
Public Function GetSynchronizationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSlotPhaseSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSlotPhaseSynchronizationModeUpon return, contains whether the measurement is performed from the frame or the slot boundary.

###### Return Value

Int32

##### Remarks

SlotPhaseSynchronizationMode

Frame

##### See Also

###### Reference

RFmxLteMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7a1df758-96d0-6e6e-dda7-a4d74eb973d4.htm language=enus -->
## TOPIC 00189: rfmxltedotnet/html/7a1df758-96d0-6e6e-dda7-a4d74eb973d4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7a1df758-96d0-6e6e-dda7-a4d74eb973d4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7a1df758-96d0-6e6e-dda7-a4d74eb973d4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpResults.FetchOffsetMeasurement Method

RFmxLteMXAcpResultsFetchOffsetMeasurement Method

LTE Uplink Adjacent Channel Power

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchOffsetMeasurement(
	string selectorString,
	double timeout,
	out double lowerRelativePower,
	out double upperRelativePower,
	out double lowerAbsolutePower,
	out double upperAbsolutePower
)
```

```text
Public Function FetchOffsetMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef lowerRelativePower As Double,
	<OutAttribute> ByRef upperRelativePower As Double,
	<OutAttribute> ByRef lowerAbsolutePower As Double,
	<OutAttribute> ByRef upperAbsolutePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **lowerRelativePower**
  - Type: SystemDouble Upon return, contains the power in lower (negative) offset channel relative to value returned by the GetTotalAggregatedPower(String, Double) method. For the intra-band non-contiguous type of carrier aggregation, if this offset is not applicable, a NaN is returned. For more information about the applicability of the offset channel, refer to the 3GPP TS 36.521 specification.
- **upperRelativePower**
  - Type: SystemDouble Upon return, contains the power in upper (positive) offset channel relative to the value returned by the ACP Results Total Aggregated Pwr method. For the intra-band non-contiguous type of carrier aggregation, if this offset is not applicable, a NaN is returned. For more information about the applicability of the offset channel, refer to the 3GPP TS 36.521 specification.
- **lowerAbsolutePower**
  - Type: SystemDouble Upon return, contains the lower (negative) offset channel power. For the intra-band non-contiguous type of carrier aggregation, if this offset is not applicable, a NaN is returned. For more information about the applicability of an offset channel, refer to the 3GPP TS 36.521 specification.
- **upperAbsolutePower**
  - Type: SystemDouble Upon return, contains the upper (positive) offset channel power. For the intra-band non-contiguous type of carrier aggregation, if this offset is not applicable, a NaN is returned. For more information about the applicability of offset channel, refer 3GPP TS 36.521 specification.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7a47e3bf-2fa2-5a1a-c301-5e727df41ddf.htm language=enus -->
## TOPIC 00190: rfmxltedotnet/html/7a47e3bf-2fa2-5a1a-c301-5e727df41ddf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7a47e3bf-2fa2-5a1a-c301-5e727df41ddf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7a47e3bf-2fa2-5a1a-c301-5e727df41ddf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpAveragingType Enumeration

RFmxLteMXChpAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXChpAveragingType
```

```text
Public Enumeration RFmxLteMXChpAveragingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
|  | Log | 1 | The power spectrum is averaged in a logarithmic scale. |
|  | Scalar | 2 | The square root of the power spectrum is averaged. |
|  | Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Minimum | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7a55b6bf-ae83-cbab-94c5-a352806c514b.htm language=enus -->
## TOPIC 00191: rfmxltedotnet/html/7a55b6bf-ae83-cbab-94c5-a352806c514b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7a55b6bf-ae83-cbab-94c5-a352806c514b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7a55b6bf-ae83-cbab-94c5-a352806c514b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetMulticarrierFilterEnabled Method

RFmxLteMXModAccConfigurationGetMulticarrierFilterEnabled Method

Gets whether to use a filter to suppress the interference from out of band emissions into the carriers being measured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMulticarrierFilterEnabled(
	string selectorString,
	out RFmxLteMXModAccMulticarrierFilterEnabled value
)
```

```text
Public Function GetMulticarrierFilterEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccMulticarrierFilterEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccMulticarrierFilterEnabledUpon return, contains whether to use a filter to suppress the interference from out of band emissions into the carriers being measured.

###### Return Value

Int32

##### Remarks

ModAccMulticarrierFilterEnabled

False

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7ae7df23-ceda-207b-8f6a-ba186d49d187.htm language=enus -->
## TOPIC 00192: rfmxltedotnet/html/7ae7df23-ceda-207b-8f6a-ba186d49d187.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7ae7df23-ceda-207b-8f6a-ba186d49d187.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7ae7df23-ceda-207b-8f6a-ba186d49d187.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.GetAveragingCount Method

RFmxLteMXChpConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxLteMXChpAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXChpAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ChpAveragingCount

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7b74c42c-3a6b-d657-dfdf-1841ef1e3c1b.htm language=enus -->
## TOPIC 00193: rfmxltedotnet/html/7b74c42c-3a6b-d657-dfdf-1841ef1e3c1b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7b74c42c-3a6b-d657-dfdf-1841ef1e3c1b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7b74c42c-3a6b-d657-dfdf-1841ef1e3c1b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetMeasurementOffset Method

RFmxLteMXModAccConfigurationGetMeasurementOffset Method

SetSynchronizationMode(String, RFmxLteMXModAccSynchronizationMode)

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxLteMXModAccSynchronizationMode) method. This value is expressed in slots.

###### Return Value

Int32

##### Remarks

ModAccMeasurementOffset

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7bd0d18b-20af-c203-e172-3297889e6a0a.htm language=enus -->
## TOPIC 00194: rfmxltedotnet/html/7bd0d18b-20af-c203-e172-3297889e6a0a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7bd0d18b-20af-c203-e172-3297889e6a0a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7bd0d18b-20af-c203-e172-3297889e6a0a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.SetAveragingCount Method

RFmxLteMXObwConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxLteMXObwAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXObwAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ObwAveragingCount

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7c0f315a-b0c4-515f-5cc6-7a28e68605e6.htm language=enus -->
## TOPIC 00195: rfmxltedotnet/html/7c0f315a-b0c4-515f-5cc6-7a28e68605e6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7c0f315a-b0c4-515f-5cc6-7a28e68605e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7c0f315a-b0c4-515f-5cc6-7a28e68605e6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.SetAveragingType Method

RFmxLteMXObwConfigurationSetAveragingType Method

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxLteMXObwAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxLteMXObwAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwAveragingTypeSpecifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

###### Return Value

Int32

##### Remarks

ObwAveragingType

Rms

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7c19e634-39b7-c450-fa05-b36cdc11045a.htm language=enus -->
## TOPIC 00196: rfmxltedotnet/html/7c19e634-39b7-c450-fa05-b36cdc11045a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7c19e634-39b7-c450-fa05-b36cdc11045a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7c19e634-39b7-c450-fa05-b36cdc11045a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpNoiseCompensationType Enumeration

RFmxLteMXChpNoiseCompensationType Enumeration

Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXChpNoiseCompensationType
```

```text
Public Enumeration RFmxLteMXChpNoiseCompensationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalyzerAndTermination | 0 | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
|  | AnalyzerOnly | 1 | Compensates only for analyzer noise. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7c83b6c4-93ee-3aaf-d92d-cc989bac931f.htm language=enus -->
## TOPIC 00197: rfmxltedotnet/html/7c83b6c4-93ee-3aaf-d92d-cc989bac931f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7c83b6c4-93ee-3aaf-d92d-cc989bac931f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7c83b6c4-93ee-3aaf-d92d-cc989bac931f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchSynchronizationSignalConstellation Method

RFmxLteMXModAccResultsFetchSynchronizationSignalConstellation Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSynchronizationSignalConstellation(
	string selectorString,
	double timeout,
	ref ComplexSingle[] sssConstellation,
	ref ComplexSingle[] pssConstellation
)
```

```text
Public Function FetchSynchronizationSignalConstellation ( 
	selectorString As String,
	timeout As Double,
	ByRef sssConstellation As ComplexSingle(),
	ByRef pssConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **sssConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains SSS constellation trace.
- **pssConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains PSS constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7d421b41-a3c4-18e4-a249-ff1201015610.htm language=enus -->
## TOPIC 00198: rfmxltedotnet/html/7d421b41-a3c4-18e4-a249-ff1201015610.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7d421b41-a3c4-18e4-a249-ff1201015610.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7d421b41-a3c4-18e4-a249-ff1201015610.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPsschNumberOfResourceBlocks Method

RFmxLteMXComponentCarrierGetPsschNumberOfResourceBlocks Method

Gets the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPsschNumberOfResourceBlocks(
	string selectorString,
	out int value
)
```

```text
Public Function GetPsschNumberOfResourceBlocks ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation.

###### Return Value

Int32

##### Remarks

PsschNumberOfResourceBlocks

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7d73b2e2-5518-4074-aeb2-ef5ac2b38a6c.htm language=enus -->
## TOPIC 00199: rfmxltedotnet/html/7d73b2e2-5518-4074-aeb2-ef5ac2b38a6c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7d73b2e2-5518-4074-aeb2-ef5ac2b38a6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7d73b2e2-5518-4074-aeb2-ef5ac2b38a6c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetMaximumPeakIQOriginOffset Method

RFmxLteMXModAccResultsGetMaximumPeakIQOriginOffset Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumPeakIQOriginOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumPeakIQOriginOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the estimated maximum IQ origin offset over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBc.

###### Return Value

Int32

##### Remarks

ModAccResultsMaximumPeakIQOriginOffset

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7dc94757-8b29-e4a4-13f7-a5e5b5754452.htm language=enus -->
## TOPIC 00200: rfmxltedotnet/html/7dc94757-8b29-e4a4-13f7-a5e5b5754452.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7dc94757-8b29-e4a4-13f7-a5e5b5754452.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7dc94757-8b29-e4a4-13f7-a5e5b5754452.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetFftOverlap Method

RFmxLteMXAcpConfigurationSetFftOverlap Method

SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod)

SequentialFft

SetFftOverlapMode(String, RFmxLteMXAcpFftOverlapMode)

UserDefined

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftOverlap(
	string selectorString,
	double value
)
```

```text
Public Function SetFftOverlap ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, the samples to overlap between the consecutive chunks as a percentage of the AcpSequentialFftSize property value.

###### Return Value

Int32

##### Remarks

AcpFftOverlap

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7e085628-aba3-ed9b-6b24-d6388fec61ec.htm language=enus -->
## TOPIC 00201: rfmxltedotnet/html/7e085628-aba3-ed9b-6b24-d6388fec61ec.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7e085628-aba3-ed9b-6b24-d6388fec61ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7e085628-aba3-ed9b-6b24-d6388fec61ec.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetNumberOfSubblocks Method

RFmxLteMXGetNumberOfSubblocks Method

Gets the number of subblocks that are configured in intra-band non-contiguous carrier aggregation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfSubblocks(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfSubblocks ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the number of subblocks that are configured in intra-band non-contiguous carrier aggregation.

###### Return Value

Int32

##### Remarks

NumberOfSubblocks

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7e1802e2-22ab-96ef-c80d-08686e71192e.htm language=enus -->
## TOPIC 00202: rfmxltedotnet/html/7e1802e2-22ab-96ef-c80d-08686e71192e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7e1802e2-22ab-96ef-c80d-08686e71192e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7e1802e2-22ab-96ef-c80d-08686e71192e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetDeltaFMaximum Method

RFmxLteMXSemConfigurationGetDeltaFMaximum Method

Gets the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDoubleUpon return, contains the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemDeltaFMaximum

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7e75be19-d997-0aec-8052-0122194ccadf.htm language=enus -->
## TOPIC 00203: rfmxltedotnet/html/7e75be19-d997-0aec-8052-0122194ccadf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7e75be19-d997-0aec-8052-0122194ccadf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7e75be19-d997-0aec-8052-0122194ccadf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPuschModulationType Method

RFmxLteMXComponentCarrierGetPuschModulationType Method

Gets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschModulationType(
	string selectorString,
	out RFmxLteMXPuschModulationType value
)
```

```text
Public Function GetPuschModulationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXPuschModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPuschModulationTypeUpon return, contains the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

PuschModulationType

ModulationTypeQpsk

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7eed7edd-b201-1460-02bc-097f26733c8b.htm language=enus -->
## TOPIC 00204: rfmxltedotnet/html/7eed7edd-b201-1460-02bc-097f26733c8b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7eed7edd-b201-1460-02bc-097f26733c8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7eed7edd-b201-1460-02bc-097f26733c8b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpNoiseCompensationEnabled Enumeration

RFmxLteMXChpNoiseCompensationEnabled Enumeration

SetNoiseCalibrationMode(String, RFmxLteMXChpNoiseCalibrationMode)

Auto

Manual

SetMeasurementMode(String, RFmxLteMXChpMeasurementMode)

Measure

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXChpNoiseCompensationEnabled
```

```text
Public Enumeration RFmxLteMXChpNoiseCompensationEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Disables noise compensation. |
|  | True | 1 | Enables noise compensation. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7f19efef-f49b-ad51-c6e4-c83914721892.htm language=enus -->
## TOPIC 00205: rfmxltedotnet/html/7f19efef-f49b-ad51-c6e4-c83914721892.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7f19efef-f49b-ad51-c6e4-c83914721892.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7f19efef-f49b-ad51-c6e4-c83914721892.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetSweepTimeInterval Method

RFmxLteMXChpConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxLteMXChpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSweepTimeInterval(
	string selectorString,
	double value
)
```

```text
Public Function SetSweepTimeInterval ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXChpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ChpSweepTimeInterval

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7f288989-7c69-e497-6e1f-a0965d4fe5d0.htm language=enus -->
## TOPIC 00206: rfmxltedotnet/html/7f288989-7c69-e497-6e1f-a0965d4fe5d0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7f288989-7c69-e497-6e1f-a0965d4fe5d0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7f288989-7c69-e497-6e1f-a0965d4fe5d0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.ConfigureOffsetFrequency Method

RFmxLteMXSemConfigurationConfigureOffsetFrequency Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetFrequency(
	string selectorString,
	double offsetStartFrequency,
	double offsetStopFrequency,
	RFmxLteMXSemOffsetSideband offsetSideband
)
```

```text
Public Function ConfigureOffsetFrequency ( 
	selectorString As String,
	offsetStartFrequency As Double,
	offsetStopFrequency As Double,
	offsetSideband As RFmxLteMXSemOffsetSideband
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the signal name, subblock number, and offset number. Example:"subblock0/offset0" You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **offsetStartFrequency**
  - Type: SystemDoubleSpecifies the start frequency of an offset segment relative to the carrier channel bandwidth edge (single-carrier) or the subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz.
- **offsetStopFrequency**
  - Type: SystemDoubleSpecifies the stop frequency of an offset segment relative to the carrier channel bandwidth edge (single-carrier) or the subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz.
- **offsetSideband**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemOffsetSidebandSpecifies whether the offset segment is present on one side, or on both sides of the carrier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7f50d104-f28e-8825-fb25-b252562daea4.htm language=enus -->
## TOPIC 00207: rfmxltedotnet/html/7f50d104-f28e-8825-fb25-b252562daea4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7f50d104-f28e-8825-fb25-b252562daea4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7f50d104-f28e-8825-fb25-b252562daea4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetUplinkMaskType Method

RFmxLteMXSemConfigurationGetUplinkMaskType Method

General_CAClassB

CANS04

CANCNS01

Custom

3GPP 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkMaskType(
	string selectorString,
	out RFmxLteMXSemUplinkMaskType value
)
```

```text
Public Function GetUplinkMaskType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSemUplinkMaskType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemUplinkMaskType Upon return, contains the spectrum emission mask used in the measurement for uplink. Each mask type refers to a different Network Signalled (NS) value. General_CAClassB, CANS04, and CANCNS01 refers to carrier aggregation case. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2.1 of the 3GPP 36.521 specification for more information about standard-defined mask types.

###### Return Value

Int32

##### Remarks

SemUplinkMaskType

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7fdb0435-93d3-4a34-11dd-b4fae9a49fd5.htm language=enus -->
## TOPIC 00208: rfmxltedotnet/html/7fdb0435-93d3-4a34-11dd-b4fae9a49fd5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7fdb0435-93d3-4a34-11dd-b4fae9a49fd5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7fdb0435-93d3-4a34-11dd-b4fae9a49fd5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchNPuschConstellationTrace Method

RFmxLteMXModAccResultsFetchNPuschConstellationTrace Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchNPuschConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] dataConstellation,
	ref ComplexSingle[] dmrsConstellation
)
```

```text
Public Function FetchNPuschConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef dataConstellation As ComplexSingle(),
	ByRef dmrsConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **dataConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the data constellation trace.
- **dmrsConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the demodulation reference signal (DMRS) constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/7fe311b2-456f-1725-9bde-10f21e330cdf.htm language=enus -->
## TOPIC 00209: rfmxltedotnet/html/7fe311b2-456f-1725-9bde-10f21e330cdf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/7fe311b2-456f-1725-9bde-10f21e330cdf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/7fe311b2-456f-1725-9bde-10f21e330cdf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpResults.FetchAbsolutePowersTrace Method

RFmxLteMXAcpResultsFetchAbsolutePowersTrace Method

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: NationalInstrumentsSpectrumSingle Returns the trace of the measured integrated power in the channel specified by the traceIndex parameter. The carrier power is reported in dBm when you set the RFmxLteMXAcpPowerUnits method to dBm, and in dBm/Hz when you set the RFmxLteMXAcpPowerUnits method to dBm/Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/80588e88-b760-3933-0ea3-b33f6de0547c.htm language=enus -->
## TOPIC 00210: rfmxltedotnet/html/80588e88-b760-3933-0ea3-b33f6de0547c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/80588e88-b760-3933-0ea3-b33f6de0547c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/80588e88-b760-3933-0ea3-b33f6de0547c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetAutoNPuschChannelDetectionEnabled Method

RFmxLteMXComponentCarrierGetAutoNPuschChannelDetectionEnabled Method

SetNPuschToneOffset(String, Int32)

SetNPuschModulationType(String, RFmxLteMXNPuschModulationType)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoNPuschChannelDetectionEnabled(
	string selectorString,
	out RFmxLteMXAutoNPuschChannelDetectionEnabled value
)
```

```text
Public Function GetAutoNPuschChannelDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAutoNPuschChannelDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoNPuschChannelDetectionEnabled Upon return, contains whether the values of the SetNPuschToneOffset(String, Int32), NPUSCH Number of Tones, and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) properties are auto-detected by the measurement or specified by you.

###### Return Value

Int32

##### Remarks

AutoNPuschChannelDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/805e3173-074e-8538-e240-651ed8c5ff61.htm language=enus -->
## TOPIC 00211: rfmxltedotnet/html/805e3173-074e-8538-e240-651ed8c5ff61.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/805e3173-074e-8538-e240-651ed8c5ff61.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/805e3173-074e-8538-e240-651ed8c5ff61.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetSweepTimeInterval Method

RFmxLteMXAcpConfigurationGetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxLteMXAcpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetSweepTimeInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXAcpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

AcpSweepTimeInterval

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/80dee843-28dd-5ab3-c63b-082cd752d13d.htm language=enus -->
## TOPIC 00212: rfmxltedotnet/html/80dee843-28dd-5ab3-c63b-082cd752d13d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/80dee843-28dd-5ab3-c63b-082cd752d13d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/80dee843-28dd-5ab3-c63b-082cd752d13d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetLowerOffsetAbsoluteIntegratedPower Method

RFmxLteMXSemResultsGetLowerOffsetAbsoluteIntegratedPower Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetAbsoluteIntegratedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetAbsoluteIntegratedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetAbsoluteIntegratedPower

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8119134b-4af7-e450-0946-5ccde35cd15a.htm language=enus -->
## TOPIC 00213: rfmxltedotnet/html/8119134b-4af7-e450-0946-5ccde35cd15a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8119134b-4af7-e450-0946-5ccde35cd15a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8119134b-4af7-e450-0946-5ccde35cd15a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.BuildCarrierString Method

RFmxLteMXBuildCarrierString Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildCarrierString(
	string selectorString,
	int carrierNumber
)
```

```text
Public Shared Function BuildCarrierString ( 
	selectorString As String,
	carrierNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildResultString(String) method to build the selector string.
- **carrierNumber**
  - Type: SystemInt32 Specifies the carrier number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/81419ae8-61ee-b55a-e4ef-ad204c48c087.htm language=enus -->
## TOPIC 00214: rfmxltedotnet/html/81419ae8-61ee-b55a-e4ef-ad204c48c087.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/81419ae8-61ee-b55a-e4ef-ad204c48c087.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/81419ae8-61ee-b55a-e4ef-ad204c48c087.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchInBandEmissionTrace Method

RFmxLteMXModAccResultsFetchInBandEmissionTrace Method

3GPP 36.521

3GPP 36.521

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchInBandEmissionTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> inBandEmission,
	ref AnalogWaveform<float> inBandEmissionMask
)
```

```text
Public Function FetchInBandEmissionTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef inBandEmission As AnalogWaveform(Of Single),
	ByRef inBandEmissionMask As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **inBandEmission**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the in-band emission margin.
- **inBandEmissionMask**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the in-band emission mask.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/81c31ee8-427f-70a0-0237-3738dde79269.htm language=enus -->
## TOPIC 00215: rfmxltedotnet/html/81c31ee8-427f-70a0-0237-3738dde79269.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/81c31ee8-427f-70a0-0237-3738dde79269.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/81c31ee8-427f-70a0-0237-3738dde79269.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpResults.FetchMeasurement Method

RFmxLteMXTxpResultsFetchMeasurement Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurement(
	string selectorString,
	double timeout,
	out double averagePowerMean,
	out double peakPowerMaximum
)
```

```text
Public Function FetchMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef averagePowerMean As Double,
	<OutAttribute> ByRef peakPowerMaximum As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the RFmxLTE Build Subblock String method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **averagePowerMean**
  - Type: SystemDoubleUpon return, contains the average power of the the signal over which power measurments are performed. This value is expressed in dBm.
- **peakPowerMaximum**
  - Type: SystemDoubleUpon return, contains the peak power of the the signal over which power measurments are performed. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXTxpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/81fcf9de-b4ed-9051-945b-fc128c4a6923.htm language=enus -->
## TOPIC 00216: rfmxltedotnet/html/81fcf9de-b4ed-9051-945b-fc128c4a6923.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/81fcf9de-b4ed-9051-945b-fc128c4a6923.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/81fcf9de-b4ed-9051-945b-fc128c4a6923.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetAveragingCount Method

RFmxLteMXModAccConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxLteMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXModAccAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ModAccAveragingCount

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/82230182-7536-5c9d-a759-ee039e09d904.htm language=enus -->
## TOPIC 00217: rfmxltedotnet/html/82230182-7536-5c9d-a759-ee039e09d904.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/82230182-7536-5c9d-a759-ee039e09d904.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/82230182-7536-5c9d-a759-ee039e09d904.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults Class

RFmxLteMXModAccResults Class

Provides methods to fetch and read the ModAcc measurement results.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXModAccResults : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXModAccResults
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXModAccResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchCompositeEvm | Fetches the composite EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchCompositeEvmArray | Returns an array of the composite EVM for ModAcc measurements. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchCompositeMagnitudeAndPhaseError | Returns the mean RMS composite magnitude error, phase error, the maximum peak composite magnitude error, and the phase error. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchCompositeMagnitudeAndPhaseErrorArray | Returns the arrays of the mean RMS composite magnitude error and phase error, and the max peak composite magnitude error and phase error. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchCsrsConstellation | Fetches the constellation trace for a cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchCsrsEvm | Fetches the cell-specific reference signal EVM. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read results from this method. |
|  | FetchCsrsEvmArray | Fetches the array of CSRS EVMs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchDownlinkDetectedCellID | Fetches the detected cell ID. This method is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS). Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkDetectedCellIDArray | Fetches the array of detected cell IDs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchDownlinkPbchConstellation | Fetches the PBCH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkPcfichConstellation | Fetches the PCFICH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkPdcchConstellation | Fetches the PDCCH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkPhichConstellation | Fetches the PHICH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkTransmitPower | Fetches the reference signal power and the OFDM symbol transmit power. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkTransmitPowerArray | Fetches the array of reference signal powers and the OFDM symbol transmit powers for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchEvmHighPerSymbolTrace | Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmLowPerSymbolTrace | Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C-W/2. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmPerSlotTrace | Returns the EVM of each slot averaged across all the symbols within the slots and all the allocated subcarriers. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmPerSubcarrierTrace | Returns the EVM of each allocated subcarrier averaged across all the symbols within the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmPerSymbolTrace | Returns the EVM on each symbol within the SetMeasurementLength(String, Int32) method averaged across all the allocated subcarriers. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method. |
|  | FetchInBandEmissionMargin | Returns the in-band emission margin on non allocated resource blocks (RBs) in the uplink signal. This value is expressed in dB. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchInBandEmissionMarginArray | Returns an array of margins on non allocated resource blocks (RBs) in the uplink signal for all component carriers within the subblock. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchInBandEmissionTrace | Returns the in-band emission (IBE) and limit traces. In-band emission is the interference falling into non allocated resource blocks. The IBE for various spectral regions (general, carrier leakage, and I/Q image) are evaluated according to section 6.5.2.3.5 of the 3GPP 36.521 specification and concatenated to form a composite trace. The limit trace is derived from the limits in the section 6.5.2.3.5 of the 3GPP 36.521 specification. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchIQImpairments | Returns the mean I/Q origin offset, mean I/Q gain imbalance, and mean I/Q quadrature error. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchIQImpairmentsArray | Returns an array of the mean I/Q origin offset, mean I/Q gain imbalance, and mean I/Q quadrature error. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchMaximumEvmPerSlotTrace | Returns the peak value of an EVM for each slot computed across all the symbols and all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumEvmPerSubcarrierTrace | Returns the peak value of an EVM for each allocated subcarrier computed across all the symbols within the value of the SetMeasurementLength(String, Int32). The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumEvmPerSymbolTrace | Returns the peak value of an EVM for each symbol computed across all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumFrequencyErrorPerSlotTrace | Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumMagnitudeErrorPerSymbolTrace | Returns the peak value of the magnitude error for each symbol computed across all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumPhaseErrorPerSymbolTrace | Returns the peak value of the phase error for each symbol computed across all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchNPuschConstellationTrace | Returns the recovered narrowband physical uplink shared channel (NPUSCH) constellation points. The constellation points of different slots in the measurement length are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchNPuschDataEvm | Fetches the narrowband physical uplink shared channel (NPUSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | FetchNPuschDmrsEvm | Fetches the EVM values calculated on NPUSCH DMRS over the length of the measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | FetchNPuschSymbolPower | Fetches the narrowband physical uplink shared channel (NPUSCH) symbol powers. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch1024QamConstellation | Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch1024QamEvm | Fetches the physical downlink shared channel (PDSCH) 1024QAM EVMs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch1024QamEvmArray | Fetches an array of physical downlink shared channel (PDSCH) 1024QAM EVMs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPdsch16QamConstellation | Fetches the physical downlink shared channel (PDSCH) 16 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch256QamConstellation | Fetches the physical downlink shared channel (PDSCH) 256 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch64QamConstellation | Fetches the physical downlink shared channel (PDSCH) 64 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdschEvm | Fetches the physical downlink shared channel (PDSCH) EVMs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdschEvmArray | Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPdschQpskConstellation | Fetches the physical downlink shared channel (PDSCH) QPSK trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPsschConstellationTrace | Returns the recovered physical sidelink shared channel (PSSCH) constellation points. The constellation points of different slots in the measurement length are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPsschDataEvm | Fetches the physical sidelink shared channel (PSSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschDataEvmArray | Fetches the array of the physical sidelink shared channel (PSSCH) data EVM for ModAcc measurements. Use "subblock(n)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschDmrsEvm | Fetches the EVM values calculated on PSSCH DMRS over the length of the measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschDmrsEvmArray | Fetches the array of the EVM values calculated on PSSCH DMRS over the length of the measurement. Use "subblock(n)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschSymbolPower | Fetches the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPsschSymbolPowerArray | Fetches the array of the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPuschConstellationTrace | Returns the recovered physical uplink shared channel (PUSCH) constellation points. The constellation points of different slots in the SetMeasurementLength(String, Int32) are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDataEvm | Fetches the physical uplink shared channel (PUSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDataEvmArray | Returns an array of the Mean RMS PUSCH data EVM and the maximum peak PUSCH data EVM. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPuschDemodulatedBits | Fetches the recovered bits during EVM calculation. The bits of different slots in the SetMeasurementLength(String, Int32) method are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDmrsEvm | Fetches the EVM values calculated on PUSCH DMRS calculated over the length of the measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDmrsEvmArray | Returns an array of the PUSCH mean RMS DMRS EVM and the PUSCH maximum peak DMRS EVM of all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPuschSymbolPower | Fetches the physical uplink shared channel (PUSCH) symbol power measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschSymbolPowerArray | Returns an array of powers of the physical uplink shared channel (PUSCH) data symbols and DMRS of all the component carriers in the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchRmsMagnitudeErrorPerSymbolTrace | Returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchRmsPhaseErrorPerSymbolTrace | Returns the RMS mean value of the phase error for each symbol computed over all the allocated subcarriers and within the measurement length. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSpectralFlatness | Returns the spectral flatness measurements of the component carrier. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSpectralFlatnessArray | Returns the arrays of spectral flatness measurements of all component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSpectralFlatnessTrace | Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of the 3GPP TS 36.521 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSrsConstellation | Fetches the constellation trace for the SRS channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSrsEvm | Fetches the mean RMS EVM and the mean power for the SRS channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSrsEvmArray | Fetches the array of SRS EVMs for all the component carriers within the subblock. This value is expressed in percentage or dB. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSubblockInBandEmissionMargin | Returns the margin on non-allocated resource blocks (RBs) within the subblock aggregated bandwidth. This value is expressed in dB. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Refer to section 6.5.2A.3 of the 3GPP TS 36.521 specification for more information about in-band emission margin. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSubblockInBandEmissionTrace | Returns the in-band emission trace and the limit trace within the subblock aggregated bandwidth. The in-band emissions are a measure of the interference in the non-allocated resources blocks. The in-band emissions for various regions, such as general, carrier leakage, and I/Q image, are evaluated according to the method defined in the 3GPP 36.521 specification, and concatenated to form a composite trace. Limit trace is derived from the limits defined in section 6.5.2A.3 of the 3GPP TS 36.521 specification. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSubblockIQImpairments | Returns the mean I/Q origin offset, the mean I/Q gain imbalance, and the mean I/Q quadrature error of a subblock. This method is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Otherwise, the method returns NaN, as measurements of this result are currently not supported. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSynchronizationSignalConstellation | Fetches the constellations traces for PSS and SSS. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSynchronizationSignalEvm | Fetches the primary synchronization signal (PSS) EVM and secondary synchronization signal (SSS) EVM. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSynchronizationSignalEvmArray | Fetches the array of primary synchronization signal (PSS) EVMs and secondary synchronization signal (SSS) EVMS for all the component carriers within a subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | GetDownlinkDetectedCellID | Gets the detected cell ID value. |
|  | GetDownlinkOfdmSymbolTransmitPower | Gets the mean value of power calculated in one OFDM symbol over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetDownlinkRSTransmitPower | Gets the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetInBandEmissionMargin | Gets the in-band emission margin. This value is expressed in dB. |
|  | GetMaximumPeakCompositeEvm | Gets the maximum value of the peak EVMs calculated on all the configured channels over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMaximumPeakCompositeMagnitudeError | Gets the peak value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels. |
|  | GetMaximumPeakCompositePhaseError | Gets the peak value of phase error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all thee configured channels. This value is expressed in degrees. |
|  | GetMaximumPeakFrequencyError | Gets the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in Hz. |
|  | GetMaximumPeakIQOriginOffset | Gets the estimated maximum IQ origin offset over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBc. |
|  | GetMeanFrequencyError | Gets the estimated carrier frequency offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetMeanIQGainImbalance | Gets the estimated I/Q gain imbalance averaged over the measurement length. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. NoteWhen you set the CC Bandwidth Method to 200.0 k and the NPUSCH Num Tones Method to 12, this result is available. For other values of NPUSCH Num Tones, this result will be reported as NaN. |
| Note |  |  |
| When you set the CC Bandwidth Method to 200.0 k and the NPUSCH Num Tones Method to 12, this result is available. For other values of NPUSCH Num Tones, this result will be reported as NaN. |  |  |
|  | GetMeanIQOriginOffset | Gets the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBc. |
|  | GetMeanIQTimingSkew | Returns the estimated IQ timing skew averaged over measured length. IQ timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds |
|  | GetMeanQuadratureError | Gets the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in degrees. |
|  | GetMeanRmsCompositeEvm | Gets the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsCompositeMagnitudeError | Gets the RMS mean value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels. |
|  | GetMeanRmsCompositePhaseError | Gets the RMS mean value of the composite phase error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels. This value is expressed in degrees. |
|  | GetMeanRmsCsrsEvm | Gets the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPbchEvm | Gets the mean value of RMS EVMs calculated on PBCH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPcfichEvm | Gets the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPdcchEvm | Gets the mean value of RMS EVMs calculated on PDCCH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPhichEvm | Gets the mean value of RMS EVMs calculated on PHICH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPssEvm | Gets the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsSrsEvm | Gets the mean value of RMS EVMs calculated on the SRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsSssEvm | Gets the mean value of RMS EVMs calculated on secondary synchronization signal (SSS) channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanSrsPower | Gets the mean value of power calculated on SRS over the slots specified by the SetMeasurementLength(String, Int32) method. This values is expressed in dBm. |
|  | GetMeanSymbolClockError | Gets the estimated symbol clock error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in ppm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetMeanTimeOffset | Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of ModAccSynchronizationMode method. This value is expressed in seconds. |
|  | GetNPuschMaximumPeakDataEvm | Gets the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetNPuschMaximumPeakDmrsEvm | Gets the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetNPuschMeanDataPower | Gets the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetNPuschMeanDmrsPower | Gets the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetNPuschMeanRmsDataEvm | Gets the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetNPuschMeanRmsDmrsEvm | Gets the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms1024QamEvm | Gets the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms16QamEvm | Gets the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms256QamEvm | Gets the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms64QamEvm | Gets the mean value of RMS EVMs calculated on all 64 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRmsEvm | Gets the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRmsQpskEvm | Gets the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPeakCompositeEvmSlotIndex | Gets the slot index where the ModAcc maximum peak composite EVM occurs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPeakCompositeEvmSubcarrierIndex | Gets the subcarrier index where the maximum peak composite EVM for ModAcc occurs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPeakCompositeEvmSymbolIndex | Gets the symbol index of the GetMaximumPeakCompositeEvm(String, Double) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMaximumPeakDataEvm | Gets the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMaximumPeakDmrsEvm | Gets the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanDataPower | Gets the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanDmrsPower | Gets the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanRmsDataEvm | Gets the mean value of the RMS EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanRmsDmrsEvm | Gets the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMaximumPeakDataEvm | Gets the maximum value of the peak EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMaximumPeakDmrsEvm | Gets the maximum value of the peak EVMs calculated on PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMeanDataPower | Gets the mean value of the power calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMeanDmrsPower | Gets the mean value of the power calculated on the PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetPuschMeanRmsDataEvm | Gets the mean value of the RMS EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMeanRmsDmrsEvm | Gets the mean value of the RMS EVMs calculated on the PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetSpectralFlatnessRange1MaximumToRange1Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. This value is expressed in dB. |
|  | GetSpectralFlatnessRange1MaximumToRange2Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetSpectralFlatnessRange2MaximumToRange1Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients from frequency Measurement Offset parameter to frequency Range1. This value is expressed in dB. |
|  | GetSpectralFlatnessRange2MaximumToRange2Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Measurement Offset parameter. This value is expressed in dB. |
|  | GetSubblockInBandEmissionMargin | Gets the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB. |
|  | GetSubblockMeanIQGainImbalance | Gets the estimated I/Q gain imbalance averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock. This result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Otherwise, this parameter returns NaN, as measurement of this result is currently not supported. |
|  | GetSubblockMeanIQOriginOffset | Gets the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method in the subblock. This value is expressed in dBc. |
|  | GetSubblockMeanQuadratureError | Gets the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8258f0d8-5a9e-f24e-5b4e-70c545c02b49.htm language=enus -->
## TOPIC 00218: rfmxltedotnet/html/8258f0d8-5a9e-f24e-5b4e-70c545c02b49.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8258f0d8-5a9e-f24e-5b4e-70c545c02b49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8258f0d8-5a9e-f24e-5b4e-70c545c02b49.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetFftWindowLength Method

RFmxLteMXModAccConfigurationSetFftWindowLength Method

SetFftWindowType(String, RFmxLteMXModAccFftWindowType)

Type3GPP

3GPP 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftWindowLength(
	string selectorString,
	double value
)
```

```text
Public Function SetFftWindowLength ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(String, RFmxLteMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of 3GPP 36.521 specification for more information.

###### Return Value

Int32

##### Remarks

ModAccFftWindowLength

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/829b9fcc-8590-0040-df42-eb0e4d88a89f.htm language=enus -->
## TOPIC 00219: rfmxltedotnet/html/829b9fcc-8590-0040-df42-eb0e4d88a89f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/829b9fcc-8590-0040-df42-eb0e4d88a89f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/829b9fcc-8590-0040-df42-eb0e4d88a89f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.GetNoiseCompensationType Method

RFmxLteMXChpConfigurationGetNoiseCompensationType Method

Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCompensationType(
	string selectorString,
	out RFmxLteMXChpNoiseCompensationType value
)
```

```text
Public Function GetNoiseCompensationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXChpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpNoiseCompensationTypeUpon return, contains the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

ChpNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/831a4e56-3097-a3d1-e32c-3a18b6d00476.htm language=enus -->
## TOPIC 00220: rfmxltedotnet/html/831a4e56-3097-a3d1-e32c-3a18b6d00476.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/831a4e56-3097-a3d1-e32c-3a18b6d00476.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/831a4e56-3097-a3d1-e32c-3a18b6d00476.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetAveragingCount Method

RFmxLteMXTxpConfigurationGetAveragingCount Method

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32Upon return, contains the number of acquisitions used for averaging when Averaging Enabled is True.

###### Return Value

Int32

##### Remarks

TxpAveragingCount

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/83c38d84-42f4-f4da-7b34-5a74a348bb9d.htm language=enus -->
## TOPIC 00221: rfmxltedotnet/html/83c38d84-42f4-f4da-7b34-5a74a348bb9d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/83c38d84-42f4-f4da-7b34-5a74a348bb9d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/83c38d84-42f4-f4da-7b34-5a74a348bb9d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.ConfigureNPuschFormat Method

RFmxLteMXComponentCarrierConfigureNPuschFormat Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNPuschFormat(
	string selectorString,
	int format
)
```

```text
Public Function ConfigureNPuschFormat ( 
	selectorString As String,
	format As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **format**
  - Type: SystemInt32Specifies the NPUSCH format. A value of 1 indicates that NPUSCH carries user data (UL-SCH) and a value of 2 indicates, NPUSCH carries uplink control information.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/83d10f76-a849-3884-da3f-1d07fae7d68f.htm language=enus -->
## TOPIC 00222: rfmxltedotnet/html/83d10f76-a849-3884-da3f-1d07fae7d68f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/83d10f76-a849-3884-da3f-1d07fae7d68f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/83d10f76-a849-3884-da3f-1d07fae7d68f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetNPuschNumberOfTones Method

RFmxLteMXComponentCarrierGetNPuschNumberOfTones Method

Gets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH).

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNPuschNumberOfTones(
	string selectorString,
	out int value
)
```

```text
Public Function GetNPuschNumberOfTones ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH).

###### Return Value

Int32

##### Remarks

NPuschNumberOfTones

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/84149489-bd4d-8975-be61-102071980347.htm language=enus -->
## TOPIC 00223: rfmxltedotnet/html/84149489-bd4d-8975-be61-102071980347.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/84149489-bd4d-8975-be61-102071980347.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/84149489-bd4d-8975-be61-102071980347.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetMeanQuadratureError Method

RFmxLteMXModAccResultsGetMeanQuadratureError Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanQuadratureError(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanQuadratureError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

ModAccResultsMeanQuadratureError

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/843e70bd-c171-0c44-006e-4d76e89e3e67.htm language=enus -->
## TOPIC 00224: rfmxltedotnet/html/843e70bd-c171-0c44-006e-4d76e89e3e67.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/843e70bd-c171-0c44-006e-4d76e89e3e67.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/843e70bd-c171-0c44-006e-4d76e89e3e67.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSrsEnabled Enumeration

RFmxLteMXSrsEnabled Enumeration

Specifies whether the LTE signal getting measured contains SRS transmission.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXSrsEnabled
```

```text
Public Enumeration RFmxLteMXSrsEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Measurement expects signal without SRS transmission. |
|  | True | 1 | Measurement expects signal with SRS transmission. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/85bfe222-bd8b-8818-a541-7a1a9a8d6a11.htm language=enus -->
## TOPIC 00225: rfmxltedotnet/html/85bfe222-bd8b-8818-a541-7a1a9a8d6a11.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/85bfe222-bd8b-8818-a541-7a1a9a8d6a11.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/85bfe222-bd8b-8818-a541-7a1a9a8d6a11.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.BuildListString Method

RFmxLteMXBuildListString Method

Creates the list string.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildListString(
	string listName,
	string resultName
)
```

```text
Public Shared Function BuildListString ( 
	listName As String,
	resultName As String
) As String
```

###### Parameters

- **listName**
  - Type: SystemString Specifies the list name for building the selector string. This input accepts the list name with or without the "list::" prefix.
- **resultName**
  - Type: SystemString Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1"

###### Return Value

String

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/86f6b601-3f8c-eab3-cb8e-e03514c5a48e.htm language=enus -->
## TOPIC 00226: rfmxltedotnet/html/86f6b601-3f8c-eab3-cb8e-e03514c5a48e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/86f6b601-3f8c-eab3-cb8e-e03514c5a48e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/86f6b601-3f8c-eab3-cb8e-e03514c5a48e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetAutoResourceBlockDetectionEnabled Method

RFmxLteMXComponentCarrierGetAutoResourceBlockDetectionEnabled Method

SetPuschModulationType(String, RFmxLteMXPuschModulationType)

SetPuschNumberOfResourceBlockClusters(String, Int32)

SetPuschResourceBlockOffset(String, Int32)

SetPuschNumberOfResourceBlocks(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoResourceBlockDetectionEnabled(
	string selectorString,
	out RFmxLteMXAutoResourceBlockDetectionEnabled value
)
```

```text
Public Function GetAutoResourceBlockDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAutoResourceBlockDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoResourceBlockDetectionEnabled Upon return, contains whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) properties are auto-detected by the measurement or if you specify the values of these properties.

###### Return Value

Int32

##### Remarks

AutoResourceBlockDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/871797d0-5426-0413-5657-c754ebbee178.htm language=enus -->
## TOPIC 00227: rfmxltedotnet/html/871797d0-5426-0413-5657-c754ebbee178.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/871797d0-5426-0413-5657-c754ebbee178.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/871797d0-5426-0413-5657-c754ebbee178.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpResults.FetchSubblockMeasurement Method

RFmxLteMXAcpResultsFetchSubblockMeasurement Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSubblockMeasurement(
	string selectorString,
	double timeout,
	out double subblockPower,
	out double integrationBandwidth,
	out double frequency
)
```

```text
Public Function FetchSubblockMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef subblockPower As Double,
	<OutAttribute> ByRef integrationBandwidth As Double,
	<OutAttribute> ByRef frequency As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **subblockPower**
  - Type: SystemDouble Upon return, contains the sum of powers of all the frequency bins over the integration bandwidth of the subblock.
- **integrationBandwidth**
  - Type: SystemDouble Upon return, contains the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock.
- **frequency**
  - Type: SystemDouble Upon return, contains the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8826532a-3f7f-6373-282c-14d81dcf4939.htm language=enus -->
## TOPIC 00228: rfmxltedotnet/html/8826532a-3f7f-6373-282c-14d81dcf4939.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8826532a-3f7f-6373-282c-14d81dcf4939.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8826532a-3f7f-6373-282c-14d81dcf4939.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetSrskTC Method

RFmxLteMXComponentCarrierSetSrskTC Method

Sets the transmission comb index. If you set this method to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this method to 1, SRS is transmitted on the odd subcarriers in the allocated region.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSrskTC(
	string selectorString,
	int value
)
```

```text
Public Function SetSrskTC ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the transmission comb index. If you set this method to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this method to 1, SRS is transmitted on the odd subcarriers in the allocated region.

###### Return Value

Int32

##### Remarks

SrskTC

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8873a3ed-9052-4001-2c1d-8bb93dba8a01.htm language=enus -->
## TOPIC 00229: rfmxltedotnet/html/8873a3ed-9052-4001-2c1d-8bb93dba8a01.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8873a3ed-9052-4001-2c1d-8bb93dba8a01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8873a3ed-9052-4001-2c1d-8bb93dba8a01.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration Properties

RFmxLteMXSemConfiguration Properties

The [RFmxLteMXSemConfiguration](bfedd73d-aa2b-92af-b0b9-30b430edb15e.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ComponentCarrier | Gets the RFmxLteMXSemComponentCarrierConfiguration instance. |

Top

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8873fa04-9576-5ed1-efa2-cdc08ed3e2d6.htm language=enus -->
## TOPIC 00230: rfmxltedotnet/html/8873fa04-9576-5ed1-efa2-cdc08ed3e2d6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8873fa04-9576-5ed1-efa2-cdc08ed3e2d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8873fa04-9576-5ed1-efa2-cdc08ed3e2d6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration Methods

RFmxLteMXObwConfiguration Methods

The [RFmxLteMXObwConfiguration](c67ad35a-6e1f-d1f8-9627-60a4e6e4c7b6.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the OBW measurement. |
|  | ConfigureRbwFilter | Configures the RBW filter. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the OBW measurement. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXObwAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the OBW measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the OBW measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetRbwFilterAutoBandwidth | Gets whether the measurement computes the RBW. |
|  | GetRbwFilterBandwidth | Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | GetRbwFilterType | Gets the shape of the digital RBW filter. |
|  | GetSpan | Gets the frequency search space to find the OBW. This value is expressed in Hz. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the OBW measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXObwAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the OBW measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the OBW measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetRbwFilterAutoBandwidth | Sets whether the measurement computes the RBW. |
|  | SetRbwFilterBandwidth | Sets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | SetRbwFilterType | Sets the shape of the digital RBW filter. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/89d75e91-5ba5-b61b-5fa9-9a7ba99a4bf9.htm language=enus -->
## TOPIC 00231: rfmxltedotnet/html/89d75e91-5ba5-b61b-5fa9-9a7ba99a4bf9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/89d75e91-5ba5-b61b-5fa9-9a7ba99a4bf9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/89d75e91-5ba5-b61b-5fa9-9a7ba99a4bf9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetNumberOfPdschChannels Method

RFmxLteMXComponentCarrierSetNumberOfPdschChannels Method

Sets the number of physical downlink shared channel (PDSCH) allocations in a subframe.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfPdschChannels(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfPdschChannels ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the carrier number, subblock number and subframe number. Example: "carrier0" or "subblock0" or "subframe0" or "subblock0/carrier0/subframe0". You can use the BuildSubframeString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the number of physical downlink shared channel (PDSCH) allocations in a subframe.

###### Return Value

Int32

##### Remarks

NumberOfPdschChannels

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8b8faf0f-b3a0-8da1-576b-e5dd58190bff.htm language=enus -->
## TOPIC 00232: rfmxltedotnet/html/8b8faf0f-b3a0-8da1-576b-e5dd58190bff.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8b8faf0f-b3a0-8da1-576b-e5dd58190bff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8b8faf0f-b3a0-8da1-576b-e5dd58190bff.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtResults.GetMeanAbsoluteOnPower Method

RFmxLteMXPvtResultsGetMeanAbsoluteOnPower Method

Gets the average power of the subframes within the captured burst.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanAbsoluteOnPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanAbsoluteOnPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the subframes within the captured burst.

###### Return Value

Int32

##### Remarks

PvtResultsMeanAbsoluteOnPower

##### See Also

###### Reference

RFmxLteMXPvtResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8c3f13f7-65c3-8b4a-5959-b66782074278.htm language=enus -->
## TOPIC 00233: rfmxltedotnet/html/8c3f13f7-65c3-8b4a-5959-b66782074278.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8c3f13f7-65c3-8b4a-5959-b66782074278.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8c3f13f7-65c3-8b4a-5959-b66782074278.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.AbortMeasurements Method

RFmxLteMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8c888144-93ce-5298-1e46-561969cda916.htm language=enus -->
## TOPIC 00234: rfmxltedotnet/html/8c888144-93ce-5298-1e46-561969cda916.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8c888144-93ce-5298-1e46-561969cda916.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8c888144-93ce-5298-1e46-561969cda916.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetCenterFrequency Method

RFmxLteMXSetCenterFrequency Method

For a single carrier, this method specifies the center frequency of the acquired RF signal.

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleFor a single carrier, this method specifies the center frequency of the acquired RF signal.

###### Return Value

Int32

##### Remarks

CenterFrequency

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/8dc1d83d-b9b3-2fff-1969-d5dd38b11626.htm language=enus -->
## TOPIC 00235: rfmxltedotnet/html/8dc1d83d-b9b3-2fff-1969-d5dd38b11626.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/8dc1d83d-b9b3-2fff-1969-d5dd38b11626.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/8dc1d83d-b9b3-2fff-1969-d5dd38b11626.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.GetMeasurementEnabled Method

RFmxLteMXChpConfigurationGetMeasurementEnabled Method

Gets whether to enable the channel power measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/91e2e3e1-396e-a07e-0579-8059d4239975.htm language=enus -->
## TOPIC 00236: rfmxltedotnet/html/91e2e3e1-396e-a07e-0579-8059d4239975.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/91e2e3e1-396e-a07e-0579-8059d4239975.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/91e2e3e1-396e-a07e-0579-8059d4239975.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSem Properties

RFmxLteMXSem Properties

The [RFmxLteMXSem](dda7b0ea-61e5-0499-eabb-dd612933584d.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXSemConfiguration instance that provides methods to configure the SEM measurement. |
|  | Results | Gets the RFmxLteMXSemResults instance that provides methods to fetch and read the SEM measurement results. |

Top

##### See Also

###### Reference

RFmxLteMXSem Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/92a2a5de-232a-1be4-e9d3-16dc18dad9db.htm language=enus -->
## TOPIC 00237: rfmxltedotnet/html/92a2a5de-232a-1be4-e9d3-16dc18dad9db.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/92a2a5de-232a-1be4-e9d3-16dc18dad9db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/92a2a5de-232a-1be4-e9d3-16dc18dad9db.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.SetNumberOfOffsets Method

RFmxLteMXSemConfigurationSetNumberOfOffsets Method

Sets the number of SEM offset segments.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfOffsets(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfOffsets ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the number of SEM offset segments.

###### Return Value

Int32

##### Remarks

SemNumberOfOffsets

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/930037db-51b5-6ada-703e-ebe4cf969acb.htm language=enus -->
## TOPIC 00238: rfmxltedotnet/html/930037db-51b5-6ada-703e-ebe4cf969acb.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/930037db-51b5-6ada-703e-ebe4cf969acb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/930037db-51b5-6ada-703e-ebe4cf969acb.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemComponentCarrierResults Methods

RFmxLteMXSemComponentCarrierResults Methods

The [RFmxLteMXSemComponentCarrierResults](527c0d6b-1b6d-6502-ee5f-3448f7b4d13c.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Returns the absolute power and relative power measured in the component carrier. The relative power is relative to subblock power. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMeasurementArray | Returns an array of the absolute powers and relative powers measured in the component carriers. The relative power is relative to subblock power. Use "subblock(n)" as the selector string to read results from this method. |
|  | GetAbsoluteIntegratedPower | Gets the sum of powers of all the frequency bins over the integration bandwidth of the carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetAbsolutePeakPower | Gets the peak power in the component carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPeakFrequency | Gets the frequency at which the peak power occurs in the component carrier. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetRelativeIntegratedPower | Gets the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXSemComponentCarrierResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/933ffdfe-7b3a-efd2-9dcc-2a302b914ab1.htm language=enus -->
## TOPIC 00239: rfmxltedotnet/html/933ffdfe-7b3a-efd2-9dcc-2a302b914ab1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/933ffdfe-7b3a-efd2-9dcc-2a302b914ab1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/933ffdfe-7b3a-efd2-9dcc-2a302b914ab1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXCyclicPrefixMode Enumeration

RFmxLteMXCyclicPrefixMode Enumeration

Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXCyclicPrefixMode
```

```text
Public Enumeration RFmxLteMXCyclicPrefixMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Normal | 0 | The CP duration is 4.67 microseconds, and the number of symbols in a slot is 7. |
|  | Extended | 1 | The CP duration is 16.67 microseconds, and the number of symbols in a slot is 6. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/93a8f9ea-cd72-fde9-9852-40626d97faf3.htm language=enus -->
## TOPIC 00240: rfmxltedotnet/html/93a8f9ea-cd72-fde9-9852-40626d97faf3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/93a8f9ea-cd72-fde9-9852-40626d97faf3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/93a8f9ea-cd72-fde9-9852-40626d97faf3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetMiConfiguration Method

RFmxLteMXGetMiConfiguration Method

3GPP TS 36.141

3GPP TS 36.211

SetDuplexScheme(String, RFmxLteMXDuplexScheme)

Tdd

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMiConfiguration(
	string selectorString,
	out RFmxLteMXMiConfiguration value
)
```

```text
Public Function GetMiConfiguration ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXMiConfiguration
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXMiConfiguration Upon return, contains whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the SetDuplexScheme(String, RFmxLteMXDuplexScheme) method to Tdd.

###### Return Value

Int32

##### Remarks

MiConfiguration

Standard

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/950a3d95-d59a-087b-e590-5c6a66ead550.htm language=enus -->
## TOPIC 00241: rfmxltedotnet/html/950a3d95-d59a-087b-e590-5c6a66ead550.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/950a3d95-d59a-087b-e590-5c6a66ead550.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/950a3d95-d59a-087b-e590-5c6a66ead550.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.ConfigureMeasurementOffsetAndInterval Method

RFmxLteMXTxpConfigurationConfigureMeasurementOffsetAndInterval Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementOffsetAndInterval(
	string selectorString,
	double measurementOffset,
	double measurementInterval
)
```

```text
Public Function ConfigureMeasurementOffsetAndInterval ( 
	selectorString As String,
	measurementOffset As Double,
	measurementInterval As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementOffset**
  - Type: SystemDoubleSpecifies the offset to skip from the start of the acquired waveform for the measurement. The value is expressed in seconds.
- **measurementInterval**
  - Type: SystemDoubleSpecifies the measurement interval. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/954723fa-50c3-2afd-715d-9694a05ddbad.htm language=enus -->
## TOPIC 00242: rfmxltedotnet/html/954723fa-50c3-2afd-715d-9694a05ddbad.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/954723fa-50c3-2afd-715d-9694a05ddbad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/954723fa-50c3-2afd-715d-9694a05ddbad.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetOffsetRelativeLimitStart Method

RFmxLteMXSemConfigurationGetOffsetRelativeLimitStart Method

Gets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRelativeLimitStart(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetRelativeLimitStart ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemOffsetRelativeLimitStart

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/97697860-4e41-8038-7f22-8a8809174e49.htm language=enus -->
## TOPIC 00243: rfmxltedotnet/html/97697860-4e41-8038-7f22-8a8809174e49.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/97697860-4e41-8038-7f22-8a8809174e49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/97697860-4e41-8038-7f22-8a8809174e49.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.ClearAllNamedResults Method

RFmxLteMXListClearAllNamedResults Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The list name that is passed when creating the list is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/99362b43-7edf-4f16-c32b-43f04857c5c9.htm language=enus -->
## TOPIC 00244: rfmxltedotnet/html/99362b43-7edf-4f16-c32b-43f04857c5c9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/99362b43-7edf-4f16-c32b-43f04857c5c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/99362b43-7edf-4f16-c32b-43f04857c5c9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObw Methods

RFmxLteMXObw Methods

The [RFmxLteMXObw](ca2350cc-fc40-c9f9-d501-d3a9d8dca8dd.htm) type exposes the following members.

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

RFmxLteMXObw Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/9b8e610c-fd99-2c69-ecdd-599677e86390.htm language=enus -->
## TOPIC 00245: rfmxltedotnet/html/9b8e610c-fd99-2c69-ecdd-599677e86390.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/9b8e610c-fd99-2c69-ecdd-599677e86390.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/9b8e610c-fd99-2c69-ecdd-599677e86390.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccEvmUnit Enumeration

RFmxLteMXModAccEvmUnit Enumeration

Specifies the units of the EVM results.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccEvmUnit
```

```text
Public Enumeration RFmxLteMXModAccEvmUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Percentage | 0 | The EVM is reported as a percentage. |
|  | dB | 1 | The EVM is reported in dB. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/9ba5c132-877a-ed4b-e17a-806b09fd3fff.htm language=enus -->
## TOPIC 00246: rfmxltedotnet/html/9ba5c132-877a-ed4b-e17a-806b09fd3fff.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/9ba5c132-877a-ed4b-e17a-806b09fd3fff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/9ba5c132-877a-ed4b-e17a-806b09fd3fff.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.ConfigureAveraging Method

RFmxLteMXPvtConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxLteMXPvtAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxLteMXPvtAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxLteMXPvtAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxLteMXPvtAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPvtAveragingEnabledSpecifies whether to enable averaging for the measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.
- **averagingType**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPvtAveragingTypeSpecifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/9cb408fd-443a-3ab8-e7a5-943d8acd278a.htm language=enus -->
## TOPIC 00247: rfmxltedotnet/html/9cb408fd-443a-3ab8-e7a5-943d8acd278a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/9cb408fd-443a-3ab8-e7a5-943d8acd278a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/9cb408fd-443a-3ab8-e7a5-943d8acd278a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccIQMismatchEstimationsEnabled Enumeration

RFmxLteMXModAccIQMismatchEstimationsEnabled Enumeration

| Note |
| --- |
| Timing skew value is estimated only when you set the Link direction property to Uplink. |

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccIQMismatchEstimationsEnabled
```

```text
Public Enumeration RFmxLteMXModAccIQMismatchEstimationsEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | IQ mismatch estimation is disabled. |
|  | True | 1 | IQ mismatch estimation is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/9fa4bd3e-726d-29bb-7dcc-e5b4a891679c.htm language=enus -->
## TOPIC 00248: rfmxltedotnet/html/9fa4bd3e-726d-29bb-7dcc-e5b4a891679c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/9fa4bd3e-726d-29bb-7dcc-e5b4a891679c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/9fa4bd3e-726d-29bb-7dcc-e5b4a891679c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.ConfigureFrequency Method

RFmxLteMXConfigureFrequency Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **centerFrequency**
  - Type: SystemDouble Specifies the center frequency of the acquired RF signal for a single carrier. The parameter specifies the reference frequency of the subblock for intra-band carrier aggregation. The default value of this parameter is hardware dependent.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/9faffc5e-e9c2-11e7-6ef4-8d392c7e0179.htm language=enus -->
## TOPIC 00249: rfmxltedotnet/html/9faffc5e-e9c2-11e7-6ef4-8d392c7e0179.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/9faffc5e-e9c2-11e7-6ef4-8d392c7e0179.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/9faffc5e-e9c2-11e7-6ef4-8d392c7e0179.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPbchPower Method

RFmxLteMXComponentCarrierSetPbchPower Method

Sets the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPbchPower(
	string selectorString,
	double value
)
```

```text
Public Function SetPbchPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PbchPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a01c7972-58ef-dbee-ef67-49baa1c46bb8.htm language=enus -->
## TOPIC 00250: rfmxltedotnet/html/a01c7972-58ef-dbee-ef67-49baa1c46bb8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a01c7972-58ef-dbee-ef67-49baa1c46bb8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a01c7972-58ef-dbee-ef67-49baa1c46bb8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPuschDataEvmArray Method

RFmxLteMXModAccResultsFetchPuschDataEvmArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPuschDataEvmArray(
	string selectorString,
	double timeout,
	ref double[] meanRmsDataEvm,
	ref double[] maximumPeakDataEvm
)
```

```text
Public Function FetchPuschDataEvmArray ( 
	selectorString As String,
	timeout As Double,
	ByRef meanRmsDataEvm As Double(),
	ByRef maximumPeakDataEvm As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsDataEvm**
  - Type: SystemDouble Upon return, contains the array of the mean value of the RMS EVMs calculated on PUSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method.
- **maximumPeakDataEvm**
  - Type: SystemDouble Upon return, contains the array of the maximum value of the peak EVMs calculated on PUSCH data symbols over the slots specified by the ModAcc Meas Length method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
