# NI DOCUMENT BUNDLE: rfmx-wlan-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-wlan-dotnet start=251 end=276 -->
<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e158a177-fe2d-e004-e949-7a88b6d9be2e.htm language=enus -->
## TOPIC 00251: rfmxwlandotnet/html/e158a177-fe2d-e004-e949-7a88b6d9be2e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e158a177-fe2d-e004-e949-7a88b6d9be2e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e158a177-fe2d-e004-e949-7a88b6d9be2e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchPsduCrcStatus Method

RFmxWlanMXOfdmModAccResultsFetchPsduCrcStatus Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPsduCrcStatus(
	string selectorString,
	double timeout,
	out RFmxWlanMXOfdmModAccPsduCrcStatus psduCrcStatus
)
```

```text
Public Function FetchPsduCrcStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef psduCrcStatus As RFmxWlanMXOfdmModAccPsduCrcStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **psduCrcStatus**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccPsduCrcStatus Upon return, contains the PSDU CRC status.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e212194d-620b-7903-7b88-3fd894d9a986.htm language=enus -->
## TOPIC 00252: rfmxwlandotnet/html/e212194d-620b-7903-7b88-3fd894d9a986.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e212194d-620b-7903-7b88-3fd894d9a986.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e212194d-620b-7903-7b88-3fd894d9a986.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetReferenceLevelHeadroom Method

RFmxWlanMXSetReferenceLevelHeadroom Method

SetReferenceLevel(String, Double)

Default values

Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReferenceLevelHeadroom(
	string selectorString,
	double value
)
```

```text
Public Function SetReferenceLevelHeadroom ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

###### Return Value

Int32

##### Remarks

ReferenceLevelHeadroom

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e2212320-8acc-e813-82bc-75fb021707c0.htm language=enus -->
## TOPIC 00253: rfmxwlandotnet/html/e2212320-8acc-e813-82bc-75fb021707c0.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e2212320-8acc-e813-82bc-75fb021707c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e2212320-8acc-e813-82bc-75fb021707c0.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetDataPeakPowerMaximum Method

RFmxWlanMXDsssModAccResultsGetDataPeakPowerMaximum Method

Gets the peak power of the data field of the PPDU. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDataPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetDataPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the data field of the PPDU. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

DsssModAccResultsDataPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e280e08c-67e3-353e-8b37-6ded23dfb48e.htm language=enus -->
## TOPIC 00254: rfmxwlandotnet/html/e280e08c-67e3-353e-8b37-6ded23dfb48e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e280e08c-67e3-353e-8b37-6ded23dfb48e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e280e08c-67e3-353e-8b37-6ded23dfb48e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmPhaseRotationCoefficient3 Method

RFmxWlanMXGetOfdmPhaseRotationCoefficient3 Method

IEEE Standard P802.11be/D6.0

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmPhaseRotationCoefficient3(
	string selectorString,
	out RFmxWlanMXOfdmPhaseRotationCoefficient3 value
)
```

```text
Public Function GetOfdmPhaseRotationCoefficient3 ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmPhaseRotationCoefficient3
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmPhaseRotationCoefficient3 Upon return, contains the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D6.0 .

###### Return Value

Int32

##### Remarks

OfdmPhaseRotationCoefficient3

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e38fc835-12d3-99a8-094e-680078060ae9.htm language=enus -->
## TOPIC 00255: rfmxwlandotnet/html/e38fc835-12d3-99a8-094e-680078060ae9.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e38fc835-12d3-99a8-094e-680078060ae9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e38fc835-12d3-99a8-094e-680078060ae9.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetNumberOfAnalysisThreads Method

RFmxWlanMXDsssModAccConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for DSSSModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism for DSSSModAcc measurement.

###### Return Value

Int32

##### Remarks

DsssModAccNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e39a0c85-1b5c-1b7e-48b3-036cebfa0823.htm language=enus -->
## TOPIC 00256: rfmxwlandotnet/html/e39a0c85-1b5c-1b7e-48b3-036cebfa0823.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e39a0c85-1b5c-1b7e-48b3-036cebfa0823.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e39a0c85-1b5c-1b7e-48b3-036cebfa0823.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetUserStreamDataRmsEvmMean Method

RFmxWlanMXOfdmModAccResultsGetUserStreamDataRmsEvmMean Method

Gets the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUserStreamDataRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetUserStreamDataRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Stream number and User number. Example: "User0", "result::r1/User0" or "result::r1/User0/Stream0". You can use the BuildStreamString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsUserStreamDataRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e4000d6b-d1f6-def1-18b5-d295fccdd84a.htm language=enus -->
## TOPIC 00257: rfmxwlandotnet/html/e4000d6b-d1f6-def1-18b5-d295fccdd84a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e4000d6b-d1f6-def1-18b5-d295fccdd84a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e4000d6b-d1f6-def1-18b5-d295fccdd84a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccAveragingEnabled Enumeration

RFmxWlanMXOfdmModAccAveragingEnabled Enumeration

Specifies whether to enable averaging for OFDMModAcc measurements.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccAveragingEnabled
```

```text
Public Enumeration RFmxWlanMXOfdmModAccAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the results are averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e42ca639-7931-f366-b7e9-592567be623f.htm language=enus -->
## TOPIC 00258: rfmxwlandotnet/html/e42ca639-7931-f366-b7e9-592567be623f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e42ca639-7931-f366-b7e9-592567be623f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e42ca639-7931-f366-b7e9-592567be623f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.GetOffsetRelativeLimitStart Method

RFmxWlanMXSemConfigurationGetOffsetRelativeLimitStart Method

Gets the relative power limit corresponding to the start of the offset segment. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the relative power limit corresponding to the start of the offset segment. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemOffsetRelativeLimitStart

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e473072d-8fd5-1b71-27e6-95a2203208ad.htm language=enus -->
## TOPIC 00259: rfmxwlandotnet/html/e473072d-8fd5-1b71-27e6-95a2203208ad.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e473072d-8fd5-1b71-27e6-95a2203208ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e473072d-8fd5-1b71-27e6-95a2203208ad.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetAttributeDouble Method

RFmxWlanMXSetAttributeDouble Method

Sets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemStringSpecifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx WLAN Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemDoubleSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e5bd841a-4762-1a80-6d10-6036b1c89f06.htm language=enus -->
## TOPIC 00260: rfmxwlandotnet/html/e5bd841a-4762-1a80-6d10-6036b1c89f06.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e5bd841a-4762-1a80-6d10-6036b1c89f06.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e5bd841a-4762-1a80-6d10-6036b1c89f06.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.FetchIQImpairments Method

RFmxWlanMXDsssModAccResultsFetchIQImpairments Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchIQImpairments(
	string selectorString,
	double timeout,
	out double iqOriginOffsetMean,
	out double iqGainImbalanceMean,
	out double iqQuadratureErrorMean
)
```

```text
Public Function FetchIQImpairments ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef iqOriginOffsetMean As Double,
	<OutAttribute> ByRef iqGainImbalanceMean As Double,
	<OutAttribute> ByRef iqQuadratureErrorMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **iqOriginOffsetMean**
  - Type: SystemDouble Upon return, contains the I/Q origin offset. This value is expressed in dB. I/Q origin offset is the ratio of the mean value of the signal to the RMS value of the signal. When you set the SetAveragingEnabled(String, RFmxWlanMXDsssModAccAveragingEnabled) method to True , this parameter returns the mean of the I/Q origin offset results computed for each averaging count.
- **iqGainImbalanceMean**
  - Type: SystemDouble Upon return, contains the I/Q gain imbalance results. This value is expressed in dB. I/Q gain imbalance is the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. When you set the DSSSModAcc Averaging Enabled method to True , this parameter returns the mean of the I/Q gain imbalance results computed for each averaging count.
- **iqQuadratureErrorMean**
  - Type: SystemDouble Upon return, contains the I/Q quadrature error. This value is expressed in degrees. Quadrature error is the deviation in angle from 90 degrees between the in-phase (I) and quadrature-phase (Q) signals. When the DSSSModAcc Averaging Enabled method is set to True , this parameter returns the mean of the I/Q quadrature error results computed for each averaging count.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e61d2e2c-9c40-7457-7884-277d4adc32b6.htm language=enus -->
## TOPIC 00261: rfmxwlandotnet/html/e61d2e2c-9c40-7457-7884-277d4adc32b6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e61d2e2c-9c40-7457-7884-277d4adc32b6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e61d2e2c-9c40-7457-7884-277d4adc32b6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXExtension.GetWlanSignalConfiguration Method

RFmxWlanMXExtensionGetWlanSignalConfiguration Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetWlanSignalConfiguration(RFmxInstrMX) | Creates a new default WLAN signal configuration if it doesn't exist; otherwise, it returns the existing default WLAN signal configuration. |
|  | GetWlanSignalConfiguration(RFmxInstrMX, String) | Creates a WLAN signal configuration for specified signal name. Existing WLAN signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxWlanMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e64e4795-aab8-5c7b-b742-f1addac65188.htm language=enus -->
## TOPIC 00262: rfmxwlandotnet/html/e64e4795-aab8-5c7b-b742-f1addac65188.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e64e4795-aab8-5c7b-b742-f1addac65188.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e64e4795-aab8-5c7b-b742-f1addac65188.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.Txp Property

RFmxWlanMXTxp Property

RFmxWlanMXTxp

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXTxp Txp { get; }
```

```text
Public ReadOnly Property Txp As RFmxWlanMXTxp
	Get
```

###### Property Value

RFmxWlanMXTxp

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e68d6e60-dcd5-0075-fb4e-c31ce746ec53.htm language=enus -->
## TOPIC 00263: rfmxwlandotnet/html/e68d6e60-dcd5-0075-fb4e-c31ce746ec53.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e68d6e60-dcd5-0075-fb4e-c31ce746ec53.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e68d6e60-dcd5-0075-fb4e-c31ce746ec53.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchDecodedServiceBitsTrace Method

RFmxWlanMXOfdmModAccResultsFetchDecodedServiceBitsTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDecodedServiceBitsTrace(
	string selectorString,
	double timeout,
	ref int[] decodedServiceBits
)
```

```text
Public Function FetchDecodedServiceBitsTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef decodedServiceBits As Integer()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and user number. If you do not specify the result name, the default result instance is used. Example: "user0""result::r1/user0" You can use the BuildUserString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **decodedServiceBits**
  - Type: SystemInt32 Upon return, contains an array of Service bits obtained after demodulation and decoding.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ec12fad9-10f2-3b73-197b-3bfb28f6c753.htm language=enus -->
## TOPIC 00264: rfmxwlandotnet/html/ec12fad9-10f2-3b73-197b-3bfb28f6c753.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ec12fad9-10f2-3b73-197b-3bfb28f6c753.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ec12fad9-10f2-3b73-197b-3bfb28f6c753.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSem.Results Property

RFmxWlanMXSemResults Property

RFmxWlanMXSemResults

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXSemResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxWlanMXSemResults
	Get
```

###### Property Value

RFmxWlanMXSemResults

##### See Also

###### Reference

RFmxWlanMXSem Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ec31af17-7ff4-23da-6396-9ca4422ccb4e.htm language=enus -->
## TOPIC 00265: rfmxwlandotnet/html/ec31af17-7ff4-23da-6396-9ca4422ccb4e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ec31af17-7ff4-23da-6396-9ca4422ccb4e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ec31af17-7ff4-23da-6396-9ca4422ccb4e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetVectorAveragingTimeAlignmentEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetVectorAveragingTimeAlignmentEnabled Method

Gets whether to enable time alignment for the acquired I/Q data across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetVectorAveragingTimeAlignmentEnabled(
	string selectorString,
	out RFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabled value
)
```

```text
Public Function GetVectorAveragingTimeAlignmentEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabledUpon return, contains whether to enable time alignment for the acquired I/Q data across multiple acquisitions.

###### Return Value

Int32

##### Remarks

OfdmModAccVectorAveragingTimeAlignmentEnabled

True

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ecbb9ba4-6573-b9bc-3650-a5055620a012.htm language=enus -->
## TOPIC 00266: rfmxwlandotnet/html/ecbb9ba4-6573-b9bc-3650-a5055620a012.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ecbb9ba4-6573-b9bc-3650-a5055620a012.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ecbb9ba4-6573-b9bc-3650-a5055620a012.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchUserStreamDataRmsEvmPerSymbolMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchUserStreamDataRmsEvmPerSymbolMeanTrace Method

SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUserStreamDataRmsEvmPerSymbolMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> userStreamDataRmsEvmPerSymbolMean
)
```

```text
Public Function FetchUserStreamDataRmsEvmPerSymbolMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef userStreamDataRmsEvmPerSymbolMean As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0""result::r1/user0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **userStreamDataRmsEvmPerSymbolMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the Averaging Enabled method to True , this parameter returns the mean of the user stream data RMS EVM per symbol computed for each averaging count.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ed37c3d2-7e0f-b270-47aa-eb85ef54e177.htm language=enus -->
## TOPIC 00267: rfmxwlandotnet/html/ed37c3d2-7e0f-b270-47aa-eb85ef54e177.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ed37c3d2-7e0f-b270-47aa-eb85ef54e177.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ed37c3d2-7e0f-b270-47aa-eb85ef54e177.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmAutoPhaseRotationDetectionEnabled Method

RFmxWlanMXGetOfdmAutoPhaseRotationDetectionEnabled Method

Gets whether to enable auto detection of phase rotation coefficients.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmAutoPhaseRotationDetectionEnabled(
	string selectorString,
	out RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled value
)
```

```text
Public Function GetOfdmAutoPhaseRotationDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmAutoPhaseRotationDetectionEnabledUpon return, contains whether to enable auto detection of phase rotation coefficients.

###### Return Value

Int32

##### Remarks

OfdmAutoPhaseRotationDetectionEnabled

True

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ed97dab1-7862-7f0e-208e-b7ae7c5bb4fa.htm language=enus -->
## TOPIC 00268: rfmxwlandotnet/html/ed97dab1-7862-7f0e-208e-b7ae7c5bb4fa.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ed97dab1-7862-7f0e-208e-b7ae7c5bb4fa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ed97dab1-7862-7f0e-208e-b7ae7c5bb4fa.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetDataModulationFormat Method

RFmxWlanMXDsssModAccResultsGetDataModulationFormat Method

Gets the data modulation format results of the analyzed waveform.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDataModulationFormat(
	string selectorString,
	out RFmxWlanMXDsssModAccDataModulationFormat value
)
```

```text
Public Function GetDataModulationFormat ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXDsssModAccDataModulationFormat
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccDataModulationFormatUpon return, contains the data modulation format results of the analyzed waveform.

###### Return Value

Int32

##### Remarks

DsssModAccResultsDataModulationFormat

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/edb1e825-c704-145b-e8e7-017517b4ddb7.htm language=enus -->
## TOPIC 00269: rfmxwlandotnet/html/edb1e825-c704-145b-e8e7-017517b4ddb7.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/edb1e825-c704-145b-e8e7-017517b4ddb7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/edb1e825-c704-145b-e8e7-017517b4ddb7.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccBurstStartDetectionEnabled Enumeration

RFmxWlanMXDsssModAccBurstStartDetectionEnabled Enumeration

Specifies whether the measurement detects the rising edge of a burst in the acquired waveform.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXDsssModAccBurstStartDetectionEnabled
```

```text
Public Enumeration RFmxWlanMXDsssModAccBurstStartDetectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Disables detection of a rising edge of the burst in the acquired waveform for measurement. |
|  | True | 1 | Enables detection of a rising edge of the burst in the acquired waveform for measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/f21e7a59-2d73-0462-5213-3602a8d848f4.htm language=enus -->
## TOPIC 00270: rfmxwlandotnet/html/f21e7a59-2d73-0462-5213-3602a8d848f4.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/f21e7a59-2d73-0462-5213-3602a8d848f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/f21e7a59-2d73-0462-5213-3602a8d848f4.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchRUOffsetAndSize Method

RFmxWlanMXOfdmModAccResultsFetchRUOffsetAndSize Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRUOffsetAndSize(
	string selectorString,
	double timeout,
	out int ruOffset,
	out int ruSize
)
```

```text
Public Function FetchRUOffsetAndSize ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef ruOffset As Integer,
	<OutAttribute> ByRef ruSize As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and user number. If you do not specify the result name, the default result instance is used. Example: "user0""result::r1/user0" You can use the BuildUserString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **ruOffset**
  - Type: SystemInt32 Upon return, contains the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0.
- **ruSize**
  - Type: SystemInt32 Upon return, contains the RU size for the specified user.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/f2344021-85b9-93f4-7104-63c515d664f8.htm language=enus -->
## TOPIC 00271: rfmxwlandotnet/html/f2344021-85b9-93f4-7104-63c515d664f8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/f2344021-85b9-93f4-7104-63c515d664f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/f2344021-85b9-93f4-7104-63c515d664f8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetEhtStfAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetEhtStfAveragePowerMean Method

Gets the average power of the EHT-STF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEhtStfAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetEhtStfAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the EHT-STF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsEhtStfAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/f6cc8afc-7ad1-76f9-e30a-bc700ad25575.htm language=enus -->
## TOPIC 00272: rfmxwlandotnet/html/f6cc8afc-7ad1-76f9-e30a-bc700ad25575.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/f6cc8afc-7ad1-76f9-e30a-bc700ad25575.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/f6cc8afc-7ad1-76f9-e30a-bc700ad25575.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmFrequencyBand Enumeration

RFmxWlanMXOfdmFrequencyBand Enumeration

IEEE Standard 802.11n – 2009

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmFrequencyBand
```

```text
Public Enumeration RFmxWlanMXOfdmFrequencyBand
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Band2_4GHz | 0 | Corresponds to the ISM band ranging from 2.4 GHz to 2.5 GHz. |
|  | Band5GHz | 1 | Corresponds to the 5 GHz band. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/f7772367-8eb1-354d-a5e0-9e5968c26c84.htm language=enus -->
## TOPIC 00273: rfmxwlandotnet/html/f7772367-8eb1-354d-a5e0-9e5968c26c84.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/f7772367-8eb1-354d-a5e0-9e5968c26c84.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/f7772367-8eb1-354d-a5e0-9e5968c26c84.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetOptimizeDynamicRangeForEvmMargin Method

RFmxWlanMXOfdmModAccConfigurationSetOptimizeDynamicRangeForEvmMargin Method

SetOptimizeDynamicRangeForEvmEnabled(String, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOptimizeDynamicRangeForEvmMargin(
	string selectorString,
	double value
)
```

```text
Public Function SetOptimizeDynamicRangeForEvmMargin ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the margin above the reference level you specify when you set the SetOptimizeDynamicRangeForEvmEnabled(String, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled) method to True . This value is expressed in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccOptimizeDynamicRangeForEvmMargin

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ff708801-0aa1-2163-10a4-f1af43c1a17b.htm language=enus -->
## TOPIC 00274: rfmxwlandotnet/html/ff708801-0aa1-2163-10a4-f1af43c1a17b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ff708801-0aa1-2163-10a4-f1af43c1a17b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ff708801-0aa1-2163-10a4-f1af43c1a17b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccEvmUnit Enumeration

RFmxWlanMXDsssModAccEvmUnit Enumeration

Specifies the unit for the EVM results.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXDsssModAccEvmUnit
```

```text
Public Enumeration RFmxWlanMXDsssModAccEvmUnit
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Percentage | 0 | Returns the EVM results as a percentage. |
|  | dB | 1 | Returns the EVM results in dB. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ff8804a4-22d9-60e4-93d4-47fb4ca799e2.htm language=enus -->
## TOPIC 00275: rfmxwlandotnet/html/ff8804a4-22d9-60e4-93d4-47fb4ca799e2.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ff8804a4-22d9-60e4-93d4-47fb4ca799e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ff8804a4-22d9-60e4-93d4-47fb4ca799e2.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemUpperOffsetMeasurementStatus Enumeration

RFmxWlanMXSemUpperOffsetMeasurementStatus Enumeration

Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXSemUpperOffsetMeasurementStatus
```

```text
Public Enumeration RFmxWlanMXSemUpperOffsetMeasurementStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 | The spectrum exceeds the SEM measurement mask and limits for the upper offset segment. |
|  | Pass | 1 | The spectrum does not exceed the SEM measurement mask and limits for the upper offset segment. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ff9b7cde-fa16-9a10-e9f2-d0e30a3e500c.htm language=enus -->
## TOPIC 00276: rfmxwlandotnet/html/ff9b7cde-fa16-9a10-e9f2-d0e30a3e500c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ff9b7cde-fa16-9a10-e9f2-d0e30a3e500c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ff9b7cde-fa16-9a10-e9f2-d0e30a3e500c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetEvmUnit Method

RFmxWlanMXOfdmModAccConfigurationSetEvmUnit Method

Sets the unit for EVM results.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvmUnit(
	string selectorString,
	RFmxWlanMXOfdmModAccEvmUnit value
)
```

```text
Public Function SetEvmUnit ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccEvmUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccEvmUnitSpecifies the unit for EVM results.

###### Return Value

Int32

##### Remarks

OfdmModAccEvmUnit

dB

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
