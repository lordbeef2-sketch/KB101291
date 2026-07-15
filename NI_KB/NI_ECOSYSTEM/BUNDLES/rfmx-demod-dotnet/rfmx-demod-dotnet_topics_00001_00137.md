# NI DOCUMENT BUNDLE: rfmx-demod-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-demod-dotnet start=1 end=137 -->
<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/20d5de6d-bf7b-da3f-bf54-3dc298d17739.htm language=enus -->
## TOPIC 00001: rfmxdemoddotnet/html/20d5de6d-bf7b-da3f-bf54-3dc298d17739.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/20d5de6d-bf7b-da3f-bf54-3dc298d17739.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/20d5de6d-bf7b-da3f-bf54-3dc298d17739.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchEqualizerCoefficients Method

RFmxDemodMXDDemodResultsFetchEqualizerCoefficients Method

Fetches the updated equalizer coefficients.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEqualizerCoefficients(
	string selectorString,
	double timeout,
	out double x0,
	out double dx,
	ref ComplexSingle[] equalizerCoefficients
)
```

```text
Public Function FetchEqualizerCoefficients ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef x0 As Double,
	<OutAttribute> ByRef dx As Double,
	ByRef equalizerCoefficients As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete
- **x0 Double**
  - This parameter always returns 0.
- **dx Double**
  - Upon return, contains the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4.
- **equalizerCoefficients ComplexSingle**
  - Upon return, contains the updated coefficients.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchEqualizerCoefficients() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/20ea9f3e-b06f-32e0-68ed-1d0b1c261f9c.htm language=enus -->
## TOPIC 00002: rfmxdemoddotnet/html/20ea9f3e-b06f-32e0-68ed-1d0b1c261f9c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/20ea9f3e-b06f-32e0-68ed-1d0b1c261f9c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/20ea9f3e-b06f-32e0-68ed-1d0b1c261f9c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.SetRbwFilterBandwidth Method

RFmxDemodMXADemodConfigurationSetRbwFilterBandwidth Method

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter to be applied to the signal acquired using zero span.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetRbwFilterBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the bandwidth, in Hz, of the RBW filter to be applied to the signal acquired using zero span.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodSetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/259efda9-8eaf-1cb6-2941-7691d016980d.htm language=enus -->
## TOPIC 00003: rfmxdemoddotnet/html/259efda9-8eaf-1cb6-2941-7691d016980d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/259efda9-8eaf-1cb6-2941-7691d016980d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/259efda9-8eaf-1cb6-2941-7691d016980d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetOffsetEvmMaximumRms Method

RFmxDemodMXDDemodResultsGetOffsetEvmMaximumRms Method

Gets the maximum of the RMS EVM, as a percentage, measured per acquisition, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetEvmMaximumRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetEvmMaximumRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the RMS EVM, as a percentage, measured per acquisition.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsOffsetEVMMaximumRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/25ee447a-0c3e-7506-cc80-b05494b258f7.htm language=enus -->
## TOPIC 00004: rfmxdemoddotnet/html/25ee447a-0c3e-7506-cc80-b05494b258f7.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/25ee447a-0c3e-7506-cc80-b05494b258f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/25ee447a-0c3e-7506-cc80-b05494b258f7.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodModulationType Enumeration

RFmxDemodMXDDemodModulationType Enumeration

Specifies the digital modulation type of the signal that needs to be analyzed.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodModulationType
```

```text
Public Enumeration RFmxDemodMXDDemodModulationType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Ask | 0 | The modulation type is amplitude-shift keying (ASK). |
| Fsk | 1 | The modulation type is frequency-shift keying (FSK). |
| Psk | 2 | The modulation type is phase-shift keying (PSK). |
| Qam | 3 | The modulation type is quadrature-amplitude modulation (QAM). |
| Msk | 4 | The modulation type is minimum shift keying (MSK). |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/26bcc17c-0218-3cf7-015d-713e25377a8e.htm language=enus -->
## TOPIC 00005: rfmxdemoddotnet/html/26bcc17c-0218-3cf7-015d-713e25377a8e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/26bcc17c-0218-3cf7-015d-713e25377a8e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/26bcc17c-0218-3cf7-015d-713e25377a8e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetAutoLevelInitialReferenceLevel Method

RFmxDemodMXGetAutoLevelInitialReferenceLevel Method

pk-pk

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoLevelInitialReferenceLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetAutoLevelInitialReferenceLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetAutoLevelInitialReferenceLevel() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/2c66d109-50b2-a33e-918e-16e176f04612.htm language=enus -->
## TOPIC 00006: rfmxdemoddotnet/html/2c66d109-50b2-a33e-918e-16e176f04612.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/2c66d109-50b2-a33e-918e-16e176f04612.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/2c66d109-50b2-a33e-918e-16e176f04612.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ConfigureFrequency Method

RFmxDemodMXConfigureFrequency Method

Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **centerFrequency Double**
  - Specifies the carrier frequency, in hertz (Hz), of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_CfgFrequency() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/33ba1b37-219f-f40f-779b-57241d70e643.htm language=enus -->
## TOPIC 00007: rfmxdemoddotnet/html/33ba1b37-219f-f40f-779b-57241d70e643.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/33ba1b37-219f-f40f-779b-57241d70e643.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/33ba1b37-219f-f40f-779b-57241d70e643.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants.TimerEvent Field

RFmxDemodMXConstantsTimerEvent Field

The trigger is received from the timer event.

Namespace:

NationalInstruments.RFmx.DemodMX

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

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/34937865-3e01-2054-31dd-8ab958e98c4e.htm language=enus -->
## TOPIC 00008: rfmxdemoddotnet/html/34937865-3e01-2054-31dd-8ab958e98c4e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/34937865-3e01-2054-31dd-8ab958e98c4e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/34937865-3e01-2054-31dd-8ab958e98c4e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetPulseShapingFilterParameter Method

RFmxDemodMXDDemodConfigurationGetPulseShapingFilterParameter Method

Gets the rolloff factor for raised cosine and root raised cosine filter, which are used as pulse shaping filter and measurement filter, respectively.

Namespace:

NationalInstruments.RFmx.DemodMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the rolloff factor for raised cosine and root raised cosine filter, which are used as pulse shaping filter and measurement filter. For Gaussian filter, this parameter specifies the Bandwidth*Sample Duration.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetPulseShapingFilterParameter() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/34dca40e-8c87-84f6-f65e-f2f5174ca34c.htm language=enus -->
## TOPIC 00009: rfmxdemoddotnet/html/34dca40e-8c87-84f6-f65e-f2f5174ca34c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/34dca40e-8c87-84f6-f65e-f2f5174ca34c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/34dca40e-8c87-84f6-f65e-f2f5174ca34c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetAttributeString Method

RFmxDemodMXGetAttributeString Method

Gets the value of a string attribute.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value String**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetAttributeString() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/35e43092-83dd-fc5e-1f74-5e47a21169d6.htm language=enus -->
## TOPIC 00010: rfmxdemoddotnet/html/35e43092-83dd-fc5e-1f74-5e47a21169d6.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/35e43092-83dd-fc5e-1f74-5e47a21169d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/35e43092-83dd-fc5e-1f74-5e47a21169d6.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetAMModulationDepthMaximumNegativePeak Method

RFmxDemodMXADemodResultsGetAMModulationDepthMaximumNegativePeak Method

Gets the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMModulationDepthMaximumNegativePeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetAMModulationDepthMaximumNegativePeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumNegativePeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/3902107f-3cda-eb62-fc04-061a1ded2a51.htm language=enus -->
## TOPIC 00011: rfmxdemoddotnet/html/3902107f-3cda-eb62-fc04-061a1ded2a51.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/3902107f-3cda-eb62-fc04-061a1ded2a51.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/3902107f-3cda-eb62-fc04-061a1ded2a51.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetAveragingEnabled Method

RFmxDemodMXDDemodConfigurationGetAveragingEnabled Method

Gets whether averaging is enabled for digital demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxDemodMXDDemodAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXDDemodAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodAveragingEnabled**
  - Upon return, contains the value that indicates that the averaging for the measurement is enabled.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/3bc43394-ceb0-b9ba-614a-3902013f2f0a.htm language=enus -->
## TOPIC 00012: rfmxdemoddotnet/html/3bc43394-ceb0-b9ba-614a-3902013f2f0a.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/3bc43394-ceb0-b9ba-614a-3902013f2f0a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/3bc43394-ceb0-b9ba-614a-3902013f2f0a.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetMeasurementEnabled Method

RFmxDemodMXADemodConfigurationGetMeasurementEnabled Method

Gets whether the analog demodulation measurement is enabled.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - if analog demodulation measurement is enabled; otherwise, .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/3c9094e3-9de5-07fe-e869-48c55d4e7db2.htm language=enus -->
## TOPIC 00013: rfmxdemoddotnet/html/3c9094e3-9de5-07fe-e869-48c55d4e7db2.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/3c9094e3-9de5-07fe-e869-48c55d4e7db2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/3c9094e3-9de5-07fe-e869-48c55d4e7db2.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SendSoftwareEdgeTrigger Method

RFmxDemodMXSendSoftwareEdgeTrigger Method

ConfigureSoftwareEdgeTrigger(String, Double, Boolean)

Namespace:

NationalInstruments.RFmx.DemodMX

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

##### Remarks

This method maps to the RFmxDemod_SendSoftwareEdgeTrigger() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4563df09-6a2a-76c3-c8c7-3cd5654b6b6c.htm language=enus -->
## TOPIC 00014: rfmxdemoddotnet/html/4563df09-6a2a-76c3-c8c7-3cd5654b6b6c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4563df09-6a2a-76c3-c8c7-3cd5654b6b6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4563df09-6a2a-76c3-c8c7-3cd5654b6b6c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetAudioMeasurementEnabled Method

RFmxDemodMXADemodConfigurationGetAudioMeasurementEnabled Method

Gets whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAudioMeasurementEnabled(
	string selectorString,
	out RFmxDemodMXADemodAudioMeasurementEnabled value
)
```

```text
Public Function GetAudioMeasurementEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXADemodAudioMeasurementEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXADemodAudioMeasurementEnabled**
  - Upon return, contains the value that indicates whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetAudioMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/45d62d51-5999-4f4f-b75b-75e1bf107b67.htm language=enus -->
## TOPIC 00015: rfmxdemoddotnet/html/45d62d51-5999-4f4f-b75b-75e1bf107b67.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/45d62d51-5999-4f4f-b75b-75e1bf107b67.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/45d62d51-5999-4f4f-b75b-75e1bf107b67.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetSynchronizationBits Method

RFmxDemodMXDDemodConfigurationGetSynchronizationBits Method

Gets the synchronization bits used to create the reference sequence that needs to be searched in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSynchronizationBits(
	string selectorString,
	ref sbyte[] value
)
```

```text
Public Function GetSynchronizationBits ( 
	selectorString As String,
	ByRef value As SByte()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value SByte**
  - [Missing <param name="value"/> documentation for "M:NationalInstruments.RFmx.DemodMX.RFmxDemodMXDDemodConfiguration.GetSynchronizationBits(System.String,System.SByte[]@)"]

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetSynchronizationBits() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4910b482-99c7-f2cc-7fdd-5228662f024d.htm language=enus -->
## TOPIC 00016: rfmxdemoddotnet/html/4910b482-99c7-f2cc-7fdd-5228662f024d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4910b482-99c7-f2cc-7fdd-5228662f024d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4910b482-99c7-f2cc-7fdd-5228662f024d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SetTriggerDelay Method

RFmxDemodMXSetTriggerDelay Method

Sets the trigger delay time, in seconds.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value Double**
  - Specifies the trigger delay time, in seconds.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_SetTriggerDelay() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/49f89d2d-7bd5-016b-7dd2-805a67252f10.htm language=enus -->
## TOPIC 00017: rfmxdemoddotnet/html/49f89d2d-7bd5-016b-7dd2-805a67252f10.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/49f89d2d-7bd5-016b-7dd2-805a67252f10.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/49f89d2d-7bd5-016b-7dd2-805a67252f10.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetAMModulationDepthMeanNegativePeak Method

RFmxDemodMXADemodResultsGetAMModulationDepthMeanNegativePeak Method

Gets the mean negative peak amplitude of the modulating signal, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMModulationDepthMeanNegativePeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetAMModulationDepthMeanNegativePeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean negative peak amplitude of the modulating signal, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanNegativePeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4a35220f-625c-19be-619f-ebecd8bd0520.htm language=enus -->
## TOPIC 00018: rfmxdemoddotnet/html/4a35220f-625c-19be-619f-ebecd8bd0520.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4a35220f-625c-19be-619f-ebecd8bd0520.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4a35220f-625c-19be-619f-ebecd8bd0520.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetAMModulationDepthMaximumRms Method

RFmxDemodMXADemodResultsGetAMModulationDepthMaximumRms Method

Gets the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMModulationDepthMaximumRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetAMModulationDepthMaximumRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of all RMS values in multiple acquisitions, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4be377f2-e21f-9ee8-6991-93fa3bbee11f.htm language=enus -->
## TOPIC 00019: rfmxdemoddotnet/html/4be377f2-e21f-9ee8-6991-93fa3bbee11f.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4be377f2-e21f-9ee8-6991-93fa3bbee11f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4be377f2-e21f-9ee8-6991-93fa3bbee11f.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXExtension Class

RFmxDemodMXExtension Class

Provides extension methods to create Demod signal configuration. These methods are added to RFmxInstrMX class.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxDemodMXExtension
```

```text
<ExtensionAttribute>
Public NotInheritable Class RFmxDemodMXExtension
```

The RFmxDemodMXExtension type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetDemodSignalConfiguration(RFmxInstrMX) | Returns a new default Demod signal configuration if a default signal does not exists, or returns the existing default Demod signal configuration. |
|  | GetDemodSignalConfiguration(RFmxInstrMX, String) | Returns a Demod signal configuration for a specified signal name. An existing Demod signal configuration is returned if the specified signal name exists. |

Top

##### Remarks

For more info

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4dc90d25-e18d-5485-7e75-14d3ed46a4eb.htm language=enus -->
## TOPIC 00020: rfmxdemoddotnet/html/4dc90d25-e18d-5485-7e75-14d3ed46a4eb.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4dc90d25-e18d-5485-7e75-14d3ed46a4eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4dc90d25-e18d-5485-7e75-14d3ed46a4eb.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetAttributeSByteArray Method

RFmxDemodMXGetAttributeSByteArray Method

Gets the value of a signed byte array attribute.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeSByteArray(
	string selectorString,
	int attributeIdentifier,
	ref sbyte[] value
)
```

```text
Public Function GetAttributeSByteArray ( 
	selectorString As String,
	attributeIdentifier As Integer,
	ByRef value As SByte()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value SByte**
  - Contains the value of the specified attribute ID.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetAttributeI8Array() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4efd8cfc-bd88-1484-8702-34783e6ec9c5.htm language=enus -->
## TOPIC 00021: rfmxdemoddotnet/html/4efd8cfc-bd88-1484-8702-34783e6ec9c5.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4efd8cfc-bd88-1484-8702-34783e6ec9c5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4efd8cfc-bd88-1484-8702-34783e6ec9c5.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemod Methods

RFmxDemodMXADemod Methods

The [RFmxDemodMXADemod](5794347b-3f0d-8385-d5a3-a5718198f4f8.htm) type exposes the following members.

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

RFmxDemodMXADemod Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/4f754101-e200-c0b0-ec44-8aeb8cab3f69.htm language=enus -->
## TOPIC 00022: rfmxdemoddotnet/html/4f754101-e200-c0b0-ec44-8aeb8cab3f69.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/4f754101-e200-c0b0-ec44-8aeb8cab3f69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/4f754101-e200-c0b0-ec44-8aeb8cab3f69.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetIQImpairmentsMeanIQOriginOffset Method

RFmxDemodMXDDemodResultsGetIQImpairmentsMeanIQOriginOffset Method

Gets the offset, in dB, from the ideal location of the constellation origin.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQImpairmentsMeanIQOriginOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQImpairmentsMeanIQOriginOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the offset, in dB, from the ideal location of the constellation origin.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsIQImpairmentsMeanIQOriginOffset() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/50194a27-86de-7cfd-1fd9-361c57b91893.htm language=enus -->
## TOPIC 00023: rfmxdemoddotnet/html/50194a27-86de-7cfd-1fd9-361c57b91893.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/50194a27-86de-7cfd-1fd9-361c57b91893.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/50194a27-86de-7cfd-1fd9-361c57b91893.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants.PxiTriggerLine4 Field

RFmxDemodMXConstantsPxiTriggerLine4 Field

Exports the signal to the PXI trigger line 4.

Namespace:

NationalInstruments.RFmx.DemodMX

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

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/514cb361-ab38-3d36-8f6f-1438a53b56ec.htm language=enus -->
## TOPIC 00024: rfmxdemoddotnet/html/514cb361-ab38-3d36-8f6f-1438a53b56ec.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/514cb361-ab38-3d36-8f6f-1438a53b56ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/514cb361-ab38-3d36-8f6f-1438a53b56ec.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.WaitForMeasurementComplete Method

RFmxDemodMXWaitForMeasurementComplete Method

Waits for the number for seconds specified using the timeout parameter for all measurements to complete.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_WaitForMeasurementComplete() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/572b1e1c-e5d0-1532-f9c3-6967a0aa0c2e.htm language=enus -->
## TOPIC 00025: rfmxdemoddotnet/html/572b1e1c-e5d0-1532-f9c3-6967a0aa0c2e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/572b1e1c-e5d0-1532-f9c3-6967a0aa0c2e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/572b1e1c-e5d0-1532-f9c3-6967a0aa0c2e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetEvmNormalizationReference Method

RFmxDemodMXDDemodConfigurationSetEvmNormalizationReference Method

Sets the reference used to normalize the error vector magnitude (EVM).

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvmNormalizationReference(
	string selectorString,
	RFmxDemodMXDDemodEvmNormalizationReference value
)
```

```text
Public Function SetEvmNormalizationReference ( 
	selectorString As String,
	value As RFmxDemodMXDDemodEvmNormalizationReference
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodEvmNormalizationReference**
  - Specifies the reference used to normalize the EVM.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodSetEVMNormalizationReference() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/578856ce-4b96-011a-2759-b704c264982c.htm language=enus -->
## TOPIC 00026: rfmxdemoddotnet/html/578856ce-4b96-011a-2759-b704c264982c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/578856ce-4b96-011a-2759-b704c264982c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/578856ce-4b96-011a-2759-b704c264982c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetIQPowerEdgeTriggerSlope Method

RFmxDemodMXGetIQPowerEdgeTriggerSlope Method

Gets the value that indicates whether the device asserts the trigger when the signal power is rising or falling.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerSlope(
	string selectorString,
	out RFmxDemodMXIQPowerEdgeTriggerSlope value
)
```

```text
Public Function GetIQPowerEdgeTriggerSlope ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXIQPowerEdgeTriggerSlope
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value RFmxDemodMXIQPowerEdgeTriggerSlope**
  - Upon return, contains the value that indicates whether the device asserts the trigger when the signal power is rising or falling.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetIQPowerEdgeTriggerSlope() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/59834849-541f-c200-13cd-8ef8eec048c2.htm language=enus -->
## TOPIC 00027: rfmxdemoddotnet/html/59834849-541f-c200-13cd-8ef8eec048c2.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/59834849-541f-c200-13cd-8ef8eec048c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/59834849-541f-c200-13cd-8ef8eec048c2.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ConfigureReferenceLevel Method

RFmxDemodMXConfigureReferenceLevel Method

pk-pk

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureReferenceLevel(
	string selectorString,
	double referenceLevel
)
```

```text
Public Function ConfigureReferenceLevel ( 
	selectorString As String,
	referenceLevel As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **referenceLevel Double**
  - Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_CfgReferenceLevel() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/5b144f82-5df1-6911-65ee-ed52c46e9708.htm language=enus -->
## TOPIC 00028: rfmxdemoddotnet/html/5b144f82-5df1-6911-65ee-ed52c46e9708.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/5b144f82-5df1-6911-65ee-ed52c46e9708.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/5b144f82-5df1-6911-65ee-ed52c46e9708.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetEqualizerMode Method

RFmxDemodMXDDemodConfigurationGetEqualizerMode Method

Gets whether the measurement needs to perform equalization.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEqualizerMode(
	string selectorString,
	out RFmxDemodMXDDemodEqualizerMode value
)
```

```text
Public Function GetEqualizerMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXDDemodEqualizerMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodEqualizerMode**
  - Upon return, contains a value that indicates whether the measurement needs to perform equalization.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetEqualizerMode() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/5f60f835-aee5-5c4a-d33f-e7a6e7e96189.htm language=enus -->
## TOPIC 00029: rfmxdemoddotnet/html/5f60f835-aee5-5c4a-d33f-e7a6e7e96189.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/5f60f835-aee5-5c4a-d33f-e7a6e7e96189.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/5f60f835-aee5-5c4a-d33f-e7a6e7e96189.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetExternalAttenuation Method

RFmxDemodMXGetExternalAttenuation Method

Gets the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer.

Namespace:

NationalInstruments.RFmx.DemodMX

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

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetExternalAttenuation() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/604e98ef-5014-fa3d-ddf8-11899d989bd1.htm language=enus -->
## TOPIC 00030: rfmxdemoddotnet/html/604e98ef-5014-fa3d-ddf8-11899d989bd1.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/604e98ef-5014-fa3d-ddf8-11899d989bd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/604e98ef-5014-fa3d-ddf8-11899d989bd1.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodFskReferenceCompensationEnabled Enumeration

RFmxDemodMXDDemodFskReferenceCompensationEnabled Enumeration

Specifies whether the frequency-shift keying (FSK) deviation that you specify is to be compensated for gain errors, and is used to compute the FSK error.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodFskReferenceCompensationEnabled
```

```text
Public Enumeration RFmxDemodMXDDemodFskReferenceCompensationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Does not compensate for gain errors. |
| True | 1 | Compensates for gain errors. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/62eae154-95ac-c0cf-2b8d-01cabb547d1c.htm language=enus -->
## TOPIC 00031: rfmxdemoddotnet/html/62eae154-95ac-c0cf-2b8d-01cabb547d1c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/62eae154-95ac-c0cf-2b8d-01cabb547d1c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/62eae154-95ac-c0cf-2b8d-01cabb547d1c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchFskResults Method

RFmxDemodMXDDemodResultsFetchFskResults Method

Fetches frequency-shift keying (FSK) results.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFskResults(
	string selectorString,
	double timeout,
	out double meanFskDeviation,
	out double meanRmsFskError,
	out double maximumPeakFskError
)
```

```text
Public Function FetchFskResults ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanFskDeviation As Double,
	<OutAttribute> ByRef meanRmsFskError As Double,
	<OutAttribute> ByRef maximumPeakFskError As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **meanFskDeviation Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsFskError Double**
  - Upon return, contains the mean of the RMS frequency error, in hertz (Hz), of the FSK symbols measured per acquisition.
- **maximumPeakFskError Double**
  - Upon return, contains the mean peak deviation error of the FSK symbols measured per acquisition.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchFSKResults() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/637d40dc-5ac1-ffd7-c1ba-c31067cba85d.htm language=enus -->
## TOPIC 00032: rfmxdemoddotnet/html/637d40dc-5ac1-ffd7-c1ba-c31067cba85d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/637d40dc-5ac1-ffd7-c1ba-c31067cba85d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/637d40dc-5ac1-ffd7-c1ba-c31067cba85d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.ConfigureAveraging Method

RFmxDemodMXADemodConfigurationConfigureAveraging Method

Configures averaging for analog demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxDemodMXADemodAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxDemodMXADemodAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxDemodMXADemodAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxDemodMXADemodAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxDemodMXADemodAveragingEnabled**
  - Enables averaging for digital demodulation measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set SetAveragingEnabled(String, RFmxDemodMXADemodAveragingEnabled) to True.
- **averagingType RFmxDemodMXADemodAveragingType**
  - Specifies the averaging type for the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodCfgAveraging() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/63ccab6e-2948-675f-fbb5-c398b69b21dd.htm language=enus -->
## TOPIC 00033: rfmxdemoddotnet/html/63ccab6e-2948-675f-fbb5-c398b69b21dd.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/63ccab6e-2948-675f-fbb5-c398b69b21dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/63ccab6e-2948-675f-fbb5-c398b69b21dd.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ClearNamedResult Method

RFmxDemodMXClearNamedResult Method

selectorString

Namespace:

NationalInstruments.RFmx.DemodMX

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

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ClearNamedResult() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/64571ffe-3a98-298f-82c6-613a4ab77cfe.htm language=enus -->
## TOPIC 00034: rfmxdemoddotnet/html/64571ffe-3a98-298f-82c6-613a4ab77cfe.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/64571ffe-3a98-298f-82c6-613a4ab77cfe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/64571ffe-3a98-298f-82c6-613a4ab77cfe.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetFMDeviationMeanRms Method

RFmxDemodMXADemodResultsGetFMDeviationMeanRms Method

Gets the mean RMS frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMDeviationMeanRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMDeviationMeanRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean RMS frequency deviation, in Hz, of the FM signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMeanRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/648428c2-340e-1f36-f7a1-83181c8b1a40.htm language=enus -->
## TOPIC 00035: rfmxdemoddotnet/html/648428c2-340e-1f36-f7a1-83181c8b1a40.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/648428c2-340e-1f36-f7a1-83181c8b1a40.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/648428c2-340e-1f36-f7a1-83181c8b1a40.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchMeasurementWaveform(String, Double, ComplexWaveform<ComplexSingle>, Int32, Double) Method

RFmxDemodMXDDemodResultsFetchMeasurementWaveform(String, Double, ComplexWaveformComplexSingle, Int32, Double) Method

Fetches the measurement waveform.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurementWaveform(
	string selectorString,
	double timeout,
	ref ComplexWaveform<ComplexSingle> measurementWaveform,
	out int samplesPerSymbol,
	out double symbolRate
)
```

```text
Public Function FetchMeasurementWaveform ( 
	selectorString As String,
	timeout As Double,
	ByRef measurementWaveform As ComplexWaveform(Of ComplexSingle),
	<OutAttribute> ByRef samplesPerSymbol As Integer,
	<OutAttribute> ByRef symbolRate As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementWaveform ComplexWaveformComplexSingle**
  - Upon return, contains the demodulated waveform used for measurement.
- **samplesPerSymbol Int32**
  - Upon return, contains the samples per symbol used to acquire the signal for the measurement.
- **symbolRate Double**
  - Upon return, contains the symbol rate in hertz (Hz).

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchMeasurementWaveform() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

FetchMeasurementWaveform Overload

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/661366d8-d588-5cad-9d15-bf3dabbf6599.htm language=enus -->
## TOPIC 00036: rfmxdemoddotnet/html/661366d8-d588-5cad-9d15-bf3dabbf6599.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/661366d8-d588-5cad-9d15-bf3dabbf6599.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/661366d8-d588-5cad-9d15-bf3dabbf6599.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetMeasurementFilterType Method

RFmxDemodMXDDemodConfigurationSetMeasurementFilterType Method

Sets whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementFilterType(
	string selectorString,
	RFmxDemodMXDDemodMeasurementFilterType value
)
```

```text
Public Function SetMeasurementFilterType ( 
	selectorString As String,
	value As RFmxDemodMXDDemodMeasurementFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodMeasurementFilterType**
  - Specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodSetMeasurementFilterType() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/673c61cd-d38a-ce29-8ef4-abe381846173.htm language=enus -->
## TOPIC 00037: rfmxdemoddotnet/html/673c61cd-d38a-ce29-8ef4-abe381846173.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/673c61cd-d38a-ce29-8ef4-abe381846173.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/673c61cd-d38a-ce29-8ef4-abe381846173.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants Class

RFmxDemodMXConstants Class

Specifies constants for I/O terminals.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxDemodMXConstants
```

```text
Public NotInheritable Class RFmxDemodMXConstants
```

The RFmxDemodMXConstants type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | Exports the signal to the PFI 0 connector on the NI 5142. |
|  | Pfi1 | Exports the signal to the PFI 1 connector on the NI 5142 and NI 5622. |
|  | PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. |
|  | PxiStarLine | Exports the signal to the PXI star trigger line. |
|  | PxiTriggerLine0 | Exports the signal to the PXI trigger line 0. |
|  | PxiTriggerLine1 | Exports the signal to the PXI trigger line 1. |
|  | PxiTriggerLine2 | Exports the signal to the PXI trigger line 2. |
|  | PxiTriggerLine3 | Exports the signal to the PXI trigger line 3. |
|  | PxiTriggerLine4 | Exports the signal to the PXI trigger line 4. |
|  | PxiTriggerLine5 | Exports the signal to the PXI trigger line 5. |
|  | PxiTriggerLine6 | Exports the signal to the PXI trigger line 6. |
|  | PxiTriggerLine7 | Exports the signal to the PXI trigger line 7. |
|  | TimerEvent | The trigger is received from the timer event. |

Top

##### Remarks

For more information about RFmx Demod, refer to the RFmx Demod Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/679abc1d-7ed3-206b-0fdc-a95250eb28c6.htm language=enus -->
## TOPIC 00038: rfmxdemoddotnet/html/679abc1d-7ed3-206b-0fdc-a95250eb28c6.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/679abc1d-7ed3-206b-0fdc-a95250eb28c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/679abc1d-7ed3-206b-0fdc-a95250eb28c6.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetSearchLengthAuto Method

RFmxDemodMXDDemodConfigurationSetSearchLengthAuto Method

Sets whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSearchLengthAuto(
	string selectorString,
	RFmxDemodMXDDemodSearchLengthAuto value
)
```

```text
Public Function SetSearchLengthAuto ( 
	selectorString As String,
	value As RFmxDemodMXDDemodSearchLengthAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodSearchLengthAuto**
  - Specifies the synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

###### Return Value

Int32

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/67b13711-c788-dc26-2086-0ef184877fe7.htm language=enus -->
## TOPIC 00039: rfmxdemoddotnet/html/67b13711-c788-dc26-2086-0ef184877fe7.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/67b13711-c788-dc26-2086-0ef184877fe7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/67b13711-c788-dc26-2086-0ef184877fe7.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXExtension.GetDemodSignalConfiguration(RFmxInstrMX) Method

RFmxDemodMXExtensionGetDemodSignalConfiguration(RFmxInstrMX) Method

Returns a new default Demod signal configuration if a default signal does not exists, or returns the existing default Demod signal configuration.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxDemodMX GetDemodSignalConfiguration(
	this RFmxInstrMX instrSession
)
```

```text
<ExtensionAttribute>
Public Shared Function GetDemodSignalConfiguration ( 
	instrSession As RFmxInstrMX
) As RFmxDemodMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an instr session.

###### Return Value

RFmxDemodMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxDemodMXExtension Class

GetDemodSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/67d5c1b9-13c9-c36d-e3d4-bdf370e8a394.htm language=enus -->
## TOPIC 00040: rfmxdemoddotnet/html/67d5c1b9-13c9-c36d-e3d4-bdf370e8a394.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/67d5c1b9-13c9-c36d-e3d4-bdf370e8a394.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/67d5c1b9-13c9-c36d-e3d4-bdf370e8a394.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SetLimitedConfigurationChange Method

RFmxDemodMXSetLimitedConfigurationChange Method

Sets the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLimitedConfigurationChange(
	string selectorString,
	RFmxDemodMXLimitedConfigurationChange value
)
```

```text
Public Function SetLimitedConfigurationChange ( 
	selectorString As String,
	value As RFmxDemodMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXLimitedConfigurationChange**
  - Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this property can help achieve faster measurements. When you set this property to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than Disabled for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6822b2a3-4a5b-7884-1707-d38b6a7ffc0e.htm language=enus -->
## TOPIC 00041: rfmxdemoddotnet/html/6822b2a3-4a5b-7884-1707-d38b6a7ffc0e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6822b2a3-4a5b-7884-1707-d38b6a7ffc0e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6822b2a3-4a5b-7884-1707-d38b6a7ffc0e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigurePulseShapingFilterCustomCoefficients Method

RFmxDemodMXDDemodConfigurationConfigurePulseShapingFilterCustomCoefficients Method

Configures the pulse shaping filter coefficients.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigurePulseShapingFilterCustomCoefficients(
	string selectorString,
	double x0,
	double dx,
	float[] pulseShapingFilterCustomCoefficients
)
```

```text
Public Function ConfigurePulseShapingFilterCustomCoefficients ( 
	selectorString As String,
	x0 As Double,
	dx As Double,
	pulseShapingFilterCustomCoefficients As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **x0 Double**
  - Always pass 0 to this parameter. Any other values will be ignored.
- **dx Double**
  - Specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4.
- **pulseShapingFilterCustomCoefficients Single**
  - [Missing <param name="pulseShapingFilterCustomCoefficients"/> documentation for "M:NationalInstruments.RFmx.DemodMX.RFmxDemodMXDDemodConfiguration.ConfigurePulseShapingFilterCustomCoefficients(System.String,System.Double,System.Double,System.Single[])"]

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6841100a-c706-f68c-da9a-ec37db0a08aa.htm language=enus -->
## TOPIC 00042: rfmxdemoddotnet/html/6841100a-c706-f68c-da9a-ec37db0a08aa.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6841100a-c706-f68c-da9a-ec37db0a08aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6841100a-c706-f68c-da9a-ec37db0a08aa.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchMagnitudeErrorTrace Method

RFmxDemodMXDDemodResultsFetchMagnitudeErrorTrace Method

Fetches the magnitude error trace.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **magnitudeError AnalogWaveformSingle**
  - Upon return, contains the magnitude error.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchMagnitudeErrorTrace() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6af90293-1163-10d5-96a8-592f4cd166df.htm language=enus -->
## TOPIC 00043: rfmxdemoddotnet/html/6af90293-1163-10d5-96a8-592f4cd166df.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6af90293-1163-10d5-96a8-592f4cd166df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6af90293-1163-10d5-96a8-592f4cd166df.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetAudioFilterUpperCutoffFrequency Method

RFmxDemodMXADemodConfigurationGetAudioFilterUpperCutoffFrequency Method

Gets the upper cutoff frequency, in hertz (Hz), of the custom audio filter.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAudioFilterUpperCutoffFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetAudioFilterUpperCutoffFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the upper cutoff frequency, in Hz, of the custom audio filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetAudioFilterUpperCutoffFrequency() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6b4a4cce-c94c-fc93-9044-adb893a2aca5.htm language=enus -->
## TOPIC 00044: rfmxdemoddotnet/html/6b4a4cce-c94c-fc93-9044-adb893a2aca5.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6b4a4cce-c94c-fc93-9044-adb893a2aca5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6b4a4cce-c94c-fc93-9044-adb893a2aca5.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXExtension.GetDemodSignalConfiguration(RFmxInstrMX, String) Method

RFmxDemodMXExtensionGetDemodSignalConfiguration(RFmxInstrMX, String) Method

Returns a Demod signal configuration for a specified signal name. An existing Demod signal configuration is returned if the specified signal name exists.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxDemodMX GetDemodSignalConfiguration(
	this RFmxInstrMX instrSession,
	string signalName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetDemodSignalConfiguration ( 
	instrSession As RFmxInstrMX,
	signalName As String
) As RFmxDemodMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an instr session.
- **signalName String**
  - Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1"

###### Return Value

RFmxDemodMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### Remarks

This method maps to the RFmxDemod_CreateSignalConfiguration() function in C.

##### See Also

###### Reference

RFmxDemodMXExtension Class

GetDemodSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6b6c2940-8598-54c2-046c-35d0780f4913.htm language=enus -->
## TOPIC 00045: rfmxdemoddotnet/html/6b6c2940-8598-54c2-046c-35d0780f4913.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6b6c2940-8598-54c2-046c-35d0780f4913.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6b6c2940-8598-54c2-046c-35d0780f4913.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetDifferentialEnabled Method

RFmxDemodMXDDemodConfigurationSetDifferentialEnabled Method

Sets whether the symbols are differentially encoded, and applicable only to phase-shift keying (PSK) and minimum-shift keying (MSK) modulation types.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDifferentialEnabled(
	string selectorString,
	RFmxDemodMXDDemodDifferentialEnabled value
)
```

```text
Public Function SetDifferentialEnabled ( 
	selectorString As String,
	value As RFmxDemodMXDDemodDifferentialEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodDifferentialEnabled**
  - Specifies whether the symbols are differentially encoded, and is applicable only to PSK and MSK modulation types.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodSetDifferentialEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6c337d2f-ea74-da2e-9d61-bb3d8136e7db.htm language=enus -->
## TOPIC 00046: rfmxdemoddotnet/html/6c337d2f-ea74-da2e-9d61-bb3d8136e7db.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6c337d2f-ea74-da2e-9d61-bb3d8136e7db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6c337d2f-ea74-da2e-9d61-bb3d8136e7db.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigureEqualizerInitialCoefficients Method

RFmxDemodMXDDemodConfigurationConfigureEqualizerInitialCoefficients Method

Configures the equalizer coefficients.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureEqualizerInitialCoefficients(
	string selectorString,
	double x0,
	double dx,
	ComplexSingle[] equalizerInitialCoefficients
)
```

```text
Public Function ConfigureEqualizerInitialCoefficients ( 
	selectorString As String,
	x0 As Double,
	dx As Double,
	equalizerInitialCoefficients As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **x0 Double**
  - Always pass 0 to this parameter. Any other values will be ignored.
- **dx Double**
  - Specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4.
- **equalizerInitialCoefficients ComplexSingle**
  - [Missing <param name="equalizerInitialCoefficients"/> documentation for "M:NationalInstruments.RFmx.DemodMX.RFmxDemodMXDDemodConfiguration.ConfigureEqualizerInitialCoefficients(System.String,System.Double,System.Double,NationalInstruments.ComplexSingle[])"]

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodCfgEqualizerInitialCoefficients() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6c9d0bc2-3994-b87a-b94d-dcb74f8b62d3.htm language=enus -->
## TOPIC 00047: rfmxdemoddotnet/html/6c9d0bc2-3994-b87a-b94d-dcb74f8b62d3.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6c9d0bc2-3994-b87a-b94d-dcb74f8b62d3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6c9d0bc2-3994-b87a-b94d-dcb74f8b62d3.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ConfigureSoftwareEdgeTrigger Method

RFmxDemodMXConfigureSoftwareEdgeTrigger Method

Configures the software-edge trigger.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSoftwareEdgeTrigger(
	string selectorString,
	double triggerDelay,
	bool triggerEnabled
)
```

```text
Public Function ConfigureSoftwareEdgeTrigger ( 
	selectorString As String,
	triggerDelay As Double,
	triggerEnabled As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **triggerDelay Double**
  - Specifies the trigger delay time, in seconds.
- **triggerEnabled Boolean**
  - to enable the trigger; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_CfgSoftwareEdgeTrigger() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6d35a65b-5098-6849-ea16-f9a544f00992.htm language=enus -->
## TOPIC 00048: rfmxdemoddotnet/html/6d35a65b-5098-6849-ea16-f9a544f00992.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6d35a65b-5098-6849-ea16-f9a544f00992.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6d35a65b-5098-6849-ea16-f9a544f00992.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetCarrierMeanPhaseError Method

RFmxDemodMXDDemodResultsGetCarrierMeanPhaseError Method

Gets the phase offset, in degrees, from the transmitted carrier phase.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierMeanPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierMeanPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the phase offset, in degrees, from the transmitted carrier phase.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsCarrierMeanPhaseError() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6e619f5c-2301-2bc8-6187-2caa4219539f.htm language=enus -->
## TOPIC 00049: rfmxdemoddotnet/html/6e619f5c-2301-2bc8-6187-2caa4219539f.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6e619f5c-2301-2bc8-6187-2caa4219539f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6e619f5c-2301-2bc8-6187-2caa4219539f.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetWarning Method

RFmxDemodMXGetWarning Method

Retrieves and then clears the warning information for the session.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Upon return, contains the warning code for the session.
- **warningDescription String**
  - Upon return, contains the warning description for the session.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetError() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6eafe841-d62f-4fb2-744e-75034e448be5.htm language=enus -->
## TOPIC 00050: rfmxdemoddotnet/html/6eafe841-d62f-4fb2-744e-75034e448be5.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6eafe841-d62f-4fb2-744e-75034e448be5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6eafe841-d62f-4fb2-744e-75034e448be5.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodPulseShapingFilterType Enumeration

RFmxDemodMXDDemodPulseShapingFilterType Enumeration

SetMeasurementFilterType(String, RFmxDemodMXDDemodMeasurementFilterType)

Auto

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodPulseShapingFilterType
```

```text
Public Enumeration RFmxDemodMXDDemodPulseShapingFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rectangular | 0 | The transmitted waveform is filtered using a rectangular filter. |
| RaisedCosine | 1 | The transmitted waveform is filtered using a raised cosine filter. Specify the filter alpha in the pulse shaping filter alpha or BT. |
| RootRaisedCosine | 2 | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter alpha in the pulse shaping filter alpha or BT. |
| Gaussian | 3 | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the pulse shaping filter alpha or BT. This filter is applicable only to FSK and MSK modulation types. |
| Custom | 4 | The transmitted waveform is filtered using the coefficients that you specify in the ConfigurePulseShapingFilterCustomCoefficients(String, Double, Double, Single) method. |
| HalfSine | 5 | The transmitted waveform is filtered using a half sine filter. |
| LinearGmskEdge | 6 | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/6f8153fe-beb1-6302-6639-0afa6bf2450d.htm language=enus -->
## TOPIC 00051: rfmxdemoddotnet/html/6f8153fe-beb1-6302-6639-0afa6bf2450d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/6f8153fe-beb1-6302-6639-0afa6bf2450d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/6f8153fe-beb1-6302-6639-0afa6bf2450d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetSyncFound Method

RFmxDemodMXDDemodResultsGetSyncFound Method

Gets whether the synchronization bits were found in the demodulated signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSyncFound(
	string selectorString,
	out bool value
)
```

```text
Public Function GetSyncFound ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Boolean**
  - if the synchronization bits were found in the demodulated signal; otherwise, .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsSyncFound() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/709b6a82-959a-c0b7-38cf-d3f6e42abb88.htm language=enus -->
## TOPIC 00052: rfmxdemoddotnet/html/709b6a82-959a-c0b7-38cf-d3f6e42abb88.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/709b6a82-959a-c0b7-38cf-d3f6e42abb88.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/709b6a82-959a-c0b7-38cf-d3f6e42abb88.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetPhaseErrorMaximum Method

RFmxDemodMXDDemodResultsGetPhaseErrorMaximum Method

Gets the maximum of the phase error, in degrees, measured per acquisition.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseErrorMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseErrorMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the phase error, in degrees, measured per acquisition.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsPhaseErrorMaximum() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7117a79b-7c1a-5af6-c279-3769348245ce.htm language=enus -->
## TOPIC 00053: rfmxdemoddotnet/html/7117a79b-7c1a-5af6-c279-3769348245ce.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7117a79b-7c1a-5af6-c279-3769348245ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7117a79b-7c1a-5af6-c279-3769348245ce.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetSamplesPerSymbol Method

RFmxDemodMXDDemodConfigurationGetSamplesPerSymbol Method

Gets the samples per symbol used to acquire and demodulate the signal. Sample Rate = Symbol Rate * Samples per Symbol.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSamplesPerSymbol(
	string selectorString,
	out int value
)
```

```text
Public Function GetSamplesPerSymbol ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the samples per symbol used to acquire and demodulate the signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetSamplesPerSymbol() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/71690118-3ce0-4eca-dafb-4000ea65b5e2.htm language=enus -->
## TOPIC 00054: rfmxdemoddotnet/html/71690118-3ce0-4eca-dafb-4000ea65b5e2.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/71690118-3ce0-4eca-dafb-4000ea65b5e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/71690118-3ce0-4eca-dafb-4000ea65b5e2.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetAttributeDouble Method

RFmxDemodMXGetAttributeDouble Method

Gets the value of a double attribute.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Double**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetAttributeF64() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/717ce76b-5407-ed16-fdaf-4fb90ff2648e.htm language=enus -->
## TOPIC 00055: rfmxdemoddotnet/html/717ce76b-5407-ed16-fdaf-4fb90ff2648e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/717ce76b-5407-ed16-fdaf-4fb90ff2648e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/717ce76b-5407-ed16-fdaf-4fb90ff2648e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SetAttributeSByteArray Method

RFmxDemodMXSetAttributeSByteArray Method

Set the value of a signed byte array attribute.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeSByteArray(
	string selectorString,
	int attributeIdentifier,
	sbyte[] value
)
```

```text
Public Function SetAttributeSByteArray ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As SByte()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value SByte**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_SetAttributeI8Array() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7273cd77-5d5a-67f2-3691-355be110f8af.htm language=enus -->
## TOPIC 00056: rfmxdemoddotnet/html/7273cd77-5d5a-67f2-3691-355be110f8af.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7273cd77-5d5a-67f2-3691-355be110f8af.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7273cd77-5d5a-67f2-3691-355be110f8af.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.CloneSignalConfiguration Method

RFmxDemodMXCloneSignalConfiguration Method

Creates a new instance of a signal by copying all the values from an existing signal instance.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int CloneSignalConfiguration(
	string newSignalName,
	out RFmxDemodMX signalConfiguration
)
```

```text
Public Function CloneSignalConfiguration ( 
	newSignalName As String,
	<OutAttribute> ByRef signalConfiguration As RFmxDemodMX
) As Integer
```

###### Parameters

- **newSignalName String**
  - Specifies the name of the new signal.
- **signalConfiguration RFmxDemodMX**
  - Upon return, contains a new instance of a signal by copying all the values from an existing signal instance.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_CloneSignalConfiguration() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/727ddf33-22a8-f52e-e1d6-ec1ab59ac332.htm language=enus -->
## TOPIC 00057: rfmxdemoddotnet/html/727ddf33-22a8-f52e-e1d6-ec1ab59ac332.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/727ddf33-22a8-f52e-e1d6-ec1ab59ac332.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/727ddf33-22a8-f52e-e1d6-ec1ab59ac332.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchMeasurementWaveform(String, Double, ComplexWaveform<ComplexSingle>, RFmxDemodMXDDemodSamplesPerSymbol, Double) Method

RFmxDemodMXDDemodResultsFetchMeasurementWaveform(String, Double, ComplexWaveformComplexSingle, RFmxDemodMXDDemodSamplesPerSymbol, Double) Method

**Note: This API is now obsolete.**

Fetches the measurement waveform.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use FetchMeasurementWaveform() overload that takes in samplesPerSymbol as an integer.")]
public int FetchMeasurementWaveform(
	string selectorString,
	double timeout,
	ref ComplexWaveform<ComplexSingle> measurementWaveform,
	out RFmxDemodMXDDemodSamplesPerSymbol samplesPerSymbol,
	out double symbolRate
)
```

```text
<ObsoleteAttribute("Use FetchMeasurementWaveform() overload that takes in samplesPerSymbol as an integer.")>
Public Function FetchMeasurementWaveform ( 
	selectorString As String,
	timeout As Double,
	ByRef measurementWaveform As ComplexWaveform(Of ComplexSingle),
	<OutAttribute> ByRef samplesPerSymbol As RFmxDemodMXDDemodSamplesPerSymbol,
	<OutAttribute> ByRef symbolRate As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementWaveform ComplexWaveformComplexSingle**
  - Upon return, contains the demodulated waveform used for measurement.
- **samplesPerSymbol RFmxDemodMXDDemodSamplesPerSymbol**
  - Upon return, contains the samples per symbol used to acquire the signal for the measurement.
- **symbolRate Double**
  - Upon return, contains the symbol rate in hertz (Hz).

###### Return Value

Int32

##### Remarks

This method has been Obseleted. Use FetchMeasurementWaveform() overload that takes in samplesPerSymbol as an integer.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

FetchMeasurementWaveform Overload

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/72b1b96c-1ef9-9ef0-02f1-ba17aa4e4d1f.htm language=enus -->
## TOPIC 00058: rfmxdemoddotnet/html/72b1b96c-1ef9-9ef0-02f1-ba17aa4e4d1f.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/72b1b96c-1ef9-9ef0-02f1-ba17aa4e4d1f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/72b1b96c-1ef9-9ef0-02f1-ba17aa4e4d1f.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXLimitedConfigurationChange Enumeration

RFmxDemodMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXLimitedConfigurationChange
```

```text
Public Enumeration RFmxDemodMXLimitedConfigurationChange
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| NoChange | 1 | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency | 2 | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and SetExternalAttenuation(String, Double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| ReferenceLevel | 3 | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the SetReferenceLevel(String, Double) method value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the SetIQPowerEdgeTriggerLevelType(String, RFmxDemodMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| FrequencyAndReferenceLevel | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| SelectedPortsFrequencyAndReferenceLevel | 5 | Signal configuration, other than center frequency, reference level, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/73271adb-4903-6549-e960-1d92464f877f.htm language=enus -->
## TOPIC 00059: rfmxdemoddotnet/html/73271adb-4903-6549-e960-1d92464f877f.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/73271adb-4903-6549-e960-1d92464f877f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/73271adb-4903-6549-e960-1d92464f877f.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetFskReferenceCompensationEnabled Method

RFmxDemodMXDDemodConfigurationGetFskReferenceCompensationEnabled Method

Gets whether the frequency-shift keying (FSK) deviation that you specify is to be compensated for gain errors and is used to compute FSK error.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFskReferenceCompensationEnabled(
	string selectorString,
	out RFmxDemodMXDDemodFskReferenceCompensationEnabled value
)
```

```text
Public Function GetFskReferenceCompensationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXDDemodFskReferenceCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodFskReferenceCompensationEnabled**
  - Upon return, contains the value that indicates whether the FSK deviation that you specify is to be compensated for gain errors and is used to compute FSK error.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetFSKReferenceCompensationEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/735d4c2b-bc1f-4d35-fc8b-a6866def6437.htm language=enus -->
## TOPIC 00060: rfmxdemoddotnet/html/735d4c2b-bc1f-4d35-fc8b-a6866def6437.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/735d4c2b-bc1f-4d35-fc8b-a6866def6437.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/735d4c2b-bc1f-4d35-fc8b-a6866def6437.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetEvmMaximumRms Method

RFmxDemodMXDDemodResultsGetEvmMaximumRms Method

Gets the maximum of the RMS EVM measured per acquisition, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMaximumRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMaximumRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the RMS EVM measured per acquisition, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsEVMMaximumRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7363768e-1b0d-b399-5739-dc25714d8f38.htm language=enus -->
## TOPIC 00061: rfmxdemoddotnet/html/7363768e-1b0d-b399-5739-dc25714d8f38.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7363768e-1b0d-b399-5739-dc25714d8f38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7363768e-1b0d-b399-5739-dc25714d8f38.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigureSamplesPerSymbol(String, Int32) Method

RFmxDemodMXDDemodConfigurationConfigureSamplesPerSymbol(String, Int32) Method

Configures the samples per symbol to be used to acquire the signal for the measurement.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSamplesPerSymbol(
	string selectorString,
	int samplesPerSymbol
)
```

```text
Public Function ConfigureSamplesPerSymbol ( 
	selectorString As String,
	samplesPerSymbol As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **samplesPerSymbol Int32**
  - Specifies the samples per symbol used to acquire the signal for the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodCfgSamplesPerSymbol() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

ConfigureSamplesPerSymbol Overload

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/73742daf-3bdc-7b37-cc7f-88d50b4c1353.htm language=enus -->
## TOPIC 00062: rfmxdemoddotnet/html/73742daf-3bdc-7b37-cc7f-88d50b4c1353.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/73742daf-3bdc-7b37-cc7f-88d50b4c1353.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/73742daf-3bdc-7b37-cc7f-88d50b4c1353.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetErrorString Method

RFmxDemodMXGetErrorString Method

Gets the error description that specifies the origin/reason of the error or warning.

Namespace:

NationalInstruments.RFmx.DemodMX

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

- **errorCode Int32**
  - Specifies the error or warning code.
- **errorDescription String**
  - Upon return, contains the error description.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetErrorString() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7418366a-5821-19ba-681e-fa42b13f659a.htm language=enus -->
## TOPIC 00063: rfmxdemoddotnet/html/7418366a-5821-19ba-681e-fa42b13f659a.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7418366a-5821-19ba-681e-fa42b13f659a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7418366a-5821-19ba-681e-fa42b13f659a.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetFMDeviationMaximumPositivePeak Method

RFmxDemodMXADemodResultsGetFMDeviationMaximumPositivePeak Method

Gets the maximum positive peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMDeviationMaximumPositivePeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMDeviationMaximumPositivePeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum positive peak frequency deviation, in Hz, of the FM signal measured across multiple acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMaximumPositivePeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/743795b9-05ee-7689-eaac-7eadc745237f.htm language=enus -->
## TOPIC 00064: rfmxdemoddotnet/html/743795b9-05ee-7689-eaac-7eadc745237f.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/743795b9-05ee-7689-eaac-7eadc745237f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/743795b9-05ee-7689-eaac-7eadc745237f.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodAveragingType Enumeration

RFmxDemodMXADemodAveragingType Enumeration

Specifies the averaging type for the measurement.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXADemodAveragingType
```

```text
Public Enumeration RFmxDemodMXADemodAveragingType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Linear | 0 | The averaged result is the mean value measured across multiple acquisitions. |
| Maximum | 1 | The averaged result is the maximum value measured across multiple acquisitions. |
| Minimum | 2 | The averaged result is the minimum value measured across multiple acquisitions. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7458d21c-0122-81a6-434b-1b46a6bf9f94.htm language=enus -->
## TOPIC 00065: rfmxdemoddotnet/html/7458d21c-0122-81a6-434b-1b46a6bf9f94.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7458d21c-0122-81a6-434b-1b46a6bf9f94.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7458d21c-0122-81a6-434b-1b46a6bf9f94.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodMeasurementFilterType Enumeration

RFmxDemodMXDDemodMeasurementFilterType Enumeration

Specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodMeasurementFilterType
```

```text
Public Enumeration RFmxDemodMXDDemodMeasurementFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Auto | 0 | The signal analyzer computes the measurement filter coefficients based on the pulse shaping filter information that you specify in the pulse shaping filter. If the SetPulseShapingFilterType(String, RFmxDemodMXDDemodPulseShapingFilterType) method is set to Custom, then the signal analyzer enables equalization. |
| Custom | 1 | The signal analyzer uses the coefficients specified by ConfigureMeasurementFilterCustomCoefficients(String, Double, Double, Single) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7565e9e2-50ab-d66b-e13f-bcb8fa41e4c2.htm language=enus -->
## TOPIC 00066: rfmxdemoddotnet/html/7565e9e2-50ab-d66b-e13f-bcb8fa41e4c2.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7565e9e2-50ab-d66b-e13f-bcb8fa41e4c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7565e9e2-50ab-d66b-e13f-bcb8fa41e4c2.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemod.Results Property

RFmxDemodMXDDemodResults Property

RFmxDemodMXDDemodResults

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxDemodMXDDemodResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxDemodMXDDemodResults
	Get
```

###### Property Value

RFmxDemodMXDDemodResults

##### See Also

###### Reference

RFmxDemodMXDDemod Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7620300d-53c1-ab3b-69c5-95fcd2915b08.htm language=enus -->
## TOPIC 00067: rfmxdemoddotnet/html/7620300d-53c1-ab3b-69c5-95fcd2915b08.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7620300d-53c1-ab3b-69c5-95fcd2915b08.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7620300d-53c1-ab3b-69c5-95fcd2915b08.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.SetAveragingCount Method

RFmxDemodMXADemodConfigurationSetAveragingCount Method

Sets the number of acquisitions used for averaging.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Specifies the number of acquisitions used for averaging when you set SetAveragingEnabled(String, RFmxDemodMXADemodAveragingEnabled) to True.

###### Return Value

Int32

##### Remarks

SetAveragingEnabled(String, RFmxDemodMXADemodAveragingEnabled)

True

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/78474e64-c7c3-1f4b-d446-f1908002cabc.htm language=enus -->
## TOPIC 00068: rfmxdemoddotnet/html/78474e64-c7c3-1f4b-d446-f1908002cabc.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/78474e64-c7c3-1f4b-d446-f1908002cabc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/78474e64-c7c3-1f4b-d446-f1908002cabc.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchPhaseErrorTrace Method

RFmxDemodMXDDemodResultsFetchPhaseErrorTrace Method

Fetches the phase error trace.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPhaseErrorTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> phaseError
)
```

```text
Public Function FetchPhaseErrorTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef phaseError As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **phaseError AnalogWaveformSingle**
  - Upon return, contains the phase error.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchPhaseErrorTrace() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/789346de-3d66-548f-db7b-f41b070ec863.htm language=enus -->
## TOPIC 00069: rfmxdemoddotnet/html/789346de-3d66-548f-db7b-f41b070ec863.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/789346de-3d66-548f-db7b-f41b070ec863.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/789346de-3d66-548f-db7b-f41b070ec863.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.FetchDemodSignalTrace Method

RFmxDemodMXADemodResultsFetchDemodSignalTrace Method

Fetches the demodulated signal trace.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDemodSignalTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> demodulatedSignal
)
```

```text
Public Function FetchDemodSignalTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef demodulatedSignal As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **demodulatedSignal AnalogWaveformSingle**
  - Upon return, contains the demodulated signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodFetchDemodSignalTrace() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/797220fb-4969-0618-43c7-37fdba22b7d9.htm language=enus -->
## TOPIC 00070: rfmxdemoddotnet/html/797220fb-4969-0618-43c7-37fdba22b7d9.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/797220fb-4969-0618-43c7-37fdba22b7d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/797220fb-4969-0618-43c7-37fdba22b7d9.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetFMDeviationMeanHalfPeakToPeak Method

RFmxDemodMXADemodResultsGetFMDeviationMeanHalfPeakToPeak Method

Gets the mean (peak-to-peak)/2 frequency variation, in hertz (Hz), around the nominal frequency of the frequency-modulated (FM) carrier.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMDeviationMeanHalfPeakToPeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMDeviationMeanHalfPeakToPeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMeanHalfPeaktoPeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/797e2085-469c-f026-9fa9-508e073ee76c.htm language=enus -->
## TOPIC 00071: rfmxdemoddotnet/html/797e2085-469c-f026-9fa9-508e073ee76c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/797e2085-469c-f026-9fa9-508e073ee76c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/797e2085-469c-f026-9fa9-508e073ee76c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetAudioFilterType Method

RFmxDemodMXADemodConfigurationGetAudioFilterType Method

Gets the audio filter to be applied on the analog demodulated signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAudioFilterType(
	string selectorString,
	out RFmxDemodMXADemodAudioFilterType value
)
```

```text
Public Function GetAudioFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXADemodAudioFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXADemodAudioFilterType**
  - Upon return, contains the audio filter to be applied on the analog demodulated signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetAudioFilterType() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/79e640de-a380-a933-5689-ebf0b0e96950.htm language=enus -->
## TOPIC 00072: rfmxdemoddotnet/html/79e640de-a380-a933-5689-ebf0b0e96950.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/79e640de-a380-a933-5689-ebf0b0e96950.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/79e640de-a380-a933-5689-ebf0b0e96950.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ClearAllNamedResults Method

RFmxDemodMXClearAllNamedResults Method

Clears all results for the current signal instance.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Pass an empty string. The signal name passed when creating the signal configuration is used.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ClearAllNamedResults() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7a3a1e67-0cbb-569f-e903-ec5f4fca6425.htm language=enus -->
## TOPIC 00073: rfmxdemoddotnet/html/7a3a1e67-0cbb-569f-e903-ec5f4fca6425.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7a3a1e67-0cbb-569f-e903-ec5f4fca6425.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7a3a1e67-0cbb-569f-e903-ec5f4fca6425.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetIQOffsetRemovalEnabled Method

RFmxDemodMXDDemodConfigurationSetIQOffsetRemovalEnabled Method

Sets whether to remove the I/Q offset before the EVM measurement.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQOffsetRemovalEnabled(
	string selectorString,
	RFmxDemodMXDDemodIQOffsetRemovalEnabled value
)
```

```text
Public Function SetIQOffsetRemovalEnabled ( 
	selectorString As String,
	value As RFmxDemodMXDDemodIQOffsetRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodIQOffsetRemovalEnabled**
  - Specifies whether to remove the I/Q offset before the EVM measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7aba283f-909a-bf4f-2bc6-13a7ad39a41e.htm language=enus -->
## TOPIC 00074: rfmxdemoddotnet/html/7aba283f-909a-bf4f-2bc6-13a7ad39a41e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7aba283f-909a-bf4f-2bc6-13a7ad39a41e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7aba283f-909a-bf4f-2bc6-13a7ad39a41e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetIQPowerEdgeTriggerLevelType Method

RFmxDemodMXGetIQPowerEdgeTriggerLevelType Method

SetIQPowerEdgeTriggerLevel(String, Double)

SetTriggerType(String, RFmxDemodMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerLevelType(
	string selectorString,
	out RFmxDemodMXIQPowerEdgeTriggerLevelType value
)
```

```text
Public Function GetIQPowerEdgeTriggerLevelType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXIQPowerEdgeTriggerLevelType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value RFmxDemodMXIQPowerEdgeTriggerLevelType**
  - Upon return, contains the value that indicates the reference for the GetIQPowerEdgeTriggerLevelType(String, RFmxDemodMXIQPowerEdgeTriggerLevelType) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetIQPowerEdgeTriggerLevelType() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7afb0d5a-5d4d-91bc-8521-b6023e3a1d6b.htm language=enus -->
## TOPIC 00075: rfmxdemoddotnet/html/7afb0d5a-5d4d-91bc-8521-b6023e3a1d6b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7afb0d5a-5d4d-91bc-8521-b6023e3a1d6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7afb0d5a-5d4d-91bc-8521-b6023e3a1d6b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants.PxiTriggerLine2 Field

RFmxDemodMXConstantsPxiTriggerLine2 Field

Exports the signal to the PXI trigger line 2.

Namespace:

NationalInstruments.RFmx.DemodMX

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

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7bb8f451-f08f-f977-f98d-e179faae1aa4.htm language=enus -->
## TOPIC 00076: rfmxdemoddotnet/html/7bb8f451-f08f-f977-f98d-e179faae1aa4.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7bb8f451-f08f-f977-f98d-e179faae1aa4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7bb8f451-f08f-f977-f98d-e179faae1aa4.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetSynchronizationEnabled Method

RFmxDemodMXDDemodConfigurationSetSynchronizationEnabled Method

Sets whether the demodulator needs to search and synchronize the signal to a known reference sequence.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSynchronizationEnabled(
	string selectorString,
	RFmxDemodMXDDemodSynchronizationEnabled value
)
```

```text
Public Function SetSynchronizationEnabled ( 
	selectorString As String,
	value As RFmxDemodMXDDemodSynchronizationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodSynchronizationEnabled**
  - Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodSetSynchronizationEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7bf627f9-175d-839c-029e-117f465f9837.htm language=enus -->
## TOPIC 00077: rfmxdemoddotnet/html/7bf627f9-175d-839c-029e-117f465f9837.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7bf627f9-175d-839c-029e-117f465f9837.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7bf627f9-175d-839c-029e-117f465f9837.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SetExternalAttenuation Method

RFmxDemodMXSetExternalAttenuation Method

Sets the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value Double**
  - Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_SetExternalAttenuation() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7c427703-ef71-0048-2ac4-b36eccfb07be.htm language=enus -->
## TOPIC 00078: rfmxdemoddotnet/html/7c427703-ef71-0048-2ac4-b36eccfb07be.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7c427703-ef71-0048-2ac4-b36eccfb07be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7c427703-ef71-0048-2ac4-b36eccfb07be.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetCarrierMeanFrequencyError Method

RFmxDemodMXDDemodResultsGetCarrierMeanFrequencyError Method

**Note: This API is now obsolete.**

Gets the frequency offset, in hertz (Hz), from the transmitted carrier frequency.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use GetCarrierMeanFrequencyOffset to get the value")]
public int GetCarrierMeanFrequencyError(
	string selectorString,
	out double value
)
```

```text
<ObsoleteAttribute("Use GetCarrierMeanFrequencyOffset to get the value")>
Public Function GetCarrierMeanFrequencyError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the frequency offset, in Hz, from the transmitted carrier frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsCarrierMeanFrequencyError() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7ca7f730-4346-db0b-c19a-0112f9afa416.htm language=enus -->
## TOPIC 00079: rfmxdemoddotnet/html/7ca7f730-4346-db0b-c19a-0112f9afa416.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7ca7f730-4346-db0b-c19a-0112f9afa416.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7ca7f730-4346-db0b-c19a-0112f9afa416.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.SetRbwFilterAlpha Method

RFmxDemodMXADemodConfigurationSetRbwFilterAlpha Method

Sets the roll-off factor of the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAlpha(
	string selectorString,
	double value
)
```

```text
Public Function SetRbwFilterAlpha ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the roll-off factor of the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodSetRBWFilterAlpha() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7d3adedd-0943-3cc8-325d-3c49dac25673.htm language=enus -->
## TOPIC 00080: rfmxdemoddotnet/html/7d3adedd-0943-3cc8-325d-3c49dac25673.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7d3adedd-0943-3cc8-325d-3c49dac25673.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7d3adedd-0943-3cc8-325d-3c49dac25673.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SetTriggerType Method

RFmxDemodMXSetTriggerType Method

Sets the type of reference trigger to use for signal acquisition.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerType(
	string selectorString,
	RFmxDemodMXTriggerType value
)
```

```text
Public Function SetTriggerType ( 
	selectorString As String,
	value As RFmxDemodMXTriggerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value RFmxDemodMXTriggerType**
  - Specifies the type of reference trigger to use for signal acquisition.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_SetTriggerType() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7dc51539-89fb-dcc9-44ce-c52fbe45007d.htm language=enus -->
## TOPIC 00081: rfmxdemoddotnet/html/7dc51539-89fb-dcc9-44ce-c52fbe45007d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7dc51539-89fb-dcc9-44ce-c52fbe45007d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7dc51539-89fb-dcc9-44ce-c52fbe45007d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetFMDeviationMaximumNegativePeak Method

RFmxDemodMXADemodResultsGetFMDeviationMaximumNegativePeak Method

Gets the maximum negative peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMDeviationMaximumNegativePeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMDeviationMaximumNegativePeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum negative peak frequency deviation, in Hz, of the FM signal measured across multiple acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMaximumNegativePeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/7ecfe6db-611d-0245-634b-65e3b30eb8fa.htm language=enus -->
## TOPIC 00082: rfmxdemoddotnet/html/7ecfe6db-611d-0245-634b-65e3b30eb8fa.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/7ecfe6db-611d-0245-634b-65e3b30eb8fa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/7ecfe6db-611d-0245-634b-65e3b30eb8fa.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetAllTracesEnabled Method

RFmxDemodMXADemodConfigurationGetAllTracesEnabled Method

Gets whether the traces to be stored and retrieved after performing the analog demodulation measurements is enabled.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - to enable the traces to be stored and retrieved after performing the analog demodulation measurement;otherwise, .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetAllTracesEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/809b06f6-384b-75e2-30fe-d4838e31e59b.htm language=enus -->
## TOPIC 00083: rfmxdemoddotnet/html/809b06f6-384b-75e2-30fe-d4838e31e59b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/809b06f6-384b-75e2-30fe-d4838e31e59b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/809b06f6-384b-75e2-30fe-d4838e31e59b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetMagnitudeErrorMean Method

RFmxDemodMXDDemodResultsGetMagnitudeErrorMean Method

Gets the mean of the magnitude error measured per acquisition, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMagnitudeErrorMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetMagnitudeErrorMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the magnitude error measured per acquisition, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsMagnitudeErrorMean() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/98d2aae6-48c0-922b-50d5-fab35882218c.htm language=enus -->
## TOPIC 00084: rfmxdemoddotnet/html/98d2aae6-48c0-922b-50d5-fab35882218c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/98d2aae6-48c0-922b-50d5-fab35882218c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/98d2aae6-48c0-922b-50d5-fab35882218c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants.PxiTriggerLine6 Field

RFmxDemodMXConstantsPxiTriggerLine6 Field

Exports the signal to the PXI trigger line 6.

Namespace:

NationalInstruments.RFmx.DemodMX

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

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/9be2d8d3-708b-4d69-f5cf-f328b84dc31b.htm language=enus -->
## TOPIC 00085: rfmxdemoddotnet/html/9be2d8d3-708b-4d69-f5cf-f328b84dc31b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/9be2d8d3-708b-4d69-f5cf-f328b84dc31b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/9be2d8d3-708b-4d69-f5cf-f328b84dc31b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.SetDigitalEdgeTriggerEdge Method

RFmxDemodMXSetDigitalEdgeTriggerEdge Method

Sets the signal analyzer to detect a rising or falling edge on the digital-edge trigger signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerEdge(
	string selectorString,
	RFmxDemodMXDigitalEdgeTriggerEdge value
)
```

```text
Public Function SetDigitalEdgeTriggerEdge ( 
	selectorString As String,
	value As RFmxDemodMXDigitalEdgeTriggerEdge
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value RFmxDemodMXDigitalEdgeTriggerEdge**
  - Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_SetDigitalEdgeTriggerEdge() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/9bf3b9cd-eb3c-354c-2053-4d622a5febb8.htm language=enus -->
## TOPIC 00086: rfmxdemoddotnet/html/9bf3b9cd-eb3c-354c-2053-4d622a5febb8.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/9bf3b9cd-eb3c-354c-2053-4d622a5febb8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/9bf3b9cd-eb3c-354c-2053-4d622a5febb8.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetMeanModulationFrequency Method

RFmxDemodMXADemodResultsGetMeanModulationFrequency Method

Gets the mean of the demodulated signal frequency, in hertz (Hz).

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanModulationFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanModulationFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the demodulated signal frequency, in Hz.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsMeanModulationFrequency() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/9cda5107-be50-260b-5fdf-943b68a8689e.htm language=enus -->
## TOPIC 00087: rfmxdemoddotnet/html/9cda5107-be50-260b-5fdf-943b68a8689e.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/9cda5107-be50-260b-5fdf-943b68a8689e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/9cda5107-be50-260b-5fdf-943b68a8689e.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetAttributeInt Method

RFmxDemodMXGetAttributeInt Method

Gets the value of an integer attribute.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetAttributeI32() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/9d2e6124-7f5b-ed9b-f4a4-384b6d0ed2b5.htm language=enus -->
## TOPIC 00088: rfmxdemoddotnet/html/9d2e6124-7f5b-ed9b-f4a4-384b6d0ed2b5.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/9d2e6124-7f5b-ed9b-f4a4-384b6d0ed2b5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/9d2e6124-7f5b-ed9b-f4a4-384b6d0ed2b5.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodSymbolMapType Enumeration

RFmxDemodMXDDemodSymbolMapType Enumeration

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodSymbolMapType
```

```text
Public Enumeration RFmxDemodMXDDemodSymbolMapType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Auto | 0 | Uses a default symbol map. |
| Custom | 1 | Uses the map that you specify using the ConfigureSymbolMap(String, RFmxDemodMXDDemodSymbolMapType, ComplexSingle) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/9e95f2a8-4f79-68f4-ae3f-8e8b027448f4.htm language=enus -->
## TOPIC 00089: rfmxdemoddotnet/html/9e95f2a8-4f79-68f4-ae3f-8e8b027448f4.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/9e95f2a8-4f79-68f4-ae3f-8e8b027448f4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/9e95f2a8-4f79-68f4-ae3f-8e8b027448f4.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodSignalStructure Enumeration

RFmxDemodMXDDemodSignalStructure Enumeration

Specifies whether the signal is either a bursty signal or a continuous signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodSignalStructure
```

```text
Public Enumeration RFmxDemodMXDDemodSignalStructure
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Bursted | 0 | The signal is a bursty signal. |
| Continuous | 1 | The signal is a continuous signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/9f932145-a196-677f-4dfb-6e901df88104.htm language=enus -->
## TOPIC 00090: rfmxdemoddotnet/html/9f932145-a196-677f-4dfb-6e901df88104.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/9f932145-a196-677f-4dfb-6e901df88104.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/9f932145-a196-677f-4dfb-6e901df88104.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetFMDeviationMeanStandardDeviation Method

RFmxDemodMXADemodResultsGetFMDeviationMeanStandardDeviation Method

Gets the mean frequency deviation, in hertz (Hz), around the nominal frequency of the FM carrier.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMDeviationMeanStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMDeviationMeanStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean frequency deviation, in Hz, around the nominal frequency of the FM carrier.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMeanStandardDeviation() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/a1928a74-55e9-e031-b42b-39b400d07606.htm language=enus -->
## TOPIC 00091: rfmxdemoddotnet/html/a1928a74-55e9-e031-b42b-39b400d07606.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/a1928a74-55e9-e031-b42b-39b400d07606.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/a1928a74-55e9-e031-b42b-39b400d07606.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ConfigureRF Method

RFmxDemodMXConfigureRF Method

Configures the RF properties of the signal by specifying the selector string.

Namespace:

NationalInstruments.RFmx.DemodMX

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

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **centerFrequency Double**
  - Specifies the carrier frequency, in hertz (Hz), of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.
- **referenceLevel Double**
  - Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- **externalAttenuation Double**
  - Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_CfgRF() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/a1d47742-c6c0-d064-4c3c-2afa0135b696.htm language=enus -->
## TOPIC 00092: rfmxdemoddotnet/html/a1d47742-c6c0-d064-4c3c-2afa0135b696.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/a1d47742-c6c0-d064-4c3c-2afa0135b696.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/a1d47742-c6c0-d064-4c3c-2afa0135b696.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetEqualizerConvergenceFactor Method

RFmxDemodMXDDemodConfigurationGetEqualizerConvergenceFactor Method

Gets the incremental step used by the equalizer to adapt to the channel during the training stage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEqualizerConvergenceFactor(
	string selectorString,
	out double value
)
```

```text
Public Function GetEqualizerConvergenceFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the incremental step used to adapt to the channel by the equalizer during the training stage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetEqualizerConvergenceFactor() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/a45ed27a-09f1-9803-8239-68d4cd2440f1.htm language=enus -->
## TOPIC 00093: rfmxdemoddotnet/html/a45ed27a-09f1-9803-8239-68d4cd2440f1.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/a45ed27a-09f1-9803-8239-68d4cd2440f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/a45ed27a-09f1-9803-8239-68d4cd2440f1.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.FetchCarrierMeasurement Method

RFmxDemodMXADemodResultsFetchCarrierMeasurement Method

Fetches the carrier measurement.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurement(
	string selectorString,
	double timeout,
	out double meanCarrierFrequencyError,
	out double meanCarrierPower
)
```

```text
Public Function FetchCarrierMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanCarrierFrequencyError As Double,
	<OutAttribute> ByRef meanCarrierPower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **meanCarrierFrequencyError Double**
  - Upon return, contains the mean of the measured carrier frequency offset, in hertz (Hz).
- **meanCarrierPower Double**
  - Upon return, contains the mean of the measured carrier power, in dBm.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodFetchCarrierMeasurement() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/a713f0c4-b661-2e32-b5a3-59d2ce36ce07.htm language=enus -->
## TOPIC 00094: rfmxdemoddotnet/html/a713f0c4-b661-2e32-b5a3-59d2ce36ce07.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/a713f0c4-b661-2e32-b5a3-59d2ce36ce07.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/a713f0c4-b661-2e32-b5a3-59d2ce36ce07.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults Class

RFmxDemodMXDDemodResults Class

Provides methods to fetch and read the digital demodulation measurement results.

##### Inheritance Hierarchy

RFmxDemodMXSubObject

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxDemodMXDDemodResults : RFmxDemodMXSubObject
```

```text
Public NotInheritable Class RFmxDemodMXDDemodResults
	Inherits RFmxDemodMXSubObject
```

The RFmxDemodMXDDemodResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchCarrierMeasurement | Fetches the carrier measurement. |
|  | FetchConstellationTrace | Fetches the constellation trace. |
|  | FetchDemodulatedBits | Fetches the demodulated bit stream. |
|  | FetchEqualizerCoefficients | Fetches the updated equalizer coefficients. |
|  | FetchEvm | Fetches the error vector magnitude (EVM) measurements. |
|  | FetchEvmTrace | Fetches the error vector magnitude (EVM) trace. |
|  | FetchFskDeviationTrace | Fetches the frequency-shift keying (FSK) deviation trace. |
|  | FetchFskResults | Fetches frequency-shift keying (FSK) results. |
|  | FetchIQImpairments | Fetches I/Q impairments. |
|  | FetchMagnitudeError | Fetches the magnitude error measurements. |
|  | FetchMagnitudeErrorTrace | Fetches the magnitude error trace. |
|  | FetchMeanAmplitudeDroop | Fetches the mean amplitude droop per symbol. |
|  | FetchMeanIQOriginOffset | Fetches the offset, in dB, from the ideal location of the constellation origin. |
|  | FetchMeanQuadratureSkew | Fetches the mean quadrature skew. |
|  | FetchMeanRhoFactor | Fetches the correlation of the measurement waveform and the reference waveform. |
|  | FetchMeasurementWaveform(String, Double, ComplexWaveformComplexSingle, RFmxDemodMXDDemodSamplesPerSymbol, Double) | Obsolete. Fetches the measurement waveform. |
|  | FetchMeasurementWaveform(String, Double, ComplexWaveformComplexSingle, Int32, Double) | Fetches the measurement waveform. |
|  | FetchOffsetConstellationTrace | TODO: |
|  | FetchOffsetEvm | Fetches the offset error vector magnitude (EVM). |
|  | FetchOffsetEvmTrace | Fetches the offset error vector magnitude (EVM) trace measured on offset quadrature PSK (OQPSK) signal. |
|  | FetchPhaseError | Fetches the phase error measurements. |
|  | FetchPhaseErrorTrace | Fetches the phase error trace. |
|  | FetchReferenceWaveform | Fetches the reference waveform. |
|  | FetchSyncFound | Fetches the synchronization bits found status in the demodulated signal. |
|  | GetCarrierMeanFrequencyDrift | Gets the measured carrier frequency drift, in hertz (Hz). |
|  | GetCarrierMeanFrequencyError | Obsolete. Gets the frequency offset, in hertz (Hz), from the transmitted carrier frequency. |
|  | GetCarrierMeanFrequencyOffset | Gets the frequency offset, in hertz (Hz), from the transmitted carrier frequency. |
|  | GetCarrierMeanPhaseError | Gets the phase offset, in degrees, from the transmitted carrier phase. |
|  | GetEvmMaximumPeak | Gets the maximum of the peak EVM measured per acquisition, as a percentage. |
|  | GetEvmMaximumRms | Gets the maximum of the RMS EVM measured per acquisition, as a percentage. |
|  | GetEvmMeanModulationErrorRatio | Gets the modulation error ratio (MER), in dB. |
|  | GetEvmMeanPeak | Gets the mean of the peak error vector magnitude (EVM) measured per acquisition, as a percentage. |
|  | GetEvmMeanRms | Gets the mean of the RMS EVM measured per acquisition, as a percentage. |
|  | GetFskMaximumPeakFskError | Gets the mean peak deviation error, in hertz (Hz), of the frequency-shift keying (FSK) symbols measured per acquisition. |
|  | GetFskMeanDeviation | Gets the reference frequency-shift keying (FSK) deviation, in hertz (Hz), used to measure the FSK error. |
|  | GetFskMeanPeakDeviationError | Obsolete. Gets the mean peak deviation error, in hertz (Hz), of the frequency-shift keying (FSK) symbols measured per acquisition. |
|  | GetFskMeanRmsDeviationError | Obsolete. Gets the mean of the root mean squared (RMS) frequency error, in hertz (Hz), of the frequency-shift keying (FSK) symbols measured per acquisition. |
|  | GetFskMeanRmsFskError | Gets the mean of the root mean squared (RMS) frequency error, in hertz (Hz), of the frequency-shift keying (FSK) symbols measured per acquisition. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQImpairmentsMeanIQGainImbalance | Gets the measured ratio of I gain to Q gain, in dB. |
|  | GetIQImpairmentsMeanIQOriginOffset | Gets the offset, in dB, from the ideal location of the constellation origin. |
|  | GetIQImpairmentsMeanQuadratureSkew | Gets a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. |
|  | GetMagnitudeErrorMaximum | Gets the maximum of the magnitude error measured per acquisition, as a percentage. |
|  | GetMagnitudeErrorMean | Gets the mean of the magnitude error measured per acquisition, as a percentage. |
|  | GetMeanAmplitudeDroop | Gets the mean amplitude droop per symbol. |
|  | GetMeanRhoFactor | Gets the correlation of the measurement waveform and the reference waveform. |
|  | GetOffsetEvmMaximumPeak | Gets the maximum of the peak error vector magnitude (EVM), as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
|  | GetOffsetEvmMaximumRms | Gets the maximum of the RMS EVM, as a percentage, measured per acquisition, as a percentage. |
|  | GetOffsetEvmMeanPeak | Gets the mean of the peak error vector magnitude (EVM) measured per acquisition, as a percentage. |
|  | GetOffsetEvmMeanRms | Gets the mean of the RMS EVM measured per acquisition, as a percentage. |
|  | GetPhaseErrorMaximum | Gets the maximum of the phase error, in degrees, measured per acquisition. |
|  | GetPhaseErrorMean | Gets the mean of the phase error, in degrees, measured per acquisition. |
|  | GetSyncFound | Gets whether the synchronization bits were found in the demodulated signal. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | Read | Configures hardware for acquisition, performs measurement on acquired data for the modulation type configured using the ConfigureModulationType(String, RFmxDemodMXDDemodModulationType, RFmxDemodMXDDemodM, RFmxDemodMXDDemodDifferentialEnabled) method and returns the frequency offset, error vector magnitude (EVM), and modulation error ratio (MER) results. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### Remarks

For more information about RFmx Demod, refer to the RFmx Demod Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/ac285134-1a09-4226-6095-e9a365b9ddd5.htm language=enus -->
## TOPIC 00095: rfmxdemoddotnet/html/ac285134-1a09-4226-6095-e9a365b9ddd5.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/ac285134-1a09-4226-6095-e9a365b9ddd5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/ac285134-1a09-4226-6095-e9a365b9ddd5.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetPMDeviationMaximumNegativePeak Method

RFmxDemodMXADemodResultsGetPMDeviationMaximumNegativePeak Method

Gets the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPMDeviationMaximumNegativePeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetPMDeviationMaximumNegativePeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumNegativePeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/ac46c60e-a4eb-f181-c003-556625660276.htm language=enus -->
## TOPIC 00096: rfmxdemoddotnet/html/ac46c60e-a4eb-f181-c003-556625660276.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/ac46c60e-a4eb-f181-c003-556625660276.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/ac46c60e-a4eb-f181-c003-556625660276.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetIQImpairmentsMeanQuadratureSkew Method

RFmxDemodMXDDemodResultsGetIQImpairmentsMeanQuadratureSkew Method

Gets a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQImpairmentsMeanQuadratureSkew(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQImpairmentsMeanQuadratureSkew ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsIQImpairmentsMeanQuadratureSkew() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/af39836a-c30f-9c78-ef46-2e43bdd0a5b0.htm language=enus -->
## TOPIC 00097: rfmxdemoddotnet/html/af39836a-c30f-9c78-ef46-2e43bdd0a5b0.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/af39836a-c30f-9c78-ef46-2e43bdd0a5b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/af39836a-c30f-9c78-ef46-2e43bdd0a5b0.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetFskMeanPeakDeviationError Method

RFmxDemodMXDDemodResultsGetFskMeanPeakDeviationError Method

**Note: This API is now obsolete.**

Gets the mean peak deviation error, in hertz (Hz), of the frequency-shift keying (FSK) symbols measured per acquisition.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use GetFskMaximumPeakFskError to get the value")]
public int GetFskMeanPeakDeviationError(
	string selectorString,
	out double value
)
```

```text
<ObsoleteAttribute("Use GetFskMaximumPeakFskError to get the value")>
Public Function GetFskMeanPeakDeviationError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean peak deviation error, in Hz, of the FSK symbols measured per acquisition.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsFSKMeanPeakDeviationError() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm language=enus -->
## TOPIC 00098: rfmxdemoddotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.InstrMX Namespace

NationalInstruments.RFmx.InstrMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxDemodMXExtension | Provides extension methods to create Demod signal configuration. These methods are added to RFmxInstrMX class. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/afe5afa5-4ed2-0fb5-262d-f80c9bb1af26.htm language=enus -->
## TOPIC 00099: rfmxdemoddotnet/html/afe5afa5-4ed2-0fb5-262d-f80c9bb1af26.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/afe5afa5-4ed2-0fb5-262d-f80c9bb1af26.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/afe5afa5-4ed2-0fb5-262d-f80c9bb1af26.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetSearchLengthAuto Method

RFmxDemodMXDDemodConfigurationGetSearchLengthAuto Method

Gets whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSearchLengthAuto(
	string selectorString,
	out RFmxDemodMXDDemodSearchLengthAuto value
)
```

```text
Public Function GetSearchLengthAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXDDemodSearchLengthAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodSearchLengthAuto**
  - Upon return, contains synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

###### Return Value

Int32

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/b1a11d03-7ce7-1e84-35db-7ed80ba8a9ec.htm language=enus -->
## TOPIC 00100: rfmxdemoddotnet/html/b1a11d03-7ce7-1e84-35db-7ed80ba8a9ec.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/b1a11d03-7ce7-1e84-35db-7ed80ba8a9ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/b1a11d03-7ce7-1e84-35db-7ed80ba8a9ec.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigureAveraging Method

RFmxDemodMXDDemodConfigurationConfigureAveraging Method

Configures averaging for digital demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxDemodMXDDemodAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxDemodMXDDemodAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxDemodMXDDemodAveragingEnabled**
  - Enables averaging for digital demodulation measurements.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you enable averaging.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodCfgAveraging() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/ba7e8a40-dc62-360b-0d44-e1668fe7ce60.htm language=enus -->
## TOPIC 00101: rfmxdemoddotnet/html/ba7e8a40-dc62-360b-0d44-e1668fe7ce60.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/ba7e8a40-dc62-360b-0d44-e1668fe7ce60.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/ba7e8a40-dc62-360b-0d44-e1668fe7ce60.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetAMModulationDepthMeanRms Method

RFmxDemodMXADemodResultsGetAMModulationDepthMeanRms Method

Gets the mean root mean square (RMS) amplitude of the modulating signal, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMModulationDepthMeanRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetAMModulationDepthMeanRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean RMS amplitude of the modulating signal, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/baa1b08e-4967-fbd7-7b4e-5d7c9d270f48.htm language=enus -->
## TOPIC 00102: rfmxdemoddotnet/html/baa1b08e-4967-fbd7-7b4e-5d7c9d270f48.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/baa1b08e-4967-fbd7-7b4e-5d7c9d270f48.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/baa1b08e-4967-fbd7-7b4e-5d7c9d270f48.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchEvm Method

RFmxDemodMXDDemodResultsFetchEvm Method

Fetches the error vector magnitude (EVM) measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

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
	out double meanModulationErrorRatio,
	out double maximumPeakEvm,
	out double meanPeakEvm
)
```

```text
Public Function FetchEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRmsEvm As Double,
	<OutAttribute> ByRef maximumRmsEvm As Double,
	<OutAttribute> ByRef meanModulationErrorRatio As Double,
	<OutAttribute> ByRef maximumPeakEvm As Double,
	<OutAttribute> ByRef meanPeakEvm As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsEvm Double**
  - Upon return, contains the mean of the RMS EVM, as a percentage, measured per acquisition.
- **maximumRmsEvm Double**
  - Upon return, contains the maximum of the RMS EVM, as a percentage, measured per acquisition.
- **meanModulationErrorRatio Double**
  - Upon return, contains the modulation error ratio, in dB.
- **maximumPeakEvm Double**
  - Upon return, contains the maximum of the peak EVM measured per acquisition.
- **meanPeakEvm Double**
  - Upon return, contains the mean of the peak EVM measured per acquisition.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchEVM() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/bb295da3-a77c-0e3a-59b7-9793e0d21eae.htm language=enus -->
## TOPIC 00103: rfmxdemoddotnet/html/bb295da3-a77c-0e3a-59b7-9793e0d21eae.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/bb295da3-a77c-0e3a-59b7-9793e0d21eae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/bb295da3-a77c-0e3a-59b7-9793e0d21eae.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXIQPowerEdgeTriggerLevelType Enumeration

RFmxDemodMXIQPowerEdgeTriggerLevelType Enumeration

SetIQPowerEdgeTriggerLevel(String, Double)

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXIQPowerEdgeTriggerLevelType
```

```text
Public Enumeration RFmxDemodMXIQPowerEdgeTriggerLevelType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The RFmxDemodMXIQPowerEdgeTriggerLevel method specifies the absolute power. |
| Absolute | 1 | The value of the RFmxDemodMXIQPowerEdgeTriggerLevel method is relative to the value of the ConfigureReferenceLevel(String, Double) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/bf1d0f98-150d-e82b-2c23-5796f53f3789.htm language=enus -->
## TOPIC 00104: rfmxdemoddotnet/html/bf1d0f98-150d-e82b-2c23-5796f53f3789.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/bf1d0f98-150d-e82b-2c23-5796f53f3789.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/bf1d0f98-150d-e82b-2c23-5796f53f3789.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.ConfigureMeasurementInterval Method

RFmxDemodMXADemodConfigurationConfigureMeasurementInterval Method

Configures the measurement interval for analog demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementInterval(
	string selectorString,
	double measurementInterval
)
```

```text
Public Function ConfigureMeasurementInterval ( 
	selectorString As String,
	measurementInterval As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementInterval Double**
  - Specifies the signal acquisition time, in seconds, for analog demodulation measurements.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodCfgMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/c0318158-f658-7c1c-5991-1f2a1a358a47.htm language=enus -->
## TOPIC 00105: rfmxdemoddotnet/html/c0318158-f658-7c1c-5991-1f2a1a358a47.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/c0318158-f658-7c1c-5991-1f2a1a358a47.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/c0318158-f658-7c1c-5991-1f2a1a358a47.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetRbwFilterAlpha Method

RFmxDemodMXADemodConfigurationGetRbwFilterAlpha Method

Gets the roll-off factor of the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterAlpha(
	string selectorString,
	out double value
)
```

```text
Public Function GetRbwFilterAlpha ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the roll-off factor of the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetRBWFilterAlpha() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/c206f699-3188-40ce-4aec-d854892d56f1.htm language=enus -->
## TOPIC 00106: rfmxdemoddotnet/html/c206f699-3188-40ce-4aec-d854892d56f1.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/c206f699-3188-40ce-4aec-d854892d56f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/c206f699-3188-40ce-4aec-d854892d56f1.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemod.Configuration Property

RFmxDemodMXDDemodConfiguration Property

RFmxDemodMXDDemodConfiguration

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxDemodMXDDemodConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxDemodMXDDemodConfiguration
	Get
```

###### Property Value

RFmxDemodMXDDemodConfiguration

##### See Also

###### Reference

RFmxDemodMXDDemod Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/c215d03d-14f3-f5e8-7e50-c8ab2d68eeb7.htm language=enus -->
## TOPIC 00107: rfmxdemoddotnet/html/c215d03d-14f3-f5e8-7e50-c8ab2d68eeb7.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/c215d03d-14f3-f5e8-7e50-c8ab2d68eeb7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/c215d03d-14f3-f5e8-7e50-c8ab2d68eeb7.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants Fields

RFmxDemodMXConstants Fields

The [RFmxDemodMXConstants](673c61cd-d38a-ce29-8ef4-abe381846173.htm) type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | Exports the signal to the PFI 0 connector on the NI 5142. |
|  | Pfi1 | Exports the signal to the PFI 1 connector on the NI 5142 and NI 5622. |
|  | PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. |
|  | PxiStarLine | Exports the signal to the PXI star trigger line. |
|  | PxiTriggerLine0 | Exports the signal to the PXI trigger line 0. |
|  | PxiTriggerLine1 | Exports the signal to the PXI trigger line 1. |
|  | PxiTriggerLine2 | Exports the signal to the PXI trigger line 2. |
|  | PxiTriggerLine3 | Exports the signal to the PXI trigger line 3. |
|  | PxiTriggerLine4 | Exports the signal to the PXI trigger line 4. |
|  | PxiTriggerLine5 | Exports the signal to the PXI trigger line 5. |
|  | PxiTriggerLine6 | Exports the signal to the PXI trigger line 6. |
|  | PxiTriggerLine7 | Exports the signal to the PXI trigger line 7. |
|  | TimerEvent | The trigger is received from the timer event. |

Top

##### See Also

###### Reference

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/c30d663e-35ea-38a2-d3b4-8ea7137a6601.htm language=enus -->
## TOPIC 00108: rfmxdemoddotnet/html/c30d663e-35ea-38a2-d3b4-8ea7137a6601.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/c30d663e-35ea-38a2-d3b4-8ea7137a6601.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/c30d663e-35ea-38a2-d3b4-8ea7137a6601.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults Class

RFmxDemodMXADemodResults Class

Provides methods to fetch and read the analog demodulation measurement results.

##### Inheritance Hierarchy

RFmxDemodMXSubObject

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxDemodMXADemodResults : RFmxDemodMXSubObject
```

```text
Public NotInheritable Class RFmxDemodMXADemodResults
	Inherits RFmxDemodMXSubObject
```

The RFmxDemodMXADemodResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchAMMaximumModulationDepth | Fetches the amplitude-modulated (AM) maximum modulation depth. |
|  | FetchAMMeanModulationDepth | Fetches amplitude-modulated (AM) mean modulation depth for analog demodulation measurements. |
|  | FetchCarrierMeasurement | Fetches the carrier measurement. |
|  | FetchDemodSignalTrace | Fetches the demodulated signal trace. |
|  | FetchDemodSpectrumTrace | Fetches the demodulated signal spectrum trace. |
|  | FetchDistortions | Fetches distortions for analog demodulation measurements. |
|  | FetchFMMaximumDeviation | Fetches the frequency-modulated (FM) maximum deviation measurements. |
|  | FetchFMMeanDeviation | Fetches the frequency-modulated (FM) mean deviation measurements. |
|  | FetchMeanModulationFrequency | Fetches the mean modulation frequency. |
|  | FetchPMMaximumDeviation | Fetches the phase-modulated (PM) maximum deviation. |
|  | FetchPMMeanDeviation | Fetches the phase-modulated (PM) mean deviation measurements. |
|  | GetAMModulationDepthMaximumHalfPeakToPeak | Gets the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
|  | GetAMModulationDepthMaximumNegativePeak | Gets the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
|  | GetAMModulationDepthMaximumPositivePeak | Gets the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
|  | GetAMModulationDepthMaximumRms | Gets the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
|  | GetAMModulationDepthMaximumStandardDeviation | Gets the maximum modulation depth measured across multiple acquisitions, as a percentage. |
|  | GetAMModulationDepthMeanHalfPeakToPeak | Gets the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage. |
|  | GetAMModulationDepthMeanNegativePeak | Gets the mean negative peak amplitude of the modulating signal, as a percentage. |
|  | GetAMModulationDepthMeanPositivePeak | Gets the mean positive peak amplitude of the modulating signal, as a percentage. |
|  | GetAMModulationDepthMeanRms | Gets the mean root mean square (RMS) amplitude of the modulating signal, as a percentage. |
|  | GetAMModulationDepthMeanStandardDeviation | Gets the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |
|  | GetAverageSinad | Gets the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. |
|  | GetAverageSnr | Gets the averaged signal-to-noise ratio, in dB, of the demodulated signal. |
|  | GetAverageThd | Gets the average of total harmonic distortion (THD) present in the signal, as a percentage. |
|  | GetAverageThdWithNoise | Gets the average of total harmonic distortion (THD) and noise present in the signal, as a percentage. |
|  | GetFMDeviationMaximumHalfPeakToPeak | Gets the maximum (peak-to-peak)/2 frequency variation, in hertz (Hz), around the nominal frequency of the FM carrier measured across multiple acquisitions. |
|  | GetFMDeviationMaximumNegativePeak | Gets the maximum negative peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions. |
|  | GetFMDeviationMaximumPositivePeak | Gets the maximum positive peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions. |
|  | GetFMDeviationMaximumRms | Gets the maximum root mean squared (RMS) frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions. |
|  | GetFMDeviationMaximumStandardDeviation | Gets the maximum frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions. |
|  | GetFMDeviationMeanHalfPeakToPeak | Gets the mean (peak-to-peak)/2 frequency variation, in hertz (Hz), around the nominal frequency of the frequency-modulated (FM) carrier. |
|  | GetFMDeviationMeanNegativePeak | Gets the mean negative peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal. |
|  | GetFMDeviationMeanPositivePeak | Gets the mean positive peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal. |
|  | GetFMDeviationMeanRms | Gets the mean RMS frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal. |
|  | GetFMDeviationMeanStandardDeviation | Gets the mean frequency deviation, in hertz (Hz), around the nominal frequency of the FM carrier. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeanCarrierFrequencyError | Gets the mean of the measured carrier frequency offset, in hertz (Hz). |
|  | GetMeanCarrierPower | Gets the mean of the measured carrier power, in dBm. |
|  | GetMeanModulationFrequency | Gets the mean of the demodulated signal frequency, in hertz (Hz). |
|  | GetPMDeviationMaximumHalfPeakToPeak | Gets the maximum (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
|  | GetPMDeviationMaximumNegativePeak | Gets the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
|  | GetPMDeviationMaximumPositivePeak | Gets the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
|  | GetPMDeviationMaximumRms | Gets the maximum root mean squared (RMS) phase deviation, in degrees, of the phase-modulated (PM) signal measured across multiple acquisitions. |
|  | GetPMDeviationMaximumStandardDeviation | Gets the maximum phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
|  | GetPMDeviationMeanHalfPeakToPeak | Gets the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. |
|  | GetPMDeviationMeanNegativePeak | Gets the mean negative peak phase deviation, in degrees, around the unmodulated carrier phase. |
|  | GetPMDeviationMeanPositivePeak | Gets the the mean positive peak phase deviation, in degrees, around the unmodulated carrier phase. |
|  | GetPMDeviationMeanRms | Gets the mean root mean squared (RMS) phase deviation, in degrees, of the phase-modulated (PM) signal. |
|  | GetPMDeviationMeanStandardDeviation | Gets the the mean phase deviation, in degrees, around the unmodulated carrier phase. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ReadAM | Configures hardware for acquisition, performs measurement on acquired data, and returns the amplitude-modulated (AM) measurement results. |
|  | ReadFM | Configures hardware for acquisition, performs measurement on acquired data, and returns the frequency-modulated (FM) measurement results. |
|  | ReadPM | Configures hardware for acquisition, performs measurement on acquired data, and returns the phase-modulated (PM) measurement results. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### Remarks

For more information about RFmx Demod, refer to the RFmx Demod Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/c75f3e5a-918d-13a8-961f-948331e5dfd7.htm language=enus -->
## TOPIC 00109: rfmxdemoddotnet/html/c75f3e5a-918d-13a8-961f-948331e5dfd7.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/c75f3e5a-918d-13a8-961f-948331e5dfd7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/c75f3e5a-918d-13a8-961f-948331e5dfd7.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetAMModulationDepthMeanStandardDeviation Method

RFmxDemodMXADemodResultsGetAMModulationDepthMeanStandardDeviation Method

Gets the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMModulationDepthMeanStandardDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetAMModulationDepthMeanStandardDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanStandardDeviation() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/c8cc3eba-fb90-f482-14e1-3170d2c3ae7d.htm language=enus -->
## TOPIC 00110: rfmxdemoddotnet/html/c8cc3eba-fb90-f482-14e1-3170d2c3ae7d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/c8cc3eba-fb90-f482-14e1-3170d2c3ae7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/c8cc3eba-fb90-f482-14e1-3170d2c3ae7d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetOffsetEvmMaximumPeak Method

RFmxDemodMXDDemodResultsGetOffsetEvmMaximumPeak Method

Gets the maximum of the peak error vector magnitude (EVM), as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetEvmMaximumPeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetEvmMaximumPeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsOffsetEVMMaximumPeak() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/cad0b965-adab-8a93-299f-3dca4767db7b.htm language=enus -->
## TOPIC 00111: rfmxdemoddotnet/html/cad0b965-adab-8a93-299f-3dca4767db7b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/cad0b965-adab-8a93-299f-3dca4767db7b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/cad0b965-adab-8a93-299f-3dca4767db7b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetEvmMeanModulationErrorRatio Method

RFmxDemodMXDDemodResultsGetEvmMeanModulationErrorRatio Method

Gets the modulation error ratio (MER), in dB.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEvmMeanModulationErrorRatio(
	string selectorString,
	out double value
)
```

```text
Public Function GetEvmMeanModulationErrorRatio ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the MER, in dB.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsEVMMeanModulationErrorRatio() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/cb47d9e7-a8ec-e728-6109-49a54ada546c.htm language=enus -->
## TOPIC 00112: rfmxdemoddotnet/html/cb47d9e7-a8ec-e728-6109-49a54ada546c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/cb47d9e7-a8ec-e728-6109-49a54ada546c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/cb47d9e7-a8ec-e728-6109-49a54ada546c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetFMDeviationMaximumRms Method

RFmxDemodMXADemodResultsGetFMDeviationMaximumRms Method

Gets the maximum root mean squared (RMS) frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFMDeviationMaximumRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetFMDeviationMaximumRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum RMS frequency deviation, in Hz, of the FM signal measured across multiple acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMaximumRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/cbaf5893-67f6-247e-ff13-161a4c4f5ad2.htm language=enus -->
## TOPIC 00113: rfmxdemoddotnet/html/cbaf5893-67f6-247e-ff13-161a4c4f5ad2.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/cbaf5893-67f6-247e-ff13-161a4c4f5ad2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/cbaf5893-67f6-247e-ff13-161a4c4f5ad2.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.GetPMDeviationMaximumPositivePeak Method

RFmxDemodMXADemodResultsGetPMDeviationMaximumPositivePeak Method

Gets the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPMDeviationMaximumPositivePeak(
	string selectorString,
	out double value
)
```

```text
Public Function GetPMDeviationMaximumPositivePeak ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumPositivePeak() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/cf8decdf-5fce-655d-efc5-237df19f2797.htm language=enus -->
## TOPIC 00114: rfmxdemoddotnet/html/cf8decdf-5fce-655d-efc5-237df19f2797.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/cf8decdf-5fce-655d-efc5-237df19f2797.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/cf8decdf-5fce-655d-efc5-237df19f2797.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.GetOffsetEvmMeanRms Method

RFmxDemodMXDDemodResultsGetOffsetEvmMeanRms Method

Gets the mean of the RMS EVM measured per acquisition, as a percentage.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetEvmMeanRms(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetEvmMeanRms ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean of the RMS EVM measured per acquisition, as a percentage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetResultsOffsetEVMMeanRMS() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d05d8e89-87f4-58a5-f572-a2251adfa98b.htm language=enus -->
## TOPIC 00115: rfmxdemoddotnet/html/d05d8e89-87f4-58a5-f572-a2251adfa98b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d05d8e89-87f4-58a5-f572-a2251adfa98b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d05d8e89-87f4-58a5-f572-a2251adfa98b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigureFskDeviation Method

RFmxDemodMXDDemodConfigurationConfigureFskDeviation Method

Configures the expected frequency-shift keying (FSK) deviation.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFskDeviation(
	string selectorString,
	double fskDeviation,
	RFmxDemodMXDDemodFskReferenceCompensationEnabled fskRefCompEnabled
)
```

```text
Public Function ConfigureFskDeviation ( 
	selectorString As String,
	fskDeviation As Double,
	fskRefCompEnabled As RFmxDemodMXDDemodFskReferenceCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **fskDeviation Double**
  - Specifies the expected FSK frequency deviation.
- **fskRefCompEnabled RFmxDemodMXDDemodFskReferenceCompensationEnabled**
  - Specifies whether the FSK deviation that you specify is to be compensated for gain errors, and is used to compute FSK error.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodCfgFSKDeviation() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d2e8a19c-efed-5f30-9d45-aec91ef6b5cb.htm language=enus -->
## TOPIC 00116: rfmxdemoddotnet/html/d2e8a19c-efed-5f30-9d45-aec91ef6b5cb.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d2e8a19c-efed-5f30-9d45-aec91ef6b5cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d2e8a19c-efed-5f30-9d45-aec91ef6b5cb.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration Class

RFmxDemodMXADemodConfiguration Class

Provides methods to configure analog demodulation measurements.

##### Inheritance Hierarchy

RFmxDemodMXSubObject

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxDemodMXADemodConfiguration : RFmxDemodMXSubObject
```

```text
Public NotInheritable Class RFmxDemodMXADemodConfiguration
	Inherits RFmxDemodMXSubObject
```

The RFmxDemodMXADemodConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAMCarrierSuppressed | Configures the presence of the amplitude modulated (AM) carrier. |
|  | ConfigureAudioFilter | Configures the audio filter for analog demodulation measurements. |
|  | ConfigureAveraging | Configures averaging for analog demodulation measurements. |
|  | ConfigureCarrierCorrection | Configures the carrier correction in analog demodulation measurements. |
|  | ConfigureFMDeEmphasis | Configures analog demodulation measurements for the de-emphasis filter in the FM transmitter. |
|  | ConfigureMeasurementInterval | Configures the measurement interval for analog demodulation measurements. |
|  | ConfigureModulationType | Configures the modulation type for analog demodulated measurements. |
|  | ConfigureRbwFilter | Configures the resolution bandwidth (RBW) filter. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether the traces to be stored and retrieved after performing the analog demodulation measurements is enabled. |
|  | GetAMCarrierSuppressed | Gets whether the carrier of the AM (amplitude modulated) signal is absent. |
|  | GetAudioFilterLowerCutoffFrequency | Gets the lower cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | GetAudioFilterType | Gets the audio filter to be applied on the analog demodulated signal. |
|  | GetAudioFilterUpperCutoffFrequency | Gets the upper cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | GetAudioMeasurementEnabled | Gets whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging. |
|  | GetAveragingEnabled | Gets whether averaging is enabled. |
|  | GetAveragingType | Gets the averaging type for the measurement. |
|  | GetCarrierCorrectionFrequencyEnabled | Gets whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. |
|  | GetCarrierCorrectionPhaseEnabled | Gets whether to correct the carrier phase error when demodulating phase-modulated (PM) signals. |
|  | GetFMDeEmphasis | Gets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether the analog demodulation measurement is enabled. |
|  | GetMeasurementInterval | Gets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. |
|  | GetModulationType | Gets the digital modulation type of the signal that needs to be analyzed. |
|  | GetRbwFilterAlpha | Gets the roll-off factor of the root-raised-cosine (RRC) filter. |
|  | GetRbwFilterBandwidth | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter to be applied to the signal acquired. |
|  | GetRbwFilterType | Gets the shape of the digital resolution bandwidth (RBW) filter. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement. |
|  | SetAMCarrierSuppressed | Sets whether the carrier of the AM (amplitude modulated) signal is absent. |
|  | SetAudioFilterLowerCutoffFrequency | Sets the lower cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | SetAudioFilterType | Sets the audio filter to be applied on the analog demodulated signal. |
|  | SetAudioFilterUpperCutoffFrequency | Sets the upper cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | SetAudioMeasurementEnabled | Sets whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the measurement. |
|  | SetAveragingType | Sets the averaging type for the measurement. |
|  | SetCarrierCorrectionFrequencyEnabled | Sets whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. |
|  | SetCarrierCorrectionPhaseEnabled | Sets whether to correct the carrier phase error when demodulating phase-modulated (PM) signals. |
|  | SetFMDeEmphasis | Sets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter. |
|  | SetMeasurementEnabled | Sets whether to enable the analog demodulation measurements. |
|  | SetMeasurementInterval | Sets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. |
|  | SetModulationType | Sets the digital modulation type of the signal that needs to be analyzed. |
|  | SetRbwFilterAlpha | Sets the roll-off factor of the root-raised-cosine (RRC) filter. |
|  | SetRbwFilterBandwidth | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter to be applied to the signal acquired using zero span. |
|  | SetRbwFilterType | Sets the shape of the digital resolution bandwidth (RBW) filter. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### Remarks

For more information about RFmx Demod, refer to the RFmx Demod Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d3153e51-a222-c1f0-2739-41b7c2d63281.htm language=enus -->
## TOPIC 00117: rfmxdemoddotnet/html/d3153e51-a222-c1f0-2739-41b7c2d63281.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d3153e51-a222-c1f0-2739-41b7c2d63281.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d3153e51-a222-c1f0-2739-41b7c2d63281.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants.PxiTriggerLine1 Field

RFmxDemodMXConstantsPxiTriggerLine1 Field

Exports the signal to the PXI trigger line 1.

Namespace:

NationalInstruments.RFmx.DemodMX

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

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d41f3c3a-db8a-70ed-b8f1-c7c5c08f334b.htm language=enus -->
## TOPIC 00118: rfmxdemoddotnet/html/d41f3c3a-db8a-70ed-b8f1-c7c5c08f334b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d41f3c3a-db8a-70ed-b8f1-c7c5c08f334b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d41f3c3a-db8a-70ed-b8f1-c7c5c08f334b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodResults.FetchMeanRhoFactor Method

RFmxDemodMXDDemodResultsFetchMeanRhoFactor Method

Fetches the correlation of the measurement waveform and the reference waveform.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeanRhoFactor(
	string selectorString,
	double timeout,
	out double meanRhoFactor
)
```

```text
Public Function FetchMeanRhoFactor ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRhoFactor As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRhoFactor Double**
  - Upon return, contains the correlation of the measurement waveform and the reference waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodFetchMeanRhoFactor() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d7934783-54df-6f80-1386-b80ae52e07ff.htm language=enus -->
## TOPIC 00119: rfmxdemoddotnet/html/d7934783-54df-6f80-1386-b80ae52e07ff.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d7934783-54df-6f80-1386-b80ae52e07ff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d7934783-54df-6f80-1386-b80ae52e07ff.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetMeasurementInterval Method

RFmxDemodMXADemodConfigurationGetMeasurementInterval Method

Gets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeasurementInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the signal acquisition time, in seconds, for the analog demodulation measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d7fb4cbe-58e6-28c9-9000-72a1c845e6bc.htm language=enus -->
## TOPIC 00120: rfmxdemoddotnet/html/d7fb4cbe-58e6-28c9-9000-72a1c845e6bc.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d7fb4cbe-58e6-28c9-9000-72a1c845e6bc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d7fb4cbe-58e6-28c9-9000-72a1c845e6bc.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetResultFetchTimeout Method

RFmxDemodMXGetResultFetchTimeout Method

Gets the time, in seconds, for which the measurement waits for fetching results.

Namespace:

NationalInstruments.RFmx.DemodMX

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

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the time, in seconds, for which the measurement waits for fetching results.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetResultFetchTimeout() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/d93f9768-0205-850f-a04f-5a01dd71007a.htm language=enus -->
## TOPIC 00121: rfmxdemoddotnet/html/d93f9768-0205-850f-a04f-5a01dd71007a.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/d93f9768-0205-850f-a04f-5a01dd71007a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/d93f9768-0205-850f-a04f-5a01dd71007a.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.ConfigureExternalAttenuation Method

RFmxDemodMXConfigureExternalAttenuation Method

Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureExternalAttenuation(
	string selectorString,
	double externalAttenuation
)
```

```text
Public Function ConfigureExternalAttenuation ( 
	selectorString As String,
	externalAttenuation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **externalAttenuation Double**
  - Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_CfgExternalAttenuation() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/e0a5bf77-c363-1e76-aca6-cde8976ecc0b.htm language=enus -->
## TOPIC 00122: rfmxdemoddotnet/html/e0a5bf77-c363-1e76-aca6-cde8976ecc0b.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/e0a5bf77-c363-1e76-aca6-cde8976ecc0b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/e0a5bf77-c363-1e76-aca6-cde8976ecc0b.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetIQPowerEdgeTriggerSource Method

RFmxDemodMXGetIQPowerEdgeTriggerSource Method

Gets the channel from which the device monitors the trigger.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - Pass an empty string. The signal name passed when creating the signal configuration is used.
- **value String**
  - Upon return, contains the channel from which the device monitors the trigger.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_GetIQPowerEdgeTriggerSource() function in C.

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/e25ef582-a046-1c43-4ca5-77dc1a4ea42c.htm language=enus -->
## TOPIC 00123: rfmxdemoddotnet/html/e25ef582-a046-1c43-4ca5-77dc1a4ea42c.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/e25ef582-a046-1c43-4ca5-77dc1a4ea42c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/e25ef582-a046-1c43-4ca5-77dc1a4ea42c.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetSymbolMapType Method

RFmxDemodMXDDemodConfigurationGetSymbolMapType Method

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSymbolMapType(
	string selectorString,
	out RFmxDemodMXDDemodSymbolMapType value
)
```

```text
Public Function GetSymbolMapType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXDDemodSymbolMapType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodSymbolMapType**
  - Upon return, contains the value that indicates whether the measurement uses the default symbol map or the map that you configure using the ConfigureSymbolMap(String, RFmxDemodMXDDemodSymbolMapType, ComplexSingle) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetSymbolMapType() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/e2bdf7a8-c26d-7295-db78-55689f36a7b3.htm language=enus -->
## TOPIC 00124: rfmxdemoddotnet/html/e2bdf7a8-c26d-7295-db78-55689f36a7b3.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/e2bdf7a8-c26d-7295-db78-55689f36a7b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/e2bdf7a8-c26d-7295-db78-55689f36a7b3.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodResults.FetchAMMeanModulationDepth Method

RFmxDemodMXADemodResultsFetchAMMeanModulationDepth Method

Fetches amplitude-modulated (AM) mean modulation depth for analog demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAMMeanModulationDepth(
	string selectorString,
	double timeout,
	out double meanModulationDepth,
	out double meanHalfPeakToPeak,
	out double meanRms,
	out double meanPositivePeak,
	out double meanNegativePeak
)
```

```text
Public Function FetchAMMeanModulationDepth ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanModulationDepth As Double,
	<OutAttribute> ByRef meanHalfPeakToPeak As Double,
	<OutAttribute> ByRef meanRms As Double,
	<OutAttribute> ByRef meanPositivePeak As Double,
	<OutAttribute> ByRef meanNegativePeak As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.
- **meanModulationDepth Double**
  - Upon return, contains the mean amplitude variation, in percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.
- **meanHalfPeakToPeak Double**
  - Upon return, contains the mean (peak-to-peak)/2 amplitude, in percentage, of the modulating signal.
- **meanRms Double**
  - Upon return, contains the mean RMS amplitude of the modulating signal.
- **meanPositivePeak Double**
  - Upon return, contains the mean positive peak amplitude, in percentage, of the modulating signal.
- **meanNegativePeak Double**
  - Upon return, contains the mean negative peak amplitude, in percentage, of the modulating signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodFetchAMMeanModulationDepth() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodResults Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/e6a96684-8066-d260-e998-c1284f313933.htm language=enus -->
## TOPIC 00125: rfmxdemoddotnet/html/e6a96684-8066-d260-e998-c1284f313933.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/e6a96684-8066-d260-e998-c1284f313933.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/e6a96684-8066-d260-e998-c1284f313933.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMX.GetAttributeBool Method

RFmxDemodMXGetAttributeBool Method

Gets the value of a Boolean attribute.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeBool(
	string selectorString,
	int attributeIdentifier,
	out bool value
)
```

```text
Public Function GetAttributeBool ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Boolean**
  - Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxDemodMX Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/e6ec7ad6-0a32-193a-33ed-5f0e4edfd0b3.htm language=enus -->
## TOPIC 00126: rfmxdemoddotnet/html/e6ec7ad6-0a32-193a-33ed-5f0e4edfd0b3.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/e6ec7ad6-0a32-193a-33ed-5f0e4edfd0b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/e6ec7ad6-0a32-193a-33ed-5f0e4edfd0b3.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXConstants.PxieDStarBLine Field

RFmxDemodMXConstantsPxieDStarBLine Field

The signal is exported to the PXIe DStar B trigger line.

Namespace:

NationalInstruments.RFmx.DemodMX

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

RFmxDemodMXConstants Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f61889bc-f321-93b5-2d69-7b54532fdaa7.htm language=enus -->
## TOPIC 00127: rfmxdemoddotnet/html/f61889bc-f321-93b5-2d69-7b54532fdaa7.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f61889bc-f321-93b5-2d69-7b54532fdaa7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f61889bc-f321-93b5-2d69-7b54532fdaa7.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration Methods

RFmxDemodMXADemodConfiguration Methods

The [RFmxDemodMXADemodConfiguration](d2e8a19c-efed-5f30-9d45-aec91ef6b5cb.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAMCarrierSuppressed | Configures the presence of the amplitude modulated (AM) carrier. |
|  | ConfigureAudioFilter | Configures the audio filter for analog demodulation measurements. |
|  | ConfigureAveraging | Configures averaging for analog demodulation measurements. |
|  | ConfigureCarrierCorrection | Configures the carrier correction in analog demodulation measurements. |
|  | ConfigureFMDeEmphasis | Configures analog demodulation measurements for the de-emphasis filter in the FM transmitter. |
|  | ConfigureMeasurementInterval | Configures the measurement interval for analog demodulation measurements. |
|  | ConfigureModulationType | Configures the modulation type for analog demodulated measurements. |
|  | ConfigureRbwFilter | Configures the resolution bandwidth (RBW) filter. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether the traces to be stored and retrieved after performing the analog demodulation measurements is enabled. |
|  | GetAMCarrierSuppressed | Gets whether the carrier of the AM (amplitude modulated) signal is absent. |
|  | GetAudioFilterLowerCutoffFrequency | Gets the lower cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | GetAudioFilterType | Gets the audio filter to be applied on the analog demodulated signal. |
|  | GetAudioFilterUpperCutoffFrequency | Gets the upper cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | GetAudioMeasurementEnabled | Gets whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging. |
|  | GetAveragingEnabled | Gets whether averaging is enabled. |
|  | GetAveragingType | Gets the averaging type for the measurement. |
|  | GetCarrierCorrectionFrequencyEnabled | Gets whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. |
|  | GetCarrierCorrectionPhaseEnabled | Gets whether to correct the carrier phase error when demodulating phase-modulated (PM) signals. |
|  | GetFMDeEmphasis | Gets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether the analog demodulation measurement is enabled. |
|  | GetMeasurementInterval | Gets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. |
|  | GetModulationType | Gets the digital modulation type of the signal that needs to be analyzed. |
|  | GetRbwFilterAlpha | Gets the roll-off factor of the root-raised-cosine (RRC) filter. |
|  | GetRbwFilterBandwidth | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter to be applied to the signal acquired. |
|  | GetRbwFilterType | Gets the shape of the digital resolution bandwidth (RBW) filter. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement. |
|  | SetAMCarrierSuppressed | Sets whether the carrier of the AM (amplitude modulated) signal is absent. |
|  | SetAudioFilterLowerCutoffFrequency | Sets the lower cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | SetAudioFilterType | Sets the audio filter to be applied on the analog demodulated signal. |
|  | SetAudioFilterUpperCutoffFrequency | Sets the upper cutoff frequency, in hertz (Hz), of the custom audio filter. |
|  | SetAudioMeasurementEnabled | Sets whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the measurement. |
|  | SetAveragingType | Sets the averaging type for the measurement. |
|  | SetCarrierCorrectionFrequencyEnabled | Sets whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. |
|  | SetCarrierCorrectionPhaseEnabled | Sets whether to correct the carrier phase error when demodulating phase-modulated (PM) signals. |
|  | SetFMDeEmphasis | Sets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter. |
|  | SetMeasurementEnabled | Sets whether to enable the analog demodulation measurements. |
|  | SetMeasurementInterval | Sets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. |
|  | SetModulationType | Sets the digital modulation type of the signal that needs to be analyzed. |
|  | SetRbwFilterAlpha | Sets the roll-off factor of the root-raised-cosine (RRC) filter. |
|  | SetRbwFilterBandwidth | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter to be applied to the signal acquired using zero span. |
|  | SetRbwFilterType | Sets the shape of the digital resolution bandwidth (RBW) filter. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f664c86f-cbee-4adb-bbf9-2e505a663182.htm language=enus -->
## TOPIC 00128: rfmxdemoddotnet/html/f664c86f-cbee-4adb-bbf9-2e505a663182.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f664c86f-cbee-4adb-bbf9-2e505a663182.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f664c86f-cbee-4adb-bbf9-2e505a663182.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodM Enumeration

RFmxDemodMXDDemodM Enumeration

Specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXDDemodM
```

```text
Public Enumeration RFmxDemodMXDDemodM
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| M2 | 2 | The M-ary number is 2. |
| M4 | 4 | The M-ary number is 4. |
| M8 | 8 | The M-ary number is 8. |
| M16 | 16 | The M-ary number is 16. |
| M32 | 32 | The M-ary number is 32. |
| M64 | 64 | The M-ary number is 64. |
| M128 | 128 | The M-ary number is 128. |
| M256 | 256 | The M-ary number is 256. |
| M512 | 512 | The M-ary number is 512. |
| M1024 | 1,024 | The M-ary number is 1024. |
| M2048 | 2,048 | The M-ary number is 2048. |
| M4096 | 4,096 | The M-ary number is 4096. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f71899c8-fd6d-46f2-529a-d63bdab4150f.htm language=enus -->
## TOPIC 00129: rfmxdemoddotnet/html/f71899c8-fd6d-46f2-529a-d63bdab4150f.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f71899c8-fd6d-46f2-529a-d63bdab4150f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f71899c8-fd6d-46f2-529a-d63bdab4150f.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodAMCarrierSuppressedEnabled Enumeration

RFmxDemodMXADemodAMCarrierSuppressedEnabled Enumeration

Specifies whether the carrier of the amplitude modulated (AM) signal is absent.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxDemodMXADemodAMCarrierSuppressedEnabled
```

```text
Public Enumeration RFmxDemodMXADemodAMCarrierSuppressedEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The carrier of the AM signal is present. |
| True | 1 | The carrier of the AM signal is absent. |

##### See Also

###### Reference

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f73294e7-af0e-cad3-9f0e-113b2bf159b8.htm language=enus -->
## TOPIC 00130: rfmxdemoddotnet/html/f73294e7-af0e-cad3-9f0e-113b2bf159b8.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f73294e7-af0e-cad3-9f0e-113b2bf159b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f73294e7-af0e-cad3-9f0e-113b2bf159b8.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigureSignalStructure Method

RFmxDemodMXDDemodConfigurationConfigureSignalStructure Method

Configures the structure of the incoming signal to be either a continuous signal or a bursty signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSignalStructure(
	string selectorString,
	RFmxDemodMXDDemodSignalStructure signalStructure
)
```

```text
Public Function ConfigureSignalStructure ( 
	selectorString As String,
	signalStructure As RFmxDemodMXDDemodSignalStructure
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **signalStructure RFmxDemodMXDDemodSignalStructure**
  - specifies whether the signal is either a bursty signal or a continuous signal.

###### Return Value

Int32

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f7463861-1218-1b2c-0220-e2364fd1ed22.htm language=enus -->
## TOPIC 00131: rfmxdemoddotnet/html/f7463861-1218-1b2c-0220-e2364fd1ed22.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f7463861-1218-1b2c-0220-e2364fd1ed22.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f7463861-1218-1b2c-0220-e2364fd1ed22.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetFskDeviation Method

RFmxDemodMXDDemodConfigurationSetFskDeviation Method

Sets the expected frequency-shift keying (FSK) frequency deviation. At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFskDeviation(
	string selectorString,
	double value
)
```

```text
Public Function SetFskDeviation ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the expected FSK frequency deviation.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodSetFSKDeviation() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f7cc9bef-0d2c-3533-c90a-6f1ca439aa42.htm language=enus -->
## TOPIC 00132: rfmxdemoddotnet/html/f7cc9bef-0d2c-3533-c90a-6f1ca439aa42.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f7cc9bef-0d2c-3533-c90a-6f1ca439aa42.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f7cc9bef-0d2c-3533-c90a-6f1ca439aa42.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.GetPulseShapingFilterType Method

RFmxDemodMXDDemodConfigurationGetPulseShapingFilterType Method

Gets the pulse-shaping filter used to transmit the signal.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseShapingFilterType(
	string selectorString,
	out RFmxDemodMXDDemodPulseShapingFilterType value
)
```

```text
Public Function GetPulseShapingFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXDDemodPulseShapingFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodPulseShapingFilterType**
  - Upon return, contains the pulse-shaping filter used to transmit the signal. This determines the measurement filter to be used for analysis when you set the SetMeasurementFilterType(String, RFmxDemodMXDDemodMeasurementFilterType) to Auto.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodGetPulseShapingFilterType() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/f8b15816-2530-8573-881f-331a84afa3a6.htm language=enus -->
## TOPIC 00133: rfmxdemoddotnet/html/f8b15816-2530-8573-881f-331a84afa3a6.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/f8b15816-2530-8573-881f-331a84afa3a6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/f8b15816-2530-8573-881f-331a84afa3a6.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.GetCarrierCorrectionPhaseEnabled Method

RFmxDemodMXADemodConfigurationGetCarrierCorrectionPhaseEnabled Method

Gets whether to correct the carrier phase error when demodulating phase-modulated (PM) signals.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierCorrectionPhaseEnabled(
	string selectorString,
	out RFmxDemodMXADemodCarrierPhaseCorrectionEnabled value
)
```

```text
Public Function GetCarrierCorrectionPhaseEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxDemodMXADemodCarrierPhaseCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXADemodCarrierPhaseCorrectionEnabled**
  - Upon return, contains a value that indicates whether to correct the carrier phase error when demodulating PM signals.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodGetCarrierCorrectionPhaseEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/fa3c7144-f9e4-8ffc-725c-a7e97d770a48.htm language=enus -->
## TOPIC 00134: rfmxdemoddotnet/html/fa3c7144-f9e4-8ffc-725c-a7e97d770a48.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/fa3c7144-f9e4-8ffc-725c-a7e97d770a48.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/fa3c7144-f9e4-8ffc-725c-a7e97d770a48.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.ConfigureSymbolRate Method

RFmxDemodMXDDemodConfigurationConfigureSymbolRate Method

Configures the symbol rate for digital demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSymbolRate(
	string selectorString,
	double symbolRate
)
```

```text
Public Function ConfigureSymbolRate ( 
	selectorString As String,
	symbolRate As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **symbolRate Double**
  - Specifies the symbol rate in hertz (Hz).

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodCfgSymbolRate() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/fb6ff8d9-360c-9ef0-732a-cdb35a4ea235.htm language=enus -->
## TOPIC 00135: rfmxdemoddotnet/html/fb6ff8d9-360c-9ef0-732a-cdb35a4ea235.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/fb6ff8d9-360c-9ef0-732a-cdb35a4ea235.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/fb6ff8d9-360c-9ef0-732a-cdb35a4ea235.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.SetMeasurementEnabled Method

RFmxDemodMXADemodConfigurationSetMeasurementEnabled Method

Sets whether to enable the analog demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

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
  - to enable the analog demodulation measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodSetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/fc5cfbf6-06a5-1d00-4ccf-cff1e9a7c699.htm language=enus -->
## TOPIC 00136: rfmxdemoddotnet/html/fc5cfbf6-06a5-1d00-4ccf-cff1e9a7c699.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/fc5cfbf6-06a5-1d00-4ccf-cff1e9a7c699.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/fc5cfbf6-06a5-1d00-4ccf-cff1e9a7c699.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXDDemodConfiguration.SetSymbolMapType Method

RFmxDemodMXDDemodConfigurationSetSymbolMapType Method

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSymbolMapType(
	string selectorString,
	RFmxDemodMXDDemodSymbolMapType value
)
```

```text
Public Function SetSymbolMapType ( 
	selectorString As String,
	value As RFmxDemodMXDDemodSymbolMapType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxDemodMXDDemodSymbolMapType**
  - Specifies whether the measurement uses the default symbol map or the map that you configure using the ConfigureSymbolMap(String, RFmxDemodMXDDemodSymbolMapType, ComplexSingle) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_DDemodSetSymbolMapType() function in C.

##### See Also

###### Reference

RFmxDemodMXDDemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-demod-dotnet path=rfmxdemoddotnet/html/fd3724cf-4bed-b85e-ca94-8306f00ad61d.htm language=enus -->
## TOPIC 00137: rfmxdemoddotnet/html/fd3724cf-4bed-b85e-ca94-8306f00ad61d.htm

- bundle_id: `rfmx-demod-dotnet`
- source_path: `rfmxdemoddotnet/html/fd3724cf-4bed-b85e-ca94-8306f00ad61d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-dotnet/raw/resource/enus/rfmxdemoddotnet/html/fd3724cf-4bed-b85e-ca94-8306f00ad61d.htm
- document_id: `rfmx-demod-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxDemodMXADemodConfiguration.ConfigureCarrierCorrection Method

RFmxDemodMXADemodConfigurationConfigureCarrierCorrection Method

Configures the carrier correction in analog demodulation measurements.

Namespace:

NationalInstruments.RFmx.DemodMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierCorrection(
	string selectorString,
	RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled carrierFrequencyCorrectionEnabled,
	RFmxDemodMXADemodCarrierPhaseCorrectionEnabled carrierPhaseCorrectionEnabled
)
```

```text
Public Function ConfigureCarrierCorrection ( 
	selectorString As String,
	carrierFrequencyCorrectionEnabled As RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled,
	carrierPhaseCorrectionEnabled As RFmxDemodMXADemodCarrierPhaseCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **carrierFrequencyCorrectionEnabled RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled**
  - Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated or phase-modulated signals.
- **carrierPhaseCorrectionEnabled RFmxDemodMXADemodCarrierPhaseCorrectionEnabled**
  - Specifies whether to correct the phase error in the carrier when demodulating phase-modulated signals.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxDemod_ADemodCfgCarrierCorrection() function in C.

##### See Also

###### Reference

RFmxDemodMXADemodConfiguration Class

NationalInstruments.RFmx.DemodMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
