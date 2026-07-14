# NI DOCUMENT BUNDLE: rfmx-wlan-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-wlan-dotnet start=1 end=250 -->
<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/0383ac0e-83c1-4af8-2769-ead224b12309.htm language=enus -->
## TOPIC 00001: rfmxwlandotnet/html/0383ac0e-83c1-4af8-2769-ead224b12309.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/0383ac0e-83c1-4af8-2769-ead224b12309.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/0383ac0e-83c1-4af8-2769-ead224b12309.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccFecCodingType Enumeration

RFmxWlanMXOfdmModAccFecCodingType Enumeration

Returns the FEC coding type for a specified user.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccFecCodingType
```

```text
Public Enumeration RFmxWlanMXOfdmModAccFecCodingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bcc | 0 | Indicates that the FEC coding type is BCC. |
|  | Ldpc | 1 | Indicates that the FEC coding type is LDPC. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/0449d103-8536-ed3b-323a-d5048f768b1d.htm language=enus -->
## TOPIC 00002: rfmxwlandotnet/html/0449d103-8536-ed3b-323a-d5048f768b1d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/0449d103-8536-ed3b-323a-d5048f768b1d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/0449d103-8536-ed3b-323a-d5048f768b1d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetLowerOffsetPeakFrequency Method

RFmxWlanMXSemResultsGetLowerOffsetPeakFrequency Method

Gets the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetPeakFrequency

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/04e2ac9e-e628-f175-78b4-8aea03655c94.htm language=enus -->
## TOPIC 00003: rfmxwlandotnet/html/04e2ac9e-e628-f175-78b4-8aea03655c94.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/04e2ac9e-e628-f175-78b4-8aea03655c94.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/04e2ac9e-e628-f175-78b4-8aea03655c94.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetCommonClockSourceEnabled Method

RFmxWlanMXOfdmModAccConfigurationSetCommonClockSourceEnabled Method

Sets whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCommonClockSourceEnabled(
	string selectorString,
	RFmxWlanMXOfdmModAccCommonClockSourceEnabled value
)
```

```text
Public Function SetCommonClockSourceEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccCommonClockSourceEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccCommonClockSourceEnabledSpecifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock.

###### Return Value

Int32

##### Remarks

OfdmModAccCommonClockSourceEnabled

True

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/04ed41e9-d721-91a5-e632-b553dae65449.htm language=enus -->
## TOPIC 00004: rfmxwlandotnet/html/04ed41e9-d721-91a5-e632-b553dae65449.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/04ed41e9-d721-91a5-e632-b553dae65449.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/04ed41e9-d721-91a5-e632-b553dae65449.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.FetchSpectrum Method

RFmxWlanMXSemResultsFetchSpectrum Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSpectrum(
	string selectorString,
	double timeout,
	ref Spectrum<float> spectrum,
	ref Spectrum<float> compositeMask
)
```

```text
Public Function FetchSpectrum ( 
	selectorString As String,
	timeout As Double,
	ByRef spectrum As Spectrum(Of Single),
	ByRef compositeMask As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **spectrum**
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the spectrum trace.
- **compositeMask**
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the SEM measurement mask trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/0758cca1-10d4-becf-f181-8adc60fc0ee2.htm language=enus -->
## TOPIC 00005: rfmxwlandotnet/html/0758cca1-10d4-becf-f181-8adc60fc0ee2.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/0758cca1-10d4-becf-f181-8adc60fc0ee2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/0758cca1-10d4-becf-f181-8adc60fc0ee2.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetFrequencyErrorCorrectionEnabled Method

RFmxWlanMXDsssModAccConfigurationGetFrequencyErrorCorrectionEnabled Method

Gets whether to enable frequency error correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyErrorCorrectionEnabled(
	string selectorString,
	out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled value
)
```

```text
Public Function GetFrequencyErrorCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabledUpon return, contains whether to enable frequency error correction.

###### Return Value

Int32

##### Remarks

DsssModAccFrequencyErrorCorrectionEnabled

True

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/08e51462-b750-b8bc-e322-d77d1329f4b8.htm language=enus -->
## TOPIC 00006: rfmxwlandotnet/html/08e51462-b750-b8bc-e322-d77d1329f4b8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/08e51462-b750-b8bc-e322-d77d1329f4b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/08e51462-b750-b8bc-e322-d77d1329f4b8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetOffsetRelativeLimitStart Method

RFmxWlanMXSemConfigurationSetOffsetRelativeLimitStart Method

Sets the relative power limit corresponding to the start of the offset segment. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the relative power limit corresponding to the start of the offset segment. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemOffsetRelativeLimitStart

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/09179721-8a9a-f94b-1f81-4b2ffdd31455.htm language=enus -->
## TOPIC 00007: rfmxwlandotnet/html/09179721-8a9a-f94b-1f81-4b2ffdd31455.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/09179721-8a9a-f94b-1f81-4b2ffdd31455.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/09179721-8a9a-f94b-1f81-4b2ffdd31455.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetCenterFrequency Method

RFmxWlanMXSetCenterFrequency Method

On a MIMO session, use segment(n) along with a named or default signal instance as the selector string to configure this method. Refer to the Selector Strings topic for information about the string syntax for named signals.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### Remarks

CenterFrequency

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/094c5dbb-43d5-043f-628f-0429440be1b1.htm language=enus -->
## TOPIC 00008: rfmxwlandotnet/html/094c5dbb-43d5-043f-628f-0429440be1b1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/094c5dbb-43d5-043f-628f-0429440be1b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/094c5dbb-43d5-043f-628f-0429440be1b1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetSweepTimeInterval Method

RFmxWlanMXSemConfigurationSetSweepTimeInterval Method

Sets the sweep time for the SEM measurement. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemDoubleSpecifies the sweep time for the SEM measurement. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SemSweepTimeInterval

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/0b051f21-e88f-825d-b4ea-b43c19f07949.htm language=enus -->
## TOPIC 00009: rfmxwlandotnet/html/0b051f21-e88f-825d-b4ea-b43c19f07949.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/0b051f21-e88f-825d-b4ea-b43c19f07949.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/0b051f21-e88f-825d-b4ea-b43c19f07949.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHEStfPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetHEStfPeakPowerMaximum Method

Gets the peak power of the HE-STF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHEStfPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetHEStfPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the HE-STF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHEStfPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/0f0c0d00-818a-e84f-e324-01c054c38b07.htm language=enus -->
## TOPIC 00010: rfmxwlandotnet/html/0f0c0d00-818a-e84f-e324-01c054c38b07.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/0f0c0d00-818a-e84f-e324-01c054c38b07.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/0f0c0d00-818a-e84f-e324-01c054c38b07.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetEhtSigRmsEvmMean Method

RFmxWlanMXOfdmModAccResultsGetEhtSigRmsEvmMean Method

Gets the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEhtSigRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetEhtSigRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsEhtSigRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/0f72ec81-da73-a2f7-35b0-6c2d5b84a201.htm language=enus -->
## TOPIC 00011: rfmxwlandotnet/html/0f72ec81-da73-a2f7-35b0-6c2d5b84a201.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/0f72ec81-da73-a2f7-35b0-6c2d5b84a201.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/0f72ec81-da73-a2f7-35b0-6c2d5b84a201.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampResults.GetFallTimeMean Method

RFmxWlanMXPowerRampResultsGetFallTimeMean Method

Gets the power-ramp fall time of the burst. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFallTimeMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetFallTimeMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the power-ramp fall time of the burst. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PowerRampResultsFallTimeMean

##### See Also

###### Reference

RFmxWlanMXPowerRampResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/102c7f64-8eaa-6777-888e-7b77b755de7a.htm language=enus -->
## TOPIC 00012: rfmxwlandotnet/html/102c7f64-8eaa-6777-888e-7b77b755de7a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/102c7f64-8eaa-6777-888e-7b77b755de7a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/102c7f64-8eaa-6777-888e-7b77b755de7a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemAveragingType Enumeration

RFmxWlanMXSemAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXSemAveragingType
```

```text
Public Enumeration RFmxWlanMXSemAveragingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
|  | Log | 1 | The power spectrum is averaged in a logarithmic scale. |
|  | Scalar | 2 | The square root of the power spectrum is averaged. |
|  | Maximum | 3 | The peak power in the spectrum is retained from one acquisition to the next at each frequency bin. |
|  | Minimum | 4 | The least power in the spectrum is retained from one acquisition to the next at each frequency bin. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/125a87cb-1e0d-3ecc-fb67-a2984d611e39.htm language=enus -->
## TOPIC 00013: rfmxwlandotnet/html/125a87cb-1e0d-3ecc-fb67-a2984d611e39.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/125a87cb-1e0d-3ecc-fb67-a2984d611e39.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/125a87cb-1e0d-3ecc-fb67-a2984d611e39.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchLtfSize Method

RFmxWlanMXOfdmModAccResultsFetchLtfSize Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLtfSize(
	string selectorString,
	double timeout,
	out RFmxWlanMXOfdmLtfSize ltfSize
)
```

```text
Public Function FetchLtfSize ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef ltfSize As RFmxWlanMXOfdmLtfSize
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **ltfSize**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmLtfSize Upon return, contains the HE-LTF or EHT-LTF size. This result is applicable only to 802.11ax and 802.11be signals.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/12a320d0-98f0-ad96-fff6-1405192ffe04.htm language=enus -->
## TOPIC 00014: rfmxwlandotnet/html/12a320d0-98f0-ad96-fff6-1405192ffe04.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/12a320d0-98f0-ad96-fff6-1405192ffe04.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/12a320d0-98f0-ad96-fff6-1405192ffe04.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.AutoDetectSignalAnalysisOnly Method

RFmxWlanMXAutoDetectSignalAnalysisOnly Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int AutoDetectSignalAnalysisOnly(
	string selectorString,
	ComplexWaveform<ComplexSingle> IQ
)
```

```text
Public Function AutoDetectSignalAnalysisOnly ( 
	selectorString As String,
	IQ As ComplexWaveform(Of ComplexSingle)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used
- **IQ**
  - Type: NationalInstrumentsComplexWaveformComplexSingleSpecifies the data for a complex waveform including the start, delta, and actual values.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/12a977ca-9013-c872-15d3-ec5560a9ab35.htm language=enus -->
## TOPIC 00015: rfmxwlandotnet/html/12a977ca-9013-c872-15d3-ec5560a9ab35.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/12a977ca-9013-c872-15d3-ec5560a9ab35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/12a977ca-9013-c872-15d3-ec5560a9ab35.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.AnalyzeIQ1Waveform Method

RFmxWlanMXAnalyzeIQ1Waveform Method

IQ

IQ

IQorSpectral

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string .
- **resultName**
  - Type: SystemString Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1""r1"
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

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/131a2aeb-a3ac-e998-3eb3-107cb4c7b16f.htm language=enus -->
## TOPIC 00016: rfmxwlandotnet/html/131a2aeb-a3ac-e998-3eb3-107cb4c7b16f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/131a2aeb-a3ac-e998-3eb3-107cb4c7b16f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/131a2aeb-a3ac-e998-3eb3-107cb4c7b16f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.BuildStreamString Method

RFmxWlanMXBuildStreamString Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildStreamString(
	string selectorString,
	int streamNumber
)
```

```text
Public Shared Function BuildStreamString ( 
	selectorString As String,
	streamNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **streamNumber**
  - Type: SystemInt32 Specifies the stream number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/131c66d7-9ed7-2b9a-ba1b-c02bdc557749.htm language=enus -->
## TOPIC 00017: rfmxwlandotnet/html/131c66d7-9ed7-2b9a-ba1b-c02bdc557749.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/131c66d7-9ed7-2b9a-ba1b-c02bdc557749.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/131c66d7-9ed7-2b9a-ba1b-c02bdc557749.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchChainRmsEvmPerSubcarrierMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchChainRmsEvmPerSubcarrierMeanTrace Method

SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchChainRmsEvmPerSubcarrierMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> chainRmsEvmPerSubcarrierMean
)
```

```text
Public Function FetchChainRmsEvmPerSubcarrierMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef chainRmsEvmPerSubcarrierMean As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **chainRmsEvmPerSubcarrierMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the chain RMS EVM per subcarrier trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/135efc82-d28a-cd1c-03bb-c873de906364.htm language=enus -->
## TOPIC 00018: rfmxwlandotnet/html/135efc82-d28a-cd1c-03bb-c873de906364.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/135efc82-d28a-cd1c-03bb-c873de906364.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/135efc82-d28a-cd1c-03bb-c873de906364.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmPreFecPaddingFactor Method

RFmxWlanMXSetOfdmPreFecPaddingFactor Method

Sets the pre-FEC padding factor used in 802.11ax TB PPDU and 802.11be TB PPDU for decoding PLCP service data unit (PSDU) bits.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmPreFecPaddingFactor(
	string selectorString,
	int value
)
```

```text
Public Function SetOfdmPreFecPaddingFactor ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the pre-FEC padding factor used in 802.11ax TB PPDU and 802.11be TB PPDU for decoding PLCP service data unit (PSDU) bits.

###### Return Value

Int32

##### Remarks

OfdmPreFecPaddingFactor

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/16f81bb7-cc5a-45d0-cabd-1e8aa475393c.htm language=enus -->
## TOPIC 00019: rfmxwlandotnet/html/16f81bb7-cc5a-45d0-cabd-1e8aa475393c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/16f81bb7-cc5a-45d0-cabd-1e8aa475393c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/16f81bb7-cc5a-45d0-cabd-1e8aa475393c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchChainDataRmsEvmPerSymbolMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchChainDataRmsEvmPerSymbolMeanTrace Method

SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchChainDataRmsEvmPerSymbolMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> chainDataRmsEvmPerSymbolMean
)
```

```text
Public Function FetchChainDataRmsEvmPerSymbolMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef chainDataRmsEvmPerSymbolMean As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **chainDataRmsEvmPerSymbolMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the chain data-subcarriers RMS EVM per symbol trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/175de8ea-755d-827a-d0a6-00edff0d5d64.htm language=enus -->
## TOPIC 00020: rfmxwlandotnet/html/175de8ea-755d-827a-d0a6-00edff0d5d64.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/175de8ea-755d-827a-d0a6-00edff0d5d64.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/175de8ea-755d-827a-d0a6-00edff0d5d64.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetTriggerGateEnabled Method

RFmxWlanMXGetTriggerGateEnabled Method

Enables time-domain gating of the acquired signal for SEM measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerGateEnabled(
	string selectorString,
	out RFmxWlanMXTriggerGateEnabled value
)
```

```text
Public Function GetTriggerGateEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXTriggerGateEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXTriggerGateEnabledEnables time-domain gating of the acquired signal for SEM measurement.

###### Return Value

Int32

##### Remarks

TriggerGateEnabled

False

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/19b940f7-91cb-6c49-63de-c316dedb7d6b.htm language=enus -->
## TOPIC 00021: rfmxwlandotnet/html/19b940f7-91cb-6c49-63de-c316dedb7d6b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/19b940f7-91cb-6c49-63de-c316dedb7d6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/19b940f7-91cb-6c49-63de-c316dedb7d6b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled Enumeration

RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled Enumeration

Specifies whether to enable I/Q origin offset correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled
```

```text
Public Enumeration RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Disables the I/Q origin offset correction. |
|  | True | 1 | Enables the I/Q origin offset correction. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/19d5c0e1-024d-380c-d33f-1efaca93f5e8.htm language=enus -->
## TOPIC 00022: rfmxwlandotnet/html/19d5c0e1-024d-380c-d33f-1efaca93f5e8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/19d5c0e1-024d-380c-d33f-1efaca93f5e8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/19d5c0e1-024d-380c-d33f-1efaca93f5e8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetRLSigAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetRLSigAveragePowerMean Method

Gets the average power of the RL-SIG field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRLSigAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetRLSigAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the RL-SIG field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsRLSigAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/1a0694b9-05d1-d4c7-956f-8c972e88c210.htm language=enus -->
## TOPIC 00023: rfmxwlandotnet/html/1a0694b9-05d1-d4c7-956f-8c972e88c210.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/1a0694b9-05d1-d4c7-956f-8c972e88c210.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/1a0694b9-05d1-d4c7-956f-8c972e88c210.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampConfiguration.SetMeasurementEnabled Method

RFmxWlanMXPowerRampConfigurationSetMeasurementEnabled Method

Sets whether to enable PowerRamp measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanSpecifies whether to enable PowerRamp measurement.

###### Return Value

Int32

##### Remarks

PowerRampMeasurementEnabled

##### See Also

###### Reference

RFmxWlanMXPowerRampConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/1a09101a-7dce-a4df-18a0-d7a23271daa8.htm language=enus -->
## TOPIC 00024: rfmxwlandotnet/html/1a09101a-7dce-a4df-18a0-d7a23271daa8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/1a09101a-7dce-a4df-18a0-d7a23271daa8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/1a09101a-7dce-a4df-18a0-d7a23271daa8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetStreamPilotRmsEvmMean Method

RFmxWlanMXOfdmModAccResultsGetStreamPilotRmsEvmMean Method

Gets the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStreamPilotRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetStreamPilotRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Stream number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Stream0". You can use the BuildStreamString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsStreamPilotRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/1f015bcd-cb99-ee53-2dd1-8d2f33ba0455.htm language=enus -->
## TOPIC 00025: rfmxwlandotnet/html/1f015bcd-cb99-ee53-2dd1-8d2f33ba0455.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/1f015bcd-cb99-ee53-2dd1-8d2f33ba0455.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/1f015bcd-cb99-ee53-2dd1-8d2f33ba0455.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAcc.Configuration Property

RFmxWlanMXOfdmModAccConfiguration Property

RFmxWlanMXOfdmModAccConfiguration

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXOfdmModAccConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxWlanMXOfdmModAccConfiguration
	Get
```

###### Property Value

RFmxWlanMXOfdmModAccConfiguration

##### See Also

###### Reference

RFmxWlanMXOfdmModAcc Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/1fbcb5c0-b60e-9dab-b43c-c36e41c53994.htm language=enus -->
## TOPIC 00026: rfmxwlandotnet/html/1fbcb5c0-b60e-9dab-b43c-c36e41c53994.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/1fbcb5c0-b60e-9dab-b43c-c36e41c53994.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/1fbcb5c0-b60e-9dab-b43c-c36e41c53994.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemOffsetSideband Enumeration

RFmxWlanMXSemOffsetSideband Enumeration

Specifies whether the offset segment is present on one side or on both sides of the carrier.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXSemOffsetSideband
```

```text
Public Enumeration RFmxWlanMXSemOffsetSideband
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Negative | 0 | Configures a lower offset segment to the left of the carrier. |
|  | Positive | 1 | Configures an upper offset segment to the right of the carrier. |
|  | Both | 2 | Configures both negative and positive offset segments. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/219c9c92-fa83-601d-3c0c-db37b3816473.htm language=enus -->
## TOPIC 00027: rfmxwlandotnet/html/219c9c92-fa83-601d-3c0c-db37b3816473.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/219c9c92-fa83-601d-3c0c-db37b3816473.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/219c9c92-fa83-601d-3c0c-db37b3816473.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetRmsCommonPhaseErrorMean Method

RFmxWlanMXOfdmModAccResultsGetRmsCommonPhaseErrorMean Method

Gets the RMS common phase error.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsCommonPhaseErrorMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsCommonPhaseErrorMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS common phase error.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsRmsCommonPhaseErrorMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/21cd59bc-60e4-3f4e-103d-8fa086acea7e.htm language=enus -->
## TOPIC 00028: rfmxwlandotnet/html/21cd59bc-60e4-3f4e-103d-8fa086acea7e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/21cd59bc-60e4-3f4e-103d-8fa086acea7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/21cd59bc-60e4-3f4e-103d-8fa086acea7e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.ConfigureNumberOfOffsets Method

RFmxWlanMXSemConfigurationConfigureNumberOfOffsets Method

SetMaskType(String, RFmxWlanMXSemMaskType)

Custom

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfOffsets(
	string selectorString,
	int numberOfOffsets
)
```

```text
Public Function ConfigureNumberOfOffsets ( 
	selectorString As String,
	numberOfOffsets As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **numberOfOffsets**
  - Type: SystemInt32Specifies the number of SEM offset segments.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/21d53683-25de-7c38-2aca-51ff1e076ee7.htm language=enus -->
## TOPIC 00029: rfmxwlandotnet/html/21d53683-25de-7c38-2aca-51ff1e076ee7.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/21d53683-25de-7c38-2aca-51ff1e076ee7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/21d53683-25de-7c38-2aca-51ff1e076ee7.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetIQPowerEdgeTriggerLevelType Method

RFmxWlanMXSetIQPowerEdgeTriggerLevelType Method

SetIQPowerEdgeTriggerLevel(String, Double)

SetTriggerType(String, RFmxWlanMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerLevelType(
	string selectorString,
	RFmxWlanMXIQPowerEdgeTriggerLevelType value
)
```

```text
Public Function SetIQPowerEdgeTriggerLevelType ( 
	selectorString As String,
	value As RFmxWlanMXIQPowerEdgeTriggerLevelType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXIQPowerEdgeTriggerLevelType Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to IQPowerEdge .

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevelType

Relative

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/220e0e09-23ba-b65b-d3a1-6fe004070f25.htm language=enus -->
## TOPIC 00030: rfmxwlandotnet/html/220e0e09-23ba-b65b-d3a1-6fe004070f25.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/220e0e09-23ba-b65b-d3a1-6fe004070f25.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/220e0e09-23ba-b65b-d3a1-6fe004070f25.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetMaximumMeasurementLength Method

RFmxWlanMXOfdmModAccConfigurationGetMaximumMeasurementLength Method

Gets the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumMeasurementLength(
	string selectorString,
	out int value
)
```

```text
Public Function GetMaximumMeasurementLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols.

###### Return Value

Int32

##### Remarks

OfdmModAccMaximumMeasurementLength

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/225832ab-fbdd-b8dd-c757-2b97f9ef6a2a.htm language=enus -->
## TOPIC 00031: rfmxwlandotnet/html/225832ab-fbdd-b8dd-c757-2b97f9ef6a2a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/225832ab-fbdd-b8dd-c757-2b97f9ef6a2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/225832ab-fbdd-b8dd-c757-2b97f9ef6a2a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SignalConfigurationName Property

RFmxWlanMXSignalConfigurationName Property

Gets the signal configuration name.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public string SignalConfigurationName { get; }
```

```text
Public ReadOnly Property SignalConfigurationName As String
	Get
```

###### Property Value

String

###### Implements

ISignalConfiguration.SignalConfigurationName

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/22bcb4b0-c6a9-335f-81ab-a1f73d33f198.htm language=enus -->
## TOPIC 00032: rfmxwlandotnet/html/22bcb4b0-c6a9-335f-81ab-a1f73d33f198.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/22bcb4b0-c6a9-335f-81ab-a1f73d33f198.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/22bcb4b0-c6a9-335f-81ab-a1f73d33f198.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetNumberOfAnalysisThreads Method

RFmxWlanMXSemConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for SEM measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemInt32Specifies the maximum number of threads used for parallelism for SEM measurement.

###### Return Value

Int32

##### Remarks

SemNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/22dee314-a7c3-9576-a2da-9c4cab2dbd9f.htm language=enus -->
## TOPIC 00033: rfmxwlandotnet/html/22dee314-a7c3-9576-a2da-9c4cab2dbd9f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/22dee314-a7c3-9576-a2da-9c4cab2dbd9f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/22dee314-a7c3-9576-a2da-9c4cab2dbd9f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHELtfAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetHELtfAveragePowerMean Method

Gets the average power of the HE-LTF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHELtfAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetHELtfAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the HE-LTF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHELtfAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/22ec8831-35b0-d00d-a439-95a02f06205e.htm language=enus -->
## TOPIC 00034: rfmxwlandotnet/html/22ec8831-35b0-d00d-a439-95a02f06205e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/22ec8831-35b0-d00d-a439-95a02f06205e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/22ec8831-35b0-d00d-a439-95a02f06205e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetChannelEstimationType Method

RFmxWlanMXOfdmModAccConfigurationSetChannelEstimationType Method

Sets the fields in the PPDU used to estimate the channel frequency response.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChannelEstimationType(
	string selectorString,
	RFmxWlanMXOfdmModAccChannelEstimationType value
)
```

```text
Public Function SetChannelEstimationType ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccChannelEstimationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccChannelEstimationTypeSpecifies the fields in the PPDU used to estimate the channel frequency response.

###### Return Value

Int32

##### Remarks

OfdmModAccChannelEstimationType

Reference

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/234c9bbd-10c0-4efc-9914-bd9d4af26360.htm language=enus -->
## TOPIC 00035: rfmxwlandotnet/html/234c9bbd-10c0-4efc-9914-bd9d4af26360.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/234c9bbd-10c0-4efc-9914-bd9d4af26360.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/234c9bbd-10c0-4efc-9914-bd9d4af26360.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRamp Properties

RFmxWlanMXPowerRamp Properties

The [RFmxWlanMXPowerRamp](98a4f451-4f84-bd46-4848-3d3ae53097f8.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxWlanMXPowerRampConfiguration instance that provides methods to configure the PowerRamp measurement. |
|  | Results | Gets the RFmxWlanMXPowerRampResults instance that provides methods to fetch and read the PowerRamp measurement results. |

Top

##### See Also

###### Reference

RFmxWlanMXPowerRamp Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/249ad48e-a849-6221-0c22-1929fe45482c.htm language=enus -->
## TOPIC 00036: rfmxwlandotnet/html/249ad48e-a849-6221-0c22-1929fe45482c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/249ad48e-a849-6221-0c22-1929fe45482c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/249ad48e-a849-6221-0c22-1929fe45482c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetEvmUnit Method

RFmxWlanMXDsssModAccConfigurationGetEvmUnit Method

Gets the unit for the EVM results.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmUnit(
	string selectorString,
	out RFmxWlanMXDsssModAccEvmUnit value
)
```

```text
Public Function GetEvmUnit ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXDsssModAccEvmUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccEvmUnitUpon return, contains the unit for the EVM results.

###### Return Value

Int32

##### Remarks

DsssModAccEvmUnit

Percentage

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/267f3cde-f60a-155b-9e37-5c72c1b42bd3.htm language=enus -->
## TOPIC 00037: rfmxwlandotnet/html/267f3cde-f60a-155b-9e37-5c72c1b42bd3.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/267f3cde-f60a-155b-9e37-5c72c1b42bd3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/267f3cde-f60a-155b-9e37-5c72c1b42bd3.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampConfiguration.GetAveragingEnabled Method

RFmxWlanMXPowerRampConfigurationGetAveragingEnabled Method

Gets if averaging is enabled for PowerRamp measurements.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxWlanMXPowerRampAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXPowerRampAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXPowerRampAveragingEnabledUpon return, contains if averaging is enabled for PowerRamp measurements.

###### Return Value

Int32

##### Remarks

PowerRampAveragingEnabled

False

##### See Also

###### Reference

RFmxWlanMXPowerRampConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/26d89425-7966-7796-20e5-a9b32afd80a1.htm language=enus -->
## TOPIC 00038: rfmxwlandotnet/html/26d89425-7966-7796-20e5-a9b32afd80a1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/26d89425-7966-7796-20e5-a9b32afd80a1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/26d89425-7966-7796-20e5-a9b32afd80a1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetOffsetSideband Method

RFmxWlanMXSemConfigurationSetOffsetSideband Method

Sets whether the offset segment is present on one side or on both sides of the carrier.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetSideband(
	string selectorString,
	RFmxWlanMXSemOffsetSideband value
)
```

```text
Public Function SetOffsetSideband ( 
	selectorString As String,
	value As RFmxWlanMXSemOffsetSideband
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemOffsetSidebandSpecifies whether the offset segment is present on one side or on both sides of the carrier.

###### Return Value

Int32

##### Remarks

SemOffsetSideband

Both

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/26f41cad-63ad-d15f-fcf2-d4035cadc812.htm language=enus -->
## TOPIC 00039: rfmxwlandotnet/html/26f41cad-63ad-d15f-fcf2-d4035cadc812.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/26f41cad-63ad-d15f-fcf2-d4035cadc812.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/26f41cad-63ad-d15f-fcf2-d4035cadc812.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmPreFecPaddingFactor Method

RFmxWlanMXGetOfdmPreFecPaddingFactor Method

Gets the pre-FEC padding factor used in 802.11ax TB PPDU and 802.11be TB PPDU for decoding PLCP service data unit (PSDU) bits.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmPreFecPaddingFactor(
	string selectorString,
	out int value
)
```

```text
Public Function GetOfdmPreFecPaddingFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the pre-FEC padding factor used in 802.11ax TB PPDU and 802.11be TB PPDU for decoding PLCP service data unit (PSDU) bits.

###### Return Value

Int32

##### Remarks

OfdmPreFecPaddingFactor

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/280abdbc-b3b2-3f9b-0a3e-3d26510082ff.htm language=enus -->
## TOPIC 00040: rfmxwlandotnet/html/280abdbc-b3b2-3f9b-0a3e-3d26510082ff.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/280abdbc-b3b2-3f9b-0a3e-3d26510082ff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/280abdbc-b3b2-3f9b-0a3e-3d26510082ff.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetAmplitudeTrackingEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetAmplitudeTrackingEnabled Method

Gets whether to enable pilot-based mean amplitude tracking per OFDM data symbol.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeTrackingEnabled(
	string selectorString,
	out RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled value
)
```

```text
Public Function GetAmplitudeTrackingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccAmplitudeTrackingEnabledUpon return, contains whether to enable pilot-based mean amplitude tracking per OFDM data symbol.

###### Return Value

Int32

##### Remarks

OfdmModAccAmplitudeTrackingEnabled

False

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/2887a933-9d9c-ae39-3720-1ea42cad2bda.htm language=enus -->
## TOPIC 00041: rfmxwlandotnet/html/2887a933-9d9c-ae39-3720-1ea42cad2bda.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/2887a933-9d9c-ae39-3720-1ea42cad2bda.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/2887a933-9d9c-ae39-3720-1ea42cad2bda.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.PowerRamp Property

RFmxWlanMXPowerRamp Property

RFmxWlanMXPowerRamp

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXPowerRamp PowerRamp { get; }
```

```text
Public ReadOnly Property PowerRamp As RFmxWlanMXPowerRamp
	Get
```

###### Property Value

RFmxWlanMXPowerRamp

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/2a40a580-c51c-68bf-c116-5ac5e27885cf.htm language=enus -->
## TOPIC 00042: rfmxwlandotnet/html/2a40a580-c51c-68bf-c116-5ac5e27885cf.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/2a40a580-c51c-68bf-c116-5ac5e27885cf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/2a40a580-c51c-68bf-c116-5ac5e27885cf.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemAveragingEnabled Enumeration

RFmxWlanMXSemAveragingEnabled Enumeration

Specifies whether to enable averaging for the SEM measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXSemAveragingEnabled
```

```text
Public Enumeration RFmxWlanMXSemAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The SEM measurement uses the SetAveragingCount(String, Int32) method as the number of acquisitions over which the SEM measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/2ac09804-7247-affb-ed9f-2c7f8e2e36ca.htm language=enus -->
## TOPIC 00043: rfmxwlandotnet/html/2ac09804-7247-affb-ed9f-2c7f8e2e36ca.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/2ac09804-7247-affb-ed9f-2c7f8e2e36ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/2ac09804-7247-affb-ed9f-2c7f8e2e36ca.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmPhaseRotationCoefficient1 Enumeration

RFmxWlanMXOfdmPhaseRotationCoefficient1 Enumeration

IEEE Standard P802.11be/D6.0

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmPhaseRotationCoefficient1
```

```text
Public Enumeration RFmxWlanMXOfdmPhaseRotationCoefficient1
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PlusOne | 0 | Specifies that phase rotation coefficient 1 is +1. |
|  | MinusOne | 1 | Specifies that phase rotation coefficient 1 is -1. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/2aff9a60-9862-727a-76fc-fc0cec6072a9.htm language=enus -->
## TOPIC 00044: rfmxwlandotnet/html/2aff9a60-9862-727a-76fc-fc0cec6072a9.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/2aff9a60-9862-727a-76fc-fc0cec6072a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/2aff9a60-9862-727a-76fc-fc0cec6072a9.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled Enumeration

RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled Enumeration

Specifies whether to enable I/Q quadrature error correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled
```

```text
Public Enumeration RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | I/Q quadrature error correction is disabled. |
|  | True | 1 | I/Q quadrature error correction is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/2dc38ba2-a924-36ab-d718-c227c73a7a8b.htm language=enus -->
## TOPIC 00045: rfmxwlandotnet/html/2dc38ba2-a924-36ab-d718-c227c73a7a8b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/2dc38ba2-a924-36ab-d718-c227c73a7a8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/2dc38ba2-a924-36ab-d718-c227c73a7a8b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetReferenceDataConstellationIdentifier Method

RFmxWlanMXOfdmModAccConfigurationGetReferenceDataConstellationIdentifier Method

SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReferenceDataConstellationIdentifier(
	string selectorString,
	out string value
)
```

```text
Public Function GetReferenceDataConstellationIdentifier ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringIdentifies the reference files used for combined signal demodulation. The value of this method must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True.

###### Return Value

Int32

##### Remarks

OfdmModAccReferenceDataConstellationIdentifier

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/2ffeb8d9-3e1b-4d2a-6135-f35b5a8f71f4.htm language=enus -->
## TOPIC 00046: rfmxwlandotnet/html/2ffeb8d9-3e1b-4d2a-6135-f35b5a8f71f4.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/2ffeb8d9-3e1b-4d2a-6135-f35b5a8f71f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/2ffeb8d9-3e1b-4d2a-6135-f35b5a8f71f4.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetErrorString Method

RFmxWlanMXGetErrorString Method

Converts the status code returned by an RFmxWLAN function into a string.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/30a7c6e6-74cc-686d-fb0c-073f8a5485a4.htm language=enus -->
## TOPIC 00047: rfmxwlandotnet/html/30a7c6e6-74cc-686d-fb0c-073f8a5485a4.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/30a7c6e6-74cc-686d-fb0c-073f8a5485a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/30a7c6e6-74cc-686d-fb0c-073f8a5485a4.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchUserDataConstellationTrace Method

RFmxWlanMXOfdmModAccResultsFetchUserDataConstellationTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUserDataConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] userDataConstellation
)
```

```text
Public Function FetchUserDataConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef userDataConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0""result::r1/user0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **userDataConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the demodulated QAM symbols from all the data-subcarriers in all of the OFDM symbols for each user.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/30eab6b8-306e-d864-0a59-1f875444f63c.htm language=enus -->
## TOPIC 00048: rfmxwlandotnet/html/30eab6b8-306e-d864-0a59-1f875444f63c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/30eab6b8-306e-d864-0a59-1f875444f63c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/30eab6b8-306e-d864-0a59-1f875444f63c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXExtension.GetWlanSignalConfiguration Method (RFmxInstrMX)

RFmxWlanMXExtensionGetWlanSignalConfiguration Method (RFmxInstrMX)

Creates a new default WLAN signal configuration if it doesn't exist; otherwise, it returns the
 existing default WLAN signal configuration.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxWlanMX GetWlanSignalConfiguration(
	this RFmxInstrMX instrSession
)
```

```text
<ExtensionAttribute>
Public Shared Function GetWlanSignalConfiguration ( 
	instrSession As RFmxInstrMX
) As RFmxWlanMX
```

###### Parameters

- **instrSession**
  - Type: RFmxInstrMXSpecifies an instr session.

###### Return Value

RFmxWlanMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxWlanMXExtension Class

GetWlanSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/312e8fdb-2f4f-c026-4b45-0e1bf8ffac8c.htm language=enus -->
## TOPIC 00049: rfmxwlandotnet/html/312e8fdb-2f4f-c026-4b45-0e1bf8ffac8c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/312e8fdb-2f4f-c026-4b45-0e1bf8ffac8c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/312e8fdb-2f4f-c026-4b45-0e1bf8ffac8c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccCommonClockSourceEnabled Enumeration

RFmxWlanMXOfdmModAccCommonClockSourceEnabled Enumeration

Specifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccCommonClockSourceEnabled
```

```text
Public Enumeration RFmxWlanMXOfdmModAccCommonClockSourceEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Specifies that the transmitter does not use a common reference clock. The OFDMModAcc measurement computes the symbol clock error and carrier frequency error independently. |
|  | True | 1 | Specifies that the transmitter uses a common reference clock. The OFDMModAcc measurement derives the symbol clock error from the configured center frequency and carrier frequency error. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/35b903fa-8abd-21bc-b39a-cf7665e3ed3c.htm language=enus -->
## TOPIC 00050: rfmxwlandotnet/html/35b903fa-8abd-21bc-b39a-cf7665e3ed3c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/35b903fa-8abd-21bc-b39a-cf7665e3ed3c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/35b903fa-8abd-21bc-b39a-cf7665e3ed3c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetPeakEvm802_11_2016Mean Method

RFmxWlanMXDsssModAccResultsGetPeakEvm802_11_2016Mean Method

Gets the peak EVM of the burst. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakEvm802_11_2016Mean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakEvm802_11_2016Mean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak EVM of the burst. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

DsssModAccResultsPeakEvm802_11_2016Mean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/365a592d-1898-d63c-c46f-7236044f24cc.htm language=enus -->
## TOPIC 00051: rfmxwlandotnet/html/365a592d-1898-d63c-c46f-7236044f24cc.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/365a592d-1898-d63c-c46f-7236044f24cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/365a592d-1898-d63c-c46f-7236044f24cc.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.ConfigureIQPowerEdgeTrigger Method

RFmxWlanMXConfigureIQPowerEdgeTrigger Method

On a MIMO session, configures the IQ Power edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureIQPowerEdgeTrigger(
	string selectorString,
	string iqPowerEdgeTriggerSource,
	RFmxWlanMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope,
	double iqPowerEdgeTriggerLevel,
	double triggerDelay,
	RFmxWlanMXTriggerMinimumQuietTimeMode triggerMinimumQuietTimeMode,
	double triggerMinimumQuietTimeDuration,
	RFmxWlanMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType,
	bool enableTrigger
)
```

```text
Public Function ConfigureIQPowerEdgeTrigger ( 
	selectorString As String,
	iqPowerEdgeTriggerSource As String,
	iqPowerEdgeTriggerSlope As RFmxWlanMXIQPowerEdgeTriggerSlope,
	iqPowerEdgeTriggerLevel As Double,
	triggerDelay As Double,
	triggerMinimumQuietTimeMode As RFmxWlanMXTriggerMinimumQuietTimeMode,
	triggerMinimumQuietTimeDuration As Double,
	iqPowerEdgeTriggerLevelType As RFmxWlanMXIQPowerEdgeTriggerLevelType,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **iqPowerEdgeTriggerSource**
  - Type: SystemStringSpecifies the channel from which the device monitors the trigger.This parameter is used only when you set the Trigger Type method to IQ Power Edge. The default value of this method is hardware dependent. To make a specific MIMO port as the trigger master, use the port specifier format port::(device_name)/(source_terminal). Example: “port::myrfsa1/0”
- **iqPowerEdgeTriggerSlope**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXIQPowerEdgeTriggerSlopeSpecifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify.
- **iqPowerEdgeTriggerLevel**
  - Type: SystemDouble Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative , or in dBm when it is set to Absolute .
- **triggerDelay**
  - Type: SystemDoubleSpecifies the trigger delay time. This value is expressed in seconds.
- **triggerMinimumQuietTimeMode**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXTriggerMinimumQuietTimeModeSpecifies whether the measurement computes the minimum quiet time used for triggering.
- **triggerMinimumQuietTimeDuration**
  - Type: SystemDouble Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(String, RFmxWlanMXIQPowerEdgeTriggerSlope) to Rising , the signal is quiet when it is below the trigger level.
- **iqPowerEdgeTriggerLevelType**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXIQPowerEdgeTriggerLevelType Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute . The value is expressed in dB when this parameter is set to Relative . The value is expressed in dBm when this parameter is set to Absolute .
- **enableTrigger**
  - Type: SystemBooleanSpecifies whether the trigger is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/366a6ec4-cc90-a9f6-3d12-7adf1024b2bd.htm language=enus -->
## TOPIC 00052: rfmxwlandotnet/html/366a6ec4-cc90-a9f6-3d12-7adf1024b2bd.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/366a6ec4-cc90-a9f6-3d12-7adf1024b2bd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/366a6ec4-cc90-a9f6-3d12-7adf1024b2bd.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchDataAveragePower Method

RFmxWlanMXOfdmModAccResultsFetchDataAveragePower Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDataAveragePower(
	string selectorString,
	double timeout,
	out double dataAveragePowerMean
)
```

```text
Public Function FetchDataAveragePower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef dataAveragePowerMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **dataAveragePowerMean**
  - Type: SystemDouble Upon return, contains the average power of the data field. This value is expressed in dBm. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the data average power results computed for each averaging count.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/3742e413-4677-02b5-7d3c-6ab25fdaef64.htm language=enus -->
## TOPIC 00053: rfmxwlandotnet/html/3742e413-4677-02b5-7d3c-6ab25fdaef64.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/3742e413-4677-02b5-7d3c-6ab25fdaef64.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/3742e413-4677-02b5-7d3c-6ab25fdaef64.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetPpduAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetPpduAveragePowerMean Method

Gets the average power of the PPDU. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPpduAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPpduAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the PPDU. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsPpduAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/379e96b9-69ba-af32-931e-79ef7997f597.htm language=enus -->
## TOPIC 00054: rfmxwlandotnet/html/379e96b9-69ba-af32-931e-79ef7997f597.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/379e96b9-69ba-af32-931e-79ef7997f597.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/379e96b9-69ba-af32-931e-79ef7997f597.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.SetAveragingEnabled Method

RFmxWlanMXDsssModAccConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for DSSSModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxWlanMXDsssModAccAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxWlanMXDsssModAccAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccAveragingEnabledSpecifies whether to enable averaging for DSSSModAcc measurement.

###### Return Value

Int32

##### Remarks

DsssModAccAveragingEnabled

False

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/379f69fe-74cf-0d54-1ed9-bc745f26b805.htm language=enus -->
## TOPIC 00055: rfmxwlandotnet/html/379f69fe-74cf-0d54-1ed9-bc745f26b805.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/379f69fe-74cf-0d54-1ed9-bc745f26b805.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/379f69fe-74cf-0d54-1ed9-bc745f26b805.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.ConfigureNumberOfFrequencySegmentsAndReceiveChains Method

RFmxWlanMXConfigureNumberOfFrequencySegmentsAndReceiveChains Method

Configures the number of frequency segments and receive chains.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfFrequencySegmentsAndReceiveChains(
	string selectorString,
	int numberOfFrequencySegments,
	int numberOfReceiveChains
)
```

```text
Public Function ConfigureNumberOfFrequencySegmentsAndReceiveChains ( 
	selectorString As String,
	numberOfFrequencySegments As Integer,
	numberOfReceiveChains As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **numberOfFrequencySegments**
  - Type: SystemInt32Specifies the number of frequency segments. The default value is 1.
- **numberOfReceiveChains**
  - Type: SystemInt32Specifies the number of receive chains. The default value is 1.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/380fd422-1a12-b8fb-72f5-c598bfe29b0b.htm language=enus -->
## TOPIC 00056: rfmxwlandotnet/html/380fd422-1a12-b8fb-72f5-c598bfe29b0b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/380fd422-1a12-b8fb-72f5-c598bfe29b0b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/380fd422-1a12-b8fb-72f5-c598bfe29b0b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetFrequencyErrorEstimationMethod Method

RFmxWlanMXOfdmModAccConfigurationSetFrequencyErrorEstimationMethod Method

Sets the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyErrorEstimationMethod(
	string selectorString,
	RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod value
)
```

```text
Public Function SetFrequencyErrorEstimationMethod ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccFrequencyErrorEstimationMethodSpecifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal.

###### Return Value

Int32

##### Remarks

OfdmModAccFrequencyErrorEstimationMethod

PreambleAndPilots

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/3e33c0f5-f638-6ca5-c1c9-29fc4b033465.htm language=enus -->
## TOPIC 00057: rfmxwlandotnet/html/3e33c0f5-f638-6ca5-c1c9-29fc4b033465.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/3e33c0f5-f638-6ca5-c1c9-29fc4b033465.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/3e33c0f5-f638-6ca5-c1c9-29fc4b033465.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccPayloadHeaderCrcStatus Enumeration

RFmxWlanMXDsssModAccPayloadHeaderCrcStatus Enumeration

IEEE Standard 802.11 2016

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXDsssModAccPayloadHeaderCrcStatus
```

```text
Public Enumeration RFmxWlanMXDsssModAccPayloadHeaderCrcStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 | Returns that the header CRC failed. |
|  | Pass | 1 | Returns that the header CRC passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/3ebb0128-b3e0-f14e-a1a2-df8c29fe8a20.htm language=enus -->
## TOPIC 00058: rfmxwlandotnet/html/3ebb0128-b3e0-f14e-a1a2-df8c29fe8a20.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/3ebb0128-b3e0-f14e-a1a2-df8c29fe8a20.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/3ebb0128-b3e0-f14e-a1a2-df8c29fe8a20.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.FetchDecodedHeaderBitsTrace Method

RFmxWlanMXDsssModAccResultsFetchDecodedHeaderBitsTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDecodedHeaderBitsTrace(
	string selectorString,
	double timeout,
	ref int[] decodedHeaderBits
)
```

```text
Public Function FetchDecodedHeaderBitsTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef decodedHeaderBits As Integer()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **decodedHeaderBits**
  - Type: SystemInt32 Upon return, contains an array of bits in the Header field.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/3eece562-209e-0ba7-a919-c56e6d23da46.htm language=enus -->
## TOPIC 00059: rfmxwlandotnet/html/3eece562-209e-0ba7-a919-c56e6d23da46.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/3eece562-209e-0ba7-a919-c56e6d23da46.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/3eece562-209e-0ba7-a919-c56e6d23da46.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHTStfPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetHTStfPeakPowerMaximum Method

Gets the peak power of the HT-STF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHTStfPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetHTStfPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the HT-STF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHTStfPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/3ff023d0-121c-04dd-2ea3-799cc59748d6.htm language=enus -->
## TOPIC 00060: rfmxwlandotnet/html/3ff023d0-121c-04dd-2ea3-799cc59748d6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/3ff023d0-121c-04dd-2ea3-799cc59748d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/3ff023d0-121c-04dd-2ea3-799cc59748d6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.FetchLowerOffsetPowerArray Method

RFmxWlanMXSemResultsFetchLowerOffsetPowerArray Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLowerOffsetPowerArray(
	string selectorString,
	double timeout,
	ref double[] totalAbsolutePower,
	ref double[] totalRelativePower,
	ref double[] peakAbsolutePower,
	ref double[] peakFrequency,
	ref double[] peakRelativePower
)
```

```text
Public Function FetchLowerOffsetPowerArray ( 
	selectorString As String,
	timeout As Double,
	ByRef totalAbsolutePower As Double(),
	ByRef totalRelativePower As Double(),
	ByRef peakAbsolutePower As Double(),
	ByRef peakFrequency As Double(),
	ByRef peakRelativePower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **totalAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of average powers of the lower offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm.
- **totalRelativePower**
  - Type: SystemDouble Upon return, contains an array of average powers of the lower offsets relative to the peak power of the carrier channel. This value is expressed in dB.
- **peakAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of peak powers of the lower offsets. This value is expressed in dBm.
- **peakFrequency**
  - Type: SystemDouble Upon return, contains an array of frequencies at which the peak power occurs in the lower offsets. This value is expressed in Hz.
- **peakRelativePower**
  - Type: SystemDouble Upon return, contains an array of peak powers of the lower offsets, relative to the peak power of the carrier channel. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/442b057d-a970-5b20-3a4d-8ffe392de1ee.htm language=enus -->
## TOPIC 00061: rfmxwlandotnet/html/442b057d-a970-5b20-3a4d-8ffe392de1ee.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/442b057d-a970-5b20-3a4d-8ffe392de1ee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/442b057d-a970-5b20-3a4d-8ffe392de1ee.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.DeleteSignalConfiguration Method

RFmxWlanMXDeleteSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/448af882-4033-583f-ecf0-865f2e5c4251.htm language=enus -->
## TOPIC 00062: rfmxwlandotnet/html/448af882-4033-583f-ecf0-865f2e5c4251.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/448af882-4033-583f-ecf0-865f2e5c4251.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/448af882-4033-583f-ecf0-865f2e5c4251.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.CloneSignalConfiguration Method

RFmxWlanMXCloneSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int CloneSignalConfiguration(
	string newSignalName,
	out RFmxWlanMX signalConfiguration
)
```

```text
Public Function CloneSignalConfiguration ( 
	newSignalName As String,
	<OutAttribute> ByRef signalConfiguration As RFmxWlanMX
) As Integer
```

###### Parameters

- **newSignalName**
  - Type: SystemString Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName""NewSigName"
- **signalConfiguration**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXUpon return, contains a new wlan signal instance.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/44aa223b-a4e3-8c55-9f00-d35034832c89.htm language=enus -->
## TOPIC 00063: rfmxwlandotnet/html/44aa223b-a4e3-8c55-9f00-d35034832c89.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/44aa223b-a4e3-8c55-9f00-d35034832c89.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/44aa223b-a4e3-8c55-9f00-d35034832c89.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.ConfigureMeasurementLength Method

RFmxWlanMXDsssModAccConfigurationConfigureMeasurementLength Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementLength(
	string selectorString,
	int measurementOffset,
	int maximumMeasurementLength
)
```

```text
Public Function ConfigureMeasurementLength ( 
	selectorString As String,
	measurementOffset As Integer,
	maximumMeasurementLength As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementOffset**
  - Type: SystemInt32Specifies the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips.
- **maximumMeasurementLength**
  - Type: SystemInt32Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/44db3081-e8ca-488e-affe-eb6f00a9309f.htm language=enus -->
## TOPIC 00064: rfmxwlandotnet/html/44db3081-e8ca-488e-affe-eb6f00a9309f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/44db3081-e8ca-488e-affe-eb6f00a9309f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/44db3081-e8ca-488e-affe-eb6f00a9309f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.ConfigureAcquisitionLength Method

RFmxWlanMXOfdmModAccConfigurationConfigureAcquisitionLength Method

acquisitionLength

acquisitionLengthMode

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAcquisitionLength(
	string selectorString,
	RFmxWlanMXOfdmModAccAcquisitionLengthMode acquisitionLengthMode,
	double acquisitionLength
)
```

```text
Public Function ConfigureAcquisitionLength ( 
	selectorString As String,
	acquisitionLengthMode As RFmxWlanMXOfdmModAccAcquisitionLengthMode,
	acquisitionLength As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **acquisitionLengthMode**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccAcquisitionLengthModeSpecifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc methods.
- **acquisitionLength**
  - Type: SystemDouble Specifies the length of the waveform to be acquired for the OFDMModAcc measurement when you set the acquisitionLengthMode parameter to Manual . This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/45996e33-b414-0708-2f8a-3bdcd965e926.htm language=enus -->
## TOPIC 00065: rfmxwlandotnet/html/45996e33-b414-0708-2f8a-3bdcd965e926.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/45996e33-b414-0708-2f8a-3bdcd965e926.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/45996e33-b414-0708-2f8a-3bdcd965e926.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchUnusedToneErrorMarginPerRU Method

RFmxWlanMXOfdmModAccResultsFetchUnusedToneErrorMarginPerRU Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUnusedToneErrorMarginPerRU(
	string selectorString,
	double timeout,
	ref double[] unusedToneErrorMarginPerRU
)
```

```text
Public Function FetchUnusedToneErrorMarginPerRU ( 
	selectorString As String,
	timeout As Double,
	ByRef unusedToneErrorMarginPerRU As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **unusedToneErrorMarginPerRU**
  - Type: SystemDouble Upon return, contains an array of unused tone error margin per RU, which is the difference between the unused tone error mask and the unused tone error for each RU. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/45ababa0-e997-490e-d128-b3fd45775ad1.htm language=enus -->
## TOPIC 00066: rfmxwlandotnet/html/45ababa0-e997-490e-d128-b3fd45775ad1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/45ababa0-e997-490e-d128-b3fd45775ad1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/45ababa0-e997-490e-d128-b3fd45775ad1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetIQOriginOffsetCorrectionEnabled Method

RFmxWlanMXDsssModAccConfigurationGetIQOriginOffsetCorrectionEnabled Method

Gets whether to enable I/Q origin offset correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOriginOffsetCorrectionEnabled(
	string selectorString,
	out RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled value
)
```

```text
Public Function GetIQOriginOffsetCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabledUpon return, contains whether to enable I/Q origin offset correction.

###### Return Value

Int32

##### Remarks

DsssModAccIQOriginOffsetCorrectionEnabled

True

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/45ee18e1-7c93-aebb-a959-856ff171a9ab.htm language=enus -->
## TOPIC 00067: rfmxwlandotnet/html/45ee18e1-7c93-aebb-a959-856ff171a9ab.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/45ee18e1-7c93-aebb-a959-856ff171a9ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/45ee18e1-7c93-aebb-a959-856ff171a9ab.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.WlanMX Namespace

NationalInstruments.RFmx.WlanMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxWlanMX | Defines a root class which is used to identify and control WLAN signal configuration. |
|  | RFmxWlanMXConstants | Specifies constants for I/O terminals. |
|  | RFmxWlanMXDsssModAcc | Represents the DSSSModAcc measurement. |
|  | RFmxWlanMXDsssModAccConfiguration | Provides methods to configure the DSSSModAcc measurement. |
|  | RFmxWlanMXDsssModAccResults | Provides methods to fetch and read the DSSSModAcc measurement results. |
|  | RFmxWlanMXOfdmModAcc | Represents the OFDMModAcc measurement. |
|  | RFmxWlanMXOfdmModAccConfiguration | Provides methods to configure the OFDMModAcc measurement. |
|  | RFmxWlanMXOfdmModAccResults | Provides methods to fetch and read the OFDMModAcc measurement results. |
|  | RFmxWlanMXPowerRamp | Represents the PowerRamp measurement. |
|  | RFmxWlanMXPowerRampConfiguration | Provides methods to configure the PowerRamp measurement. |
|  | RFmxWlanMXPowerRampResults | Provides methods to fetch and read the PowerRamp measurement results. |
|  | RFmxWlanMXSem | Represents the SEM measurement. |
|  | RFmxWlanMXSemConfiguration | Provides methods to configure the SEM measurement. |
|  | RFmxWlanMXSemResults | Provides methods to fetch and read the SEM measurement results. |
|  | RFmxWlanMXTxp | Represents the TXP measurement. |
|  | RFmxWlanMXTxpConfiguration | Provides methods to configure the TXP measurement. |
|  | RFmxWlanMXTxpResults | Provides methods to fetch and read the TXP measurement results. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | RFmxWlanMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to DigitalEdge . |
|  | RFmxWlanMXDsssModAccAcquisitionLengthMode | Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. |
|  | RFmxWlanMXDsssModAccAveragingEnabled | Specifies whether to enable averaging for DSSSModAcc measurement. |
|  | RFmxWlanMXDsssModAccBurstStartDetectionEnabled | Specifies whether the measurement detects the rising edge of a burst in the acquired waveform. |
|  | RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled | Specifies whether to enable chip clock error correction. |
|  | RFmxWlanMXDsssModAccDataDecodingEnabled | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
|  | RFmxWlanMXDsssModAccDataModulationFormat | Returns the data modulation format results of the analyzed waveform. |
|  | RFmxWlanMXDsssModAccEqualizationEnabled | Specifies whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |
|  | RFmxWlanMXDsssModAccEvmUnit | Specifies the unit for the EVM results. |
|  | RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled | Specifies whether to enable frequency error correction. |
|  | RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled | Specifies whether to enable I/Q origin offset correction. |
|  | RFmxWlanMXDsssModAccPayloadHeaderCrcStatus | Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016 . |
|  | RFmxWlanMXDsssModAccPowerMeasurementEnabled | Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU. |
|  | RFmxWlanMXDsssModAccPreambleType | Returns the detected preamble type of the acquired burst. |
|  | RFmxWlanMXDsssModAccPsduCrcStatus | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
|  | RFmxWlanMXDsssModAccPsduCrcStaus | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
|  | RFmxWlanMXDsssModAccPulseShapingFilterType | Specifies the type of pulse shaping filter used at the transmitter. This method is ignored when you set the SetEqualizationEnabled(String, RFmxWlanMXDsssModAccEqualizationEnabled) method to True . |
|  | RFmxWlanMXDsssModAccSpectrumInverted | Specifies whether the spectrum of the measured signal is inverted. |
|  | RFmxWlanMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to IQPowerEdge . |
|  | RFmxWlanMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
|  | RFmxWlanMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | RFmxWlanMXMeasurementTypes | Specifies the type of measurement. |
|  | RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled | Enables auto detection of phase rotation coefficients. |
|  | RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled | Specifies whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement. |
|  | RFmxWlanMXOfdmDcmEnabled | Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. |
|  | RFmxWlanMXOfdmEhtSigCompressionEnabled | Enables EHT-SIG compression. This is applicable only for 802.11be MU PPDU signals. |
|  | RFmxWlanMXOfdmFecCodingType | Specifies the type of forward error correction (FEC) coding used. |
|  | RFmxWlanMXOfdmFrequencyBand | Specifies the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |
|  | RFmxWlanMXOfdmGuardIntervalType | Specifies the size of the guard interval of OFDM symbols. |
|  | RFmxWlanMXOfdmHeaderDecodingEnabled | Specifies whether to enable the decoding of the header fields in the PPDU. |
|  | RFmxWlanMXOfdmLtfSize | Specifies the LTF symbol size. This method is applicable only for 802.11ax and 802.11be signals. For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False. |
|  | RFmxWlanMXOfdmModAccAcquisitionLengthMode | Specifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc properties. |
|  | RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled | Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol. |
|  | RFmxWlanMXOfdmModAccAutoLevelAllowOverflow | Specifies whether the AutoLevel(String, Double) function should search for the optimum reference levels while allowing ADC overflow. |
|  | RFmxWlanMXOfdmModAccAveragingEnabled | Specifies whether to enable averaging for OFDMModAcc measurements. |
|  | RFmxWlanMXOfdmModAccAveragingType | Specifies the averaging type for the OFDMModAcc measurement. |
|  | RFmxWlanMXOfdmModAccBurstStartDetectionEnabled | Specifies whether the measurement detects a rising edge of a burst in the acquired waveform. |
|  | RFmxWlanMXOfdmModAccCalibrationDataValid | Returns whether the calibration data is valid. |
|  | RFmxWlanMXOfdmModAccChannelEstimationInterpolationType | Specifies the interpolation type and/or smoothing type used on the channel estimates. |
|  | RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled | Specifies whether to use the legacy channel estimation field for combining with the reference channel frequency response. |
|  | RFmxWlanMXOfdmModAccChannelEstimationType | Specifies the fields in the PPDU used to estimate the channel frequency response. |
|  | RFmxWlanMXOfdmModAccChannelMatrixPowerEnabled | Specifies whether the channel frequency response matrix power measurements are enabled. This enables cross-power measurements for MIMO signals and user-power measurements for MU signals. |
|  | RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled | Specifies whether to enable demodulation of the signal that is formed by combining signals from multiple transmitter chains. |
|  | RFmxWlanMXOfdmModAccCommonClockSourceEnabled | Specifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock. |
|  | RFmxWlanMXOfdmModAccCommonPilotErrorScalingReference | Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE. |
|  | RFmxWlanMXOfdmModAccDataDecodingEnabled | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
|  | RFmxWlanMXOfdmModAccDcmEnabled | Returns whether DCM is enabled for a specified user. |
|  | RFmxWlanMXOfdmModAccEhtSigCrcStatus | Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform. |
|  | RFmxWlanMXOfdmModAccEvmReferenceDataSymbolsMode | Specifies whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation. |
|  | RFmxWlanMXOfdmModAccEvmUnit | Specifies the unit for EVM results. |
|  | RFmxWlanMXOfdmModAccFecCodingType | Returns the FEC coding type for a specified user. |
|  | RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod | Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal. |
|  | RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled | Specifies whether to enable I/Q gain imbalance correction. |
|  | RFmxWlanMXOfdmModAccIQImpairmentsEstimationEnabled | Specifies whether to enable the estimation of I/Q gain imbalance, I/Q quadrature error, and I/Q timing skew impairments. |
|  | RFmxWlanMXOfdmModAccIQImpairmentsModel | Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. |
|  | RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled | Specifies whether to estimate I/Q impairments independently for each subcarrier. |
|  | RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled | Specifies whether to enable I/Q quadrature error correction. |
|  | RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled | Specifies whether to enable I/Q timing skew correction. |
|  | RFmxWlanMXOfdmModAccLSigParityCheckStatus | Returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms. |
|  | RFmxWlanMXOfdmModAccMeasurementMode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement. |
|  | RFmxWlanMXOfdmModAccNoiseCompensationApplied | Returns whether the noise compensation is applied. |
|  | RFmxWlanMXOfdmModAccNoiseCompensationEnabled | Specifies whether the contribution of the instrument noise is compensated for EVM computation. |
|  | RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled | Specifies whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |
|  | RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled | Specifies whether to optimize the analyzer's dynamic range for the EVM measurement. |
|  | RFmxWlanMXOfdmModAccPhaseRotationCoefficient1 | Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D6.0. |
|  | RFmxWlanMXOfdmModAccPhaseRotationCoefficient2 | Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0. |
|  | RFmxWlanMXOfdmModAccPhaseRotationCoefficient3 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D6.0. |
|  | RFmxWlanMXOfdmModAccPhaseTrackingEnabled | Specifies whether to enable pilot-based common phase error correction per OFDM data symbol. |
|  | RFmxWlanMXOfdmModAccPowerMeasurementEnabled | Specifies whether power measurements are performed. |
|  | RFmxWlanMXOfdmModAccPsduCrcStatus | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
|  | RFmxWlanMXOfdmModAccSigBCrcStatus | Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. |
|  | RFmxWlanMXOfdmModAccSigCrcStatus | Returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. |
|  | RFmxWlanMXOfdmModAccSpectrumInverted | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
|  | RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled | Specifies whether to enable symbol clock error correction. |
|  | RFmxWlanMXOfdmModAccUnusedToneErrorMaskReference | Specifies the reference used to create the unused tone error mask for the 802.11ax or 802.11be TB PPDU signals. |
|  | RFmxWlanMXOfdmModAccUSigCrcStatus | Returns whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be waveform. |
|  | RFmxWlanMXOfdmModAccVectorAveragingPhaseAlignmentEnabled | Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXOfdmModAccAveragingType method to Vector . You can set this method to False when there is no phase offset between the acquired I/Q data of all averaging counts. |
|  | RFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabled | Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXOfdmModAccAveragingType method to Vector . You can set this method to False when there is no time offset between the acquired I/Q data of all averaging counts. |
|  | RFmxWlanMXOfdmMUMimoLtfModeEnabled | Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. |
|  | RFmxWlanMXOfdmPhaseRotationCoefficient1 | Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D6.0 . |
|  | RFmxWlanMXOfdmPhaseRotationCoefficient2 | Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0 . |
|  | RFmxWlanMXOfdmPhaseRotationCoefficient3 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D6.0 . |
|  | RFmxWlanMXOfdmPpduType | Specifies the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(String, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . |
|  | RFmxWlanMXOfdmPreamblePuncturingEnabled | Specifies whether the 802.11ax MU PPDU or the 802.11be MU PPDU signal is preamble punctured. |
|  | RFmxWlanMXOfdmStbcEnabled | Specifies whether space-time block coding is enabled. This method is applicable only for 802.11ax TB PPDU. |
|  | RFmxWlanMXOfdmTransmitPowerClass | Specifies the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(String, RFmxWlanMXStandard) method to Standard802_11p . |
|  | RFmxWlanMXPowerRampAveragingEnabled | Specifies if averaging is enabled for PowerRamp measurements. |
|  | RFmxWlanMXPropertyId | Specifies all the attribute identifiers. |
|  | RFmxWlanMXSemAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | RFmxWlanMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |
|  | RFmxWlanMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
|  | RFmxWlanMXSemLowerOffsetMeasurementStatus | Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. |
|  | RFmxWlanMXSemMaskType | Specifies whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
|  | RFmxWlanMXSemMeasurementStatus | Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. |
|  | RFmxWlanMXSemOffsetSideband | Specifies whether the offset segment is present on one side or on both sides of the carrier. |
|  | RFmxWlanMXSemSpanAuto | Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
|  | RFmxWlanMXSemSweepTimeAuto | Specifies whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
|  | RFmxWlanMXSemUpperOffsetMeasurementStatus | Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment. |
|  | RFmxWlanMXStandard | Specifies the signal under analysis as defined in IEEE Standard 802.11 . |
|  | RFmxWlanMXTriggerGateEnabled | Enables time-domain gating of the acquired signal for SEM measurement. |
|  | RFmxWlanMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
|  | RFmxWlanMXTriggerType | Specifies the trigger type. |
|  | RFmxWlanMXTxpAveragingEnabled | Specifies whether to enable averaging for the TXP measurement. |
|  | RFmxWlanMXTxpBurstDetectionEnabled | Specifies whether the measurement detects the start and the end of a WLAN packet automatically. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4648a8df-9c5a-b313-54c7-72b188ccb546.htm language=enus -->
## TOPIC 00068: rfmxwlandotnet/html/4648a8df-9c5a-b313-54c7-72b188ccb546.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4648a8df-9c5a-b313-54c7-72b188ccb546.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4648a8df-9c5a-b313-54c7-72b188ccb546.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetPeakEvm802_11_2007Mean Method

RFmxWlanMXDsssModAccResultsGetPeakEvm802_11_2007Mean Method

Gets the peak EVM of the burst. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakEvm802_11_2007Mean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakEvm802_11_2007Mean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak EVM of the burst. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

DsssModAccResultsPeakEvm802_11_2007Mean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/467265c3-a344-e0ed-91bd-d7a7fc4ab74b.htm language=enus -->
## TOPIC 00069: rfmxwlandotnet/html/467265c3-a344-e0ed-91bd-d7a7fc4ab74b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/467265c3-a344-e0ed-91bd-d7a7fc4ab74b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/467265c3-a344-e0ed-91bd-d7a7fc4ab74b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.ResetAttribute Method

RFmxWlanMXResetAttribute Method

Resets the attribute to its default value.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ResetAttribute(
	string selectorString,
	RFmxWlanMXPropertyId attributeId
)
```

```text
Public Function ResetAttribute ( 
	selectorString As String,
	attributeId As RFmxWlanMXPropertyId
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the selector string for the method being reset. Refer to the Using a Selector String (.NET) topic in the NI-RFmx WLAN Help for more information about configuring the selector string.
- **attributeId**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXPropertyIdSpecifies an attribute identifier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4681f573-b4a9-8ca9-f1dd-5739ee387330.htm language=enus -->
## TOPIC 00070: rfmxwlandotnet/html/4681f573-b4a9-8ca9-f1dd-5739ee387330.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4681f573-b4a9-8ca9-f1dd-5739ee387330.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4681f573-b4a9-8ca9-f1dd-5739ee387330.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchCrossPower Method

RFmxWlanMXOfdmModAccResultsFetchCrossPower Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCrossPower(
	string selectorString,
	double timeout,
	out double crossPowerMean
)
```

```text
Public Function FetchCrossPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef crossPowerMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **crossPowerMean**
  - Type: SystemDouble Upon return, contains the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the cross power results computed for each averaging count. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/46d20336-d1a0-08d4-3848-95168147589f.htm language=enus -->
## TOPIC 00071: rfmxwlandotnet/html/46d20336-d1a0-08d4-3848-95168147589f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/46d20336-d1a0-08d4-3848-95168147589f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/46d20336-d1a0-08d4-3848-95168147589f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetLimitedConfigurationChange Method

RFmxWlanMXGetLimitedConfigurationChange Method

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLimitedConfigurationChange(
	string selectorString,
	out RFmxWlanMXLimitedConfigurationChange value
)
```

```text
Public Function GetLimitedConfigurationChange ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXLimitedConfigurationChangeUpon return, contains the set of properties that are considered by RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

LimitedConfigurationChange

Disabled

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/46e58c51-aa75-596b-9351-8024ea2ed017.htm language=enus -->
## TOPIC 00072: rfmxwlandotnet/html/46e58c51-aa75-596b-9351-8024ea2ed017.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/46e58c51-aa75-596b-9351-8024ea2ed017.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/46e58c51-aa75-596b-9351-8024ea2ed017.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmScramblerSeed Method

RFmxWlanMXSetOfdmScramblerSeed Method

SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmScramblerSeed(
	string selectorString,
	int value
)
```

```text
Public Function SetOfdmScramblerSeed ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the user number. Example: "user0". You can use the BuildUserString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the scrambler seed for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True.

###### Return Value

Int32

##### Remarks

OfdmScramblerSeed

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/47337b3d-0232-9fe3-0b92-be3c163b347f.htm language=enus -->
## TOPIC 00073: rfmxwlandotnet/html/47337b3d-0232-9fe3-0b92-be3c163b347f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/47337b3d-0232-9fe3-0b92-be3c163b347f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/47337b3d-0232-9fe3-0b92-be3c163b347f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.BuildOffsetString Method

RFmxWlanMXBuildOffsetString Method

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **offsetNumber**
  - Type: SystemInt32 Specifies the offset number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/475bbf45-0a5e-7526-80fd-6077748a9ff9.htm language=enus -->
## TOPIC 00074: rfmxwlandotnet/html/475bbf45-0a5e-7526-80fd-6077748a9ff9.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/475bbf45-0a5e-7526-80fd-6077748a9ff9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/475bbf45-0a5e-7526-80fd-6077748a9ff9.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmTransmitPowerClass Method

RFmxWlanMXSetOfdmTransmitPowerClass Method

IEEE Standard 802.11–2016

SetStandard(String, RFmxWlanMXStandard)

Standard802_11p

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmTransmitPowerClass(
	string selectorString,
	RFmxWlanMXOfdmTransmitPowerClass value
)
```

```text
Public Function SetOfdmTransmitPowerClass ( 
	selectorString As String,
	value As RFmxWlanMXOfdmTransmitPowerClass
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmTransmitPowerClass Specifies the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(String, RFmxWlanMXStandard) method to Standard802_11p .

###### Return Value

Int32

##### Remarks

OfdmTransmitPowerClass

A

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/47830ac7-5f78-f684-d41c-6a9c51073981.htm language=enus -->
## TOPIC 00075: rfmxwlandotnet/html/47830ac7-5f78-f684-d41c-6a9c51073981.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/47830ac7-5f78-f684-d41c-6a9c51073981.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/47830ac7-5f78-f684-d41c-6a9c51073981.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPropertyId Enumeration

RFmxWlanMXPropertyId Enumeration

Specifies all the attribute identifiers.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXPropertyId
```

```text
Public Enumeration RFmxWlanMXPropertyId
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SelectedPorts | 10489853 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | CenterFrequency | 10485761 | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. On a MIMO session, use segment(n) along with a named or default signal instance as the selector string to configure this method. Refer to the Selector Strings topic for information about the string syntax for named signals. |
|  | ReferenceLevel | 10485762 | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals. |
|  | ExternalAttenuation | 10485763 | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help . |
|  | ReferenceLevelHeadroom | 10489852 | Specifies the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
|  | TriggerType | 10485764 | Specifies the trigger type. |
|  | DigitalEdgeTriggerSource | 10485765 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to DigitalEdge . On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is configured to "segment0/chain0" and is considered as the master port. |
|  | DigitalEdgeTriggerEdge | 10485766 | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to DigitalEdge . |
|  | IQPowerEdgeTriggerSource | 10485767 | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to IQPowerEdge . On a MIMO session, configures the IQ Power edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port. |
|  | IQPowerEdgeTriggerLevel | 10485768 | Specifies the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxWlanMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute . |
|  | IQPowerEdgeTriggerLevelType | 10489855 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to IQPowerEdge . |
|  | IQPowerEdgeTriggerSlope | 10485769 | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
|  | TriggerDelay | 10485770 | Specifies the trigger delay time. This value is expressed in seconds. |
|  | TriggerMinimumQuietTimeMode | 10485771 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
|  | TriggerMinimumQuietTimeDuration | 10485772 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | TriggerGateEnabled | 10485802 | Enables time-domain gating of the acquired signal for SEM measurement. |
|  | TriggerGateLength | 10485803 | Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the SetTriggerGateEnabled(String, RFmxWlanMXTriggerGateEnabled) method to True . |
|  | Standard | 10485773 | Specifies the signal under analysis as defined in IEEE Standard 802.11 . |
|  | ChannelBandwidth | 10485774 | Specifies the channel spacing as defined under section 3.1 of IEEE Standard 802.11–2016 (pp. 130) . This value is specified in Hz. |
|  | NumberOfFrequencySegments | 10485775 | Specifies the number of frequency segments for 802.11ac and 802.11ax signals. |
|  | NumberOfReceiveChains | 10485776 | Specifies the number of receive chains for OFDM standards. |
|  | OfdmFrequencySegmentIndex | 10485780 | Specifies the frequency segment index to be analyzed in an 80+80 MHz 802.11ax signal. You must set this method to either of the valid values when you want to analyze one of the two segments. |
|  | OfdmTransmitPowerClass | 10485781 | Specifies the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(String, RFmxWlanMXStandard) method to Standard802_11p . |
|  | OfdmFrequencyBand | 10485782 | Specifies the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |
|  | OfdmAutoPpduTypeDetectionEnabled | 10485799 | Specifies whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement. |
|  | OfdmPpduType | 10485783 | Specifies the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(String, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . |
|  | OfdmHeaderDecodingEnabled | 10485800 | Specifies whether to enable the decoding of the header fields in the PPDU. |
|  | OfdmEhtSigCompressionEnabled | 10485818 | Specifies whether to enable EHT-SIG compression. This method is applicable only for 802.11be MU PPDU signals. |
|  | OfdmNumberOfUsers | 10485784 | Specifies the number of users in a multi-user (MU) PPDU. |
|  | OfdmMcsIndex | 10485785 | Specifies the modulation and coding scheme (MCS) index or the data rate when you set the SetOfdmHeaderDecodingEnabled(String, RFmxWlanMXOfdmHeaderDecodingEnabled) method to False . |
|  | OfdmScramblerSeed | 10485821 | Specifies the scrambler seed for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
|  | OfdmFecCodingType | 10485810 | Specifies the type of forward error correction (FEC) coding used. |
|  | OfdmRUSize | 10485786 | Specifies the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax and 802.11be signals. |
|  | OfdmRUOffsetMruIndex | 10485787 | Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0 . |
|  | OfdmGuardIntervalType | 10485788 | Specifies the size of the guard interval of OFDM symbols. |
|  | OfdmLtfSize | 10485789 | Specifies the LTF symbol size. This method is applicable only for 802.11ax and 802.11be signals. For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False. |
|  | OfdmPreFecPaddingFactor | 10485811 | Specifies the pre-FEC padding factor used in 802.11ax TB PPDU and 802.11be TB PPDU for decoding PLCP service data unit (PSDU) bits. |
|  | OfdmLdpcExtraSymbolSegment | 10485812 | Specifies the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU and 802.11be TB PPDU. |
|  | OfdmPEDisambiguity | 10485809 | Specifies the packet extension disambiguity information. |
|  | OfdmStbcEnabled | 10485813 | Specifies whether space-time block coding is enabled. This method is applicable only for 802.11ax TB PPDU. |
|  | OfdmNumberOfSpaceTimeStreams | 10485790 | Specifies the number of space time streams. |
|  | OfdmSpaceTimeStreamOffset | 10485791 | Specifies the space time stream offset. |
|  | OfdmNumberOfHESigBSymbols | 10485792 | Specifies the number of HE-SIG-B symbols. |
|  | OfdmNumberOfEhtSigSymbols | 10485819 | Specifies the number of EHT-SIG symbols. This method is applicable only for 802.11be MU PPDU signals. |
|  | OfdmDcmEnabled | 10485793 | Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. |
|  | OfdmNumberOfLtfSymbols | 10485794 | Specifies the number of HE-LTF or EHT-LTF symbols in the 802.11ax TB PPDU or 802.11be TB PPDU, respectively. |
|  | OfdmMUMimoLtfModeEnabled | 10485801 | Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. |
|  | OfdmPreamblePuncturingEnabled | 10485807 | Specifies whether the 802.11ax MU PPDU or the 802.11be MU PPDU signal is preamble punctured. |
|  | OfdmPreamblePuncturingBitmap | 10485808 | Specifies the punctured 20 MHz sub-channels in the 802.11ax MU PPDU or the 802.11be MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits. |
|  | OfdmAutoPhaseRotationDetectionEnabled | 10485820 | Specifies whether to enable auto detection of phase rotation coefficients. |
|  | OfdmPhaseRotationCoefficient1 | 10485815 | Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D6.0 . |
|  | OfdmPhaseRotationCoefficient2 | 10485816 | Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0 . |
|  | OfdmPhaseRotationCoefficient3 | 10485817 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D6.0 . |
|  | DetectedStandard | 10485777 | Returns the standard detected by the AutoDetectSignal(String, Double) function. |
|  | DetectedChannelBandwidth | 10485778 | Returns the channel bandwidth detected by the AutoDetectSignal(String, Double) . The value is expressed in Hz. |
|  | DetectedBurstLength | 10485779 | Returns the duration of the packet detected by the AutoDetectSignal(String, Double) function. The value is expressed in seconds. |
|  | DsssModAccMeasurementEnabled | 10498058 | Specifies whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016 . |
|  | DsssModAccAcquisitionLengthMode | 10498059 | Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. |
|  | DsssModAccAcquisitionLength | 10498060 | Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the SetAcquisitionLengthMode(String, RFmxWlanMXDsssModAccAcquisitionLengthMode) method to Manual . This value is expressed in seconds. |
|  | DsssModAccMeasurementOffset | 10498061 | Specifies the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips. |
|  | DsssModAccMaximumMeasurementLength | 10498062 | Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. |
|  | DsssModAccPulseShapingFilterType | 10498063 | Specifies the type of pulse shaping filter used at the transmitter. This method is ignored when you set the SetEqualizationEnabled(String, RFmxWlanMXDsssModAccEqualizationEnabled) method to True . |
|  | DsssModAccPulseShapingFilterParameter | 10498064 | Specifies the value of the filter roll-off when you set the Pulse Shaping Filter Type method to Raised Cosine or Root Raised Cosine. This method is ignored if you set the Pulse Shaping Filter Type method to Rectangular. |
|  | DsssModAccEqualizationEnabled | 10498065 | Specifies whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |
|  | DsssModAccBurstStartDetectionEnabled | 10498170 | Specifies whether the measurement detects the rising edge of a burst in the acquired waveform. |
|  | DsssModAccEvmUnit | 10498066 | Specifies the unit for the EVM results. |
|  | DsssModAccPowerMeasurementEnabled | 10498067 | Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU. |
|  | DsssModAccPowerNumberOfCustomGates | 10498068 | Specifies the number of custom gates used for power measurement. |
|  | DsssModAccPowerCustomGateStartTime | 10498069 | Specifies the start time of the custom power gate. This value is expressed in seconds. |
|  | DsssModAccPowerCustomGateStopTime | 10498070 | Specifies the stop time for the custom power gate. This value is expressed in seconds. |
|  | DsssModAccFrequencyErrorCorrectionEnabled | 10498092 | Specifies whether to enable frequency error correction. |
|  | DsssModAccChipClockErrorCorrectionEnabled | 10498093 | Specifies whether to enable chip clock error correction. |
|  | DsssModAccIQOriginOffsetCorrectionEnabled | 10498094 | Specifies whether to enable I/Q origin offset correction. |
|  | DsssModAccSpectrumInverted | 10498171 | Specifies whether the spectrum of the measured signal is inverted. |
|  | DsssModAccDataDecodingEnabled | 10498172 | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
|  | DsssModAccAveragingEnabled | 10498095 | Specifies whether to enable averaging for DSSSModAcc measurement. |
|  | DsssModAccAveragingCount | 10498096 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXDsssModAccAveragingEnabled) method to True . |
|  | DsssModAccAllTracesEnabled | 10498097 | Specifies whether to enable all the traces computed by DSSSModAcc measurement. |
|  | DsssModAccNumberOfAnalysisThreads | 10498161 | Specifies the maximum number of threads used for parallelism for DSSSModAcc measurement. |
|  | DsssModAccResultsRmsEvmMean | 10498098 | Returns the RMS EVM of the burst. This value is expressed as a percentage or in dB. |
|  | DsssModAccResultsPeakEvm802_11_2016Mean | 10498108 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
|  | DsssModAccResultsPeakEvm802_11_2016Maximum | 10498109 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
|  | DsssModAccResultsPeakEvm802_11_2007Mean | 10498101 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
|  | DsssModAccResultsPeakEvm802_11_2007Maximum | 10498102 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
|  | DsssModAccResultsPeakEvm802_11_1999Mean | 10498099 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
|  | DsssModAccResultsPeakEvm802_11_1999Maximum | 10498100 | Returns the peak EVM of the burst. This value is expressed as percentage or in dB. |
|  | DsssModAccResultsNumberOfChipsUsed | 10498125 | Returns the number of chips used for the DSSSModAcc measurement. |
|  | DsssModAccResultsFrequencyErrorMean | 10498126 | Returns the carrier frequency error of the transmitter. This value is expressed in Hz. |
|  | DsssModAccResultsChipClockErrorMean | 10498130 | Returns the chip clock error of the transmitter. This value is expressed in parts per million (ppm). |
|  | DsssModAccResultsIQGainImbalanceMean | 10498131 | Returns the I/Q gain imbalance. This value is expressed in dB. |
|  | DsssModAccResultsIQQuadratureErrorMean | 10498135 | Returns the I/Q quadrature error. This value is expressed in degrees. |
|  | DsssModAccResultsIQOriginOffsetMean | 10498139 | Returns the I/Q origin offset. This value is expressed in dB. |
|  | DsssModAccResultsRmsMagnitudeErrorMean | 10498146 | Returns the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage. |
|  | DsssModAccResultsRmsPhaseErrorMean | 10498147 | Returns the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees. |
|  | DsssModAccResultsPreambleAveragePowerMean | 10498162 | Returns the average power of the preamble field of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsPreamblePeakPowerMaximum | 10498163 | Returns the peak power of the preamble field of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsHeaderAveragePowerMean | 10498164 | Returns the average power of the header field of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsHeaderPeakPowerMaximum | 10498165 | Returns the peak power of the header field of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsDataAveragePowerMean | 10498166 | Returns the average power of the data field of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsDataPeakPowerMaximum | 10498167 | Returns the peak power of the data field of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsPpduAveragePowerMean | 10498168 | Returns the average power of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsPpduPeakPowerMaximum | 10498169 | Returns the peak power of the PPDU. This value is expressed in dBm. |
|  | DsssModAccResultsCustomGateAveragePowerMean | 10498110 | Returns the average power of the custom gate. This value is expressed in dBm. |
|  | DsssModAccResultsCustomGatePeakPowerMaximum | 10498111 | Returns the peak power of the custom gate. This value is expressed in dBm. |
|  | DsssModAccResultsDataModulationFormat | 10498152 | Returns the data modulation format results of the analyzed waveform. |
|  | DsssModAccResultsPayloadLength | 10498153 | Returns the payload length of the acquired burst. This value is expressed in bytes. |
|  | DsssModAccResultsPreambleType | 10498154 | Returns the detected preamble type of the acquired burst. |
|  | DsssModAccResultsLockedClocksBit | 10498156 | Returns the value of the locked clocks bit in the Long PHY SERVICE field. |
|  | DsssModAccResultsHeaderCrcStatus | 10498157 | Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016 . |
|  | DsssModAccResultsPsduCrcStatus | 10498158 | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
|  | OfdmModAccMeasurementEnabled | 10502144 | Specifies whether to enable OFDMModAcc measurement for OFDM based standards. |
|  | OfdmModAccAveragingEnabled | 10502146 | Specifies whether to enable averaging for OFDMModAcc measurements. |
|  | OfdmModAccAveragingCount | 10502147 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True . |
|  | OfdmModAccAveragingType | 10502316 | Specifies the averaging type for the OFDMModAcc measurement. This method is considered only when you set the OfdmModAccAveragingEnabled method to True and when you set the OfdmModAccAveragingCount method to a value greater than 1. |
|  | OfdmModAccVectorAveragingTimeAlignmentEnabled | 10502317 | Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXOfdmModAccAveragingType method to Vector . You can set this method to False when there is no time offset between the acquired I/Q data of all averaging counts. |
|  | OfdmModAccVectorAveragingPhaseAlignmentEnabled | 10502318 | Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXOfdmModAccAveragingType method to Vector . You can set this method to False when there is no phase offset between the acquired I/Q data of all averaging counts. |
|  | OfdmModAccMeasurementMode | 10502246 | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement. |
|  | OfdmModAccEvmReferenceDataSymbolsMode | 10502291 | Specifies whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation. |
|  | OfdmModAccEvmUnit | 10502152 | Specifies the unit for EVM results. |
|  | OfdmModAccAcquisitionLengthMode | 10502153 | Specifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc properties. |
|  | OfdmModAccAcquisitionLength | 10502154 | Specifies the length of the waveform to be acquired for the OFDMModAcc measurement, when you set the SetAcquisitionLengthMode(String, RFmxWlanMXOfdmModAccAcquisitionLengthMode) method to Manual . This value is expressed in seconds. |
|  | OfdmModAccMeasurementOffset | 10502155 | Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols. |
|  | OfdmModAccMaximumMeasurementLength | 10502156 | Specifies the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols. |
|  | OfdmModAccCombinedSignalDemodulationEnabled | 10502346 | Specifies whether to enable demodulation of the signal that is formed by combining signals from multiple transmitter chains. |
|  | OfdmModAccReferenceDataConstellationIdentifier | 10502347 | Identifies the reference files used for combined signal demodulation. The value of this method must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
|  | OfdmModAccBurstStartDetectionEnabled | 10502277 | Specifies whether the measurement detects a rising edge of a burst in the acquired waveform. |
|  | OfdmModAccFrequencyErrorEstimationMethod | 10502270 | Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal. |
|  | OfdmModAccCommonClockSourceEnabled | 10502157 | Specifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock. |
|  | OfdmModAccCommonPilotErrorScalingReference | 10502353 | Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE. |
|  | OfdmModAccAmplitudeTrackingEnabled | 10502158 | Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol. |
|  | OfdmModAccPhaseTrackingEnabled | 10502159 | Specifies whether to enable pilot-based common phase error correction per OFDM data symbol. |
|  | OfdmModAccSymbolClockErrorCorrectionEnabled | 10502160 | Specifies whether to enable symbol clock error correction. |
|  | OfdmModAccSpectrumInverted | 10502266 | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
|  | OfdmModAccChannelEstimationType | 10502161 | Specifies the fields in the PPDU used to estimate the channel frequency response. |
|  | OfdmModAccChannelEstimationInterpolationType | 10502250 | Specifies the interpolation type and/or smoothing type used on the channel estimates. |
|  | OfdmModAccChannelEstimationSmoothingLength | 10502251 | Specifies the length of the triangular-weighted moving window across subcarriers that is used for averaging the channel estimate. |
|  | OfdmModAccChannelEstimationRelativeDelaySpread | 10502327 | Specifies the expected channel delay spread relative to the OFDM symbol length. |
|  | OfdmModAccChannelEstimationLLtfEnabled | 10502279 | Specifies whether to use the legacy channel estimation field for combining with the reference channel frequency response. |
|  | OfdmModAccPowerMeasurementEnabled | 10502167 | Specifies whether power measurements are performed. |
|  | OfdmModAccPowerNumberOfCustomGates | 10502168 | Specifies the number of custom gates for power measurement. |
|  | OfdmModAccPowerCustomGateStartTime | 10502169 | Specifies the start time of the custom power gate. This value is expressed in seconds. |
|  | OfdmModAccPowerCustomGateStopTime | 10502170 | Specifies the stop time of the custom power gate, and must be greater than the corresponding SetPowerCustomGateStartTime(String, Double) method. This value is expressed in seconds. |
|  | OfdmModAccChannelMatrixPowerEnabled | 10502285 | Specifies whether the channel frequency response matrix power measurements are enabled. This enables cross-power measurements for MIMO signals and user-power measurements for MU signals. |
|  | OfdmModAccIQImpairmentsEstimationEnabled | 10502267 | Specifies whether to enable the estimation of I/Q gain imbalance, I/Q quadrature error, and I/Q timing skew impairments. |
|  | OfdmModAccIQImpairmentsModel | 10502171 | Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. |
|  | OfdmModAccIQGainImbalanceCorrectionEnabled | 10502172 | Specifies whether to enable I/Q gain imbalance correction. |
|  | OfdmModAccIQQuadratureErrorCorrectionEnabled | 10502173 | Specifies whether to enable I/Q quadrature error correction. |
|  | OfdmModAccIQTimingSkewCorrectionEnabled | 10502174 | Specifies whether to enable I/Q timing skew correction. |
|  | OfdmModAccIQImpairmentsPerSubcarrierEnabled | 10502271 | Specifies whether to estimate I/Q impairments independently for each subcarrier. |
|  | OfdmModAccUnusedToneErrorMaskReference | 10502252 | Specifies the reference used to create the unused tone error mask for the 802.11ax or 802.11be TB PPDU signals. |
|  | OfdmModAccDataDecodingEnabled | 10502283 | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
|  | OfdmModAccNoiseCompensationEnabled | 10502247 | Specifies whether the contribution of the instrument noise is compensated for EVM computation. |
|  | OfdmModAccNoiseCompensationInputPowerCheckEnabled | 10502248 | Specifies whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |
|  | OfdmModAccNoiseCompensationReferenceLevelCoercionLimit | 10502249 | Specifies the reference level coercion limit for noise compensation. This value is expressed in dB. |
|  | OfdmModAccOptimizeDynamicRangeForEvmEnabled | 10502268 | Specifies whether to optimize the analyzer's dynamic range for the EVM measurement. |
|  | OfdmModAccOptimizeDynamicRangeForEvmMargin | 10502269 | Specifies the margin above the reference level you specify when you set the SetOptimizeDynamicRangeForEvmEnabled(String, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled) method to True . This value is expressed in dB. |
|  | OfdmModAccAutoLevelAllowOverflow | 10502321 | Specifies whether the AutoLevel(String, Double) function should search for the optimum reference levels while allowing ADC overflow. |
|  | OfdmModAccAllTracesEnabled | 10502149 | Specifies whether to enable all the traces computed by the OFDMModAcc measurement. |
|  | OfdmModAccNumberOfAnalysisThreads | 10502148 | Specifies the maximum number of threads used for parallelism for the OFDMModAcc measurement. |
|  | OfdmModAccResultsCompositeRmsEvmMean | 10502254 | Returns the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set OFDMModAccAveragingEnabled method to True, this method returns the mean of RMS EVM results for the specified user that is computed for each averaging count. |
|  | OfdmModAccResultsCompositeDataRmsEvmMean | 10502255 | Returns the RMS EVM of data-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of data RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsCompositePilotRmsEvmMean | 10502256 | Returns the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method is set to True, this method returns the mean of pilot RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsStreamRmsEvmMean | 10502260 | Returns the stream RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of Stream RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsStreamDataRmsEvmMean | 10502261 | Returns the stream RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of Stream Data RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsStreamPilotRmsEvmMean | 10502262 | Returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of stream Pilot RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsChainRmsEvmMean | 10502257 | Returns the chain RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of chain RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsChainDataRmsEvmMean | 10502258 | Returns the chain RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of data chain RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsChainPilotRmsEvmMean | 10502259 | Returns the chain RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of pilot chain RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsUserStreamRmsEvmMean | 10502263 | Returns the RMS EVM of all subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. This result is applicable for MU PPDU. When you set OFDMModAccAveragingEnabled method to True, this method returns the mean of User Stream RMS EVM results for the specified user that is computed for each averaging count. |
|  | OfdmModAccResultsUserStreamDataRmsEvmMean | 10502264 | Returns the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. This result is applicable for MU PPDU. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of data RMS EVM results for the specified user that is computed for each averaging count. |
|  | OfdmModAccResultsUserStreamPilotRmsEvmMean | 10502265 | Returns the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. This result is applicable for MU PPDU. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of pilot RMS EVM results for the specified user that is computed for each averaging count. |
|  | OfdmModAccResultsLSigRmsEvmMean | 10502331 | Returns the RMS EVM of subcarriers in the L-SIG symbol. This value is expressed as a percentage or in dB. |
|  | OfdmModAccResultsSigRmsEvmMean | 10502332 | Returns the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB. |
|  | OfdmModAccResultsSigBRmsEvmMean | 10502333 | Returns the RMS EVM of subcarriers in the SIG-B symbol. This value is expressed as a percentage or in dB. |
|  | OfdmModAccResultsUSigRmsEvmMean | 10502334 | Returns the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB. |
|  | OfdmModAccResultsEhtSigRmsEvmMean | 10502335 | Returns the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB. |
|  | OfdmModAccResultsLStfAveragePowerMean | 10502202 | Returns the average power of the L-STF or STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsLStfPeakPowerMaximum | 10502203 | Returns the peak power of the L-STF or STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsLLtfAveragePowerMean | 10502204 | Returns the average power of the L-LTF or LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsLLtfPeakPowerMaximum | 10502205 | Returns the peak power of the L-LTF or LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsLSigAveragePowerMean | 10502206 | Returns the average power of the L-SIG or SIGNAL field. This value is expressed in dBm. |
|  | OfdmModAccResultsLSigPeakPowerMaximum | 10502207 | Returns the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm. |
|  | OfdmModAccResultsRLSigAveragePowerMean | 10502208 | Returns the average power of the RL-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsRLSigPeakPowerMaximum | 10502209 | Returns the peak power of the RL-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTSigAveragePowerMean | 10502210 | Returns the average power of the HT-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTSigPeakPowerMaximum | 10502211 | Returns the peak power of the HT-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtSigAAveragePowerMean | 10502212 | Returns the average power of the VHT-SIG-A field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtSigAPeakPowerMaximum | 10502213 | Returns the peak power of the VHT-SIG-A field. This value is expressed in dBm. |
|  | OfdmModAccResultsHESigAAveragePowerMean | 10502214 | Returns the average power of the HE-SIG-A field. This value is expressed in dBm. |
|  | OfdmModAccResultsHESigAPeakPowerMaximum | 10502215 | Returns the peak power of the HE-SIG-A field. This value is expressed in dBm. |
|  | OfdmModAccResultsUSigAveragePowerMean | 10502336 | Returns the average power of the U-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsUSigPeakPowerMaximum | 10502337 | Returns the peak power of the U-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtSigBAveragePowerMean | 10502216 | Returns the average power of the VHT-SIG-B field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtSigBPeakPowerMaximum | 10502217 | Returns the peak power of the VHT-SIG-B field. This value is expressed in dBm. |
|  | OfdmModAccResultsHESigBAveragePowerMean | 10502218 | Returns the average power of the HE-SIG-B field. This value is expressed in dBm. |
|  | OfdmModAccResultsHESigBPeakPowerMaximum | 10502219 | Returns the peak power of the HE-SIG-B field. This value is expressed in dBm. |
|  | OfdmModAccResultsEhtSigAveragePowerMean | 10502338 | Returns the average power of the EHT-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsEhtSigPeakPowerMaximum | 10502339 | Returns the peak power of the EHT-SIG field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTStfAveragePowerMean | 10502220 | Returns the average power of the HT-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTStfPeakPowerMaximum | 10502221 | Returns the peak power of the HT-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTGFStfAveragePowerMean | 10502222 | Returns the average power of the HT-GF-STF. This value is expressed in dBm. |
|  | OfdmModAccResultsHTGFStfPeakPowerMaximum | 10502223 | Returns the peak power of the HT-GF-STF. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtStfAveragePowerMean | 10502224 | Returns the average power of the VHT-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtStfPeakPowerMaximum | 10502225 | Returns the peak power of the VHT-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHEStfAveragePowerMean | 10502226 | Returns the average power of the HE-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHEStfPeakPowerMaximum | 10502227 | Returns the peak power of the HE-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsEhtStfAveragePowerMean | 10502340 | Returns the average power of the EHT-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsEhtStfPeakPowerMaximum | 10502341 | Returns the peak power of the EHT-STF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTDltfAveragePowerMean | 10502228 | Returns the average power of the HT-DLTF. This value is expressed in dBm. |
|  | OfdmModAccResultsHTDltfPeakPowerMaximum | 10502229 | Returns the peak power of the HT-DLTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTEltfAveragePowerMean | 10502230 | Returns the average power of the HT-ELTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHTEltfPeakPowerMaximum | 10502231 | Returns the peak power of the HT-ELTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtLtfAveragePowerMean | 10502232 | Returns the average power of the VHT-LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsVhtLtfPeakPowerMaximum | 10502233 | Returns the peak power of the VHT-LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHELtfAveragePowerMean | 10502234 | Returns the average power of the HE-LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsHELtfPeakPowerMaximum | 10502235 | Returns the peak power of the HE-LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsEhtLtfAveragePowerMean | 10502342 | Returns the average power of the EHT-LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsEhtLtfPeakPowerMaximum | 10502343 | Returns the peak power of the EHT-LTF field. This value is expressed in dBm. |
|  | OfdmModAccResultsDataAveragePowerMean | 10502236 | Returns the average power of the data field. This value is expressed in dBm. |
|  | OfdmModAccResultsDataPeakPowerMaximum | 10502237 | Returns the peak power of the data field. This value is expressed in dBm. |
|  | OfdmModAccResultsPEAveragePowerMean | 10502238 | Returns the average power of the packet extension field. This value is expressed in dBm. |
|  | OfdmModAccResultsPEPeakPowerMaximum | 10502239 | Returns the peak power of the packet extension field. This value is expressed in dBm. |
|  | OfdmModAccResultsPpduAveragePowerMean | 10502240 | Returns the average power of the PPDU. This value is expressed in dBm. |
|  | OfdmModAccResultsPpduPeakPowerMaximum | 10502241 | Returns the peak power of the PPDU. This value is expressed in dBm. |
|  | OfdmModAccResultsCustomGateAveragePowerMean | 10502242 | Returns the average power of the custom gate. This value is expressed in dBm. |
|  | OfdmModAccResultsCustomGatePeakPowerMaximum | 10502243 | Returns the peak power of the custom gate. This value is expressed in dBm. |
|  | OfdmModAccResultsCrossPowerMean | 10502286 | Returns the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. This value is expressed in dB. |
|  | OfdmModAccResultsUserPowerMean | 10502287 | Returns the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. This value is expressed in dBm. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of chain RMS EVM results computed for each averaging count. |
|  | OfdmModAccResultsStreamPowerMean | 10502348 | Returns average stream power across iterations for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
|  | OfdmModAccResultsSpectralFlatnessMargin | 10502179 | Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB. |
|  | OfdmModAccResultsSpectralFlatnessMarginSubcarrierIndex | 10502180 | Returns the subcarrier index corresponding to the GetSpectralFlatnessMargin(String, Double) result. |
|  | OfdmModAccResultsUnusedToneErrorMargin | 10502181 | Returns the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB. |
|  | OfdmModAccResultsUnusedToneErrorMarginRUIndex | 10502182 | Returns the 26-tone RU index corresponding to the GetUnusedToneErrorMargin(String, Double) result. |
|  | OfdmModAccResultsBurstStartTimeMean | 10502320 | Returns the absolute time corresponding to the detected start of the analyzed burst. The start time is computed with respect to the initial time value of the acquired waveform. This value is expressed in seconds. |
|  | OfdmModAccResultsNumberOfSymbolsUsed | 10502166 | Returns the number of OFDM symbols used by the measurement. |
|  | OfdmModAccResultsNoiseCompensationApplied | 10502183 | Returns whether the noise compensation is applied. |
|  | OfdmModAccResultsFrequencyErrorMean | 10502184 | Returns the carrier frequency error of the transmitter. This value is expressed in Hz. |
|  | OfdmModAccResultsFrequencyErrorCcdf10Percent | 10502185 | Returns the 10% point of Complementary Cumulative Distribution Function (CCDF) of the absolute frequency error. This value is expressed in Hz. |
|  | OfdmModAccResultsSymbolClockErrorMean | 10502186 | Returns the symbol clock error of the transmitter. |
|  | OfdmModAccResultsRelativeIQOriginOffsetMean | 10502187 | Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB. |
|  | OfdmModAccResultsAbsoluteIQOriginOffsetMean | 10502188 | Returns the absolute I/Q origin offset, which is the power of the DC subcarrier. This value is expressed in dBm. |
|  | OfdmModAccResultsIQGainImbalanceMean | 10502189 | Returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. This value is expressed in dB. |
|  | OfdmModAccResultsIQQuadratureErrorMean | 10502190 | Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees. |
|  | OfdmModAccResultsIQTimingSkewMean | 10502191 | Returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds. |
|  | OfdmModAccResultsRmsCommonPhaseErrorMean | 10502192 | Returns the RMS common phase error. |
|  | OfdmModAccResultsRmsCommonPilotErrorMean | 10502253 | Returns the RMS common pilot error. This value is expressed as a percentage. |
|  | OfdmModAccResultsPpduType | 10502193 | Returns the PPDU type of the measured signal. |
|  | OfdmModAccResultsMcsIndex | 10502194 | Returns the MCS index or the data rate of the measured signal. |
|  | OfdmModAccResultsAggregation | 10502345 | Returns the value of the Aggregation field as decoded from the high-throughput signal (HT-SIG) field of 802.11n signal. |
|  | OfdmModAccResultsFecCodingType | 10502314 | Returns the FEC coding type for a specified user. |
|  | OfdmModAccResultsRUSize | 10502195 | Returns the RU or the MRU size. |
|  | OfdmModAccResultsRUOffsetMruIndex | 10502196 | Returns the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0 . |
|  | OfdmModAccResultsNumberOfUsers | 10502197 | Returns the number of users. |
|  | OfdmModAccResultsNumberOfHESigBSymbols | 10502198 | Returns the number of HE-SIG-B symbols. |
|  | OfdmModAccResultsGuardIntervalType | 10502199 | Returns the size of the guard interval of OFDM symbols. |
|  | OfdmModAccResultsLtfSize | 10502200 | Returns the HE-LTF size or EHT-LTF size when you set the SetStandard(String, RFmxWlanMXStandard) method to Standard802_11ax or Standard802_11be , respectively. |
|  | OfdmModAccResultsNumberOfSpaceTimeStreams | 10502201 | Returns the number of space time streams. |
|  | OfdmModAccResultsSpaceTimeStreamOffset | 10502288 | Returns the space time stream offset. This method is applicable only to 802.11ax and 802.11be signals. |
|  | OfdmModAccResultsDcmEnabled | 10502315 | Returns whether DCM is enabled for a specified user. |
|  | OfdmModAccResultsLSigParityCheckStatus | 10502280 | Returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms. |
|  | OfdmModAccResultsSigCrcStatus | 10502281 | Returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. |
|  | OfdmModAccResultsSigBCrcStatus | 10502282 | Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. |
|  | OfdmModAccResultsUSigCrcStatus | 10502289 | Returns whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be waveform. |
|  | OfdmModAccResultsEhtSigCrcStatus | 10502290 | Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform. |
|  | OfdmModAccResultsPsduCrcStatus | 10502284 | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
|  | OfdmModAccResultsScramblerSeed | 10502344 | Returns the detected initial state of the scrambler, which is used to scramble the data bits in the device under test (DUT). RFmx uses the same seed to descramble the received bit-sequence. |
|  | OfdmModAccResultsPEDuration | 10502293 | Returns the duration of the packet extension field for the 802.11ax and 802.11be signals. This value is expressed in seconds. |
|  | OfdmModAccResultsPhaseRotationCoefficient1 | 10502328 | Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D6.0. |
|  | OfdmModAccResultsPhaseRotationCoefficient2 | 10502329 | Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0. |
|  | OfdmModAccResultsPhaseRotationCoefficient3 | 10502330 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D6.0. |
|  | SemMeasurementEnabled | 10506240 | Specifies whether to enable the spectral emission mask (SEM) measurement. |
|  | SemMaskType | 10506242 | Specifies whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
|  | SemCarrierIntegrationBandwidth | 10506245 | Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz. |
|  | SemNumberOfOffsets | 10506246 | Specifies the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | SemOffsetStartFrequency | 10506247 | Specifies the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | SemOffsetStopFrequency | 10506248 | Specifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |
|  | SemOffsetSideband | 10506249 | Specifies whether the offset segment is present on one side or on both sides of the carrier. |
|  | SemOffsetRelativeLimitStart | 10506250 | Specifies the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. |
|  | SemOffsetRelativeLimitStop | 10506251 | Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
|  | SemSpanAuto | 10506252 | Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
|  | SemSpan | 10506253 | Specifies the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz. |
|  | SemSweepTimeAuto | 10506257 | Specifies whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
|  | SemSweepTimeInterval | 10506258 | Specifies the sweep time for the SEM measurement. This value is expressed in seconds. |
|  | SemAveragingEnabled | 10506259 | Specifies whether to enable averaging for the SEM measurement. |
|  | SemAveragingCount | 10506260 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled) method to True . |
|  | SemAveragingType | 10506261 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
|  | SemAmplitudeCorrectionType | 10506262 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SemAllTracesEnabled | 10506263 | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | SemNumberOfAnalysisThreads | 10506264 | Specifies the maximum number of threads used for parallelism for SEM measurement. |
|  | SemResultsMeasurementStatus | 10506267 | Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. |
|  | SemResultsCarrierAbsoluteIntegratedPower | 10506268 | Returns the average power of the carrier channel over the bandwidth indicated by the GetCarrierIntegrationBandwidth(String, Double) method. This value is expressed in dBm. |
|  | SemResultsCarrierAbsolutePeakPower | 10506270 | Returns the peak power in the carrier channel over the bandwidth indicated by the GetCarrierIntegrationBandwidth(String, Double) method. This value is expressed in dBm. SEM mask level is determined by this result. |
|  | SemResultsCarrierPeakFrequency | 10506271 | Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. |
|  | SemResultsLowerOffsetMeasurementStatus | 10506273 | Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. |
|  | SemResultsLowerOffsetAbsoluteIntegratedPower | 10506274 | Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm. |
|  | SemResultsLowerOffsetRelativeIntegratedPower | 10506275 | Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | SemResultsLowerOffsetAbsolutePeakPower | 10506276 | Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. |
|  | SemResultsLowerOffsetRelativePeakPower | 10506277 | Returns the peak power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | SemResultsLowerOffsetPeakFrequency | 10506278 | Returns the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz. |
|  | SemResultsLowerOffsetMargin | 10506279 | Returns the margin from the SEM measurement mask for the lower (negative) offset. This value is expressed in dB. |
|  | SemResultsLowerOffsetMarginAbsolutePower | 10506280 | Returns the power level of the spectrum corresponding to the result of the GetLowerOffsetMargin(String, Double) method. This value is expressed in dBm. |
|  | SemResultsLowerOffsetMarginRelativePower | 10506281 | Returns the power level of the spectrum corresponding to the result of the GetLowerOffsetMargin(String, Double) method. This value is expressed in dB. |
|  | SemResultsLowerOffsetMarginFrequency | 10506282 | Returns the frequency of the spectrum corresponding to the result of the GetLowerOffsetMargin(String, Double) method. This value is expressed in Hz. |
|  | SemResultsUpperOffsetMeasurementStatus | 10506283 | Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment. |
|  | SemResultsUpperOffsetAbsoluteIntegratedPower | 10506284 | Returns the average power of the offset (positive) offset channel over the bandwidth determined by the start and stop frequencies of the offset channel. This value is expressed in dBm. |
|  | SemResultsUpperOffsetRelativeIntegratedPower | 10506285 | Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | SemResultsUpperOffsetAbsolutePeakPower | 10506286 | Returns the peak power of the offset (positive) offset segment. This value is expressed in dBm. |
|  | SemResultsUpperOffsetRelativePeakPower | 10506287 | Returns the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | SemResultsUpperOffsetPeakFrequency | 10506288 | Returns the frequency at which the peak power occurs in the offset (positive) channel. This value is expressed in Hz. |
|  | SemResultsUpperOffsetMargin | 10506289 | Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB. |
|  | SemResultsUpperOffsetMarginAbsolutePower | 10506290 | Returns the power level of the spectrum corresponding to the result of the GetUpperOffsetMargin(String, Double) method. This value is expressed in dBm. |
|  | SemResultsUpperOffsetMarginRelativePower | 10506291 | Returns the power level of the spectrum corresponding to the result of the GetUpperOffsetMargin(String, Double) method. This value is expressed in dB. |
|  | SemResultsUpperOffsetMarginFrequency | 10506292 | Returns the frequency of the spectrum corresponding to the result of the GetUpperOffsetMargin(String, Double) method. This value is expressed in Hz. |
|  | TxpMeasurementEnabled | 10489856 | Specifies whether to enable the transmit power (TXP) measurement. |
|  | TxpMaximumMeasurementInterval | 10489858 | Specifies the maximum measurement interval. This value is expressed in seconds. |
|  | TxpBurstDetectionEnabled | 10489859 | Specifies whether the measurement detects the start and the end of a WLAN packet automatically. |
|  | TxpAveragingEnabled | 10489860 | Specifies whether to enable averaging for the TXP measurement. |
|  | TxpAveragingCount | 10489861 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXTxpAveragingEnabled) method to True . |
|  | TxpAllTracesEnabled | 10489862 | Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
|  | TxpNumberOfAnalysisThreads | 10489863 | Specifies the maximum number of threads used for parallelism for TXP measurement. |
|  | TxpResultsAveragePowerMean | 10489865 | Returns the average power of the acquired signal. This value is expressed in dBm. |
|  | TxpResultsPeakPowerMaximum | 10489873 | Returns the peak power of the acquired signal. This value is expressed in dBm. |
|  | PowerRampMeasurementEnabled | 10493962 | Specifies whether to enable PowerRamp measurement. |
|  | PowerRampAcquisitionLength | 10493964 | Specifies the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds. |
|  | PowerRampAveragingEnabled | 10493972 | Specifies if averaging is enabled for PowerRamp measurements. |
|  | PowerRampAveragingCount | 10493973 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXPowerRampAveragingEnabled) method to True . |
|  | PowerRampAllTracesEnabled | 10493974 | Specifies whether to enable all the traces computed by the PowerRamp measurement. |
|  | PowerRampNumberOfAnalysisThreads | 10493975 | Specifies the maximum number of threads used for parallelism for PowerRamp measurement. |
|  | PowerRampResultsRiseTimeMean | 10493976 | Returns the power-ramp rise time of the burst. This value is expressed in seconds. |
|  | PowerRampResultsFallTimeMean | 10493977 | Returns the power-ramp fall time of the burst. This value is expressed in seconds. |
|  | AutoLevelInitialReferenceLevel | 10485796 | Specifies the initial reference level which the AutoLevel(String, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SampleClockRateFactor | 10485814 | Specifies the factor by which the sample clock rate is multiplied at the transmitter to generate a signal compressed in the frequency domain and expanded in the time domain. |
|  | LimitedConfigurationChange | 10485797 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | ResultFetchTimeout | 10534912 | Specifies the time, in seconds, to wait before results are available in the RFmxWLAN_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/47d0d074-90b1-b25b-d0d7-1f968c78e7f1.htm language=enus -->
## TOPIC 00076: rfmxwlandotnet/html/47d0d074-90b1-b25b-d0d7-1f968c78e7f1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/47d0d074-90b1-b25b-d0d7-1f968c78e7f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/47d0d074-90b1-b25b-d0d7-1f968c78e7f1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetDigitalEdgeTriggerSource Method

RFmxWlanMXGetDigitalEdgeTriggerSource Method

SetTriggerType(String, RFmxWlanMXTriggerType)

DigitalEdge

On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is configured to "segment0/chain0" and is considered as the master port.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to DigitalEdge .

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/48768da3-e0af-6de6-f3b1-9086752278e0.htm language=enus -->
## TOPIC 00077: rfmxwlandotnet/html/48768da3-e0af-6de6-f3b1-9086752278e0.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/48768da3-e0af-6de6-f3b1-9086752278e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/48768da3-e0af-6de6-f3b1-9086752278e0.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.SetChipClockErrorCorrectionEnabled Method

RFmxWlanMXDsssModAccConfigurationSetChipClockErrorCorrectionEnabled Method

Sets whether to enable chip clock error correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChipClockErrorCorrectionEnabled(
	string selectorString,
	RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled value
)
```

```text
Public Function SetChipClockErrorCorrectionEnabled ( 
	selectorString As String,
	value As RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccChipClockErrorCorrectionEnabledSpecifies whether to enable chip clock error correction.

###### Return Value

Int32

##### Remarks

DsssModAccChipClockErrorCorrectionEnabled

True

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/48b4ca0e-196d-3b4e-9299-95baa6c6714c.htm language=enus -->
## TOPIC 00078: rfmxwlandotnet/html/48b4ca0e-196d-3b4e-9299-95baa6c6714c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/48b4ca0e-196d-3b4e-9299-95baa6c6714c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/48b4ca0e-196d-3b4e-9299-95baa6c6714c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetCompositePilotRmsEvmMean Method

RFmxWlanMXOfdmModAccResultsGetCompositePilotRmsEvmMean Method

Gets the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCompositePilotRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetCompositePilotRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsCompositePilotRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4953352b-03ca-b956-5265-f9e51db0473f.htm language=enus -->
## TOPIC 00079: rfmxwlandotnet/html/4953352b-03ca-b956-5265-f9e51db0473f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4953352b-03ca-b956-5265-f9e51db0473f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4953352b-03ca-b956-5265-f9e51db0473f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetTriggerGateEnabled Method

RFmxWlanMXSetTriggerGateEnabled Method

Enables time-domain gating of the acquired signal for SEM measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerGateEnabled(
	string selectorString,
	RFmxWlanMXTriggerGateEnabled value
)
```

```text
Public Function SetTriggerGateEnabled ( 
	selectorString As String,
	value As RFmxWlanMXTriggerGateEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXTriggerGateEnabledEnables time-domain gating of the acquired signal for SEM measurement.

###### Return Value

Int32

##### Remarks

TriggerGateEnabled

False

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/49cc92e8-ecc4-bb20-faf9-5d3eed4dbd83.htm language=enus -->
## TOPIC 00080: rfmxwlandotnet/html/49cc92e8-ecc4-bb20-faf9-5d3eed4dbd83.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/49cc92e8-ecc4-bb20-faf9-5d3eed4dbd83.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/49cc92e8-ecc4-bb20-faf9-5d3eed4dbd83.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemAmplitudeCorrectionType Enumeration

RFmxWlanMXSemAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXSemAmplitudeCorrectionType
```

```text
Public Enumeration RFmxWlanMXSemAmplitudeCorrectionType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
|  | SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4a5b6891-5607-fa32-0ab7-677c8a40f639.htm language=enus -->
## TOPIC 00081: rfmxwlandotnet/html/4a5b6891-5607-fa32-0ab7-677c8a40f639.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4a5b6891-5607-fa32-0ab7-677c8a40f639.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4a5b6891-5607-fa32-0ab7-677c8a40f639.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchUserPower Method

RFmxWlanMXOfdmModAccResultsFetchUserPower Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUserPower(
	string selectorString,
	double timeout,
	out double userPowerMean
)
```

```text
Public Function FetchUserPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef userPowerMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and user number. If you do not specify the result name, the default result instance is used. Example: "user0""result::r1/user0" You can use the BuildUserString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **userPowerMean**
  - Type: SystemDouble Upon return, contains the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the user power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4ab1e030-9fb6-8cb4-49ae-d4dedcaaea88.htm language=enus -->
## TOPIC 00082: rfmxwlandotnet/html/4ab1e030-9fb6-8cb4-49ae-d4dedcaaea88.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4ab1e030-9fb6-8cb4-49ae-d4dedcaaea88.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4ab1e030-9fb6-8cb4-49ae-d4dedcaaea88.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchStreamRmsEvm Method

RFmxWlanMXOfdmModAccResultsFetchStreamRmsEvm Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchStreamRmsEvm(
	string selectorString,
	double timeout,
	out double streamRmsEvmMean,
	out double streamDataRmsEvmMean,
	out double streamPilotRmsEvmMean
)
```

```text
Public Function FetchStreamRmsEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef streamRmsEvmMean As Double,
	<OutAttribute> ByRef streamDataRmsEvmMean As Double,
	<OutAttribute> ByRef streamPilotRmsEvmMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and stream number. If you do not specify the result name, the default result instance is used. Example: "segment0/stream0""result::r1/segment0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **streamRmsEvmMean**
  - Type: SystemDouble Upon return, contains the stream RMS EVM of all subcarriers in all OFDM symbols. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB.
- **streamDataRmsEvmMean**
  - Type: SystemDouble Upon return, contains the stream RMS EVM of data subcarriers in all OFDM symbols. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of data stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB.
- **streamPilotRmsEvmMean**
  - Type: SystemDouble Upon return, contains the stream RMS EVM of pilot subcarriers in all OFDM symbols. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of pilot stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4ab93496-053e-158c-23ad-ee70df52e5b0.htm language=enus -->
## TOPIC 00083: rfmxwlandotnet/html/4ab93496-053e-158c-23ad-ee70df52e5b0.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4ab93496-053e-158c-23ad-ee70df52e5b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4ab93496-053e-158c-23ad-ee70df52e5b0.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchPhaseNoisePsdMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchPhaseNoisePsdMeanTrace Method

OfdmModAccAveragingEnabled

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPhaseNoisePsdMeanTrace(
	string selectorString,
	double timeout,
	ref Spectrum<float> phaseNoisePsdMean
)
```

```text
Public Function FetchPhaseNoisePsdMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef phaseNoisePsdMean As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and segment number. You can also pass selectorStringOut from the BuildSegmentString(String, Int32) method as an input to this method. Example: "segment0""result::r1/segment0" You can use the RFmxWLAN Build Segment String method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **phaseNoisePsdMean**
  - Type: NationalInstrumentsSpectrumSingleReturns the mean of the phase noise PSD trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4b2175c6-76e7-6e96-cb70-61be4cdf689e.htm language=enus -->
## TOPIC 00084: rfmxwlandotnet/html/4b2175c6-76e7-6e96-cb70-61be4cdf689e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4b2175c6-76e7-6e96-cb70-61be4cdf689e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4b2175c6-76e7-6e96-cb70-61be4cdf689e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetPhaseRotationCoefficient2 Method

RFmxWlanMXOfdmModAccResultsGetPhaseRotationCoefficient2 Method

Gets the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseRotationCoefficient2(
	string selectorString,
	out RFmxWlanMXOfdmModAccPhaseRotationCoefficient2 value
)
```

```text
Public Function GetPhaseRotationCoefficient2 ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccPhaseRotationCoefficient2
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example:"""result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccPhaseRotationCoefficient2 Upon return, contains the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4bdab826-314f-e282-1af1-cb13f9312f89.htm language=enus -->
## TOPIC 00085: rfmxwlandotnet/html/4bdab826-314f-e282-1af1-cb13f9312f89.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4bdab826-314f-e282-1af1-cb13f9312f89.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4bdab826-314f-e282-1af1-cb13f9312f89.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchSpectralFlatnessMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchSpectralFlatnessMeanTrace Method

SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSpectralFlatnessMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> spectralFlatnessMean,
	ref AnalogWaveform<float> spectralFlatnessLowerMask,
	ref AnalogWaveform<float> spectralFlatnessUpperMask
)
```

```text
Public Function FetchSpectralFlatnessMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef spectralFlatnessMean As AnalogWaveform(Of Single),
	ByRef spectralFlatnessLowerMask As AnalogWaveform(Of Single),
	ByRef spectralFlatnessUpperMask As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, chain number, and stream number. Example: "segment0/chain0/stream0""result::r1/segment0/chain0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **spectralFlatnessMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the spectral flatness trace.
- **spectralFlatnessLowerMask**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the lower spectral flatness mask trace.
- **spectralFlatnessUpperMask**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the upper spectral flatness mask trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4cb26bc9-bddf-436d-1229-78f44ec4d1e1.htm language=enus -->
## TOPIC 00086: rfmxwlandotnet/html/4cb26bc9-bddf-436d-1229-78f44ec4d1e1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4cb26bc9-bddf-436d-1229-78f44ec4d1e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4cb26bc9-bddf-436d-1229-78f44ec4d1e1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.DisableTrigger Method

RFmxWlanMXDisableTrigger Method

Namespace:

NationalInstruments.RFmx.WlanMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4cb4eeb1-9bac-9c68-155c-4683a4ea3b9b.htm language=enus -->
## TOPIC 00087: rfmxwlandotnet/html/4cb4eeb1-9bac-9c68-155c-4683a4ea3b9b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4cb4eeb1-9bac-9c68-155c-4683a4ea3b9b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4cb4eeb1-9bac-9c68-155c-4683a4ea3b9b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.ConfigurePowerMeasurementEnabled Method

RFmxWlanMXDsssModAccConfigurationConfigurePowerMeasurementEnabled Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigurePowerMeasurementEnabled(
	string selectorString,
	RFmxWlanMXDsssModAccPowerMeasurementEnabled powerMeasurementEnabled
)
```

```text
Public Function ConfigurePowerMeasurementEnabled ( 
	selectorString As String,
	powerMeasurementEnabled As RFmxWlanMXDsssModAccPowerMeasurementEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **powerMeasurementEnabled**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDsssModAccPowerMeasurementEnabled Specifies if power measurement is performed. This parameter computes power of various fields in the PPDU. Additionally, this measurement computes power over the custom gates that you can configure using the SetPowerNumberOfCustomGates(String, Int32) , the SetPowerCustomGateStartTime(String, Double) and the SetPowerCustomGateStopTime(String, Double) methods.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4cbb518a-e9cd-025c-8e41-1b4622968d48.htm language=enus -->
## TOPIC 00088: rfmxwlandotnet/html/4cbb518a-e9cd-025c-8e41-1b4622968d48.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4cbb518a-e9cd-025c-8e41-1b4622968d48.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4cbb518a-e9cd-025c-8e41-1b4622968d48.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetOptimizeDynamicRangeForEvmMargin Method

RFmxWlanMXOfdmModAccConfigurationGetOptimizeDynamicRangeForEvmMargin Method

SetOptimizeDynamicRangeForEvmEnabled(String, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOptimizeDynamicRangeForEvmMargin(
	string selectorString,
	out double value
)
```

```text
Public Function GetOptimizeDynamicRangeForEvmMargin ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the margin above the reference level you specify when you set the SetOptimizeDynamicRangeForEvmEnabled(String, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled) method to True . This value is expressed in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccOptimizeDynamicRangeForEvmMargin

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4ce0504f-a387-c91d-2b27-75e120cf9acd.htm language=enus -->
## TOPIC 00089: rfmxwlandotnet/html/4ce0504f-a387-c91d-2b27-75e120cf9acd.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4ce0504f-a387-c91d-2b27-75e120cf9acd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4ce0504f-a387-c91d-2b27-75e120cf9acd.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchDataConstellationTrace Method

RFmxWlanMXOfdmModAccResultsFetchDataConstellationTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDataConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] dataConstellation
)
```

```text
Public Function FetchDataConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef dataConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and stream number. If you do not specify the result name, the default result instance is used. Example: "segment0/stream0""result::r1/segment0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **dataConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the demodulated QAM symbols from all the data-subcarriers in all the OFDM symbols.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4e89d440-3b0a-0666-07ac-31e76b98b414.htm language=enus -->
## TOPIC 00090: rfmxwlandotnet/html/4e89d440-3b0a-0666-07ac-31e76b98b414.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4e89d440-3b0a-0666-07ac-31e76b98b414.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4e89d440-3b0a-0666-07ac-31e76b98b414.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccAveragingType Enumeration

RFmxWlanMXOfdmModAccAveragingType Enumeration

Specifies the averaging type for the OFDMModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccAveragingType
```

```text
Public Enumeration RFmxWlanMXOfdmModAccAveragingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rms | 0 | The OFDMModAcc measurement is performed on I/Q data acquired in each averaging count. The scalar results and traces are linearly averaged over the averaging count. |
|  | Vector | 5 | The acquired I/Q data is averaged across averaging count after aligning the data in time and phase using the SetVectorAveragingTimeAlignmentEnabled(String, RFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabled) and SetVectorAveragingPhaseAlignmentEnabled(String, RFmxWlanMXOfdmModAccVectorAveragingPhaseAlignmentEnabled) properties, respectively. The averaged I/Q data is used for the measurement. Note: You must ensure that the frequency reference is locked between the generator and the analyzer. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4efd39e6-f30e-9ee8-a001-2e447940fb2a.htm language=enus -->
## TOPIC 00091: rfmxwlandotnet/html/4efd39e6-f30e-9ee8-a001-2e447940fb2a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4efd39e6-f30e-9ee8-a001-2e447940fb2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4efd39e6-f30e-9ee8-a001-2e447940fb2a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXConstants.PxiTriggerLine2 Field

RFmxWlanMXConstantsPxiTriggerLine2 Field

The signal is exported to the PXI trigger line 2.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMXConstants Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4f76d4cc-4f80-d313-4dfc-235110280801.htm language=enus -->
## TOPIC 00092: rfmxwlandotnet/html/4f76d4cc-4f80-d313-4dfc-235110280801.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4f76d4cc-4f80-d313-4dfc-235110280801.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4f76d4cc-4f80-d313-4dfc-235110280801.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.FetchUpperOffsetMargin Method

RFmxWlanMXSemResultsFetchUpperOffsetMargin Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUpperOffsetMargin(
	string selectorString,
	double timeout,
	out RFmxWlanMXSemUpperOffsetMeasurementStatus measurementStatus,
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
	<OutAttribute> ByRef measurementStatus As RFmxWlanMXSemUpperOffsetMeasurementStatus,
	<OutAttribute> ByRef margin As Double,
	<OutAttribute> ByRef marginFrequency As Double,
	<OutAttribute> ByRef marginAbsolutePower As Double,
	<OutAttribute> ByRef marginRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, chain number, and offset number. Example: "segment0/chain0/offset0""result::r1/segment0/chain0/offset0" You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **measurementStatus**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemUpperOffsetMeasurementStatus Upon return, contains the upper (positive) offset segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the upper offset segment.
- **margin**
  - Type: SystemDouble Upon return, contains the margin from the SEM measurement mask for the upper offset. Margin is defined as the maximum difference between the spectrum and the mask. This value is expressed in dB.
- **marginFrequency**
  - Type: SystemDouble Upon return, contains the frequency corresponding to the margin for the upper offset. This value is expressed in Hz.
- **marginAbsolutePower**
  - Type: SystemDouble Upon return, contains the power level of the spectrum, corresponding to the SEM Results Upper Offset Margin result. This value is expressed in dBm.
- **marginRelativePower**
  - Type: SystemDouble Upon return, contains the power level of the spectrum, corresponding to the GetUpperOffsetMargin(String, Double) result. The power level is returned relative to the peak power of the carrier channel. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/4fa0063e-2a42-78c6-883f-f97535b8d344.htm language=enus -->
## TOPIC 00093: rfmxwlandotnet/html/4fa0063e-2a42-78c6-883f-f97535b8d344.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/4fa0063e-2a42-78c6-883f-f97535b8d344.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/4fa0063e-2a42-78c6-883f-f97535b8d344.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHTGFStfPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetHTGFStfPeakPowerMaximum Method

Gets the peak power of the HT-GF-STF. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHTGFStfPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetHTGFStfPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the HT-GF-STF. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHTGFStfPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/502d9c42-c308-addd-b6a5-bddbfb9094e6.htm language=enus -->
## TOPIC 00094: rfmxwlandotnet/html/502d9c42-c308-addd-b6a5-bddbfb9094e6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/502d9c42-c308-addd-b6a5-bddbfb9094e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/502d9c42-c308-addd-b6a5-bddbfb9094e6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetLowerOffsetAbsoluteIntegratedPower Method

RFmxWlanMXSemResultsGetLowerOffsetAbsoluteIntegratedPower Method

Gets the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetAbsoluteIntegratedPower

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/50515319-194f-5356-f018-4c78b95e6f84.htm language=enus -->
## TOPIC 00095: rfmxwlandotnet/html/50515319-194f-5356-f018-4c78b95e6f84.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/50515319-194f-5356-f018-4c78b95e6f84.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/50515319-194f-5356-f018-4c78b95e6f84.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetNumberOfHESigBSymbols Method

RFmxWlanMXOfdmModAccResultsGetNumberOfHESigBSymbols Method

Gets the number of HE-SIG-B symbols.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfHESigBSymbols(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfHESigBSymbols ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemInt32Upon return, contains the number of HE-SIG-B symbols.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsNumberOfHESigBSymbols

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/505a85ba-6eed-6e97-372d-b1f2e34cdd03.htm language=enus -->
## TOPIC 00096: rfmxwlandotnet/html/505a85ba-6eed-6e97-372d-b1f2e34cdd03.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/505a85ba-6eed-6e97-372d-b1f2e34cdd03.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/505a85ba-6eed-6e97-372d-b1f2e34cdd03.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmRUOffsetMruIndex Method

RFmxWlanMXGetOfdmRUOffsetMruIndex Method

Gets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs.
If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of
 IEEE P802.11be/D6.0
 .

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmRUOffsetMruIndex(
	string selectorString,
	out int value
)
```

```text
Public Function GetOfdmRUOffsetMruIndex ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the user number. Example: "user0". You can use the BuildUserString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0 .

###### Return Value

Int32

##### Remarks

OfdmRUOffsetMruIndex

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/51b40eb1-1b84-b93e-c34e-e6e1b8f9b6f1.htm language=enus -->
## TOPIC 00097: rfmxwlandotnet/html/51b40eb1-1b84-b93e-c34e-e6e1b8f9b6f1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/51b40eb1-1b84-b93e-c34e-e6e1b8f9b6f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/51b40eb1-1b84-b93e-c34e-e6e1b8f9b6f1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.SetPowerCustomGateStartTime Method

RFmxWlanMXDsssModAccConfigurationSetPowerCustomGateStartTime Method

Sets the start time of the custom power gate. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPowerCustomGateStartTime(
	string selectorString,
	double value
)
```

```text
Public Function SetPowerCustomGateStartTime ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the gate number. Example: "gate0". You can use the BuildGateString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the start time of the custom power gate. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

DsssModAccPowerCustomGateStartTime

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5211b93d-44cd-4982-e069-73877fb87eed.htm language=enus -->
## TOPIC 00098: rfmxwlandotnet/html/5211b93d-44cd-4982-e069-73877fb87eed.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5211b93d-44cd-4982-e069-73877fb87eed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5211b93d-44cd-4982-e069-73877fb87eed.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXConstants.Pfi0 Field

RFmxWlanMXConstantsPfi0 Field

The signal is exported to the PFI 0.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMXConstants Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/525dfd9b-ae95-b490-ad81-ffaa106a314d.htm language=enus -->
## TOPIC 00099: rfmxwlandotnet/html/525dfd9b-ae95-b490-ad81-ffaa106a314d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/525dfd9b-ae95-b490-ad81-ffaa106a314d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/525dfd9b-ae95-b490-ad81-ffaa106a314d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchPilotConstellationTrace Method

RFmxWlanMXOfdmModAccResultsFetchPilotConstellationTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPilotConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] pilotConstellation
)
```

```text
Public Function FetchPilotConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef pilotConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and stream number. If you do not specify the result name, the default result instance is used. Example: "segment0/stream0""result::r1/segment0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **pilotConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the demodulated QAM symbols from all the pilot-subcarriers in all OFDM symbols.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/526c346a-c32d-9e48-b110-1b2e13b3696a.htm language=enus -->
## TOPIC 00100: rfmxwlandotnet/html/526c346a-c32d-9e48-b110-1b2e13b3696a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/526c346a-c32d-9e48-b110-1b2e13b3696a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/526c346a-c32d-9e48-b110-1b2e13b3696a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchUserPilotConstellationTrace Method

RFmxWlanMXOfdmModAccResultsFetchUserPilotConstellationTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUserPilotConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] userPilotConstellation
)
```

```text
Public Function FetchUserPilotConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef userPilotConstellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0""result::r1/user0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **userPilotConstellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the demodulated QAM symbols from all the pilot-subcarriers in all of the OFDM symbols for each user.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5272ebae-3bce-b8fb-7306-a0d81a55603b.htm language=enus -->
## TOPIC 00101: rfmxwlandotnet/html/5272ebae-3bce-b8fb-7306-a0d81a55603b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5272ebae-3bce-b8fb-7306-a0d81a55603b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5272ebae-3bce-b8fb-7306-a0d81a55603b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpConfiguration Class

RFmxWlanMXTxpConfiguration Class

Provides methods to configure the TXP measurement.

##### Inheritance Hierarchy

RFmxWlanMXSubObject

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxWlanMXTxpConfiguration : RFmxWlanMXSubObject
```

```text
Public NotInheritable Class RFmxWlanMXTxpConfiguration
	Inherits RFmxWlanMXSubObject
```

The RFmxWlanMXTxpConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the measurement. |
|  | ConfigureBurstDetectionEnabled | Configures burst detection for the TXP measurement. |
|  | ConfigureMaximumMeasurementInterval | Configures the maximum measurement interval for the TXP measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXTxpAveragingEnabled) method to True . |
|  | GetAveragingEnabled | Gets whether to enable averaging for the TXP measurement. |
|  | GetBurstDetectionEnabled | Gets whether the measurement detects the start and the end of a WLAN packet automatically. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaximumMeasurementInterval | Gets the maximum measurement interval. This value is expressed in seconds. |
|  | GetMeasurementEnabled | Gets whether to enable the transmit power (TXP) measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for TXP measurement. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXTxpAveragingEnabled) method to True . |
|  | SetAveragingEnabled | Sets whether to enable averaging for the TXP measurement. |
|  | SetBurstDetectionEnabled | Sets whether the measurement detects the start and the end of a WLAN packet automatically. |
|  | SetMaximumMeasurementInterval | Sets the maximum measurement interval. This value is expressed in seconds. |
|  | SetMeasurementEnabled | Sets whether to enable the transmit power (TXP) measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for TXP measurement. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/528afbc5-d478-625e-2b29-d20fd12ff499.htm language=enus -->
## TOPIC 00102: rfmxwlandotnet/html/528afbc5-d478-625e-2b29-d20fd12ff499.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/528afbc5-d478-625e-2b29-d20fd12ff499.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/528afbc5-d478-625e-2b29-d20fd12ff499.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmPreamblePuncturingEnabled Method

RFmxWlanMXSetOfdmPreamblePuncturingEnabled Method

Sets whether the 802.11ax MU PPDU or the 802.11be MU PPDU signal is preamble punctured.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmPreamblePuncturingEnabled(
	string selectorString,
	RFmxWlanMXOfdmPreamblePuncturingEnabled value
)
```

```text
Public Function SetOfdmPreamblePuncturingEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmPreamblePuncturingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmPreamblePuncturingEnabledSpecifies whether the 802.11ax MU PPDU or the 802.11be MU PPDU signal is preamble punctured.

###### Return Value

Int32

##### Remarks

OfdmPreamblePuncturingEnabled

False

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/52a41fc9-dea6-98c4-1fc0-c69303587293.htm language=enus -->
## TOPIC 00103: rfmxwlandotnet/html/52a41fc9-dea6-98c4-1fc0-c69303587293.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/52a41fc9-dea6-98c4-1fc0-c69303587293.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/52a41fc9-dea6-98c4-1fc0-c69303587293.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchIQQuadratureErrorPerSubcarrierMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchIQQuadratureErrorPerSubcarrierMeanTrace Method

SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchIQQuadratureErrorPerSubcarrierMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> iqQuadratureErrorPerSubcarrierMean
)
```

```text
Public Function FetchIQQuadratureErrorPerSubcarrierMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef iqQuadratureErrorPerSubcarrierMean As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **iqQuadratureErrorPerSubcarrierMean**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the I/Q quadrature error per subcarrier trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/535f2b28-1218-204f-575a-d9a3e9f39fe6.htm language=enus -->
## TOPIC 00104: rfmxwlandotnet/html/535f2b28-1218-204f-575a-d9a3e9f39fe6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/535f2b28-1218-204f-575a-d9a3e9f39fe6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/535f2b28-1218-204f-575a-d9a3e9f39fe6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmLtfSize Method

RFmxWlanMXSetOfdmLtfSize Method

For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmLtfSize(
	string selectorString,
	RFmxWlanMXOfdmLtfSize value
)
```

```text
Public Function SetOfdmLtfSize ( 
	selectorString As String,
	value As RFmxWlanMXOfdmLtfSize
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmLtfSizeSpecifies the LTF symbol size. This method is applicable only for 802.11ax and 802.11be signals.

###### Return Value

Int32

##### Remarks

OfdmLtfSize

LtfSize4x

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/53672370-be85-5de2-3827-2646accf201d.htm language=enus -->
## TOPIC 00105: rfmxwlandotnet/html/53672370-be85-5de2-3827-2646accf201d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/53672370-be85-5de2-3827-2646accf201d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/53672370-be85-5de2-3827-2646accf201d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetHeaderAveragePowerMean Method

RFmxWlanMXDsssModAccResultsGetHeaderAveragePowerMean Method

Gets the average power of the header field of the PPDU. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHeaderAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetHeaderAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the header field of the PPDU. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

DsssModAccResultsHeaderAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/546de406-0e0f-dde7-fb08-657fd59197a9.htm language=enus -->
## TOPIC 00106: rfmxwlandotnet/html/546de406-0e0f-dde7-fb08-657fd59197a9.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/546de406-0e0f-dde7-fb08-657fd59197a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/546de406-0e0f-dde7-fb08-657fd59197a9.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchPreambleFrequencyErrorTrace Method

RFmxWlanMXOfdmModAccResultsFetchPreambleFrequencyErrorTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPreambleFrequencyErrorTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> preambleFrequencyError
)
```

```text
Public Function FetchPreambleFrequencyErrorTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef preambleFrequencyError As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **preambleFrequencyError**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/54f30677-249d-7cb2-ac2f-e65f9ff3723b.htm language=enus -->
## TOPIC 00107: rfmxwlandotnet/html/54f30677-249d-7cb2-ac2f-e65f9ff3723b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/54f30677-249d-7cb2-ac2f-e65f9ff3723b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/54f30677-249d-7cb2-ac2f-e65f9ff3723b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetDetectedStandard Method

RFmxWlanMXGetDetectedStandard Method

AutoDetectSignal(String, Double)

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectedStandard(
	string selectorString,
	out RFmxWlanMXStandard value
)
```

```text
Public Function GetDetectedStandard ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXStandard
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXStandard Upon return, contains the standard detected by the AutoDetectSignal(String, Double) function.

###### Return Value

Int32

##### Remarks

DetectedStandard

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/55e7255d-fb71-2e57-7161-e4d33bdb44da.htm language=enus -->
## TOPIC 00108: rfmxwlandotnet/html/55e7255d-fb71-2e57-7161-e4d33bdb44da.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/55e7255d-fb71-2e57-7161-e4d33bdb44da.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/55e7255d-fb71-2e57-7161-e4d33bdb44da.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.AbortMeasurements Method

RFmxWlanMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/560913d5-9052-7fc9-e20a-0688f5fdb3f2.htm language=enus -->
## TOPIC 00109: rfmxwlandotnet/html/560913d5-9052-7fc9-e20a-0688f5fdb3f2.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/560913d5-9052-7fc9-e20a-0688f5fdb3f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/560913d5-9052-7fc9-e20a-0688f5fdb3f2.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.Commit Method

RFmxWlanMXCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/56249ec2-e9c9-d260-5551-7ff0ca99060d.htm language=enus -->
## TOPIC 00110: rfmxwlandotnet/html/56249ec2-e9c9-d260-5551-7ff0ca99060d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/56249ec2-e9c9-d260-5551-7ff0ca99060d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/56249ec2-e9c9-d260-5551-7ff0ca99060d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchSigCrcStatus Method

RFmxWlanMXOfdmModAccResultsFetchSigCrcStatus Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSigCrcStatus(
	string selectorString,
	double timeout,
	out RFmxWlanMXOfdmModAccSigCrcStatus sigCrcStatus
)
```

```text
Public Function FetchSigCrcStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef sigCrcStatus As RFmxWlanMXOfdmModAccSigCrcStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **sigCrcStatus**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccSigCrcStatus Upon return, contains whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/56508db9-eaaf-f375-9556-18dea9c969bd.htm language=enus -->
## TOPIC 00111: rfmxwlandotnet/html/56508db9-eaaf-f375-9556-18dea9c969bd.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/56508db9-eaaf-f375-9556-18dea9c969bd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/56508db9-eaaf-f375-9556-18dea9c969bd.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmPreamblePuncturingEnabled Method

RFmxWlanMXGetOfdmPreamblePuncturingEnabled Method

Gets whether the 802.11ax MU PPDU or the 802.11be MU PPDU signal is preamble punctured.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmPreamblePuncturingEnabled(
	string selectorString,
	out RFmxWlanMXOfdmPreamblePuncturingEnabled value
)
```

```text
Public Function GetOfdmPreamblePuncturingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmPreamblePuncturingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmPreamblePuncturingEnabledUpon return, contains whether the 802.11ax MU PPDU or the 802.11be MU PPDU signal is preamble punctured.

###### Return Value

Int32

##### Remarks

OfdmPreamblePuncturingEnabled

False

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5698e527-44f8-a068-e37e-db4e54cf7cfb.htm language=enus -->
## TOPIC 00112: rfmxwlandotnet/html/5698e527-44f8-a068-e37e-db4e54cf7cfb.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5698e527-44f8-a068-e37e-db4e54cf7cfb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5698e527-44f8-a068-e37e-db4e54cf7cfb.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.GetSweepTimeAuto Method

RFmxWlanMXSemConfigurationGetSweepTimeAuto Method

Gets whether the sweep time for the SEM measurement is computed automatically or is configured by you.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxWlanMXSemSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXSemSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemSweepTimeAutoUpon return, contains whether the sweep time for the SEM measurement is computed automatically or is configured by you.

###### Return Value

Int32

##### Remarks

SemSweepTimeAuto

True

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/56bab08d-488a-1055-7822-a25f0fe68d8b.htm language=enus -->
## TOPIC 00113: rfmxwlandotnet/html/56bab08d-488a-1055-7822-a25f0fe68d8b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/56bab08d-488a-1055-7822-a25f0fe68d8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/56bab08d-488a-1055-7822-a25f0fe68d8b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpConfiguration Methods

RFmxWlanMXTxpConfiguration Methods

The [RFmxWlanMXTxpConfiguration](5272ebae-3bce-b8fb-7306-a0d81a55603b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the measurement. |
|  | ConfigureBurstDetectionEnabled | Configures burst detection for the TXP measurement. |
|  | ConfigureMaximumMeasurementInterval | Configures the maximum measurement interval for the TXP measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXTxpAveragingEnabled) method to True . |
|  | GetAveragingEnabled | Gets whether to enable averaging for the TXP measurement. |
|  | GetBurstDetectionEnabled | Gets whether the measurement detects the start and the end of a WLAN packet automatically. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaximumMeasurementInterval | Gets the maximum measurement interval. This value is expressed in seconds. |
|  | GetMeasurementEnabled | Gets whether to enable the transmit power (TXP) measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for TXP measurement. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXTxpAveragingEnabled) method to True . |
|  | SetAveragingEnabled | Sets whether to enable averaging for the TXP measurement. |
|  | SetBurstDetectionEnabled | Sets whether the measurement detects the start and the end of a WLAN packet automatically. |
|  | SetMaximumMeasurementInterval | Sets the maximum measurement interval. This value is expressed in seconds. |
|  | SetMeasurementEnabled | Sets whether to enable the transmit power (TXP) measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for TXP measurement. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxWlanMXTxpConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/56cd406d-4b59-f7dd-02b2-1e0a2def8b18.htm language=enus -->
## TOPIC 00114: rfmxwlandotnet/html/56cd406d-4b59-f7dd-02b2-1e0a2def8b18.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/56cd406d-4b59-f7dd-02b2-1e0a2def8b18.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/56cd406d-4b59-f7dd-02b2-1e0a2def8b18.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetVhtSigBPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetVhtSigBPeakPowerMaximum Method

Gets the peak power of the VHT-SIG-B field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetVhtSigBPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetVhtSigBPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the VHT-SIG-B field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsVhtSigBPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/56cf1ac2-f0bd-d27d-6db7-fd8cae724315.htm language=enus -->
## TOPIC 00115: rfmxwlandotnet/html/56cf1ac2-f0bd-d27d-6db7-fd8cae724315.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/56cf1ac2-f0bd-d27d-6db7-fd8cae724315.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/56cf1ac2-f0bd-d27d-6db7-fd8cae724315.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetUpperOffsetMarginFrequency Method

RFmxWlanMXSemResultsGetUpperOffsetMarginFrequency Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetMarginFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetMarginFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the frequency of the spectrum corresponding to the result of the GetUpperOffsetMargin(String, Double) method. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMarginFrequency

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/56e053a7-bcfa-5ca6-3f65-807c543fee0b.htm language=enus -->
## TOPIC 00116: rfmxwlandotnet/html/56e053a7-bcfa-5ca6-3f65-807c543fee0b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/56e053a7-bcfa-5ca6-3f65-807c543fee0b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/56e053a7-bcfa-5ca6-3f65-807c543fee0b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetLSigParityCheckStatus Method

RFmxWlanMXOfdmModAccResultsGetLSigParityCheckStatus Method

Gets whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLSigParityCheckStatus(
	string selectorString,
	out RFmxWlanMXOfdmModAccLSigParityCheckStatus value
)
```

```text
Public Function GetLSigParityCheckStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccLSigParityCheckStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccLSigParityCheckStatusUpon return, contains whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsLSigParityCheckStatus

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5717ec3d-4d8a-d004-c9f7-00c5895dd933.htm language=enus -->
## TOPIC 00117: rfmxwlandotnet/html/5717ec3d-4d8a-d004-c9f7-00c5895dd933.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5717ec3d-4d8a-d004-c9f7-00c5895dd933.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5717ec3d-4d8a-d004-c9f7-00c5895dd933.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.GetAveragingEnabled Method

RFmxWlanMXSemConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the SEM measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxWlanMXSemAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXSemAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemAveragingEnabledUpon return, contains whether to enable averaging for the SEM measurement.

###### Return Value

Int32

##### Remarks

SemAveragingEnabled

False

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/575b3aa2-95f3-1a2c-e813-190030cbc957.htm language=enus -->
## TOPIC 00118: rfmxwlandotnet/html/575b3aa2-95f3-1a2c-e813-190030cbc957.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/575b3aa2-95f3-1a2c-e813-190030cbc957.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/575b3aa2-95f3-1a2c-e813-190030cbc957.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmFrequencyBand Method

RFmxWlanMXSetOfdmFrequencyBand Method

IEEE Standard 802.11n – 2009

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmFrequencyBand(
	string selectorString,
	RFmxWlanMXOfdmFrequencyBand value
)
```

```text
Public Function SetOfdmFrequencyBand ( 
	selectorString As String,
	value As RFmxWlanMXOfdmFrequencyBand
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmFrequencyBand Specifies the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 .

###### Return Value

Int32

##### Remarks

OfdmFrequencyBand

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/57b4aad5-cf21-9168-8e43-58eb689d921a.htm language=enus -->
## TOPIC 00119: rfmxwlandotnet/html/57b4aad5-cf21-9168-8e43-58eb689d921a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/57b4aad5-cf21-9168-8e43-58eb689d921a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/57b4aad5-cf21-9168-8e43-58eb689d921a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpResults.GetAveragePowerMean Method

RFmxWlanMXTxpResultsGetAveragePowerMean Method

Gets the average power of the acquired signal. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the acquired signal. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXTxpResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/57c69864-f3f5-3f5b-2b21-19cef38b4034.htm language=enus -->
## TOPIC 00120: rfmxwlandotnet/html/57c69864-f3f5-3f5b-2b21-19cef38b4034.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/57c69864-f3f5-3f5b-2b21-19cef38b4034.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/57c69864-f3f5-3f5b-2b21-19cef38b4034.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampConfiguration.GetAcquisitionLength Method

RFmxWlanMXPowerRampConfigurationGetAcquisitionLength Method

Gets the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAcquisitionLength(
	string selectorString,
	out double value
)
```

```text
Public Function GetAcquisitionLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PowerRampAcquisitionLength

##### See Also

###### Reference

RFmxWlanMXPowerRampConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/57d9cfaa-c5f2-cf3c-b07b-55a63ddcef69.htm language=enus -->
## TOPIC 00121: rfmxwlandotnet/html/57d9cfaa-c5f2-cf3c-b07b-55a63ddcef69.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/57d9cfaa-c5f2-cf3c-b07b-55a63ddcef69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/57d9cfaa-c5f2-cf3c-b07b-55a63ddcef69.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.FetchPpduInformation Method

RFmxWlanMXDsssModAccResultsFetchPpduInformation Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | FetchPpduInformation(String, Double, RFmxWlanMXDsssModAccDataModulationFormat, Int32, RFmxWlanMXDsssModAccPreambleType, Int32, RFmxWlanMXDsssModAccPayloadHeaderCrcStatus, RFmxWlanMXDsssModAccPsduCrcStatus) |  |
|  | FetchPpduInformation(String, Double, RFmxWlanMXDsssModAccDataModulationFormat, Int32, RFmxWlanMXDsssModAccPreambleType, Int32, Int32, Int32) | Obsolete. Fetches the PPDU information. |

Top

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/584048fd-5fdd-fe51-b7f0-7024f034c142.htm language=enus -->
## TOPIC 00122: rfmxwlandotnet/html/584048fd-5fdd-fe51-b7f0-7024f034c142.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/584048fd-5fdd-fe51-b7f0-7024f034c142.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/584048fd-5fdd-fe51-b7f0-7024f034c142.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetTriggerMinimumQuietTimeDuration Method

RFmxWlanMXSetTriggerMinimumQuietTimeDuration Method

Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/589e0b0e-0f9d-5583-e650-17e62fa009d6.htm language=enus -->
## TOPIC 00123: rfmxwlandotnet/html/589e0b0e-0f9d-5583-e650-17e62fa009d6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/589e0b0e-0f9d-5583-e650-17e62fa009d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/589e0b0e-0f9d-5583-e650-17e62fa009d6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmPreamblePuncturingBitmap Method

RFmxWlanMXSetOfdmPreamblePuncturingBitmap Method

The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit 

indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant 

bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps 

to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel 

in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU 

are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels 

of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing 

information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmPreamblePuncturingBitmap(
	string selectorString,
	long value
)
```

```text
Public Function SetOfdmPreamblePuncturingBitmap ( 
	selectorString As String,
	value As Long
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt64Specifies the punctured 20 MHz sub-channels in the 802.11ax MU PPDU or the 802.11be MU PPDU signal when preamble puncturing is enabled.

###### Return Value

Int32

##### Remarks

OfdmPreamblePuncturingBitmap

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/58dae736-1dd0-1a15-2b08-6cd9bd689799.htm language=enus -->
## TOPIC 00124: rfmxwlandotnet/html/58dae736-1dd0-1a15-2b08-6cd9bd689799.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/58dae736-1dd0-1a15-2b08-6cd9bd689799.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/58dae736-1dd0-1a15-2b08-6cd9bd689799.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration Class

RFmxWlanMXSemConfiguration Class

Provides methods to configure the SEM measurement.

##### Inheritance Hierarchy

RFmxWlanMXSubObject

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxWlanMXSemConfiguration : RFmxWlanMXSubObject
```

```text
Public NotInheritable Class RFmxWlanMXSemConfiguration
	Inherits RFmxWlanMXSubObject
```

The RFmxWlanMXSemConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the measurement. |
|  | ConfigureMaskType | Configures the mask type for the SEM measurement. |
|  | ConfigureNumberOfOffsets | Configures the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | ConfigureOffsetFrequencyArray | Configures the array of offset start and stop frequencies and specifies whether the offsets are present on one side, or on both the sides of the carrier when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | ConfigureOffsetRelativeLimitArray | Configures an array of relative mask limits corresponding the start and stop frequencies of the offsets when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . The relative limits are relative to the peak power of the carrier. |
|  | ConfigureSpan | Configures the frequency range around the center frequency to be acquired for the SEM measurement. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled) method to True . |
|  | GetAveragingEnabled | Gets whether to enable averaging for the SEM measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
|  | GetCarrierIntegrationBandwidth | Gets the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaskType | Gets whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
|  | GetMeasurementEnabled | Gets whether to enable the spectral emission mask (SEM) measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for SEM measurement. |
|  | GetNumberOfOffsets | Gets the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | GetOffsetRelativeLimitStart | Gets the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. |
|  | GetOffsetRelativeLimitStop | Gets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
|  | GetOffsetSideband | Gets whether the offset segment is present on one side or on both sides of the carrier. |
|  | GetOffsetStartFrequency | Gets the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | GetOffsetStopFrequency | Gets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |
|  | GetSpan | Gets the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz. |
|  | GetSpanAuto | Gets whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
|  | GetSweepTimeAuto | Gets whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
|  | GetSweepTimeInterval | Gets the sweep time for the SEM measurement. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled) method to True . |
|  | SetAveragingEnabled | Sets whether to enable averaging for the SEM measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
|  | SetMaskType | Sets whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
|  | SetMeasurementEnabled | Sets whether to enable the spectral emission mask (SEM) measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for SEM measurement. |
|  | SetNumberOfOffsets | Sets the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | SetOffsetRelativeLimitStart | Sets the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. |
|  | SetOffsetRelativeLimitStop | Sets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
|  | SetOffsetSideband | Sets whether the offset segment is present on one side or on both sides of the carrier. |
|  | SetOffsetStartFrequency | Sets the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | SetOffsetStopFrequency | Sets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |
|  | SetSpan | Sets the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz. |
|  | SetSpanAuto | Sets whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
|  | SetSweepTimeAuto | Sets whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
|  | SetSweepTimeInterval | Sets the sweep time for the SEM measurement. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/58ded265-cba7-59ad-e4ab-809f44e416d5.htm language=enus -->
## TOPIC 00125: rfmxwlandotnet/html/58ded265-cba7-59ad-e4ab-809f44e416d5.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/58ded265-cba7-59ad-e4ab-809f44e416d5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/58ded265-cba7-59ad-e4ab-809f44e416d5.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetChainDataRmsEvmMean Method

RFmxWlanMXOfdmModAccResultsGetChainDataRmsEvmMean Method

Gets the chain RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChainDataRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetChainDataRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the chain RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsChainDataRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/590e28b2-3d09-7930-a7ed-1fb71914c326.htm language=enus -->
## TOPIC 00126: rfmxwlandotnet/html/590e28b2-3d09-7930-a7ed-1fb71914c326.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/590e28b2-3d09-7930-a7ed-1fb71914c326.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/590e28b2-3d09-7930-a7ed-1fb71914c326.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.ConfigureStandard Method

RFmxWlanMXConfigureStandard Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureStandard(
	string selectorString,
	RFmxWlanMXStandard standard
)
```

```text
Public Function ConfigureStandard ( 
	selectorString As String,
	standard As RFmxWlanMXStandard
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **standard**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXStandard Specifies the signal under analysis as defined under IEEE Standard 802.11 . On a MIMO session, the supported standards are 802.11n, 802.11ac, 802.11ax, and 802.11be.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5967366e-7559-79a4-16ef-8614d0622ac5.htm language=enus -->
## TOPIC 00127: rfmxwlandotnet/html/5967366e-7559-79a4-16ef-8614d0622ac5.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5967366e-7559-79a4-16ef-8614d0622ac5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5967366e-7559-79a4-16ef-8614d0622ac5.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmMUMimoLtfModeEnabled Method

RFmxWlanMXSetOfdmMUMimoLtfModeEnabled Method

Sets whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmMUMimoLtfModeEnabled(
	string selectorString,
	RFmxWlanMXOfdmMUMimoLtfModeEnabled value
)
```

```text
Public Function SetOfdmMUMimoLtfModeEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmMUMimoLtfModeEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmMUMimoLtfModeEnabledSpecifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code.

###### Return Value

Int32

##### Remarks

OfdmMUMimoLtfModeEnabled

False

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/597a82f1-18a5-3186-a071-15c38b42bfdb.htm language=enus -->
## TOPIC 00128: rfmxwlandotnet/html/597a82f1-18a5-3186-a071-15c38b42bfdb.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/597a82f1-18a5-3186-a071-15c38b42bfdb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/597a82f1-18a5-3186-a071-15c38b42bfdb.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.FetchMeasurementStatus Method

RFmxWlanMXSemResultsFetchMeasurementStatus Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurementStatus(
	string selectorString,
	double timeout,
	out RFmxWlanMXSemMeasurementStatus measurementStatus
)
```

```text
Public Function FetchMeasurementStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxWlanMXSemMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **measurementStatus**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemMeasurementStatus Upon return, contains the overall measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/598b7b11-a779-a3d2-b34b-408fe888cba9.htm language=enus -->
## TOPIC 00129: rfmxwlandotnet/html/598b7b11-a779-a3d2-b34b-408fe888cba9.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/598b7b11-a779-a3d2-b34b-408fe888cba9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/598b7b11-a779-a3d2-b34b-408fe888cba9.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.CheckMeasurementStatus Method

RFmxWlanMXCheckMeasurementStatus Method

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **isDone**
  - Type: SystemBooleanIndicates whether the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/59a9b81a-2077-252d-b3fa-c3ae4a791c11.htm language=enus -->
## TOPIC 00130: rfmxwlandotnet/html/59a9b81a-2077-252d-b3fa-c3ae4a791c11.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/59a9b81a-2077-252d-b3fa-c3ae4a791c11.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/59a9b81a-2077-252d-b3fa-c3ae4a791c11.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccChannelEstimationInterpolationType Enumeration

RFmxWlanMXOfdmModAccChannelEstimationInterpolationType Enumeration

Specifies the interpolation type and/or smoothing type used on the channel estimates.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccChannelEstimationInterpolationType
```

```text
Public Enumeration RFmxWlanMXOfdmModAccChannelEstimationInterpolationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Linear | 0 | Linear interpolation is performed on reference channel estimates across subcarriers. |
|  | TriangularSmoothing | 1 | Channel estimates are smoothed using a triangular weighted moving average window across subcarriers. |
|  | WienerFilter | 2 | Wiener filter is used for interpolation and smoothing on reference channel estimates across subcarriers. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/59e131f6-bc52-dff9-1887-e8ef49e3e640.htm language=enus -->
## TOPIC 00131: rfmxwlandotnet/html/59e131f6-bc52-dff9-1887-e8ef49e3e640.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/59e131f6-bc52-dff9-1887-e8ef49e3e640.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/59e131f6-bc52-dff9-1887-e8ef49e3e640.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetRmsEvmMean Method

RFmxWlanMXDsssModAccResultsGetRmsEvmMean Method

Gets the RMS EVM of the burst. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS EVM of the burst. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

DsssModAccResultsRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5a794bd2-2f4c-0715-b19f-3563fde8ca58.htm language=enus -->
## TOPIC 00132: rfmxwlandotnet/html/5a794bd2-2f4c-0715-b19f-3563fde8ca58.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5a794bd2-2f4c-0715-b19f-3563fde8ca58.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5a794bd2-2f4c-0715-b19f-3563fde8ca58.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.BuildUserString Method

RFmxWlanMXBuildUserString Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildUserString(
	string selectorString,
	int userNumber
)
```

```text
Public Shared Function BuildUserString ( 
	selectorString As String,
	userNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **userNumber**
  - Type: SystemInt32 Specifies the user number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5a8985ae-7bc5-aa19-b98a-51e562e1cf30.htm language=enus -->
## TOPIC 00133: rfmxwlandotnet/html/5a8985ae-7bc5-aa19-b98a-51e562e1cf30.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5a8985ae-7bc5-aa19-b98a-51e562e1cf30.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5a8985ae-7bc5-aa19-b98a-51e562e1cf30.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetCustomGatePeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetCustomGatePeakPowerMaximum Method

Gets the peak power of the custom gate. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCustomGatePeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetCustomGatePeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the custom gate. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsCustomGatePeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5c996ed8-a0ad-13e7-6de9-101f73eac2b8.htm language=enus -->
## TOPIC 00134: rfmxwlandotnet/html/5c996ed8-a0ad-13e7-6de9-101f73eac2b8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5c996ed8-a0ad-13e7-6de9-101f73eac2b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5c996ed8-a0ad-13e7-6de9-101f73eac2b8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetIQGainImbalanceMean Method

RFmxWlanMXDsssModAccResultsGetIQGainImbalanceMean Method

Gets the I/Q gain imbalance. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQGainImbalanceMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQGainImbalanceMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the I/Q gain imbalance. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

DsssModAccResultsIQGainImbalanceMean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5e95a86a-d424-81e1-558c-8365f9aa2bf2.htm language=enus -->
## TOPIC 00135: rfmxwlandotnet/html/5e95a86a-d424-81e1-558c-8365f9aa2bf2.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5e95a86a-d424-81e1-558c-8365f9aa2bf2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5e95a86a-d424-81e1-558c-8365f9aa2bf2.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetPowerNumberOfCustomGates Method

RFmxWlanMXOfdmModAccConfigurationSetPowerNumberOfCustomGates Method

Sets the number of custom gates for power measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPowerNumberOfCustomGates(
	string selectorString,
	int value
)
```

```text
Public Function SetPowerNumberOfCustomGates ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the number of custom gates for power measurement.

###### Return Value

Int32

##### Remarks

OfdmModAccPowerNumberOfCustomGates

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/5f9d1582-7d53-642b-3ecd-dc31cacfc5be.htm language=enus -->
## TOPIC 00136: rfmxwlandotnet/html/5f9d1582-7d53-642b-3ecd-dc31cacfc5be.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/5f9d1582-7d53-642b-3ecd-dc31cacfc5be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/5f9d1582-7d53-642b-3ecd-dc31cacfc5be.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetNumberOfOffsets Method

RFmxWlanMXSemConfigurationSetNumberOfOffsets Method

SetMaskType(String, RFmxWlanMXSemMaskType)

Custom

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom .

###### Return Value

Int32

##### Remarks

SemNumberOfOffsets

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/60c0a5f9-171d-f38c-19c0-5403a0101d47.htm language=enus -->
## TOPIC 00137: rfmxwlandotnet/html/60c0a5f9-171d-f38c-19c0-5403a0101d47.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/60c0a5f9-171d-f38c-19c0-5403a0101d47.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/60c0a5f9-171d-f38c-19c0-5403a0101d47.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.SetPowerNumberOfCustomGates Method

RFmxWlanMXDsssModAccConfigurationSetPowerNumberOfCustomGates Method

Sets the number of custom gates used for power measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPowerNumberOfCustomGates(
	string selectorString,
	int value
)
```

```text
Public Function SetPowerNumberOfCustomGates ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the number of custom gates used for power measurement.

###### Return Value

Int32

##### Remarks

DsssModAccPowerNumberOfCustomGates

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6382b986-a8e0-46e0-ad2d-9beed90405e0.htm language=enus -->
## TOPIC 00138: rfmxwlandotnet/html/6382b986-a8e0-46e0-ad2d-9beed90405e0.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6382b986-a8e0-46e0-ad2d-9beed90405e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6382b986-a8e0-46e0-ad2d-9beed90405e0.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchDecodedSigBitsTrace Method

RFmxWlanMXOfdmModAccResultsFetchDecodedSigBitsTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDecodedSigBitsTrace(
	string selectorString,
	double timeout,
	ref int[] decodedSigBits
)
```

```text
Public Function FetchDecodedSigBitsTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef decodedSigBits As Integer()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **decodedSigBits**
  - Type: SystemInt32 Upon return, contains an array of bits in the HT-SIG field of the 802.11n waveform, the VHT-SIG-A field of the 802.11ac waveform, or the HE-SIG-A field of the 802.11ax waveform.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/67097b93-d80e-b898-c926-43ac9a61643f.htm language=enus -->
## TOPIC 00139: rfmxwlandotnet/html/67097b93-d80e-b898-c926-43ac9a61643f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/67097b93-d80e-b898-c926-43ac9a61643f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/67097b93-d80e-b898-c926-43ac9a61643f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetAllTracesEnabled Method

RFmxWlanMXOfdmModAccConfigurationSetAllTracesEnabled Method

Sets whether to enable all the traces computed by the OFDMModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanSpecifies whether to enable all the traces computed by the OFDMModAcc measurement.

###### Return Value

Int32

##### Remarks

OfdmModAccAllTracesEnabled

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/67ad2199-ee9f-1514-30c8-326e858e8c27.htm language=enus -->
## TOPIC 00140: rfmxwlandotnet/html/67ad2199-ee9f-1514-30c8-326e858e8c27.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/67ad2199-ee9f-1514-30c8-326e858e8c27.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/67ad2199-ee9f-1514-30c8-326e858e8c27.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchNumberOfHESigBSymbols Method

RFmxWlanMXOfdmModAccResultsFetchNumberOfHESigBSymbols Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchNumberOfHESigBSymbols(
	string selectorString,
	double timeout,
	out int numberOfHESigBSymbols
)
```

```text
Public Function FetchNumberOfHESigBSymbols ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef numberOfHESigBSymbols As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **numberOfHESigBSymbols**
  - Type: SystemInt32 Upon return, contains the number of HE-SIG-B symbols. This result is applicable for 802.11ax MU PPDU signals, and is decoded from the HE-SIG-A field.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/684cd949-a2b2-dff9-1db5-dcb0af2962b7.htm language=enus -->
## TOPIC 00141: rfmxwlandotnet/html/684cd949-a2b2-dff9-1db5-dcb0af2962b7.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/684cd949-a2b2-dff9-1db5-dcb0af2962b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/684cd949-a2b2-dff9-1db5-dcb0af2962b7.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetChainPilotRmsEvmMean Method

RFmxWlanMXOfdmModAccResultsGetChainPilotRmsEvmMean Method

Gets the chain RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChainPilotRmsEvmMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetChainPilotRmsEvmMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the chain RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsChainPilotRmsEvmMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/689a50ab-9e2b-b427-8ad6-334809ba0476.htm language=enus -->
## TOPIC 00142: rfmxwlandotnet/html/689a50ab-9e2b-b427-8ad6-334809ba0476.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/689a50ab-9e2b-b427-8ad6-334809ba0476.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/689a50ab-9e2b-b427-8ad6-334809ba0476.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmPreamblePuncturingBitmap Method

RFmxWlanMXGetOfdmPreamblePuncturingBitmap Method

The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit 

indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant 

bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps 

to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel 

in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU 

are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels 

of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing 

information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmPreamblePuncturingBitmap(
	string selectorString,
	out long value
)
```

```text
Public Function GetOfdmPreamblePuncturingBitmap ( 
	selectorString As String,
	<OutAttribute> ByRef value As Long
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt64Upon return, contains the punctured 20 MHz sub-channels in the 802.11ax MU PPDU or the 802.11be MU PPDU signal when preamble puncturing is enabled.

###### Return Value

Int32

##### Remarks

OfdmPreamblePuncturingBitmap

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/69ca0b7d-4315-20f0-7712-a35c15737516.htm language=enus -->
## TOPIC 00143: rfmxwlandotnet/html/69ca0b7d-4315-20f0-7712-a35c15737516.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/69ca0b7d-4315-20f0-7712-a35c15737516.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/69ca0b7d-4315-20f0-7712-a35c15737516.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetPpduPeakPowerMaximum Method

RFmxWlanMXDsssModAccResultsGetPpduPeakPowerMaximum Method

Gets the peak power of the PPDU. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPpduPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPpduPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the PPDU. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

DsssModAccResultsPpduPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6a54e309-795b-15a2-4abb-3d8d032318e6.htm language=enus -->
## TOPIC 00144: rfmxwlandotnet/html/6a54e309-795b-15a2-4abb-3d8d032318e6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6a54e309-795b-15a2-4abb-3d8d032318e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6a54e309-795b-15a2-4abb-3d8d032318e6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.FetchUpperOffsetPowerArray Method

RFmxWlanMXSemResultsFetchUpperOffsetPowerArray Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUpperOffsetPowerArray(
	string selectorString,
	double timeout,
	ref double[] totalAbsolutePower,
	ref double[] totalRelativePower,
	ref double[] peakAbsolutePower,
	ref double[] peakFrequency,
	ref double[] peakRelativePower
)
```

```text
Public Function FetchUpperOffsetPowerArray ( 
	selectorString As String,
	timeout As Double,
	ByRef totalAbsolutePower As Double(),
	ByRef totalRelativePower As Double(),
	ByRef peakAbsolutePower As Double(),
	ByRef peakFrequency As Double(),
	ByRef peakRelativePower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **totalAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of average powers of the upper offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm.
- **totalRelativePower**
  - Type: SystemDouble Upon return, contains an array of average powers of the upper offsets relative to the peak power of the carrier channel. This value is expressed in dB.
- **peakAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of peak powers of the upper offsets. This value is expressed in dBm.
- **peakFrequency**
  - Type: SystemDouble Upon return, contains an array of frequencies at which the peak power occurs in the upper offsets. This value is expressed in Hz.
- **peakRelativePower**
  - Type: SystemDouble Upon return, contains an array of peak powers of the upper offsets, relative to the peak power of the carrier channel. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6a5590cf-74eb-b283-ab0c-dc3d87ccd783.htm language=enus -->
## TOPIC 00145: rfmxwlandotnet/html/6a5590cf-74eb-b283-ab0c-dc3d87ccd783.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6a5590cf-74eb-b283-ab0c-dc3d87ccd783.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6a5590cf-74eb-b283-ab0c-dc3d87ccd783.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemMaskType Enumeration

RFmxWlanMXSemMaskType Enumeration

Specifies whether the mask used for the SEM measurement is defined either as per the standard or as specified by you.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXSemMaskType
```

```text
Public Enumeration RFmxWlanMXSemMaskType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Standard | 0 | Mask limits are configured as per the specified standard, channel bandwidth, and band. |
|  | Custom | 1 | The measurement uses the mask limits that you specify. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6aad040a-d3c6-c347-dd5e-69ceca6f2778.htm language=enus -->
## TOPIC 00146: rfmxwlandotnet/html/6aad040a-d3c6-c347-dd5e-69ceca6f2778.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6aad040a-d3c6-c347-dd5e-69ceca6f2778.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6aad040a-d3c6-c347-dd5e-69ceca6f2778.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.ConfigureFrequency Method

RFmxWlanMXConfigureFrequency Method

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies a selector string comprising of segment number. Example: "segment0" You can use the BuildChainString(String, Int32) method to build the selector string. If number of segments is greater than 1, you can use the BuildSegmentString(String, Int32) method to build the selector string.
- **centerFrequency**
  - Type: SystemDouble Specifies the center frequency. This value is expressed in Hz. The default of this method is hardware dependent.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6b718be7-ee5d-2acd-eb9c-9d741e4acea3.htm language=enus -->
## TOPIC 00147: rfmxwlandotnet/html/6b718be7-ee5d-2acd-eb9c-9d741e4acea3.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6b718be7-ee5d-2acd-eb9c-9d741e4acea3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6b718be7-ee5d-2acd-eb9c-9d741e4acea3.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.ConfigureCommonClockSourceEnabled Method

RFmxWlanMXOfdmModAccConfigurationConfigureCommonClockSourceEnabled Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCommonClockSourceEnabled(
	string selectorString,
	RFmxWlanMXOfdmModAccCommonClockSourceEnabled commonClockSourceEnabled
)
```

```text
Public Function ConfigureCommonClockSourceEnabled ( 
	selectorString As String,
	commonClockSourceEnabled As RFmxWlanMXOfdmModAccCommonClockSourceEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **commonClockSourceEnabled**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccCommonClockSourceEnabledSpecifies if the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6b94302b-0a60-d9ae-9a68-99a769c1e641.htm language=enus -->
## TOPIC 00148: rfmxwlandotnet/html/6b94302b-0a60-d9ae-9a68-99a769c1e641.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6b94302b-0a60-d9ae-9a68-99a769c1e641.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6b94302b-0a60-d9ae-9a68-99a769c1e641.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetIQGainImbalanceCorrectionEnabled Method

RFmxWlanMXOfdmModAccConfigurationSetIQGainImbalanceCorrectionEnabled Method

Sets whether to enable I/Q gain imbalance correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQGainImbalanceCorrectionEnabled(
	string selectorString,
	RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled value
)
```

```text
Public Function SetIQGainImbalanceCorrectionEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabledSpecifies whether to enable I/Q gain imbalance correction.

###### Return Value

Int32

##### Remarks

OfdmModAccIQGainImbalanceCorrectionEnabled

False

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/6e1dc404-6a45-6e72-d88a-9b1584990fc8.htm language=enus -->
## TOPIC 00149: rfmxwlandotnet/html/6e1dc404-6a45-6e72-d88a-9b1584990fc8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/6e1dc404-6a45-6e72-d88a-9b1584990fc8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/6e1dc404-6a45-6e72-d88a-9b1584990fc8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetLLtfAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetLLtfAveragePowerMean Method

Gets the average power of the L-LTF or LTF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLLtfAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetLLtfAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the L-LTF or LTF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsLLtfAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/72addfdb-4f09-ff72-4b0c-6bde356cc75c.htm language=enus -->
## TOPIC 00150: rfmxwlandotnet/html/72addfdb-4f09-ff72-4b0c-6bde356cc75c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/72addfdb-4f09-ff72-4b0c-6bde356cc75c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/72addfdb-4f09-ff72-4b0c-6bde356cc75c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetRmsCommonPilotErrorMean Method

RFmxWlanMXOfdmModAccResultsGetRmsCommonPilotErrorMean Method

Gets the RMS common pilot error. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsCommonPilotErrorMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsCommonPilotErrorMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS common pilot error. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsRmsCommonPilotErrorMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/733b469b-92ba-4f8e-90f0-075da29fdffc.htm language=enus -->
## TOPIC 00151: rfmxwlandotnet/html/733b469b-92ba-4f8e-90f0-075da29fdffc.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/733b469b-92ba-4f8e-90f0-075da29fdffc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/733b469b-92ba-4f8e-90f0-075da29fdffc.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetPulseShapingFilterParameter Method

RFmxWlanMXDsssModAccConfigurationGetPulseShapingFilterParameter Method

Gets the value of the filter roll-off when you set the Pulse Shaping Filter Type method to Raised Cosine or Root Raised Cosine. This method is ignored if you set the Pulse Shaping Filter Type method to Rectangular.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseShapingFilterParameter(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseShapingFilterParameter ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the value of the filter roll-off when you set the Pulse Shaping Filter Type method to Raised Cosine or Root Raised Cosine. This method is ignored if you set the Pulse Shaping Filter Type method to Rectangular.

###### Return Value

Int32

##### Remarks

DsssModAccPulseShapingFilterParameter

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/73c40273-5680-e7dc-3a04-493eafa41b79.htm language=enus -->
## TOPIC 00152: rfmxwlandotnet/html/73c40273-5680-e7dc-3a04-493eafa41b79.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/73c40273-5680-e7dc-3a04-493eafa41b79.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/73c40273-5680-e7dc-3a04-493eafa41b79.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmPpduType Enumeration

RFmxWlanMXOfdmPpduType Enumeration

SetOfdmAutoPpduTypeDetectionEnabled(String, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled)

False

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmPpduType
```

```text
Public Enumeration RFmxWlanMXOfdmPpduType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | NonHT | 0 | Specifies an 802.11a, 802.11j, or 802.11p PPDU type, or 802.11n, 802.11ac, or 802.11ax PPDU type when operating in the Non-HT mode. |
|  | Mixed | 1 | Specifies the HT-Mixed PPDU (802.11n) type. |
|  | Greenfield | 2 | Specifies the HT-Greenfield PPDU (802.11n) type. |
|  | SU | 3 | Specifies the VHT SU PPDU type if you set the SetStandard(String, RFmxWlanMXStandard) method to Standard802_11ac or the HE SU PPDU type if you set the Standard method to Standard802_11ax . |
|  | MU | 4 | Specifies the VHT MU PPDU type if you set the Standard method to Standard802_11ac , the HE MU PPDU type if you set the Standard method to Standard802_11ax , or the EHT MU PPDU type if you set the Standard method to Standard802_11be . |
|  | ExtendedRangeSU | 5 | Specifies the HE Extended Range SU PPDU (802.11ax) type. |
|  | TriggerBased | 6 | Specifies the HE TB PPDU if you set the Standard method to Standard802_11ax or the EHT TB PPDU if you set the Standard method to Standard802_11be . |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/73c6c1c9-5a36-8cc8-ab3f-890865a542e6.htm language=enus -->
## TOPIC 00153: rfmxwlandotnet/html/73c6c1c9-5a36-8cc8-ab3f-890865a542e6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/73c6c1c9-5a36-8cc8-ab3f-890865a542e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/73c6c1c9-5a36-8cc8-ab3f-890865a542e6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.SetNumberOfAnalysisThreads Method

RFmxWlanMXDsssModAccConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for DSSSModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemInt32Specifies the maximum number of threads used for parallelism for DSSSModAcc measurement.

###### Return Value

Int32

##### Remarks

DsssModAccNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/748e5a33-f9d9-ef2c-f303-3bfe426a2f11.htm language=enus -->
## TOPIC 00154: rfmxwlandotnet/html/748e5a33-f9d9-ef2c-f303-3bfe426a2f11.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/748e5a33-f9d9-ef2c-f303-3bfe426a2f11.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/748e5a33-f9d9-ef2c-f303-3bfe426a2f11.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccPsduCrcStatus Enumeration

RFmxWlanMXDsssModAccPsduCrcStatus Enumeration

Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXDsssModAccPsduCrcStatus
```

```text
Public Enumeration RFmxWlanMXDsssModAccPsduCrcStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 |  |
|  | Pass | 1 |  |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/756d602a-446e-f4e3-5158-6591fc5cbe3f.htm language=enus -->
## TOPIC 00155: rfmxwlandotnet/html/756d602a-446e-f4e3-5158-6591fc5cbe3f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/756d602a-446e-f4e3-5158-6591fc5cbe3f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/756d602a-446e-f4e3-5158-6591fc5cbe3f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetChannelEstimationRelativeDelaySpread Method

RFmxWlanMXOfdmModAccConfigurationGetChannelEstimationRelativeDelaySpread Method

Gets the expected channel delay spread relative to the OFDM symbol length.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChannelEstimationRelativeDelaySpread(
	string selectorString,
	out double value
)
```

```text
Public Function GetChannelEstimationRelativeDelaySpread ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the expected channel delay spread relative to the OFDM symbol length.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/757237b1-a73d-8129-4d03-70ab81a185e4.htm language=enus -->
## TOPIC 00156: rfmxwlandotnet/html/757237b1-a73d-8129-4d03-70ab81a185e4.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/757237b1-a73d-8129-4d03-70ab81a185e4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/757237b1-a73d-8129-4d03-70ab81a185e4.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetLowerOffsetMarginRelativePower Method

RFmxWlanMXSemResultsGetLowerOffsetMarginRelativePower Method

Namespace:

NationalInstruments.RFmx.WlanMX

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

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the power level of the spectrum corresponding to the result of the GetLowerOffsetMargin(String, Double) method. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetMarginRelativePower

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/774e5a8c-d12c-b01e-d2eb-da80b7e90c5b.htm language=enus -->
## TOPIC 00157: rfmxwlandotnet/html/774e5a8c-d12c-b01e-d2eb-da80b7e90c5b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/774e5a8c-d12c-b01e-d2eb-da80b7e90c5b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/774e5a8c-d12c-b01e-d2eb-da80b7e90c5b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetTriggerDelay Method

RFmxWlanMXGetTriggerDelay Method

Gets the trigger delay time. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemDoubleUpon return, contains the trigger delay time. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TriggerDelay

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/78b320e9-c569-ac3a-b611-744fe6f8a690.htm language=enus -->
## TOPIC 00158: rfmxwlandotnet/html/78b320e9-c569-ac3a-b611-744fe6f8a690.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/78b320e9-c569-ac3a-b611-744fe6f8a690.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/78b320e9-c569-ac3a-b611-744fe6f8a690.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetIQPowerEdgeTriggerSlope Method

RFmxWlanMXSetIQPowerEdgeTriggerSlope Method

Sets whether the device asserts the trigger when the signal power is rising or falling.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerSlope(
	string selectorString,
	RFmxWlanMXIQPowerEdgeTriggerSlope value
)
```

```text
Public Function SetIQPowerEdgeTriggerSlope ( 
	selectorString As String,
	value As RFmxWlanMXIQPowerEdgeTriggerSlope
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXIQPowerEdgeTriggerSlopeSpecifies whether the device asserts the trigger when the signal power is rising or falling.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSlope

Rising

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/78eac535-abd2-45a0-89e2-82618246e736.htm language=enus -->
## TOPIC 00159: rfmxwlandotnet/html/78eac535-abd2-45a0-89e2-82618246e736.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/78eac535-abd2-45a0-89e2-82618246e736.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/78eac535-abd2-45a0-89e2-82618246e736.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXConstants.PxiTriggerLine4 Field

RFmxWlanMXConstantsPxiTriggerLine4 Field

The signal is exported to the PXI trigger line 4.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMXConstants Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/78eb8245-6fc2-c8a8-e786-5dd75f0fcb7f.htm language=enus -->
## TOPIC 00160: rfmxwlandotnet/html/78eb8245-6fc2-c8a8-e786-5dd75f0fcb7f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/78eb8245-6fc2-c8a8-e786-5dd75f0fcb7f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/78eb8245-6fc2-c8a8-e786-5dd75f0fcb7f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.ConfigureEvmUnit Method

RFmxWlanMXOfdmModAccConfigurationConfigureEvmUnit Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureEvmUnit(
	string selectorString,
	RFmxWlanMXOfdmModAccEvmUnit evmUnit
)
```

```text
Public Function ConfigureEvmUnit ( 
	selectorString As String,
	evmUnit As RFmxWlanMXOfdmModAccEvmUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **evmUnit**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccEvmUnitSpecifies the unit for the EVM results.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/796357bf-c3ab-c1cf-a679-da0c6fd79f11.htm language=enus -->
## TOPIC 00161: rfmxwlandotnet/html/796357bf-c3ab-c1cf-a679-da0c6fd79f11.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/796357bf-c3ab-c1cf-a679-da0c6fd79f11.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/796357bf-c3ab-c1cf-a679-da0c6fd79f11.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetUpperOffsetRelativePeakPower Method

RFmxWlanMXSemResultsGetUpperOffsetRelativePeakPower Method

Gets the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

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

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetRelativePeakPower

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/7f59145e-f199-5d36-9225-34e9921604b6.htm language=enus -->
## TOPIC 00162: rfmxwlandotnet/html/7f59145e-f199-5d36-9225-34e9921604b6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/7f59145e-f199-5d36-9225-34e9921604b6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/7f59145e-f199-5d36-9225-34e9921604b6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXExtension Methods

RFmxWlanMXExtension Methods

The [RFmxWlanMXExtension](8700fb87-ea3c-68ad-ea88-7ef1adc4e291.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetWlanSignalConfiguration(RFmxInstrMX) | Creates a new default WLAN signal configuration if it doesn't exist; otherwise, it returns the existing default WLAN signal configuration. |
|  | GetWlanSignalConfiguration(RFmxInstrMX, String) | Creates a WLAN signal configuration for specified signal name. Existing WLAN signal configuration is returned if specified signal name exists. |
|  | WlanOfdmModAccClearNoiseCalibrationDatabase | Clears the noise calibration database used for EVM noise compensation. |

Top

##### See Also

###### Reference

RFmxWlanMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/7f91c94a-a508-4b9b-e114-91862a89ae07.htm language=enus -->
## TOPIC 00163: rfmxwlandotnet/html/7f91c94a-a508-4b9b-e114-91862a89ae07.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/7f91c94a-a508-4b9b-e114-91862a89ae07.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/7f91c94a-a508-4b9b-e114-91862a89ae07.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpConfiguration.SetMeasurementEnabled Method

RFmxWlanMXTxpConfigurationSetMeasurementEnabled Method

Sets whether to enable the transmit power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanSpecifies whether to enable the transmit power (TXP) measurement.

###### Return Value

Int32

##### Remarks

TxpMeasurementEnabled

##### See Also

###### Reference

RFmxWlanMXTxpConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/7fbed1a6-2873-e884-fc15-2b001e371435.htm language=enus -->
## TOPIC 00164: rfmxwlandotnet/html/7fbed1a6-2873-e884-fc15-2b001e371435.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/7fbed1a6-2873-e884-fc15-2b001e371435.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/7fbed1a6-2873-e884-fc15-2b001e371435.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.ConfigureOffsetFrequencyArray Method

RFmxWlanMXSemConfigurationConfigureOffsetFrequencyArray Method

SetMaskType(String, RFmxWlanMXSemMaskType)

Custom

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetFrequencyArray(
	string selectorString,
	double[] offsetStartFrequency,
	double[] offsetStopFrequency,
	RFmxWlanMXSemOffsetSideband[] offsetSideband
)
```

```text
Public Function ConfigureOffsetFrequencyArray ( 
	selectorString As String,
	offsetStartFrequency As Double(),
	offsetStopFrequency As Double(),
	offsetSideband As RFmxWlanMXSemOffsetSideband()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetStartFrequency**
  - Type: SystemDoubleSpecifies the array of offset start frequencies, relative to the carrier frequency. This value is expressed in Hz.
- **offsetStopFrequency**
  - Type: SystemDoubleSpecifies the array of offset stop frequencies, relative to the carrier frequency. This value is expressed in Hz.
- **offsetSideband**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemOffsetSidebandSpecifies whether the offset segments present on one or both sides of the carrier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/80cae52a-a218-db2b-b10e-f8ae8545748f.htm language=enus -->
## TOPIC 00165: rfmxwlandotnet/html/80cae52a-a218-db2b-b10e-f8ae8545748f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/80cae52a-a218-db2b-b10e-f8ae8545748f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/80cae52a-a218-db2b-b10e-f8ae8545748f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccPsduCrcStaus Enumeration

RFmxWlanMXDsssModAccPsduCrcStaus Enumeration

Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXDsssModAccPsduCrcStaus
```

```text
Public Enumeration RFmxWlanMXDsssModAccPsduCrcStaus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 | Indicates that the PSDU CRC failed. |
|  | Pass | 1 | Indicates that the PSDU CRC passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/80cc4542-89dc-5c76-2544-319a6523dc5a.htm language=enus -->
## TOPIC 00166: rfmxwlandotnet/html/80cc4542-89dc-5c76-2544-319a6523dc5a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/80cc4542-89dc-5c76-2544-319a6523dc5a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/80cc4542-89dc-5c76-2544-319a6523dc5a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxp Class

RFmxWlanMXTxp Class

Represents the TXP measurement.

##### Inheritance Hierarchy

RFmxWlanMXSubObject

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxWlanMXTxp : RFmxWlanMXSubObject
```

```text
Public NotInheritable Class RFmxWlanMXTxp
	Inherits RFmxWlanMXSubObject
```

The RFmxWlanMXTxp type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxWlanMXTxpConfiguration instance that provides methods to configure the TXP measurement. |
|  | Results | Gets the RFmxWlanMXTxpResults instance that provides methods to fetch and read the TXP measurement results. |

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

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/8359275e-39cb-86d7-4535-3d595fda0295.htm language=enus -->
## TOPIC 00167: rfmxwlandotnet/html/8359275e-39cb-86d7-4535-3d595fda0295.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/8359275e-39cb-86d7-4535-3d595fda0295.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/8359275e-39cb-86d7-4535-3d595fda0295.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.FetchCarrierMeasurement Method

RFmxWlanMXSemResultsFetchCarrierMeasurement Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurement(
	string selectorString,
	double timeout,
	out double absolutePower,
	out double relativePower
)
```

```text
Public Function FetchCarrierMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef absolutePower As Double,
	<OutAttribute> ByRef relativePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **absolutePower**
  - Type: SystemDouble Upon return, contains the average power of the carrier channel over the bandwidth indicated by the GetCarrierIntegrationBandwidth(String, Double) method. This value is expressed in dBm.
- **relativePower**
  - Type: SystemDouble Upon return, contains the average power of the carrier channel, relative to the peak power of the carrier channel, over the bandwidth indicated by the SEM Carrier IBW method. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/8450a1d7-9ea9-0556-1a94-fcd7b01892bb.htm language=enus -->
## TOPIC 00168: rfmxwlandotnet/html/8450a1d7-9ea9-0556-1a94-fcd7b01892bb.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/8450a1d7-9ea9-0556-1a94-fcd7b01892bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/8450a1d7-9ea9-0556-1a94-fcd7b01892bb.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRamp.Configuration Property

RFmxWlanMXPowerRampConfiguration Property

RFmxWlanMXPowerRampConfiguration

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXPowerRampConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxWlanMXPowerRampConfiguration
	Get
```

###### Property Value

RFmxWlanMXPowerRampConfiguration

##### See Also

###### Reference

RFmxWlanMXPowerRamp Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/845a5c37-87d6-f594-f179-e7d1152f9936.htm language=enus -->
## TOPIC 00169: rfmxwlandotnet/html/845a5c37-87d6-f594-f179-e7d1152f9936.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/845a5c37-87d6-f594-f179-e7d1152f9936.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/845a5c37-87d6-f594-f179-e7d1152f9936.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpConfiguration.ConfigureMaximumMeasurementInterval Method

RFmxWlanMXTxpConfigurationConfigureMaximumMeasurementInterval Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMaximumMeasurementInterval(
	string selectorString,
	double maximumMeasurementInterval
)
```

```text
Public Function ConfigureMaximumMeasurementInterval ( 
	selectorString As String,
	maximumMeasurementInterval As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **maximumMeasurementInterval**
  - Type: SystemDouble Specifies the maximum measurement interval. This value is expressed in seconds. When you set the SetBurstDetectionEnabled(String, RFmxWlanMXTxpBurstDetectionEnabled) method to True , the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this parameter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXTxpConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/845bd348-abad-c799-b754-4b7af2ed1414.htm language=enus -->
## TOPIC 00170: rfmxwlandotnet/html/845bd348-abad-c799-b754-4b7af2ed1414.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/845bd348-abad-c799-b754-4b7af2ed1414.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/845bd348-abad-c799-b754-4b7af2ed1414.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetVectorAveragingTimeAlignmentEnabled Method

RFmxWlanMXOfdmModAccConfigurationSetVectorAveragingTimeAlignmentEnabled Method

Sets whether to enable time alignment for the acquired I/Q data across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetVectorAveragingTimeAlignmentEnabled(
	string selectorString,
	RFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabled value
)
```

```text
Public Function SetVectorAveragingTimeAlignmentEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccVectorAveragingTimeAlignmentEnabledSpecifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions.

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

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/848c2450-3407-cab2-a147-fabdb1f070fe.htm language=enus -->
## TOPIC 00171: rfmxwlandotnet/html/848c2450-3407-cab2-a147-fabdb1f070fe.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/848c2450-3407-cab2-a147-fabdb1f070fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/848c2450-3407-cab2-a147-fabdb1f070fe.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetOffsetStartFrequency Method

RFmxWlanMXSemConfigurationSetOffsetStartFrequency Method

Sets the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetStartFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetStartFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemOffsetStartFrequency

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/84b14177-abb1-1b39-3461-13453d3cff47.htm language=enus -->
## TOPIC 00172: rfmxwlandotnet/html/84b14177-abb1-1b39-3461-13453d3cff47.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/84b14177-abb1-1b39-3461-13453d3cff47.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/84b14177-abb1-1b39-3461-13453d3cff47.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetAllNamedResultNames Method

RFmxWlanMXGetAllNamedResultNames Method

Gets the named result names of the signal that you specify in the
 selectorString
 parameter.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllNamedResultNames(
	string selectorString,
	out string[] resultNames,
	out bool defaultResultExists
)
```

```text
Public Function GetAllNamedResultNames ( 
	selectorString As String,
	<OutAttribute> ByRef resultNames As String(),
	<OutAttribute> ByRef defaultResultExists As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **resultNames**
  - Type: SystemStringReturns an array of result names.
- **defaultResultExists**
  - Type: SystemBooleanUpon return, indicates whether the default result exists.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/8536f957-378e-802b-813e-0656b60cb9dc.htm language=enus -->
## TOPIC 00173: rfmxwlandotnet/html/8536f957-378e-802b-813e-0656b60cb9dc.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/8536f957-378e-802b-813e-0656b60cb9dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/8536f957-378e-802b-813e-0656b60cb9dc.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpConfiguration.ConfigureAveraging Method

RFmxWlanMXTxpConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxWlanMXTxpAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxWlanMXTxpAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXTxpAveragingEnabledSpecifies whether to enable averaging for the TXP measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True .

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXTxpConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/873530bf-6c10-0dc2-21cc-947b30a94a35.htm language=enus -->
## TOPIC 00174: rfmxwlandotnet/html/873530bf-6c10-0dc2-21cc-947b30a94a35.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/873530bf-6c10-0dc2-21cc-947b30a94a35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/873530bf-6c10-0dc2-21cc-947b30a94a35.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetMeasurementStatus Method

RFmxWlanMXSemResultsGetMeasurementStatus Method

Gets the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxWlanMXSemMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXSemMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemMeasurementStatusUpon return, contains the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.

###### Return Value

Int32

##### Remarks

SemResultsMeasurementStatus

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/8e81286e-196c-2869-d25c-520aa6b92e4f.htm language=enus -->
## TOPIC 00175: rfmxwlandotnet/html/8e81286e-196c-2869-d25c-520aa6b92e4f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/8e81286e-196c-2869-d25c-520aa6b92e4f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/8e81286e-196c-2869-d25c-520aa6b92e4f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampResults.FetchRiseTrace Method

RFmxWlanMXPowerRampResultsFetchRiseTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRiseTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> rawWaveform,
	ref AnalogWaveform<float> processedWaveform,
	ref AnalogWaveform<float> threshold,
	ref AnalogWaveform<float> powerReference
)
```

```text
Public Function FetchRiseTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef rawWaveform As AnalogWaveform(Of Single),
	ByRef processedWaveform As AnalogWaveform(Of Single),
	ByRef threshold As AnalogWaveform(Of Single),
	ByRef powerReference As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string .
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **rawWaveform**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the power versus time trace of the acquired waveform at the beginning of the burst.
- **processedWaveform**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the power versus time trace of the power envelope of the acquired waveform at the beginning of the burst.
- **threshold**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the threshold trace indicating the 10 percent and the 90 percent power levels.
- **powerReference**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the power reference trace which indicates the 100% power level, corresponding to the steady state average power level of the initial portion of the burst.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXPowerRampResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/938793c2-999f-0950-0919-ef8dc0c30053.htm language=enus -->
## TOPIC 00176: rfmxwlandotnet/html/938793c2-999f-0950-0919-ef8dc0c30053.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/938793c2-999f-0950-0919-ef8dc0c30053.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/938793c2-999f-0950-0919-ef8dc0c30053.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampResults Methods

RFmxWlanMXPowerRampResults Methods

The [RFmxWlanMXPowerRampResults](655d6d40-64b3-958b-b28e-317c79c6a035.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchFallTrace | Returns the raw, processed, thresholding and power reference waveforms at the end of a burst. |
|  | FetchMeasurement | Returns the PowerRamp rise time and fall time. |
|  | FetchRiseTrace | Returns the raw, processed, threshold and power-reference traces at the beginning of a burst. |
|  | GetFallTimeMean | Gets the power-ramp fall time of the burst. This value is expressed in seconds. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetRiseTimeMean | Gets the power-ramp rise time of the burst. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxWlanMXPowerRampResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/9590cf4d-14dd-4899-4319-02b3f93c835a.htm language=enus -->
## TOPIC 00177: rfmxwlandotnet/html/9590cf4d-14dd-4899-4319-02b3f93c835a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/9590cf4d-14dd-4899-4319-02b3f93c835a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/9590cf4d-14dd-4899-4319-02b3f93c835a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.GetAmplitudeCorrectionType Method

RFmxWlanMXSemConfigurationGetAmplitudeCorrectionType Method

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeCorrectionType(
	string selectorString,
	out RFmxWlanMXSemAmplitudeCorrectionType value
)
```

```text
Public Function GetAmplitudeCorrectionType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXSemAmplitudeCorrectionType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemAmplitudeCorrectionTypeUpon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

###### Return Value

Int32

##### Remarks

SemAmplitudeCorrectionType

RFCenterFrequency

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/95a4b811-d034-0fab-c16b-26fab2ac2427.htm language=enus -->
## TOPIC 00178: rfmxwlandotnet/html/95a4b811-d034-0fab-c16b-26fab2ac2427.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/95a4b811-d034-0fab-c16b-26fab2ac2427.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/95a4b811-d034-0fab-c16b-26fab2ac2427.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmFecCodingType Enumeration

RFmxWlanMXOfdmFecCodingType Enumeration

Specifies the type of forward error correction (FEC) coding used.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmFecCodingType
```

```text
Public Enumeration RFmxWlanMXOfdmFecCodingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bcc | 0 | The FEC coding type used is binary convolutional code (BCC). |
|  | Ldpc | 1 | The FEC coding type used is low-density parity check (LDPC). |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/95aafecc-8d0c-dc15-2ca4-c549979e958a.htm language=enus -->
## TOPIC 00179: rfmxwlandotnet/html/95aafecc-8d0c-dc15-2ca4-c549979e958a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/95aafecc-8d0c-dc15-2ca4-c549979e958a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/95aafecc-8d0c-dc15-2ca4-c549979e958a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetPeakEvm802_11_1999Mean Method

RFmxWlanMXDsssModAccResultsGetPeakEvm802_11_1999Mean Method

Gets the peak EVM of the burst. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakEvm802_11_1999Mean(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakEvm802_11_1999Mean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak EVM of the burst. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

DsssModAccResultsPeakEvm802_11_1999Mean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/95b63985-fe29-96c4-bf36-92d1622354cc.htm language=enus -->
## TOPIC 00180: rfmxwlandotnet/html/95b63985-fe29-96c4-bf36-92d1622354cc.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/95b63985-fe29-96c4-bf36-92d1622354cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/95b63985-fe29-96c4-bf36-92d1622354cc.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetMeasurementOffset Method

RFmxWlanMXOfdmModAccConfigurationGetMeasurementOffset Method

Gets the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemInt32Upon return, contains the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols.

###### Return Value

Int32

##### Remarks

OfdmModAccMeasurementOffset

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/961bb197-e018-0799-e020-550b6b80512b.htm language=enus -->
## TOPIC 00181: rfmxwlandotnet/html/961bb197-e018-0799-e020-550b6b80512b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/961bb197-e018-0799-e020-550b6b80512b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/961bb197-e018-0799-e020-550b6b80512b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccAutoLevelAllowOverflow Enumeration

RFmxWlanMXOfdmModAccAutoLevelAllowOverflow Enumeration

AutoLevel(String, Double)

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccAutoLevelAllowOverflow
```

```text
Public Enumeration RFmxWlanMXOfdmModAccAutoLevelAllowOverflow
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Disables searching for the optimum reference levels while allowing ADC overflow. |
|  | True | 1 | Enables searching for the optimum reference levels while allowing ADC overflow. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/a59cdb01-8eab-c76f-1160-b973779a07d4.htm language=enus -->
## TOPIC 00182: rfmxwlandotnet/html/a59cdb01-8eab-c76f-1160-b973779a07d4.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/a59cdb01-8eab-c76f-1160-b973779a07d4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/a59cdb01-8eab-c76f-1160-b973779a07d4.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetNumberOfSymbolsUsed Method

RFmxWlanMXOfdmModAccResultsGetNumberOfSymbolsUsed Method

Gets the number of OFDM symbols used by the measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfSymbolsUsed(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfSymbolsUsed ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemInt32Upon return, contains the number of OFDM symbols used by the measurement.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsNumberOfSymbolsUsed

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/a629691c-b22d-ac06-5f53-bc9c7e986ace.htm language=enus -->
## TOPIC 00183: rfmxwlandotnet/html/a629691c-b22d-ac06-5f53-bc9c7e986ace.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/a629691c-b22d-ac06-5f53-bc9c7e986ace.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/a629691c-b22d-ac06-5f53-bc9c7e986ace.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchPreamblePeakPowers802_11ac Method

RFmxWlanMXOfdmModAccResultsFetchPreamblePeakPowers802_11ac Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPreamblePeakPowers802_11ac(
	string selectorString,
	double timeout,
	out double vhtSigAPeakPowerMaximum,
	out double vhtStfPeakPowerMaximum,
	out double vhtLtfPeakPowerMaximum,
	out double vhtSigBPeakPowerMaximum
)
```

```text
Public Function FetchPreamblePeakPowers802_11ac ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef vhtSigAPeakPowerMaximum As Double,
	<OutAttribute> ByRef vhtStfPeakPowerMaximum As Double,
	<OutAttribute> ByRef vhtLtfPeakPowerMaximum As Double,
	<OutAttribute> ByRef vhtSigBPeakPowerMaximum As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **vhtSigAPeakPowerMaximum**
  - Type: SystemDouble Upon return, contains the peak power of the VHT-SIG-A field. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the maximum of the VHT-SIG-A field peak power results computed for each averaging count. This value is expressed in dBm.
- **vhtStfPeakPowerMaximum**
  - Type: SystemDouble Upon return, contains the peak power of the VHT-STF field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the maximum of the VHT-STF peak power results computed for each averaging count. This value is expressed in dBm.
- **vhtLtfPeakPowerMaximum**
  - Type: SystemDouble Upon return, contains the peak power of the VHT-LTF field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the maximum of the VHT-LTF peak power results computed for each averaging count. This value is expressed in dBm.
- **vhtSigBPeakPowerMaximum**
  - Type: SystemDouble Upon return, contains the peak power of the VHT-SIG-B field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the maximum of the VHT-SIG-B field peak power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/a8e4717f-a58c-6862-a0d6-ad1d1e34388d.htm language=enus -->
## TOPIC 00184: rfmxwlandotnet/html/a8e4717f-a58c-6862-a0d6-ad1d1e34388d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/a8e4717f-a58c-6862-a0d6-ad1d1e34388d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/a8e4717f-a58c-6862-a0d6-ad1d1e34388d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.BuildResultString Method

RFmxWlanMXBuildResultString Method

Creates selector string for use with configuration or fetch.

Namespace:

NationalInstruments.RFmx.WlanMX

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

- **resultName**
  - Type: SystemStringSpecifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1".

###### Return Value

String

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/aa3f0a2c-b7cf-be6c-8aff-23c1fee22173.htm language=enus -->
## TOPIC 00185: rfmxwlandotnet/html/aa3f0a2c-b7cf-be6c-8aff-23c1fee22173.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/aa3f0a2c-b7cf-be6c-8aff-23c1fee22173.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/aa3f0a2c-b7cf-be6c-8aff-23c1fee22173.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHESigBPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetHESigBPeakPowerMaximum Method

Gets the peak power of the HE-SIG-B field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHESigBPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetHESigBPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the HE-SIG-B field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHESigBPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/aaaeaf05-dda7-bbf1-3b3d-6a9ba3cf1b25.htm language=enus -->
## TOPIC 00186: rfmxwlandotnet/html/aaaeaf05-dda7-bbf1-3b3d-6a9ba3cf1b25.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/aaaeaf05-dda7-bbf1-3b3d-6a9ba3cf1b25.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/aaaeaf05-dda7-bbf1-3b3d-6a9ba3cf1b25.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchSymbolStreamEvmPerSubcarrierTrace Method

RFmxWlanMXOfdmModAccResultsFetchSymbolStreamEvmPerSubcarrierTrace Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSymbolStreamEvmPerSubcarrierTrace(
	string selectorString,
	double timeout,
	int symbolIndex,
	ref AnalogWaveform<float> symbolStreamEvmPerSubcarrier
)
```

```text
Public Function FetchSymbolStreamEvmPerSubcarrierTrace ( 
	selectorString As String,
	timeout As Double,
	symbolIndex As Integer,
	ByRef symbolStreamEvmPerSubcarrier As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and stream number. If you do not specify the result name, the default result instance is used. Example: "segment0/stream0""result::r1/segment0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **symbolIndex**
  - Type: SystemInt32Specifies the symbol index for which to fetch the trace.
- **symbolStreamEvmPerSubcarrier**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the stream EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ab1982ac-5727-4b8c-721e-0b853df1391a.htm language=enus -->
## TOPIC 00187: rfmxwlandotnet/html/ab1982ac-5727-4b8c-721e-0b853df1391a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ab1982ac-5727-4b8c-721e-0b853df1391a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ab1982ac-5727-4b8c-721e-0b853df1391a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.ConfigurePowerMeasurementCustomGateArray Method

RFmxWlanMXDsssModAccConfigurationConfigurePowerMeasurementCustomGateArray Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigurePowerMeasurementCustomGateArray(
	string selectorString,
	double[] startTime,
	double[] stopTime
)
```

```text
Public Function ConfigurePowerMeasurementCustomGateArray ( 
	selectorString As String,
	startTime As Double(),
	stopTime As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **startTime**
  - Type: SystemDoubleSpecifies the array of start time of the custom power gates. This value is expressed in seconds. A value of 0 indicates that the start time is the start of the PPDU.
- **stopTime**
  - Type: SystemDoubleSpecifies the array of stop time of the custom power gates. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ab1b787e-7e9d-f037-2afc-7a9d117b58d6.htm language=enus -->
## TOPIC 00188: rfmxwlandotnet/html/ab1b787e-7e9d-f037-2afc-7a9d117b58d6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ab1b787e-7e9d-f037-2afc-7a9d117b58d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ab1b787e-7e9d-f037-2afc-7a9d117b58d6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetLowerOffsetRelativeIntegratedPower Method

RFmxWlanMXSemResultsGetLowerOffsetRelativeIntegratedPower Method

Gets the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetRelativeIntegratedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetRelativeIntegratedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetRelativeIntegratedPower

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/abe1cf9a-92ed-96de-bfb3-0e1daa1ab22d.htm language=enus -->
## TOPIC 00189: rfmxwlandotnet/html/abe1cf9a-92ed-96de-bfb3-0e1daa1ab22d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/abe1cf9a-92ed-96de-bfb3-0e1daa1ab22d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/abe1cf9a-92ed-96de-bfb3-0e1daa1ab22d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccLSigParityCheckStatus Enumeration

RFmxWlanMXOfdmModAccLSigParityCheckStatus Enumeration

Returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccLSigParityCheckStatus
```

```text
Public Enumeration RFmxWlanMXOfdmModAccLSigParityCheckStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | NotApplicable | -1 | Returns that the parity check is invalid for the current waveform. |
|  | Fail | 0 | Returns that the parity check failed. |
|  | Pass | 1 | Returns that the parity check passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ad873017-ed0a-9058-18f2-7a10773e46c6.htm language=enus -->
## TOPIC 00190: rfmxwlandotnet/html/ad873017-ed0a-9058-18f2-7a10773e46c6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ad873017-ed0a-9058-18f2-7a10773e46c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ad873017-ed0a-9058-18f2-7a10773e46c6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXIQPowerEdgeTriggerSlope Enumeration

RFmxWlanMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or falling.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXIQPowerEdgeTriggerSlope
```

```text
Public Enumeration RFmxWlanMXIQPowerEdgeTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 0 | The trigger asserts when the signal power is rising. |
|  | Falling | 1 | The trigger asserts when the signal power is falling. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/af01360b-d3e6-a62f-97a3-58b3dfc94a56.htm language=enus -->
## TOPIC 00191: rfmxwlandotnet/html/af01360b-d3e6-a62f-97a3-58b3dfc94a56.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/af01360b-d3e6-a62f-97a3-58b3dfc94a56.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/af01360b-d3e6-a62f-97a3-58b3dfc94a56.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmNumberOfEhtSigSymbols Method

RFmxWlanMXGetOfdmNumberOfEhtSigSymbols Method

Gets the number of EHT-SIG symbols. This method is applicable only for 802.11be MU PPDU signals.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmNumberOfEhtSigSymbols(
	string selectorString,
	out int value
)
```

```text
Public Function GetOfdmNumberOfEhtSigSymbols ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the number of EHT-SIG symbols. This method is applicable only for 802.11be MU PPDU signals.

###### Return Value

Int32

##### Remarks

OfdmNumberOfEhtSigSymbols

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b1536270-b939-712b-4b8c-0c6fd117f460.htm language=enus -->
## TOPIC 00192: rfmxwlandotnet/html/b1536270-b939-712b-4b8c-0c6fd117f460.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b1536270-b939-712b-4b8c-0c6fd117f460.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b1536270-b939-712b-4b8c-0c6fd117f460.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetPeakEvm802_11_2007Maximum Method

RFmxWlanMXDsssModAccResultsGetPeakEvm802_11_2007Maximum Method

Gets the peak EVM of the burst. This value is expressed as a percentage or in dB.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakEvm802_11_2007Maximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakEvm802_11_2007Maximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak EVM of the burst. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### Remarks

DsssModAccResultsPeakEvm802_11_2007Maximum

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b1bbc488-e2d9-23e7-7353-716df688edd8.htm language=enus -->
## TOPIC 00193: rfmxwlandotnet/html/b1bbc488-e2d9-23e7-7353-716df688edd8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b1bbc488-e2d9-23e7-7353-716df688edd8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b1bbc488-e2d9-23e7-7353-716df688edd8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchEvmSubcarrierIndices Method

RFmxWlanMXOfdmModAccResultsFetchEvmSubcarrierIndices Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEvmSubcarrierIndices(
	string selectorString,
	double timeout,
	ref int[] subcarrierIndices
)
```

```text
Public Function FetchEvmSubcarrierIndices ( 
	selectorString As String,
	timeout As Double,
	ByRef subcarrierIndices As Integer()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **subcarrierIndices**
  - Type: SystemInt32 Upon return, contains an array of subcarrier indices for which the EVM results are computed.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b2083302-4b38-cfbc-470c-61d721a164b7.htm language=enus -->
## TOPIC 00194: rfmxwlandotnet/html/b2083302-4b38-cfbc-470c-61d721a164b7.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b2083302-4b38-cfbc-470c-61d721a164b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b2083302-4b38-cfbc-470c-61d721a164b7.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmPhaseRotationCoefficient2 Method

RFmxWlanMXGetOfdmPhaseRotationCoefficient2 Method

IEEE Standard P802.11be/D6.0

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmPhaseRotationCoefficient2(
	string selectorString,
	out RFmxWlanMXOfdmPhaseRotationCoefficient2 value
)
```

```text
Public Function GetOfdmPhaseRotationCoefficient2 ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmPhaseRotationCoefficient2
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmPhaseRotationCoefficient2 Upon return, contains the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0 .

###### Return Value

Int32

##### Remarks

OfdmPhaseRotationCoefficient2

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b2183b1c-0de5-1340-8443-9250fba264b6.htm language=enus -->
## TOPIC 00195: rfmxwlandotnet/html/b2183b1c-0de5-1340-8443-9250fba264b6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b2183b1c-0de5-1340-8443-9250fba264b6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b2183b1c-0de5-1340-8443-9250fba264b6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchUserStreamRmsEvm Method

RFmxWlanMXOfdmModAccResultsFetchUserStreamRmsEvm Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUserStreamRmsEvm(
	string selectorString,
	double timeout,
	out double userStreamRmsEvmMean,
	out double userStreamDataRmsEvmMean,
	out double userStreamPilotRmsEvmMean
)
```

```text
Public Function FetchUserStreamRmsEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef userStreamRmsEvmMean As Double,
	<OutAttribute> ByRef userStreamDataRmsEvmMean As Double,
	<OutAttribute> ByRef userStreamPilotRmsEvmMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0""result::r1/user0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **userStreamRmsEvmMean**
  - Type: SystemDouble Upon return, contains the RMS EVM of all subcarriers in all OFDM symbols for the specified user. When you set the SetEvmUnit(String, RFmxWlanMXOfdmModAccEvmUnit) method to Percentage , the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit method to dB , the measurement returns this result in dB. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the user stream RMS EVM computed for each averaging count.
- **userStreamDataRmsEvmMean**
  - Type: SystemDouble Upon return, contains the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. When you set the SetEvmUnit(String, RFmxWlanMXOfdmModAccEvmUnit) method to Percentage , the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit method to dB , the measurement returns this result in dB. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the user stream data RMS EVM computed for each averaging count.
- **userStreamPilotRmsEvmMean**
  - Type: SystemDouble Upon return, contains the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. When you set the SetEvmUnit(String, RFmxWlanMXOfdmModAccEvmUnit) method to Percentage , the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit method to dB , the measurement returns this result in dB. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the user stream pilot RMS EVM computed for each averaging count.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b2f8ddc5-0a9d-6552-704b-8990f8c7fc8b.htm language=enus -->
## TOPIC 00196: rfmxwlandotnet/html/b2f8ddc5-0a9d-6552-704b-8990f8c7fc8b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b2f8ddc5-0a9d-6552-704b-8990f8c7fc8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b2f8ddc5-0a9d-6552-704b-8990f8c7fc8b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchChannelFrequencyResponseMeanTrace Method

RFmxWlanMXOfdmModAccResultsFetchChannelFrequencyResponseMeanTrace Method

SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchChannelFrequencyResponseMeanTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> channelFrequencyResponseMeanMagnitude,
	ref AnalogWaveform<float> channelFrequencyResponseMeanPhase
)
```

```text
Public Function FetchChannelFrequencyResponseMeanTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef channelFrequencyResponseMeanMagnitude As AnalogWaveform(Of Single),
	ByRef channelFrequencyResponseMeanPhase As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, chain number, and stream number. Example: "segment0/chain0/stream0""result::r1/segment0/chain0/stream0" You can use the BuildStreamString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **channelFrequencyResponseMeanMagnitude**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the channel frequency response magnitude trace.
- **channelFrequencyResponseMeanPhase**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the channel frequency response phase trace, which is the deviation of the measured phase response of the channel from the ideal linear phase response.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b612f1d2-644e-dd1c-a392-db351f87345f.htm language=enus -->
## TOPIC 00197: rfmxwlandotnet/html/b612f1d2-644e-dd1c-a392-db351f87345f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b612f1d2-644e-dd1c-a392-db351f87345f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b612f1d2-644e-dd1c-a392-db351f87345f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchPpduAveragePower Method

RFmxWlanMXOfdmModAccResultsFetchPpduAveragePower Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPpduAveragePower(
	string selectorString,
	double timeout,
	out double ppduAveragePowerMean
)
```

```text
Public Function FetchPpduAveragePower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef ppduAveragePowerMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **ppduAveragePowerMean**
  - Type: SystemDouble Upon return, contains the average power of the PPDU. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the PPDU average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b8059c39-e6e7-9efd-3583-3e1f4627edd1.htm language=enus -->
## TOPIC 00198: rfmxwlandotnet/html/b8059c39-e6e7-9efd-3583-3e1f4627edd1.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b8059c39-e6e7-9efd-3583-3e1f4627edd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b8059c39-e6e7-9efd-3583-3e1f4627edd1.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccResults.GetDataAveragePowerMean Method

RFmxWlanMXDsssModAccResultsGetDataAveragePowerMean Method

Gets the average power of the data field of the PPDU. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDataAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetDataAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the data field of the PPDU. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

DsssModAccResultsDataAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXDsssModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b84a33c7-7250-ded8-97a2-d9d393725832.htm language=enus -->
## TOPIC 00199: rfmxwlandotnet/html/b84a33c7-7250-ded8-97a2-d9d393725832.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b84a33c7-7250-ded8-97a2-d9d393725832.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b84a33c7-7250-ded8-97a2-d9d393725832.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccAcquisitionLengthMode Enumeration

RFmxWlanMXOfdmModAccAcquisitionLengthMode Enumeration

Specifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc properties.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccAcquisitionLengthMode
```

```text
Public Enumeration RFmxWlanMXOfdmModAccAcquisitionLengthMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Manual | 0 | Uses the acquisition length specified by the SetAcquisitionLength(String, Double) method. |
|  | Auto | 1 | Computes the acquisition length based on the SetMeasurementOffset(String, Int32) and the SetMaximumMeasurementLength(String, Int32) properties. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b888bd58-08b9-7267-216a-76a836f96a56.htm language=enus -->
## TOPIC 00200: rfmxwlandotnet/html/b888bd58-08b9-7267-216a-76a836f96a56.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b888bd58-08b9-7267-216a-76a836f96a56.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b888bd58-08b9-7267-216a-76a836f96a56.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetCombinedSignalDemodulationEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetCombinedSignalDemodulationEnabled Method

Gets whether to enable demodulation of the signal that is formed by combining signals from multiple transmitter chains.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCombinedSignalDemodulationEnabled(
	string selectorString,
	out RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled value
)
```

```text
Public Function GetCombinedSignalDemodulationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabledUpon return, contains whether to enable demodulation of the signal that is formed by combining signals from multiple transmitter chains.

###### Return Value

Int32

##### Remarks

OfdmModAccCombinedSignalDemodulationEnabled

False

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b88f38da-d63a-e59a-9de5-4191548872d8.htm language=enus -->
## TOPIC 00201: rfmxwlandotnet/html/b88f38da-d63a-e59a-9de5-4191548872d8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b88f38da-d63a-e59a-9de5-4191548872d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b88f38da-d63a-e59a-9de5-4191548872d8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetVhtSigAAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetVhtSigAAveragePowerMean Method

Gets the average power of the VHT-SIG-A field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetVhtSigAAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetVhtSigAAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the VHT-SIG-A field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsVhtSigAAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/b8d4e1ab-db94-1b28-f6d8-5c6564891191.htm language=enus -->
## TOPIC 00202: rfmxwlandotnet/html/b8d4e1ab-db94-1b28-f6d8-5c6564891191.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/b8d4e1ab-db94-1b28-f6d8-5c6564891191.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/b8d4e1ab-db94-1b28-f6d8-5c6564891191.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetChannelEstimationType Method

RFmxWlanMXOfdmModAccConfigurationGetChannelEstimationType Method

Gets the fields in the PPDU used to estimate the channel frequency response.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChannelEstimationType(
	string selectorString,
	out RFmxWlanMXOfdmModAccChannelEstimationType value
)
```

```text
Public Function GetChannelEstimationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccChannelEstimationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccChannelEstimationTypeUpon return, contains the fields in the PPDU used to estimate the channel frequency response.

###### Return Value

Int32

##### Remarks

OfdmModAccChannelEstimationType

Reference

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/baf1e3a1-add7-35b4-7971-33d5700d1151.htm language=enus -->
## TOPIC 00203: rfmxwlandotnet/html/baf1e3a1-add7-35b4-7971-33d5700d1151.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/baf1e3a1-add7-35b4-7971-33d5700d1151.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/baf1e3a1-add7-35b4-7971-33d5700d1151.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.ConfigureSelectedPortsMultiple Method

RFmxWlanMXConfigureSelectedPortsMultiple Method

SetNumberOfFrequencySegments(String, Int32)

SetNumberOfReceiveChains(String, Int32)

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSelectedPortsMultiple(
	string selectorString,
	string[] selectedPorts
)
```

```text
Public Function ConfigureSelectedPortsMultiple ( 
	selectorString As String,
	selectedPorts As String()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **selectedPorts**
  - Type: SystemString Specifies the list of MIMO ports to be configured. Use "port::(deviceName)/(channelNumber)" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::(deviceName)/(channelNumber)/(port)" . Example: port::myrfsa1/0/if1 You can use the RFmxInstr_BuildPortString method to build the selected port.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bb2897cc-1196-0199-36de-25053241a144.htm language=enus -->
## TOPIC 00204: rfmxwlandotnet/html/bb2897cc-1196-0199-36de-25053241a144.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bb2897cc-1196-0199-36de-25053241a144.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bb2897cc-1196-0199-36de-25053241a144.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetBurstStartDetectionEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetBurstStartDetectionEnabled Method

Gets whether the measurement detects a rising edge of a burst in the acquired waveform.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstStartDetectionEnabled(
	string selectorString,
	out RFmxWlanMXOfdmModAccBurstStartDetectionEnabled value
)
```

```text
Public Function GetBurstStartDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccBurstStartDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccBurstStartDetectionEnabledUpon return, contains whether the measurement detects a rising edge of a burst in the acquired waveform.

###### Return Value

Int32

##### Remarks

OfdmModAccBurstStartDetectionEnabled

False

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bb5b54b2-44eb-b1aa-bffb-738570e5bd02.htm language=enus -->
## TOPIC 00205: rfmxwlandotnet/html/bb5b54b2-44eb-b1aa-bffb-738570e5bd02.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bb5b54b2-44eb-b1aa-bffb-738570e5bd02.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bb5b54b2-44eb-b1aa-bffb-738570e5bd02.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.GetOffsetStopFrequency Method

RFmxWlanMXSemConfigurationGetOffsetStopFrequency Method

Gets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetStopFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetStopFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemOffsetStopFrequency

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bbc3d152-a2f1-987b-cb91-6e8af930eb81.htm language=enus -->
## TOPIC 00206: rfmxwlandotnet/html/bbc3d152-a2f1-987b-cb91-6e8af930eb81.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bbc3d152-a2f1-987b-cb91-6e8af930eb81.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bbc3d152-a2f1-987b-cb91-6e8af930eb81.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHTDltfPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetHTDltfPeakPowerMaximum Method

Gets the peak power of the HT-DLTF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHTDltfPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetHTDltfPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the HT-DLTF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHTDltfPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bc21b551-ed4c-7396-61f9-e6dc7011669a.htm language=enus -->
## TOPIC 00207: rfmxwlandotnet/html/bc21b551-ed4c-7396-61f9-e6dc7011669a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bc21b551-ed4c-7396-61f9-e6dc7011669a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bc21b551-ed4c-7396-61f9-e6dc7011669a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXConstants.PxiTriggerLine7 Field

RFmxWlanMXConstantsPxiTriggerLine7 Field

The signal is exported to the PXI trigger line 7.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMXConstants Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bc99fbe7-fd0b-9b26-d3e0-2fe7b1aefc12.htm language=enus -->
## TOPIC 00208: rfmxwlandotnet/html/bc99fbe7-fd0b-9b26-d3e0-2fe7b1aefc12.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bc99fbe7-fd0b-9b26-d3e0-2fe7b1aefc12.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bc99fbe7-fd0b-9b26-d3e0-2fe7b1aefc12.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetPhaseTrackingEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetPhaseTrackingEnabled Method

Gets whether to enable pilot-based common phase error correction per OFDM data symbol.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseTrackingEnabled(
	string selectorString,
	out RFmxWlanMXOfdmModAccPhaseTrackingEnabled value
)
```

```text
Public Function GetPhaseTrackingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccPhaseTrackingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccPhaseTrackingEnabledUpon return, contains whether to enable pilot-based common phase error correction per OFDM data symbol.

###### Return Value

Int32

##### Remarks

OfdmModAccPhaseTrackingEnabled

True

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bca23db5-2624-9651-b557-2c7293b025be.htm language=enus -->
## TOPIC 00209: rfmxwlandotnet/html/bca23db5-2624-9651-b557-2c7293b025be.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bca23db5-2624-9651-b557-2c7293b025be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bca23db5-2624-9651-b557-2c7293b025be.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXConstants.PxiTriggerLine5 Field

RFmxWlanMXConstantsPxiTriggerLine5 Field

The signal is exported to the PXI trigger line 5.

Namespace:

NationalInstruments.RFmx.WlanMX

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

RFmxWlanMXConstants Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bd521f94-cc22-fc65-7b66-ee44b1a1c54a.htm language=enus -->
## TOPIC 00210: rfmxwlandotnet/html/bd521f94-cc22-fc65-7b66-ee44b1a1c54a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bd521f94-cc22-fc65-7b66-ee44b1a1c54a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bd521f94-cc22-fc65-7b66-ee44b1a1c54a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetOffsetStopFrequency Method

RFmxWlanMXSemConfigurationSetOffsetStopFrequency Method

Sets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetStopFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetStopFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemOffsetStopFrequency

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bd614e6d-ef57-4de9-38a4-da69a6efb20a.htm language=enus -->
## TOPIC 00211: rfmxwlandotnet/html/bd614e6d-ef57-4de9-38a4-da69a6efb20a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bd614e6d-ef57-4de9-38a4-da69a6efb20a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bd614e6d-ef57-4de9-38a4-da69a6efb20a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccPhaseRotationCoefficient2 Enumeration

RFmxWlanMXOfdmModAccPhaseRotationCoefficient2 Enumeration

Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccPhaseRotationCoefficient2
```

```text
Public Enumeration RFmxWlanMXOfdmModAccPhaseRotationCoefficient2
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PlusOne | 0 | Specifies that phase rotation coefficient 2 is +1. |
|  | MinusOne | 1 | Specifies that phase rotation coefficient 2 is -1. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bdcb3f01-6708-c186-8ab2-cc36c4580363.htm language=enus -->
## TOPIC 00212: rfmxwlandotnet/html/bdcb3f01-6708-c186-8ab2-cc36c4580363.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bdcb3f01-6708-c186-8ab2-cc36c4580363.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bdcb3f01-6708-c186-8ab2-cc36c4580363.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetUpperOffsetMarginAbsolutePower Method

RFmxWlanMXSemResultsGetUpperOffsetMarginAbsolutePower Method

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the power level of the spectrum corresponding to the result of the GetUpperOffsetMargin(String, Double) method. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMarginAbsolutePower

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/be97dd39-9983-0103-019a-9794ee42933a.htm language=enus -->
## TOPIC 00213: rfmxwlandotnet/html/be97dd39-9983-0103-019a-9794ee42933a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/be97dd39-9983-0103-019a-9794ee42933a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/be97dd39-9983-0103-019a-9794ee42933a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetDigitalEdgeTriggerEdge Method

RFmxWlanMXSetDigitalEdgeTriggerEdge Method

SetTriggerType(String, RFmxWlanMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerEdge(
	string selectorString,
	RFmxWlanMXDigitalEdgeTriggerEdge value
)
```

```text
Public Function SetDigitalEdgeTriggerEdge ( 
	selectorString As String,
	value As RFmxWlanMXDigitalEdgeTriggerEdge
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXDigitalEdgeTriggerEdge Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to DigitalEdge .

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerEdge

Rising

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/bf7da8b4-c355-51d0-b471-6ee01f0afe34.htm language=enus -->
## TOPIC 00214: rfmxwlandotnet/html/bf7da8b4-c355-51d0-b471-6ee01f0afe34.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/bf7da8b4-c355-51d0-b471-6ee01f0afe34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/bf7da8b4-c355-51d0-b471-6ee01f0afe34.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetAveragingCount Method

RFmxWlanMXDsssModAccConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxWlanMXDsssModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXDsssModAccAveragingEnabled) method to True .

###### Return Value

Int32

##### Remarks

DsssModAccAveragingCount

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/c741439e-0f0b-14a6-6b40-312377f6d330.htm language=enus -->
## TOPIC 00215: rfmxwlandotnet/html/c741439e-0f0b-14a6-6b40-312377f6d330.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/c741439e-0f0b-14a6-6b40-312377f6d330.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/c741439e-0f0b-14a6-6b40-312377f6d330.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.SetAllTracesEnabled Method

RFmxWlanMXDsssModAccConfigurationSetAllTracesEnabled Method

Sets whether to enable all the traces computed by DSSSModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanSpecifies whether to enable all the traces computed by DSSSModAcc measurement.

###### Return Value

Int32

##### Remarks

DsssModAccAllTracesEnabled

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ca08843d-f277-6c53-a275-56055de4b0b8.htm language=enus -->
## TOPIC 00216: rfmxwlandotnet/html/ca08843d-f277-6c53-a275-56055de4b0b8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ca08843d-f277-6c53-a275-56055de4b0b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ca08843d-f277-6c53-a275-56055de4b0b8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetResultFetchTimeout Method

RFmxWlanMXSetResultFetchTimeout Method

Sets the time, in seconds, to wait before results are available in the RFmxWLAN_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemDoubleSpecifies the time, in seconds, to wait before results are available in the RFmxWLAN_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ca2c2874-fccc-ceee-0120-dcf8b719eb2b.htm language=enus -->
## TOPIC 00217: rfmxwlandotnet/html/ca2c2874-fccc-ceee-0120-dcf8b719eb2b.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ca2c2874-fccc-ceee-0120-dcf8b719eb2b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ca2c2874-fccc-ceee-0120-dcf8b719eb2b.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.SetAveragingCount Method

RFmxWlanMXSemConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled) method to True .

###### Return Value

Int32

##### Remarks

SemAveragingCount

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cb71d837-c48b-68ab-877c-7d251adbff2e.htm language=enus -->
## TOPIC 00218: rfmxwlandotnet/html/cb71d837-c48b-68ab-877c-7d251adbff2e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cb71d837-c48b-68ab-877c-7d251adbff2e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cb71d837-c48b-68ab-877c-7d251adbff2e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.AutoLevel Method

RFmxWlanMXOfdmModAccConfigurationAutoLevel Method

SetReferenceLevel(String, Double)

SetAutoLevelAllowOverflow(String, RFmxWlanMXOfdmModAccAutoLevelAllowOverflow)

False

True

After calling this method, you need to perform the ModAcc measurement.

- A valid OFDMModAcc measurement configuration
- SetReferenceLevel(String, Double) method set to peak power of the signal
- Repetitive signals at the analyzer's input along with trigger settings that measure the same portion of the waveform every time the measurement is performed
- No other measurements are running in parallel

False

True

SetNoiseCompensationEnabled(String, RFmxWlanMXOfdmModAccNoiseCompensationEnabled)

True

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int AutoLevel(
	string selectorString,
	double timeout
)
```

```text
Public Function AutoLevel ( 
	selectorString As String,
	timeout As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the EVM results. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cb9a67f8-accf-8b81-1000-b1815aeab6fe.htm language=enus -->
## TOPIC 00219: rfmxwlandotnet/html/cb9a67f8-accf-8b81-1000-b1815aeab6fe.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cb9a67f8-accf-8b81-1000-b1815aeab6fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cb9a67f8-accf-8b81-1000-b1815aeab6fe.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetChannelEstimationLLtfEnabled Method

RFmxWlanMXOfdmModAccConfigurationSetChannelEstimationLLtfEnabled Method

Sets whether to use the legacy channel estimation field for combining with the reference channel frequency response.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChannelEstimationLLtfEnabled(
	string selectorString,
	RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled value
)
```

```text
Public Function SetChannelEstimationLLtfEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccChannelEstimationLLtfEnabledSpecifies whether to use the legacy channel estimation field for combining with the reference channel frequency response.

###### Return Value

Int32

##### Remarks

OfdmModAccChannelEstimationLLtfEnabled

False

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cbb438b5-234e-fe33-6c8c-36ef37a94b6c.htm language=enus -->
## TOPIC 00220: rfmxwlandotnet/html/cbb438b5-234e-fe33-6c8c-36ef37a94b6c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cbb438b5-234e-fe33-6c8c-36ef37a94b6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cbb438b5-234e-fe33-6c8c-36ef37a94b6c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetNumberOfReceiveChains Method

RFmxWlanMXSetNumberOfReceiveChains Method

Sets the number of receive chains for OFDM standards.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfReceiveChains(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfReceiveChains ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the number of receive chains for OFDM standards.

###### Return Value

Int32

##### Remarks

NumberOfReceiveChains

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cd1e5c61-ca78-f6f5-52a9-c7ce48197d0e.htm language=enus -->
## TOPIC 00221: rfmxwlandotnet/html/cd1e5c61-ca78-f6f5-52a9-c7ce48197d0e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cd1e5c61-ca78-f6f5-52a9-c7ce48197d0e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cd1e5c61-ca78-f6f5-52a9-c7ce48197d0e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetAveragingEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for OFDMModAcc measurements.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxWlanMXOfdmModAccAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccAveragingEnabledUpon return, contains whether to enable averaging for OFDMModAcc measurements.

###### Return Value

Int32

##### Remarks

OfdmModAccAveragingEnabled

False

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cd71e0f3-f70a-712b-a725-1ba3b02f8c1f.htm language=enus -->
## TOPIC 00222: rfmxwlandotnet/html/cd71e0f3-f70a-712b-a725-1ba3b02f8c1f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cd71e0f3-f70a-712b-a725-1ba3b02f8c1f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cd71e0f3-f70a-712b-a725-1ba3b02f8c1f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXTxpConfiguration.SetAllTracesEnabled Method

RFmxWlanMXTxpConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the TXP measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanSpecifies whether to enable the traces to be stored and retrieved after performing the TXP measurement.

###### Return Value

Int32

##### Remarks

TxpAllTracesEnabled

##### See Also

###### Reference

RFmxWlanMXTxpConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cdde0814-d2a1-9894-5f47-50675ea21765.htm language=enus -->
## TOPIC 00223: rfmxwlandotnet/html/cdde0814-d2a1-9894-5f47-50675ea21765.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cdde0814-d2a1-9894-5f47-50675ea21765.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cdde0814-d2a1-9894-5f47-50675ea21765.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAcc.Results Property

RFmxWlanMXDsssModAccResults Property

RFmxWlanMXDsssModAccResults

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXDsssModAccResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxWlanMXDsssModAccResults
	Get
```

###### Property Value

RFmxWlanMXDsssModAccResults

##### See Also

###### Reference

RFmxWlanMXDsssModAcc Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cdfc7cc3-3e03-7027-8327-8c32a21da13c.htm language=enus -->
## TOPIC 00224: rfmxwlandotnet/html/cdfc7cc3-3e03-7027-8327-8c32a21da13c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cdfc7cc3-3e03-7027-8327-8c32a21da13c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cdfc7cc3-3e03-7027-8327-8c32a21da13c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration Methods

RFmxWlanMXSemConfiguration Methods

The [RFmxWlanMXSemConfiguration](58dae736-1dd0-1a15-2b08-6cd9bd689799.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the measurement. |
|  | ConfigureMaskType | Configures the mask type for the SEM measurement. |
|  | ConfigureNumberOfOffsets | Configures the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | ConfigureOffsetFrequencyArray | Configures the array of offset start and stop frequencies and specifies whether the offsets are present on one side, or on both the sides of the carrier when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | ConfigureOffsetRelativeLimitArray | Configures an array of relative mask limits corresponding the start and stop frequencies of the offsets when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . The relative limits are relative to the peak power of the carrier. |
|  | ConfigureSpan | Configures the frequency range around the center frequency to be acquired for the SEM measurement. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled) method to True . |
|  | GetAveragingEnabled | Gets whether to enable averaging for the SEM measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
|  | GetCarrierIntegrationBandwidth | Gets the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaskType | Gets whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
|  | GetMeasurementEnabled | Gets whether to enable the spectral emission mask (SEM) measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for SEM measurement. |
|  | GetNumberOfOffsets | Gets the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | GetOffsetRelativeLimitStart | Gets the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. |
|  | GetOffsetRelativeLimitStop | Gets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
|  | GetOffsetSideband | Gets whether the offset segment is present on one side or on both sides of the carrier. |
|  | GetOffsetStartFrequency | Gets the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | GetOffsetStopFrequency | Gets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |
|  | GetSpan | Gets the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz. |
|  | GetSpanAuto | Gets whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
|  | GetSweepTimeAuto | Gets whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
|  | GetSweepTimeInterval | Gets the sweep time for the SEM measurement. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxWlanMXSemAveragingEnabled) method to True . |
|  | SetAveragingEnabled | Sets whether to enable averaging for the SEM measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
|  | SetMaskType | Sets whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
|  | SetMeasurementEnabled | Sets whether to enable the spectral emission mask (SEM) measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for SEM measurement. |
|  | SetNumberOfOffsets | Sets the number of offset segments for the SEM measurement when you set the SetMaskType(String, RFmxWlanMXSemMaskType) method to Custom . |
|  | SetOffsetRelativeLimitStart | Sets the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. |
|  | SetOffsetRelativeLimitStop | Sets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
|  | SetOffsetSideband | Sets whether the offset segment is present on one side or on both sides of the carrier. |
|  | SetOffsetStartFrequency | Sets the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | SetOffsetStopFrequency | Sets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |
|  | SetSpan | Sets the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz. |
|  | SetSpanAuto | Sets whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
|  | SetSweepTimeAuto | Sets whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
|  | SetSweepTimeInterval | Sets the sweep time for the SEM measurement. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ce17e155-1bb6-f547-7f3e-ac8e88fa35d6.htm language=enus -->
## TOPIC 00225: rfmxwlandotnet/html/ce17e155-1bb6-f547-7f3e-ac8e88fa35d6.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ce17e155-1bb6-f547-7f3e-ac8e88fa35d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ce17e155-1bb6-f547-7f3e-ac8e88fa35d6.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXPowerRampConfiguration.SetAllTracesEnabled Method

RFmxWlanMXPowerRampConfigurationSetAllTracesEnabled Method

Sets whether to enable all the traces computed by the PowerRamp measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanSpecifies whether to enable all the traces computed by the PowerRamp measurement.

###### Return Value

Int32

##### Remarks

PowerRampAllTracesEnabled

##### See Also

###### Reference

RFmxWlanMXPowerRampConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ce68ab83-2af5-4ddf-a854-ab5fce38329a.htm language=enus -->
## TOPIC 00226: rfmxwlandotnet/html/ce68ab83-2af5-4ddf-a854-ab5fce38329a.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ce68ab83-2af5-4ddf-a854-ab5fce38329a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ce68ab83-2af5-4ddf-a854-ab5fce38329a.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetFrequencyErrorEstimationMethod Method

RFmxWlanMXOfdmModAccConfigurationGetFrequencyErrorEstimationMethod Method

Gets the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyErrorEstimationMethod(
	string selectorString,
	out RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod value
)
```

```text
Public Function GetFrequencyErrorEstimationMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccFrequencyErrorEstimationMethodUpon return, contains the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal.

###### Return Value

Int32

##### Remarks

OfdmModAccFrequencyErrorEstimationMethod

PreambleAndPilots

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ce82e6e2-de05-ceca-c889-cd2636143a44.htm language=enus -->
## TOPIC 00227: rfmxwlandotnet/html/ce82e6e2-de05-ceca-c889-cd2636143a44.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ce82e6e2-de05-ceca-c889-cd2636143a44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ce82e6e2-de05-ceca-c889-cd2636143a44.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetVhtSigAPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetVhtSigAPeakPowerMaximum Method

Gets the peak power of the VHT-SIG-A field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetVhtSigAPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetVhtSigAPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the VHT-SIG-A field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsVhtSigAPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/cf719050-5f36-c2cd-9705-b08e2339aa4e.htm language=enus -->
## TOPIC 00228: rfmxwlandotnet/html/cf719050-5f36-c2cd-9705-b08e2339aa4e.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/cf719050-5f36-c2cd-9705-b08e2339aa4e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/cf719050-5f36-c2cd-9705-b08e2339aa4e.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchChainRmsEvm Method

RFmxWlanMXOfdmModAccResultsFetchChainRmsEvm Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchChainRmsEvm(
	string selectorString,
	double timeout,
	out double chainRmsEvmMean,
	out double chainDataRmsEvmMean,
	out double chainPilotRmsEvmMean
)
```

```text
Public Function FetchChainRmsEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef chainRmsEvmMean As Double,
	<OutAttribute> ByRef chainDataRmsEvmMean As Double,
	<OutAttribute> ByRef chainPilotRmsEvmMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0""result::r1/segment0/chain0" You can use the BuildChainString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **chainRmsEvmMean**
  - Type: SystemDouble Upon return, contains the chain RMS EVM of all subcarriers in all OFDM symbols. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of chain RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB.
- **chainDataRmsEvmMean**
  - Type: SystemDouble Upon return, contains the chain RMS EVM of data subcarriers in all OFDM symbols. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of data chain RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB.
- **chainPilotRmsEvmMean**
  - Type: SystemDouble Upon return, contains the chain RMS EVM of pilot subcarriers in all OFDM symbols. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of pilot chain RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d0d37d8c-696c-878e-516e-a325be1b644f.htm language=enus -->
## TOPIC 00229: rfmxwlandotnet/html/d0d37d8c-696c-878e-516e-a325be1b644f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d0d37d8c-696c-878e-516e-a325be1b644f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d0d37d8c-696c-878e-516e-a325be1b644f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.SetSymbolClockErrorCorrectionEnabled Method

RFmxWlanMXOfdmModAccConfigurationSetSymbolClockErrorCorrectionEnabled Method

Sets whether to enable symbol clock error correction.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSymbolClockErrorCorrectionEnabled(
	string selectorString,
	RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled value
)
```

```text
Public Function SetSymbolClockErrorCorrectionEnabled ( 
	selectorString As String,
	value As RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabledSpecifies whether to enable symbol clock error correction.

###### Return Value

Int32

##### Remarks

OfdmModAccSymbolClockErrorCorrectionEnabled

True

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d1b4c31a-fb95-54cb-5001-c49e48df6e17.htm language=enus -->
## TOPIC 00230: rfmxwlandotnet/html/d1b4c31a-fb95-54cb-5001-c49e48df6e17.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d1b4c31a-fb95-54cb-5001-c49e48df6e17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d1b4c31a-fb95-54cb-5001-c49e48df6e17.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemConfiguration.GetCarrierIntegrationBandwidth Method

RFmxWlanMXSemConfigurationGetCarrierIntegrationBandwidth Method

Gets the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierIntegrationBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierIntegrationBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemCarrierIntegrationBandwidth

##### See Also

###### Reference

RFmxWlanMXSemConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d25ab1d0-4c4f-8e3f-a1ca-4366fbe71785.htm language=enus -->
## TOPIC 00231: rfmxwlandotnet/html/d25ab1d0-4c4f-8e3f-a1ca-4366fbe71785.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d25ab1d0-4c4f-8e3f-a1ca-4366fbe71785.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d25ab1d0-4c4f-8e3f-a1ca-4366fbe71785.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetRUOffsetMruIndex Method

RFmxWlanMXOfdmModAccResultsGetRUOffsetMruIndex Method

Gets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs.
 If an MRU is configured, the MRU Index is as defined in Table 36-8 to Table 36-15 of
 IEEE P802.11be/D6.0.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRUOffsetMruIndex(
	string selectorString,
	out int value
)
```

```text
Public Function GetRUOffsetMruIndex ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and User number. Example: "User0", "result::r1/User0". You can use the BuildUserString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsRUOffsetMruIndex

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d2be7b22-3a2a-079f-2c62-f2c2b155aa12.htm language=enus -->
## TOPIC 00232: rfmxwlandotnet/html/d2be7b22-3a2a-079f-2c62-f2c2b155aa12.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d2be7b22-3a2a-079f-2c62-f2c2b155aa12.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d2be7b22-3a2a-079f-2c62-f2c2b155aa12.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetHESigBAveragePowerMean Method

RFmxWlanMXOfdmModAccResultsGetHESigBAveragePowerMean Method

Gets the average power of the HE-SIG-B field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHESigBAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetHESigBAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the HE-SIG-B field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsHESigBAveragePowerMean

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d326d455-c584-c96a-3243-381a01286345.htm language=enus -->
## TOPIC 00233: rfmxwlandotnet/html/d326d455-c584-c96a-3243-381a01286345.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d326d455-c584-c96a-3243-381a01286345.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d326d455-c584-c96a-3243-381a01286345.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXSemResults.GetUpperOffsetMeasurementStatus Method

RFmxWlanMXSemResultsGetUpperOffsetMeasurementStatus Method

Gets the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetMeasurementStatus(
	string selectorString,
	out RFmxWlanMXSemUpperOffsetMeasurementStatus value
)
```

```text
Public Function GetUpperOffsetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXSemUpperOffsetMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXSemUpperOffsetMeasurementStatusUpon return, contains the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMeasurementStatus

##### See Also

###### Reference

RFmxWlanMXSemResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d50b20d4-2eb8-9170-2387-2713d0519ec3.htm language=enus -->
## TOPIC 00234: rfmxwlandotnet/html/d50b20d4-2eb8-9170-2387-2713d0519ec3.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d50b20d4-2eb8-9170-2387-2713d0519ec3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d50b20d4-2eb8-9170-2387-2713d0519ec3.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccEhtSigCrcStatus Enumeration

RFmxWlanMXOfdmModAccEhtSigCrcStatus Enumeration

Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccEhtSigCrcStatus
```

```text
Public Enumeration RFmxWlanMXOfdmModAccEhtSigCrcStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | NotApplicable | -1 | Returns that the EHT-SIG CRC is invalid for the current waveform. |
|  | Fail | 0 | Returns that the EHT-SIG CRC failed. |
|  | Pass | 1 | Returns that the EHT-SIG CRC passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d50c2b63-ba07-79f4-7fc1-f53ed6dae34c.htm language=enus -->
## TOPIC 00235: rfmxwlandotnet/html/d50c2b63-ba07-79f4-7fc1-f53ed6dae34c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d50c2b63-ba07-79f4-7fc1-f53ed6dae34c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d50c2b63-ba07-79f4-7fc1-f53ed6dae34c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.BuildGateString Method

RFmxWlanMXBuildGateString Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildGateString(
	string selectorString,
	int gateNumber
)
```

```text
Public Shared Function BuildGateString ( 
	selectorString As String,
	gateNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: """""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **gateNumber**
  - Type: SystemInt32 Specifies the gate number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d65d600b-9bd0-4332-786d-b3912dc45a67.htm language=enus -->
## TOPIC 00236: rfmxwlandotnet/html/d65d600b-9bd0-4332-786d-b3912dc45a67.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d65d600b-9bd0-4332-786d-b3912dc45a67.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d65d600b-9bd0-4332-786d-b3912dc45a67.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmRUOffsetMruIndex Method

RFmxWlanMXSetOfdmRUOffsetMruIndex Method

Sets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs.
If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of
 IEEE P802.11be/D6.0
 .

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmRUOffsetMruIndex(
	string selectorString,
	int value
)
```

```text
Public Function SetOfdmRUOffsetMruIndex ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the user number. Example: "user0". You can use the BuildUserString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the location of or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0 .

###### Return Value

Int32

##### Remarks

OfdmRUOffsetMruIndex

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d6cd4ce2-e6d0-8fdf-5806-7abdbf06c5ce.htm language=enus -->
## TOPIC 00237: rfmxwlandotnet/html/d6cd4ce2-e6d0-8fdf-5806-7abdbf06c5ce.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d6cd4ce2-e6d0-8fdf-5806-7abdbf06c5ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d6cd4ce2-e6d0-8fdf-5806-7abdbf06c5ce.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXDsssModAccConfiguration.GetAllTracesEnabled Method

RFmxWlanMXDsssModAccConfigurationGetAllTracesEnabled Method

Gets whether to enable all the traces computed by DSSSModAcc measurement.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanUpon return, contains whether to enable all the traces computed by DSSSModAcc measurement.

###### Return Value

Int32

##### Remarks

DsssModAccAllTracesEnabled

##### See Also

###### Reference

RFmxWlanMXDsssModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d8a5472d-3c76-0446-d6e8-e2ea27dcdd63.htm language=enus -->
## TOPIC 00238: rfmxwlandotnet/html/d8a5472d-3c76-0446-d6e8-e2ea27dcdd63.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d8a5472d-3c76-0446-d6e8-e2ea27dcdd63.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d8a5472d-3c76-0446-d6e8-e2ea27dcdd63.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.AutoLevel Method

RFmxWlanMXAutoLevel Method

SetReferenceLevel(String, Double)

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

SetAutoLevelInitialReferenceLevel(String, Double)

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int AutoLevel(
	string selectorString,
	double measurementInterval
)
```

```text
Public Function AutoLevel ( 
	selectorString As String,
	measurementInterval As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementInterval**
  - Type: SystemDouble Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level method does not use any trigger for acquisition. It ignores the user-configured trigger methods. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal.

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d8ef1b06-88af-0cb0-41fd-faf5b712f12d.htm language=enus -->
## TOPIC 00239: rfmxwlandotnet/html/d8ef1b06-88af-0cb0-41fd-faf5b712f12d.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d8ef1b06-88af-0cb0-41fd-faf5b712f12d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d8ef1b06-88af-0cb0-41fd-faf5b712f12d.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.GetMeasurementEnabled Method

RFmxWlanMXOfdmModAccConfigurationGetMeasurementEnabled Method

Gets whether to enable OFDMModAcc measurement for OFDM based standards.

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemBooleanUpon return, contains whether to enable OFDMModAcc measurement for OFDM based standards.

###### Return Value

Int32

##### Remarks

OfdmModAccMeasurementEnabled

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/d9efd287-2772-4447-c8bf-7ff627374892.htm language=enus -->
## TOPIC 00240: rfmxwlandotnet/html/d9efd287-2772-4447-c8bf-7ff627374892.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/d9efd287-2772-4447-c8bf-7ff627374892.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/d9efd287-2772-4447-c8bf-7ff627374892.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.FetchSymbolClockErrorMean Method

RFmxWlanMXOfdmModAccResultsFetchSymbolClockErrorMean Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSymbolClockErrorMean(
	string selectorString,
	double timeout,
	out double symbolClockErrorMean
)
```

```text
Public Function FetchSymbolClockErrorMean ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef symbolClockErrorMean As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and segment number. Example: "segment0""result::r1/segment0" You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds.
- **symbolClockErrorMean**
  - Type: SystemDouble Upon return, contains the symbol clock error of the transmitter. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the symbol clock error results computed for each averaging count. This value is expressed in parts per million (ppm).

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/da3d1bf5-ac5e-e070-98ca-6bfc7b34f930.htm language=enus -->
## TOPIC 00241: rfmxwlandotnet/html/da3d1bf5-ac5e-e070-98ca-6bfc7b34f930.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/da3d1bf5-ac5e-e070-98ca-6bfc7b34f930.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/da3d1bf5-ac5e-e070-98ca-6bfc7b34f930.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccChannelEstimationType Enumeration

RFmxWlanMXOfdmModAccChannelEstimationType Enumeration

Specifies the fields in the PPDU used to estimate the channel frequency response.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccChannelEstimationType
```

```text
Public Enumeration RFmxWlanMXOfdmModAccChannelEstimationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Reference | 0 | The channel is estimated using long training fields (LTFs) in the preamble and the most recently received midamble, if present. |
|  | ReferenceAndData | 1 | The channel is estimated using long training fields (LTFs) in the preamble, the midamble (if present), and the data field. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/db10ea64-566b-05fa-4e07-7b406785853c.htm language=enus -->
## TOPIC 00242: rfmxwlandotnet/html/db10ea64-566b-05fa-4e07-7b406785853c.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/db10ea64-566b-05fa-4e07-7b406785853c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/db10ea64-566b-05fa-4e07-7b406785853c.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.GetOfdmPhaseRotationCoefficient1 Method

RFmxWlanMXGetOfdmPhaseRotationCoefficient1 Method

IEEE Standard P802.11be/D6.0

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOfdmPhaseRotationCoefficient1(
	string selectorString,
	out RFmxWlanMXOfdmPhaseRotationCoefficient1 value
)
```

```text
Public Function GetOfdmPhaseRotationCoefficient1 ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmPhaseRotationCoefficient1
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmPhaseRotationCoefficient1 Upon return, contains the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D6.0 .

###### Return Value

Int32

##### Remarks

OfdmPhaseRotationCoefficient1

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/dc80039d-c5cb-4a02-ae58-c34c08a627b2.htm language=enus -->
## TOPIC 00243: rfmxwlandotnet/html/dc80039d-c5cb-4a02-ae58-c34c08a627b2.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/dc80039d-c5cb-4a02-ae58-c34c08a627b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/dc80039d-c5cb-4a02-ae58-c34c08a627b2.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccSigCrcStatus Enumeration

RFmxWlanMXOfdmModAccSigCrcStatus Enumeration

Returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxWlanMXOfdmModAccSigCrcStatus
```

```text
Public Enumeration RFmxWlanMXOfdmModAccSigCrcStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | NotApplicable | -1 | Returns that the SIG CRC is invalid for the current waveform. |
|  | Fail | 0 | Returns that the SIG CRC failed. |
|  | Pass | 1 | Returns that the SIG CRC passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/de8a4426-b20c-5466-507e-633bd6c5aba8.htm language=enus -->
## TOPIC 00244: rfmxwlandotnet/html/de8a4426-b20c-5466-507e-633bd6c5aba8.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/de8a4426-b20c-5466-507e-633bd6c5aba8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/de8a4426-b20c-5466-507e-633bd6c5aba8.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetIQPowerEdgeTriggerSource Method

RFmxWlanMXSetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxWlanMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.WlanMX

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
  - Type: SystemString Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxWlanMXTriggerType) method to IQPowerEdge .

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/de906110-9dd6-63cb-b292-4743aa4ad9b3.htm language=enus -->
## TOPIC 00245: rfmxwlandotnet/html/de906110-9dd6-63cb-b292-4743aa4ad9b3.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/de906110-9dd6-63cb-b292-4743aa4ad9b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/de906110-9dd6-63cb-b292-4743aa4ad9b3.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccConfiguration.ConfigureAveraging Method

RFmxWlanMXOfdmModAccConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxWlanMXOfdmModAccAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxWlanMXOfdmModAccAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmModAccAveragingEnabledSpecifies whether to enable averaging for OFDMModAcc measurements.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True .

###### Return Value

Int32

##### See Also

###### Reference

RFmxWlanMXOfdmModAccConfiguration Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/debaf706-d88e-eaab-92ac-d8b8c5aae248.htm language=enus -->
## TOPIC 00246: rfmxwlandotnet/html/debaf706-d88e-eaab-92ac-d8b8c5aae248.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/debaf706-d88e-eaab-92ac-d8b8c5aae248.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/debaf706-d88e-eaab-92ac-d8b8c5aae248.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetGuardIntervalType Method

RFmxWlanMXOfdmModAccResultsGetGuardIntervalType Method

Gets the size of the guard interval of OFDM symbols.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetGuardIntervalType(
	string selectorString,
	out RFmxWlanMXOfdmGuardIntervalType value
)
```

```text
Public Function GetGuardIntervalType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxWlanMXOfdmGuardIntervalType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name. Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.WlanMXRFmxWlanMXOfdmGuardIntervalTypeUpon return, contains the size of the guard interval of OFDM symbols.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsGuardIntervalType

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/deca6034-aa1d-71b3-cab3-24b5721a77f9.htm language=enus -->
## TOPIC 00247: rfmxwlandotnet/html/deca6034-aa1d-71b3-cab3-24b5721a77f9.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/deca6034-aa1d-71b3-cab3-24b5721a77f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/deca6034-aa1d-71b3-cab3-24b5721a77f9.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults Class

RFmxWlanMXOfdmModAccResults Class

Provides methods to fetch and read the OFDMModAcc measurement results.

##### Inheritance Hierarchy

RFmxWlanMXSubObject

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxWlanMXOfdmModAccResults : RFmxWlanMXSubObject
```

```text
Public NotInheritable Class RFmxWlanMXOfdmModAccResults
	Inherits RFmxWlanMXSubObject
```

The RFmxWlanMXOfdmModAccResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchChainDataRmsEvmPerSymbolMeanTrace | Fetches the chain data-subcarriers RMS EVM per symbol trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the chain data RMS EVM per symbol computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchChainPilotRmsEvmPerSymbolMeanTrace | Fetches the chain pilot-subcarriers RMS EVM per symbol trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the chain pilot RMS EVM per symbol computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchChainRmsEvm | Fetches the chain RMS EVM results. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchChainRmsEvmPerSubcarrierMeanTrace | Fetches the chain RMS EVM per subcarrier trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the chain RMS EVM per subcarrier computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchChainRmsEvmPerSymbolMeanTrace | Fetches the chain RMS EVM per symbol trace. When you set the When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the chain RMS EVM per symbol computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchChannelFrequencyResponseMeanTrace | Fetches the channel frequency response trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the channel frequency response trace computed for each averaging count. Use "segment(n)/chain(k)/stream(l)" as the selector string to read results from this method. |
|  | FetchCommonPilotErrorTrace | Fetches the common pilot error magnitude and phase traces. Use "segment(n)" as the selector string to read results from this method. |
|  | FetchCompositeRmsEvm | Fetches the composite RMS EVM results. |
|  | FetchCrossPower | Fetches the cross power. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchCustomGatePowersArray | Fetches the average and peak power of the custom gates. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchDataAveragePower | Fetches the average power of the data field. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchDataConstellationTrace | Fetches the constellation trace for the data-subcarriers. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchDataPeakPower | Fetches the peak power of the data field. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchDecodedEhtSigBitsTrace | Fetches the decoded EHT-SIG bits trace. |
|  | FetchDecodedLSigBitsTrace | Fetches the decoded L-SIG bits trace. |
|  | FetchDecodedPsduBitsTrace | Fetches the decoded PLCP service data unit (PSDU) bits. |
|  | FetchDecodedServiceBitsTrace | Fetches the decoded Service bits. |
|  | FetchDecodedSigBBitsTrace | Fetches the decoded SIG-B bits. |
|  | FetchDecodedSigBitsTrace | Fetches the decoded SIG bits. |
|  | FetchDecodedUSigBitsTrace | Fetches the decoded U-SIG bits trace. |
|  | FetchEvmSubcarrierIndices | Fetches the array of subcarrier indices for which the EVM results are computed. |
|  | FetchFrequencyErrorCcdf10Percent | Fetches the 10% point of the complementary cumulative distribution method (CCDF) of frequency error across the number of iterations. Use "segment(n)" as the selector string to read results from this method. |
|  | FetchFrequencyErrorMean | Fetches the carrier frequency error of the transmitter. Use "segment(n)" as the selector string to read results from this method. |
|  | FetchGroupDelayMeanTrace | Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the group delay trace computed for each averaging count. Use "segment(n)/chain(k)/stream(l)" as the selector string to read results from this method. |
|  | FetchGuardIntervalType | Fetches the guard interval type. |
|  | FetchIQGainImbalancePerSubcarrierMeanTrace | Fetches the I/Q gain imbalance per subcarrier trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the I/Q gain imbalance computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchIQImpairments | Fetches the I/Q Impairment results for the OFDMModAcc measurement. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchIQQuadratureErrorPerSubcarrierMeanTrace | Fetches the I/Q quadrature error per subcarrier trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the I/Q quadrature error computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchLSigParityCheckStatus | Fetches the L-SIG parity check status. |
|  | FetchLtfSize | Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively. |
|  | FetchMcsIndex | Fetches the MCS index. Use "user(n)" as the selector string to read results from this method. |
|  | FetchNumberOfHESigBSymbols | Fetches the number of HE-SIG-B symbols. |
|  | FetchNumberOfSpaceTimeStreams | Fetches the number of space time streams. Use "user(n)" as the selector string to read results from this method. |
|  | FetchNumberOfSymbolsUsed | Fetches the number of OFDM symbols used for EVM measurement. |
|  | FetchNumberOfUsers | Fetches the number of users. |
|  | FetchPEAveragePower | Fetches the average power of the packet extension field. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPEDuration | Fetches the duration of the packet extension field. |
|  | FetchPEPeakPower | Fetches the peak power of the packet extension field. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPhaseNoisePsdMeanTrace | Fetches the phase noise power spectral density (PSD) trace for signals containing an OFDM payload. Phase noise estimates are derived from the common pilot error estimates. When you set the OfdmModAccAveragingEnabled property to True, this method returns the mean of the phase noise PSD computed for each averaging count. |
|  | FetchPilotConstellationTrace | Fetches the constellation trace for the pilot-subcarriers. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchPpduAveragePower | Fetches the average power of the PPDU. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPpduPeakPower | Fetches the peak power of the PPDU. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPpduType | Fetches the PPDU type. |
|  | FetchPreambleAveragePowers802_11ac | Fetches the average power of the 802.11ac specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreambleAveragePowers802_11ax | Fetches the average power of the 802.11ax specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreambleAveragePowers802_11be | Fetches the average power of the 802.11be specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreambleAveragePowers802_11n | Fetches the average power of the 802.11n specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreambleAveragePowersCommon | Fetches the average power of the preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreambleFrequencyErrorTrace | Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols. |
|  | FetchPreamblePeakPowers802_11ac | Fetches the peak power of the 802.11ac specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreamblePeakPowers802_11ax | Fetches the peak power of the 802.11ax specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreamblePeakPowers802_11be | Fetches the peak power of the 802.11be specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreamblePeakPowers802_11n | Fetches the peak power of the 802.11n specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPreamblePeakPowersCommon | Fetches the peak power of the preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchPsduCrcStatus | Fetches the PLCP service data unit (PSDU) CRC status. |
|  | FetchRUOffsetAndSize | Fetches the RU offset and the RU size of the specified user. Use "user(n)" as the selector string to read results from this method. |
|  | FetchSigBCrcStatus | Fetches the SIG-B CRC Status. |
|  | FetchSigCrcStatus | Fetches the SIG CRC Status. |
|  | FetchSpectralFlatness | Fetches the spectral flatness margin results. Use "segment(n)/chain(k)/stream(l)" as the selector string to read results from this method. |
|  | FetchSpectralFlatnessMeanTrace | Fetches the spectral flatness trace, and the lower and upper spectral flatness mask traces. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the spectral flatness trace computed on the mean of the channel estimates computed for each averaging count. Use "segment(n)/chain(k)/stream(l)" as the selector string to read results from this method. |
|  | FetchStreamDataRmsEvmPerSymbolMeanTrace | Fetches the stream data subcarriers RMS EVM per symbol trace. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchStreamPilotRmsEvmPerSymbolMeanTrace | Fetches the stream pilot subcarriers RMS EVM per symbol trace. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchStreamRmsEvm | Fetches the stream RMS EVM results. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchStreamRmsEvmPerSubcarrierMeanTrace | Fetches the stream RMS EVM per subcarrier trace. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchStreamRmsEvmPerSymbolMeanTrace | Fetches the stream RMS EVM per symbol trace. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchSubcarrierChainEvmPerSymbolTrace | Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchSubcarrierStreamEvmPerSymbolTrace | Fetches the stream EVM per symbol trace for a subcarrier. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchSymbolChainEvmPerSubcarrierTrace | Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchSymbolClockErrorMean | Fetches the symbol clock error of the transmitter. Use "segment(n)" as the selector string to read results from this method. |
|  | FetchSymbolStreamEvmPerSubcarrierTrace | Fetches the stream EVM per subcarrier trace for a symbol. Use "segment(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUnusedToneError | Fetches the unused tone error margin results. Refer to Unused Tone Error Measurement for more information. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchUnusedToneErrorMarginPerRU | Fetches the unused tone error margin result per RU. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchUnusedToneErrorMeanTrace | Fetches the unused tone error trace and the unused tone error mask trace. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the unused tone error computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
|  | FetchUserDataConstellationTrace | Fetches the constellation trace for the data-subcarriers of each user. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUserPilotConstellationTrace | Fetches the constellation trace for the pilot-subcarriers of each user. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUserPower | Fetches the user power. Use "user(n)" as the selector string to read results from this method. |
|  | FetchUserStreamDataRmsEvmPerSymbolMeanTrace | Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUserStreamPilotRmsEvmPerSymbolMeanTrace | Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUserStreamRmsEvm | Fetches the stream RMS EVM results for the specified user. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUserStreamRmsEvmPerSubcarrierMeanTrace | Fetches the stream RMS EVM per subcarrier trace for each user. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | FetchUserStreamRmsEvmPerSymbolMeanTrace | Fetches the stream RMS EVM per symbol trace for each user. When you set the SetAveragingEnabled(String, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the user stream RMS EVM per symbol computed for each averaging count. Use "user(n)/stream(k)" as the selector string to read results from this method. |
|  | GetAbsoluteIQOriginOffsetMean | Gets the absolute I/Q origin offset, which is the power of the DC subcarrier. This value is expressed in dBm. |
|  | GetAggregation | Gets the value of the Aggregation field as decoded from the high-throughput signal (HT-SIG) field of 802.11n signal. |
|  | GetBurstStartTimeMean | Returns the absolute time corresponding to the detected start of the analyzed burst. The start time is computed with respect to the initial time value of the acquired waveform. This value is expressed in seconds. |
|  | GetChainDataRmsEvmMean | Gets the chain RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetChainPilotRmsEvmMean | Gets the chain RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetChainRmsEvmMean | Gets the chain RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetCompositeDataRmsEvmMean | Gets the RMS EVM of data-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetCompositePilotRmsEvmMean | Gets the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetCompositeRmsEvmMean | Gets the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetCrossPowerMean | Gets the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. This value is expressed in dB. |
|  | GetCustomGateAveragePowerMean | Gets the average power of the custom gate. This value is expressed in dBm. |
|  | GetCustomGatePeakPowerMaximum | Gets the peak power of the custom gate. This value is expressed in dBm. |
|  | GetDataAveragePowerMean | Gets the average power of the data field. This value is expressed in dBm. |
|  | GetDataPeakPowerMaximum | Gets the peak power of the data field. This value is expressed in dBm. |
|  | GetDcmEnabled | Gets whether DCM is enabled for a specified user. |
|  | GetEhtLtfAveragePowerMean | Gets the average power of the EHT-LTF field. This value is expressed in dBm. |
|  | GetEhtLtfPeakPowerMaximum | Gets the peak power of the EHT-LTF field. This value is expressed in dBm. |
|  | GetEhtSigAveragePowerMean | Gets the average power of the EHT-SIG field. This value is expressed in dBm. |
|  | GetEhtSigCrcStatus | Gets whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform. |
|  | GetEhtSigPeakPowerMaximum | Gets the peak power of the EHT-SIG field. This value is expressed in dBm. |
|  | GetEhtSigRmsEvmMean | Gets the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB. |
|  | GetEhtStfAveragePowerMean | Gets the average power of the EHT-STF field. This value is expressed in dBm. |
|  | GetEhtStfPeakPowerMaximum | Gets the peak power of the EHT-STF field. This value is expressed in dBm. |
|  | GetFecCodingType | Gets the FEC coding type for a specified user. |
|  | GetFrequencyErrorCcdf10Percent | Gets the 10% point of Complementary Cumulative Distribution Function (CCDF) of the absolute frequency error. This value is expressed in Hz. |
|  | GetFrequencyErrorMean | Gets the carrier frequency error of the transmitter. This value is expressed in Hz. |
|  | GetGuardIntervalType | Gets the size of the guard interval of OFDM symbols. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetHELtfAveragePowerMean | Gets the average power of the HE-LTF field. This value is expressed in dBm. |
|  | GetHELtfPeakPowerMaximum | Gets the peak power of the HE-LTF field. This value is expressed in dBm. |
|  | GetHESigAAveragePowerMean | Gets the average power of the HE-SIG-A field. This value is expressed in dBm. |
|  | GetHESigAPeakPowerMaximum | Gets the peak power of the HE-SIG-A field. This value is expressed in dBm. |
|  | GetHESigBAveragePowerMean | Gets the average power of the HE-SIG-B field. This value is expressed in dBm. |
|  | GetHESigBPeakPowerMaximum | Gets the peak power of the HE-SIG-B field. This value is expressed in dBm. |
|  | GetHEStfAveragePowerMean | Gets the average power of the HE-STF field. This value is expressed in dBm. |
|  | GetHEStfPeakPowerMaximum | Gets the peak power of the HE-STF field. This value is expressed in dBm. |
|  | GetHTDltfAveragePowerMean | Gets the average power of the HT-DLTF. This value is expressed in dBm. |
|  | GetHTDltfPeakPowerMaximum | Gets the peak power of the HT-DLTF field. This value is expressed in dBm. |
|  | GetHTEltfAveragePowerMean | Gets the average power of the HT-ELTF field. This value is expressed in dBm. |
|  | GetHTEltfPeakPowerMaximum | Gets the peak power of the HT-ELTF field. This value is expressed in dBm. |
|  | GetHTGFStfAveragePowerMean | Gets the average power of the HT-GF-STF. This value is expressed in dBm. |
|  | GetHTGFStfPeakPowerMaximum | Gets the peak power of the HT-GF-STF. This value is expressed in dBm. |
|  | GetHTSigAveragePowerMean | Gets the average power of the HT-SIG field. This value is expressed in dBm. |
|  | GetHTSigPeakPowerMaximum | Gets the peak power of the HT-SIG field. This value is expressed in dBm. |
|  | GetHTStfAveragePowerMean | Gets the average power of the HT-STF field. This value is expressed in dBm. |
|  | GetHTStfPeakPowerMaximum | Gets the peak power of the HT-STF field. This value is expressed in dBm. |
|  | GetIQGainImbalanceMean | Gets the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. This value is expressed in dB. |
|  | GetIQQuadratureErrorMean | Gets the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees. |
|  | GetIQTimingSkewMean | Gets the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds. |
|  | GetLLtfAveragePowerMean | Gets the average power of the L-LTF or LTF field. This value is expressed in dBm. |
|  | GetLLtfPeakPowerMaximum | Gets the peak power of the L-LTF or LTF field. This value is expressed in dBm. |
|  | GetLSigAveragePowerMean | Gets the average power of the L-SIG or SIGNAL field. This value is expressed in dBm. |
|  | GetLSigParityCheckStatus | Gets whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms. |
|  | GetLSigPeakPowerMaximum | Gets the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm. |
|  | GetLSigRmsEvmMean | Gets the RMS EVM of subcarriers in the L-SIG symbol. This value is expressed as a percentage or in dB. |
|  | GetLStfAveragePowerMean | Gets the average power of the L-STF or STF field. This value is expressed in dBm. |
|  | GetLStfPeakPowerMaximum | Gets the peak power of the L-STF or STF field. This value is expressed in dBm. |
|  | GetLtfSize | Gets the HE-LTF size or EHT-LTF size when you set the SetStandard(String, RFmxWlanMXStandard) method to Standard802_11ax or Standard802_11be , respectively. |
|  | GetMcsIndex | Gets the MCS index or the data rate of the measured signal. |
|  | GetNoiseCompensationApplied | Gets whether the noise compensation is applied. |
|  | GetNumberOfHESigBSymbols | Gets the number of HE-SIG-B symbols. |
|  | GetNumberOfSpaceTimeStreams | Gets the number of space time streams. |
|  | GetNumberOfSymbolsUsed | Gets the number of OFDM symbols used by the measurement. |
|  | GetNumberOfUsers | Gets the number of users. |
|  | GetPEAveragePowerMean | Gets the average power of the packet extension field. This value is expressed in dBm. |
|  | GetPEDuration | Gets the duration of the packet extension field for the 802.11ax and 802.11be signals. This value is expressed in seconds. |
|  | GetPEPeakPowerMaximum | Gets the peak power of the packet extension field. This value is expressed in dBm. |
|  | GetPhaseRotationCoefficient1 | Gets the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D6.0. |
|  | GetPhaseRotationCoefficient2 | Gets the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D6.0. |
|  | GetPhaseRotationCoefficient3 | Gets the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D6.0. |
|  | GetPpduAveragePowerMean | Gets the average power of the PPDU. This value is expressed in dBm. |
|  | GetPpduPeakPowerMaximum | Gets the peak power of the PPDU. This value is expressed in dBm. |
|  | GetPpduType | Gets the PPDU type of the measured signal. |
|  | GetPsduCrcStatus | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
|  | GetRelativeIQOriginOffsetMean | Gets the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB. |
|  | GetRLSigAveragePowerMean | Gets the average power of the RL-SIG field. This value is expressed in dBm. |
|  | GetRLSigPeakPowerMaximum | Gets the peak power of the RL-SIG field. This value is expressed in dBm. |
|  | GetRmsCommonPhaseErrorMean | Gets the RMS common phase error. |
|  | GetRmsCommonPilotErrorMean | Gets the RMS common pilot error. This value is expressed as a percentage. |
|  | GetRUOffsetMruIndex | Gets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in Table 36-8 to Table 36-15 of IEEE P802.11be/D6.0. |
|  | GetRUSize | Gets the RU size. |
|  | GetScramblerSeed | Gets the detected initial state of the scrambler, which is used to scramble the data bits in the device under test (DUT). RFmx uses the same seed to descramble the received bit-sequence. |
|  | GetSigBCrcStatus | Gets whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. |
|  | GetSigBRmsEvmMean | Gets the RMS EVM of subcarriers in the SIG-B symbol. This value is expressed as a percentage or in dB. |
|  | GetSigCrcStatus | Gets whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. |
|  | GetSigRmsEvmMean | Gets the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB. |
|  | GetSpaceTimeStreamOffset | Gets the space time stream offset. This method is applicable only to 802.11ax and 802.11be signals. |
|  | GetSpectralFlatnessMargin | Gets the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB. |
|  | GetSpectralFlatnessMarginSubcarrierIndex | Gets the subcarrier index corresponding to the GetSpectralFlatnessMargin(String, Double) result. |
|  | GetStreamDataRmsEvmMean | Gets the stream RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetStreamPilotRmsEvmMean | Gets the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetStreamPowerMean | Gets average stream power across iterations for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(String, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
|  | GetStreamRmsEvmMean | Gets the stream RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |
|  | GetSymbolClockErrorMean | Gets the symbol clock error of the transmitter. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUnusedToneErrorMargin | Gets the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB. |
|  | GetUnusedToneErrorMarginRUIndex | Gets the 26-tone RU index corresponding to the GetUnusedToneErrorMargin(String, Double) result. |
|  | GetUserPowerMean | Gets the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. This value is expressed in dBm. |
|  | GetUserStreamDataRmsEvmMean | Gets the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. |
|  | GetUserStreamPilotRmsEvmMean | Gets the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. |
|  | GetUserStreamRmsEvmMean | Gets the RMS EVM of all subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. |
|  | GetUSigAveragePowerMean | Gets the average power of the U-SIG field. This value is expressed in dBm. |
|  | GetUSigCrcStatus | Gets whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be waveform. |
|  | GetUSigPeakPowerMaximum | Gets the peak power of the U-SIG field. This value is expressed in dBm. |
|  | GetUSigRmsEvmMean | Gets the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB. |
|  | GetVhtLtfAveragePowerMean | Gets the average power of the VHT-LTF field. This value is expressed in dBm. |
|  | GetVhtLtfPeakPowerMaximum | Gets the peak power of the VHT-LTF field. This value is expressed in dBm. |
|  | GetVhtSigAAveragePowerMean | Gets the average power of the VHT-SIG-A field. This value is expressed in dBm. |
|  | GetVhtSigAPeakPowerMaximum | Gets the peak power of the VHT-SIG-A field. This value is expressed in dBm. |
|  | GetVhtSigBAveragePowerMean | Gets the average power of the VHT-SIG-B field. This value is expressed in dBm. |
|  | GetVhtSigBPeakPowerMaximum | Gets the peak power of the VHT-SIG-B field. This value is expressed in dBm. |
|  | GetVhtStfAveragePowerMean | Gets the average power of the VHT-STF field. This value is expressed in dBm. |
|  | GetVhtStfPeakPowerMaximum | Gets the peak power of the VHT-STF field. This value is expressed in dBm. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ded5518b-57fa-55b3-b4d1-a1a4983aad1f.htm language=enus -->
## TOPIC 00248: rfmxwlandotnet/html/ded5518b-57fa-55b3-b4d1-a1a4983aad1f.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ded5518b-57fa-55b3-b4d1-a1a4983aad1f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ded5518b-57fa-55b3-b4d1-a1a4983aad1f.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.SetOfdmLdpcExtraSymbolSegment Method

RFmxWlanMXSetOfdmLdpcExtraSymbolSegment Method

Sets the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU and 802.11be TB PPDU.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOfdmLdpcExtraSymbolSegment(
	string selectorString,
	int value
)
```

```text
Public Function SetOfdmLdpcExtraSymbolSegment ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU and 802.11be TB PPDU.

###### Return Value

Int32

##### Remarks

OfdmLdpcExtraSymbolSegment

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/ded65f1e-d7b2-0da7-5ee7-baefe618e043.htm language=enus -->
## TOPIC 00249: rfmxwlandotnet/html/ded65f1e-d7b2-0da7-5ee7-baefe618e043.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/ded65f1e-d7b2-0da7-5ee7-baefe618e043.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/ded65f1e-d7b2-0da7-5ee7-baefe618e043.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMXOfdmModAccResults.GetEhtStfPeakPowerMaximum Method

RFmxWlanMXOfdmModAccResultsGetEhtStfPeakPowerMaximum Method

Gets the peak power of the EHT-STF field. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEhtStfPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetEhtStfPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the peak power of the EHT-STF field. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

OfdmModAccResultsEhtStfPeakPowerMaximum

##### See Also

###### Reference

RFmxWlanMXOfdmModAccResults Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-wlan-dotnet path=rfmxwlandotnet/html/e05a3564-7e5c-df16-5dea-9fe1164c25c3.htm language=enus -->
## TOPIC 00250: rfmxwlandotnet/html/e05a3564-7e5c-df16-5dea-9fe1164c25c3.htm

- bundle_id: `rfmx-wlan-dotnet`
- source_path: `rfmxwlandotnet/html/e05a3564-7e5c-df16-5dea-9fe1164c25c3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-dotnet/raw/resource/enus/rfmxwlandotnet/html/e05a3564-7e5c-df16-5dea-9fe1164c25c3.htm
- document_id: `rfmx-wlan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxWlanMX.DsssModAcc Property

RFmxWlanMXDsssModAcc Property

RFmxWlanMXDsssModAcc

Namespace:

NationalInstruments.RFmx.WlanMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxWlanMXDsssModAcc DsssModAcc { get; }
```

```text
Public ReadOnly Property DsssModAcc As RFmxWlanMXDsssModAcc
	Get
```

###### Property Value

RFmxWlanMXDsssModAcc

##### See Also

###### Reference

RFmxWlanMX Class

NationalInstruments.RFmx.WlanMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
