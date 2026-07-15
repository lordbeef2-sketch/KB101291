# NI DOCUMENT BUNDLE: rfmx-specan-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-dotnet start=251 end=500 -->
<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/695eacc0-7f81-3ac8-6a3a-e9ac60618dec.htm language=enus -->
## TOPIC 00251: rfmxspecandotnet/html/695eacc0-7f81-3ac8-6a3a-e9ac60618dec.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/695eacc0-7f81-3ac8-6a3a-e9ac60618dec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/695eacc0-7f81-3ac8-6a3a-e9ac60618dec.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetRangeRelativeAttenuation Method

RFmxSpecAnMXSpurConfigurationGetRangeRelativeAttenuation Method

SetExternalAttenuation(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeRelativeAttenuation(
	string selectorString,
	out double value
)
```

```text
Public Function GetRangeRelativeAttenuation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the attenuation, in dB, relative to the external attenuation specified by the SetExternalAttenuation(String, Double) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetRangeRelativeAttenuation() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/69722686-adbf-106b-e9b5-2bf6cc3b76fe.htm language=enus -->
## TOPIC 00252: rfmxspecandotnet/html/69722686-adbf-106b-e9b5-2bf6cc3b76fe.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/69722686-adbf-106b-e9b5-2bf6cc3b76fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/69722686-adbf-106b-e9b5-2bf6cc3b76fe.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.Initiate Method

RFmxSpecAnMXListInitiate Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies a selector string comprising the result name. The result name can either be specified through this input or the resultName parameter.If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **resultName String**
  - Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1"

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6979a1ba-bc58-da50-c702-bd9749baa5fc.htm language=enus -->
## TOPIC 00253: rfmxspecandotnet/html/6979a1ba-bc58-da50-c702-bd9749baa5fc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6979a1ba-bc58-da50-c702-bd9749baa5fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6979a1ba-bc58-da50-c702-bd9749baa5fc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.FetchTotalCarrierPower Method

RFmxSpecAnMXAcpResultsFetchTotalCarrierPower Method

SetPowerUnits(String, RFmxSpecAnMXAcpPowerUnits)

dBm

SetPowerUnits(String, RFmxSpecAnMXAcpPowerUnits)

dBmPerHertz

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **totalCarrierPower Double**
  - Upon return, contains the total integrated power of all the active carriers measured when you set the SetPowerUnits(String, RFmxSpecAnMXAcpPowerUnits) method to dBm. This method returns the power spectral density based on the power in all the active carriers measured when you set the SetPowerUnits(String, RFmxSpecAnMXAcpPowerUnits) method to dBmPerHertz.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPFetchTotalCarrierPower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/697dbd6d-a4ba-4f6e-e76e-45a8b6d3f973.htm language=enus -->
## TOPIC 00254: rfmxspecandotnet/html/697dbd6d-a4ba-4f6e-e76e-45a8b6d3f973.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/697dbd6d-a4ba-4f6e-e76e-45a8b6d3f973.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/697dbd6d-a4ba-4f6e-e76e-45a8b6d3f973.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.GetGainExpansion Method

RFmxSpecAnMXIdpdConfigurationGetGainExpansion Method

Gets the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetGainExpansion(
	string selectorString,
	out double value
)
```

```text
Public Function GetGainExpansion ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

IdpdGainExpansion

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/69827016-0755-4609-f665-adc8ab3cc2d5.htm language=enus -->
## TOPIC 00255: rfmxspecandotnet/html/69827016-0755-4609-f665-adc8ab3cc2d5.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/69827016-0755-4609-f665-adc8ab3cc2d5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/69827016-0755-4609-f665-adc8ab3cc2d5.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetNumberOfCarriers Method

RFmxSpecAnMXChpConfigurationSetNumberOfCarriers Method

Sets the number of carriers.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfCarriers(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfCarriers ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetNumberOfCarriers() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/69b92a8d-4751-599c-9c37-d463f113b571.htm language=enus -->
## TOPIC 00256: rfmxspecandotnet/html/69b92a8d-4751-599c-9c37-d463f113b571.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/69b92a8d-4751-599c-9c37-d463f113b571.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/69b92a8d-4751-599c-9c37-d463f113b571.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetAllTracesEnabled Method

RFmxSpecAnMXSpurConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the spurious emissions (Spur) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - to enable the traces to be stored and retrieved after performing the Spur measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetAllTracesEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/69e90031-a823-8b17-f464-261562603d0d.htm language=enus -->
## TOPIC 00257: rfmxspecandotnet/html/69e90031-a823-8b17-f464-261562603d0d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/69e90031-a823-8b17-f464-261562603d0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/69e90031-a823-8b17-f464-261562603d0d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.Dispose Method

RFmxSpecAnMXListDispose Method

Deletes the list and clears any trace of the current list, if any.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

You can call this method safely more than once, even if the list is already deleted.

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6a7b4475-757f-4a1e-9c45-9be3383cd801.htm language=enus -->
## TOPIC 00258: rfmxspecandotnet/html/6a7b4475-757f-4a1e-9c45-9be3383cd801.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6a7b4475-757f-4a1e-9c45-9be3383cd801.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6a7b4475-757f-4a1e-9c45-9be3383cd801.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetCalibrationLossTemperature Method

RFmxSpecAnMXNFConfigurationSetCalibrationLossTemperature Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCalibrationLossTemperature(
	string selectorString,
	double value
)
```

```text
Public Function SetCalibrationLossTemperature ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the physical temperature of the ohmic loss elements specified by the SetCalibrationLoss(String, Double) method. This value is expressed in kelvin.

###### Return Value

Int32

##### Remarks

NFCalibrationLossTemperature

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6b32e057-a8aa-5c3d-a76c-b22e3be50539.htm language=enus -->
## TOPIC 00259: rfmxspecandotnet/html/6b32e057-a8aa-5c3d-a76c-b22e3be50539.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6b32e057-a8aa-5c3d-a76c-b22e3be50539.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6b32e057-a8aa-5c3d-a76c-b22e3be50539.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureNumberOfCarriers Method

RFmxSpecAnMXSemConfigurationConfigureNumberOfCarriers Method

Configures the number of carriers for the spectral emission mask (SEM) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfCarriers(
	string selectorString,
	int numberOfCarriers
)
```

```text
Public Function ConfigureNumberOfCarriers ( 
	selectorString As String,
	numberOfCarriers As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **numberOfCarriers Int32**
  - Specifies the number of carriers for the SEM measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgNumberOfCarriers() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6b381acb-9953-935e-f0b1-70b8e573805b.htm language=enus -->
## TOPIC 00260: rfmxspecandotnet/html/6b381acb-9953-935e-f0b1-70b8e573805b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6b381acb-9953-935e-f0b1-70b8e573805b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6b381acb-9953-935e-f0b1-70b8e573805b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetRbwFilterBandwidth Method

RFmxSpecAnMXIMConfigurationSetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxSpecAnMXIMRbwFilterAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxSpecAnMXIMRbwFilterAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

IMRbwFilterBandwidth

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6b681cfe-8394-7430-b4b4-2d6e87968fa7.htm language=enus -->
## TOPIC 00261: rfmxspecandotnet/html/6b681cfe-8394-7430-b4b4-2d6e87968fa7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6b681cfe-8394-7430-b4b4-2d6e87968fa7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6b681cfe-8394-7430-b4b4-2d6e87968fa7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetRrcFilterEnabled Method

RFmxSpecAnMXChpConfigurationGetRrcFilterEnabled Method

**Note: This API is now obsolete.**

Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use CarrierRrcFilterEnabled instead")]
public int GetRrcFilterEnabled(
	string selectorString,
	out RFmxSpecAnMXChpRrcFilterEnabled value
)
```

```text
<ObsoleteAttribute("Use CarrierRrcFilterEnabled instead")>
Public Function GetRrcFilterEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpRrcFilterEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpRrcFilterEnabled**
  - Upon return, indicates whether the RRC filter is applied on the acquired channel after measuring the channel power.

###### Return Value

Int32

##### Remarks

This method is obsoleted. Use GetCarrierRrcFilterEnabled method to get the value. This method maps to the RFmxSpecAn_CHPGetRRCFilterEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6b95c06d-4f4b-94f1-bed9-3d879bea1c10.htm language=enus -->
## TOPIC 00262: rfmxspecandotnet/html/6b95c06d-4f4b-94f1-bed9-3d879bea1c10.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6b95c06d-4f4b-94f1-bed9-3d879bea1c10.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6b95c06d-4f4b-94f1-bed9-3d879bea1c10.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.ConfigureRbwFilter Method

RFmxSpecAnMXTxpConfigurationConfigureRbwFilter Method

Configures the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRbwFilter(
	string selectorString,
	double rbw,
	RFmxSpecAnMXTxpRbwFilterType rbwFilterType,
	double rrcAlpha
)
```

```text
Public Function ConfigureRbwFilter ( 
	selectorString As String,
	rbw As Double,
	rbwFilterType As RFmxSpecAnMXTxpRbwFilterType,
	rrcAlpha As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rbw Double**
  - Specifies the bandwidth, in hertz (Hz), of the RBW filter used to measure the signal.
- **rbwFilterType RFmxSpecAnMXTxpRbwFilterType**
  - Specifies the shape of the digital RBW filter.
- **rrcAlpha Double**
  - Specifies the roll-off factor for the root-raised-cosine (RRC) filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPCfgRBWFilter() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6bfaea76-4ce4-7928-30e8-828acb65f99f.htm language=enus -->
## TOPIC 00263: rfmxspecandotnet/html/6bfaea76-4ce4-7928-30e8-828acb65f99f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6bfaea76-4ce4-7928-30e8-828acb65f99f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6bfaea76-4ce4-7928-30e8-828acb65f99f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFResults.FetchAnalyzerNoiseFigure Method

RFmxSpecAnMXNFResultsFetchAnalyzerNoiseFigure Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAnalyzerNoiseFigure(
	string selectorString,
	double timeout,
	ref double[] analyzerNoiseFigure
)
```

```text
Public Function FetchAnalyzerNoiseFigure ( 
	selectorString As String,
	timeout As Double,
	ByRef analyzerNoiseFigure As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **analyzerNoiseFigure Double**
  - Upon return, contains an array of the noise figure values of the analyzer measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6c289f12-a964-8916-3cd4-169d16afca38.htm language=enus -->
## TOPIC 00264: rfmxspecandotnet/html/6c289f12-a964-8916-3cd4-169d16afca38.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6c289f12-a964-8916-3cd4-169d16afca38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6c289f12-a964-8916-3cd4-169d16afca38.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpMeasurementMode Enumeration

RFmxSpecAnMXChpMeasurementMode Enumeration

Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpMeasurementMode
```

```text
Public Enumeration RFmxSpecAnMXChpMeasurementMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Measure | 0 | CHP measurement is performed on the acquired signal. |
| CalibrateNoiseFloor | 1 | Manual noise calibration of the signal analyzer is performed for the CHP measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6c4a7e2b-e404-9f68-a54e-5ec0af086223.htm language=enus -->
## TOPIC 00265: rfmxspecandotnet/html/6c4a7e2b-e404-9f68-a54e-5ec0af086223.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6c4a7e2b-e404-9f68-a54e-5ec0af086223.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6c4a7e2b-e404-9f68-a54e-5ec0af086223.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetSweepTimeInterval Method

RFmxSpecAnMXAcpConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxSpecAnMXAcpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the sweep time, in seconds, when you set SetSweepTimeAuto(String, RFmxSpecAnMXAcpSweepTimeAuto) to False.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetSweepTimeInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6d9a9863-9341-b0a8-8dd0-a4b67cd69bec.htm language=enus -->
## TOPIC 00266: rfmxspecandotnet/html/6d9a9863-9341-b0a8-8dd0-a4b67cd69bec.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6d9a9863-9341-b0a8-8dd0-a4b67cd69bec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6d9a9863-9341-b0a8-8dd0-a4b67cd69bec.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetDutType Method

RFmxSpecAnMXNFConfigurationGetDutType Method

Gets the type of DUT.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDutType(
	string selectorString,
	out RFmxSpecAnMXNFDutType value
)
```

```text
Public Function GetDutType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXNFDutType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFDutType**
  - Upon return, contains the type of DUT.

###### Return Value

Int32

##### Remarks

NFDutType

Amplifier

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6dcf974d-34c6-bbf4-1de8-32ebc46b67a3.htm language=enus -->
## TOPIC 00267: rfmxspecandotnet/html/6dcf974d-34c6-bbf4-1de8-32ebc46b67a3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6dcf974d-34c6-bbf4-1de8-32ebc46b67a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6dcf974d-34c6-bbf4-1de8-32ebc46b67a3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChp Properties

RFmxSpecAnMXChp Properties

The [RFmxSpecAnMXChp](1c5d7ca7-b725-c4b9-5a91-55e2f7961555.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXChpConfiguration instance that allows configuration of channel power (CHP) measurement. |
|  | Results | Gets the RFmxSpecAnMXChpResults instance that provides methods to retrieve channel power (CHP) measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXChp Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6dd0e439-3ce6-9d3c-48ea-f993acd2a82e.htm language=enus -->
## TOPIC 00268: rfmxspecandotnet/html/6dd0e439-3ce6-9d3c-48ea-f993acd2a82e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6dd0e439-3ce6-9d3c-48ea-f993acd2a82e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6dd0e439-3ce6-9d3c-48ea-f993acd2a82e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMemoryPolynomialOrder Method

RFmxSpecAnMXDpdConfigurationSetMemoryPolynomialOrder Method

SetModel(String, RFmxSpecAnMXDpdModel)

MemoryPolynomial

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMemoryPolynomialOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetMemoryPolynomialOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the order of the DPD polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6de636bd-9655-5cae-bb6c-3aa913dc0559.htm language=enus -->
## TOPIC 00269: rfmxspecandotnet/html/6de636bd-9655-5cae-bb6c-3aa913dc0559.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6de636bd-9655-5cae-bb6c-3aa913dc0559.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6de636bd-9655-5cae-bb6c-3aa913dc0559.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetRbwFilterBandwidth Method

RFmxSpecAnMXObwConfigurationSetRbwFilterBandwidth Method

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the bandwidth, in Hz, of the RBW filter used to sweep the acquired signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6e1848c0-ffe5-0e4d-1735-a1ea67380e76.htm language=enus -->
## TOPIC 00270: rfmxspecandotnet/html/6e1848c0-ffe5-0e4d-1735-a1ea67380e76.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6e1848c0-ffe5-0e4d-1735-a1ea67380e76.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6e1848c0-ffe5-0e4d-1735-a1ea67380e76.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObw Properties

RFmxSpecAnMXObw Properties

The [RFmxSpecAnMXObw](254e26ef-fa8f-01bc-4aa7-0307babd1ee4.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXObwConfiguration instance that allows configuration of OBW measurement. |
|  | Results | Gets the RFmxSpecAnMXObwResults instance that provides methods to retrieve OBW measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXObw Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6e2aa55c-b392-3d43-707a-d049af26bba0.htm language=enus -->
## TOPIC 00271: rfmxspecandotnet/html/6e2aa55c-b392-3d43-707a-d049af26bba0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6e2aa55c-b392-3d43-707a-d049af26bba0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6e2aa55c-b392-3d43-707a-d049af26bba0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetRbwFilterAutoBandwidth Method

RFmxSpecAnMXAcpConfigurationGetRbwFilterAutoBandwidth Method

Gets whether the measurement computes the resolution bandwidth (RBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterAutoBandwidth(
	string selectorString,
	out RFmxSpecAnMXAcpRbwAutoBandwidth value
)
```

```text
Public Function GetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpRbwAutoBandwidth**
  - Upon return, indicates whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetRBWFilterAutoBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6f70ec5b-facf-7ef7-c446-969b7d96112d.htm language=enus -->
## TOPIC 00272: rfmxspecandotnet/html/6f70ec5b-facf-7ef7-c446-969b7d96112d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6f70ec5b-facf-7ef7-c446-969b7d96112d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6f70ec5b-facf-7ef7-c446-969b7d96112d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetOffsetRrcFilterEnabled Method

RFmxSpecAnMXAcpConfigurationGetOffsetRrcFilterEnabled Method

Gets whether the root-raised-cosine (RRC) filter is applied on the acquired offset channel before measuring the offset channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRrcFilterEnabled(
	string selectorString,
	out RFmxSpecAnMXAcpOffsetRrcFilterEnabled value
)
```

```text
Public Function GetOffsetRrcFilterEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpOffsetRrcFilterEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXAcpOffsetRrcFilterEnabled**
  - Upon return, indicates whether the RRC filter is applied on the acquired offset channel before measuring the offset channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetRRCFilterEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6f91cce9-b366-abbf-14b0-3996d8acf40c.htm language=enus -->
## TOPIC 00273: rfmxspecandotnet/html/6f91cce9-b366-abbf-14b0-3996d8acf40c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6f91cce9-b366-abbf-14b0-3996d8acf40c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6f91cce9-b366-abbf-14b0-3996d8acf40c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarker Properties

RFmxSpecAnMXMarker Properties

The [RFmxSpecAnMXMarker](fae67d4d-bf0a-183a-05fe-17c8cdc7a97a.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXMarkerConfiguration instance that allows configuration of Marker measurement. |
|  | Results | Gets the RFmxSpecAnMXMarkerResults instance that provides methods to retrieve Marker measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXMarker Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6fa34682-2e35-794b-a8af-bbb1713af3b0.htm language=enus -->
## TOPIC 00274: rfmxspecandotnet/html/6fa34682-2e35-794b-a8af-bbb1713af3b0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6fa34682-2e35-794b-a8af-bbb1713af3b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6fa34682-2e35-794b-a8af-bbb1713af3b0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetOffsetFrequencyDefinition Method

RFmxSpecAnMXAcpConfigurationGetOffsetFrequencyDefinition Method

SetOffsetFrequency(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetFrequencyDefinition(
	string selectorString,
	out RFmxSpecAnMXAcpOffsetFrequencyDefinition value
)
```

```text
Public Function GetOffsetFrequencyDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpOffsetFrequencyDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXAcpOffsetFrequencyDefinition**
  - Upon return, contains the offset frequency definition used to specify the SetOffsetFrequency(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetFrequencyDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6faea33d-b476-ae60-a6e4-16a9ceadb886.htm language=enus -->
## TOPIC 00275: rfmxspecandotnet/html/6faea33d-b476-ae60-a6e4-16a9ceadb886.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6faea33d-b476-ae60-a6e4-16a9ceadb886.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6faea33d-b476-ae60-a6e4-16a9ceadb886.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpAveragingType Enumeration

RFmxSpecAnMXChpAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpAveragingType
```

```text
Public Enumeration RFmxSpecAnMXChpAveragingType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithm scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6fc0b834-bc0d-b017-86b6-bbb5a1979039.htm language=enus -->
## TOPIC 00276: rfmxspecandotnet/html/6fc0b834-bc0d-b017-86b6-bbb5a1979039.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6fc0b834-bc0d-b017-86b6-bbb5a1979039.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6fc0b834-bc0d-b017-86b6-bbb5a1979039.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpRbwFilterBandwidthDefinition Enumeration

RFmxSpecAnMXAcpRbwFilterBandwidthDefinition Enumeration

SetRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpRbwFilterBandwidthDefinition
```

```text
Public Enumeration RFmxSpecAnMXAcpRbwFilterBandwidthDefinition
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| BandwidthDefinition3dB | 0 | Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the SetRbwFilterType(String, RFmxSpecAnMXAcpRbwFilterType) method to FftBased, RBW is the 3 dB bandwidth of the window specified by the SetFftWindow(String, RFmxSpecAnMXAcpFftWindow) method. |
| BandwidthDefinitionBinWidth | 2 | Defines the RBW in terms of the bin width of the spectrum computed using an FFT when you set the SetRbwFilterType(String, RFmxSpecAnMXAcpRbwFilterType) method to FftBased. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6fe039d3-aaca-51fe-24c6-7054bf63f058.htm language=enus -->
## TOPIC 00277: rfmxspecandotnet/html/6fe039d3-aaca-51fe-24c6-7054bf63f058.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6fe039d3-aaca-51fe-24c6-7054bf63f058.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6fe039d3-aaca-51fe-24c6-7054bf63f058.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.ResetToDefault Method

RFmxSpecAnMXResetToDefault Method

Resets a signal to the default values.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

##### Remarks

This method maps to the RFmxSpecAn_ResetToDefault() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/70bc3602-9d55-7b75-3164-affd2b7fbdcc.htm language=enus -->
## TOPIC 00278: rfmxspecandotnet/html/70bc3602-9d55-7b75-3164-affd2b7fbdcc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/70bc3602-9d55-7b75-3164-affd2b7fbdcc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/70bc3602-9d55-7b75-3164-affd2b7fbdcc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumMeasurementMethod Enumeration

RFmxSpecAnMXSpectrumMeasurementMethod Enumeration

Specifies the method for performing the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumMeasurementMethod
```

```text
Public Enumeration RFmxSpecAnMXSpectrumMeasurementMethod
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The Spectrum measurement acquires the spectrum using the same signal analyzer setting across frequency bands. |
| SequentialFft | 2 | The Spectrum measurement acquires I/Q samples for a duration specified by the SpectrumSweepTimeInterval method. These samples are divided into smaller chunks. If the method SpectrumRbwFilterAutoBandwidth is True, The size of each chunk is defined by the SpectrumSequentialFftSize method. If the method Spectrum RBW Auto is False, the Spectrum Sequential FFT Size is auto computed based on the configured SpectrumRbwFilterBandwidth. The overlap between the chunks is defined by the SpectrumFftOverlapMode method. FFT is computed on each of these chunks. The resultant FFTs are averaged as per the configured averaging type in the method SpectrumFftOverlapTypeto get the spectrum. Sequential FFT method should be used for the following scenarios. While performing fast Spectrum measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following methods have limited support when you set the RFmxSpecAnMXSpectrumConfiguration.ConfigureMeasurementMethod method to SequentialFft.The RFmxSpecAnMXSpectrumConfiguration.SetVbwFilterAutoBandwidth method will only support True value. The RFmxSpecAnMXSpectrumConfiguration.SetRbwFilterType method will only support FftBased value. The RFmxSpecAnMXSpectrumConfiguration.SetSweepTimeAuto method will only support False value. The RFmxSpecAnMXSpectrumConfiguration.SetAveragingCount method will only support a value greater than or equal to 1. The RFmxSpecAnMXSpectrumConfiguration.SetNumberOfAnalysisThreads method will only support a value of 1. The RFmxSpecAnMXSpectrumConfiguration.SetAmplitudeCorrectionType Method will only support a value of RFCenterFrequency. The RFmxSpecAnMXSpectrumConfiguration.SetVbwFilterVbwToRbwRatio Method will only support a value greater than or equal to 3. Note For multi-span FFT, the averaging count should be 1. |
| Note |  |  |
| For multi-span FFT, the averaging count should be 1. |  |  |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/70ee5b3c-768f-f2ce-bf7d-2d592baeea5f.htm language=enus -->
## TOPIC 00279: rfmxspecandotnet/html/70ee5b3c-768f-f2ce-bf7d-2d592baeea5f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/70ee5b3c-768f-f2ce-bf7d-2d592baeea5f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/70ee5b3c-768f-f2ce-bf7d-2d592baeea5f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetTargetGainType Method

RFmxSpecAnMXDpdConfigurationSetTargetGainType Method

Sets the gain expected from the DUT after applying DPD on the input waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTargetGainType(
	string selectorString,
	RFmxSpecAnMXDpdTargetGainType value
)
```

```text
Public Function SetTargetGainType ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdTargetGainType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdTargetGainType**
  - Contains a value that indicates the gain expected from the DUT after applying DPD on the input waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetTargetGainType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/70f372d9-6d66-88df-57b6-474a4f98f2dd.htm language=enus -->
## TOPIC 00280: rfmxspecandotnet/html/70f372d9-6d66-88df-57b6-474a4f98f2dd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/70f372d9-6d66-88df-57b6-474a4f98f2dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/70f372d9-6d66-88df-57b6-474a4f98f2dd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.ConfigureBandwidthPercentage Method

RFmxSpecAnMXObwConfigurationConfigureBandwidthPercentage Method

Configures the percentage of the total power that is contained in the occupied bandwidth (OBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureBandwidthPercentage(
	string selectorString,
	double bandwidthPercentage
)
```

```text
Public Function ConfigureBandwidthPercentage ( 
	selectorString As String,
	bandwidthPercentage As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **bandwidthPercentage Double**
  - Specifies the percentage of the total power that is contained in the OBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWCfgBandwidthPercentage() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/710cc37f-ed3e-f4f2-16e2-19ec17923c6f.htm language=enus -->
## TOPIC 00281: rfmxspecandotnet/html/710cc37f-ed3e-f4f2-16e2-19ec17923c6f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/710cc37f-ed3e-f4f2-16e2-19ec17923c6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/710cc37f-ed3e-f4f2-16e2-19ec17923c6f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdEvmEnabled Enumeration

RFmxSpecAnMXIdpdEvmEnabled Enumeration

Specifies whether to enable EVM computation.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIdpdEvmEnabled
```

```text
Public Enumeration RFmxSpecAnMXIdpdEvmEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables EVM computation. NaN is returned for Mean RMS EVM. |
| True | 1 | Enables EVM computation. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/71a6cb75-8429-6aed-4c26-a1c0cc7b303f.htm language=enus -->
## TOPIC 00282: rfmxspecandotnet/html/71a6cb75-8429-6aed-4c26-a1c0cc7b303f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/71a6cb75-8429-6aed-4c26-a1c0cc7b303f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/71a6cb75-8429-6aed-4c26-a1c0cc7b303f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetIQPowerEdgeTriggerSource Method

RFmxSpecAnMXGetIQPowerEdgeTriggerSource Method

Gets the channel from which the device monitors the trigger.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the channel from which the device monitors the trigger.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_GetIQPowerEdgeTriggerSource() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/727cab1b-c044-32b1-26a9-97d952742352.htm language=enus -->
## TOPIC 00283: rfmxspecandotnet/html/727cab1b-c044-32b1-26a9-97d952742352.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/727cab1b-c044-32b1-26a9-97d952742352.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/727cab1b-c044-32b1-26a9-97d952742352.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpVbwFilterAutoBandwidth Enumeration

RFmxSpecAnMXTxpVbwFilterAutoBandwidth Enumeration

Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXTxpVbwFilterAutoBandwidth
```

```text
Public Enumeration RFmxSpecAnMXTxpVbwFilterAutoBandwidth
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Specify the video bandwidth in the TXP VBW method. The SetVbwFilterVbwToRbwRatio(String, Double) method is disregarded in this mode. |
| True | 1 | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the SetVbwFilterVbwToRbwRatio(String, Double) method and the TXP RBW method. The value of the TXP VBW method is disregarded in this mode. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7287fa0c-e193-721d-a84f-6266d059f1e8.htm language=enus -->
## TOPIC 00284: rfmxspecandotnet/html/7287fa0c-e193-721d-a84f-6266d059f1e8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7287fa0c-e193-721d-a84f-6266d059f1e8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7287fa0c-e193-721d-a84f-6266d059f1e8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetCarrierFrequency Method

RFmxSpecAnMXAcpConfigurationGetCarrierFrequency Method

Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the center frequency, in Hz, of the carrier, relative to the RF center frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetCarrierFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/72f91b4b-2f38-262d-bac3-6c014448a012.htm language=enus -->
## TOPIC 00285: rfmxspecandotnet/html/72f91b4b-2f38-262d-bac3-6c014448a012.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/72f91b4b-2f38-262d-bac3-6c014448a012.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/72f91b4b-2f38-262d-bac3-6c014448a012.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.GetPowerLinearityTradeoff Method

RFmxSpecAnMXIdpdConfigurationGetPowerLinearityTradeoff Method

Gets the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPowerLinearityTradeoff(
	string selectorString,
	out double value
)
```

```text
Public Function GetPowerLinearityTradeoff ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

IdpdPowerLinearityTradeoff

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/737d697a-5562-cedb-941e-99a786bfd28d.htm language=enus -->
## TOPIC 00286: rfmxspecandotnet/html/737d697a-5562-cedb-941e-99a786bfd28d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/737d697a-5562-cedb-941e-99a786bfd28d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/737d697a-5562-cedb-941e-99a786bfd28d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetUpperOffsetTotalAbsolutePower Method

RFmxSpecAnMXSemResultsGetUpperOffsetTotalAbsolutePower Method

Gets the upper (positive) offset segment power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetTotalAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetTotalAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the upper (positive) offset segment power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsUpperOffsetTotalAbsolutePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/739738fd-a6c2-4919-8117-d0b9eb1039d9.htm language=enus -->
## TOPIC 00287: rfmxspecandotnet/html/739738fd-a6c2-4919-8117-d0b9eb1039d9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/739738fd-a6c2-4919-8117-d0b9eb1039d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/739738fd-a6c2-4919-8117-d0b9eb1039d9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.ConfigureMemoryModelCorrectionType Method

RFmxSpecAnMXDpdApplyDpdConfigureMemoryModelCorrectionType Method

SetModel(String, RFmxSpecAnMXDpdModel)

MemoryPolynomial

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMemoryModelCorrectionType(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType memoryModelCorrectionType
)
```

```text
Public Function ConfigureMemoryModelCorrectionType ( 
	selectorString As String,
	memoryModelCorrectionType As RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **memoryModelCorrectionType RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType**
  - Specifies the predistortion type when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to GeneralizedMemoryPolynomial or MemoryPolynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgApplyDPDMemoryModelCorrectionType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/747df10c-482a-ae32-aa65-f21869a8cbb6.htm language=enus -->
## TOPIC 00288: rfmxspecandotnet/html/747df10c-482a-ae32-aa65-f21869a8cbb6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/747df10c-482a-ae32-aa65-f21869a8cbb6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/747df10c-482a-ae32-aa65-f21869a8cbb6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetFftOverlapMode Method

RFmxSpecAnMXSpectrumConfigurationSetFftOverlapMode Method

SpectrumMeasurementMethod

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftOverlapMode(
	string selectorString,
	RFmxSpecAnMXSpectrumFftOverlapMode value
)
```

```text
Public Function SetFftOverlapMode ( 
	selectorString As String,
	value As RFmxSpecAnMXSpectrumFftOverlapMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumFftOverlapMode**
  - Specifies the overlap mode when you set the SpectrumMeasurementMethod method to SequentialFft.

###### Return Value

Int32

##### Remarks

SpectrumFftOverlapMode

Disabled

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/755f9578-00de-c471-6420-8a820c808e1c.htm language=enus -->
## TOPIC 00289: rfmxspecandotnet/html/755f9578-00de-c471-6420-8a820c808e1c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/755f9578-00de-c471-6420-8a820c808e1c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/755f9578-00de-c471-6420-8a820c808e1c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetOffsetPowerReferenceSpecific Method

RFmxSpecAnMXAcpConfigurationGetOffsetPowerReferenceSpecific Method

Gets the carrier index, for which the measured power is the power reference for the offset channel relative power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the index of the carrier to be used as the reference carrier.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetPowerReferenceSpecific() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7967cb85-0cbf-8786-58f6-24cf25360f73.htm language=enus -->
## TOPIC 00290: rfmxspecandotnet/html/7967cb85-0cbf-8786-58f6-24cf25360f73.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7967cb85-0cbf-8786-58f6-24cf25360f73.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7967cb85-0cbf-8786-58f6-24cf25360f73.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetIntermodOrder Method

RFmxSpecAnMXIMConfigurationSetIntermodOrder Method

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIntermodOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetIntermodOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Int32**
  - Specifies the order of the intermod. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMIntermodOrder

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/797bc9f1-b709-59da-9aa6-83844eff97ef.htm language=enus -->
## TOPIC 00291: rfmxspecandotnet/html/797bc9f1-b709-59da-9aa6-83844eff97ef.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/797bc9f1-b709-59da-9aa6-83844eff97ef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/797bc9f1-b709-59da-9aa6-83844eff97ef.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerConfiguration.ConfigurePeakExcursion Method

RFmxSpecAnMXMarkerConfigurationConfigurePeakExcursion Method

Configures the peak excursion.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigurePeakExcursion(
	string selectorString,
	RFmxSpecAnMXMarkerPeakExcursionEnabled peakExcursionEnabled,
	double peakExcursion
)
```

```text
Public Function ConfigurePeakExcursion ( 
	selectorString As String,
	peakExcursionEnabled As RFmxSpecAnMXMarkerPeakExcursionEnabled,
	peakExcursion As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **peakExcursionEnabled RFmxSpecAnMXMarkerPeakExcursionEnabled**
  - Specifies whether to enable the peak excursion check for the trace while finding the peaks.
- **peakExcursion Double**
  - Specifies the peak excursion value for finding the peaks on trace when you set the peakExcursionEnabled parameter to True. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered a peak.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_MarkerCfgPeakExcursion() function in C.

##### See Also

###### Reference

RFmxSpecAnMXMarkerConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/79cccb0d-f93e-eb14-3808-8046c9371ae0.htm language=enus -->
## TOPIC 00292: rfmxspecandotnet/html/79cccb0d-f93e-eb14-3808-8046c9371ae0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/79cccb0d-f93e-eb14-3808-8046c9371ae0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/79cccb0d-f93e-eb14-3808-8046c9371ae0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureOffsetRelativeLimitArray Method

RFmxSpecAnMXSemConfigurationConfigureOffsetRelativeLimitArray Method

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetRelativeLimitArray(
	string selectorString,
	RFmxSpecAnMXSemOffsetRelativeLimitMode[] relativeLimitMode,
	double[] relativeLimitStart,
	double[] relativeLimitStop
)
```

```text
Public Function ConfigureOffsetRelativeLimitArray ( 
	selectorString As String,
	relativeLimitMode As RFmxSpecAnMXSemOffsetRelativeLimitMode(),
	relativeLimitStart As Double(),
	relativeLimitStop As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **relativeLimitMode RFmxSpecAnMXSemOffsetRelativeLimitMode**
  - Specifies whether the relative limit mask is a flat line or a line with a slope.
- **relativeLimitStart Double**
  - Specifies the array of relative power limits, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the SetOffsetRelativeLimitMode(String, RFmxSpecAnMXSemOffsetRelativeLimitMode) to Couple.
- **relativeLimitStop Double**
  - Specifies the array of relative power limits, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the SetOffsetRelativeLimitMode(String, RFmxSpecAnMXSemOffsetRelativeLimitMode) to Couple.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetRelativeLimitArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/79d0b18d-e042-ca66-1c43-ef79ec0b3725.htm language=enus -->
## TOPIC 00293: rfmxspecandotnet/html/79d0b18d-e042-ca66-1c43-ef79ec0b3725.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/79d0b18d-e042-ca66-1c43-ef79ec0b3725.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/79d0b18d-e042-ca66-1c43-ef79ec0b3725.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetCompressionPointEnabled Method

RFmxSpecAnMXAmpmConfigurationSetCompressionPointEnabled Method

Sets the computation of compression points corresponding to the compression levels specified by RFmxSpecAnMXAmpmCompressionPointEnabled method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCompressionPointEnabled(
	string selectorString,
	RFmxSpecAnMXAmpmCompressionPointEnabled value
)
```

```text
Public Function SetCompressionPointEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmCompressionPointEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmCompressionPointEnabled**
  - Contains a value of computation of compression points corresponding to the compression levels specified by RFmxSpecAnMXAmpmCompressionPointEnabled method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/79d2c6a2-5fe2-6751-c49d-1db6a0d696eb.htm language=enus -->
## TOPIC 00294: rfmxspecandotnet/html/79d2c6a2-5fe2-6751-c49d-1db6a0d696eb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/79d2c6a2-5fe2-6751-c49d-1db6a0d696eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/79d2c6a2-5fe2-6751-c49d-1db6a0d696eb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetSpan Method

RFmxSpecAnMXSpectrumConfigurationGetSpan Method

Gets the frequency range, in hertz (Hz), around the center frequency to be acquired for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpan(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpan ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the frequency range, in hertz (Hz), around the center frequency to be acquired for the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumGetSpan() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7a0cf6b1-e5cc-eedd-050d-42976498e2e6.htm language=enus -->
## TOPIC 00295: rfmxspecandotnet/html/7a0cf6b1-e5cc-eedd-050d-42976498e2e6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7a0cf6b1-e5cc-eedd-050d-42976498e2e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7a0cf6b1-e5cc-eedd-050d-42976498e2e6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMemoryPolynomialMemoryDepth Method

RFmxSpecAnMXDpdConfigurationSetMemoryPolynomialMemoryDepth Method

SetModel(String, RFmxSpecAnMXDpdModel)

MemoryPolynomial

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMemoryPolynomialMemoryDepth(
	string selectorString,
	int value
)
```

```text
Public Function SetMemoryPolynomialMemoryDepth ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Contains the memory depth of the DPD polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialMemoryDepth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7a544c3b-b040-c70e-93c6-da23885be031.htm language=enus -->
## TOPIC 00296: rfmxspecandotnet/html/7a544c3b-b040-c70e-93c6-da23885be031.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7a544c3b-b040-c70e-93c6-da23885be031.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7a544c3b-b040-c70e-93c6-da23885be031.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.BuildListString Method

RFmxSpecAnMXBuildListString Method

Creates the list string.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **listName String**
  - Specifies the list name for building the selector string. This input accepts the list name with or without the "list::" prefix.
- **resultName String**
  - Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1"

###### Return Value

String

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7a8fcc29-185e-8993-9e10-2773c4c32884.htm language=enus -->
## TOPIC 00297: rfmxspecandotnet/html/7a8fcc29-185e-8993-9e10-2773c4c32884.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7a8fcc29-185e-8993-9e10-2773c4c32884.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7a8fcc29-185e-8993-9e10-2773c4c32884.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdAutoCarrierDetectionEnabled Enumeration

RFmxSpecAnMXDpdAutoCarrierDetectionEnabled Enumeration

Specifies if auto detection of carrier offset and carrier bandwidth is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdAutoCarrierDetectionEnabled
```

```text
Public Enumeration RFmxSpecAnMXDpdAutoCarrierDetectionEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables auto detection for carrier offset and carrier bandwidth. |
| True | 1 | Enables auto detection for carrier offset and carrier bandwidth. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7aa5c5b5-2b72-b221-ed8c-bbfef0d8967a.htm language=enus -->
## TOPIC 00298: rfmxspecandotnet/html/7aa5c5b5-2b72-b221-ed8c-bbfef0d8967a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7aa5c5b5-2b72-b221-ed8c-bbfef0d8967a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7aa5c5b5-2b72-b221-ed8c-bbfef0d8967a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.ConfigureOffsetArray Method

RFmxSpecAnMXAcpConfigurationConfigureOffsetArray Method

Configures an offset channel on one or both sides of carrier with center-to-center spacing as specified by the offset frequency and offset frequency definition. In case of multiple carriers, offset frequency is relative to the closest carrier.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetArray(
	string selectorString,
	double[] offsetFrequency,
	RFmxSpecAnMXAcpOffsetSideband[] offsetSideband,
	RFmxSpecAnMXAcpOffsetEnabled[] offsetEnabled
)
```

```text
Public Function ConfigureOffsetArray ( 
	selectorString As String,
	offsetFrequency As Double(),
	offsetSideband As RFmxSpecAnMXAcpOffsetSideband(),
	offsetEnabled As RFmxSpecAnMXAcpOffsetEnabled()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetFrequency Double**
  - Specifies an array of center or edge frequencies, in hertz (Hz), of the offset channel, relative to the center frequency of the closest carrier as determined by the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXAcpOffsetFrequencyDefinition) method. The sign of offset frequency is ignored and the offsetSideband parameter determines whether the upper, lower, or both offsets are measured.
- **offsetSideband RFmxSpecAnMXAcpOffsetSideband**
  - Specifies whether the offset segment is present on one side, or on both sides of the carriers.
- **offsetEnabled RFmxSpecAnMXAcpOffsetEnabled**
  - Specifies whether to enable the offset channel for ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPCfgOffsetArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7ac00003-eaa3-0c78-2991-dc5d3a354834.htm language=enus -->
## TOPIC 00299: rfmxspecandotnet/html/7ac00003-eaa3-0c78-2991-dc5d3a354834.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7ac00003-eaa3-0c78-2991-dc5d3a354834.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7ac00003-eaa3-0c78-2991-dc5d3a354834.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetRelativeAttenuation Method

RFmxSpecAnMXSemConfigurationGetOffsetRelativeAttenuation Method

SetExternalAttenuation(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRelativeAttenuation(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetRelativeAttenuation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the attenuation, in dB, relative to the SetExternalAttenuation(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetRelativeAttenuation() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7ad268b6-897c-5028-ac23-59ebaaed6501.htm language=enus -->
## TOPIC 00300: rfmxspecandotnet/html/7ad268b6-897c-5028-ac23-59ebaaed6501.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7ad268b6-897c-5028-ac23-59ebaaed6501.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7ad268b6-897c-5028-ac23-59ebaaed6501.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetMeasurementEnabled Method

RFmxSpecAnMXChpConfigurationSetMeasurementEnabled Method

Sets whether to enable the channel power (CHP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - to enable the traces to enable the CHP measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7ad4fbeb-07b9-2cce-c0ac-466b0fc7706e.htm language=enus -->
## TOPIC 00301: rfmxspecandotnet/html/7ad4fbeb-07b9-2cce-c0ac-466b0fc7706e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7ad4fbeb-07b9-2cce-c0ac-466b0fc7706e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7ad4fbeb-07b9-2cce-c0ac-466b0fc7706e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFAveragingEnabled Enumeration

RFmxSpecAnMXNFAveragingEnabled Enumeration

Specifies whether to enable averaging for the noise figure (NF) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFAveragingEnabled
```

```text
Public Enumeration RFmxSpecAnMXNFAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The NF measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions for each frequency which you specify in the SetFrequencyList(String, Double) method, over which the NF measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7ae3807b-60dc-0b75-c593-1a4ebb48a776.htm language=enus -->
## TOPIC 00302: rfmxspecandotnet/html/7ae3807b-60dc-0b75-c593-1a4ebb48a776.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7ae3807b-60dc-0b75-c593-1a4ebb48a776.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7ae3807b-60dc-0b75-c593-1a4ebb48a776.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMResults.GetWorstCaseIntermodAbsolutePower Method

RFmxSpecAnMXIMResultsGetWorstCaseIntermodAbsolutePower Method

Gets the worst case intermod power that is equal to the maximum of the values of both the IM Results Upper Intermod Power and IM Results Lower Intermod Power results. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetWorstCaseIntermodAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetWorstCaseIntermodAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and ImIntermod number. Example: "ImIntermod0", "result::r1/ImIntermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the worst case intermod power that is equal to the maximum of the values of both the IM Results Upper Intermod Power and IM Results Lower Intermod Power results. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

IMResultsWorstCaseIntermodAbsolutePower

##### See Also

###### Reference

RFmxSpecAnMXIMResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7b0635cc-0893-dd92-5bd7-07a799519fd0.htm language=enus -->
## TOPIC 00303: rfmxspecandotnet/html/7b0635cc-0893-dd92-5bd7-07a799519fd0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7b0635cc-0893-dd92-5bd7-07a799519fd0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7b0635cc-0893-dd92-5bd7-07a799519fd0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetReferenceLevelHeadroom Method

RFmxSpecAnMXGetReferenceLevelHeadroom Method

Default values

Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

###### Return Value

Int32

##### Remarks

ReferenceLevelHeadroom

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7b099f3e-59f9-23e4-d291-41882bb14009.htm language=enus -->
## TOPIC 00304: rfmxspecandotnet/html/7b099f3e-59f9-23e4-d291-41882bb14009.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7b099f3e-59f9-23e4-d291-41882bb14009.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7b099f3e-59f9-23e4-d291-41882bb14009.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtMeasurementLocationType Enumeration

RFmxSpecAnMXPavtMeasurementLocationType Enumeration

Specifies the location at which the segment is measured.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXPavtMeasurementLocationType
```

```text
Public Enumeration RFmxSpecAnMXPavtMeasurementLocationType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Time | 0 | The measurement is performed over a single record across multiple segments separated in time. The measurment locations of the segments are specified by the SetSegmentStartTime(String, Double) method. The number of segments is equal to the number of measurement start times. |
| Trigger | 1 | The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7b0cf047-6b2a-6cc9-54d1-d0f4e4743a58.htm language=enus -->
## TOPIC 00305: rfmxspecandotnet/html/7b0cf047-6b2a-6cc9-54d1-d0f4e4743a58.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7b0cf047-6b2a-6cc9-54d1-d0f4e4743a58.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7b0cf047-6b2a-6cc9-54d1-d0f4e4743a58.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.ConfigureSoftwareEdgeTrigger Method

RFmxSpecAnMXConfigureSoftwareEdgeTrigger Method

Configures the device to wait for a Software Trigger and then marks a reference point within the record.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **triggerDelay Double**
  - Specifies the trigger delay time, in seconds.
- **enableTrigger Boolean**
  - Specifies whether to enable the trigger.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CfgSoftwareEdgeTrigger() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7b12b675-66f7-8ce2-28fd-ef5950011baf.htm language=enus -->
## TOPIC 00306: rfmxspecandotnet/html/7b12b675-66f7-8ce2-28fd-ef5950011baf.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7b12b675-66f7-8ce2-28fd-ef5950011baf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7b12b675-66f7-8ce2-28fd-ef5950011baf.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetRelativeAttenuation Method

RFmxSpecAnMXSemConfigurationSetOffsetRelativeAttenuation Method

SetExternalAttenuation(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetRelativeAttenuation(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetRelativeAttenuation ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the attenuation, in dB, relative to the SetExternalAttenuation(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetRelativeAttenuation() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/7cae8d4b-fce0-9357-f7c3-4a3e750fac3e.htm language=enus -->
## TOPIC 00307: rfmxspecandotnet/html/7cae8d4b-fce0-9357-f7c3-4a3e750fac3e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/7cae8d4b-fce0-9357-f7c3-4a3e750fac3e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/7cae8d4b-fce0-9357-f7c3-4a3e750fac3e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpCarrierRrcFilterEnabled Enumeration

RFmxSpecAnMXChpCarrierRrcFilterEnabled Enumeration

Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpCarrierRrcFilterEnabled
```

```text
Public Enumeration RFmxSpecAnMXChpCarrierRrcFilterEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The channel power of the acquired channel is measured directly. |
| True | 1 | The measurement applies the RRC filter on the acquired channel before measuring the channel power. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/83b8716a-bc0d-ae21-f1bf-f7e7edb79389.htm language=enus -->
## TOPIC 00308: rfmxspecandotnet/html/83b8716a-bc0d-ae21-f1bf-f7e7edb79389.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/83b8716a-bc0d-ae21-f1bf-f7e7edb79389.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/83b8716a-bc0d-ae21-f1bf-f7e7edb79389.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFCalibrationLossCompensationEnabled Enumeration

RFmxSpecAnMXNFCalibrationLossCompensationEnabled Enumeration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFCalibrationLossCompensationEnabled
```

```text
Public Enumeration RFmxSpecAnMXNFCalibrationLossCompensationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The NF measurement ignores the ohmic losses. |
| True | 1 | The NF measurement accounts for the ohmic losses. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/83f79e4d-de1a-6720-d349-37e6fa6d6a2f.htm language=enus -->
## TOPIC 00309: rfmxspecandotnet/html/83f79e4d-de1a-6720-d349-37e6fa6d6a2f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/83f79e4d-de1a-6720-d349-37e6fa6d6a2f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/83f79e4d-de1a-6720-d349-37e6fa6d6a2f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetMeasurementMethod Method

RFmxSpecAnMXSpectrumConfigurationGetMeasurementMethod Method

Gets the method for performing the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementMethod(
	string selectorString,
	out RFmxSpecAnMXSpectrumMeasurementMethod value
)
```

```text
Public Function GetMeasurementMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumMeasurementMethod**
  - Upon return, contains the method for performing the Spectrum measurement.

###### Return Value

Int32

##### Remarks

SpectrumMeasurementMethod

Normal

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/84213bcf-1874-5100-1d1e-139a3d2f9c79.htm language=enus -->
## TOPIC 00310: rfmxspecandotnet/html/84213bcf-1874-5100-1d1e-139a3d2f9c79.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/84213bcf-1874-5100-1d1e-139a3d2f9c79.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/84213bcf-1874-5100-1d1e-139a3d2f9c79.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdSignalType Enumeration

RFmxSpecAnMXIdpdSignalType Enumeration

Specifies the type of reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIdpdSignalType
```

```text
Public Enumeration RFmxSpecAnMXIdpdSignalType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Modulated | 0 | Specifies the reference waveform is a banded signal like cellular or connectivity standard signals. |
| Tones | 1 | Specifies the reference waveform is a continuous signal comprising of one or more tones. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/845294bb-8407-9c33-7d69-3c29c3d3476e.htm language=enus -->
## TOPIC 00311: rfmxspecandotnet/html/845294bb-8407-9c33-7d69-3c29c3d3476e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/845294bb-8407-9c33-7d69-3c29c3d3476e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/845294bb-8407-9c33-7d69-3c29c3d3476e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureCarrierEnabled Method

RFmxSpecAnMXSemConfigurationConfigureCarrierEnabled Method

Configures whether to consider the carrier power as part of total carrier power measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierEnabled(
	string selectorString,
	RFmxSpecAnMXSemCarrierEnabled carrierEnabled
)
```

```text
Public Function ConfigureCarrierEnabled ( 
	selectorString As String,
	carrierEnabled As RFmxSpecAnMXSemCarrierEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **carrierEnabled RFmxSpecAnMXSemCarrierEnabled**
  - Specifies whether to consider the carrier power as part of total carrier power measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/84a6164f-be8c-09c9-6293-05ca041ddc69.htm language=enus -->
## TOPIC 00312: rfmxspecandotnet/html/84a6164f-be8c-09c9-6293-05ca041ddc69.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/84a6164f-be8c-09c9-6293-05ca041ddc69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/84a6164f-be8c-09c9-6293-05ca041ddc69.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetIntermodSide Method

RFmxSpecAnMXIMConfigurationSetIntermodSide Method

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIntermodSide(
	string selectorString,
	RFmxSpecAnMXIMIntermodSide value
)
```

```text
Public Function SetIntermodSide ( 
	selectorString As String,
	value As RFmxSpecAnMXIMIntermodSide
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXIMIntermodSide**
  - Specifies whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMIntermodSide

Both

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8552d010-e26c-a696-107c-75ddb57d4173.htm language=enus -->
## TOPIC 00313: rfmxspecandotnet/html/8552d010-e26c-a696-107c-75ddb57d4173.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8552d010-e26c-a696-107c-75ddb57d4173.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8552d010-e26c-a696-107c-75ddb57d4173.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfResults.GetTenPercentPower Method

RFmxSpecAnMXCcdfResultsGetTenPercentPower Method

Gets the power, in dB, above the mean power, over which 10% of the total samples in the signal are present.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTenPercentPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetTenPercentPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the power, in dB, above the mean power, over which 10% of the total samples in the signal are present.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFGetResultsTenPercentPower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/855d29a2-d4e5-c80b-6501-a772ac334def.htm language=enus -->
## TOPIC 00314: rfmxspecandotnet/html/855d29a2-d4e5-c80b-6501-a772ac334def.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/855d29a2-d4e5-c80b-6501-a772ac334def.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/855d29a2-d4e5-c80b-6501-a772ac334def.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetOffsetFrequency Method

RFmxSpecAnMXAcpConfigurationGetOffsetFrequency Method

SetOffsetFrequencyDefinition(String, RFmxSpecAnMXAcpOffsetFrequencyDefinition)

SetOffsetSideband(String, RFmxSpecAnMXAcpOffsetSideband)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the center or edge frequency, in hertz (Hz), of the offset channel, relative to the center frequency of the closest carrier as determined by the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXAcpOffsetFrequencyDefinition) method. The sign of offset frequency is ignored and the SetOffsetSideband(String, RFmxSpecAnMXAcpOffsetSideband) method determines whether the upper, lower, or both offsets are measured.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/857e870e-da0a-a1fe-c586-cbc9730c928a.htm language=enus -->
## TOPIC 00315: rfmxspecandotnet/html/857e870e-da0a-a1fe-c586-cbc9730c928a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/857e870e-da0a-a1fe-c586-cbc9730c928a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/857e870e-da0a-a1fe-c586-cbc9730c928a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.GetListStepRange Method

RFmxSpecAnMXListGetListStepRange Method

Returns range of list step instances in a list.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMX GetListStepRange(
	int stepStartIndex,
	int stepStopIndex
)
```

```text
Public Function GetListStepRange ( 
	stepStartIndex As Integer,
	stepStopIndex As Integer
) As RFmxSpecAnMX
```

###### Parameters

- **stepStartIndex Int32**
  - Pass the starting index of the range of list step.
- **stepStopIndex Int32**
  - Pass the last index of the range of list step.

###### Return Value

RFmxSpecAnMX

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/858f86c7-68df-842f-bd7e-c8eefdcf0054.htm language=enus -->
## TOPIC 00316: rfmxspecandotnet/html/858f86c7-68df-842f-bd7e-c8eefdcf0054.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/858f86c7-68df-842f-bd7e-c8eefdcf0054.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/858f86c7-68df-842f-bd7e-c8eefdcf0054.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetNoiseCompensationType Method

RFmxSpecAnMXChpConfigurationSetNoiseCompensationType Method

Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCompensationType(
	string selectorString,
	RFmxSpecAnMXChpNoiseCompensationType value
)
```

```text
Public Function SetNoiseCompensationType ( 
	selectorString As String,
	value As RFmxSpecAnMXChpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpNoiseCompensationType**
  - Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

ChpNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/858ffe3c-8469-91b5-0f70-fc05168763a0.htm language=enus -->
## TOPIC 00317: rfmxspecandotnet/html/858ffe3c-8469-91b5-0f70-fc05168763a0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/858ffe3c-8469-91b5-0f70-fc05168763a0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/858ffe3c-8469-91b5-0f70-fc05168763a0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdf Properties

RFmxSpecAnMXCcdf Properties

The [RFmxSpecAnMXCcdf](c9209057-a936-baad-dae3-cd405e038e71.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXCcdfConfiguration instance that allows configuration of CCDF measurement. |
|  | Results | Gets the RFmxSpecAnMXCcdfResults instance that provides methods to retrieve CCDF measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXCcdf Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/85f6c66a-1864-ccee-31c9-10c42ac05d8e.htm language=enus -->
## TOPIC 00318: rfmxspecandotnet/html/85f6c66a-1864-ccee-31c9-10c42ac05d8e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/85f6c66a-1864-ccee-31c9-10c42ac05d8e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/85f6c66a-1864-ccee-31c9-10c42ac05d8e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetAttributeString Method

RFmxSpecAnMXGetAttributeString Method

Gets the value of a of an RFmx string.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value String**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_GetAttributeString() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/86112e85-41d7-f823-8e25-0eb78b1dc3f1.htm language=enus -->
## TOPIC 00319: rfmxspecandotnet/html/86112e85-41d7-f823-8e25-0eb78b1dc3f1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/86112e85-41d7-f823-8e25-0eb78b1dc3f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/86112e85-41d7-f823-8e25-0eb78b1dc3f1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetColdSourceMode Method

RFmxSpecAnMXNFConfigurationGetColdSourceMode Method

Gets whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetColdSourceMode(
	string selectorString,
	out RFmxSpecAnMXNFColdSourceMode value
)
```

```text
Public Function GetColdSourceMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXNFColdSourceMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFColdSourceMode**
  - Upon return, contains whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

###### Return Value

Int32

##### Remarks

NFColdSourceMode

Measure

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8618fee9-7b8f-1d44-a08a-f89497b32955.htm language=enus -->
## TOPIC 00320: rfmxspecandotnet/html/8618fee9-7b8f-1d44-a08a-f89497b32955.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8618fee9-7b8f-1d44-a08a-f89497b32955.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8618fee9-7b8f-1d44-a08a-f89497b32955.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerConfiguration.ConfigureYLocation Method

RFmxSpecAnMXMarkerConfigurationConfigureYLocation Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureYLocation(
	string selectorString,
	double markerYLocation
)
```

```text
Public Function ConfigureYLocation ( 
	selectorString As String,
	markerYLocation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of marker number. Example:"marker0" You can use the RFmxSpecAn_BuildMarkerString2 method to build the selector string.
- **markerYLocation Double**
  - Specifies the Y location of the marker when you set the Marker Type parameter to fixed.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXMarkerConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/86200341-d497-4ffb-c2eb-5dd88b5649ef.htm language=enus -->
## TOPIC 00321: rfmxspecandotnet/html/86200341-d497-4ffb-c2eb-5dd88b5649ef.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/86200341-d497-4ffb-c2eb-5dd88b5649ef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/86200341-d497-4ffb-c2eb-5dd88b5649ef.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.ConfigureFft Method

RFmxSpecAnMXSpectrumConfigurationConfigureFft Method

Configures window and FFT to obtain a spectrum for the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFft(
	string selectorString,
	RFmxSpecAnMXSpectrumFftWindow fftWindow,
	double fftPadding
)
```

```text
Public Function ConfigureFft ( 
	selectorString As String,
	fftWindow As RFmxSpecAnMXSpectrumFftWindow,
	fftPadding As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **fftWindow RFmxSpecAnMXSpectrumFftWindow**
  - Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types.
- **fftPadding Double**
  - Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth of the device.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumCfgFFT() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/86330072-4418-89bd-fb33-88df7473df23.htm language=enus -->
## TOPIC 00322: rfmxspecandotnet/html/86330072-4418-89bd-fb33-88df7473df23.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/86330072-4418-89bd-fb33-88df7473df23.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/86330072-4418-89bd-fb33-88df7473df23.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetCancellationEnabled Method

RFmxSpecAnMXPhaseNoiseConfigurationGetCancellationEnabled Method

Gets whether to enable or disable the phase noise cancellation. Refer to the Phase Noise topic for more information on phase noise cancellation.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCancellationEnabled(
	string selectorString,
	out RFmxSpecAnMXPhaseNoiseCancellationEnabled value
)
```

```text
Public Function GetCancellationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXPhaseNoiseCancellationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPhaseNoiseCancellationEnabled**
  - Upon return, contains whether to enable or disable the phase noise cancellation. Refer to the Phase Noise topic for more information on phase noise cancellation.

###### Return Value

Int32

##### Remarks

PhaseNoiseCancellationEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8634fd4b-ea02-2f93-8fa0-9a8268fa5c2a.htm language=enus -->
## TOPIC 00323: rfmxspecandotnet/html/8634fd4b-ea02-2f93-8fa0-9a8268fa5c2a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8634fd4b-ea02-2f93-8fa0-9a8268fa5c2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8634fd4b-ea02-2f93-8fa0-9a8268fa5c2a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.GetMeasurementInterval Method

RFmxSpecAnMXFcntConfigurationGetMeasurementInterval Method

Gets the acquisition time, in seconds, for the frequency count (Fcnt) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the acquisition time, in seconds, for the Fcnt measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8643e06d-7e24-6bd1-5108-e605d0c8b224.htm language=enus -->
## TOPIC 00324: rfmxspecandotnet/html/8643e06d-7e24-6bd1-5108-e605d0c8b224.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8643e06d-7e24-6bd1-5108-e605d0c8b224.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8643e06d-7e24-6bd1-5108-e605d0c8b224.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangePeakThreshold Method

RFmxSpecAnMXSpurConfigurationSetRangePeakThreshold Method

SetRangeStartFrequency(String, Double)

SetRangeStopFrequency(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangePeakThreshold(
	string selectorString,
	double value
)
```

```text
Public Function SetRangePeakThreshold ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the threshold level, in dBm, above which the measurement detects spurs in the range that you specify using the SetRangeStartFrequency(String, Double) and SetRangeStopFrequency(String, Double) methods.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangePeakThreshold() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/865fc738-6d36-3b9c-e12f-53bfacdf7315.htm language=enus -->
## TOPIC 00325: rfmxspecandotnet/html/865fc738-6d36-3b9c-e12f-53bfacdf7315.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/865fc738-6d36-3b9c-e12f-53bfacdf7315.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/865fc738-6d36-3b9c-e12f-53bfacdf7315.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.ConfigureRangeAbsoluteLimitArray Method

RFmxSpecAnMXSpurConfigurationConfigureRangeAbsoluteLimitArray Method

Configures the absolute power limits corresponding to the beginning and end of the frequency range and specifies whether the absolute limit threshold is a flat line or a line with a slope.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRangeAbsoluteLimitArray(
	string selectorString,
	RFmxSpecAnMXSpurAbsoluteLimitMode[] absoluteLimitMode,
	double[] absoluteLimitStart,
	double[] absoluteLimitStop
)
```

```text
Public Function ConfigureRangeAbsoluteLimitArray ( 
	selectorString As String,
	absoluteLimitMode As RFmxSpecAnMXSpurAbsoluteLimitMode(),
	absoluteLimitStart As Double(),
	absoluteLimitStop As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **absoluteLimitMode RFmxSpecAnMXSpurAbsoluteLimitMode**
  - Specifies whether the absolute limit threshold is a flat line or a line with a slope.
- **absoluteLimitStart Double**
  - Specifies the array of absolute power limits, in dBm, corresponding to the beginning of the frequency range. The value of this parameter is also set as the absolute power limit for the range when you set the SetRangeAbsoluteLimitMode(String, RFmxSpecAnMXSpurAbsoluteLimitMode) method to Couple.
- **absoluteLimitStop Double**
  - Specifies the array of absolute power limits, in dBm, corresponding to the end of the frequency range. This parameter is ignored when you set the SetRangeAbsoluteLimitMode(String, RFmxSpecAnMXSpurAbsoluteLimitMode) method to Couple.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurCfgRangeAbsoluteLimitArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8692a5f5-513d-208b-a4f4-72839b1d1811.htm language=enus -->
## TOPIC 00326: rfmxspecandotnet/html/8692a5f5-513d-208b-a4f4-72839b1d1811.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8692a5f5-513d-208b-a4f4-72839b1d1811.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8692a5f5-513d-208b-a4f4-72839b1d1811.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.SetNumberOfRecords Method

RFmxSpecAnMXCcdfConfigurationSetNumberOfRecords Method

Sets the number of acquisitions used for the complementary cumulative distribution function (CCDF) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfRecords(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfRecords ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of acquisitions used for the CCDF measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFSetNumberOfRecords() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8716c23e-e772-9e00-ee63-0d5a39c45954.htm language=enus -->
## TOPIC 00327: rfmxspecandotnet/html/8716c23e-e772-9e00-ee63-0d5a39c45954.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8716c23e-e772-9e00-ee63-0d5a39c45954.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8716c23e-e772-9e00-ee63-0d5a39c45954.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Ccdf Property

RFmxSpecAnMXCcdf Property

Gets the RFmxSpecAnMXCcdf instance that represents the CCDF measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXCcdf Ccdf { get; }
```

```text
Public ReadOnly Property Ccdf As RFmxSpecAnMXCcdf
	Get
```

###### Property Value

RFmxSpecAnMXCcdf

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/876f37ac-5080-b367-3bda-1b1e6c37fe0e.htm language=enus -->
## TOPIC 00328: rfmxspecandotnet/html/876f37ac-5080-b367-3bda-1b1e6c37fe0e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/876f37ac-5080-b367-3bda-1b1e6c37fe0e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/876f37ac-5080-b367-3bda-1b1e6c37fe0e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumDetectorType Enumeration

RFmxSpecAnMXSpectrumDetectorType Enumeration

Specifies the type of detector to be used.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumDetectorType
```

```text
Public Enumeration RFmxSpecAnMXSpectrumDetectorType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | The detector is disabled. |
| Sample | 1 | The central point in the bucket is detected. |
| Normal | 2 | The maximum and minimum values of the samples are detected in alternate buckets. |
| Peak | 3 | The maximum value of the samples in the bucket is detected. |
| NegativePeak | 4 | The minimum value of the samples in the bucket is detected. |
| AverageRms | 5 | The average RMS of all the samples in the bucket is detected. |
| AverageVoltage | 6 | The average voltage of all the samples in the bucket is detected. |
| AverageLog | 7 | The average log of all the samples in the bucket is detected. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/87779196-f3ee-0d4b-8a69-a38f7e1460dc.htm language=enus -->
## TOPIC 00329: rfmxspecandotnet/html/87779196-f3ee-0d4b-8a69-a38f7e1460dc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/87779196-f3ee-0d4b-8a69-a38f7e1460dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/87779196-f3ee-0d4b-8a69-a38f7e1460dc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFExternalPreampPresent Enumeration

RFmxSpecAnMXNFExternalPreampPresent Enumeration

Specifies whether an external preamplifier is present in the signal path.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFExternalPreampPresent
```

```text
Public Enumeration RFmxSpecAnMXNFExternalPreampPresent
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | No external preamplifier present in the signal path. |
| True | 1 | An external preamplifier present in the signal path. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/877c81b4-04e3-9b90-0409-f9b47a985998.htm language=enus -->
## TOPIC 00330: rfmxspecandotnet/html/877c81b4-04e3-9b90-0409-f9b47a985998.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/877c81b4-04e3-9b90-0409-f9b47a985998.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/877c81b4-04e3-9b90-0409-f9b47a985998.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetSmoothingPercentage Method

RFmxSpecAnMXPhaseNoiseConfigurationSetSmoothingPercentage Method

Sets the number of trace points to use in the moving average filter as a percentage of total number of points in the log plot trace.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSmoothingPercentage(
	string selectorString,
	double value
)
```

```text
Public Function SetSmoothingPercentage ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the number of trace points to use in the moving average filter as a percentage of total number of points in the log plot trace.

###### Return Value

Int32

##### Remarks

PhaseNoiseSmoothingPercentage

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/87a4a7e9-b523-04af-f040-7ff4c073d3aa.htm language=enus -->
## TOPIC 00331: rfmxspecandotnet/html/87a4a7e9-b523-04af-f040-7ff4c073d3aa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/87a4a7e9-b523-04af-f040-7ff4c073d3aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/87a4a7e9-b523-04af-f040-7ff4c073d3aa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpResults.FetchCarrierMeasurement Method

RFmxSpecAnMXChpResultsFetchCarrierMeasurement Method

Fetches channel power (CHP) measurement results.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurement(
	string selectorString,
	double timeout,
	out double absolutePower,
	out double psd,
	out double relativePower
)
```

```text
Public Function FetchCarrierMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef absolutePower As Double,
	<OutAttribute> ByRef psd As Double,
	<OutAttribute> ByRef relativePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absolutePower Double**
  - Upon return, contains the averaged channel power, in dBm, measured in the specified integration bandwidth.
- **psd Double**
  - Upon return, contains the power spectral density of the channel, in dBm/Hz.
- **relativePower Double**
  - Upon return, contains the carrier power, in dB, measured relative to the total carrier power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPFetchCarrierMeasurement() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/88416a87-78b3-b24f-1039-84a767f978f7.htm language=enus -->
## TOPIC 00332: rfmxspecandotnet/html/88416a87-78b3-b24f-1039-84a767f978f7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/88416a87-78b3-b24f-1039-84a767f978f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/88416a87-78b3-b24f-1039-84a767f978f7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetAveragingCount Method

RFmxSpecAnMXSemConfigurationSetAveragingCount Method

RFmxSpecAnMXSemAveragingEnabled

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the number of acquisitions used for averaging when you set the RFmxSpecAnMXSemAveragingEnabled method to True.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetAveragingCount() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8875b735-f8a9-4e65-6867-504af4996ca1.htm language=enus -->
## TOPIC 00333: rfmxspecandotnet/html/8875b735-f8a9-4e65-6867-504af4996ca1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8875b735-f8a9-4e65-6867-504af4996ca1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8875b735-f8a9-4e65-6867-504af4996ca1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetIQOriginOffsetCorrectionEnabled Method

RFmxSpecAnMXDpdConfigurationSetIQOriginOffsetCorrectionEnabled Method

Sets the IQ origin offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQOriginOffsetCorrectionEnabled(
	string selectorString,
	RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled value
)
```

```text
Public Function SetIQOriginOffsetCorrectionEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled**
  - Specifies the IQ origin offset correction for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8877d388-d6b9-6d07-b533-b59660c80ec0.htm language=enus -->
## TOPIC 00334: rfmxspecandotnet/html/8877d388-d6b9-6d07-b533-b59660c80ec0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8877d388-d6b9-6d07-b533-b59660c80ec0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8877d388-d6b9-6d07-b533-b59660c80ec0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpFftOverlapMode Enumeration

RFmxSpecAnMXAcpFftOverlapMode Enumeration

SetMeasurementMethod(String, RFmxSpecAnMXAcpMeasurementMethod)

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpFftOverlapMode
```

```text
Public Enumeration RFmxSpecAnMXAcpFftOverlapMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the overlap between the chunks. |
| Automatic | 1 | Measurement computes the overlap based on the ACP FFT Window set by the user. When you set the SetFftWindow(String, RFmxSpecAnMXAcpFftWindow) method to FlatTop, the number of overlapped samples between consecutive chunks is 50% of the value of the SetSequentialFftSize(String, Int32) method. When you set the ACP FFT Window method to None, the chunks are not overlapped. |
| UserDefined | 2 | Measurement uses the overlap that you specify in the SetFftOverlap(String, Double) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8a665f36-c239-35a5-a60b-e353105e3403.htm language=enus -->
## TOPIC 00335: rfmxspecandotnet/html/8a665f36-c239-35a5-a60b-e353105e3403.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8a665f36-c239-35a5-a60b-e353105e3403.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8a665f36-c239-35a5-a60b-e353105e3403.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTriggerType Enumeration

RFmxSpecAnMXTriggerType Enumeration

Specifies the trigger type.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXTriggerType
```

```text
Public Enumeration RFmxSpecAnMXTriggerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | Specifies that no reference trigger is configured. |
| DigitalEdge | 1 | Specifies that the reference trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(String, String) method. |
| IQPowerEdge | 2 | The reference trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSlope(String, RFmxSpecAnMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8aa9a4a9-9a27-93c9-3a3d-3c39e9d1a0d9.htm language=enus -->
## TOPIC 00336: rfmxspecandotnet/html/8aa9a4a9-9a27-93c9-3a3d-3c39e9d1a0d9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8aa9a4a9-9a27-93c9-3a3d-3c39e9d1a0d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8aa9a4a9-9a27-93c9-3a3d-3c39e9d1a0d9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurRangeEnabled Enumeration

RFmxSpecAnMXSpurRangeEnabled Enumeration

Specifies whether to measure the spurious emissions (Spur) in the frequency range.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpurRangeEnabled
```

```text
Public Enumeration RFmxSpecAnMXSpurRangeEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the acquisition of the frequency range. |
| True | 1 | Enables measurement of Spurs in the frequency range. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8aaf5bf8-d0e2-b28c-d451-5f862f8509ce.htm language=enus -->
## TOPIC 00337: rfmxspecandotnet/html/8aaf5bf8-d0e2-b28c-d451-5f862f8509ce.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8aaf5bf8-d0e2-b28c-d451-5f862f8509ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8aaf5bf8-d0e2-b28c-d451-5f862f8509ce.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMIntermodEnabled Enumeration

RFmxSpecAnMXIMIntermodEnabled Enumeration

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIMIntermodEnabled
```

```text
Public Enumeration RFmxSpecAnMXIMIntermodEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables an intermod for the IM measurement. The results for the disabled intermods are displayed as NaN. |
| True | 1 | Enables an intermod for the IM measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8ad7bff6-039c-caf6-b373-70e4d731dc74.htm language=enus -->
## TOPIC 00338: rfmxspecandotnet/html/8ad7bff6-039c-caf6-b373-70e4d731dc74.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8ad7bff6-039c-caf6-b373-70e4d731dc74.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8ad7bff6-039c-caf6-b373-70e4d731dc74.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQ Class

RFmxSpecAnMXIQ Class

Represents an I/Q measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXIQ : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXIQ
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXIQ type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXIQConfiguration instance that enables configuration of I/Q measurement. |
|  | Results | Gets the RFmxSpecAnMXIQResults instance that provides methods to retrieve I/Q measurement results. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8af9191e-c5df-6996-1ecb-49ecf2eb8f6c.htm language=enus -->
## TOPIC 00339: rfmxspecandotnet/html/8af9191e-c5df-6996-1ecb-49ecf2eb8f6c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8af9191e-c5df-6996-1ecb-49ecf2eb8f6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8af9191e-c5df-6996-1ecb-49ecf2eb8f6c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetFrequencyConverterFrequencyContext Method

RFmxSpecAnMXNFConfigurationGetFrequencyConverterFrequencyContext Method

Gets the context of the NF Frequency List method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyConverterFrequencyContext(
	string selectorString,
	out RFmxSpecAnMXNFFrequencyConverterFrequencyContext value
)
```

```text
Public Function GetFrequencyConverterFrequencyContext ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXNFFrequencyConverterFrequencyContext
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFFrequencyConverterFrequencyContext**
  - Upon return, contains the context of the NF Frequency List method.

###### Return Value

Int32

##### Remarks

NFFrequencyConverterFrequencyContext

RF

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8b262703-4911-5cd1-1df6-672e318a1d19.htm language=enus -->
## TOPIC 00340: rfmxspecandotnet/html/8b262703-4911-5cd1-1df6-672e318a1d19.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8b262703-4911-5cd1-1df6-672e318a1d19.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8b262703-4911-5cd1-1df6-672e318a1d19.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetDutInputLossFrequency Method

RFmxSpecAnMXNFConfigurationSetDutInputLossFrequency Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDutInputLossFrequency(
	string selectorString,
	double[] value
)
```

```text
Public Function SetDutInputLossFrequency ( 
	selectorString As String,
	value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies an array of frequencies corresponding to the value of the SetDutInputLoss(String, Double) method. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

NFDutInputLossFrequency

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8b368b3c-b3ca-9fe9-a631-2b87c56dcfc3.htm language=enus -->
## TOPIC 00341: rfmxspecandotnet/html/8b368b3c-b3ca-9fe9-a631-2b87c56dcfc3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8b368b3c-b3ca-9fe9-a631-2b87c56dcfc3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8b368b3c-b3ca-9fe9-a631-2b87c56dcfc3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.GetRangeSpurAmplitude Method

RFmxSpecAnMXSpurResultsGetRangeSpurAmplitude Method

Gets the power, in dBm, of the detected spurious emission (Spur).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeSpurAmplitude(
	string selectorString,
	out double value
)
```

```text
Public Function GetRangeSpurAmplitude ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name, range number and spur number. Example: "range0/spur0","result::r1/range0/spur0". You can use the BuildSpurString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the power, in dBm, of the detected Spur.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetResultsRangeAmplitude() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8d018535-2b38-8c8c-4602-5a9a82ad3256.htm language=enus -->
## TOPIC 00342: rfmxspecandotnet/html/8d018535-2b38-8c8c-4602-5a9a82ad3256.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8d018535-2b38-8c8c-4602-5a9a82ad3256.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8d018535-2b38-8c8c-4602-5a9a82ad3256.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.SetThresholdEnabled Method

RFmxSpecAnMXCcdfConfigurationSetThresholdEnabled Method

Sets whether to enable thresholding of the acquired samples to be used for the complementary cumulative distribution function (CCDF) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetThresholdEnabled(
	string selectorString,
	RFmxSpecAnMXCcdfThresholdEnabled value
)
```

```text
Public Function SetThresholdEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXCcdfThresholdEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXCcdfThresholdEnabled**
  - Specifies whether to enable thresholding of the acquired samples to be used for the CCDF measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFSetThresholdEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8d1e175d-bb6d-178f-cbae-964c8f83b79e.htm language=enus -->
## TOPIC 00343: rfmxspecandotnet/html/8d1e175d-bb6d-178f-cbae-964c8f83b79e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8d1e175d-bb6d-178f-cbae-964c8f83b79e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8d1e175d-bb6d-178f-cbae-964c8f83b79e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetNumberOfCarriers Method

RFmxSpecAnMXDpdConfigurationGetNumberOfCarriers Method

SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfCarriers(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfCarriers ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of carriers in the reference waveform when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False.

###### Return Value

Int32

##### Remarks

DpdNumberOfCarriers

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8d4491c1-7cf3-bcce-9b83-890cb296d7c8.htm language=enus -->
## TOPIC 00344: rfmxspecandotnet/html/8d4491c1-7cf3-bcce-9b83-890cb296d7c8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8d4491c1-7cf3-bcce-9b83-890cb296d7c8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8d4491c1-7cf3-bcce-9b83-890cb296d7c8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.ListType Property

RFmxSpecAnMXListListType Property

Type

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8e57c96d-b050-5f10-078e-8d44e9694c3b.htm language=enus -->
## TOPIC 00345: rfmxspecandotnet/html/8e57c96d-b050-5f10-078e-8d44e9694c3b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8e57c96d-b050-5f10-078e-8d44e9694c3b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8e57c96d-b050-5f10-078e-8d44e9694c3b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFDutInputLossCompensationEnabled Enumeration

RFmxSpecAnMXNFDutInputLossCompensationEnabled Enumeration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFDutInputLossCompensationEnabled
```

```text
Public Enumeration RFmxSpecAnMXNFDutInputLossCompensationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The NF measurement ignores the ohmic losses. |
| True | 1 | The NF measurement accounts for the ohmic losses. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8e6f7ccf-4a33-df06-f62a-a7c13bd0649c.htm language=enus -->
## TOPIC 00346: rfmxspecandotnet/html/8e6f7ccf-4a33-df06-f62a-a7c13bd0649c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8e6f7ccf-4a33-df06-f62a-a7c13bd0649c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8e6f7ccf-4a33-df06-f62a-a7c13bd0649c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumMeasurementMode Enumeration

RFmxSpecAnMXSpectrumMeasurementMode Enumeration

Specifies whether the measurement calibrates the noise floor of analyzer or performs the spectrum measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumMeasurementMode
```

```text
Public Enumeration RFmxSpecAnMXSpectrumMeasurementMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Measure | 0 | Spectrum measurement is performed on the acquired signal. |
| CalibrateNoiseFloor | 1 | Manual noise calibration of the signal analyzer is performed for the spectrum measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8e909775-9253-088a-f104-fc2c3a55710c.htm language=enus -->
## TOPIC 00347: rfmxspecandotnet/html/8e909775-9253-088a-f104-fc2c3a55710c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8e909775-9253-088a-f104-fc2c3a55710c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8e909775-9253-088a-f104-fc2c3a55710c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetAveragingEnabled Method

RFmxSpecAnMXChpConfigurationGetAveragingEnabled Method

Indicates whether averaging for the channel power (CHP) measurement is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxSpecAnMXChpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpAveragingEnabled**
  - Upon return, contains a value that indicates whether averaging for the CHP measurement is enabled.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8ef45637-2a3b-2496-d2d8-14a3dad7080b.htm language=enus -->
## TOPIC 00348: rfmxspecandotnet/html/8ef45637-2a3b-2496-d2d8-14a3dad7080b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8ef45637-2a3b-2496-d2d8-14a3dad7080b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8ef45637-2a3b-2496-d2d8-14a3dad7080b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Pavt Property

RFmxSpecAnMXPavt Property

RFmxSpecAnMXPavt

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXPavt Pavt { get; }
```

```text
Public ReadOnly Property Pavt As RFmxSpecAnMXPavt
	Get
```

###### Property Value

RFmxSpecAnMXPavt

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8ef4ae48-ba35-1e38-b49a-000638ed52ee.htm language=enus -->
## TOPIC 00349: rfmxspecandotnet/html/8ef4ae48-ba35-1e38-b49a-000638ed52ee.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8ef4ae48-ba35-1e38-b49a-000638ed52ee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8ef4ae48-ba35-1e38-b49a-000638ed52ee.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.SetEvmUnit Method

RFmxSpecAnMXIdpdConfigurationSetEvmUnit Method

Sets the units of the EVM results.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvmUnit(
	string selectorString,
	RFmxSpecAnMXIdpdEvmUnit value
)
```

```text
Public Function SetEvmUnit ( 
	selectorString As String,
	value As RFmxSpecAnMXIdpdEvmUnit
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIdpdEvmUnit**
  - Specifies the units of the EVM results.

###### Return Value

Int32

##### Remarks

IdpdEvmUnit

Percentage

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8f02ac59-c870-a050-e283-8243067e99d7.htm language=enus -->
## TOPIC 00350: rfmxspecandotnet/html/8f02ac59-c870-a050-e283-8243067e99d7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8f02ac59-c870-a050-e283-8243067e99d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8f02ac59-c870-a050-e283-8243067e99d7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.GetCarrierTotalRelativePower Method

RFmxSpecAnMXAcpResultsGetCarrierTotalRelativePower Method

Gets the carrier power, in dB, measured relative to the total carrier power of all active carriers.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierTotalRelativePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierTotalRelativePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the carrier power, in dB, measured relative to the total carrier power of all active carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsCarrierTotalRelativePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8f0614f3-7b58-34ea-ad7f-4fab93d3490c.htm language=enus -->
## TOPIC 00351: rfmxspecandotnet/html/8f0614f3-7b58-34ea-ad7f-4fab93d3490c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8f0614f3-7b58-34ea-ad7f-4fab93d3490c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8f0614f3-7b58-34ea-ad7f-4fab93d3490c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntResults.GetAverageRelativeFrequency Method

RFmxSpecAnMXFcntResultsGetAverageRelativeFrequency Method

SetThresholdEnabled(String, RFmxSpecAnMXFcntThresholdEnabled)

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageRelativeFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageRelativeFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the signal frequency relative to the RF center frequency. Only samples above the threshold are used when you set the SetThresholdEnabled(String, RFmxSpecAnMXFcntThresholdEnabled) method to True.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetResultsAverageRelativeFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/8f0c09a9-1b17-5013-b622-eafb88a42abc.htm language=enus -->
## TOPIC 00352: rfmxspecandotnet/html/8f0c09a9-1b17-5013-b622-eafb88a42abc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/8f0c09a9-1b17-5013-b622-eafb88a42abc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/8f0c09a9-1b17-5013-b622-eafb88a42abc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SetAttributeInt Method

RFmxSpecAnMXSetAttributeInt Method

Sets the value of a Int attribute.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SetAttributeI32() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/91dfbbf7-2828-84a6-7931-04271fa94702.htm language=enus -->
## TOPIC 00353: rfmxspecandotnet/html/91dfbbf7-2828-84a6-7931-04271fa94702.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/91dfbbf7-2828-84a6-7931-04271fa94702.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/91dfbbf7-2828-84a6-7931-04271fa94702.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.ConfigureCancellation Method

RFmxSpecAnMXPhaseNoiseConfigurationConfigureCancellation Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCancellation(
	string selectorString,
	RFmxSpecAnMXPhaseNoiseCancellationEnabled cancellationEnabled,
	double cancellationThreshold,
	float[] frequency,
	float[] referencePhaseNoise
)
```

```text
Public Function ConfigureCancellation ( 
	selectorString As String,
	cancellationEnabled As RFmxSpecAnMXPhaseNoiseCancellationEnabled,
	cancellationThreshold As Double,
	frequency As Single(),
	referencePhaseNoise As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **cancellationEnabled RFmxSpecAnMXPhaseNoiseCancellationEnabled**
  - Specifies whether to enable or disable the phase noise cancellation.
- **cancellationThreshold Double**
  - Specifies the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed.
- **frequency Single**
  - Specifies an array of frequency offsets where the reference phase noise has been measured. This value is expressed in Hz.
- **referencePhaseNoise Single**
  - Specifies an array of the reference phase noise at the frequency offsets. This value is expressed in dBc/Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/91e2c3c5-f3eb-91be-c54c-ade80122b8cd.htm language=enus -->
## TOPIC 00354: rfmxspecandotnet/html/91e2c3c5-f3eb-91be-c54c-ade80122b8cd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/91e2c3c5-f3eb-91be-c54c-ade80122b8cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/91e2c3c5-f3eb-91be-c54c-ade80122b8cd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetCarrierBandwidth Method

RFmxSpecAnMXAmpmConfigurationSetCarrierBandwidth Method

SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCarrierBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetCarrierBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AmpmCarrierBandwidth

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/92bf851e-4bca-d280-4b00-fbe921b8a322.htm language=enus -->
## TOPIC 00355: rfmxspecandotnet/html/92bf851e-4bca-d280-4b00-fbe921b8a322.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/92bf851e-4bca-d280-4b00-fbe921b8a322.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/92bf851e-4bca-d280-4b00-fbe921b8a322.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetHeadroomMode Method

RFmxSpecAnMXDpdApplyDpdSetHeadroomMode Method

**Note: This API is now obsolete.**

SetHeadroom(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This property/enum has been deprecated")]
public int SetHeadroomMode(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdHeadroomMode value
)
```

```text
<ObsoleteAttribute("This property/enum has been deprecated")>
Public Function SetHeadroomMode ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdApplyDpdHeadroomMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdHeadroomMode**
  - Contains a value that indicates whether to compute and apply the headroom of the predistorted waveform, or to apply the value that you specify using the SetHeadroom(String, Double) method, on the predistorted waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDHeadroomMode() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/92c28de3-5c9b-724d-ac74-951591390bd7.htm language=enus -->
## TOPIC 00356: rfmxspecandotnet/html/92c28de3-5c9b-724d-ac74-951591390bd7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/92c28de3-5c9b-724d-ac74-951591390bd7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/92c28de3-5c9b-724d-ac74-951591390bd7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNumberOfAnalysisThreads Method

RFmxSpecAnMXAcpConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the maximum number of threads used for parallelism for ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/96d3132e-6840-fd81-1631-c63efc736457.htm language=enus -->
## TOPIC 00357: rfmxspecandotnet/html/96d3132e-6840-fd81-1631-c63efc736457.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/96d3132e-6840-fd81-1631-c63efc736457.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/96d3132e-6840-fd81-1631-c63efc736457.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureOffsetBandwidthIntegral Method

RFmxSpecAnMXSemConfigurationConfigureOffsetBandwidthIntegral Method

Configures the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). If you set this method to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetBandwidthIntegral(
	string selectorString,
	int bandwidthIntegral
)
```

```text
Public Function ConfigureOffsetBandwidthIntegral ( 
	selectorString As String,
	bandwidthIntegral As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **bandwidthIntegral Int32**
  - Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. If you set this method to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetBandwidthIntegral() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/97c75919-870d-66ac-acfc-763db7103206.htm language=enus -->
## TOPIC 00358: rfmxspecandotnet/html/97c75919-870d-66ac-acfc-763db7103206.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/97c75919-870d-66ac-acfc-763db7103206.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/97c75919-870d-66ac-acfc-763db7103206.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX Methods

RFmxSpecAnMX Methods

The [RFmxSpecAnMX](6582dec8-b7a6-0aa0-d3ec-1efc28b3446e.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with signal instance, which were previously initiated by the Initiate or measurement read methods. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in the iq parameter. Call this method after you configure the signal and measurement properties. You can fetch measurement results using the Fetch methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is either IQ or IQ or Spectral. This method is supported only when the RFmxInstr session is created with option string "AnalysisOnly=1". Note Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the Commit(String) method. |
| Note |  |  |
| Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the Commit(String) method. |  |  |
|  | AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum that you specify in the spectrum parameter. Call this method after you configure the signal and measurement properties. You can fetch measurement results using the Fetch methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is either Spectral or IQ or Spectral. This method is supported only when the RFmxInstr session is created with option string "AnalysisOnly=1". Note Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the Commit(String) method. |
| Note |  |  |
| Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the Commit(String) method. |  |  |
|  | AutoLevel | Examines the incoming signal to calculate the peak power level and sets it as the value of the GetReferenceLevel(String, Double) method. Use this method to help calculate an approximate setting for the power level for measurements. When using PXIe-5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the AutoLevel(String, Double, Double, Double) method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method, thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildCarrierString | Obsolete. Creates the carrier string to use as the selector string with the SEM, ACP, and CHP carrier configuration or fetch properties and methods. |
|  | BuildCarrierString2 | Creates the carrier string to use as the selector string with the SEM, ACP, and CHP carrier configuration or fetch properties and methods. |
|  | BuildHarmonicString | Obsolete. Creates the selector string to use with Harmonics configuration or fetch methods. |
|  | BuildHarmonicString2 | Creates the selector string to use with Harmonics configuration or fetch methods. |
|  | BuildIntermodString | Creates the intermod string to use as the selector string with the IM configuration or fetch methods and methods. |
|  | BuildListStepString | Creates the list step string. |
|  | BuildListString | Creates the list string. |
|  | BuildMarkerString | Obsolete. Creates a selector string for use with marker configuration or fetch methods. |
|  | BuildMarkerString2 | Creates a selector string for use with marker configuration or fetch methods. |
|  | BuildOffsetString | Obsolete. Creates the offset string to use as the selector string with SEM and ACP offset configuration or fetch methods. |
|  | BuildOffsetString2 | Creates the offset string to use as the selector string with SEM and ACP offset configuration or fetch methods. |
|  | BuildRangeSpurString | Obsolete. Creates the selector string for use with Spurious emissions (Spur) measurement results or fetch methods. |
|  | BuildRangeString | Obsolete. Creates a selector string for use with Spurious emissions (Spur) configuration or fetch methods. |
|  | BuildRangeString2 | Creates a selector string for use with spurious emissions (Spur) configuration or fetch methods. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSegmentString | Creates a selector string for use with the PAVT configuration or fetch methods and methods. |
|  | BuildSpurString2 | Creates the selector string for use with Spurious emissions (Spur) measurement results or fetch methods. |
|  | CheckMeasurementStatus | Checks the status of the measurement. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the properties from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxSpecAn commits settings to the hardware when you call the RFmxInstrMX Initiate or any of the measurement Read methods. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureExternalAttenuation | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
|  | ConfigureFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. |
|  | ConfigureReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
|  | ConfigureRF | Configures the RF properties of the signal specified by the selector string. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a Software Trigger and then marks a reference point within the record. |
|  | DeleteSignalConfiguration | Deletes the current instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. This method does not do anything if it is called by using list step instance. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllNamedResultNames | Returns all the named result names of the current signal instance. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeDoubleArray | Gets the value of a double array attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeSingleArray | Gets the value of a single array attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level, in dBm, which the auto level function uses to estimate the peak power of the input signal. |
|  | GetCenterFrequency | Gets the expected carrier frequency, in hertz (Hz), of the RF signal that needs to be acquires. The signal analyzer tunes to this frequency. |
|  | GetDigitalEdgeTriggerEdge | Gets whether the RF vector signal analyzer detects a Rising or Falling on the RFmxSpecAnMXDigitalEdgeTriggerEdge signal. |
|  | GetDigitalEdgeTriggerSource | Returns the source terminal for the digital-edge trigger. |
|  | GetErrorString | Converts the status code returned by an RFmxSpecAn function into a string. |
|  | GetExternalAttenuation | Gets the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the RF signal analyzer. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQPowerEdgeTriggerLevel | Gets the power level at which the device triggers. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the GetIQPowerEdgeTriggerLevel method. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or falling. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | GetListStepTimerDuration | Gets the duration of a given list step. This value is expressed in seconds. |
|  | GetListStepTimerOffset | Gets the time offset from the start of the step for which the measurements are computed. This value is expressed in seconds. This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent. |
|  | GetReferenceLevel | Gets the reference level which represents the maximum expected power of the RF input signal. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | GetResultFetchTimeout | Gets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | GetTriggerDelay | Gets the trigger delay time, in seconds. |
|  | GetTriggerMinimumQuietTimeDuration | Gets a time duration, in seconds, for which the signal must be quiet before the RF signal analyzer arms the I/Q Power Edge trigger. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement computes the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the type of reference trigger to use for signal acquisition. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetWarning | Retrieves and then clears the warning information for the session. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. To get the status of measurements, you can use the CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you configure to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeDoubleArray | Set the value of a double array attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeSingleArray | Set the value of a single array attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level, in dBm, which the auto level function uses to estimate the peak power of the input signal. |
|  | SetCenterFrequency | Sets the expected carrier frequency, in hertz (Hz), of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. |
|  | SetDigitalEdgeTriggerEdge | Sets whether the RF vector signal analyzer detects a Rising or Falling on the RFmxSpecAnMXDigitalEdgeTriggerEdge signal. This is used only when you set the SetTriggerType(String, RFmxSpecAnMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the RFmxSpecAnMXDigitalEdgeTriggerEdge. This method is used only when you set the SetTriggerType(String, RFmxSpecAnMXTriggerType) method to DigitalEdge. |
|  | SetExternalAttenuation | Sets the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the RF signal analyzer. |
|  | SetIQPowerEdgeTriggerLevel | Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxSpecAnMXIQPowerEdgeTriggerLevelType) method to Relative; and in units specified by the value of the RFmxSpecAnMX.ConfigureReferenceLevelUnits method when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxSpecAnMXIQPowerEdgeTriggerLevelType) method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the Trigger when the signal power is rising or falling. When you set the SetTriggerType(String, RFmxSpecAnMXTriggerType) to IQPowerEdge, the device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This is used only when you set the SetTriggerType(String, RFmxSpecAnMXTriggerType) to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | SetListStepTimerDuration | Sets the duration of a given list step. This value is expressed in seconds. |
|  | SetListStepTimerOffset | Sets the time offset from the start of the step for which the measurements are computed. This value is expressed in seconds. This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent. |
|  | SetReferenceLevel | Sets the reference level which represents the maximum expected power of the RF input signal. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | SetResultFetchTimeout | Sets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. |
|  | SetSelectedPorts | Sets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | SetTriggerDelay | Sets the trigger delay time, in seconds. |
|  | SetTriggerMinimumQuietTimeDuration | Sets a time duration, in seconds, for which the signal must be quiet before the RF signal analyzer arms the ConfigureIQPowerEdgeTrigger(String, String, Double, RFmxSpecAnMXIQPowerEdgeTriggerSlope, Double, RFmxSpecAnMXTriggerMinimumQuietTimeMode, Double, Boolean). |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement computes the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the type of reference trigger to use for signal acquisition. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/97f7f1fa-375a-e5c7-e7ef-677a8df63a8d.htm language=enus -->
## TOPIC 00359: rfmxspecandotnet/html/97f7f1fa-375a-e5c7-e7ef-677a8df63a8d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/97f7f1fa-375a-e5c7-e7ef-677a8df63a8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/97f7f1fa-375a-e5c7-e7ef-677a8df63a8d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwRbwAutoBandwidth Enumeration

RFmxSpecAnMXObwRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the resolution bandwidth (RBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXObwRbwAutoBandwidth
```

```text
Public Enumeration RFmxSpecAnMXObwRbwAutoBandwidth
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(String, Double) method. |
| True | 1 | The measurement computes the RBW. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/97f99718-6461-e7e3-0d3d-b4b2ff63fdbf.htm language=enus -->
## TOPIC 00360: rfmxspecandotnet/html/97f99718-6461-e7e3-0d3d-b4b2ff63fdbf.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/97f99718-6461-e7e3-0d3d-b4b2ff63fdbf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/97f99718-6461-e7e3-0d3d-b4b2ff63fdbf.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.FetchUpperOffsetPowerArray Method

RFmxSpecAnMXSemResultsFetchUpperOffsetPowerArray Method

Fetches the arrays of upper offset segment power measurements.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **totalAbsolutePower Double**
  - Upon return, contains the array of upper (positive) offset segment powers measured.
- **totalRelativePower Double**
  - Upon return, contains the array of powers measured in each upper (positive) offset segment relative to the integrated or peak power of the reference carrier.
- **peakAbsolutePower Double**
  - Upon return, contains the array of peak powers measured in each upper (positive) offset segment. The power is measured in dBm when you set the SetPowerUnits(String, RFmxSpecAnMXSemPowerUnits) method to dBm, and in dBm/Hz when you set the SetPowerUnits(String, RFmxSpecAnMXSemPowerUnits) method to dBmPerHertz.
- **peakFrequency Double**
  - Upon return, contains the array of frequencies, in hertz (Hz), at which the peak power occurred in each offset segment.
- **peakRelativePower Double**
  - Upon return, contains the array of peak powers measured in each upper (positive) offset segment relative to the integrated or peak power of the reference carrier.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMFetchUpperOffsetPowerArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9801c159-fc02-ed2a-baeb-edba9f355075.htm language=enus -->
## TOPIC 00361: rfmxspecandotnet/html/9801c159-fc02-ed2a-baeb-edba9f355075.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9801c159-fc02-ed2a-baeb-edba9f355075.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9801c159-fc02-ed2a-baeb-edba9f355075.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetCarrierFrequency Method

RFmxSpecAnMXSemConfigurationGetCarrierFrequency Method

Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the center frequency, in Hz, of the carrier, relative to the RF center frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/981d2766-52ba-5a30-c0d8-cd873c71889c.htm language=enus -->
## TOPIC 00362: rfmxspecandotnet/html/981d2766-52ba-5a30-c0d8-cd873c71889c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/981d2766-52ba-5a30-c0d8-cd873c71889c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/981d2766-52ba-5a30-c0d8-cd873c71889c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.SetSegmentStartTime Method

RFmxSpecAnMXPavtConfigurationSetSegmentStartTime Method

SetMeasurementLocationType(String, RFmxSpecAnMXPavtMeasurementLocationType)

Time

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentStartTime(
	string selectorString,
	double value
)
```

```text
Public Function SetSegmentStartTime ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(String, RFmxSpecAnMXPavtMeasurementLocationType) method to Time.

###### Return Value

Int32

##### Remarks

PavtSegmentStartTime

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9a4134c1-a7ab-e76d-2c7e-501c578102a6.htm language=enus -->
## TOPIC 00363: rfmxspecandotnet/html/9a4134c1-a7ab-e76d-2c7e-501c578102a6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9a4134c1-a7ab-e76d-2c7e-501c578102a6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9a4134c1-a7ab-e76d-2c7e-501c578102a6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetRbwPercentage Method

RFmxSpecAnMXPhaseNoiseConfigurationSetRbwPercentage Method

Sets the RBW as a percentage of the PhaseNoise Range Start Freq method of the specified subrange when you set the PhaseNoise Range Definition method to Manual.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwPercentage(
	string selectorString,
	double value
)
```

```text
Public Function SetRbwPercentage ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the RBW as a percentage of the start frequency of each subrange when you set the PhaseNoise Range Definition method to Auto.

###### Return Value

Int32

##### Remarks

PhaseNoiseRbwPercentage

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9ca7b03d-816a-198a-76d6-2582746e834f.htm language=enus -->
## TOPIC 00364: rfmxspecandotnet/html/9ca7b03d-816a-198a-76d6-2582746e834f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9ca7b03d-816a-198a-76d6-2582746e834f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9ca7b03d-816a-198a-76d6-2582746e834f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetLowerOffsetPeakFrequency Method

RFmxSpecAnMXSemResultsGetLowerOffsetPeakFrequency Method

Gets the frequency, in hertz (Hz), at which the peak power occurred in the offset segment.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency, in Hz, at which the peak power occurred in the offset segment.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetPeakFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9e6a063e-87e6-099b-7823-56e13046468c.htm language=enus -->
## TOPIC 00365: rfmxspecandotnet/html/9e6a063e-87e6-099b-7823-56e13046468c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9e6a063e-87e6-099b-7823-56e13046468c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9e6a063e-87e6-099b-7823-56e13046468c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetApplyDpdUserLookupTableInputPower Method

RFmxSpecAnMXDpdConfigurationSetApplyDpdUserLookupTableInputPower Method

**Note: This API is now obsolete.**

DpdApplyDpdUserDpdModel

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use SetUserLookupTableInputPower() method from RFmxSpecAnMXDpdApplyDpd class")]
public int SetApplyDpdUserLookupTableInputPower(
	string selectorString,
	float[] value
)
```

```text
<ObsoleteAttribute("Use SetUserLookupTableInputPower() method from RFmxSpecAnMXDpdApplyDpd class")>
Public Function SetApplyDpdUserLookupTableInputPower ( 
	selectorString As String,
	value As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Single**
  - Specifies the input power array for the predistortion lookup table when you set the DpdApplyDpdUserDpdModel method to Lookup Table. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

DpdApplyDpdUserLookupTableInputPower

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9e83090e-c04e-bcd5-6aeb-6d023d297bd3.htm language=enus -->
## TOPIC 00366: rfmxspecandotnet/html/9e83090e-c04e-bcd5-6aeb-6d023d297bd3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9e83090e-c04e-bcd5-6aeb-6d023d297bd3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9e83090e-c04e-bcd5-6aeb-6d023d297bd3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetRbwFilterBandwidth Method

RFmxSpecAnMXAcpConfigurationGetRbwFilterBandwidth Method

Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the bandwidth, in Hz, of the RBW filter used to sweep the acquired signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9e8f475f-d6ad-7f9e-ebbc-d5cff5bd9200.htm language=enus -->
## TOPIC 00367: rfmxspecandotnet/html/9e8f475f-d6ad-7f9e-ebbc-d5cff5bd9200.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9e8f475f-d6ad-7f9e-ebbc-d5cff5bd9200.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9e8f475f-d6ad-7f9e-ebbc-d5cff5bd9200.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.GetImpairmentEstimationStop Method

RFmxSpecAnMXIdpdConfigurationGetImpairmentEstimationStop Method

Gets the stop time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetImpairmentEstimationStop(
	string selectorString,
	out double value
)
```

```text
Public Function GetImpairmentEstimationStop ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contain the stop time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

IdpdImpairmentEstimationStop

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9e98d366-0dd2-0426-8517-ec992f20c7ff.htm language=enus -->
## TOPIC 00368: rfmxspecandotnet/html/9e98d366-0dd2-0426-8517-ec992f20c7ff.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9e98d366-0dd2-0426-8517-ec992f20c7ff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9e98d366-0dd2-0426-8517-ec992f20c7ff.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetFftPadding Method

RFmxSpecAnMXChpConfigurationSetFftPadding Method

Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftPadding(
	string selectorString,
	double value
)
```

```text
Public Function SetFftPadding ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetFFTPadding() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/9e9bcf42-1b4e-d806-d236-7ced809a249f.htm language=enus -->
## TOPIC 00369: rfmxspecandotnet/html/9e9bcf42-1b4e-d806-d236-7ced809a249f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/9e9bcf42-1b4e-d806-d236-7ced809a249f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/9e9bcf42-1b4e-d806-d236-7ced809a249f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNoiseCompensationType Method

RFmxSpecAnMXAcpConfigurationSetNoiseCompensationType Method

Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCompensationType(
	string selectorString,
	RFmxSpecAnMXAcpNoiseCompensationType value
)
```

```text
Public Function SetNoiseCompensationType ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpNoiseCompensationType**
  - Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

AcpNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a0e2a983-2390-21f1-a1e6-dea53751357d.htm language=enus -->
## TOPIC 00370: rfmxspecandotnet/html/a0e2a983-2390-21f1-a1e6-dea53751357d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a0e2a983-2390-21f1-a1e6-dea53751357d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a0e2a983-2390-21f1-a1e6-dea53751357d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetNumberOfAnalysisThreads Method

RFmxSpecAnMXObwConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for occupied bandwidth (OBW) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the maximum number of threads used for parallelism for OBW measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a1075005-cb1a-4397-417c-82232f96eb83.htm language=enus -->
## TOPIC 00371: rfmxspecandotnet/html/a1075005-cb1a-4397-417c-82232f96eb83.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a1075005-cb1a-4397-417c-82232f96eb83.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a1075005-cb1a-4397-417c-82232f96eb83.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetApplyDpdUserLookupTableInputPower Method

RFmxSpecAnMXDpdConfigurationGetApplyDpdUserLookupTableInputPower Method

**Note: This API is now obsolete.**

DpdApplyDpdUserDpdModel

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use GetUserLookupTableInputPower() method from RFmxSpecAnMXDpdApplyDpd class")]
public int GetApplyDpdUserLookupTableInputPower(
	string selectorString,
	ref float[] value
)
```

```text
<ObsoleteAttribute("Use GetUserLookupTableInputPower() method from RFmxSpecAnMXDpdApplyDpd class")>
Public Function GetApplyDpdUserLookupTableInputPower ( 
	selectorString As String,
	ByRef value As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Single**
  - Upon return, contains the input power array for the predistortion lookup table when you set the DpdApplyDpdUserDpdModel method to Lookup Table. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

DpdApplyDpdUserLookupTableInputPower

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a1d64a1e-09a5-a90c-a7eb-ef4a5c41fa2f.htm language=enus -->
## TOPIC 00372: rfmxspecandotnet/html/a1d64a1e-09a5-a90c-a7eb-ef4a5c41fa2f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a1d64a1e-09a5-a90c-a7eb-ef4a5c41fa2f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a1d64a1e-09a5-a90c-a7eb-ef4a5c41fa2f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQPowerEdgeTriggerLevelType Enumeration

RFmxSpecAnMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the RFmx.SpecAnMX.RFmxSpecAnMX.SetIQPowerEdgeTriggerLevel method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIQPowerEdgeTriggerLevelType
```

```text
Public Enumeration RFmxSpecAnMXIQPowerEdgeTriggerLevelType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Relative | 0 | IQ Power EdgeLevel is relative to the value of the RFmxSpecAnMX.ConfigureReferenceLevel method. |
| Absolute | 1 | The IQ Power Edge Level specifies the absolute power. This value is expressed in units specified by the value of the RFmxSpecAnMX.ConfigureReferenceLevelUnits method. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a20c0c85-8d0c-7496-dbde-3aa52e51fed7.htm language=enus -->
## TOPIC 00373: rfmxspecandotnet/html/a20c0c85-8d0c-7496-dbde-3aa52e51fed7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a20c0c85-8d0c-7496-dbde-3aa52e51fed7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a20c0c85-8d0c-7496-dbde-3aa52e51fed7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeAbsoluteLimitMode Method

RFmxSpecAnMXSpurConfigurationSetRangeAbsoluteLimitMode Method

Sets whether the absolute limit threshold is a flat line or a line with a slope.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeAbsoluteLimitMode(
	string selectorString,
	RFmxSpecAnMXSpurAbsoluteLimitMode value
)
```

```text
Public Function SetRangeAbsoluteLimitMode ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurAbsoluteLimitMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurAbsoluteLimitMode**
  - Specifies whether the absolute limit threshold is a flat line or a line with a slope.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeAbsoluteLimitMode() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a2420010-df00-0958-91b6-52b54a0e8f0c.htm language=enus -->
## TOPIC 00374: rfmxspecandotnet/html/a2420010-df00-0958-91b6-52b54a0e8f0c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a2420010-df00-0958-91b6-52b54a0e8f0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a2420010-df00-0958-91b6-52b54a0e8f0c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.ConfigureAveragingMultiplier Method

RFmxSpecAnMXPhaseNoiseConfigurationConfigureAveragingMultiplier Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveragingMultiplier(
	string selectorString,
	int averagingMultiplier
)
```

```text
Public Function ConfigureAveragingMultiplier ( 
	selectorString As String,
	averagingMultiplier As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingMultiplier Int32**
  - Specifies the factor by which the averaging count for each sub-range to increase.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a2479acb-bf7f-9979-88bd-25653175c095.htm language=enus -->
## TOPIC 00375: rfmxspecandotnet/html/a2479acb-bf7f-9979-88bd-25653175c095.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a2479acb-bf7f-9979-88bd-25653175c095.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a2479acb-bf7f-9979-88bd-25653175c095.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavt Class

RFmxSpecAnMXPavt Class

Represents the PAVT measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXPavt : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXPavt
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXPavt type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXPavtConfiguration instance that provides methods to configure the PAVT measurement. |
|  | Results | Gets the RFmxSpecAnMXPavtResults instance that provides methods to fetch and read the PAVT measurement results. |

Top

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

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a27124da-6847-04ca-64f0-1bef14793c4b.htm language=enus -->
## TOPIC 00376: rfmxspecandotnet/html/a27124da-6847-04ca-64f0-1bef14793c4b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a27124da-6847-04ca-64f0-1bef14793c4b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a27124da-6847-04ca-64f0-1bef14793c4b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.SetThresholdEnabled Method

RFmxSpecAnMXTxpConfigurationSetThresholdEnabled Method

Sets whether to enable thresholding of the acquired samples to be used for the transmit power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetThresholdEnabled(
	string selectorString,
	RFmxSpecAnMXTxpThresholdEnabled value
)
```

```text
Public Function SetThresholdEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXTxpThresholdEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXTxpThresholdEnabled**
  - Specifies whether to enable thresholding of the acquired samples to be used for the TXP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPSetThresholdEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a2a6a1fc-9af0-f40c-e21f-173744db04ea.htm language=enus -->
## TOPIC 00377: rfmxspecandotnet/html/a2a6a1fc-9af0-f40c-e21f-173744db04ea.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a2a6a1fc-9af0-f40c-e21f-173744db04ea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a2a6a1fc-9af0-f40c-e21f-173744db04ea.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants Class

RFmxSpecAnMXConstants Class

Specifies constants for I/O terminals.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxSpecAnMXConstants
```

```text
Public NotInheritable Class RFmxSpecAnMXConstants
```

The RFmxSpecAnMXConstants type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. |
|  | Pfi1 | The signal is exported to the PXI trigger line 0. |
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

##### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a493b9ed-9c33-0817-4eae-d26231c0d07a.htm language=enus -->
## TOPIC 00378: rfmxspecandotnet/html/a493b9ed-9c33-0817-4eae-d26231c0d07a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a493b9ed-9c33-0817-4eae-d26231c0d07a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a493b9ed-9c33-0817-4eae-d26231c0d07a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNoiseCompensationEnabled Method

RFmxSpecAnMXAcpConfigurationSetNoiseCompensationEnabled Method

Sets whether to enable compensation of the channel powers for the inherent noise floor of the RF signal analyzer.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCompensationEnabled(
	string selectorString,
	RFmxSpecAnMXAcpNoiseCompensationEnabled value
)
```

```text
Public Function SetNoiseCompensationEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpNoiseCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpNoiseCompensationEnabled**
  - Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetNoiseCompensationEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a5c78132-4a30-dc99-811f-bd80fb38a3b8.htm language=enus -->
## TOPIC 00379: rfmxspecandotnet/html/a5c78132-4a30-dc99-811f-bd80fb38a3b8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a5c78132-4a30-dc99-811f-bd80fb38a3b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a5c78132-4a30-dc99-811f-bd80fb38a3b8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetMaximumIntermodOrder Method

RFmxSpecAnMXIMConfigurationSetMaximumIntermodOrder Method

Sets the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMaximumIntermodOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetMaximumIntermodOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order.

###### Return Value

Int32

##### Remarks

IMMaximumIntermodOrder

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a5ea090e-227b-60a1-3195-9be7c18cadad.htm language=enus -->
## TOPIC 00380: rfmxspecandotnet/html/a5ea090e-227b-60a1-3195-9be7c18cadad.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a5ea090e-227b-60a1-3195-9be7c18cadad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a5ea090e-227b-60a1-3195-9be7c18cadad.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetAutoCarrierDetectionEnabled Method

RFmxSpecAnMXAmpmConfigurationSetAutoCarrierDetectionEnabled Method

Sets if auto detection of carrier offset and carrier bandwidth is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoCarrierDetectionEnabled(
	string selectorString,
	RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled value
)
```

```text
Public Function SetAutoCarrierDetectionEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled**
  - Specifies if auto detection of carrier offset and carrier bandwidth is enabled.

###### Return Value

Int32

##### Remarks

AmpmAutoCarrierDetectionEnabled

True

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a6117dcc-8bd6-fc02-7d92-3545e323ca84.htm language=enus -->
## TOPIC 00381: rfmxspecandotnet/html/a6117dcc-8bd6-fc02-7d92-3545e323ca84.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a6117dcc-8bd6-fc02-7d92-3545e323ca84.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a6117dcc-8bd6-fc02-7d92-3545e323ca84.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.GetNumberOfAnalysisThreads Method

RFmxSpecAnMXHarmConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for Harmonics measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the maximum number of threads used for parallelism for Harmonics measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmGetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a6bffa00-fa45-70cd-5a91-cb80c52ebc00.htm language=enus -->
## TOPIC 00382: rfmxspecandotnet/html/a6bffa00-fa45-70cd-5a91-cb80c52ebc00.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a6bffa00-fa45-70cd-5a91-cb80c52ebc00.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a6bffa00-fa45-70cd-5a91-cb80c52ebc00.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetAllTracesEnabled Method

RFmxSpecAnMXAmpmConfigurationGetAllTracesEnabled Method

Gets the traces to be stored and retrieved after performing the AMPM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - if the traces to be stored and retrieved after performing the AMPM measurement are enabled; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetAllTracesEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a6d77ac3-a2f2-2dab-b1bd-fb1171565d61.htm language=enus -->
## TOPIC 00383: rfmxspecandotnet/html/a6d77ac3-a2f2-2dab-b1bd-fb1171565d61.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a6d77ac3-a2f2-2dab-b1bd-fb1171565d61.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a6d77ac3-a2f2-2dab-b1bd-fb1171565d61.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration Class

RFmxSpecAnMXChpConfiguration Class

Provides methods to configure the channel power (CHP) measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXChpConfiguration : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXChpConfiguration
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXChpConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the channel power (CHP) measurement. |
|  | ConfigureCarrierOffset | Configures the center frequency of the carrier, relative to the RF center frequency. |
|  | ConfigureDetector | Configures the detector settings, including detector type and the number of points to be detected. |
|  | ConfigureFft | Configures window and FFT to obtain a spectrum for the channel power (CHP) measurement. |
|  | ConfigureIntegrationBandwidth | Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power. |
|  | ConfigureNumberOfCarriers | Configures the number of carriers for the CHP measurement. |
|  | ConfigureRbwFilter | Configures the resolution bandwidth (RBW) filter. |
|  | ConfigureRrcFilter | Configures the root-raised-cosine (RRC) filter to apply on the channel before measuring the channel power. |
|  | ConfigureSpan | Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the channel power (CHP) measurement. |
|  | ConfigureSweepTime | Configures the sweep time, in seconds, when you set the SetSweepTimeAuto(String, RFmxSpecAnMXChpSweepTimeAuto) method to False. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether the traces to be stored and retrieved after performing the channel power (CHP) measurement are enabled. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging. |
|  | GetAveragingEnabled | Indicates whether averaging for the channel power (CHP) measurement is enabled. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. |
|  | GetCarrierFrequency | Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
|  | GetCarrierIntegrationBandwidth | Gets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
|  | GetCarrierRrcFilterAlpha | Gets the roll-off factor for the root-raised-cosine (RRC) filter. |
|  | GetCarrierRrcFilterEnabled | Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power. |
|  | GetDetectorPoints | Gets the number of trace points after the detector is applied. |
|  | GetDetectorType | Gets the type of detector to be used. |
|  | GetFftPadding | Gets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. |
|  | GetFftWindow | Gets the FFT window type used to reduce spectral leakage. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIntegrationBandwidth | Obsolete. Gets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
|  | GetMeasurementEnabled | Gets whether the channel power (CHP) measurement is enabled. |
|  | GetMeasurementMode | Gets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCalibrationAveragingAuto | Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
|  | GetNoiseCalibrationAveragingCount | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. |
|  | GetNoiseCalibrationMode | Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCompensationEnabled | Gets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(String, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(String, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | GetNoiseCompensationType | Gets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for channel power (CHP) measurement. |
|  | GetNumberOfCarriers | Gets the number of carriers. |
|  | GetRbwFilterAutoBandwidth | Gets whether the measurement computes the resolution bandwidth (RBW). |
|  | GetRbwFilterBandwidth | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
|  | GetRbwFilterBandwidthDefinition | Gets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method. |
|  | GetRbwFilterType | Gets the shape of the digital resolution bandwidth (RBW) filter. |
|  | GetRrcFilterAlpha | Obsolete. Gets the roll-off factor for the root-raised-cosine (RRC) filter. |
|  | GetRrcFilterEnabled | Obsolete. Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power. |
|  | GetSpan | Gets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time, in seconds. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXChpAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the channel power (CHP) measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for channel power (CHP) measurement. |
|  | SetCarrierFrequency | Sets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
|  | SetCarrierIntegrationBandwidth | Sets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
|  | SetCarrierRrcFilterAlpha | Sets the roll-off factor for the root-raised-cosine (RRC) filter. |
|  | SetCarrierRrcFilterEnabled | Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. |
|  | SetDetectorPoints | Sets the number of trace points after the detector is applied. |
|  | SetDetectorType | Sets the type of detector to be used. |
|  | SetFftPadding | Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
|  | SetFftWindow | Sets the FFT window type used to reduce spectral leakage. |
|  | SetIntegrationBandwidth | Obsolete. Sets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
|  | SetMeasurementEnabled | Sets whether to enable the channel power (CHP) measurement. |
|  | SetMeasurementMode | Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCalibrationAveragingAuto | Sets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
|  | SetNoiseCalibrationAveragingCount | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. |
|  | SetNoiseCalibrationMode | Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCompensationEnabled | Sets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(String, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(String, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
|  | SetNoiseCompensationType | Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for channel power (CHP) measurement. |
|  | SetNumberOfCarriers | Sets the number of carriers. |
|  | SetRbwFilterAutoBandwidth | Sets whether the measurement computes the resolution bandwidth (RBW). |
|  | SetRbwFilterBandwidth | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
|  | SetRbwFilterBandwidthDefinition | Sets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method. |
|  | SetRbwFilterType | Sets the shape of the digital resolution bandwidth (RBW) filter. |
|  | SetRrcFilterAlpha | Obsolete. Sets the roll-off factor for the root-raised-cosine (RRC) filter. |
|  | SetRrcFilterEnabled | Obsolete. Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. |
|  | SetSpan | Sets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time, in seconds, when you set the SetSweepTimeAuto(String, RFmxSpecAnMXChpSweepTimeAuto) method to False. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |
|  | ValidateNoiseCalibrationData | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorstring parameter. |

Top

##### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a6f88844-e0d1-fd40-496c-476546c93cfa.htm language=enus -->
## TOPIC 00384: rfmxspecandotnet/html/a6f88844-e0d1-fd40-496c-476546c93cfa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a6f88844-e0d1-fd40-496c-476546c93cfa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a6f88844-e0d1-fd40-496c-476546c93cfa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeRbwFilterAutoBandwidth Method

RFmxSpecAnMXSpurConfigurationSetRangeRbwFilterAutoBandwidth Method

Sets whether the measurement computes the resolution bandwidth (RBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeRbwFilterAutoBandwidth(
	string selectorString,
	RFmxSpecAnMXSpurRbwAutoBandwidth value
)
```

```text
Public Function SetRangeRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeRBWFilterAutoBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a6fa24a5-9667-9cae-b726-90dd5e6a3bfb.htm language=enus -->
## TOPIC 00385: rfmxspecandotnet/html/a6fa24a5-9667-9cae-b726-90dd5e6a3bfb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a6fa24a5-9667-9cae-b726-90dd5e6a3bfb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a6fa24a5-9667-9cae-b726-90dd5e6a3bfb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration Class

RFmxSpecAnMXIQConfiguration Class

Provides methods to configure the I/Q measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXIQConfiguration : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXIQConfiguration
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXIQConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAcquisition | Configures the acquisition settings for the I/Q measurement. |
|  | ConfigureBandwidth | Configures the bandwidth, in hertz (Hz), for the I/Q measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAcquisitionTime | Gets the acquisition time, in seconds, for the I/Q measurement. |
|  | GetBandwidth | Gets the minimum acquisition bandwidth, in hertz (Hz), when you set the SetBandwidthAuto(String, RFmxSpecAnMXIQBandwidthAuto) method to False. |
|  | GetBandwidthAuto | Gets whether the measurement computes the minimum acquisition bandwidth. |
|  | GetDeleteRecordOnFetch | Gets whether the measurement deletes the fetched record. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether the I/Q measurement is enabled. |
|  | GetNumberOfRecords | Gets the the number of records to acquire. |
|  | GetPretriggerTime | Gets the pretrigger time, in seconds, for the I/Q measurement. |
|  | GetSampleRate | Gets the acquisition sample rate, in samples per second (S/s). |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAcquisitionTime | Sets the acquisition time, in seconds, for the I/Q measurement. |
|  | SetBandwidth | Sets the minimum acquisition bandwidth, in hertz (Hz), when you set the SetBandwidthAuto(String, RFmxSpecAnMXIQBandwidthAuto) method to False. |
|  | SetBandwidthAuto | Sets whether the measurement computes the minimum acquisition bandwidth. |
|  | SetDeleteRecordOnFetch | Sets whether the measurement deletes the fetched record. |
|  | SetMeasurementEnabled | Sets whether to enable the I/Q measurement. |
|  | SetNumberOfRecords | Sets the number of records to acquire. |
|  | SetPretriggerTime | Sets the pretrigger time, in seconds, for the I/Q measurement. |
|  | SetSampleRate | Sets the acquisition sample rate, in samples per second (S/s). |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a71666a5-7565-d4e1-aa39-f5275dbfc17c.htm language=enus -->
## TOPIC 00386: rfmxspecandotnet/html/a71666a5-7565-d4e1-aa39-f5275dbfc17c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a71666a5-7565-d4e1-aa39-f5275dbfc17c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a71666a5-7565-d4e1-aa39-f5275dbfc17c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetFrequencyConverterImageRejection Method

RFmxSpecAnMXNFConfigurationSetFrequencyConverterImageRejection Method

Sets the gain ratio of the DUT at the image frequency to that at the RF frequency. This value is expressed in dB. Refer to NF concept help for more details.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyConverterImageRejection(
	string selectorString,
	double value
)
```

```text
Public Function SetFrequencyConverterImageRejection ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the gain ratio of the DUT at the image frequency to that at the RF frequency. This value is expressed in dB. Refer to NF concept help for more details.

###### Return Value

Int32

##### Remarks

NFFrequencyConverterImageRejection

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a71d9720-ada1-6405-88eb-a2d82a14848e.htm language=enus -->
## TOPIC 00387: rfmxspecandotnet/html/a71d9720-ada1-6405-88eb-a2d82a14848e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a71d9720-ada1-6405-88eb-a2d82a14848e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a71d9720-ada1-6405-88eb-a2d82a14848e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetCalibrationLossFrequency Method

RFmxSpecAnMXNFConfigurationGetCalibrationLossFrequency Method

SetYFactorMode(String, RFmxSpecAnMXNFYFactorMode)

Calibrate

SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod)

YFactor

SetColdSourceMode(String, RFmxSpecAnMXNFColdSourceMode)

Calibrate

ColdSource

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCalibrationLossFrequency(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetCalibrationLossFrequency ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. THis value is expressed in Hz. This method is applicable only when you set the SetYFactorMode(String, RFmxSpecAnMXNFYFactorMode) method to Calibrate and set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor, or when you set the SetColdSourceMode(String, RFmxSpecAnMXNFColdSourceMode) method to Calibrate and set the NF Meas Method method to ColdSource.

###### Return Value

Int32

##### Remarks

NFCalibrationLossFrequency

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a75ff6ce-af16-b78e-8265-e72d4e294367.htm language=enus -->
## TOPIC 00388: rfmxspecandotnet/html/a75ff6ce-af16-b78e-8265-e72d4e294367.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a75ff6ce-af16-b78e-8265-e72d4e294367.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a75ff6ce-af16-b78e-8265-e72d4e294367.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetAveragingType Method

RFmxSpecAnMXIMConfigurationGetAveragingType Method

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingType(
	string selectorString,
	out RFmxSpecAnMXIMAveragingType value
)
```

```text
Public Function GetAveragingType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIMAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIMAveragingType**
  - Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement.

###### Return Value

Int32

##### Remarks

IMAveragingType

Rms

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a76af76d-7eab-78cd-06ef-2f13db6e3c17.htm language=enus -->
## TOPIC 00389: rfmxspecandotnet/html/a76af76d-7eab-78cd-06ef-2f13db6e3c17.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a76af76d-7eab-78cd-06ef-2f13db6e3c17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a76af76d-7eab-78cd-06ef-2f13db6e3c17.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetCarrierRbwFilterBandwidthDefinition Method

RFmxSpecAnMXSemConfigurationGetCarrierRbwFilterBandwidthDefinition Method

SetCarrierRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierRbwFilterBandwidthDefinition(
	string selectorString,
	out RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition value
)
```

```text
Public Function GetCarrierRbwFilterBandwidthDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition**
  - Specifies the bandwidth definition which you use to specify the value of the SetCarrierRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierRBWFilterBandwidthDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a7977c1c-1b5a-a83b-9ced-5d09e53d09ad.htm language=enus -->
## TOPIC 00390: rfmxspecandotnet/html/a7977c1c-1b5a-a83b-9ced-5d09e53d09ad.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a7977c1c-1b5a-a83b-9ced-5d09e53d09ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a7977c1c-1b5a-a83b-9ced-5d09e53d09ad.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpNoiseCompensationEnabled Enumeration

RFmxSpecAnMXChpNoiseCompensationEnabled Enumeration

SetNoiseCalibrationMode(String, RFmxSpecAnMXChpNoiseCalibrationMode)

Auto

Manual

SetMeasurementMode(String, RFmxSpecAnMXChpMeasurementMode)

Measure

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpNoiseCompensationEnabled
```

```text
Public Enumeration RFmxSpecAnMXChpNoiseCompensationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables noise compensation. |
| True | 1 | Enables noise compensation. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a7a7ed70-13d5-75b4-5d2f-1e439fd25432.htm language=enus -->
## TOPIC 00391: rfmxspecandotnet/html/a7a7ed70-13d5-75b4-5d2f-1e439fd25432.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a7a7ed70-13d5-75b4-5d2f-1e439fd25432.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a7a7ed70-13d5-75b4-5d2f-1e439fd25432.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.SetFundamentalRbwFilterBandwidth Method

RFmxSpecAnMXHarmConfigurationSetFundamentalRbwFilterBandwidth Method

Sets the resolution bandwidth (RBW) filter to be applied on the acquired signal. The bandwidth of the filter specified is applicable for fundamental signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFundamentalRbwFilterBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetFundamentalRbwFilterBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the RBW filter to be applied on the acquired signal. The bandwidth of the filter specified is applicable for fundamental signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmSetFundamentalRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a86aaf89-aa43-692f-5bfc-2d959d08f5b3.htm language=enus -->
## TOPIC 00392: rfmxspecandotnet/html/a86aaf89-aa43-692f-5bfc-2d959d08f5b3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a86aaf89-aa43-692f-5bfc-2d959d08f5b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a86aaf89-aa43-692f-5bfc-2d959d08f5b3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.BuildCarrierString2 Method

RFmxSpecAnMXBuildCarrierString2 Method

Creates the carrier string to use as the selector string with the SEM, ACP, and CHP carrier configuration or fetch properties and methods.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildCarrierString2(
	string selectorString,
	int carrierNumber
)
```

```text
Public Shared Function BuildCarrierString2 ( 
	selectorString As String,
	carrierNumber As Integer
) As String
```

###### Parameters

- **selectorString String**
  - Specifies the selector string comprising the result name. Example: "", "result::r1".
- **carrierNumber Int32**
  - Specifies the carrier number.

###### Return Value

String

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a89bbce1-5fa5-021e-aec5-007c547c8d63.htm language=enus -->
## TOPIC 00393: rfmxspecandotnet/html/a89bbce1-5fa5-021e-aec5-007c547c8d63.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a89bbce1-5fa5-021e-aec5-007c547c8d63.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a89bbce1-5fa5-021e-aec5-007c547c8d63.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMemoryPolynomialMemoryDepth Method

RFmxSpecAnMXDpdConfigurationGetMemoryPolynomialMemoryDepth Method

Gets the memory depth of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMemoryPolynomialMemoryDepth(
	string selectorString,
	out int value
)
```

```text
Public Function GetMemoryPolynomialMemoryDepth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the memory depth of the DPD polynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetMemoryPolynomialMemoryDepth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a972b156-1ed9-327a-cbd6-efa598666260.htm language=enus -->
## TOPIC 00394: rfmxspecandotnet/html/a972b156-1ed9-327a-cbd6-efa598666260.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a972b156-1ed9-327a-cbd6-efa598666260.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a972b156-1ed9-327a-cbd6-efa598666260.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetNoiseCalibrationAveragingCount Method

RFmxSpecAnMXSpectrumConfigurationGetNoiseCalibrationAveragingCount Method

SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCalibrationAveragingCount(
	string selectorString,
	out int value
)
```

```text
Public Function GetNoiseCalibrationAveragingCount ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto) method to False.

###### Return Value

Int32

##### Remarks

SpectrumNoiseCalibrationAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a98b23bf-8b31-be53-ea17-67f6da611a76.htm language=enus -->
## TOPIC 00395: rfmxspecandotnet/html/a98b23bf-8b31-be53-ea17-67f6da611a76.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a98b23bf-8b31-be53-ea17-67f6da611a76.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a98b23bf-8b31-be53-ea17-67f6da611a76.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.ConfigureUserLookupTable Method

RFmxSpecAnMXDpdApplyDpdConfigureUserLookupTable Method

SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel)

LookupTable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUserLookupTable(
	string selectorString,
	float[] lutInputPowers,
	ComplexSingle[] lutComplexGains
)
```

```text
Public Function ConfigureUserLookupTable ( 
	selectorString As String,
	lutInputPowers As Single(),
	lutComplexGains As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **lutInputPowers Single**
  - Specifies the array of lookup table power levels, in dBm.
- **lutComplexGains ComplexSingle**
  - Specifies the array of lookup table complex gain values for magnitude and phase predistortion.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgApplyDPDUserLookupTable() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a9adb38a-5383-c1b5-8be3-3cb2f7fe66bc.htm language=enus -->
## TOPIC 00396: rfmxspecandotnet/html/a9adb38a-5383-c1b5-8be3-3cb2f7fe66bc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a9adb38a-5383-c1b5-8be3-3cb2f7fe66bc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a9adb38a-5383-c1b5-8be3-3cb2f7fe66bc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetSweepTimeAuto Method

RFmxSpecAnMXSemConfigurationGetSweepTimeAuto Method

Gets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxSpecAnMXSemSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSemSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSemSweepTimeAuto**
  - Upon return, indicates whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetSweepTimeAuto() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a9b2c101-3416-1a5c-17c0-8f6d518830ec.htm language=enus -->
## TOPIC 00397: rfmxspecandotnet/html/a9b2c101-3416-1a5c-17c0-8f6d518830ec.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a9b2c101-3416-1a5c-17c0-8f6d518830ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a9b2c101-3416-1a5c-17c0-8f6d518830ec.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetTargetGainType Method

RFmxSpecAnMXDpdConfigurationGetTargetGainType Method

Gets the gain expected from the DUT after applying DPD on the input waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTargetGainType(
	string selectorString,
	out RFmxSpecAnMXDpdTargetGainType value
)
```

```text
Public Function GetTargetGainType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdTargetGainType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdTargetGainType**
  - Upon return, contains the gain expected from the DUT after applying DPD on the input waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetTargetGainType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a9dac126-a1a1-9141-c826-0e69bd3f8f05.htm language=enus -->
## TOPIC 00398: rfmxspecandotnet/html/a9dac126-a1a1-9141-c826-0e69bd3f8f05.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a9dac126-a1a1-9141-c826-0e69bd3f8f05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a9dac126-a1a1-9141-c826-0e69bd3f8f05.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetFrequencyOffsetCorrectionEnabled Method

RFmxSpecAnMXAmpmConfigurationGetFrequencyOffsetCorrectionEnabled Method

Gets the frequency offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyOffsetCorrectionEnabled(
	string selectorString,
	out RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled value
)
```

```text
Public Function GetFrequencyOffsetCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled**
  - Upon return, contains the value of frequency offset correction for the measurement.

###### Return Value

Int32

##### Remarks

AmpmFrequencyOffsetCorrectionEnabled

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/a9dcfbdd-f623-b23f-1df5-49dfe31e722c.htm language=enus -->
## TOPIC 00399: rfmxspecandotnet/html/a9dcfbdd-f623-b23f-1df5-49dfe31e722c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/a9dcfbdd-f623-b23f-1df5-49dfe31e722c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/a9dcfbdd-f623-b23f-1df5-49dfe31e722c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetMeasurementInterval Method

RFmxSpecAnMXNFConfigurationSetMeasurementInterval Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the duration for which the signals are acquired at each frequency which you specify in the SetFrequencyList(String, Double) method. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

NFMeasurementInterval

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aa116f92-3835-e20e-9785-214ffa2d7f0a.htm language=enus -->
## TOPIC 00400: rfmxspecandotnet/html/aa116f92-3835-e20e-9785-214ffa2d7f0a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aa116f92-3835-e20e-9785-214ffa2d7f0a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aa116f92-3835-e20e-9785-214ffa2d7f0a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetDeviceTemperatureTolerance Method

RFmxSpecAnMXNFConfigurationGetDeviceTemperatureTolerance Method

Gets the tolerance for device temperature beyond which the calibration data is considered invalid. This value is expressed in Celsius.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDeviceTemperatureTolerance(
	string selectorString,
	out double value
)
```

```text
Public Function GetDeviceTemperatureTolerance ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the tolerance for device temperature beyond which the calibration data is considered invalid.

###### Return Value

Int32

##### Remarks

NFDeviceTemperatureTolerance

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aa18eff1-22cd-4852-7660-298848768a3d.htm language=enus -->
## TOPIC 00401: rfmxspecandotnet/html/aa18eff1-22cd-4852-7660-298848768a3d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aa18eff1-22cd-4852-7660-298848768a3d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aa18eff1-22cd-4852-7660-298848768a3d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetIntermodEnabled Method

RFmxSpecAnMXIMConfigurationSetIntermodEnabled Method

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIntermodEnabled(
	string selectorString,
	RFmxSpecAnMXIMIntermodEnabled value
)
```

```text
Public Function SetIntermodEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXIMIntermodEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXIMIntermodEnabled**
  - Specifies whether to enable an intermod for the IM measurement. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMIntermodEnabled

True

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aa2ea020-b3f7-1ead-b81b-679c38632586.htm language=enus -->
## TOPIC 00402: rfmxspecandotnet/html/aa2ea020-b3f7-1ead-b81b-679c38632586.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aa2ea020-b3f7-1ead-b81b-679c38632586.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aa2ea020-b3f7-1ead-b81b-679c38632586.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.GetHarmonicEnabled Method

RFmxSpecAnMXHarmConfigurationGetHarmonicEnabled Method

Gets whether a particular harmonic for measurement is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHarmonicEnabled(
	string selectorString,
	out RFmxSpecAnMXHarmHarmonicEnabled value
)
```

```text
Public Function GetHarmonicEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXHarmHarmonicEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the harmonic number. Example: "harmonic0". You can use the BuildHarmonicString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXHarmHarmonicEnabled**
  - Upon return, indicates whether a particular harmonic for measurement is enabled.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmGetHarmonicEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aa827cc9-f011-d772-fe3c-6441ab8c1b02.htm language=enus -->
## TOPIC 00403: rfmxspecandotnet/html/aa827cc9-f011-d772-fe3c-6441ab8c1b02.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aa827cc9-f011-d772-fe3c-6441ab8c1b02.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aa827cc9-f011-d772-fe3c-6441ab8c1b02.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetStartFrequency Method

RFmxSpecAnMXSemConfigurationSetOffsetStartFrequency Method

ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition)

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the start frequency, in Hz, of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetStartFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aa988093-49e0-e02c-806b-9a52deea9cc4.htm language=enus -->
## TOPIC 00404: rfmxspecandotnet/html/aa988093-49e0-e02c-806b-9a52deea9cc4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aa988093-49e0-e02c-806b-9a52deea9cc4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aa988093-49e0-e02c-806b-9a52deea9cc4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.GetAllTracesEnabled Method

RFmxSpecAnMXCcdfConfigurationGetAllTracesEnabled Method

Gets whether the traces to be stored and retrieved after performing the complementary cumulative distribution function (CCDF) measurement are enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - if the traces to be stored and retrieved after performing the CCDF measurement are enabled; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFGetAllTracesEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aac5dac7-f4d3-cc2a-1b85-675388e6de22.htm language=enus -->
## TOPIC 00405: rfmxspecandotnet/html/aac5dac7-f4d3-cc2a-1b85-675388e6de22.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aac5dac7-f4d3-cc2a-1b85-675388e6de22.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aac5dac7-f4d3-cc2a-1b85-675388e6de22.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.GetThresholdEnabled Method

RFmxSpecAnMXCcdfConfigurationGetThresholdEnabled Method

Gets whether thresholding of the acquired samples to be used for the complementary cumulative distribution function (CCDF) measurement is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetThresholdEnabled(
	string selectorString,
	out RFmxSpecAnMXCcdfThresholdEnabled value
)
```

```text
Public Function GetThresholdEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXCcdfThresholdEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXCcdfThresholdEnabled**
  - Upon return, indicates whether thresholding of the acquired samples to be used for the CCDF measurement is enabled.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFGetThresholdEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/aac86ee7-f8de-c1eb-f2a2-07ae734b19de.htm language=enus -->
## TOPIC 00406: rfmxspecandotnet/html/aac86ee7-f8de-c1eb-f2a2-07ae734b19de.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/aac86ee7-f8de-c1eb-f2a2-07ae734b19de.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/aac86ee7-f8de-c1eb-f2a2-07ae734b19de.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Commit Method

RFmxSpecAnMXCommit Method

Commits settings to the hardware. Calling this method is optional. RFmxSpecAn commits settings to the hardware when you call the RFmxInstrMX Initiate
 or any of the measurement Read methods.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

##### Remarks

This method maps to the RFmxSpecAn_Commit() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ab030efd-75d1-c32d-eb9b-8302cecc9199.htm language=enus -->
## TOPIC 00407: rfmxspecandotnet/html/ab030efd-75d1-c32d-eb9b-8302cecc9199.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ab030efd-75d1-c32d-eb9b-8302cecc9199.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ab030efd-75d1-c32d-eb9b-8302cecc9199.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.GetUpperOffsetAbsolutePower Method

RFmxSpecAnMXAcpResultsGetUpperOffsetAbsolutePower Method

Gets the upper offset channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the upper offset channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetAbsolutePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ab0386bb-5d4e-dd68-e8f0-cfb167f3b48f.htm language=enus -->
## TOPIC 00408: rfmxspecandotnet/html/ab0386bb-5d4e-dd68-e8f0-cfb167f3b48f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ab0386bb-5d4e-dd68-e8f0-cfb167f3b48f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ab0386bb-5d4e-dd68-e8f0-cfb167f3b48f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtResults Methods

RFmxSpecAnMXPavtResults Methods

The [RFmxSpecAnMXPavtResults](b8d816aa-f528-e784-21d1-754e0d869e1d.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchAmplitudeTrace | Fetches the amplitude trace for the measurement. |
|  | FetchPhaseAndAmplitude | Fetches the mean values of phase and amplitude of the segment. Use "segment(n)" as the selector string to read results from this method. |
|  | FetchPhaseAndAmplitudeArray | Fetches an array of mean values of phase and amplitude of the segments. |
|  | FetchPhaseTrace | Fetches the phase trace for the measurement. |
|  | GetFrequencyErrorMean | Gets the mean frequency error of the segment. This value is expressed in Hz |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeanAbsoluteAmplitude | Gets the mean absolute amplitude of the segment. This value is expressed in dBm. |
|  | GetMeanAbsolutePhase | Gets the mean absolute phase of the segment. This value is expressed in degrees. |
|  | GetMeanRelativeAmplitude | Gets the mean amplitude of the segment relative to the first segment of the measurement. This value is expressed in dB. Mean Relative Amplitude = ai - a0 ai is the absolute amplitude of the segment i. This value is expressed in dBm. |
|  | GetMeanRelativePhase | Gets the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXPavtResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ab0e6f0b-adf8-be63-a944-cd104e6f2e97.htm language=enus -->
## TOPIC 00409: rfmxspecandotnet/html/ab0e6f0b-adf8-be63-a944-cd104e6f2e97.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ab0e6f0b-adf8-be63-a944-cd104e6f2e97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ab0e6f0b-adf8-be63-a944-cd104e6f2e97.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNoiseCalibrationAveragingAuto Method

RFmxSpecAnMXAcpConfigurationSetNoiseCalibrationAveragingAuto Method

Sets whether RFmx automatically computes the averaging count used for instrument noise calibration.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCalibrationAveragingAuto(
	string selectorString,
	RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto value
)
```

```text
Public Function SetNoiseCalibrationAveragingAuto ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto**
  - Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

###### Return Value

Int32

##### Remarks

AcpNoiseCalibrationAveragingAuto

True

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ab121bdd-c8b1-2169-24af-0982513d8643.htm language=enus -->
## TOPIC 00410: rfmxspecandotnet/html/ab121bdd-c8b1-2169-24af-0982513d8643.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ab121bdd-c8b1-2169-24af-0982513d8643.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ab121bdd-c8b1-2169-24af-0982513d8643.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetCarrierBandwidth Method

RFmxSpecAnMXAmpmConfigurationGetCarrierBandwidth Method

SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AmpmCarrierBandwidth

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ab579893-31f4-3786-f7da-fa5e2c548719.htm language=enus -->
## TOPIC 00411: rfmxspecandotnet/html/ab579893-31f4-3786-f7da-fa5e2c548719.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ab579893-31f4-3786-f7da-fa5e2c548719.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ab579893-31f4-3786-f7da-fa5e2c548719.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetFftOverlapType Method

RFmxSpecAnMXSpectrumConfigurationGetFftOverlapType Method

SpectrumMeasurementMethod

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftOverlapType(
	string selectorString,
	out RFmxSpecAnMXSpectrumFftOverlapType value
)
```

```text
Public Function GetFftOverlapType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumFftOverlapType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumFftOverlapType**
  - Upon return, contains the overlap type when you set the SpectrumMeasurementMethod method to SequentialFft.

###### Return Value

Int32

##### Remarks

SpectrumFftOverlapType

Rms

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ac89eba0-53fe-18a4-9945-6bff9dc7fb60.htm language=enus -->
## TOPIC 00412: rfmxspecandotnet/html/ac89eba0-53fe-18a4-9945-6bff9dc7fb60.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ac89eba0-53fe-18a4-9945-6bff9dc7fb60.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ac89eba0-53fe-18a4-9945-6bff9dc7fb60.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.GetAveragingEnabled Method

RFmxSpecAnMXTxpConfigurationGetAveragingEnabled Method

Gets whether averaging for the transmit power (TXP) measurement is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxSpecAnMXTxpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXTxpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXTxpAveragingEnabled**
  - Upon return, indicates whether averaging for the TXP measurement is enabled.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPGetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ac99d833-2474-a66d-70a4-62207c753718.htm language=enus -->
## TOPIC 00413: rfmxspecandotnet/html/ac99d833-2474-a66d-70a4-62207c753718.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ac99d833-2474-a66d-70a4-62207c753718.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ac99d833-2474-a66d-70a4-62207c753718.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMeasurementInterval Method

RFmxSpecAnMXDpdConfigurationGetMeasurementInterval Method

Gets the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/af227b63-71e3-c160-82e7-a95c3b21ff6f.htm language=enus -->
## TOPIC 00414: rfmxspecandotnet/html/af227b63-71e3-c160-82e7-a95c3b21ff6f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/af227b63-71e3-c160-82e7-a95c3b21ff6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/af227b63-71e3-c160-82e7-a95c3b21ff6f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwResults.GetStopFrequency Method

RFmxSpecAnMXObwResultsGetStopFrequency Method

Gets the stop frequency, in hertz (Hz), of the occupied bandwidth (OBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the stop frequency, in Hz, of the OBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWGetResultsStopFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/af36350c-2110-5c37-c243-86f1d1cbb1ff.htm language=enus -->
## TOPIC 00415: rfmxspecandotnet/html/af36350c-2110-5c37-c243-86f1d1cbb1ff.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/af36350c-2110-5c37-c243-86f1d1cbb1ff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/af36350c-2110-5c37-c243-86f1d1cbb1ff.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNF Methods

RFmxSpecAnMXNF Methods

The [RFmxSpecAnMXNF](e6e5e4dc-8918-8ca4-9486-ff33dd491844.htm) type exposes the following members.

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

RFmxSpecAnMXNF Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm language=enus -->
## TOPIC 00416: rfmxspecandotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.InstrMX Namespace

NationalInstruments.RFmx.InstrMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxSpecAnMXExtension | Provides extension methods to create SpecAn signal configuration. These methods are added to RFmxInstrMX class. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b0b67bef-f265-d0e4-165f-f954d58fbbdc.htm language=enus -->
## TOPIC 00417: rfmxspecandotnet/html/b0b67bef-f265-d0e4-165f-f954d58fbbdc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b0b67bef-f265-d0e4-165f-f954d58fbbdc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b0b67bef-f265-d0e4-165f-f954d58fbbdc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.ConfigureRangeRelativeAttenuationArray Method

RFmxSpecAnMXSpurConfigurationConfigureRangeRelativeAttenuationArray Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRangeRelativeAttenuationArray(
	string selectorString,
	double[] relativeAttenuation
)
```

```text
Public Function ConfigureRangeRelativeAttenuationArray ( 
	selectorString As String,
	relativeAttenuation As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **relativeAttenuation Double**
  - Specifies an array of attenuation values, in dB, relative to the value of the GetExternalAttenuation(String, Double) method. Use this method to compensate for the variations in external attenuation when offset channels are spread wide in frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurCfgRangeRelativeAttenuationArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b0f57509-0eb3-b88d-9c15-2514c0f00f6d.htm language=enus -->
## TOPIC 00418: rfmxspecandotnet/html/b0f57509-0eb3-b88d-9c15-2514c0f00f6d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b0f57509-0eb3-b88d-9c15-2514c0f00f6d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b0f57509-0eb3-b88d-9c15-2514c0f00f6d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetRelativeLimitStop Method

RFmxSpecAnMXSemConfigurationSetOffsetRelativeLimitStop Method

SetOffsetRelativeLimitMode(String, RFmxSpecAnMXSemOffsetRelativeLimitMode)

Couple

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetRelativeLimitStop(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetRelativeLimitStop ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the relative power limit, in dB, corresponding to the end of the offset segment.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetRelativeLimitStop() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b119f23f-9565-7c50-14b7-f3e544ed090f.htm language=enus -->
## TOPIC 00419: rfmxspecandotnet/html/b119f23f-9565-7c50-14b7-f3e544ed090f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b119f23f-9565-7c50-14b7-f3e544ed090f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b119f23f-9565-7c50-14b7-f3e544ed090f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetThresholdLevel Method

RFmxSpecAnMXAmpmConfigurationGetThresholdLevel Method

Gets either the relative or absolute threshold power level.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetThresholdLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetThresholdLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains either the relative or absolute threshold power level.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetThresholdLevel() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b1348e4f-7ceb-e9b4-62a0-508440d1ed73.htm language=enus -->
## TOPIC 00420: rfmxspecandotnet/html/b1348e4f-7ceb-e9b4-62a0-508440d1ed73.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b1348e4f-7ceb-e9b4-62a0-508440d1ed73.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b1348e4f-7ceb-e9b4-62a0-508440d1ed73.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.GetFftWindow Method

RFmxSpecAnMXObwConfigurationGetFftWindow Method

Gets the FFT window type used to reduce spectral leakage.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftWindow(
	string selectorString,
	out RFmxSpecAnMXObwFftWindow value
)
```

```text
Public Function GetFftWindow ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXObwFftWindow
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwFftWindow**
  - Upon return, contains the FFT window type used to reduce spectral leakage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWGetFFTWindow() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b1389626-6747-d028-b0e7-ef2673fefec1.htm language=enus -->
## TOPIC 00421: rfmxspecandotnet/html/b1389626-6747-d028-b0e7-ef2673fefec1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b1389626-6747-d028-b0e7-ef2673fefec1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b1389626-6747-d028-b0e7-ef2673fefec1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetRangeDefinition Method

RFmxSpecAnMXPhaseNoiseConfigurationGetRangeDefinition Method

Gets how the measurement computes offset subranges.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeDefinition(
	string selectorString,
	out RFmxSpecAnMXPhaseNoiseRangeDefinition value
)
```

```text
Public Function GetRangeDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXPhaseNoiseRangeDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPhaseNoiseRangeDefinition**
  - Upon return, contains how the measurement computes offset subranges.

###### Return Value

Int32

##### Remarks

PhaseNoiseRangeDefinition

Auto

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b15434ad-4950-3cd8-864a-9511e42d89f6.htm language=enus -->
## TOPIC 00422: rfmxspecandotnet/html/b15434ad-4950-3cd8-864a-9511e42d89f6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b15434ad-4950-3cd8-864a-9511e42d89f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b15434ad-4950-3cd8-864a-9511e42d89f6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerResults.NextPeak Method

RFmxSpecAnMXMarkerResultsNextPeak Method

Moves the marker to the next highest, next left, or next right peak above the threshold on the configured trace.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int NextPeak(
	string selectorString,
	RFmxSpecAnMXMarkerNextPeak nextPeak,
	out bool nextPeakFound
)
```

```text
Public Function NextPeak ( 
	selectorString As String,
	nextPeak As RFmxSpecAnMXMarkerNextPeak,
	<OutAttribute> ByRef nextPeakFound As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and marker number. Example: "marker0", "result::r1/marker0". You can use the BuildMarkerString2(String, Int32) method to build the selector string.
- **nextPeak RFmxSpecAnMXMarkerNextPeak**
  - Specifies the next peak on the trace.
- **nextPeakFound Boolean**
  - Upon return, indicates whether the next peak has been found on the trace.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_MarkerNextPeak() function in C.

##### See Also

###### Reference

RFmxSpecAnMXMarkerResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b16731a1-51fe-222c-d826-bdaf73a77c18.htm language=enus -->
## TOPIC 00423: rfmxspecandotnet/html/b16731a1-51fe-222c-d826-bdaf73a77c18.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b16731a1-51fe-222c-d826-bdaf73a77c18.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b16731a1-51fe-222c-d826-bdaf73a77c18.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetFftPadding Method

RFmxSpecAnMXSpectrumConfigurationGetFftPadding Method

Gets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftPadding(
	string selectorString,
	out double value
)
```

```text
Public Function GetFftPadding ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumGetFFTPadding() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b1701bc6-3107-c100-4513-6c6b5bfb20e5.htm language=enus -->
## TOPIC 00424: rfmxspecandotnet/html/b1701bc6-3107-c100-4513-6c6b5bfb20e5.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b1701bc6-3107-c100-4513-6c6b5bfb20e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b1701bc6-3107-c100-4513-6c6b5bfb20e5.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetLimitFailMask Method

RFmxSpecAnMXSemConfigurationGetOffsetLimitFailMask Method

Gets the criteria to determine the measurement fail status.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetLimitFailMask(
	string selectorString,
	out RFmxSpecAnMXSemOffsetLimitFailMask value
)
```

```text
Public Function GetOffsetLimitFailMask ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSemOffsetLimitFailMask
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetLimitFailMask**
  - Upon return, contains the criteria to determine the measurement fail status.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetLimitFailMask() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b179f39a-18c5-df82-856b-323acf508c77.htm language=enus -->
## TOPIC 00425: rfmxspecandotnet/html/b179f39a-18c5-df82-856b-323acf508c77.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b179f39a-18c5-df82-856b-323acf508c77.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b179f39a-18c5-df82-856b-323acf508c77.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetSweepTimeInterval Method

RFmxSpecAnMXIMConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxSpecAnMXIMSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxSpecAnMXIMSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

IMSweepTimeInterval

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b1810edc-f28d-8b37-0d04-4671a163c61a.htm language=enus -->
## TOPIC 00426: rfmxspecandotnet/html/b1810edc-f28d-8b37-0d04-4671a163c61a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b1810edc-f28d-8b37-0d04-4671a163c61a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b1810edc-f28d-8b37-0d04-4671a163c61a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.FetchRangeAbsoluteLimitTrace Method

RFmxSpecAnMXSpurResultsFetchRangeAbsoluteLimitTrace Method

Fetches the absolute limit line used in the range.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRangeAbsoluteLimitTrace(
	string selectorString,
	double timeout,
	ref Spectrum<float> absoluteLimit
)
```

```text
Public Function FetchRangeAbsoluteLimitTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef absoluteLimit As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and range number. Example: "range0", "result::r1/range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absoluteLimit SpectrumSingle**
  - Upon return, contains the absolute limit trace, in dBm, used for the channel.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurFetchRangeAbsoluteLimitTrace() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b1aa2537-2812-ed27-9666-7e2818f2c01e.htm language=enus -->
## TOPIC 00427: rfmxspecandotnet/html/b1aa2537-2812-ed27-9666-7e2818f2c01e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b1aa2537-2812-ed27-9666-7e2818f2c01e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b1aa2537-2812-ed27-9666-7e2818f2c01e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.ConfigureThreshold Method

RFmxSpecAnMXCcdfConfigurationConfigureThreshold Method

Configures the threshold level for the samples that need to be considered for the complementary cumulative distribution function (CCDF) measurement. Enable the threshold when analyzing burst signals or signals with dead time.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureThreshold(
	string selectorString,
	RFmxSpecAnMXCcdfThresholdEnabled thresholdEnabled,
	double thresholdLevel,
	RFmxSpecAnMXCcdfThresholdType thresholdType
)
```

```text
Public Function ConfigureThreshold ( 
	selectorString As String,
	thresholdEnabled As RFmxSpecAnMXCcdfThresholdEnabled,
	thresholdLevel As Double,
	thresholdType As RFmxSpecAnMXCcdfThresholdType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **thresholdEnabled RFmxSpecAnMXCcdfThresholdEnabled**
  - Specifies whether to enable thresholding of the acquired samples to be used for the measurement.
- **thresholdLevel Double**
  - Specifies either the relative or absolute threshold power level based on the value of the SetThresholdType(String, RFmxSpecAnMXCcdfThresholdType) method.
- **thresholdType RFmxSpecAnMXCcdfThresholdType**
  - Specifies the reference for the power level used for thresholding.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFCfgThreshold() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b1cbb535-a004-5c4c-f039-e56147d19ec9.htm language=enus -->
## TOPIC 00428: rfmxspecandotnet/html/b1cbb535-a004-5c4c-f039-e56147d19ec9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b1cbb535-a004-5c4c-f039-e56147d19ec9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b1cbb535-a004-5c4c-f039-e56147d19ec9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxp Properties

RFmxSpecAnMXTxp Properties

The [RFmxSpecAnMXTxp](98baa105-9ec7-19c4-e109-b3cdfc846025.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXTxpConfiguration instance that allows configuration of transmit power (TXP) measurement. |
|  | Results | Gets the RFmxSpecAnMXTxpResults instance that provides methods to retrieve transmit power (TXP) measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXTxp Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b5651fc5-a552-820c-14cc-a1410eb6cbe4.htm language=enus -->
## TOPIC 00429: rfmxspecandotnet/html/b5651fc5-a552-820c-14cc-a1410eb6cbe4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b5651fc5-a552-820c-14cc-a1410eb6cbe4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b5651fc5-a552-820c-14cc-a1410eb6cbe4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetHeadroom Method

RFmxSpecAnMXDpdApplyDpdGetHeadroom Method

**Note: This API is now obsolete.**

Gets the headroom, in dB, to apply to the predistorted waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This property/enum has been deprecated")]
public int GetHeadroom(
	string selectorString,
	out double value
)
```

```text
<ObsoleteAttribute("This property/enum has been deprecated")>
Public Function GetHeadroom ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the headroom, in dB, to apply to the predistorted waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDHeadroom() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b5ff4eda-57e8-698f-6ce6-c24e75f57c05.htm language=enus -->
## TOPIC 00430: rfmxspecandotnet/html/b5ff4eda-57e8-698f-6ce6-c24e75f57c05.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b5ff4eda-57e8-698f-6ce6-c24e75f57c05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b5ff4eda-57e8-698f-6ce6-c24e75f57c05.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwRbwFilterBandwidthDefinition Enumeration

RFmxSpecAnMXObwRbwFilterBandwidthDefinition Enumeration

SetRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXObwRbwFilterBandwidthDefinition
```

```text
Public Enumeration RFmxSpecAnMXObwRbwFilterBandwidthDefinition
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| BandwidthDefinition3dB | 0 | Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the SetRbwFilterType(String, RFmxSpecAnMXObwRbwFilterType) method to FftBased, RBW is the 3 dB bandwidth of the window specified by the SetFftWindow(String, RFmxSpecAnMXObwFftWindow) method. |
| BandwidthDefinitionBinWidth | 2 | Defines the RBW in terms of the bin width of the spectrum computed using an FFT when you set the SetRbwFilterType(String, RFmxSpecAnMXObwRbwFilterType) method to FftBased. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b63a0de2-05be-3a8f-6126-2258304791f2.htm language=enus -->
## TOPIC 00431: rfmxspecandotnet/html/b63a0de2-05be-3a8f-6126-2258304791f2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b63a0de2-05be-3a8f-6126-2258304791f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b63a0de2-05be-3a8f-6126-2258304791f2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SetCenterFrequency Method

RFmxSpecAnMXSetCenterFrequency Method

Sets the expected carrier frequency, in hertz (Hz), of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the expected carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SetCenterFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b65ebadf-a199-26a9-ffdd-39341685a7ae.htm language=enus -->
## TOPIC 00432: rfmxspecandotnet/html/b65ebadf-a199-26a9-ffdd-39341685a7ae.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b65ebadf-a199-26a9-ffdd-39341685a7ae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b65ebadf-a199-26a9-ffdd-39341685a7ae.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.GetCfrMethod Method

RFmxSpecAnMXDpdPreDpdGetCfrMethod Method

DpdPreDpdCfrEnabled

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrMethod(
	string selectorString,
	out RFmxSpecAnMXDpdPreDpdCfrMethod value
)
```

```text
Public Function GetCfrMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdPreDpdCfrMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdPreDpdCfrMethod**
  - Upon return, contains the method used to perform crest factor reduction (CFR) when you set the DpdPreDpdCfrEnabled method to True. Refer to DPD concept topic for more information about CFR methods.

###### Return Value

Int32

##### Remarks

DpdPreDpdCfrMethod

Clipping

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b703e38f-b41c-3a7e-4120-91794eb69040.htm language=enus -->
## TOPIC 00433: rfmxspecandotnet/html/b703e38f-b41c-3a7e-4120-91794eb69040.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b703e38f-b41c-3a7e-4120-91794eb69040.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b703e38f-b41c-3a7e-4120-91794eb69040.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.SetHarmonicBandwidth Method

RFmxSpecAnMXHarmConfigurationSetHarmonicBandwidth Method

SetAutoSetupEnabled(String, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled)

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetHarmonicBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetHarmonicBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the harmonic number. Example: "harmonic0". You can use the BuildHarmonicString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the resolution bandwidth, in hertz (Hz), for the harmonic. The value set by this method is not used if you set the SetAutoSetupEnabled(String, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmSetHarmonicBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b7431c5e-5494-f6aa-607e-9f33cb20e5df.htm language=enus -->
## TOPIC 00434: rfmxspecandotnet/html/b7431c5e-5494-f6aa-607e-9f33cb20e5df.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b7431c5e-5494-f6aa-607e-9f33cb20e5df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b7431c5e-5494-f6aa-607e-9f33cb20e5df.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmReferencePowerType Enumeration

RFmxSpecAnMXAmpmReferencePowerType Enumeration

Specifies the reference power used for AM to AM and AM to PM traces.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAmpmReferencePowerType
```

```text
Public Enumeration RFmxSpecAnMXAmpmReferencePowerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Input | 0 | The instantaneous powers at the input port of device under test (DUT) forms the x-axis of AM to AM and AM to PM traces. |
| Output | 1 | The instantaneous powers at the output port of DUT forms the x-axis of AM to AM and AM to PM traces. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b7dd47db-15ce-7623-cf13-674b2b5beb6a.htm language=enus -->
## TOPIC 00435: rfmxspecandotnet/html/b7dd47db-15ce-7623-cf13-674b2b5beb6a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b7dd47db-15ce-7623-cf13-674b2b5beb6a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b7dd47db-15ce-7623-cf13-674b2b5beb6a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoise.Configuration Property

RFmxSpecAnMXPhaseNoiseConfiguration Property

RFmxSpecAnMXPhaseNoiseConfiguration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXPhaseNoiseConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxSpecAnMXPhaseNoiseConfiguration
	Get
```

###### Property Value

RFmxSpecAnMXPhaseNoiseConfiguration

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoise Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b7ebefa9-446b-5f93-512e-eaefa061c3c8.htm language=enus -->
## TOPIC 00436: rfmxspecandotnet/html/b7ebefa9-446b-5f93-512e-eaefa061c3c8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b7ebefa9-446b-5f93-512e-eaefa061c3c8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b7ebefa9-446b-5f93-512e-eaefa061c3c8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.ConfigureRbwFilter Method

RFmxSpecAnMXIMConfigurationConfigureRbwFilter Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRbwFilter(
	string selectorString,
	RFmxSpecAnMXIMRbwFilterAutoBandwidth rbwAuto,
	double rbw,
	RFmxSpecAnMXIMRbwFilterType rbwFilterType
)
```

```text
Public Function ConfigureRbwFilter ( 
	selectorString As String,
	rbwAuto As RFmxSpecAnMXIMRbwFilterAutoBandwidth,
	rbw As Double,
	rbwFilterType As RFmxSpecAnMXIMRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rbwAuto RFmxSpecAnMXIMRbwFilterAutoBandwidth**
  - Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Measurements topic for more details on RBW and sweep time.
- **rbw Double**
  - Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz.
- **rbwFilterType RFmxSpecAnMXIMRbwFilterType**
  - Specifies the response of the digital RBW filter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b81711e1-f86e-15f2-f04d-f3bf02ce639c.htm language=enus -->
## TOPIC 00437: rfmxspecandotnet/html/b81711e1-f86e-15f2-f04d-f3bf02ce639c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b81711e1-f86e-15f2-f04d-f3bf02ce639c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b81711e1-f86e-15f2-f04d-f3bf02ce639c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration Class

RFmxSpecAnMXPhaseNoiseConfiguration Class

Provides methods to configure the PhaseNoise measurement

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXPhaseNoiseConfiguration : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXPhaseNoiseConfiguration
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXPhaseNoiseConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAutoRange | Configures the offset range and the RBW percentage when you set the SetRangeDefinition(String, RFmxSpecAnMXPhaseNoiseRangeDefinition) method to Auto. |
|  | ConfigureAveragingMultiplier | Configures the averaging multiplier. |
|  | ConfigureCancellation | Configures phase noise cancellation for the measurement. |
|  | ConfigureIntegratedNoise | Configures the integrated noise ranges. The smoothed log plot trace is used when computing integrated measurements. |
|  | ConfigureNumberOfRanges | Configures the number of offset ranges when you set the SetRangeDefinition(String, RFmxSpecAnMXPhaseNoiseRangeDefinition) method to Manual. |
|  | ConfigureRangeArray | Configures an array of the offset range, RBW percentage and averaging count when you set the SetRangeDefinition(String, RFmxSpecAnMXPhaseNoiseRangeDefinition) method to Manual. |
|  | ConfigureRangeDefinition | Specifies how the measurement computes offset subranges. |
|  | ConfigureSmoothing | Configures the smoothing type and smoothing percentage used to smoothen the measured log plot trace. |
|  | ConfigureSpotNoiseFrequencyList | Configures a list of frequencies at which the phase noise values are to be read using the smoothed log plot trace. |
|  | ConfigureSpurRemoval | Configures enabling or disabling of the spur removal and the peak excursion to use when spur removal is enabled. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the Phase Noise measurement. |
|  | GetAveragingMultiplier | Gets the factor by which you increase the averaging count for each range. This setting applies to both Auto and Manual range definitions. |
|  | GetCancellationEnabled | Gets whether to enable or disable the phase noise cancellation. Refer to the Phase Noise topic for more information on phase noise cancellation. |
|  | GetCancellationFrequency | Gets an array of frequency offsets where the reference phase noise has been measured. |
|  | GetCancellationReferencePhaseNoise | Gets an array of reference phase noise at the frequency offsets. |
|  | GetCancellationThreshold | Gets the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed. |
|  | GetFftWindow | Gets the FFT window to use. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIntegratedNoiseRangeDefinition | Gets the frequency range for integrated noise measurements. |
|  | GetIntegratedNoiseStartFrequency | Gets an array of the start frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom. |
|  | GetIntegratedNoiseStopFrequency | Gets an array of the stop frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom. |
|  | GetMeasurementEnabled | Gets whether to enable the phase noise measurement. |
|  | GetNumberOfRanges | Gets the number of manual ranges. |
|  | GetRangeAveragingCount | Gets the averaging count for the specified range. |
|  | GetRangeDefinition | Gets how the measurement computes offset subranges. |
|  | GetRangeRbwPercentage | Gets the RBW as a percentage of the PhaseNoise Range Start Freq method of the specified subrange when you set the PhaseNoise Range Definition method to Manual. |
|  | GetRangeStartFrequency | Gets the start offset frequency for the specified range. |
|  | GetRangeStopFrequency | Gets the stop offset frequency for the specified range. |
|  | GetRbwPercentage | Gets the RBW as a percentage of the start frequency of each subrange when you set the Phase Noise Range Definition property to Auto. |
|  | GetSmoothingPercentage | Gets the number of trace points to use in the moving average filter as a percentage of total number of points in the log plot trace. |
|  | GetSmoothingType | Gets the smoothing type used to smoothen the log plot trace. |
|  | GetSpotNoiseFrequencyList | Gets an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. |
|  | GetSpurRemovalEnabled | Gets whether to remove spurs from the log plot trace. |
|  | GetSpurRemovalPeakExcursion | Gets the peak excursion to be used when spur detection is performed. Refer to the Marker topic for more information on peak excursion. |
|  | GetStartFrequency | Gets the start offset frequency. |
|  | GetStopFrequency | Gets the stop offset frequency. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the Phase Noise measurement. |
|  | SetAveragingMultiplier | Sets the factor by which you increase the averaging count for each range. This setting applies to both Auto and Manual range definitions. |
|  | SetCancellationEnabled | Sets whether to enable or disable the phase noise cancellation. Refer to the Phase Noise topic for more information on phase noise cancellation. |
|  | SetCancellationFrequency | Sets an array of frequency offsets where the reference phase noise has been measured. |
|  | SetCancellationReferencePhaseNoise | Sets an array of reference phase noise at the frequency offsets. |
|  | SetCancellationThreshold | Sets the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed. |
|  | SetFftWindow | Sets the FFT window to use. |
|  | SetIntegratedNoiseRangeDefinition | Sets the frequency range for integrated noise measurements. |
|  | SetIntegratedNoiseStartFrequency | Sets an array of the start offset frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom. |
|  | SetIntegratedNoiseStopFrequency | Sets an array of the stop offset frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom. |
|  | SetMeasurementEnabled | Sets whether to enable the phase noise measurement. |
|  | SetNumberOfRanges | Sets the number of manual ranges. |
|  | SetRangeAveragingCount | Sets the averaging count for the specified range. |
|  | SetRangeDefinition | Sets how the measurement computes offset subranges. |
|  | SetRangeRbwPercentage | Sets the RBW as a percentage of the PhaseNoise Range Start Freq method of the specified subrange when you set the PhaseNoise Range Definition method to Manual. |
|  | SetRangeStartFrequency | Sets the start offset frequency for the specified range. |
|  | SetRangeStopFrequency | Sets the stop frequency for the specified range. |
|  | SetRbwPercentage | Sets the RBW as a percentage of the PhaseNoise Range Start Freq method of the specified subrange when you set the PhaseNoise Range Definition method to Manual. |
|  | SetSmoothingPercentage | Sets the number of trace points to use in the moving average filter as a percentage of total number of points in the log plot trace. |
|  | SetSmoothingType | Sets the smoothing type used to smoothen a log plot trace. |
|  | SetSpotNoiseFrequencyList | Sets an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. |
|  | SetSpurRemovalEnabled | Sets whether to remove spurs from the log plot trace. |
|  | SetSpurRemovalPeakExcursion | Sets the peak excursion to be used when spur detection is performed. Refer to the Marker topic for more information on peak excursion. |
|  | SetStartFrequency | Sets the start offset frequency. |
|  | SetStopFrequency | Sets the stop offset frequency. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b8234c6a-11f7-50dd-e22f-04caf9cb5588.htm language=enus -->
## TOPIC 00438: rfmxspecandotnet/html/b8234c6a-11f7-50dd-e22f-04caf9cb5588.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b8234c6a-11f7-50dd-e22f-04caf9cb5588.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b8234c6a-11f7-50dd-e22f-04caf9cb5588.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.GetNumberOfAnalysisThreads Method

RFmxSpecAnMXFcntConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for frequency count (Fcnt) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the maximum number of threads used for parallelism for Fcnt measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b84ca6a7-c0ff-2dc0-e239-68f3ac17df5b.htm language=enus -->
## TOPIC 00439: rfmxspecandotnet/html/b84ca6a7-c0ff-2dc0-e239-68f3ac17df5b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b84ca6a7-c0ff-2dc0-e239-68f3ac17df5b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b84ca6a7-c0ff-2dc0-e239-68f3ac17df5b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpAveragingType Enumeration

RFmxSpecAnMXAcpAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpAveragingType
```

```text
Public Enumeration RFmxSpecAnMXAcpAveragingType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithm scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b8726418-c895-4ded-2fe0-d0dde4b9d07f.htm language=enus -->
## TOPIC 00440: rfmxspecandotnet/html/b8726418-c895-4ded-2fe0-d0dde4b9d07f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b8726418-c895-4ded-2fe0-d0dde4b9d07f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b8726418-c895-4ded-2fe0-d0dde4b9d07f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetAMToAMCurveFitOrder Method

RFmxSpecAnMXAmpmConfigurationSetAMToAMCurveFitOrder Method

Sets the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAMToAMCurveFitOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetAMToAMCurveFitOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Contains the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMSetAMToAMCurveFitOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b9440fb7-47c6-d817-9323-40fc6fa57677.htm language=enus -->
## TOPIC 00441: rfmxspecandotnet/html/b9440fb7-47c6-d817-9323-40fc6fa57677.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b9440fb7-47c6-d817-9323-40fc6fa57677.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b9440fb7-47c6-d817-9323-40fc6fa57677.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetLowerOffsetMarginFrequency Method

RFmxSpecAnMXSemResultsGetLowerOffsetMarginFrequency Method

Gets the frequency, in hertz (Hz), at which the margin occurred in the lower (negative) offset segment.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetMarginFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetMarginFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency, in hertz (Hz), at which the margin occurred in the lower (negative) offset segment.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetMarginFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b959f278-bb10-fda1-35b0-971617aec5f9.htm language=enus -->
## TOPIC 00442: rfmxspecandotnet/html/b959f278-bb10-fda1-35b0-971617aec5f9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b959f278-bb10-fda1-35b0-971617aec5f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b959f278-bb10-fda1-35b0-971617aec5f9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetAllTracesEnabled Method

RFmxSpecAnMXIMConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the IM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies whether to enable the traces to be stored and retrieved after performing the IM measurement.

###### Return Value

Int32

##### Remarks

IMAllTracesEnabled

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b980f5dc-4cb3-9c92-086e-79cda8df9b61.htm language=enus -->
## TOPIC 00443: rfmxspecandotnet/html/b980f5dc-4cb3-9c92-086e-79cda8df9b61.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b980f5dc-4cb3-9c92-086e-79cda8df9b61.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b980f5dc-4cb3-9c92-086e-79cda8df9b61.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemFftWindow Enumeration

RFmxSpecAnMXSemFftWindow Enumeration

Specifies the FFT window type to use to reduce spectral leakage.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemFftWindow
```

```text
Public Enumeration RFmxSpecAnMXSemFftWindow
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| FlatTop | 1 | Measures single-tone amplitudes accurately. |
| Hanning | 2 | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| Hamming | 3 | Analyzes closely-spaced sine waves. |
| Gaussian | 4 | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |
| Blackman | 5 | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| BlackmanHarris | 6 | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| KaiserBessel | 7 | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b9a2a8ff-6243-b0cf-444e-13c61acfa097.htm language=enus -->
## TOPIC 00444: rfmxspecandotnet/html/b9a2a8ff-6243-b0cf-444e-13c61acfa097.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b9a2a8ff-6243-b0cf-444e-13c61acfa097.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b9a2a8ff-6243-b0cf-444e-13c61acfa097.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetColdSourceMode Method

RFmxSpecAnMXNFConfigurationSetColdSourceMode Method

Sets whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetColdSourceMode(
	string selectorString,
	RFmxSpecAnMXNFColdSourceMode value
)
```

```text
Public Function SetColdSourceMode ( 
	selectorString As String,
	value As RFmxSpecAnMXNFColdSourceMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFColdSourceMode**
  - Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

###### Return Value

Int32

##### Remarks

NFColdSourceMode

Measure

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/b9ec4880-c585-259f-4708-02174287ecab.htm language=enus -->
## TOPIC 00445: rfmxspecandotnet/html/b9ec4880-c585-259f-4708-02174287ecab.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/b9ec4880-c585-259f-4708-02174287ecab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/b9ec4880-c585-259f-4708-02174287ecab.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetCarrierRrcFilterEnabled Method

RFmxSpecAnMXChpConfigurationSetCarrierRrcFilterEnabled Method

Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCarrierRrcFilterEnabled(
	string selectorString,
	RFmxSpecAnMXChpCarrierRrcFilterEnabled value
)
```

```text
Public Function SetCarrierRrcFilterEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXChpCarrierRrcFilterEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXChpCarrierRrcFilterEnabled**
  - Specifies whether to apply the RRC filter on the acquired channel after measuring the channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetCarrierRRCFilterEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ba27fa7d-0f19-24fa-ef7a-cd731869559f.htm language=enus -->
## TOPIC 00446: rfmxspecandotnet/html/ba27fa7d-0f19-24fa-ef7a-cd731869559f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ba27fa7d-0f19-24fa-ef7a-cd731869559f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ba27fa7d-0f19-24fa-ef7a-cd731869559f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.FetchRelativePowerTrace Method

RFmxSpecAnMXAmpmResultsFetchRelativePowerTrace Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRelativePowerTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> relativePower
)
```

```text
Public Function FetchRelativePowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef relativePower As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **relativePower AnalogWaveformSingle**
  - Upon return, contains the relative power trace values.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ba491eb9-ca72-0dcd-8e27-a17fd8cbb6a1.htm language=enus -->
## TOPIC 00447: rfmxspecandotnet/html/ba491eb9-ca72-0dcd-8e27-a17fd8cbb6a1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ba491eb9-ca72-0dcd-8e27-a17fd8cbb6a1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ba491eb9-ca72-0dcd-8e27-a17fd8cbb6a1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetNoiseCalibrationAveragingCount Method

RFmxSpecAnMXChpConfigurationSetNoiseCalibrationAveragingCount Method

SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCalibrationAveragingCount(
	string selectorString,
	int value
)
```

```text
Public Function SetNoiseCalibrationAveragingCount ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False.

###### Return Value

Int32

##### Remarks

ChpNoiseCalibrationAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ba76d85a-6f76-0245-f19d-8d1da921bba0.htm language=enus -->
## TOPIC 00448: rfmxspecandotnet/html/ba76d85a-6f76-0245-f19d-8d1da921bba0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ba76d85a-6f76-0245-f19d-8d1da921bba0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ba76d85a-6f76-0245-f19d-8d1da921bba0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.GetCfrShapingFactor Method

RFmxSpecAnMXDpdPreDpdGetCfrShapingFactor Method

DpdPreDpdCfrEnabled

True

DpdPreDpdCfrMethod

Sigmoid

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrShapingFactor(
	string selectorString,
	out double value
)
```

```text
Public Function GetCfrShapingFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the shaping factor to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to Sigmoid. Refer to the DPD concept topic for more information about shaping factor.

###### Return Value

Int32

##### Remarks

DpdPreDpdCfrShapingFactor

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ba7aaa0b-8771-5a10-549d-44dbbf8d85e0.htm language=enus -->
## TOPIC 00449: rfmxspecandotnet/html/ba7aaa0b-8771-5a10-549d-44dbbf8d85e0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ba7aaa0b-8771-5a10-549d-44dbbf8d85e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ba7aaa0b-8771-5a10-549d-44dbbf8d85e0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetIQOriginOffsetCorrectionEnabled Method

RFmxSpecAnMXDpdConfigurationGetIQOriginOffsetCorrectionEnabled Method

Gets the IQ origin offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOriginOffsetCorrectionEnabled(
	string selectorString,
	out RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled value
)
```

```text
Public Function GetIQOriginOffsetCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled**
  - Upon return, indicates whether the IQ origin offset correction for the measurement is enabled.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ba92dc36-8b3b-e0dc-d8e2-1a6149820a5f.htm language=enus -->
## TOPIC 00450: rfmxspecandotnet/html/ba92dc36-8b3b-e0dc-d8e2-1a6149820a5f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ba92dc36-8b3b-e0dc-d8e2-1a6149820a5f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ba92dc36-8b3b-e0dc-d8e2-1a6149820a5f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetRbwFilterType Method

RFmxSpecAnMXAcpConfigurationSetRbwFilterType Method

Sets the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxSpecAnMXAcpRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetRBWFilterType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/baf3c9b8-79e5-03a9-2c7a-eaeff2b1cf1f.htm language=enus -->
## TOPIC 00451: rfmxspecandotnet/html/baf3c9b8-79e5-03a9-2c7a-eaeff2b1cf1f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/baf3c9b8-79e5-03a9-2c7a-eaeff2b1cf1f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/baf3c9b8-79e5-03a9-2c7a-eaeff2b1cf1f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled Enumeration

RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled Enumeration

Specifies whether to enable frequency offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled
```

```text
Public Enumeration RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the frequency offset correction. |
| True | 1 | Enables the frequency offset correction. The measurement computes and corrects any frequency offset between the reference and the acquired waveforms. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bb404b9f-201e-c1af-9fe4-645476964012.htm language=enus -->
## TOPIC 00452: rfmxspecandotnet/html/bb404b9f-201e-c1af-9fe4-645476964012.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bb404b9f-201e-c1af-9fe4-645476964012.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bb404b9f-201e-c1af-9fe4-645476964012.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntThresholdType Enumeration

RFmxSpecAnMXFcntThresholdType Enumeration

Specifies the reference for the power level used for thresholding.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXFcntThresholdType
```

```text
Public Enumeration RFmxSpecAnMXFcntThresholdType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The threshold is relative to the peak power, in dB, of the acquired samples. |
| Absolute | 1 | The threshold is the absolute power, in dBm. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bb6a94c3-5d2d-292b-24ef-14248b439285.htm language=enus -->
## TOPIC 00453: rfmxspecandotnet/html/bb6a94c3-5d2d-292b-24ef-14248b439285.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bb6a94c3-5d2d-292b-24ef-14248b439285.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bb6a94c3-5d2d-292b-24ef-14248b439285.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.ValidateNoiseCalibrationData Method

RFmxSpecAnMXAcpConfigurationValidateNoiseCalibrationData Method

selectorstring

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ValidateNoiseCalibrationData(
	string selectorString,
	out RFmxSpecAnMXAcpNoiseCalibrationDataValid noiseCalibrationDataValid
)
```

```text
Public Function ValidateNoiseCalibrationData ( 
	selectorString As String,
	<OutAttribute> ByRef noiseCalibrationDataValid As RFmxSpecAnMXAcpNoiseCalibrationDataValid
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **noiseCalibrationDataValid RFmxSpecAnMXAcpNoiseCalibrationDataValid**
  - Upon return, contains whether the calibration data is valid.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bb8c55ff-8052-30be-18e1-c5bbc9061b9e.htm language=enus -->
## TOPIC 00454: rfmxspecandotnet/html/bb8c55ff-8052-30be-18e1-c5bbc9061b9e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bb8c55ff-8052-30be-18e1-c5bbc9061b9e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bb8c55ff-8052-30be-18e1-c5bbc9061b9e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetLowerOffsetMargin Method

RFmxSpecAnMXSemResultsGetLowerOffsetMargin Method

Gets the margin, in dB, from the limit mask.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetMargin(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetMargin ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the margin, in dB, from the limit mask.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetMargin() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bb8e5701-feb5-cced-4833-1993132a378c.htm language=enus -->
## TOPIC 00455: rfmxspecandotnet/html/bb8e5701-feb5-cced-4833-1993132a378c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bb8e5701-feb5-cced-4833-1993132a378c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bb8e5701-feb5-cced-4833-1993132a378c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmAMToPMEnabled Enumeration

RFmxSpecAnMXAmpmAMToPMEnabled Enumeration

Specifies whether to enable the results that rely on AM to PM characteristics.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAmpmAMToPMEnabled
```

```text
Public Enumeration RFmxSpecAnMXAmpmAMToPMEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the computation of following scalar results and traces. Empty array is returned if the disabled result is an array. NaN is returned otherwise.The following scalar results are disabled:GetMeanPhaseError(String, Double)GetPhaseErrorRange(String, Double)GetAMToPMCurveFitResidual(String, Double)AMPM Results AM to PM Curve Fit CoefficientsThe following traces are disabled:Measured AM to PM Curve Fit AM to PM Relative Phase Trace |
| True | 1 | Enables the computation of AM to PM results and traces. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bba556df-e015-cadb-2817-bc0cc19cce66.htm language=enus -->
## TOPIC 00456: rfmxspecandotnet/html/bba556df-e015-cadb-2817-bc0cc19cce66.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bba556df-e015-cadb-2817-bc0cc19cce66.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bba556df-e015-cadb-2817-bc0cc19cce66.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpResults.GetCarrierFrequency Method

RFmxSpecAnMXChpResultsGetCarrierFrequency Method

SetCenterFrequency(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string..
- **value Double**
  - Upon return, contains the center frequency, in Hz, of the carrier relative to the SetCenterFrequency(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetResultsCarrierFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bbc5b1f1-4bc3-ab20-e8a7-3e9dd12cb476.htm language=enus -->
## TOPIC 00457: rfmxspecandotnet/html/bbc5b1f1-4bc3-ab20-e8a7-3e9dd12cb476.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bbc5b1f1-4bc3-ab20-e8a7-3e9dd12cb476.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bbc5b1f1-4bc3-ab20-e8a7-3e9dd12cb476.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrum.Configuration Property

RFmxSpecAnMXSpectrumConfiguration Property

RFmxSpecAnMXSpectrumConfiguration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXSpectrumConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxSpecAnMXSpectrumConfiguration
	Get
```

###### Property Value

RFmxSpecAnMXSpectrumConfiguration

##### See Also

###### Reference

RFmxSpecAnMXSpectrum Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bbf6059c-619c-cf15-5410-316d46484ef2.htm language=enus -->
## TOPIC 00458: rfmxspecandotnet/html/bbf6059c-619c-cf15-5410-316d46484ef2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bbf6059c-619c-cf15-5410-316d46484ef2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bbf6059c-619c-cf15-5410-316d46484ef2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetNearIFOutputPowerOffset Method

RFmxSpecAnMXIMConfigurationSetNearIFOutputPowerOffset Method

SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod)

DynamicRange

SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNearIFOutputPowerOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetNearIFOutputPowerOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False.

###### Return Value

Int32

##### Remarks

IMNearIFOutputPowerOffset

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bbfceb5a-7056-6940-42fb-499101b694f6.htm language=enus -->
## TOPIC 00459: rfmxspecandotnet/html/bbfceb5a-7056-6940-42fb-499101b694f6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bbfceb5a-7056-6940-42fb-499101b694f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bbfceb5a-7056-6940-42fb-499101b694f6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoise Methods

RFmxSpecAnMXPhaseNoise Methods

The [RFmxSpecAnMXPhaseNoise](be357805-baca-5dcb-f9fc-aef55bf04f5e.htm) type exposes the following members.

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

RFmxSpecAnMXPhaseNoise Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bf53f094-1ba0-1ff5-f974-3c28e4628ba1.htm language=enus -->
## TOPIC 00460: rfmxspecandotnet/html/bf53f094-1ba0-1ff5-f974-3c28e4628ba1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bf53f094-1ba0-1ff5-f974-3c28e4628ba1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bf53f094-1ba0-1ff5-f974-3c28e4628ba1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpur Class

RFmxSpecAnMXSpur Class

Represents a Spur measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXSpur : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXSpur
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXSpur type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXSpurConfiguration instance that allows configuration of Spur measurement. |
|  | Results | Gets the RFmxSpecAnMXSpurResults instance that provides methods to retrieve Spur measurement results. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bf61688d-be22-3cc8-3fc4-9a690f30ef2d.htm language=enus -->
## TOPIC 00461: rfmxspecandotnet/html/bf61688d-be22-3cc8-3fc4-9a690f30ef2d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bf61688d-be22-3cc8-3fc4-9a690f30ef2d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bf61688d-be22-3cc8-3fc4-9a690f30ef2d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetSweepTimeInterval Method

RFmxSpecAnMXChpConfigurationGetSweepTimeInterval Method

Gets the sweep time, in seconds.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the sweep time, in seconds.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetSweepTimeInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bf8b7b4e-11af-f0fc-b16c-50aeb3f76456.htm language=enus -->
## TOPIC 00462: rfmxspecandotnet/html/bf8b7b4e-11af-f0fc-b16c-50aeb3f76456.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bf8b7b4e-11af-f0fc-b16c-50aeb3f76456.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bf8b7b4e-11af-f0fc-b16c-50aeb3f76456.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerResults.PeakSearch Method

RFmxSpecAnMXMarkerResultsPeakSearch Method

Moves the marker to the highest peak above the threshold on the configured trace.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int PeakSearch(
	string selectorString,
	out int numberOfPeaks
)
```

```text
Public Function PeakSearch ( 
	selectorString As String,
	<OutAttribute> ByRef numberOfPeaks As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and marker number. Example: "marker0", "result::r1/marker0". You can use the BuildMarkerString2(String, Int32) method to build the selector string.
- **numberOfPeaks Int32**
  - Upon return, contains the total number of peaks above the threshold, when you set the enable the marker threshold.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_MarkerPeakSearch() function in C.

##### See Also

###### Reference

RFmxSpecAnMXMarkerResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bf9d0bb5-7b3b-db4b-284f-70fc9523b073.htm language=enus -->
## TOPIC 00463: rfmxspecandotnet/html/bf9d0bb5-7b3b-db4b-284f-70fc9523b073.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bf9d0bb5-7b3b-db4b-284f-70fc9523b073.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bf9d0bb5-7b3b-db4b-284f-70fc9523b073.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled Enumeration

RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled Enumeration

Specifies if auto detection of carrier offset and carrier bandwidth is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled
```

```text
Public Enumeration RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables auto detection of carrier offset and carrier bandwidth. |
| True | 1 | Enables auto detection of carrier offset and carrier bandwidth. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bfb68982-c009-3f0a-15a9-15f76be7412b.htm language=enus -->
## TOPIC 00464: rfmxspecandotnet/html/bfb68982-c009-3f0a-15a9-15f76be7412b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bfb68982-c009-3f0a-15a9-15f76be7412b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bfb68982-c009-3f0a-15a9-15f76be7412b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFDutType Enumeration

RFmxSpecAnMXNFDutType Enumeration

Specifies the type of DUT.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFDutType
```

```text
Public Enumeration RFmxSpecAnMXNFDutType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Amplifier | 0 | Specifies that the DUT only amplifies or attenuates the signal, and does not change the frequency. |
| Downconverter | 1 | Specifies that the DUT is a downconverter, that is, the IF frequency is the difference between the LO and RF frequencies. |
| Upconverter | 2 | Specifies that the DUT is an upconverter, that is, the IF frequency is the sum of LO and RF frequencies. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bfe7941d-da08-7486-a7ce-df2faa7c7e39.htm language=enus -->
## TOPIC 00465: rfmxspecandotnet/html/bfe7941d-da08-7486-a7ce-df2faa7c7e39.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bfe7941d-da08-7486-a7ce-df2faa7c7e39.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bfe7941d-da08-7486-a7ce-df2faa7c7e39.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants.PxiTriggerLine4 Field

RFmxSpecAnMXConstantsPxiTriggerLine4 Field

The signal is exported to the PXI trigger line 4.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMXConstants Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bfea81ef-367a-99c4-7b3f-6f889558ccb5.htm language=enus -->
## TOPIC 00466: rfmxspecandotnet/html/bfea81ef-367a-99c4-7b3f-6f889558ccb5.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bfea81ef-367a-99c4-7b3f-6f889558ccb5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bfea81ef-367a-99c4-7b3f-6f889558ccb5.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.ConfigureDetector Method

RFmxSpecAnMXAcpConfigurationConfigureDetector Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDetector(
	string selectorString,
	RFmxSpecAnMXAcpDetectorType detectorType,
	int detectorPoints
)
```

```text
Public Function ConfigureDetector ( 
	selectorString As String,
	detectorType As RFmxSpecAnMXAcpDetectorType,
	detectorPoints As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **detectorType RFmxSpecAnMXAcpDetectorType**
  - Specifies the type of detector to be used.
- **detectorPoints Int32**
  - Specifies the number of points after the detector is applied.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/bffe599e-99cd-a87c-d155-8abcaebe01a4.htm language=enus -->
## TOPIC 00467: rfmxspecandotnet/html/bffe599e-99cd-a87c-d155-8abcaebe01a4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/bffe599e-99cd-a87c-d155-8abcaebe01a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/bffe599e-99cd-a87c-d155-8abcaebe01a4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseResults.GetResidualFM Method

RFmxSpecAnMXPhaseNoiseResultsGetResidualFM Method

Gets the residual FM in Hz.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetResidualFM(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetResidualFM ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the residual FM in Hz.

###### Return Value

Int32

##### Remarks

PhaseNoiseResultsResidualFM

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c005ea87-9748-6450-b635-71ee2eb31712.htm language=enus -->
## TOPIC 00468: rfmxspecandotnet/html/c005ea87-9748-6450-b635-71ee2eb31712.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c005ea87-9748-6450-b635-71ee2eb31712.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c005ea87-9748-6450-b635-71ee2eb31712.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdMeasurementSampleRateMode Enumeration

RFmxSpecAnMXDpdMeasurementSampleRateMode Enumeration

Specifies the acquisition sample rate configuration mode.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdMeasurementSampleRateMode
```

```text
Public Enumeration RFmxSpecAnMXDpdMeasurementSampleRateMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| User | 0 | The acquisition sample rate is defined by the GetMeasurementSampleRateMode(String, RFmxSpecAnMXDpdMeasurementSampleRateMode) method. |
| ReferenceWaveform | 1 | The acquisition sample rate is set to match the sample rate of the reference waveform. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c054a929-bc2c-b20f-ae1b-4b01b5e93a6b.htm language=enus -->
## TOPIC 00469: rfmxspecandotnet/html/c054a929-bc2c-b20f-ae1b-4b01b5e93a6b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c054a929-bc2c-b20f-ae1b-4b01b5e93a6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c054a929-bc2c-b20f-ae1b-4b01b5e93a6b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetMeasurementMethod Method

RFmxSpecAnMXAcpConfigurationSetMeasurementMethod Method

Sets the method for performing the adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementMethod(
	string selectorString,
	RFmxSpecAnMXAcpMeasurementMethod value
)
```

```text
Public Function SetMeasurementMethod ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpMeasurementMethod**
  - Specifies the method for performing the ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetMeasurementMethod() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c07a551e-7f91-112f-cbce-c77c334c0118.htm language=enus -->
## TOPIC 00470: rfmxspecandotnet/html/c07a551e-7f91-112f-cbce-c77c334c0118.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c07a551e-7f91-112f-cbce-c77c334c0118.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c07a551e-7f91-112f-cbce-c77c334c0118.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.SetMeasurementEnabled Method

RFmxSpecAnMXIQConfigurationSetMeasurementEnabled Method

Sets whether to enable the I/Q measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - to enable the I/Q measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQSetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c0867260-cd2b-4bd6-98de-58041b6f2653.htm language=enus -->
## TOPIC 00471: rfmxspecandotnet/html/c0867260-cd2b-4bd6-98de-58041b6f2653.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c0867260-cd2b-4bd6-98de-58041b6f2653.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c0867260-cd2b-4bd6-98de-58041b6f2653.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetCfrShapingThreshold Method

RFmxSpecAnMXDpdApplyDpdGetCfrShapingThreshold Method

DpdApplyDpdCfrEnabled

True

DpdApplyDpdCfrMethod

Sigmoid

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrShapingThreshold(
	string selectorString,
	out double value
)
```

```text
Public Function GetCfrShapingThreshold ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the shaping threshold to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrShapingThreshold

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c09cad19-7803-72f9-49fb-9fed40349516.htm language=enus -->
## TOPIC 00472: rfmxspecandotnet/html/c09cad19-7803-72f9-49fb-9fed40349516.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c09cad19-7803-72f9-49fb-9fed40349516.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c09cad19-7803-72f9-49fb-9fed40349516.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMResults.FetchInterceptPowerArray Method

RFmxSpecAnMXIMResultsFetchInterceptPowerArray Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchInterceptPowerArray(
	string selectorString,
	double timeout,
	ref int[] intermodOrder,
	ref double[] worstCaseOutputInterceptPower,
	ref double[] lowerOutputInterceptPower,
	ref double[] upperOutputInterceptPower
)
```

```text
Public Function FetchInterceptPowerArray ( 
	selectorString As String,
	timeout As Double,
	ByRef intermodOrder As Integer(),
	ByRef worstCaseOutputInterceptPower As Double(),
	ByRef lowerOutputInterceptPower As Double(),
	ByRef upperOutputInterceptPower As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **intermodOrder Int32**
  - Upon return, contains an array of the orders of the intermods.
- **worstCaseOutputInterceptPower Double**
  - Upon return, contains an array of the worst case output intercept powers which are equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm.
- **lowerOutputInterceptPower Double**
  - Upon return, contains an array of the lower output intercept power values. This value is expressed in dBm.
- **upperOutputInterceptPower Double**
  - Upon return, contains an array of the upper output intercept power values. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIMResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c0a03a0d-bcf8-544c-b773-6e8a069afbea.htm language=enus -->
## TOPIC 00473: rfmxspecandotnet/html/c0a03a0d-bcf8-544c-b773-6e8a069afbea.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c0a03a0d-bcf8-544c-b773-6e8a069afbea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c0a03a0d-bcf8-544c-b773-6e8a069afbea.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemOffsetFrequencyDefinition Enumeration

RFmxSpecAnMXSemOffsetFrequencyDefinition Enumeration

Specifies the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemOffsetFrequencyDefinition
```

```text
Public Enumeration RFmxSpecAnMXSemOffsetFrequencyDefinition
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| CarrierCenterToMeasurementBandwidthCenter | 0 | The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. Measurement Bandwidth = Resolution Bandwidth * Bandwidth Integral. |
| CarrierCenterToMeasurementBandwidthEdge | 1 | The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the nearest edge of the offset segment measurement bandwidth. |
| CarrierEdgeToMeasurementBandwidthCenter | 2 | The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the center of the nearest offset segment measurement bandwidth. |
| CarrierEdgeToMeasurementBandwidthEdge | 3 | The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the edge of the nearest offset segment measurement bandwidth. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c0a58d5b-ceb2-9e05-2ca5-488a36e9480d.htm language=enus -->
## TOPIC 00474: rfmxspecandotnet/html/c0a58d5b-ceb2-9e05-2ca5-488a36e9480d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c0a58d5b-ceb2-9e05-2ca5-488a36e9480d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c0a58d5b-ceb2-9e05-2ca5-488a36e9480d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetAutoIntermodsSetupEnabled Method

RFmxSpecAnMXIMConfigurationSetAutoIntermodsSetupEnabled Method

Sets whether the measurement computes the intermod frequencies or uses user-specified frequencies.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoIntermodsSetupEnabled(
	string selectorString,
	RFmxSpecAnMXIMAutoIntermodsSetupEnabled value
)
```

```text
Public Function SetAutoIntermodsSetupEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXIMAutoIntermodsSetupEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIMAutoIntermodsSetupEnabled**
  - Specifies whether the measurement computes the intermod frequencies or uses user-specified frequencies.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c0d57f28-f5d0-2b7b-5381-8bb66e3f83ba.htm language=enus -->
## TOPIC 00475: rfmxspecandotnet/html/c0d57f28-f5d0-2b7b-5381-8bb66e3f83ba.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c0d57f28-f5d0-2b7b-5381-8bb66e3f83ba.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c0d57f28-f5d0-2b7b-5381-8bb66e3f83ba.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Acp Property

RFmxSpecAnMXAcp Property

Gets the RFmxSpecAnMXAcp instance that represents the ACP measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXAcp Acp { get; }
```

```text
Public ReadOnly Property Acp As RFmxSpecAnMXAcp
	Get
```

###### Property Value

RFmxSpecAnMXAcp

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c1507f40-9915-f330-5056-a7e94b43d3ff.htm language=enus -->
## TOPIC 00476: rfmxspecandotnet/html/c1507f40-9915-f330-5056-a7e94b43d3ff.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c1507f40-9915-f330-5056-a7e94b43d3ff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c1507f40-9915-f330-5056-a7e94b43d3ff.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeVbwFilterAutoBandwidth Method

RFmxSpecAnMXSpurConfigurationSetRangeVbwFilterAutoBandwidth Method

Sets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeVbwFilterAutoBandwidth(
	string selectorString,
	RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth value
)
```

```text
Public Function SetRangeVbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the spurrange number. Example: "spurrange0". You can use the BuildRangeString(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth**
  - Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

###### Return Value

Int32

##### Remarks

SpurRangeVbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c1619608-0f77-9016-8717-9c87eb718391.htm language=enus -->
## TOPIC 00477: rfmxspecandotnet/html/c1619608-0f77-9016-8717-9c87eb718391.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c1619608-0f77-9016-8717-9c87eb718391.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c1619608-0f77-9016-8717-9c87eb718391.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.GetThresholdLevel Method

RFmxSpecAnMXTxpConfigurationGetThresholdLevel Method

Gets the relative or absolute threshold power level.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetThresholdLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetThresholdLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the relative or absolute threshold power level.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPGetThresholdLevel() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c28b485c-6534-8576-50c9-5f73aaf13c33.htm language=enus -->
## TOPIC 00478: rfmxspecandotnet/html/c28b485c-6534-8576-50c9-5f73aaf13c33.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c28b485c-6534-8576-50c9-5f73aaf13c33.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c28b485c-6534-8576-50c9-5f73aaf13c33.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSem Methods

RFmxSpecAnMXSem Methods

The [RFmxSpecAnMXSem](0bfffa05-d038-117f-429d-d05f92a6eb67.htm) type exposes the following members.

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

RFmxSpecAnMXSem Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c29837d6-d307-b0cd-9350-c208836cc447.htm language=enus -->
## TOPIC 00479: rfmxspecandotnet/html/c29837d6-d307-b0cd-9350-c208836cc447.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c29837d6-d307-b0cd-9350-c208836cc447.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c29837d6-d307-b0cd-9350-c208836cc447.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.SetRbwFilterType Method

RFmxSpecAnMXTxpConfigurationSetRbwFilterType Method

Sets the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxSpecAnMXTxpRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxSpecAnMXTxpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXTxpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPSetRBWFilterType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c2d3b6af-c43a-a707-c172-03c72daca6ea.htm language=enus -->
## TOPIC 00480: rfmxspecandotnet/html/c2d3b6af-c43a-a707-c172-03c72daca6ea.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c2d3b6af-c43a-a707-c172-03c72daca6ea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c2d3b6af-c43a-a707-c172-03c72daca6ea.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetPowerUnits Method

RFmxSpecAnMXSemConfigurationSetPowerUnits Method

Sets the power units.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPowerUnits(
	string selectorString,
	RFmxSpecAnMXSemPowerUnits value
)
```

```text
Public Function SetPowerUnits ( 
	selectorString As String,
	value As RFmxSpecAnMXSemPowerUnits
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSemPowerUnits**
  - Specifies the power units.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetPowerUnits() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c2e45369-dfe7-a270-ae6b-745ef4f205dc.htm language=enus -->
## TOPIC 00481: rfmxspecandotnet/html/c2e45369-dfe7-a270-ae6b-745ef4f205dc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c2e45369-dfe7-a270-ae6b-745ef4f205dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c2e45369-dfe7-a270-ae6b-745ef4f205dc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfResults.GetOneThousandthPercentPower Method

RFmxSpecAnMXCcdfResultsGetOneThousandthPercentPower Method

Gets the power, in dB, above the mean power, over which 0.001% of the total samples in the signal are present.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOneThousandthPercentPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetOneThousandthPercentPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the power, in dB, above the mean power, over which 0.001% of the total samples in the signal are present.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFGetResultsOneThousandthPercentPower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c3124d32-ca3d-4562-1a2e-fe5cb0b61460.htm language=enus -->
## TOPIC 00482: rfmxspecandotnet/html/c3124d32-ca3d-4562-1a2e-fe5cb0b61460.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c3124d32-ca3d-4562-1a2e-fe5cb0b61460.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c3124d32-ca3d-4562-1a2e-fe5cb0b61460.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtPhaseUnwrapEnabled Enumeration

RFmxSpecAnMXPavtPhaseUnwrapEnabled Enumeration

Specifies whether the phase measurement results are unwrapped or wrapped.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXPavtPhaseUnwrapEnabled
```

```text
Public Enumeration RFmxSpecAnMXPavtPhaseUnwrapEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Phase measurement results are wrapped within +/-180 degrees. |
| True | 1 | Phase measurement results are unwrapped. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c326d19d-fc24-bdc2-0af8-77a941f0385e.htm language=enus -->
## TOPIC 00483: rfmxspecandotnet/html/c326d19d-fc24-bdc2-0af8-77a941f0385e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c326d19d-fc24-bdc2-0af8-77a941f0385e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c326d19d-fc24-bdc2-0af8-77a941f0385e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetIFOutputPowerOffsetAuto Method

RFmxSpecAnMXAcpConfigurationSetIFOutputPowerOffsetAuto Method

Sets whether the measurement computes an IF output power level offset, for the offset channels to improve the dynamic range of the ACP measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIFOutputPowerOffsetAuto(
	string selectorString,
	RFmxSpecAnMXAcpIFOutputPowerOffsetAuto value
)
```

```text
Public Function SetIFOutputPowerOffsetAuto ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpIFOutputPowerOffsetAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpIFOutputPowerOffsetAuto**
  - Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetIFOutputPowerOffsetAuto() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c336a0fa-4aa2-c7f1-df1c-dce9407dc580.htm language=enus -->
## TOPIC 00484: rfmxspecandotnet/html/c336a0fa-4aa2-c7f1-df1c-dce9407dc580.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c336a0fa-4aa2-c7f1-df1c-dce9407dc580.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c336a0fa-4aa2-c7f1-df1c-dce9407dc580.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetLowerOffsetPeakRelativePower Method

RFmxSpecAnMXSemResultsGetLowerOffsetPeakRelativePower Method

Gets the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetPeakRelativePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetPeakRelativePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetPeakRelativePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c35faade-25cd-51c0-9a33-38a69670df9c.htm language=enus -->
## TOPIC 00485: rfmxspecandotnet/html/c35faade-25cd-51c0-9a33-38a69670df9c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c35faade-25cd-51c0-9a33-38a69670df9c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c35faade-25cd-51c0-9a33-38a69670df9c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.ConfigureMeasurementSampleRate Method

RFmxSpecAnMXAmpmConfigurationConfigureMeasurementSampleRate Method

Configures the acquisition sample rate, in samples per second (S/s), for the AMPM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementSampleRate(
	string selectorString,
	RFmxSpecAnMXAmpmMeasurementSampleRateMode sampleRateMode,
	double sampleRate
)
```

```text
Public Function ConfigureMeasurementSampleRate ( 
	selectorString As String,
	sampleRateMode As RFmxSpecAnMXAmpmMeasurementSampleRateMode,
	sampleRate As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sampleRateMode RFmxSpecAnMXAmpmMeasurementSampleRateMode**
  - Specifies whether the acquisition sample rate is based on the reference waveform.
- **sampleRate Double**
  - Specifies the acquisition sample rate, in S/s, when you set the sampleRateMode parameter to User.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMCfgMeasurementSampleRate() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c3af308b-9b49-6ecf-5081-1f115990355c.htm language=enus -->
## TOPIC 00486: rfmxspecandotnet/html/c3af308b-9b49-6ecf-5081-1f115990355c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c3af308b-9b49-6ecf-5081-1f115990355c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c3af308b-9b49-6ecf-5081-1f115990355c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetAveragingEnabled Method

RFmxSpecAnMXSpectrumConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxSpecAnMXSpectrumAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumAveragingEnabled**
  - Upon return, indicates whether to enable averaging for the Spectrum measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumGetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c3d31f9d-77f9-b102-a255-b60cffdf80db.htm language=enus -->
## TOPIC 00487: rfmxspecandotnet/html/c3d31f9d-77f9-b102-a255-b60cffdf80db.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c3d31f9d-77f9-b102-a255-b60cffdf80db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c3d31f9d-77f9-b102-a255-b60cffdf80db.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetLookupTableAMToAMCurveFitType Method

RFmxSpecAnMXDpdConfigurationSetLookupTableAMToAMCurveFitType Method

SetModel(String, RFmxSpecAnMXDpdModel)

LookupTable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLookupTableAMToAMCurveFitType(
	string selectorString,
	RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType value
)
```

```text
Public Function SetLookupTableAMToAMCurveFitType ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType**
  - Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetLookupTableAMtoAMCurveFitType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c4eaa543-efbb-1ac1-750f-1ae21d1089f8.htm language=enus -->
## TOPIC 00488: rfmxspecandotnet/html/c4eaa543-efbb-1ac1-750f-1ae21d1089f8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c4eaa543-efbb-1ac1-750f-1ae21d1089f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c4eaa543-efbb-1ac1-750f-1ae21d1089f8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.SetAveragingCount Method

RFmxSpecAnMXIdpdConfigurationSetAveragingCount Method

Sets the number of acquisitions used for averaging when Averaging Enabled is TRUE.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the number of acquisitions used for averaging when Averaging Enabled is TRUE.

###### Return Value

Int32

##### Remarks

IdpdAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c53edca6-69bd-be18-6cdc-8f2df07f986e.htm language=enus -->
## TOPIC 00489: rfmxspecandotnet/html/c53edca6-69bd-be18-6cdc-8f2df07f986e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c53edca6-69bd-be18-6cdc-8f2df07f986e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c53edca6-69bd-be18-6cdc-8f2df07f986e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.SetFrequencyOffsetCorrectionEnabled Method

RFmxSpecAnMXPavtConfigurationSetFrequencyOffsetCorrectionEnabled Method

Sets whether to enable frequency offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyOffsetCorrectionEnabled(
	string selectorString,
	RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled value
)
```

```text
Public Function SetFrequencyOffsetCorrectionEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled**
  - Specifies whether to enable frequency offset correction for the measurement.

###### Return Value

Int32

##### Remarks

PavtFrequencyOffsetCorrectionEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c603ee22-c4c0-fce8-4585-8f3810fc8355.htm language=enus -->
## TOPIC 00490: rfmxspecandotnet/html/c603ee22-c4c0-fce8-4585-8f3810fc8355.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c603ee22-c4c0-fce8-4585-8f3810fc8355.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c603ee22-c4c0-fce8-4585-8f3810fc8355.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.ConfigureHeadroom Method

RFmxSpecAnMXDpdApplyDpdConfigureHeadroom Method

**Note: This API is now obsolete.**

Configures the headroom, in dB, for the predistorted waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method has been deprecated")]
public int ConfigureHeadroom(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdHeadroomMode headroomMode,
	double headroom
)
```

```text
<ObsoleteAttribute("This method has been deprecated")>
Public Function ConfigureHeadroom ( 
	selectorString As String,
	headroomMode As RFmxSpecAnMXDpdApplyDpdHeadroomMode,
	headroom As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **headroomMode RFmxSpecAnMXDpdApplyDpdHeadroomMode**
  - Specifies the mode of applying headroom on the predistorted waveform.
- **headroom Double**
  - Specifies the headroom, in dB, to apply to the predistorted waveform when you set the headroomMode parameter to Manual.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgApplyDPDHeadroom() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c62efa26-2800-ba27-4eaf-d1d6843c6cd1.htm language=enus -->
## TOPIC 00491: rfmxspecandotnet/html/c62efa26-2800-ba27-4eaf-d1d6843c6cd1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c62efa26-2800-ba27-4eaf-d1d6843c6cd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c62efa26-2800-ba27-4eaf-d1d6843c6cd1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetCfrShapingFactor Method

RFmxSpecAnMXDpdApplyDpdGetCfrShapingFactor Method

DpdApplyDpdCfrEnabled

True

DpdApplyDpdCfrMethod

Sigmoid

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrShapingFactor(
	string selectorString,
	out double value
)
```

```text
Public Function GetCfrShapingFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the shaping factor to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. Refer to DPD concept topic for more information about shaping factor.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrShapingFactor

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c65f7fb8-c569-36e7-c263-2175a8bd4c59.htm language=enus -->
## TOPIC 00492: rfmxspecandotnet/html/c65f7fb8-c569-36e7-c263-2175a8bd4c59.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c65f7fb8-c569-36e7-c263-2175a8bd4c59.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c65f7fb8-c569-36e7-c263-2175a8bd4c59.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.SetFundamentalRbwFilterAlpha Method

RFmxSpecAnMXHarmConfigurationSetFundamentalRbwFilterAlpha Method

Sets the roll-off factor for the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFundamentalRbwFilterAlpha(
	string selectorString,
	double value
)
```

```text
Public Function SetFundamentalRbwFilterAlpha ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the roll-off factor for the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmSetFundamentalRBWFilterAlpha() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c6648bea-6742-f60e-8742-aee9be8b7813.htm language=enus -->
## TOPIC 00493: rfmxspecandotnet/html/c6648bea-6742-f60e-8742-aee9be8b7813.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c6648bea-6742-f60e-8742-aee9be8b7813.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c6648bea-6742-f60e-8742-aee9be8b7813.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetAveragingCount Method

RFmxSpecAnMXSpectrumConfigurationGetAveragingCount Method

Gets the number of acquisitions used for averaging.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the number of acquisitions used for averaging.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumGetAveragingCount() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c66b53ed-2bc3-7c9a-ec95-ccae522af74b.htm language=enus -->
## TOPIC 00494: rfmxspecandotnet/html/c66b53ed-2bc3-7c9a-ec95-ccae522af74b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c66b53ed-2bc3-7c9a-ec95-ccae522af74b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c66b53ed-2bc3-7c9a-ec95-ccae522af74b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetRangeVbwFilterBandwidth Method

RFmxSpecAnMXSpurConfigurationGetRangeVbwFilterBandwidth Method

SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeVbwFilterBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetRangeVbwFilterBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the spurrange number. Example: "spurrange0". You can use the BuildRangeString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the video bandwidth (VBW) in Hz when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to False.

###### Return Value

Int32

##### Remarks

SpurRangeVbwFilterBandwidth

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c682fe53-46ed-9ce0-d43a-a522dabcaca1.htm language=enus -->
## TOPIC 00495: rfmxspecandotnet/html/c682fe53-46ed-9ce0-d43a-a522dabcaca1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c682fe53-46ed-9ce0-d43a-a522dabcaca1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c682fe53-46ed-9ce0-d43a-a522dabcaca1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNoiseCalibrationAveragingCount Method

RFmxSpecAnMXAcpConfigurationSetNoiseCalibrationAveragingCount Method

SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCalibrationAveragingCount(
	string selectorString,
	int value
)
```

```text
Public Function SetNoiseCalibrationAveragingCount ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) method to False.

###### Return Value

Int32

##### Remarks

AcpNoiseCalibrationAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c68cff24-9ef2-5f69-6b2b-88015250c696.htm language=enus -->
## TOPIC 00496: rfmxspecandotnet/html/c68cff24-9ef2-5f69-6b2b-88015250c696.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c68cff24-9ef2-5f69-6b2b-88015250c696.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c68cff24-9ef2-5f69-6b2b-88015250c696.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.GetMeasurementIntervalMode Method

RFmxSpecAnMXPavtConfigurationGetMeasurementIntervalMode Method

Gets the mode of configuring the measurement interval.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementIntervalMode(
	string selectorString,
	out RFmxSpecAnMXPavtMeasurementIntervalMode value
)
```

```text
Public Function GetMeasurementIntervalMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXPavtMeasurementIntervalMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPavtMeasurementIntervalMode**
  - Upon return, contains the mode of configuring the measurement interval.

###### Return Value

Int32

##### Remarks

PavtMeasurementIntervalMode

Uniform

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c6950d07-f4f1-eaac-ca3b-4d61de842e90.htm language=enus -->
## TOPIC 00497: rfmxspecandotnet/html/c6950d07-f4f1-eaac-ca3b-4d61de842e90.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c6950d07-f4f1-eaac-ca3b-4d61de842e90.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c6950d07-f4f1-eaac-ca3b-4d61de842e90.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetAveragingType Method

RFmxSpecAnMXSpurConfigurationSetAveragingType Method

Sets averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spurious emission (Spur) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxSpecAnMXSpurAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpurAveragingType**
  - Specifies averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for Spur measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetAveragingType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c699667f-7d94-7511-911d-4d69a1a49c72.htm language=enus -->
## TOPIC 00498: rfmxspecandotnet/html/c699667f-7d94-7511-911d-4d69a1a49c72.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c699667f-7d94-7511-911d-4d69a1a49c72.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c699667f-7d94-7511-911d-4d69a1a49c72.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetMeasurementEnabled Method

RFmxSpecAnMXObwConfigurationSetMeasurementEnabled Method

Sets whether to enable occupied bandwidth (OBW) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - to enable OBW measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c6adc900-1885-908f-fdd5-1aa8b18e4066.htm language=enus -->
## TOPIC 00499: rfmxspecandotnet/html/c6adc900-1885-908f-fdd5-1aa8b18e4066.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c6adc900-1885-908f-fdd5-1aa8b18e4066.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c6adc900-1885-908f-fdd5-1aa8b18e4066.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.BuildHarmonicString Method

RFmxSpecAnMXBuildHarmonicString Method

**Note: This API is now obsolete.**

Creates the selector string to use with Harmonics configuration or fetch methods.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use BuildHarmonicString2 instead.")]
public static string BuildHarmonicString(
	string resultName,
	int harmonicNumber
)
```

```text
<ObsoleteAttribute("Use BuildHarmonicString2 instead.")>
Public Shared Function BuildHarmonicString ( 
	resultName As String,
	harmonicNumber As Integer
) As String
```

###### Parameters

- **resultName String**
  - Specifies the result name for building the selector string.
- **harmonicNumber Int32**
  - Specifies the harmonic number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c6ae38fe-84d7-bc9a-5765-2f457e39a50b.htm language=enus -->
## TOPIC 00500: rfmxspecandotnet/html/c6ae38fe-84d7-bc9a-5765-2f457e39a50b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c6ae38fe-84d7-bc9a-5765-2f457e39a50b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c6ae38fe-84d7-bc9a-5765-2f457e39a50b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants Fields

RFmxSpecAnMXConstants Fields

The [RFmxSpecAnMXConstants](a2a6a1fc-9af0-f40c-e21f-173744db04ea.htm) type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. |
|  | Pfi1 | The signal is exported to the PXI trigger line 0. |
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

RFmxSpecAnMXConstants Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
