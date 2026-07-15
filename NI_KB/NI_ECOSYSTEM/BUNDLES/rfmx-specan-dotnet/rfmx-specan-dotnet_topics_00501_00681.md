# NI DOCUMENT BUNDLE: rfmx-specan-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-dotnet start=501 end=681 -->
<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c6b150e5-5d7d-f91e-8c47-9f7f7cb20903.htm language=enus -->
## TOPIC 00501: rfmxspecandotnet/html/c6b150e5-5d7d-f91e-8c47-9f7f7cb20903.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c6b150e5-5d7d-f91e-8c47-9f7f7cb20903.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c6b150e5-5d7d-f91e-8c47-9f7f7cb20903.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetFrequencyOffsetCorrectionEnabled Method

RFmxSpecAnMXDpdConfigurationGetFrequencyOffsetCorrectionEnabled Method

Gets whether to enable frequency offset correction for the DPD measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyOffsetCorrectionEnabled(
	string selectorString,
	out RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled value
)
```

```text
Public Function GetFrequencyOffsetCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled**
  - Upon return, contains whether to enable frequency offset correction for the DPD measurement.

###### Return Value

Int32

##### Remarks

DpdFrequencyOffsetCorrectionEnabled

True

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c6b995f6-03a3-aafc-a955-cffec00e926a.htm language=enus -->
## TOPIC 00502: rfmxspecandotnet/html/c6b995f6-03a3-aafc-a955-cffec00e926a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c6b995f6-03a3-aafc-a955-cffec00e926a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c6b995f6-03a3-aafc-a955-cffec00e926a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetRbwFilterAutoBandwidth Method

RFmxSpecAnMXSemConfigurationGetOffsetRbwFilterAutoBandwidth Method

Gets whether the measurement computes the resolution bandwidth (RBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRbwFilterAutoBandwidth(
	string selectorString,
	out RFmxSpecAnMXSemOffsetRbwAutoBandwidth value
)
```

```text
Public Function GetOffsetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSemOffsetRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetRbwAutoBandwidth**
  - Upon return, indicates whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetRBWFilterAutoBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c71e70aa-dc49-b506-541c-2ac5ae9c36f9.htm language=enus -->
## TOPIC 00503: rfmxspecandotnet/html/c71e70aa-dc49-b506-541c-2ac5ae9c36f9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c71e70aa-dc49-b506-541c-2ac5ae9c36f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c71e70aa-dc49-b506-541c-2ac5ae9c36f9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseResults.FetchIntegratedNoise Method

RFmxSpecAnMXPhaseNoiseResultsFetchIntegratedNoise Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchIntegratedNoise(
	string selectorString,
	double timeout,
	ref double[] integratedPhaseNoise,
	ref double[] residualPMInRadian,
	ref double[] residualPMInDegree,
	ref double[] residualFM,
	ref double[] jitter
)
```

```text
Public Function FetchIntegratedNoise ( 
	selectorString As String,
	timeout As Double,
	ByRef integratedPhaseNoise As Double(),
	ByRef residualPMInRadian As Double(),
	ByRef residualPMInDegree As Double(),
	ByRef residualFM As Double(),
	ByRef jitter As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **integratedPhaseNoise Double**
  - Upon return, contains the integrated phase noise. This value is expressed in dBc.
- **residualPMInRadian Double**
  - Returns the residual PM in radians.
- **residualPMInDegree Double**
  - Returns the residual PM in degrees.
- **residualFM Double**
  - Upon return, contains the residual FM. This value is expressed in Hz.
- **jitter Double**
  - Upon return, contains the jitter. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c91385d4-4bb7-1ec9-0e74-5a2d15a6c32b.htm language=enus -->
## TOPIC 00504: rfmxspecandotnet/html/c91385d4-4bb7-1ec9-0e74-5a2d15a6c32b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c91385d4-4bb7-1ec9-0e74-5a2d15a6c32b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c91385d4-4bb7-1ec9-0e74-5a2d15a6c32b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetFrequencyConverterFrequencyContext Method

RFmxSpecAnMXNFConfigurationSetFrequencyConverterFrequencyContext Method

Sets the context of the NF Frequency List method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyConverterFrequencyContext(
	string selectorString,
	RFmxSpecAnMXNFFrequencyConverterFrequencyContext value
)
```

```text
Public Function SetFrequencyConverterFrequencyContext ( 
	selectorString As String,
	value As RFmxSpecAnMXNFFrequencyConverterFrequencyContext
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFFrequencyConverterFrequencyContext**
  - Specifies the context of the NF Frequency List method.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c931cf8f-7e2d-be06-bd32-eda225dce9cb.htm language=enus -->
## TOPIC 00505: rfmxspecandotnet/html/c931cf8f-7e2d-be06-bd32-eda225dce9cb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c931cf8f-7e2d-be06-bd32-eda225dce9cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c931cf8f-7e2d-be06-bd32-eda225dce9cb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerResults Methods

RFmxSpecAnMXMarkerResults Methods

The [RFmxSpecAnMXMarkerResults](443b2c91-a8b3-0463-b8a4-7add8f18391b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchFunctionValue | Returns the method value of the selected marker method type. |
|  | FetchXY | Fetches the X and Y locations of the marker. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | NextPeak | Moves the marker to the next highest, next left, or next right peak above the threshold on the configured trace. |
|  | PeakSearch | Moves the marker to the highest peak above the threshold on the configured trace. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXMarkerResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c95a4c69-c101-47bf-1dad-3d8b5abddec9.htm language=enus -->
## TOPIC 00506: rfmxspecandotnet/html/c95a4c69-c101-47bf-1dad-3d8b5abddec9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c95a4c69-c101-47bf-1dad-3d8b5abddec9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c95a4c69-c101-47bf-1dad-3d8b5abddec9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.ListName Property

RFmxSpecAnMXListListName Property

Gets the list name.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public string ListName { get; }
```

```text
Public ReadOnly Property ListName As String
	Get
```

###### Property Value

String

###### Implements

IList.ListName

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c97cc4b5-c553-e12c-03f5-9d7ac5e04e77.htm language=enus -->
## TOPIC 00507: rfmxspecandotnet/html/c97cc4b5-c553-e12c-03f5-9d7ac5e04e77.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c97cc4b5-c553-e12c-03f5-9d7ac5e04e77.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c97cc4b5-c553-e12c-03f5-9d7ac5e04e77.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetConfigurationInput Method

RFmxSpecAnMXDpdApplyDpdSetConfigurationInput Method

Sets whether to use the configuration used by the DPD measurement for applying DPD.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetConfigurationInput(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdConfigurationInput value
)
```

```text
Public Function SetConfigurationInput ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdApplyDpdConfigurationInput
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdConfigurationInput**
  - Contains a value that indicates whether to use the configuration used by the DPD measurement for applying DPD.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDConfigurationInput() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c9b18cdb-af08-ed87-e95d-647d9a591ef2.htm language=enus -->
## TOPIC 00508: rfmxspecandotnet/html/c9b18cdb-af08-ed87-e95d-647d9a591ef2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c9b18cdb-af08-ed87-e95d-647d9a591ef2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c9b18cdb-af08-ed87-e95d-647d9a591ef2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.ConfigureDutAverageInputPower Method

RFmxSpecAnMXAmpmConfigurationConfigureDutAverageInputPower Method

Configures the average power, in dBm, of the signal at the input port of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDutAverageInputPower(
	string selectorString,
	double dutAverageInputPower
)
```

```text
Public Function ConfigureDutAverageInputPower ( 
	selectorString As String,
	dutAverageInputPower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **dutAverageInputPower Double**
  - Specifies the average power, in dBm, of the signal at the input port of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMCfgDUTAverageInputPower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c9d96665-acd3-e4e8-50cf-137d673d5653.htm language=enus -->
## TOPIC 00509: rfmxspecandotnet/html/c9d96665-acd3-e4e8-50cf-137d673d5653.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c9d96665-acd3-e4e8-50cf-137d673d5653.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c9d96665-acd3-e4e8-50cf-137d673d5653.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetCarrierRrcFilterAlpha Method

RFmxSpecAnMXSemConfigurationGetCarrierRrcFilterAlpha Method

Gets the roll-off factor for the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierRrcFilterAlpha(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierRrcFilterAlpha ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the roll-off factor for the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierRRCFilterAlpha() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c9e67449-c75a-4ebd-2b0c-45463c9068d9.htm language=enus -->
## TOPIC 00510: rfmxspecandotnet/html/c9e67449-c75a-4ebd-2b0c-45463c9068d9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c9e67449-c75a-4ebd-2b0c-45463c9068d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c9e67449-c75a-4ebd-2b0c-45463c9068d9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureCarrierIntegrationBandwidth Method

RFmxSpecAnMXSemConfigurationConfigureCarrierIntegrationBandwidth Method

Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierIntegrationBandwidth(
	string selectorString,
	double integrationBandwidth
)
```

```text
Public Function ConfigureCarrierIntegrationBandwidth ( 
	selectorString As String,
	integrationBandwidth As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **integrationBandwidth Double**
  - Specifies the frequency range, in Hz, over which the measurement integrates the carrier channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierIntegrationBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/c9f31646-8155-8181-21a0-a289edc0f2a9.htm language=enus -->
## TOPIC 00511: rfmxspecandotnet/html/c9f31646-8155-8181-21a0-a289edc0f2a9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/c9f31646-8155-8181-21a0-a289edc0f2a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/c9f31646-8155-8181-21a0-a289edc0f2a9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetFftOverlap Method

RFmxSpecAnMXSpectrumConfigurationGetFftOverlap Method

SpectrumSequentialFftSize

SpectrumMeasurementMethod

SequentialFft

SpectrumFftOverlapMode

UserDefined

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the samples to overlap between the consecutive chunks as a percentage of the SpectrumSequentialFftSize method when you set the SpectrumMeasurementMethod method to SequentialFft and the SpectrumFftOverlapMode method to UserDefined. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

SpectrumFftOverlap

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ca2c5dbb-1567-7a63-de12-6cd71682165d.htm language=enus -->
## TOPIC 00512: rfmxspecandotnet/html/ca2c5dbb-1567-7a63-de12-6cd71682165d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ca2c5dbb-1567-7a63-de12-6cd71682165d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ca2c5dbb-1567-7a63-de12-6cd71682165d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetNoiseCompensationEnabled Method

RFmxSpecAnMXSpectrumConfigurationSetNoiseCompensationEnabled Method

Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCompensationEnabled(
	string selectorString,
	RFmxSpecAnMXSpectrumNoiseCompensationEnabled value
)
```

```text
Public Function SetNoiseCompensationEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXSpectrumNoiseCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumNoiseCompensationEnabled**
  - Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

###### Return Value

Int32

##### Remarks

SpectrumNoiseCompensationEnabled

True

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ca30b701-5221-061d-93a9-9ef0b0cda23a.htm language=enus -->
## TOPIC 00513: rfmxspecandotnet/html/ca30b701-5221-061d-93a9-9ef0b0cda23a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ca30b701-5221-061d-93a9-9ef0b0cda23a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ca30b701-5221-061d-93a9-9ef0b0cda23a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetFftWindow Method

RFmxSpecAnMXObwConfigurationSetFftWindow Method

Sets the FFT window type used to reduce spectral leakage.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftWindow(
	string selectorString,
	RFmxSpecAnMXObwFftWindow value
)
```

```text
Public Function SetFftWindow ( 
	selectorString As String,
	value As RFmxSpecAnMXObwFftWindow
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwFftWindow**
  - Specifies the FFT window type used to reduce spectral leakage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetFFTWindow() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ca5504b3-b128-ffdb-d31c-7b4c8568de30.htm language=enus -->
## TOPIC 00514: rfmxspecandotnet/html/ca5504b3-b128-ffdb-d31c-7b4c8568de30.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ca5504b3-b128-ffdb-d31c-7b4c8568de30.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ca5504b3-b128-ffdb-d31c-7b4c8568de30.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetFftOverlapMode Method

RFmxSpecAnMXSpectrumConfigurationGetFftOverlapMode Method

SpectrumMeasurementMethod

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftOverlapMode(
	string selectorString,
	out RFmxSpecAnMXSpectrumFftOverlapMode value
)
```

```text
Public Function GetFftOverlapMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumFftOverlapMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumFftOverlapMode**
  - Upon return, contains the overlap mode when you set the SpectrumMeasurementMethod method to SequentialFft.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ca8194d0-5945-2cb1-791c-34f6fb55a5b8.htm language=enus -->
## TOPIC 00515: rfmxspecandotnet/html/ca8194d0-5945-2cb1-791c-34f6fb55a5b8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ca8194d0-5945-2cb1-791c-34f6fb55a5b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ca8194d0-5945-2cb1-791c-34f6fb55a5b8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetAbsoluteLimitStart Method

RFmxSpecAnMXSemConfigurationGetOffsetAbsoluteLimitStart Method

Gets the absolute power limit, in dBm, corresponding to the beginning of the offset segment.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetAbsoluteLimitStart(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetAbsoluteLimitStart ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the absolute power limit, in dBm, corresponding to the beginning of the offset segment.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetAbsoluteLimitStart() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/caa8caef-7303-475b-b3e7-10e366bf7f44.htm language=enus -->
## TOPIC 00516: rfmxspecandotnet/html/caa8caef-7303-475b-b3e7-10e366bf7f44.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/caa8caef-7303-475b-b3e7-10e366bf7f44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/caa8caef-7303-475b-b3e7-10e366bf7f44.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetSequentialFftSize Method

RFmxSpecAnMXAcpConfigurationGetSequentialFftSize Method

SetMeasurementMethod(String, RFmxSpecAnMXAcpMeasurementMethod)

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSequentialFftSize(
	string selectorString,
	out int value
)
```

```text
Public Function GetSequentialFftSize ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the FFT size when you set the SetMeasurementMethod(String, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft.

###### Return Value

Int32

##### Remarks

AcpSequentialFftSize

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cab7bd93-0301-fd07-2904-ac3aee4c5c0a.htm language=enus -->
## TOPIC 00517: rfmxspecandotnet/html/cab7bd93-0301-fd07-2904-ac3aee4c5c0a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cab7bd93-0301-fd07-2904-ac3aee4c5c0a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cab7bd93-0301-fd07-2904-ac3aee4c5c0a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetAMToPMCurveFitOrder Method

RFmxSpecAnMXAmpmConfigurationSetAMToPMCurveFitOrder Method

Sets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAMToPMCurveFitOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetAMToPMCurveFitOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Contains the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMSetAMToPMCurveFitOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cadaf98e-1f35-0c6b-a939-a49b61c898aa.htm language=enus -->
## TOPIC 00518: rfmxspecandotnet/html/cadaf98e-1f35-0c6b-a939-a49b61c898aa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cadaf98e-1f35-0c6b-a939-a49b61c898aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cadaf98e-1f35-0c6b-a939-a49b61c898aa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetAMToAMEnabled Method

RFmxSpecAnMXAmpmConfigurationGetAMToAMEnabled Method

Gets whether to enable the results that rely on the AM to AM characteristics.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMToAMEnabled(
	string selectorString,
	out RFmxSpecAnMXAmpmAMToAMEnabled value
)
```

```text
Public Function GetAMToAMEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmAMToAMEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmAMToAMEnabled**
  - Upon return, contains whether to enable the results that rely on the AM to AM characteristics.

###### Return Value

Int32

##### Remarks

AmpmAMToAMEnabled

True

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cb335eac-2319-1593-30ea-0eaf5141bb6f.htm language=enus -->
## TOPIC 00519: rfmxspecandotnet/html/cb335eac-2319-1593-30ea-0eaf5141bb6f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cb335eac-2319-1593-30ea-0eaf5141bb6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cb335eac-2319-1593-30ea-0eaf5141bb6f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemLowerOffsetMeasurementStatus Enumeration

RFmxSpecAnMXSemLowerOffsetMeasurementStatus Enumeration

SetOffsetLimitFailMask(String, RFmxSpecAnMXSemOffsetLimitFailMask)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemLowerOffsetMeasurementStatus
```

```text
Public Enumeration RFmxSpecAnMXSemLowerOffsetMeasurementStatus
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Fail | 0 | Indicates that the measurement has failed. |
| Pass | 1 | Indicates that the measurement has passed. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cb80e74d-0919-9c2e-6e66-a2ddce7ec490.htm language=enus -->
## TOPIC 00520: rfmxspecandotnet/html/cb80e74d-0919-9c2e-6e66-a2ddce7ec490.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cb80e74d-0919-9c2e-6e66-a2ddce7ec490.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cb80e74d-0919-9c2e-6e66-a2ddce7ec490.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetCfrShapingFactor Method

RFmxSpecAnMXDpdApplyDpdSetCfrShapingFactor Method

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
public int SetCfrShapingFactor(
	string selectorString,
	double value
)
```

```text
Public Function SetCfrShapingFactor ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the shaping factor to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. Refer to DPD concept topic for more information about shaping factor.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrShapingFactor

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cb868e9a-6ab7-a6b6-0f9b-5219d2da5772.htm language=enus -->
## TOPIC 00521: rfmxspecandotnet/html/cb868e9a-6ab7-a6b6-0f9b-5219d2da5772.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cb868e9a-6ab7-a6b6-0f9b-5219d2da5772.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cb868e9a-6ab7-a6b6-0f9b-5219d2da5772.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.GetFrequencyOffsetCorrectionEnabled Method

RFmxSpecAnMXPavtConfigurationGetFrequencyOffsetCorrectionEnabled Method

Gets whether to enable frequency offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyOffsetCorrectionEnabled(
	string selectorString,
	out RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled value
)
```

```text
Public Function GetFrequencyOffsetCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled**
  - Upon return, contains whether to enable frequency offset correction for the measurement.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cb917e94-beb6-008c-c2df-e5a951dbfe3b.htm language=enus -->
## TOPIC 00522: rfmxspecandotnet/html/cb917e94-beb6-008c-c2df-e5a951dbfe3b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cb917e94-beb6-008c-c2df-e5a951dbfe3b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cb917e94-beb6-008c-c2df-e5a951dbfe3b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.GetSegmentMeasurementLength Method

RFmxSpecAnMXPavtConfigurationGetSegmentMeasurementLength Method

SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode)

Variable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentMeasurementLength(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentMeasurementLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.

###### Return Value

Int32

##### Remarks

PavtSegmentMeasurementLength

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cb9319cf-4a3a-60bf-e921-0aade582630b.htm language=enus -->
## TOPIC 00523: rfmxspecandotnet/html/cb9319cf-4a3a-60bf-e921-0aade582630b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cb9319cf-4a3a-60bf-e921-0aade582630b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cb9319cf-4a3a-60bf-e921-0aade582630b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemAveragingEnabled Enumeration

RFmxSpecAnMXSemAveragingEnabled Enumeration

Specifies whether to enable averaging for the spectral emission mask (SEM) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemAveragingEnabled
```

```text
Public Enumeration RFmxSpecAnMXSemAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The SEM measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the SEM measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cbbaf0ca-8bb5-eb46-d081-084d599eb3b3.htm language=enus -->
## TOPIC 00524: rfmxspecandotnet/html/cbbaf0ca-8bb5-eb46-d081-084d599eb3b3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cbbaf0ca-8bb5-eb46-d081-084d599eb3b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cbbaf0ca-8bb5-eb46-d081-084d599eb3b3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.FetchAbsoluteMaskTrace Method

RFmxSpecAnMXSemResultsFetchAbsoluteMaskTrace Method

Fetches the absolute mask trace used for SEM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAbsoluteMaskTrace(
	string selectorString,
	double timeout,
	ref Spectrum<float> absoluteMask
)
```

```text
Public Function FetchAbsoluteMaskTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef absoluteMask As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absoluteMask SpectrumSingle**
  - Upon return, contains the absolute mask trace, in dBm or dBm/Hz, used for the channel.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMFetchAbsoluteMaskTrace() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cc7e7b98-fcaa-b667-a0f2-16eafa885416.htm language=enus -->
## TOPIC 00525: rfmxspecandotnet/html/cc7e7b98-fcaa-b667-a0f2-16eafa885416.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cc7e7b98-fcaa-b667-a0f2-16eafa885416.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cc7e7b98-fcaa-b667-a0f2-16eafa885416.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.ConfigureMeasurementInterval Method

RFmxSpecAnMXNFConfigurationConfigureMeasurementInterval Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the duration for which signals are aquired at each frequency which you specify in the SetFrequencyList(String, Double) method. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/cfdaf12d-63d5-0cf3-f52d-45ac2af4412a.htm language=enus -->
## TOPIC 00526: rfmxspecandotnet/html/cfdaf12d-63d5-0cf3-f52d-45ac2af4412a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/cfdaf12d-63d5-0cf3-f52d-45ac2af4412a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/cfdaf12d-63d5-0cf3-f52d-45ac2af4412a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntResults.GetAverageAbsoluteFrequency Method

RFmxSpecAnMXFcntResultsGetAverageAbsoluteFrequency Method

Gets the instantaneous frequency of the samples averaged over all acquisitions.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAverageAbsoluteFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetAverageAbsoluteFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the instantaneous frequency of the samples averaged over all acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetResultsAverageAbsoluteFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/d00ba067-284e-6e4a-80cc-32384a5e0c42.htm language=enus -->
## TOPIC 00527: rfmxspecandotnet/html/d00ba067-284e-6e4a-80cc-32384a5e0c42.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/d00ba067-284e-6e4a-80cc-32384a5e0c42.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/d00ba067-284e-6e4a-80cc-32384a5e0c42.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetStartFrequency Method

RFmxSpecAnMXPhaseNoiseConfigurationSetStartFrequency Method

Sets the start offset frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStartFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetStartFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the start offset frequency.

###### Return Value

Int32

##### Remarks

PhaseNoiseStartFrequency

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/d6b724c8-05b0-951a-016d-8911f9527874.htm language=enus -->
## TOPIC 00528: rfmxspecandotnet/html/d6b724c8-05b0-951a-016d-8911f9527874.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/d6b724c8-05b0-951a-016d-8911f9527874.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/d6b724c8-05b0-951a-016d-8911f9527874.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetFftOverlapType Method

RFmxSpecAnMXSpectrumConfigurationSetFftOverlapType Method

SpectrumMeasurementMethod

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftOverlapType(
	string selectorString,
	RFmxSpecAnMXSpectrumFftOverlapType value
)
```

```text
Public Function SetFftOverlapType ( 
	selectorString As String,
	value As RFmxSpecAnMXSpectrumFftOverlapType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumFftOverlapType**
  - Specifies the overlap type when you set the SpectrumMeasurementMethod method to SequentialFft.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/daf806e6-cab0-6a60-8136-47bb85d1d489.htm language=enus -->
## TOPIC 00529: rfmxspecandotnet/html/daf806e6-cab0-6a60-8136-47bb85d1d489.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/daf806e6-cab0-6a60-8136-47bb85d1d489.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/daf806e6-cab0-6a60-8136-47bb85d1d489.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntResults.GetAllanDeviation Method

RFmxSpecAnMXFcntResultsGetAllanDeviation Method

Gets the two-sample deviation of the measured frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllanDeviation(
	string selectorString,
	out double value
)
```

```text
Public Function GetAllanDeviation ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(String)Â method to build the selectorString.
- **value Double**
  - Upon return, contains the two-sample deviation of the measured frequency.

###### Return Value

Int32

##### Remarks

FcntResultsAllanDeviation

##### See Also

###### Reference

RFmxSpecAnMXFcntResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/db0c0904-5cd0-51c6-c84a-10a6be2bb135.htm language=enus -->
## TOPIC 00530: rfmxspecandotnet/html/db0c0904-5cd0-51c6-c84a-10a6be2bb135.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/db0c0904-5cd0-51c6-c84a-10a6be2bb135.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/db0c0904-5cd0-51c6-c84a-10a6be2bb135.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.GetMeasurementStatus Method

RFmxSpecAnMXSpurResultsGetMeasurementStatus Method

Gets the overall measurement status.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxSpecAnMXSpurMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpurMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value RFmxSpecAnMXSpurMeasurementStatus**
  - Upon return, contains the overall measurement status.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetResultsMeasurementStatus() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/db35f979-4bdd-4dff-fe40-4f3f83c108fc.htm language=enus -->
## TOPIC 00531: rfmxspecandotnet/html/db35f979-4bdd-4dff-fe40-4f3f83c108fc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/db35f979-4bdd-4dff-fe40-4f3f83c108fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/db35f979-4bdd-4dff-fe40-4f3f83c108fc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.ValidateNoiseCalibrationData Method

RFmxSpecAnMXChpConfigurationValidateNoiseCalibrationData Method

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
	out RFmxSpecAnMXChpNoiseCalibrationDataValid noiseCalibrationDataValid
)
```

```text
Public Function ValidateNoiseCalibrationData ( 
	selectorString As String,
	<OutAttribute> ByRef noiseCalibrationDataValid As RFmxSpecAnMXChpNoiseCalibrationDataValid
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **noiseCalibrationDataValid RFmxSpecAnMXChpNoiseCalibrationDataValid**
  - Upon return, contains whether the calibration data is valid.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/db52d472-da03-c15e-3ef3-a18ceebb0550.htm language=enus -->
## TOPIC 00532: rfmxspecandotnet/html/db52d472-da03-c15e-3ef3-a18ceebb0550.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/db52d472-da03-c15e-3ef3-a18ceebb0550.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/db52d472-da03-c15e-3ef3-a18ceebb0550.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.ConfigureColdSourceDutSParameters Method

RFmxSpecAnMXNFConfigurationConfigureColdSourceDutSParameters Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureColdSourceDutSParameters(
	string selectorString,
	double[] dutSParametersFrequency,
	double[] dutS21,
	double[] dutS12,
	double[] dutS11,
	double[] dutS22
)
```

```text
Public Function ConfigureColdSourceDutSParameters ( 
	selectorString As String,
	dutSParametersFrequency As Double(),
	dutS21 As Double(),
	dutS12 As Double(),
	dutS11 As Double(),
	dutS22 As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **dutSParametersFrequency Double**
  - Specifies the array of frequencies corresponding to the s-parameters of the DUT specified by the DUTS21, DUTS12, DUTS11, and DUTS22 parameters. This value is expressed in Hz.
- **dutS21 Double**
  - Specifies an array of the gains of the DUT as a method of freqency, when the output port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUTSParametersFrequency parameter.
- **dutS12 Double**
  - Specifies an array of the input-isolations of the DUT as a method of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUTSParametersFrequency parameter.
- **dutS11 Double**
  - Specifies an array of the input-reflections of the DUT as a method of frequency, when the output port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUTSParametersFrequency parameter.
- **dutS22 Double**
  - Specifies an array of the output-reflections of the DUT as a method of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUTSParametersFrequency parameter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/db70b6e8-4482-eaed-d5e4-52d5580fb209.htm language=enus -->
## TOPIC 00533: rfmxspecandotnet/html/db70b6e8-4482-eaed-d5e4-52d5580fb209.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/db70b6e8-4482-eaed-d5e4-52d5580fb209.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/db70b6e8-4482-eaed-d5e4-52d5580fb209.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtResults.FetchPhaseAndAmplitude Method

RFmxSpecAnMXPavtResultsFetchPhaseAndAmplitude Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPhaseAndAmplitude(
	string selectorString,
	double timeout,
	out double meanRelativePhase,
	out double meanRelativeAmplitude,
	out double meanAbsolutePhase,
	out double meanAbsoluteAmplitude
)
```

```text
Public Function FetchPhaseAndAmplitude ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRelativePhase As Double,
	<OutAttribute> ByRef meanRelativeAmplitude As Double,
	<OutAttribute> ByRef meanAbsolutePhase As Double,
	<OutAttribute> ByRef meanAbsoluteAmplitude As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and segment number. If you do not specify the result name, the default result instance is used. Example:"segment0""result::r1/segment0" You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRelativePhase Double**
  - Upon return, contains the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees.
- **meanRelativeAmplitude Double**
  - Upon return, contains the mean amplitude of the segment relative to the first segment of the measurement. This value is expressed in dB.
- **meanAbsolutePhase Double**
  - Upon return, contains the mean absolute phase of the segment. This value is expressed in degrees.
- **meanAbsoluteAmplitude Double**
  - Upon return, contains the mean absolute amplitude of the segment. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPavtResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dba4770a-ce59-582b-ad66-5bb1eb908be4.htm language=enus -->
## TOPIC 00534: rfmxspecandotnet/html/dba4770a-ce59-582b-ad66-5bb1eb908be4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dba4770a-ce59-582b-ad66-5bb1eb908be4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dba4770a-ce59-582b-ad66-5bb1eb908be4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXExtension Class

RFmxSpecAnMXExtension Class

Provides extension methods to create SpecAn signal configuration. These methods are added to RFmxInstrMX class.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxSpecAnMXExtension
```

```text
<ExtensionAttribute>
Public NotInheritable Class RFmxSpecAnMXExtension
```

The RFmxSpecAnMXExtension type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetSpecAnList | Creates a new SpecAn list if it doesn't exist; otherwise, it returns the existing SpecAn list. |
|  | GetSpecAnSignalConfiguration(RFmxInstrMX) | Creates a new default SpecAn signal configuration if it doesn't exist; otherwise, it returns the existing default SpecAn signal configuration. |
|  | GetSpecAnSignalConfiguration(RFmxInstrMX, String) | Creates a SpecAn signal configuration for specified signal name. Existing SpecAn signal configuration is returned if specified signal name exists. |
|  | SpecAnClearNoiseCalibrationDatabase | Clears the noise calibration database used for noise compensation. |

Top

##### Remarks

For more information about RFmx Instruments, refer to the RFmx Instruments Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dba8b4af-b6c0-5c87-b07e-d7186876ac52.htm language=enus -->
## TOPIC 00535: rfmxspecandotnet/html/dba8b4af-b6c0-5c87-b07e-d7186876ac52.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dba8b4af-b6c0-5c87-b07e-d7186876ac52.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dba8b4af-b6c0-5c87-b07e-d7186876ac52.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetNoiseCompensationEnabled Method

RFmxSpecAnMXChpConfigurationGetNoiseCompensationEnabled Method

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
public int GetNoiseCompensationEnabled(
	string selectorString,
	out RFmxSpecAnMXChpNoiseCompensationEnabled value
)
```

```text
Public Function GetNoiseCompensationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpNoiseCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpNoiseCompensationEnabled**
  - Upon return, contains whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(String, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(String, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

ChpNoiseCompensationEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dbdcb5da-cc07-d9a2-c4c0-b4be4fb8fe60.htm language=enus -->
## TOPIC 00536: rfmxspecandotnet/html/dbdcb5da-cc07-d9a2-c4c0-b4be4fb8fe60.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dbdcb5da-cc07-d9a2-c4c0-b4be4fb8fe60.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dbdcb5da-cc07-d9a2-c4c0-b4be4fb8fe60.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmAveragingEnabled Enumeration

RFmxSpecAnMXHarmAveragingEnabled Enumeration

Specifies whether to enable averaging for the Harmonics measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXHarmAveragingEnabled
```

```text
Public Enumeration RFmxSpecAnMXHarmAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The Harmonics measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the Harmonics measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dc9cd6b3-2ede-1b2a-8af2-26572f571231.htm language=enus -->
## TOPIC 00537: rfmxspecandotnet/html/dc9cd6b3-2ede-1b2a-8af2-26572f571231.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dc9cd6b3-2ede-1b2a-8af2-26572f571231.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dc9cd6b3-2ede-1b2a-8af2-26572f571231.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.SetFrequencyTrackingEnabled Method

RFmxSpecAnMXPavtConfigurationSetFrequencyTrackingEnabled Method

True

PavtFrequencyOffsetCorrectionEnabled

True

PavtSegmentType

PhaseAndAmplitude

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyTrackingEnabled(
	string selectorString,
	RFmxSpecAnMXPavtFrequencyTrackingEnabled value
)
```

```text
Public Function SetFrequencyTrackingEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXPavtFrequencyTrackingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPavtFrequencyTrackingEnabled**
  - Specifies whether to enable frequency offset correction for the measurement.

###### Return Value

Int32

##### Remarks

PavtFrequencyTrackingEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dcb370c5-904a-095d-cc9a-427bf7e9578a.htm language=enus -->
## TOPIC 00538: rfmxspecandotnet/html/dcb370c5-904a-095d-cc9a-427bf7e9578a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dcb370c5-904a-095d-cc9a-427bf7e9578a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dcb370c5-904a-095d-cc9a-427bf7e9578a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdSynchronizationMethod Enumeration

RFmxSpecAnMXDpdSynchronizationMethod Enumeration

Specifies the method used for synchronization of the acquired waveform with the reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdSynchronizationMethod
```

```text
Public Enumeration RFmxSpecAnMXDpdSynchronizationMethod
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Direct | 1 | Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when measurement sampling rate is high. |
| AliasProtected | 2 | Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when measurement sampling rate is low. Refer to DPD concept help for more information. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dcc56421-3937-f418-f1bc-25c954321506.htm language=enus -->
## TOPIC 00539: rfmxspecandotnet/html/dcc56421-3937-f418-f1bc-25c954321506.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dcc56421-3937-f418-f1bc-25c954321506.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dcc56421-3937-f418-f1bc-25c954321506.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMaximumTimingError Method

RFmxSpecAnMXDpdConfigurationGetMaximumTimingError Method

Gets the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumTimingError(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumTimingError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

DpdMaximumTimingError

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dce8da12-2bb9-5e07-83d2-749aaa84391c.htm language=enus -->
## TOPIC 00540: rfmxspecandotnet/html/dce8da12-2bb9-5e07-83d2-749aaa84391c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dce8da12-2bb9-5e07-83d2-749aaa84391c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dce8da12-2bb9-5e07-83d2-749aaa84391c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.ConfigureMeasurementInterval Method

RFmxSpecAnMXTxpConfigurationConfigureMeasurementInterval Method

Configures the acquisition time, in seconds, for the transmit power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the acquisition time, in seconds, for the TXP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPCfgMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dd3e87c6-7c25-8071-26fa-951cd716843e.htm language=enus -->
## TOPIC 00541: rfmxspecandotnet/html/dd3e87c6-7c25-8071-26fa-951cd716843e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dd3e87c6-7c25-8071-26fa-951cd716843e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dd3e87c6-7c25-8071-26fa-951cd716843e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled Enumeration

RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled Enumeration

SetAutoSetupEnabled(String, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled)

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled
```

```text
Public Enumeration RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the Harmonics for measurement. |
| True | 1 | Enables the Harmonics for measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dd3fc6f9-ee56-f955-9bc3-2405cbe8f9be.htm language=enus -->
## TOPIC 00542: rfmxspecandotnet/html/dd3fc6f9-ee56-f955-9bc3-2405cbe8f9be.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dd3fc6f9-ee56-f955-9bc3-2405cbe8f9be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dd3fc6f9-ee56-f955-9bc3-2405cbe8f9be.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetStopFrequency Method

RFmxSpecAnMXSemConfigurationSetOffsetStopFrequency Method

ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition)

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifiesthe stop frequency, in Hz, of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetStopFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dd8b381c-d189-a473-f529-939391c5cf99.htm language=enus -->
## TOPIC 00543: rfmxspecandotnet/html/dd8b381c-d189-a473-f529-939391c5cf99.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dd8b381c-d189-a473-f529-939391c5cf99.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dd8b381c-d189-a473-f529-939391c5cf99.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdMeasurementSampleRateMode Enumeration

RFmxSpecAnMXIdpdMeasurementSampleRateMode Enumeration

Specifies acquisition sample rate configuration mode.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIdpdMeasurementSampleRateMode
```

```text
Public Enumeration RFmxSpecAnMXIdpdMeasurementSampleRateMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| User | 0 | Acquisition sample rate is defined by the IDPD Meas Sample Rate (S/s) method. |
| ReferenceWaveform | 1 | Acquisition sample rate is set to match the sample rate of the reference waveform. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ddb6fa54-7873-ba3b-bed4-92b3c61c0a6f.htm language=enus -->
## TOPIC 00544: rfmxspecandotnet/html/ddb6fa54-7873-ba3b-bed4-92b3c61c0a6f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ddb6fa54-7873-ba3b-bed4-92b3c61c0a6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ddb6fa54-7873-ba3b-bed4-92b3c61c0a6f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration Methods

RFmxSpecAnMXDpdConfiguration Methods

The [RFmxSpecAnMXDpdConfiguration](fc2eeb94-1873-9c78-7bfe-c84ab09f1c9c.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the digital predistortion (DPD) measurement. |
|  | ConfigureDpdModel | Specifies the digital predistortion (DPD) model used by the DPD measurement. |
|  | ConfigureDutAverageInputPower | Configures the average power, in dBm, of the signal at the input port of the device under test. |
|  | ConfigureGeneralizedMemoryPolynomialCrossTerms | Configures the cross terms of the generalized memory polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to GeneralizedMemoryPolynomial. |
|  | ConfigureIterativeDpdEnabled | Configures the iterative computation of the DPD polynomial according to the indirect-learning architecture when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | ConfigureLookupTableAMToAMCurveFit | Configures the degree of the polynomial and the approximation method used for polynomial approximation of the AM-to-AM response of the device under test when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | ConfigureLookupTableAMToPMCurveFit | Configures the degree of the polynomial and the approximation method, used for polynomial approximation of the AM-to-PM response of the device under test when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | ConfigureLookupTableStepSize | Configures the step size, in dB, of input power levels in the predistortion lookup table when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | ConfigureLookupTableThreshold | Configures the threshold level for the samples considered for the DPD measurement when you set the SetModel(String, RFmxSpecAnMXDpdModel) to LookupTable. |
|  | ConfigureLookupTableType | Configuers the type of DPD Lookup Table. |
|  | ConfigureMeasurementInterval | Configures the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform. |
|  | ConfigureMeasurementSampleRate | Configures the acquisition sample rate, in samples per second (S/s), for the DPD measurement. |
|  | ConfigureMemoryPolynomial | Configures the order and memory depth of the DPD polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | ConfigurePreviousDpdPolynomial | Configures the previous DPD polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | ConfigureReferenceWaveform | Configures the complex baseband equivalent of the RF signal applied to the input port of the device under test while performing the DPD measurement. |
|  | ConfigureSynchronizationMethod | Configures the synchronization method used to synchronize the reference waveform and acquired waveform. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the DPD measurement. |
|  | GetApplyDpdUserLookupTableInputPower | Obsolete. Gets the input power array for the predistortion lookup table when you set the DpdApplyDpdUserDpdModel method to Lookup Table. This value is expressed in dBm. |
|  | GetApplyDpdUserLookupTableType | Obsolete. Gets the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method toUser. |
|  | GetAutoCarrierDetectionEnabled | Gets if auto detection of carrier offset and carrier bandwidth is enabled. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging. |
|  | GetAveragingEnabled | Gets whether averaging is enabled for the DPD measurement. |
|  | GetCarrierBandwidth | Gets the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
|  | GetCarrierOffset | Gets the carrier offset when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
|  | GetDutAverageInputPower | Gets the average power, in dBm, of the signal at the input port of the device under test. |
|  | GetFrequencyOffsetCorrectionEnabled | Gets whether to enable frequency offset correction for the DPD measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQOriginOffsetCorrectionEnabled | Gets the IQ origin offset correction for the measurement. |
|  | GetIterativeDpdEnabled | Gets whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture. |
|  | GetLookupTableAMToAMCurveFitOrder | Gets the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test. |
|  | GetLookupTableAMToAMCurveFitType | Gets the polynomial approximation cost-function of the device under test AM-to-AM characteristic. |
|  | GetLookupTableAMToPMCurveFitOrder | Gets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test. |
|  | GetLookupTableAMToPMCurveFitType | Gets the cost-function for polynomial approximation of the AM-to-PM characteristic of the device under test. |
|  | GetLookupTableStepSize | Gets the step size, in dB, of the input power levels in the predistortion lookup table. |
|  | GetLookupTableThresholdEnabled | Gets whether to enable thresholding of the acquired samples to be used for the DPD measurement. |
|  | GetLookupTableThresholdLevel | Gets either the relative or absolute threshold power level. |
|  | GetLookupTableThresholdType | Gets the reference for the power level used for thresholding. |
|  | GetLookupTableType | Gets the type of the DPD lookup table (LUT). |
|  | GetMaximumTimingError | Gets the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds. |
|  | GetMeasurementEnabled | Gets whether to enable DPD measurements. |
|  | GetMeasurementInterval | Gets the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform. |
|  | GetMeasurementSampleRate | Gets the acquisition sample rate, in samples per second (S/s). |
|  | GetMeasurementSampleRateMode | Gets the acquisition sample rate configuration mode. |
|  | GetMemoryPolynomialLagMemoryDepth | Gets the lag memory depth cross term of the DPD polynomial. |
|  | GetMemoryPolynomialLagOrder | Gets the order of the DPD polynomial. |
|  | GetMemoryPolynomialLagOrderType | Gets the type of terms of the lag order DPD polynomial when you set theRFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |
|  | GetMemoryPolynomialLeadMemoryDepth | Gets the lead memory depth cross term of the DPD polynomial. |
|  | GetMemoryPolynomialLeadOrder | Gets the lead order cross term of the DPD polynomial. |
|  | GetMemoryPolynomialLeadOrderType | Gets the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |
|  | GetMemoryPolynomialMaximumLag | Gets the maximum lag stagger cross term of the DPD polynomial. |
|  | GetMemoryPolynomialMaximumLead | Gets the maximum lead stagger cross term of the DPD polynomial. |
|  | GetMemoryPolynomialMemoryDepth | Gets the memory depth of the DPD polynomial. |
|  | GetMemoryPolynomialOrder | Gets the order of the DPD polynomial. |
|  | GetMemoryPolynomialOrderType | Gets the type of terms of the DPD polynomial when you set the RFmxSpecAnMXDpdModel to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | GetModel | Gets the DPD model used by the DPD measurement. |
|  | GetNmseEnabled | Gets whether to enable the normalized mean-squared error (NMSE) computation. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the DPD measurement. |
|  | GetNumberOfCarriers | Gets the number of carriers in the reference waveform when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. |
|  | GetSignalType | Gets whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. |
|  | GetSynchronizationMethod | Gets the method used for synchronization of the acquired waveform with the reference waveform. |
|  | GetTargetGainType | Gets the gain expected from the DUT after applying DPD on the input waveform. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the DPD measurement. |
|  | SetApplyDpdUserLookupTableInputPower | Obsolete. Sets the input power array for the predistortion lookup table when you set the DpdApplyDpdUserDpdModel method to Lookup Table. This value is expressed in dBm. |
|  | SetApplyDpdUserLookupTableType | Obsolete. Sets the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method toUser. |
|  | SetAutoCarrierDetectionEnabled | Sets if auto detection of carrier offset and carrier bandwidth is enabled. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXDpdAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the DPD measurement. |
|  | SetCarrierBandwidth | Sets the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
|  | SetCarrierOffset | Sets the carrier offset when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
|  | SetDutAverageInputPower | Sets the average power, in dBm, of the signal at the input port of the device under test. |
|  | SetFrequencyOffsetCorrectionEnabled | Sets whether to enable frequency offset correction for the DPD measurement. |
|  | SetIQOriginOffsetCorrectionEnabled | Sets the IQ origin offset correction for the measurement. |
|  | SetIterativeDpdEnabled | Sets whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture. |
|  | SetLookupTableAMToAMCurveFitOrder | Sets the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | SetLookupTableAMToAMCurveFitType | Sets the polynomial approximation cost-function of the device under test AM-to-AM characteristic when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | SetLookupTableAMToPMCurveFitOrder | Sets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | SetLookupTableAMToPMCurveFitType | Sets the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | SetLookupTableStepSize | Sets the step size, in dB, of the input power levels in the predistortion lookup table when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | SetLookupTableThresholdEnabled | Sets whether to enable thresholding of the acquired samples to be used for the DPD measurement when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | SetLookupTableThresholdLevel | Sets either the relative or absolute threshold power level based on the value of RFmxSpecAnMXDpdLookupTableThresholdType. |
|  | SetLookupTableThresholdType | Sets the reference for the power level used for thresholding. |
|  | SetLookupTableType | Sets the type of the DPD lookup table (LUT). |
|  | SetMaximumTimingError | Sets the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds. |
|  | SetMeasurementEnabled | Sets whether to enable the DPD measurement. |
|  | SetMeasurementInterval | Sets the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform. |
|  | SetMeasurementSampleRate | Sets the acquisition sample rate, in samples per second (S/s), when you set the SetMeasurementSampleRateMode(String, RFmxSpecAnMXDpdMeasurementSampleRateMode) method to User. |
|  | SetMeasurementSampleRateMode | Sets the acquisition sample rate configuration mode. |
|  | SetMemoryPolynomialLagMemoryDepth | Sets the lag memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetMemoryPolynomialLagOrder | Sets the order of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetMemoryPolynomialLagOrderType | Sets the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |
|  | SetMemoryPolynomialLeadMemoryDepth | Sets the lead memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetMemoryPolynomialLeadOrder | Sets the lead order cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetMemoryPolynomialLeadOrderType | Sets the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |
|  | SetMemoryPolynomialMaximumLag | Sets the maximum lag stagger cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetMemoryPolynomialMaximumLead | Sets the maximum lead stagger cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetMemoryPolynomialMemoryDepth | Sets the memory depth of the DPD polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | SetMemoryPolynomialOrder | Sets the order of the DPD polynomial when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | SetMemoryPolynomialOrderType | Sets the type of terms of the DPD polynomial when you set the RFmxSpecAnMXDpdModel to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | SetModel | Sets the DPD model used by the DPD measurement. |
|  | SetNmseEnabled | Sets whether to enable the normalized mean-squared error (NMSE) computation. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the DPD measurement. |
|  | SetNumberOfCarriers | Sets the number of carriers in the reference waveform when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. |
|  | SetSignalType | Sets whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. |
|  | SetSynchronizationMethod | Sets the method used for synchronization of the acquired waveform with the reference waveform. |
|  | SetTargetGainType | Sets the gain expected from the DUT after applying DPD on the input waveform. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ded05405-b72d-995a-838f-909e414036c9.htm language=enus -->
## TOPIC 00545: rfmxspecandotnet/html/ded05405-b72d-995a-838f-909e414036c9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ded05405-b72d-995a-838f-909e414036c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ded05405-b72d-995a-838f-909e414036c9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumResults.FetchPowerTrace Method

RFmxSpecAnMXSpectrumResultsFetchPowerTrace Method

Fetches the power trace for the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **power AnalogWaveformSingle**
  - Upon return, contains the power versus time trace.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumFetchPowerTrace() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/df690351-20ff-5557-abe1-cfa5d1645d17.htm language=enus -->
## TOPIC 00546: rfmxspecandotnet/html/df690351-20ff-5557-abe1-cfa5d1645d17.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/df690351-20ff-5557-abe1-cfa5d1645d17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/df690351-20ff-5557-abe1-cfa5d1645d17.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdLookupTableThresholdType Enumeration

RFmxSpecAnMXDpdLookupTableThresholdType Enumeration

Specifies the reference for the power level used for thresholding.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdLookupTableThresholdType
```

```text
Public Enumeration RFmxSpecAnMXDpdLookupTableThresholdType
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/df76b3b3-a678-5a2e-5cd5-3aced6283258.htm language=enus -->
## TOPIC 00547: rfmxspecandotnet/html/df76b3b3-a678-5a2e-5cd5-3aced6283258.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/df76b3b3-a678-5a2e-5cd5-3aced6283258.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/df76b3b3-a678-5a2e-5cd5-3aced6283258.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetFftOverlap Method

RFmxSpecAnMXSpectrumConfigurationSetFftOverlap Method

SpectrumSequentialFftSize

SpectrumMeasurementMethod

SequentialFft

SpectrumFftOverlapMode

UserDefined

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the samples to overlap between the consecutive chunks as a percentage of the SpectrumSequentialFftSize method when you set the SpectrumMeasurementMethod method to SequentialFft and the SpectrumFftOverlapMode method to UserDefined. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

SpectrumFftOverlap

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/dfaf00b8-7d87-67a6-9043-9fdf1996b760.htm language=enus -->
## TOPIC 00548: rfmxspecandotnet/html/dfaf00b8-7d87-67a6-9043-9fdf1996b760.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/dfaf00b8-7d87-67a6-9043-9fdf1996b760.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/dfaf00b8-7d87-67a6-9043-9fdf1996b760.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpRbwFilterType Enumeration

RFmxSpecAnMXChpRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpRbwFilterType
```

```text
Public Enumeration RFmxSpecAnMXChpRbwFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e0197951-d6db-58b3-8de2-577719ffc1b9.htm language=enus -->
## TOPIC 00549: rfmxspecandotnet/html/e0197951-d6db-58b3-8de2-577719ffc1b9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e0197951-d6db-58b3-8de2-577719ffc1b9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e0197951-d6db-58b3-8de2-577719ffc1b9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetAveragingEnabled Method

RFmxSpecAnMXSpurConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for the spurious emission (Spur) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxSpecAnMXSpurAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpurAveragingEnabled**
  - Specifies whether to enable averaging for the Spur measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e04ee748-6e89-73e2-b99a-338bd7a0d7e2.htm language=enus -->
## TOPIC 00550: rfmxspecandotnet/html/e04ee748-6e89-73e2-b99a-338bd7a0d7e2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e04ee748-6e89-73e2-b99a-338bd7a0d7e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e04ee748-6e89-73e2-b99a-338bd7a0d7e2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.ConfigureSynchronizationMethod Method

RFmxSpecAnMXAmpmConfigurationConfigureSynchronizationMethod Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSynchronizationMethod(
	string selectorString,
	RFmxSpecAnMXAmpmSynchronizationMethod synchronizationMethod
)
```

```text
Public Function ConfigureSynchronizationMethod ( 
	selectorString As String,
	synchronizationMethod As RFmxSpecAnMXAmpmSynchronizationMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **synchronizationMethod RFmxSpecAnMXAmpmSynchronizationMethod**
  - Specifies the method used for time-synchronization of acquired waveform with reference waveform.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e0574381-dc37-a493-1e00-51610125f3e9.htm language=enus -->
## TOPIC 00551: rfmxspecandotnet/html/e0574381-dc37-a493-1e00-51610125f3e9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e0574381-dc37-a493-1e00-51610125f3e9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e0574381-dc37-a493-1e00-51610125f3e9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetUserMemoryPolynomialLeadMemoryDepth Method

RFmxSpecAnMXDpdApplyDpdGetUserMemoryPolynomialLeadMemoryDepth Method

Gets the lead memory depth cross term of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUserMemoryPolynomialLeadMemoryDepth(
	string selectorString,
	out int value
)
```

```text
Public Function GetUserMemoryPolynomialLeadMemoryDepth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the lead memory depth cross term of the DPD polynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserMemoryPolynomialLeadMemoryDepth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e081ecfc-a10c-6e7a-d0e1-758489b0e08b.htm language=enus -->
## TOPIC 00552: rfmxspecandotnet/html/e081ecfc-a10c-6e7a-d0e1-758489b0e08b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e081ecfc-a10c-6e7a-d0e1-758489b0e08b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e081ecfc-a10c-6e7a-d0e1-758489b0e08b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetAbsoluteLimitStart Method

RFmxSpecAnMXSemConfigurationSetOffsetAbsoluteLimitStart Method

SetOffsetAbsoluteLimitMode(String, RFmxSpecAnMXSemOffsetAbsoluteLimitMode)

Couple

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetAbsoluteLimitStart(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetAbsoluteLimitStart ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the absolute power limit, in dBm, corresponding to the beginning of the offset segment. This power limit is also set as the absolute power limit for the offset segment when you set the SetOffsetAbsoluteLimitMode(String, RFmxSpecAnMXSemOffsetAbsoluteLimitMode) method to Couple.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetAbsoluteLimitStart() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e0ae2144-ee3a-6ba5-5075-6129ec221e9f.htm language=enus -->
## TOPIC 00553: rfmxspecandotnet/html/e0ae2144-ee3a-6ba5-5075-6129ec221e9f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e0ae2144-ee3a-6ba5-5075-6129ec221e9f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e0ae2144-ee3a-6ba5-5075-6129ec221e9f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.ConfigureSweepTime Method

RFmxSpecAnMXChpConfigurationConfigureSweepTime Method

SetSweepTimeAuto(String, RFmxSpecAnMXChpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSweepTime(
	string selectorString,
	RFmxSpecAnMXChpSweepTimeAuto sweepTimeAuto,
	double sweepTimeInterval
)
```

```text
Public Function ConfigureSweepTime ( 
	selectorString As String,
	sweepTimeAuto As RFmxSpecAnMXChpSweepTimeAuto,
	sweepTimeInterval As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sweepTimeAuto RFmxSpecAnMXChpSweepTimeAuto**
  - Specifies whether the measurement computes the sweep time.
- **sweepTimeInterval Double**
  - Specifies the sweep time, in seconds, when you set the SetSweepTimeAuto(String, RFmxSpecAnMXChpSweepTimeAuto) to False.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPCfgSweepTime() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e0db95a4-ff3f-8888-832c-31941ca50756.htm language=enus -->
## TOPIC 00554: rfmxspecandotnet/html/e0db95a4-ff3f-8888-832c-31941ca50756.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e0db95a4-ff3f-8888-832c-31941ca50756.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e0db95a4-ff3f-8888-832c-31941ca50756.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumNoiseCalibrationDataValid Enumeration

RFmxSpecAnMXSpectrumNoiseCalibrationDataValid Enumeration

selectorstring

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumNoiseCalibrationDataValid
```

```text
Public Enumeration RFmxSpecAnMXSpectrumNoiseCalibrationDataValid
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True | 1 | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e100a633-d780-ea59-9ff3-39eca7716bfc.htm language=enus -->
## TOPIC 00555: rfmxspecandotnet/html/e100a633-d780-ea59-9ff3-39eca7716bfc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e100a633-d780-ea59-9ff3-39eca7716bfc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e100a633-d780-ea59-9ff3-39eca7716bfc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmMeasurementSampleRateMode Enumeration

RFmxSpecAnMXAmpmMeasurementSampleRateMode Enumeration

Specifies whether the acquisition sample rate is based on the reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAmpmMeasurementSampleRateMode
```

```text
Public Enumeration RFmxSpecAnMXAmpmMeasurementSampleRateMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| User | 0 | The acquisition sample rate is defined by the value returned by the GetMeasurementSampleRate(String, Double) method. |
| ReferenceWaveform | 1 | The acquisition sample rate is set to match the sample rate of the reference waveform. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e11f4e95-3246-8333-78d9-6d79ee4d285b.htm language=enus -->
## TOPIC 00556: rfmxspecandotnet/html/e11f4e95-3246-8333-78d9-6d79ee4d285b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e11f4e95-3246-8333-78d9-6d79ee4d285b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e11f4e95-3246-8333-78d9-6d79ee4d285b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetIQOriginOffsetCorrectionEnabled Method

RFmxSpecAnMXAmpmConfigurationSetIQOriginOffsetCorrectionEnabled Method

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
	RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled value
)
```

```text
Public Function SetIQOriginOffsetCorrectionEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled**
  - Specifies the IQ origin offset correction for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e1211b01-fb01-9f7a-c881-b7f2e1610638.htm language=enus -->
## TOPIC 00557: rfmxspecandotnet/html/e1211b01-fb01-9f7a-c881-b7f2e1610638.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e1211b01-fb01-9f7a-c881-b7f2e1610638.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e1211b01-fb01-9f7a-c881-b7f2e1610638.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.GetNumberOfHarmonics Method

RFmxSpecAnMXHarmConfigurationGetNumberOfHarmonics Method

Gets the number of harmonics, including fundamental, to measure.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfHarmonics(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfHarmonics ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of harmonics, including fundamental, to measure.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmGetNumberOfHarmonics() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e1404611-b399-f33c-c470-b5d0e784566e.htm language=enus -->
## TOPIC 00558: rfmxspecandotnet/html/e1404611-b399-f33c-c470-b5d0e784566e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e1404611-b399-f33c-c470-b5d0e784566e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e1404611-b399-f33c-c470-b5d0e784566e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.ConfigureReferencePowerType Method

RFmxSpecAnMXAmpmConfigurationConfigureReferencePowerType Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureReferencePowerType(
	string selectorString,
	RFmxSpecAnMXAmpmReferencePowerType referencePowerType
)
```

```text
Public Function ConfigureReferencePowerType ( 
	selectorString As String,
	referencePowerType As RFmxSpecAnMXAmpmReferencePowerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **referencePowerType RFmxSpecAnMXAmpmReferencePowerType**
  - Specifies the reference power used for AM to AM and AM to PM traces.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e14c267d-be75-825d-b933-a5ae5f4de56b.htm language=enus -->
## TOPIC 00559: rfmxspecandotnet/html/e14c267d-be75-825d-b933-a5ae5f4de56b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e14c267d-be75-825d-b933-a5ae5f4de56b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e14c267d-be75-825d-b933-a5ae5f4de56b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.ConfigureAveraging Method

RFmxSpecAnMXChpConfigurationConfigureAveraging Method

Configures averaging for the channel power (CHP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxSpecAnMXChpAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxSpecAnMXChpAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxSpecAnMXChpAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxSpecAnMXChpAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxSpecAnMXChpAveragingEnabled**
  - Specifies whether to enable averaging for the measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXChpAveragingEnabled) to True.
- **averagingType RFmxSpecAnMXChpAveragingType**
  - Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPCfgAveraging() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e157611f-4a15-d3d7-bf4b-062385710eea.htm language=enus -->
## TOPIC 00560: rfmxspecandotnet/html/e157611f-4a15-d3d7-bf4b-062385710eea.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e157611f-4a15-d3d7-bf4b-062385710eea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e157611f-4a15-d3d7-bf4b-062385710eea.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetAveragingCount Method

RFmxSpecAnMXIMConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxSpecAnMXIMAveragingEnabled)

True

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
  - Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXIMAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e1a0be14-3a80-fa34-0005-237ada333766.htm language=enus -->
## TOPIC 00561: rfmxspecandotnet/html/e1a0be14-3a80-fa34-0005-237ada333766.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e1a0be14-3a80-fa34-0005-237ada333766.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e1a0be14-3a80-fa34-0005-237ada333766.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.ConfigureAveraging Method

RFmxSpecAnMXSpectrumConfigurationConfigureAveraging Method

Configures averaging for the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxSpecAnMXSpectrumAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxSpecAnMXSpectrumAveragingType averagingtype
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxSpecAnMXSpectrumAveragingEnabled,
	averagingCount As Integer,
	averagingtype As RFmxSpecAnMXSpectrumAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxSpecAnMXSpectrumAveragingEnabled**
  - Specifies whether to enable averaging for the measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXSpectrumAveragingEnabled) method to True.
- **averagingtype RFmxSpecAnMXSpectrumAveragingType**
  - Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumCfgAveraging() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e1d6db72-ce86-4168-b534-840d87ae0fc3.htm language=enus -->
## TOPIC 00562: rfmxspecandotnet/html/e1d6db72-ce86-4168-b534-840d87ae0fc3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e1d6db72-ce86-4168-b534-840d87ae0fc3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e1d6db72-ce86-4168-b534-840d87ae0fc3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.FetchMeasurementStatus Method

RFmxSpecAnMXSpurResultsFetchMeasurementStatus Method

Fetches the overall spurious emission (Spur) measurement status.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurementStatus(
	string selectorString,
	double timeout,
	out RFmxSpecAnMXSpurMeasurementStatus measurementStatus
)
```

```text
Public Function FetchMeasurementStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxSpecAnMXSpurMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus RFmxSpecAnMXSpurMeasurementStatus**
  - Upon return contains the overall measurement status.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurFetchMeasurementStatus() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e4151519-6901-0958-3a87-ef245a68c749.htm language=enus -->
## TOPIC 00563: rfmxspecandotnet/html/e4151519-6901-0958-3a87-ef245a68c749.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e4151519-6901-0958-3a87-ef245a68c749.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e4151519-6901-0958-3a87-ef245a68c749.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetLocalPeakSearchEnabled Method

RFmxSpecAnMXIMConfigurationSetLocalPeakSearchEnabled Method

Sets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLocalPeakSearchEnabled(
	string selectorString,
	RFmxSpecAnMXIMLocalPeakSearchEnabled value
)
```

```text
Public Function SetLocalPeakSearchEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXIMLocalPeakSearchEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIMLocalPeakSearchEnabled**
  - Specifies whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets.

###### Return Value

Int32

##### Remarks

IMLocalPeakSearchEnabled

True

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e43c0bb5-c194-d924-84b3-063e144794b7.htm language=enus -->
## TOPIC 00564: rfmxspecandotnet/html/e43c0bb5-c194-d924-84b3-063e144794b7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e43c0bb5-c194-d924-84b3-063e144794b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e43c0bb5-c194-d924-84b3-063e144794b7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.GetCfrWindowLength Method

RFmxSpecAnMXDpdPreDpdGetCfrWindowLength Method

DpdPreDpdCfrEnabled

True

DpdPreDpdCfrMethod

PeakWindowing

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrWindowLength(
	string selectorString,
	out int value
)
```

```text
Public Function GetCfrWindowLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the maximum window length to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to PeakWindowing.

###### Return Value

Int32

##### Remarks

DpdPreDpdCfrWindowLength

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e446dbd6-72e3-aa10-ce16-fbfd26b4d80f.htm language=enus -->
## TOPIC 00565: rfmxspecandotnet/html/e446dbd6-72e3-aa10-ce16-fbfd26b4d80f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e446dbd6-72e3-aa10-ce16-fbfd26b4d80f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e446dbd6-72e3-aa10-ce16-fbfd26b4d80f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetCompressionPointGainReference Method

RFmxSpecAnMXAmpmConfigurationGetCompressionPointGainReference Method

Gets the gain reference for compression point calculation.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCompressionPointGainReference(
	string selectorString,
	out RFmxSpecAnMXAmpmCompressionPointGainReference value
)
```

```text
Public Function GetCompressionPointGainReference ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmCompressionPointGainReference
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmCompressionPointGainReference**
  - Upon return, contains the gain reference for compression point calculation.

###### Return Value

Int32

##### Remarks

AmpmCompressionPointGainReference

Auto

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e49bf68f-2e27-5356-9a08-2647838a346d.htm language=enus -->
## TOPIC 00566: rfmxspecandotnet/html/e49bf68f-2e27-5356-9a08-2647838a346d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e49bf68f-2e27-5356-9a08-2647838a346d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e49bf68f-2e27-5356-9a08-2647838a346d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetRangeStopFrequency Method

RFmxSpecAnMXSpurConfigurationGetRangeStopFrequency Method

Gets the stop frequency of the frequency range, in hertz (Hz), for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeStopFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetRangeStopFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the stop of the frequency range, in Hz, for the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetRangeStopFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e4ad216c-cf67-b72e-1485-5d1a95414553.htm language=enus -->
## TOPIC 00567: rfmxspecandotnet/html/e4ad216c-cf67-b72e-1485-5d1a95414553.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e4ad216c-cf67-b72e-1485-5d1a95414553.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e4ad216c-cf67-b72e-1485-5d1a95414553.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetRangeStopFrequency Method

RFmxSpecAnMXPhaseNoiseConfigurationSetRangeStopFrequency Method

Sets the stop frequency for the specified range.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeStopFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetRangeStopFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the phasenoiserange number. Example: "phasenoiserange0". You can use the BuildRangeString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the stop frequency for the specified subrange when you set the Phase Noise Range Definition method to Manual.

###### Return Value

Int32

##### Remarks

PhaseNoiseRangeStopFrequency

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e4ae2810-8665-872f-3ec8-bc97bd804d7d.htm language=enus -->
## TOPIC 00568: rfmxspecandotnet/html/e4ae2810-8665-872f-3ec8-bc97bd804d7d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e4ae2810-8665-872f-3ec8-bc97bd804d7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e4ae2810-8665-872f-3ec8-bc97bd804d7d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetLookupTableAMToPMCurveFitType Method

RFmxSpecAnMXDpdConfigurationGetLookupTableAMToPMCurveFitType Method

Gets the cost-function for polynomial approximation of the AM-to-PM characteristic of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLookupTableAMToPMCurveFitType(
	string selectorString,
	out RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType value
)
```

```text
Public Function GetLookupTableAMToPMCurveFitType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType**
  - Upon return, contains the cost-function for polynomial approximation of the AM-to-PM characteristic of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableAMtoPMCurveFitType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e4b25edc-47d9-105d-c43b-55272e0d1a1d.htm language=enus -->
## TOPIC 00569: rfmxspecandotnet/html/e4b25edc-47d9-105d-c43b-55272e0d1a1d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e4b25edc-47d9-105d-c43b-55272e0d1a1d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e4b25edc-47d9-105d-c43b-55272e0d1a1d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.GetLowerOffsetRelativePower Method

RFmxSpecAnMXAcpResultsGetLowerOffsetRelativePower Method

Gets the lower offset channel power, in dB, measured relative to the integrated power of the reference carrier.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the lower offset channel power, in dB, measured relative to the integrated power of the reference carrier.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsLowerOffsetRelativePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e4cfc78f-0e95-3387-2732-a5d6be1c67cc.htm language=enus -->
## TOPIC 00570: rfmxspecandotnet/html/e4cfc78f-0e95-3387-2732-a5d6be1c67cc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e4cfc78f-0e95-3387-2732-a5d6be1c67cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e4cfc78f-0e95-3387-2732-a5d6be1c67cc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetNoiseCompensationEnabled Method

RFmxSpecAnMXAcpConfigurationGetNoiseCompensationEnabled Method

Gets whether compensation of the channel powers for the inherent noise floor of the RF signal analyzer is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCompensationEnabled(
	string selectorString,
	out RFmxSpecAnMXAcpNoiseCompensationEnabled value
)
```

```text
Public Function GetNoiseCompensationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpNoiseCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpNoiseCompensationEnabled**
  - Upon return, indicates whether compensation of the channel powers for the inherent noise floor of the RF signal analyzer is enabled.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetNoiseCompensationEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e4e98a4b-0b03-cb97-77b1-99bab384c5d2.htm language=enus -->
## TOPIC 00571: rfmxspecandotnet/html/e4e98a4b-0b03-cb97-77b1-99bab384c5d2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e4e98a4b-0b03-cb97-77b1-99bab384c5d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e4e98a4b-0b03-cb97-77b1-99bab384c5d2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.GetMeasurementSampleRateMode Method

RFmxSpecAnMXIdpdConfigurationGetMeasurementSampleRateMode Method

Gets acquisition sample rate configuration mode.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementSampleRateMode(
	string selectorString,
	out RFmxSpecAnMXIdpdMeasurementSampleRateMode value
)
```

```text
Public Function GetMeasurementSampleRateMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIdpdMeasurementSampleRateMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIdpdMeasurementSampleRateMode**
  - Upon return, contains acquisition sample rate configuration mode.

###### Return Value

Int32

##### Remarks

IdpdMeasurementSampleRateMode

ReferenceWaveform

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e52ed899-6db7-2659-0ac2-87718c89d6a6.htm language=enus -->
## TOPIC 00572: rfmxspecandotnet/html/e52ed899-6db7-2659-0ac2-87718c89d6a6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e52ed899-6db7-2659-0ac2-87718c89d6a6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e52ed899-6db7-2659-0ac2-87718c89d6a6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.SetLowerIntermodFrequency Method

RFmxSpecAnMXIMConfigurationSetLowerIntermodFrequency Method

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLowerIntermodFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetLowerIntermodFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMLowerIntermodFrequency

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e553944e-077c-690d-4903-56104158e286.htm language=enus -->
## TOPIC 00573: rfmxspecandotnet/html/e553944e-077c-690d-4903-56104158e286.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e553944e-077c-690d-4903-56104158e286.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e553944e-077c-690d-4903-56104158e286.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseResults.GetResidualPMInRadian Method

RFmxSpecAnMXPhaseNoiseResultsGetResidualPMInRadian Method

Gets the residual PM in radians.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetResidualPMInRadian(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetResidualPMInRadian ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the residual PM in radians.

###### Return Value

Int32

##### Remarks

PhaseNoiseResultsResidualPMInRadian

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e5ad9d73-1d58-b43e-9da4-d9235f748be0.htm language=enus -->
## TOPIC 00574: rfmxspecandotnet/html/e5ad9d73-1d58-b43e-9da4-d9235f748be0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e5ad9d73-1d58-b43e-9da4-d9235f748be0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e5ad9d73-1d58-b43e-9da4-d9235f748be0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto Enumeration

RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto Enumeration

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto
```

```text
Public Enumeration RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | RFmx uses the averages that you set for the SetNoiseCalibrationAveragingCount(String, Int32) method. |
| True | 1 | RFmx uses a noise calibration averaging count of 32. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e61290b2-65c3-06de-9e71-c7d59eee4510.htm language=enus -->
## TOPIC 00575: rfmxspecandotnet/html/e61290b2-65c3-06de-9e71-c7d59eee4510.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e61290b2-65c3-06de-9e71-c7d59eee4510.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e61290b2-65c3-06de-9e71-c7d59eee4510.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.ConfigureRbwFilter Method

RFmxSpecAnMXObwConfigurationConfigureRbwFilter Method

Configures the resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRbwFilter(
	string selectorString,
	RFmxSpecAnMXObwRbwAutoBandwidth rbwAuto,
	double rbw,
	RFmxSpecAnMXObwRbwFilterType rbwFilterType
)
```

```text
Public Function ConfigureRbwFilter ( 
	selectorString As String,
	rbwAuto As RFmxSpecAnMXObwRbwAutoBandwidth,
	rbw As Double,
	rbwFilterType As RFmxSpecAnMXObwRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rbwAuto RFmxSpecAnMXObwRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Spectrum topic for more details on RBW and sweep time.
- **rbw Double**
  - Specifies the bandwidth, in hertz (Hz), of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxSpecAnMXObwRbwAutoBandwidth) method to False.
- **rbwFilterType RFmxSpecAnMXObwRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWCfgRBWFilter() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e6e5e4dc-8918-8ca4-9486-ff33dd491844.htm language=enus -->
## TOPIC 00576: rfmxspecandotnet/html/e6e5e4dc-8918-8ca4-9486-ff33dd491844.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e6e5e4dc-8918-8ca4-9486-ff33dd491844.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e6e5e4dc-8918-8ca4-9486-ff33dd491844.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNF Class

RFmxSpecAnMXNF Class

Represents the NF measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXNF : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXNF
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXNF type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXNFConfiguration instance that provides methods to configure the NF measurement |
|  | Results | Gets the RFmxSpecAnMXNFResults instance that provides methods to fetch and read the NF measurement results. |

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e6e6f072-f85d-a48c-a368-8061c13e7be2.htm language=enus -->
## TOPIC 00577: rfmxspecandotnet/html/e6e6f072-f85d-a48c-a368-8061c13e7be2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e6e6f072-f85d-a48c-a368-8061c13e7be2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e6e6f072-f85d-a48c-a368-8061c13e7be2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetIQPowerEdgeTriggerLevel Method

RFmxSpecAnMXGetIQPowerEdgeTriggerLevel Method

Relative

Absolute

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains the power level at which the device triggers. This value is expressed in dB when you set the GetIQPowerEdgeTriggerLevelType method to Relative; and is expressed in dBm when you set the GetIQPowerEdgeTriggerLevelType method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_GetIQPowerEdgeTriggerLevel() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e7069082-f1e6-afe3-3643-47218953643d.htm language=enus -->
## TOPIC 00578: rfmxspecandotnet/html/e7069082-f1e6-afe3-3643-47218953643d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e7069082-f1e6-afe3-3643-47218953643d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e7069082-f1e6-afe3-3643-47218953643d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtResults.GetMeanAbsolutePhase Method

RFmxSpecAnMXPavtResultsGetMeanAbsolutePhase Method

Gets the mean absolute phase of the segment. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanAbsolutePhase(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanAbsolutePhase ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and PavtSegment number. Example: "segment0", "result::r1/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the mean absolute phase of the segment. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

PavtResultsMeanAbsolutePhase

##### See Also

###### Reference

RFmxSpecAnMXPavtResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e726952f-14b2-9856-f000-b248851828d4.htm language=enus -->
## TOPIC 00579: rfmxspecandotnet/html/e726952f-14b2-9856-f000-b248851828d4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e726952f-14b2-9856-f000-b248851828d4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e726952f-14b2-9856-f000-b248851828d4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetUserMemoryPolynomialOrder Method

RFmxSpecAnMXDpdApplyDpdSetUserMemoryPolynomialOrder Method

SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel)

MemoryPolynomial

GeneralizedMemoryPolynomial

RFmxSpecAnMXDpdApplyDpdConfigurationInput

User

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUserMemoryPolynomialOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetUserMemoryPolynomialOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Contains the order of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDUserMemoryPolynomialOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e7294e10-e6b1-3d59-cca1-4d5f7d0607dc.htm language=enus -->
## TOPIC 00580: rfmxspecandotnet/html/e7294e10-e6b1-3d59-cca1-4d5f7d0607dc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e7294e10-e6b1-3d59-cca1-4d5f7d0607dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e7294e10-e6b1-3d59-cca1-4d5f7d0607dc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.GetRbwFilterBandwidth Method

RFmxSpecAnMXFcntConfigurationGetRbwFilterBandwidth Method

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

This method maps to the RFmxSpecAn_FCntGetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e763cb5e-a80b-ded4-d408-61d29525ffcd.htm language=enus -->
## TOPIC 00581: rfmxspecandotnet/html/e763cb5e-a80b-ded4-d408-61d29525ffcd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e763cb5e-a80b-ded4-d408-61d29525ffcd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e763cb5e-a80b-ded4-d408-61d29525ffcd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.ConfigureSpotNoiseFrequencyList Method

RFmxSpecAnMXPhaseNoiseConfigurationConfigureSpotNoiseFrequencyList Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSpotNoiseFrequencyList(
	string selectorString,
	double[] frequencyList
)
```

```text
Public Function ConfigureSpotNoiseFrequencyList ( 
	selectorString As String,
	frequencyList As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **frequencyList Double**
  - Specifies an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e8173e44-6a8d-9457-c990-32dbced17b53.htm language=enus -->
## TOPIC 00582: rfmxspecandotnet/html/e8173e44-6a8d-9457-c990-32dbced17b53.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e8173e44-6a8d-9457-c990-32dbced17b53.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e8173e44-6a8d-9457-c990-32dbced17b53.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwResults.GetOccupiedBandwidth Method

RFmxSpecAnMXObwResultsGetOccupiedBandwidth Method

SetRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the bandwidth, in Hz, that occupies the percentage of the total power of the signal that you specify in the SetRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWGetResultsOccupiedBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e88a0d1c-0f5f-df47-d0ec-dccbd068bb37.htm language=enus -->
## TOPIC 00583: rfmxspecandotnet/html/e88a0d1c-0f5f-df47-d0ec-dccbd068bb37.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e88a0d1c-0f5f-df47-d0ec-dccbd068bb37.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e88a0d1c-0f5f-df47-d0ec-dccbd068bb37.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetAllTracesEnabled Method

RFmxSpecAnMXChpConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement.

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
  - to enable the traces to be stored and retrieved after performing the CHP measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetAllTracesEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e8907ed2-6624-72c2-9472-59af02327956.htm language=enus -->
## TOPIC 00584: rfmxspecandotnet/html/e8907ed2-6624-72c2-9472-59af02327956.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e8907ed2-6624-72c2-9472-59af02327956.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e8907ed2-6624-72c2-9472-59af02327956.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetRbwFilterBandwidth Method

RFmxSpecAnMXSemConfigurationGetOffsetRbwFilterBandwidth Method

Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRbwFilterBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetRbwFilterBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the bandwidth, in Hz, of the RBW filter used to sweep the acquired offset segment.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e8be7924-0c44-e70d-31f8-0c4225a1e6ec.htm language=enus -->
## TOPIC 00585: rfmxspecandotnet/html/e8be7924-0c44-e70d-31f8-0c4225a1e6ec.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e8be7924-0c44-e70d-31f8-0c4225a1e6ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e8be7924-0c44-e70d-31f8-0c4225a1e6ec.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetYFactorNoiseSourceOffTemperature Method

RFmxSpecAnMXNFConfigurationGetYFactorNoiseSourceOffTemperature Method

Gets the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetYFactorNoiseSourceOffTemperature(
	string selectorString,
	out double value
)
```

```text
Public Function GetYFactorNoiseSourceOffTemperature ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin.

###### Return Value

Int32

##### Remarks

NFYFactorNoiseSourceOffTemperature

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e9178994-0308-8430-b046-96437e4ce6a1.htm language=enus -->
## TOPIC 00586: rfmxspecandotnet/html/e9178994-0308-8430-b046-96437e4ce6a1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e9178994-0308-8430-b046-96437e4ce6a1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e9178994-0308-8430-b046-96437e4ce6a1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdResults.FetchDpdPolynomial Method

RFmxSpecAnMXDpdResultsFetchDpdPolynomial Method

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
public int FetchDpdPolynomial(
	string selectorString,
	double timeout,
	ref ComplexSingle[] dpdPolynomial
)
```

```text
Public Function FetchDpdPolynomial ( 
	selectorString As String,
	timeout As Double,
	ByRef dpdPolynomial As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement.
- **dpdPolynomial ComplexSingle**
  - Upon return, contains the memory polynomial or generalized memory polynomial coefficients when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDFetchDPDPolynomial() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/e9c9f52c-73d5-698b-c853-63d79ae0cca3.htm language=enus -->
## TOPIC 00587: rfmxspecandotnet/html/e9c9f52c-73d5-698b-c853-63d79ae0cca3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/e9c9f52c-73d5-698b-c853-63d79ae0cca3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/e9c9f52c-73d5-698b-c853-63d79ae0cca3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.ConfigureMeasurementMethod Method

RFmxSpecAnMXSpectrumConfigurationConfigureMeasurementMethod Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementMethod(
	string selectorString,
	RFmxSpecAnMXSpectrumMeasurementMethod measurementMethod
)
```

```text
Public Function ConfigureMeasurementMethod ( 
	selectorString As String,
	measurementMethod As RFmxSpecAnMXSpectrumMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementMethod RFmxSpecAnMXSpectrumMeasurementMethod**
  - Specifies the method for performing the Spectrum measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eacbe473-479a-fe3d-6cbd-59531ee93dd1.htm language=enus -->
## TOPIC 00588: rfmxspecandotnet/html/eacbe473-479a-fe3d-6cbd-59531ee93dd1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eacbe473-479a-fe3d-6cbd-59531ee93dd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eacbe473-479a-fe3d-6cbd-59531ee93dd1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.SetMeasurementInterval Method

RFmxSpecAnMXFcntConfigurationSetMeasurementInterval Method

Sets the acquisition time, in seconds, for the frequency count (Fcnt) measurement.

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
  - Specifies the acquisition time, in seconds, for the Fcnt measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntSetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eaf06c83-f0f2-85e5-e786-99a4d4b21304.htm language=enus -->
## TOPIC 00589: rfmxspecandotnet/html/eaf06c83-f0f2-85e5-e786-99a4d4b21304.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eaf06c83-f0f2-85e5-e786-99a4d4b21304.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eaf06c83-f0f2-85e5-e786-99a4d4b21304.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpNoiseCalibrationAveragingAuto Enumeration

RFmxSpecAnMXChpNoiseCalibrationAveragingAuto Enumeration

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpNoiseCalibrationAveragingAuto
```

```text
Public Enumeration RFmxSpecAnMXChpNoiseCalibrationAveragingAuto
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | RFmx uses the averages that you set for the SetNoiseCalibrationAveragingCount(String, Int32) method. |
| True | 1 | RFmx uses a noise calibration averaging count of 32. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eafc8526-973f-c560-800f-c4fcd17e9e5c.htm language=enus -->
## TOPIC 00590: rfmxspecandotnet/html/eafc8526-973f-c560-800f-c4fcd17e9e5c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eafc8526-973f-c560-800f-c4fcd17e9e5c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eafc8526-973f-c560-800f-c4fcd17e9e5c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.ConfigureLookupTableCorrectionType Method

RFmxSpecAnMXDpdApplyDpdConfigureLookupTableCorrectionType Method

SetModel(String, RFmxSpecAnMXDpdModel)

LookupTable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureLookupTableCorrectionType(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType lutCorrectionType
)
```

```text
Public Function ConfigureLookupTableCorrectionType ( 
	selectorString As String,
	lutCorrectionType As RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **lutCorrectionType RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType**
  - Specifies the predistortion type when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgApplyDPDLookupTableCorrectionType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eb02bedb-685f-8949-4189-6141e4a762fe.htm language=enus -->
## TOPIC 00591: rfmxspecandotnet/html/eb02bedb-685f-8949-4189-6141e4a762fe.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eb02bedb-685f-8949-4189-6141e4a762fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eb02bedb-685f-8949-4189-6141e4a762fe.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.GetCfrNumberOfCarriers Method

RFmxSpecAnMXDpdPreDpdGetCfrNumberOfCarriers Method

DpdPreDpdCfrEnabled

DpdPreDpdCfrFilterEnabled

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrNumberOfCarriers(
	string selectorString,
	out int value
)
```

```text
Public Function GetCfrNumberOfCarriers ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of carriers in the input waveform when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True.

###### Return Value

Int32

##### Remarks

DpdPreDpdCfrNumberOfCarriers

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eb52c07f-7b40-4c9b-237e-e439612d4f90.htm language=enus -->
## TOPIC 00592: rfmxspecandotnet/html/eb52c07f-7b40-4c9b-237e-e439612d4f90.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eb52c07f-7b40-4c9b-237e-e439612d4f90.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eb52c07f-7b40-4c9b-237e-e439612d4f90.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetStartFrequency Method

RFmxSpecAnMXSemConfigurationGetOffsetStartFrequency Method

ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetStartFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetStartFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetStartFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eb8e45d5-3d5f-9966-0165-b616c30511c5.htm language=enus -->
## TOPIC 00593: rfmxspecandotnet/html/eb8e45d5-3d5f-9966-0165-b616c30511c5.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eb8e45d5-3d5f-9966-0165-b616c30511c5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eb8e45d5-3d5f-9966-0165-b616c30511c5.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.GetLowerOffsetAbsolutePower Method

RFmxSpecAnMXAcpResultsGetLowerOffsetAbsolutePower Method

Gets the lower offset channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the lower offset channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsLowerOffsetAbsolutePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ebb51323-e2e6-757f-51d0-4e988ad6a079.htm language=enus -->
## TOPIC 00594: rfmxspecandotnet/html/ebb51323-e2e6-757f-51d0-4e988ad6a079.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ebb51323-e2e6-757f-51d0-4e988ad6a079.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ebb51323-e2e6-757f-51d0-4e988ad6a079.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetCalibrationLossCompensationEnabled Method

RFmxSpecAnMXNFConfigurationGetCalibrationLossCompensationEnabled Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCalibrationLossCompensationEnabled(
	string selectorString,
	out RFmxSpecAnMXNFCalibrationLossCompensationEnabled value
)
```

```text
Public Function GetCalibrationLossCompensationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXNFCalibrationLossCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFCalibrationLossCompensationEnabled**
  - Upon return, contains whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the SetYFactorNoiseSourceLoss(String, Double) method.

###### Return Value

Int32

##### Remarks

NFCalibrationLossCompensationEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ebd3e73b-1b00-46c1-e520-e8b3c253d6f1.htm language=enus -->
## TOPIC 00595: rfmxspecandotnet/html/ebd3e73b-1b00-46c1-e520-e8b3c253d6f1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ebd3e73b-1b00-46c1-e520-e8b3c253d6f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ebd3e73b-1b00-46c1-e520-e8b3c253d6f1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetNoiseCompensationType Method

RFmxSpecAnMXSpectrumConfigurationGetNoiseCompensationType Method

Gets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNoiseCompensationType(
	string selectorString,
	out RFmxSpecAnMXSpectrumNoiseCompensationType value
)
```

```text
Public Function GetNoiseCompensationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumNoiseCompensationType**
  - Upon return, contains the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

SpectrumNoiseCompensationType

AnalyzerAndTermination

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ebd44448-d9c6-9c44-2c85-40777a93aa98.htm language=enus -->
## TOPIC 00596: rfmxspecandotnet/html/ebd44448-d9c6-9c44-2c85-40777a93aa98.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ebd44448-d9c6-9c44-2c85-40777a93aa98.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ebd44448-d9c6-9c44-2c85-40777a93aa98.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetAttributeInt Method

RFmxSpecAnMXGetAttributeInt Method

Gets the value of an RFmx 32-bit integer (int32) attribute.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_GetAttributeI32() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ebe27e4f-060f-6bed-0a4f-012e924a9f38.htm language=enus -->
## TOPIC 00597: rfmxspecandotnet/html/ebe27e4f-060f-6bed-0a4f-012e924a9f38.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ebe27e4f-060f-6bed-0a4f-012e924a9f38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ebe27e4f-060f-6bed-0a4f-012e924a9f38.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetDetectorType Method

RFmxSpecAnMXAcpConfigurationSetDetectorType Method

Sets the type of detector to be used.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDetectorType(
	string selectorString,
	RFmxSpecAnMXAcpDetectorType value
)
```

```text
Public Function SetDetectorType ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpDetectorType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpDetectorType**
  - Specifies the type of detector to be used.

###### Return Value

Int32

##### Remarks

AcpDetectorType

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ebfc793a-d70b-34c5-a215-82b9f3788818.htm language=enus -->
## TOPIC 00598: rfmxspecandotnet/html/ebfc793a-d70b-34c5-a215-82b9f3788818.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ebfc793a-d70b-34c5-a215-82b9f3788818.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ebfc793a-d70b-34c5-a215-82b9f3788818.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpThresholdType Enumeration

RFmxSpecAnMXTxpThresholdType Enumeration

Specifies the reference for the power level used for thresholding.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXTxpThresholdType
```

```text
Public Enumeration RFmxSpecAnMXTxpThresholdType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Relative | 0 | Specifies that the threshold is relative to the peak power, in dB, of the acquired samples. |
| Absolute | 1 | Specifies that the threshold is the absolute power, in dBm. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ebfcaa36-2bda-9d1b-0711-ddd0d9650757.htm language=enus -->
## TOPIC 00599: rfmxspecandotnet/html/ebfcaa36-2bda-9d1b-0711-ddd0d9650757.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ebfcaa36-2bda-9d1b-0711-ddd0d9650757.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ebfcaa36-2bda-9d1b-0711-ddd0d9650757.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetCancellationReferencePhaseNoise Method

RFmxSpecAnMXPhaseNoiseConfigurationSetCancellationReferencePhaseNoise Method

Sets an array of reference phase noise at the frequency offsets.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCancellationReferencePhaseNoise(
	string selectorString,
	float[] value
)
```

```text
Public Function SetCancellationReferencePhaseNoise ( 
	selectorString As String,
	value As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Single**
  - Specifies an array of reference phase noise at the frequencies specified by the Phase Noise Cancellation Frequency method.

###### Return Value

Int32

##### Remarks

PhaseNoiseCancellationReferencePhaseNoise

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ec0c5133-3eac-c4ff-b7c8-c1557ad4935b.htm language=enus -->
## TOPIC 00600: rfmxspecandotnet/html/ec0c5133-3eac-c4ff-b7c8-c1557ad4935b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ec0c5133-3eac-c4ff-b7c8-c1557ad4935b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ec0c5133-3eac-c4ff-b7c8-c1557ad4935b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMemoryPolynomialLeadOrderType Method

RFmxSpecAnMXDpdConfigurationSetMemoryPolynomialLeadOrderType Method

RFmxSpecAnMXDpdModel

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMemoryPolynomialLeadOrderType(
	string selectorString,
	RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType value
)
```

```text
Public Function SetMemoryPolynomialLeadOrderType ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType**
  - Specifies the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ec685522-b6b2-f863-1a36-311184e4fad1.htm language=enus -->
## TOPIC 00601: rfmxspecandotnet/html/ec685522-b6b2-f863-1a36-311184e4fad1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ec685522-b6b2-f863-1a36-311184e4fad1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ec685522-b6b2-f863-1a36-311184e4fad1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetFundamentalLowerToneFrequency Method

RFmxSpecAnMXIMConfigurationGetFundamentalLowerToneFrequency Method

Gets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFundamentalLowerToneFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetFundamentalLowerToneFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

IMFundamentalLowerToneFrequency

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ec878053-cb81-2f4f-6144-2f1ed7bfc15a.htm language=enus -->
## TOPIC 00602: rfmxspecandotnet/html/ec878053-cb81-2f4f-6144-2f1ed7bfc15a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ec878053-cb81-2f4f-6144-2f1ed7bfc15a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ec878053-cb81-2f4f-6144-2f1ed7bfc15a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFDutOutputLossCompensationEnabled Enumeration

RFmxSpecAnMXNFDutOutputLossCompensationEnabled Enumeration

Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFDutOutputLossCompensationEnabled
```

```text
Public Enumeration RFmxSpecAnMXNFDutOutputLossCompensationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The NF measurement ignores ohmic losses. |
| True | 1 | The NF measurement accounts for the ohmic losses. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ec8ba031-232a-fe6f-869a-c3130167efb3.htm language=enus -->
## TOPIC 00603: rfmxspecandotnet/html/ec8ba031-232a-fe6f-869a-c3130167efb3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ec8ba031-232a-fe6f-869a-c3130167efb3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ec8ba031-232a-fe6f-869a-c3130167efb3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetMeasurementEnabled Method

RFmxSpecAnMXChpConfigurationGetMeasurementEnabled Method

Gets whether the channel power (CHP) measurement is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - if the CHP measurement is enabled; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eca95e7f-5e6e-e537-be11-2ca8a627779f.htm language=enus -->
## TOPIC 00604: rfmxspecandotnet/html/eca95e7f-5e6e-e537-be11-2ca8a627779f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eca95e7f-5e6e-e537-be11-2ca8a627779f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eca95e7f-5e6e-e537-be11-2ca8a627779f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdMemoryPolynomialLagOrderType Enumeration

RFmxSpecAnMXDpdMemoryPolynomialLagOrderType Enumeration

RFmxSpecAnMXDpdModel

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdMemoryPolynomialLagOrderType
```

```text
Public Enumeration RFmxSpecAnMXDpdMemoryPolynomialLagOrderType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| AllOrders | 0 | The memory polynomial will compute all the terms for the given order. |
| OddOrdersOnly | 1 | The memory polynomial will compute the non-zero coefficients only for the odd terms. |
| EvenOrdersOnly | 2 | The memory polynomial will compute the non-zero coefficents only for the even terms. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ecd75c32-9233-47cf-3b56-ae4a435e3156.htm language=enus -->
## TOPIC 00605: rfmxspecandotnet/html/ecd75c32-9233-47cf-3b56-ae4a435e3156.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ecd75c32-9233-47cf-3b56-ae4a435e3156.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ecd75c32-9233-47cf-3b56-ae4a435e3156.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetUserMemoryPolynomialOrder Method

RFmxSpecAnMXDpdApplyDpdGetUserMemoryPolynomialOrder Method

Gets the order of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUserMemoryPolynomialOrder(
	string selectorString,
	out int value
)
```

```text
Public Function GetUserMemoryPolynomialOrder ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the order of the DPD polynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserMemoryPolynomialOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ee1a5cc0-0854-8965-45c2-e51eec59c21d.htm language=enus -->
## TOPIC 00606: rfmxspecandotnet/html/ee1a5cc0-0854-8965-45c2-e51eec59c21d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ee1a5cc0-0854-8965-45c2-e51eec59c21d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ee1a5cc0-0854-8965-45c2-e51eec59c21d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetExternalPreampFrequency Method

RFmxSpecAnMXNFConfigurationSetExternalPreampFrequency Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetExternalPreampFrequency(
	string selectorString,
	double[] value
)
```

```text
Public Function SetExternalPreampFrequency ( 
	selectorString As String,
	value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the array of frequencies corresponding to the value of the SetExternalPreampGain(String, Double) method.

###### Return Value

Int32

##### Remarks

NFExternalPreampFrequency

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ee7fe1b8-cb2f-5d68-f252-077f945b22d2.htm language=enus -->
## TOPIC 00607: rfmxspecandotnet/html/ee7fe1b8-cb2f-5d68-f252-077f945b22d2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ee7fe1b8-cb2f-5d68-f252-077f945b22d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ee7fe1b8-cb2f-5d68-f252-077f945b22d2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureOffsetAbsoluteLimit Method

RFmxSpecAnMXSemConfigurationConfigureOffsetAbsoluteLimit Method

Configures the absolute limit mode and specifies the absolute power limits corresponding to the beginning and end of the offset segment.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetAbsoluteLimit(
	string selectorString,
	RFmxSpecAnMXSemOffsetAbsoluteLimitMode absoluteLimitMode,
	double absoluteLimitStart,
	double absoluteLimitStop
)
```

```text
Public Function ConfigureOffsetAbsoluteLimit ( 
	selectorString As String,
	absoluteLimitMode As RFmxSpecAnMXSemOffsetAbsoluteLimitMode,
	absoluteLimitStart As Double,
	absoluteLimitStop As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **absoluteLimitMode RFmxSpecAnMXSemOffsetAbsoluteLimitMode**
  - Specifies whether the absolute limit mask is a flat line or a line with a slope.
- **absoluteLimitStart Double**
  - Specifies the absolute power limit, in dBm, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the absoluteLimitMode parameter to Couple.
- **absoluteLimitStop Double**
  - Specifies the absolute power limit, in dBm, corresponding to the end of the offset segment. This parameter is ignored when you set the absoluteLimitMode parameter to Couple.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetAbsoluteLimit() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ee8ddf8e-5a45-3ac6-1ec2-fd35af55d145.htm language=enus -->
## TOPIC 00608: rfmxspecandotnet/html/ee8ddf8e-5a45-3ac6-1ec2-fd35af55d145.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ee8ddf8e-5a45-3ac6-1ec2-fd35af55d145.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ee8ddf8e-5a45-3ac6-1ec2-fd35af55d145.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetCarrierFrequency Method

RFmxSpecAnMXChpConfigurationGetCarrierFrequency Method

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
  - Upon return, contains the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetCarrierFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ee92041c-7f76-bba6-e41b-b9142aa4b37e.htm language=enus -->
## TOPIC 00609: rfmxspecandotnet/html/ee92041c-7f76-bba6-e41b-b9142aa4b37e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ee92041c-7f76-bba6-e41b-b9142aa4b37e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ee92041c-7f76-bba6-e41b-b9142aa4b37e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.ValidateNoiseCalibrationData Method

RFmxSpecAnMXSpectrumConfigurationValidateNoiseCalibrationData Method

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
	out RFmxSpecAnMXSpectrumNoiseCalibrationDataValid noiseCalibrationDataValid
)
```

```text
Public Function ValidateNoiseCalibrationData ( 
	selectorString As String,
	<OutAttribute> ByRef noiseCalibrationDataValid As RFmxSpecAnMXSpectrumNoiseCalibrationDataValid
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **noiseCalibrationDataValid RFmxSpecAnMXSpectrumNoiseCalibrationDataValid**
  - Upon return, contains whether the calibration data is valid.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eeb5afee-9bfb-0679-17e9-ec5e6fb44811.htm language=enus -->
## TOPIC 00610: rfmxspecandotnet/html/eeb5afee-9bfb-0679-17e9-ec5e6fb44811.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eeb5afee-9bfb-0679-17e9-ec5e6fb44811.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eeb5afee-9bfb-0679-17e9-ec5e6fb44811.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetRbwFilterAutoBandwidth Method

RFmxSpecAnMXChpConfigurationGetRbwFilterAutoBandwidth Method

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
	out RFmxSpecAnMXChpRbwAutoBandwidth value
)
```

```text
Public Function GetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpRbwAutoBandwidth**
  - Upon return, contains a value that indicates whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetRBWFilterAutoBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eedbe316-08af-7e27-3227-797a6728a2b5.htm language=enus -->
## TOPIC 00611: rfmxspecandotnet/html/eedbe316-08af-7e27-3227-797a6728a2b5.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eedbe316-08af-7e27-3227-797a6728a2b5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eedbe316-08af-7e27-3227-797a6728a2b5.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.ConfigureRangeDefinition Method

RFmxSpecAnMXPhaseNoiseConfigurationConfigureRangeDefinition Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRangeDefinition(
	string selectorString,
	RFmxSpecAnMXPhaseNoiseRangeDefinition rangeDefinition
)
```

```text
Public Function ConfigureRangeDefinition ( 
	selectorString As String,
	rangeDefinition As RFmxSpecAnMXPhaseNoiseRangeDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rangeDefinition RFmxSpecAnMXPhaseNoiseRangeDefinition**
  - Specifies how the measurement computes offset subranges.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/eee3f86f-b3f3-75a8-e337-a8d191a9f5ce.htm language=enus -->
## TOPIC 00612: rfmxspecandotnet/html/eee3f86f-b3f3-75a8-e337-a8d191a9f5ce.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/eee3f86f-b3f3-75a8-e337-a8d191a9f5ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/eee3f86f-b3f3-75a8-e337-a8d191a9f5ce.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.FetchFrequencyResolution Method

RFmxSpecAnMXAcpResultsFetchFrequencyResolution Method

Fetches the frequency resolution, in hertz (Hz), of the spectrum acquired by the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFrequencyResolution(
	string selectorString,
	double timeout,
	out double frequencyResolution
)
```

```text
Public Function FetchFrequencyResolution ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef frequencyResolution As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **frequencyResolution Double**
  - Upon return, contains the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPFetchFrequencyResolution() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef080ce7-4c4f-b59c-b84f-4be28d555c4c.htm language=enus -->
## TOPIC 00613: rfmxspecandotnet/html/ef080ce7-4c4f-b59c-b84f-4be28d555c4c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef080ce7-4c4f-b59c-b84f-4be28d555c4c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef080ce7-4c4f-b59c-b84f-4be28d555c4c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpRrcFilterEnabled Enumeration

RFmxSpecAnMXChpRrcFilterEnabled Enumeration

**Note: This API is now obsolete.**

Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use RFmxSpecAnChpCarrierRrcFilterEnabled instead")]
public enum RFmxSpecAnMXChpRrcFilterEnabled
```

```text
<ObsoleteAttribute("Use RFmxSpecAnChpCarrierRrcFilterEnabled instead")>
Public Enumeration RFmxSpecAnMXChpRrcFilterEnabled
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef0e7ace-3d4f-f877-6bc1-b107d18f67d8.htm language=enus -->
## TOPIC 00614: rfmxspecandotnet/html/ef0e7ace-3d4f-f877-6bc1-b107d18f67d8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef0e7ace-3d4f-f877-6bc1-b107d18f67d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef0e7ace-3d4f-f877-6bc1-b107d18f67d8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNumberOfCarriers Method

RFmxSpecAnMXAcpConfigurationSetNumberOfCarriers Method

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

This method maps to the RFmxSpecAn_ACPSetNumberOfCarriers() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef179092-5325-d29b-d43b-e5a41b30d952.htm language=enus -->
## TOPIC 00615: rfmxspecandotnet/html/ef179092-5325-d29b-d43b-e5a41b30d952.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef179092-5325-d29b-d43b-e5a41b30d952.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef179092-5325-d29b-d43b-e5a41b30d952.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetMeasurementMethod Method

RFmxSpecAnMXNFConfigurationGetMeasurementMethod Method

Gets the measurement method used to perform the noise figure (NF) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementMethod(
	string selectorString,
	out RFmxSpecAnMXNFMeasurementMethod value
)
```

```text
Public Function GetMeasurementMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXNFMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFMeasurementMethod**
  - Upon return, contains the measurement method used to perform the noise figure (NF) measurement.

###### Return Value

Int32

##### Remarks

NFMeasurementMethod

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef1a0f19-2250-be33-3ada-d3f4d31f8767.htm language=enus -->
## TOPIC 00616: rfmxspecandotnet/html/ef1a0f19-2250-be33-3ada-d3f4d31f8767.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef1a0f19-2250-be33-3ada-d3f4d31f8767.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef1a0f19-2250-be33-3ada-d3f4d31f8767.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.GetThresholdLevel Method

RFmxSpecAnMXCcdfConfigurationGetThresholdLevel Method

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

This method maps to the RFmxSpecAn_CCDFGetThresholdLevel() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef1e5b01-2177-041c-bba8-64eaba399aa7.htm language=enus -->
## TOPIC 00617: rfmxspecandotnet/html/ef1e5b01-2177-041c-bba8-64eaba399aa7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef1e5b01-2177-041c-bba8-64eaba399aa7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef1e5b01-2177-041c-bba8-64eaba399aa7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXExtension Methods

RFmxSpecAnMXExtension Methods

The [RFmxSpecAnMXExtension](dba4770a-ce59-582b-ad66-5bb1eb908be4.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetSpecAnList | Creates a new SpecAn list if it doesn't exist; otherwise, it returns the existing SpecAn list. |
|  | GetSpecAnSignalConfiguration(RFmxInstrMX) | Creates a new default SpecAn signal configuration if it doesn't exist; otherwise, it returns the existing default SpecAn signal configuration. |
|  | GetSpecAnSignalConfiguration(RFmxInstrMX, String) | Creates a SpecAn signal configuration for specified signal name. Existing SpecAn signal configuration is returned if specified signal name exists. |
|  | SpecAnClearNoiseCalibrationDatabase | Clears the noise calibration database used for noise compensation. |

Top

##### See Also

###### Reference

RFmxSpecAnMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef3cb52c-1c82-b8fc-f9cd-ccd54c7f4319.htm language=enus -->
## TOPIC 00618: rfmxspecandotnet/html/ef3cb52c-1c82-b8fc-f9cd-ccd54c7f4319.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef3cb52c-1c82-b8fc-f9cd-ccd54c7f4319.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef3cb52c-1c82-b8fc-f9cd-ccd54c7f4319.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants.PxiTriggerLine7 Field

RFmxSpecAnMXConstantsPxiTriggerLine7 Field

The signal is exported to the PXI trigger line 7.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMXConstants Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ef504b99-fa1f-6148-9db7-eaede76f8b73.htm language=enus -->
## TOPIC 00619: rfmxspecandotnet/html/ef504b99-fa1f-6148-9db7-eaede76f8b73.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ef504b99-fa1f-6148-9db7-eaede76f8b73.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ef504b99-fa1f-6148-9db7-eaede76f8b73.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpCarrierRrcFilterEnabled Enumeration

RFmxSpecAnMXAcpCarrierRrcFilterEnabled Enumeration

Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpCarrierRrcFilterEnabled
```

```text
Public Enumeration RFmxSpecAnMXAcpCarrierRrcFilterEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The channel power of the acquired carrier channel is measured directly. |
| True | 1 | The measurement applies the RRC filter on the acquired carrier channel before measuring the carrier channel power. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/efac335d-7e15-c511-567b-665fdb88ed4c.htm language=enus -->
## TOPIC 00620: rfmxspecandotnet/html/efac335d-7e15-c511-567b-665fdb88ed4c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/efac335d-7e15-c511-567b-665fdb88ed4c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/efac335d-7e15-c511-567b-665fdb88ed4c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetNoiseCalibrationMode Method

RFmxSpecAnMXAcpConfigurationSetNoiseCalibrationMode Method

Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCalibrationMode(
	string selectorString,
	RFmxSpecAnMXAcpNoiseCalibrationMode value
)
```

```text
Public Function SetNoiseCalibrationMode ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpNoiseCalibrationMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpNoiseCalibrationMode**
  - Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

AcpNoiseCalibrationMode

Auto

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/efe14795-54af-c583-2365-d1a200372092.htm language=enus -->
## TOPIC 00621: rfmxspecandotnet/html/efe14795-54af-c583-2365-d1a200372092.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/efe14795-54af-c583-2365-d1a200372092.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/efe14795-54af-c583-2365-d1a200372092.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpThresholdEnabled Enumeration

RFmxSpecAnMXTxpThresholdEnabled Enumeration

Specifies whether to enable thresholding of the acquired samples to be used for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXTxpThresholdEnabled
```

```text
Public Enumeration RFmxSpecAnMXTxpThresholdEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that all samples are considered for the measurement. |
| True | 1 | Specifies that the samples above the threshold level specified in the SetThresholdLevel(String, Double) method are considered for the measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/effd77aa-853d-591f-1a8f-cd69d712673d.htm language=enus -->
## TOPIC 00622: rfmxspecandotnet/html/effd77aa-853d-591f-1a8f-cd69d712673d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/effd77aa-853d-591f-1a8f-cd69d712673d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/effd77aa-853d-591f-1a8f-cd69d712673d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetVbwFilterAutoBandwidth Method

RFmxSpecAnMXSpectrumConfigurationGetVbwFilterAutoBandwidth Method

Gets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetVbwFilterAutoBandwidth(
	string selectorString,
	out RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth value
)
```

```text
Public Function GetVbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth**
  - Upon return, contains whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

###### Return Value

Int32

##### Remarks

SpectrumVbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/effe13c0-d0c9-54eb-5fa8-db346e5da913.htm language=enus -->
## TOPIC 00623: rfmxspecandotnet/html/effe13c0-d0c9-54eb-5fa8-db346e5da913.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/effe13c0-d0c9-54eb-5fa8-db346e5da913.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/effe13c0-d0c9-54eb-5fa8-db346e5da913.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.ConfigureMeasurementInterval Method

RFmxSpecAnMXFcntConfigurationConfigureMeasurementInterval Method

Configures the acquisition time, in seconds, for the frequency count (Fcnt) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the acquisition time, in seconds, for the Fcnt measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntCfgMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f0155908-4153-509d-dc74-855b9412d1f9.htm language=enus -->
## TOPIC 00624: rfmxspecandotnet/html/f0155908-4153-509d-dc74-855b9412d1f9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f0155908-4153-509d-dc74-855b9412d1f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f0155908-4153-509d-dc74-855b9412d1f9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetCarrierRrcFilterAlpha Method

RFmxSpecAnMXChpConfigurationGetCarrierRrcFilterAlpha Method

Gets the roll-off factor for the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierRrcFilterAlpha(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierRrcFilterAlpha ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the roll-off factor for the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetCarrierRRCFilterAlpha() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f018d4d6-9e4a-390f-9e84-6aa991992a5e.htm language=enus -->
## TOPIC 00625: rfmxspecandotnet/html/f018d4d6-9e4a-390f-9e84-6aa991992a5e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f018d4d6-9e4a-390f-9e84-6aa991992a5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f018d4d6-9e4a-390f-9e84-6aa991992a5e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetCarrierMode Method

RFmxSpecAnMXAcpConfigurationSetCarrierMode Method

RFmxSpecAnMXAcpOffsetPowerReferenceCarrier

Composite

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCarrierMode(
	string selectorString,
	RFmxSpecAnMXAcpCarrierMode value
)
```

```text
Public Function SetCarrierMode ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpCarrierMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXAcpCarrierMode**
  - Specifies whether to consider the carrier power as part of total carrier power measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetCarrierMode() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f03a1511-ca0f-2bd0-3aab-150766095d7c.htm language=enus -->
## TOPIC 00626: rfmxspecandotnet/html/f03a1511-ca0f-2bd0-3aab-150766095d7c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f03a1511-ca0f-2bd0-3aab-150766095d7c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f03a1511-ca0f-2bd0-3aab-150766095d7c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeEnabled Method

RFmxSpecAnMXSpurConfigurationSetRangeEnabled Method

Sets whether to measure the spurious emissions (Spur) in the frequency range.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeEnabled(
	string selectorString,
	RFmxSpecAnMXSpurRangeEnabled value
)
```

```text
Public Function SetRangeEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurRangeEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurRangeEnabled**
  - Specifies whether to measure the Spurs in the frequency range.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f03af65a-1c73-177e-e458-48b3429b95c8.htm language=enus -->
## TOPIC 00627: rfmxspecandotnet/html/f03af65a-1c73-177e-e458-48b3429b95c8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f03af65a-1c73-177e-e458-48b3429b95c8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f03af65a-1c73-177e-e458-48b3429b95c8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetNumberOfCarriers Method

RFmxSpecAnMXChpConfigurationGetNumberOfCarriers Method

Gets the number of carriers.

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
  - Upon return, contains a value that indicates the the number of carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetNumberOfCarriers() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f05fd98a-ae29-2f76-e6d8-fea93ab36643.htm language=enus -->
## TOPIC 00628: rfmxspecandotnet/html/f05fd98a-ae29-2f76-e6d8-fea93ab36643.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f05fd98a-ae29-2f76-e6d8-fea93ab36643.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f05fd98a-ae29-2f76-e6d8-fea93ab36643.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.FetchCurveFitCoefficients Method

RFmxSpecAnMXAmpmResultsFetchCurveFitCoefficients Method

Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCurveFitCoefficients(
	string selectorString,
	double timeout,
	ref float[] amToAMCoefficients,
	ref float[] amToPMCoefficients
)
```

```text
Public Function FetchCurveFitCoefficients ( 
	selectorString As String,
	timeout As Double,
	ByRef amToAMCoefficients As Single(),
	ByRef amToPMCoefficients As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **amToAMCoefficients Single**
  - Upon return, contains the coefficients of the polynomial that approximates the AM-to-AM characteristic of the device under test.
- **amToPMCoefficients Single**
  - Upon return, contains the coefficients of the polynomial that approximates the AM-to-PM characteristic of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMFetchCurveFitCoefficients() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f0c7c78c-6520-101d-d35f-4123e02b236a.htm language=enus -->
## TOPIC 00629: rfmxspecandotnet/html/f0c7c78c-6520-101d-d35f-4123e02b236a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f0c7c78c-6520-101d-d35f-4123e02b236a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f0c7c78c-6520-101d-d35f-4123e02b236a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.GetMeasurementEnabled Method

RFmxSpecAnMXPavtConfigurationGetMeasurementEnabled Method

Gets whether to enable the Phase Amplitude Versus Time (PAVT) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Upon return, contains whether to enable the Phase Amplitude Versus Time (PAVT) measurement.

###### Return Value

Int32

##### Remarks

PavtMeasurementEnabled

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f17bf2be-9042-95db-0b8b-5ea51b95102f.htm language=enus -->
## TOPIC 00630: rfmxspecandotnet/html/f17bf2be-9042-95db-0b8b-5ea51b95102f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f17bf2be-9042-95db-0b8b-5ea51b95102f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f17bf2be-9042-95db-0b8b-5ea51b95102f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SelectMeasurements Method

RFmxSpecAnMXSelectMeasurements Method

Specifies the measurements that you want to enable.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SelectMeasurements(
	string selectorString,
	RFmxSpecAnMXMeasurementTypes measurement,
	bool enableAllTraces
)
```

```text
Public Function SelectMeasurements ( 
	selectorString As String,
	measurement As RFmxSpecAnMXMeasurementTypes,
	enableAllTraces As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurement RFmxSpecAnMXMeasurementTypes**
  - Specifies the measurement to perform.
- **enableAllTraces Boolean**
  - to enable all traces for the selected measurement; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SelectMeasurements() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f18e1d31-2b2d-cf46-311a-3d0ebea4fad4.htm language=enus -->
## TOPIC 00631: rfmxspecandotnet/html/f18e1d31-2b2d-cf46-311a-3d0ebea4fad4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f18e1d31-2b2d-cf46-311a-3d0ebea4fad4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f18e1d31-2b2d-cf46-311a-3d0ebea4fad4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetSignalType Method

RFmxSpecAnMXAmpmConfigurationGetSignalType Method

Gets whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSignalType(
	string selectorString,
	out RFmxSpecAnMXAmpmSignalType value
)
```

```text
Public Function GetSignalType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmSignalType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmSignalType**
  - Upon return, contains a value that indicates whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetSignalType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f1ae07c9-2b9e-e0c9-8c7e-122470fa79cd.htm language=enus -->
## TOPIC 00632: rfmxspecandotnet/html/f1ae07c9-2b9e-e0c9-8c7e-122470fa79cd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f1ae07c9-2b9e-e0c9-8c7e-122470fa79cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f1ae07c9-2b9e-e0c9-8c7e-122470fa79cd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled Enumeration

RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled Enumeration

Specifies whether to enable the IQ origin offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled
```

```text
Public Enumeration RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Enables the IQ origin offset correction for the measurement. |
| True | 1 | Disables the IQ origin offset correction for the measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f3ef50dd-6fe7-2f93-3bde-1c1a6a40fc38.htm language=enus -->
## TOPIC 00633: rfmxspecandotnet/html/f3ef50dd-6fe7-2f93-3bde-1c1a6a40fc38.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f3ef50dd-6fe7-2f93-3bde-1c1a6a40fc38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f3ef50dd-6fe7-2f93-3bde-1c1a6a40fc38.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumFftOverlapType Enumeration

RFmxSpecAnMXSpectrumFftOverlapType Enumeration

SpectrumMeasurementMethod

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumFftOverlapType
```

```text
Public Enumeration RFmxSpecAnMXSpectrumFftOverlapType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rms | 0 | Linear averaging of the FFTs taken over different chunks of data is performed. RMS averaging reduces signal fluctuations but not the noise floor. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one chunk FFT to the next. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f4270c57-4c58-dba2-0cf1-449e395eae01.htm language=enus -->
## TOPIC 00634: rfmxspecandotnet/html/f4270c57-4c58-dba2-0cf1-449e395eae01.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f4270c57-4c58-dba2-0cf1-449e395eae01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f4270c57-4c58-dba2-0cf1-449e395eae01.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.FetchPreCfrPapr Method

RFmxSpecAnMXDpdApplyDpdFetchPreCfrPapr Method

Fetches the PAPR of the pre-distorted waveform before CFR is applied to it.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPreCfrPapr(
	string selectorString,
	double timeout,
	out double preCfrPapr
)
```

```text
Public Function FetchPreCfrPapr ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef preCfrPapr As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement.
- **preCfrPapr Double**
  - Upon return, contains the PAPR of the pre-distorted waveform before CFR is applied when you set the DpdApplyDpdCfrEnabled attribute to True. This value is expressed in dB. When you set the DpdApplyDpdCfrEnabled attribute to False and the DpdModel attribute to LookupTable, the PAPR of the pre-distorted waveform is returned. When you set the DpdApplyDpdCfrEnabled attribute to False and the DpdModel attribute to MemoryPolynomial or GeneralizedMemoryPolynomial, the PAPR of the clipped pre-distorted waveform is returned. The pre-distorted waveform is clipped such that its peak amplitude does not exceed the peak of the input waveform, scaled to DUT average input power, by 6 dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f42d121f-d240-d3ab-abf3-f6d173469aba.htm language=enus -->
## TOPIC 00635: rfmxspecandotnet/html/f42d121f-d240-d3ab-abf3-f6d173469aba.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f42d121f-d240-d3ab-abf3-f6d173469aba.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f42d121f-d240-d3ab-abf3-f6d173469aba.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureCarrierRrcFilter Method

RFmxSpecAnMXSemConfigurationConfigureCarrierRrcFilter Method

Configures the root raised cosine (RRC) channel filter to apply on the acquired carrier channel before measuring the channel power. RRC alpha is the filter roll off.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierRrcFilter(
	string selectorString,
	RFmxSpecAnMXSemCarrierRrcFilterEnabled rrcFilterEnabled,
	double rrcAlpha
)
```

```text
Public Function ConfigureCarrierRrcFilter ( 
	selectorString As String,
	rrcFilterEnabled As RFmxSpecAnMXSemCarrierRrcFilterEnabled,
	rrcAlpha As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **rrcFilterEnabled RFmxSpecAnMXSemCarrierRrcFilterEnabled**
  - Specifies whether to apply the RRC filter on the acquired carrier channel before measuring the carrier channel power.
- **rrcAlpha Double**
  - Specifies the roll-off factor for the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierRRCFilter() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f43a5c5c-8607-23d8-56b3-0c40427fc76b.htm language=enus -->
## TOPIC 00636: rfmxspecandotnet/html/f43a5c5c-8607-23d8-56b3-0c40427fc76b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f43a5c5c-8607-23d8-56b3-0c40427fc76b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f43a5c5c-8607-23d8-56b3-0c40427fc76b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeRbwFilterBandwidthDefinition Method

RFmxSpecAnMXSpurConfigurationSetRangeRbwFilterBandwidthDefinition Method

SetRangeRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeRbwFilterBandwidthDefinition(
	string selectorString,
	RFmxSpecAnMXSpurRbwFilterBandwidthDefinition value
)
```

```text
Public Function SetRangeRbwFilterBandwidthDefinition ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurRbwFilterBandwidthDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurRbwFilterBandwidthDefinition**
  - Specifies the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeRBWFilterBandwidthDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f442fdde-c925-95f7-9b37-3c801c0eaee0.htm language=enus -->
## TOPIC 00637: rfmxspecandotnet/html/f442fdde-c925-95f7-9b37-3c801c0eaee0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f442fdde-c925-95f7-9b37-3c801c0eaee0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f442fdde-c925-95f7-9b37-3c801c0eaee0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetRangeSweepTimeAuto Method

RFmxSpecAnMXSpurConfigurationGetRangeSweepTimeAuto Method

Gets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeSweepTimeAuto(
	string selectorString,
	out RFmxSpecAnMXSpurSweepTimeAuto value
)
```

```text
Public Function GetRangeSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpurSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurSweepTimeAuto**
  - Upon return, indicates whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetRangeSweepTimeAuto() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f4cfc294-fabd-b3fd-7d9c-3e5336324618.htm language=enus -->
## TOPIC 00638: rfmxspecandotnet/html/f4cfc294-fabd-b3fd-7d9c-3e5336324618.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f4cfc294-fabd-b3fd-7d9c-3e5336324618.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f4cfc294-fabd-b3fd-7d9c-3e5336324618.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetIntermodOrder Method

RFmxSpecAnMXIMConfigurationGetIntermodOrder Method

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIntermodOrder(
	string selectorString,
	out int value
)
```

```text
Public Function GetIntermodOrder ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the order of the intermod. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMIntermodOrder

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f52f1e8b-3af6-a86c-a851-43c6c66a0028.htm language=enus -->
## TOPIC 00639: rfmxspecandotnet/html/f52f1e8b-3af6-a86c-a851-43c6c66a0028.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f52f1e8b-3af6-a86c-a851-43c6c66a0028.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f52f1e8b-3af6-a86c-a851-43c6c66a0028.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants.PxiStarLine Field

RFmxSpecAnMXConstantsPxiStarLine Field

The signal is exported to the PXI star trigger line.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMXConstants Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f53b592c-fcd1-7111-8878-66117df86174.htm language=enus -->
## TOPIC 00640: rfmxspecandotnet/html/f53b592c-fcd1-7111-8878-66117df86174.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f53b592c-fcd1-7111-8878-66117df86174.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f53b592c-fcd1-7111-8878-66117df86174.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarm Class

RFmxSpecAnMXHarm Class

Represents a Harmonics measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXHarm : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXHarm
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXHarm type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXHarmConfiguration instance that allows configuration of Harmonics measurement. |
|  | Results | Gets the RFmxSpecAnMXHarmResults instance that provides methods to retrieve Harmonics measurement results. |

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f5f24c74-f993-54f0-2fef-f2129ec70a67.htm language=enus -->
## TOPIC 00641: rfmxspecandotnet/html/f5f24c74-f993-54f0-2fef-f2129ec70a67.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f5f24c74-f993-54f0-2fef-f2129ec70a67.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f5f24c74-f993-54f0-2fef-f2129ec70a67.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpdCfrEnabled Enumeration

RFmxSpecAnMXDpdPreDpdCfrEnabled Enumeration

Specifies whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdPreDpdCfrEnabled
```

```text
Public Enumeration RFmxSpecAnMXDpdPreDpdCfrEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the CFR. The ApplyPreDpdSignalConditioning(String, ComplexWaveformComplexSingle, RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, ComplexWaveformComplexSingle, Double) function returns an error when the CFR is disabled. |
| True | 1 | Enables the CFR. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f5fe6fb7-30b0-f133-0789-b6b127fae298.htm language=enus -->
## TOPIC 00642: rfmxspecandotnet/html/f5fe6fb7-30b0-f133-0789-b6b127fae298.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f5fe6fb7-30b0-f133-0789-b6b127fae298.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f5fe6fb7-30b0-f133-0789-b6b127fae298.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetSignalType Method

RFmxSpecAnMXDpdConfigurationSetSignalType Method

Sets whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSignalType(
	string selectorString,
	RFmxSpecAnMXDpdSignalType value
)
```

```text
Public Function SetSignalType ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdSignalType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdSignalType**
  - Contains a value that indicates whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetSignalType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f621ee13-120d-764e-69e0-ac8f018656c4.htm language=enus -->
## TOPIC 00643: rfmxspecandotnet/html/f621ee13-120d-764e-69e0-ac8f018656c4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f621ee13-120d-764e-69e0-ac8f018656c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f621ee13-120d-764e-69e0-ac8f018656c4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.ConfigureYFactorNoiseSourceSettlingTime Method

RFmxSpecAnMXNFConfigurationConfigureYFactorNoiseSourceSettlingTime Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureYFactorNoiseSourceSettlingTime(
	string selectorString,
	double settlingTime
)
```

```text
Public Function ConfigureYFactorNoiseSourceSettlingTime ( 
	selectorString As String,
	settlingTime As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **settlingTime Double**
  - Specifies the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is enabled or disabled. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f635dd15-a90b-6327-3cab-cc05abfb9de8.htm language=enus -->
## TOPIC 00644: rfmxspecandotnet/html/f635dd15-a90b-6327-3cab-cc05abfb9de8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f635dd15-a90b-6327-3cab-cc05abfb9de8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f635dd15-a90b-6327-3cab-cc05abfb9de8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.ConfigureDigitalEdgeTrigger Method

RFmxSpecAnMXConfigureDigitalEdgeTrigger Method

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDigitalEdgeTrigger(
	string selectorString,
	string digitalEdgeTriggerSource,
	RFmxSpecAnMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge,
	double triggerDelay,
	bool enableTrigger
)
```

```text
Public Function ConfigureDigitalEdgeTrigger ( 
	selectorString As String,
	digitalEdgeTriggerSource As String,
	digitalEdgeTriggerEdge As RFmxSpecAnMXDigitalEdgeTriggerEdge,
	triggerDelay As Double,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **digitalEdgeTriggerSource String**
  - Specifies the source terminal for the RFmxSpecAnMXDigitalEdgeTriggerEdge.
- **digitalEdgeTriggerEdge RFmxSpecAnMXDigitalEdgeTriggerEdge**
  - Specifies the trigger edge to detect.
- **triggerDelay Double**
  - Specifies the trigger delay time, in seconds.
- **enableTrigger Boolean**
  - to enable the trigger; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CfgDigitalEdgeTrigger() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f63d4283-d726-e6e3-f9ed-b79ce274cfa8.htm language=enus -->
## TOPIC 00645: rfmxspecandotnet/html/f63d4283-d726-e6e3-f9ed-b79ce274cfa8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f63d4283-d726-e6e3-f9ed-b79ce274cfa8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f63d4283-d726-e6e3-f9ed-b79ce274cfa8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.ConfigureSegmentMeasurementIntervalArray Method

RFmxSpecAnMXPavtConfigurationConfigureSegmentMeasurementIntervalArray Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSegmentMeasurementIntervalArray(
	string selectorString,
	double[] segmentMeasurementOffset,
	double[] segmentMeasurementLength
)
```

```text
Public Function ConfigureSegmentMeasurementIntervalArray ( 
	selectorString As String,
	segmentMeasurementOffset As Double(),
	segmentMeasurementLength As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **segmentMeasurementOffset Double**
  - Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid only when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.
- **segmentMeasurementLength Double**
  - Specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f64427ae-237d-92f6-52c0-6145e6ed7ee0.htm language=enus -->
## TOPIC 00646: rfmxspecandotnet/html/f64427ae-237d-92f6-52c0-6145e6ed7ee0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f64427ae-237d-92f6-52c0-6145e6ed7ee0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f64427ae-237d-92f6-52c0-6145e6ed7ee0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTriggerMinimumQuietTimeMode Enumeration

RFmxSpecAnMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXTriggerMinimumQuietTimeMode
```

```text
Public Enumeration RFmxSpecAnMXTriggerMinimumQuietTimeMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(String, Double) method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f645951b-975e-2519-2319-89b2cd798e16.htm language=enus -->
## TOPIC 00647: rfmxspecandotnet/html/f645951b-975e-2519-2319-89b2cd798e16.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f645951b-975e-2519-2319-89b2cd798e16.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f645951b-975e-2519-2319-89b2cd798e16.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.ConfigureRangePeakCriteriaArray Method

RFmxSpecAnMXSpurConfigurationConfigureRangePeakCriteriaArray Method

Configures arrays of peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRangePeakCriteriaArray(
	string selectorString,
	double[] threshold,
	double[] excursion
)
```

```text
Public Function ConfigureRangePeakCriteriaArray ( 
	selectorString As String,
	threshold As Double(),
	excursion As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **threshold Double**
  - Specifies the array of threshold levels, in dBm, above which the measurement detects spurs in the specified range.
- **excursion Double**
  - Specifies the array of peak excursion values, in dB, used to find spurs in the spectrum. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered as spur.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurCfgRangePeakCriteriaArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f6679f53-da62-18e0-9694-a56e2d719ccc.htm language=enus -->
## TOPIC 00648: rfmxspecandotnet/html/f6679f53-da62-18e0-9694-a56e2d719ccc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f6679f53-da62-18e0-9694-a56e2d719ccc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f6679f53-da62-18e0-9694-a56e2d719ccc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpOffsetEnabled Enumeration

RFmxSpecAnMXAcpOffsetEnabled Enumeration

Specifies whether to enable the offset channel for adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpOffsetEnabled
```

```text
Public Enumeration RFmxSpecAnMXAcpOffsetEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the offset channel for ACP measurement. |
| True | 1 | Enables the offset channel for ACP measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f6699aae-6892-733c-0e51-9ea38d9471f8.htm language=enus -->
## TOPIC 00649: rfmxspecandotnet/html/f6699aae-6892-733c-0e51-9ea38d9471f8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f6699aae-6892-733c-0e51-9ea38d9471f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f6699aae-6892-733c-0e51-9ea38d9471f8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.SetSampleRate Method

RFmxSpecAnMXIQConfigurationSetSampleRate Method

Sets the acquisition sample rate, in samples per second (S/s).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSampleRate(
	string selectorString,
	double value
)
```

```text
Public Function SetSampleRate ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the acquisition sample rate, in S/s.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQSetSampleRate() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f66e8225-4638-ece7-36aa-c91e0631ca97.htm language=enus -->
## TOPIC 00650: rfmxspecandotnet/html/f66e8225-4638-ece7-36aa-c91e0631ca97.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f66e8225-4638-ece7-36aa-c91e0631ca97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f66e8225-4638-ece7-36aa-c91e0631ca97.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurAveragingEnabled Enumeration

RFmxSpecAnMXSpurAveragingEnabled Enumeration

Specifies whether to enable averaging for the spurious emission (Spur) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpurAveragingEnabled
```

```text
Public Enumeration RFmxSpecAnMXSpurAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The Spur measurement uses the SetAveragingCount(String, Int32) method as the number of acquisitions over which the Spur measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f66f87f4-0a0c-19e8-7be0-f2809e34c72c.htm language=enus -->
## TOPIC 00651: rfmxspecandotnet/html/f66f87f4-0a0c-19e8-7be0-f2809e34c72c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f66f87f4-0a0c-19e8-7be0-f2809e34c72c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f66f87f4-0a0c-19e8-7be0-f2809e34c72c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerResults.FetchXY Method

RFmxSpecAnMXMarkerResultsFetchXY Method

Fetches the X and Y locations of the marker.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchXY(
	string selectorString,
	out double markerXLocation,
	out double markerYLocation
)
```

```text
Public Function FetchXY ( 
	selectorString As String,
	<OutAttribute> ByRef markerXLocation As Double,
	<OutAttribute> ByRef markerYLocation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and marker number. Example: "marker0", "result::r1/marker0". You can use the BuildMarkerString2(String, Int32) method to build the selector string.
- **markerXLocation Double**
  - Upon return, contains the marker X location.
- **markerYLocation Double**
  - Upon return, contains the marker Y location.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_MarkerFetchXY() function in C.

##### See Also

###### Reference

RFmxSpecAnMXMarkerResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f6adb2de-af25-f804-07c1-05ba757d8070.htm language=enus -->
## TOPIC 00652: rfmxspecandotnet/html/f6adb2de-af25-f804-07c1-05ba757d8070.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f6adb2de-af25-f804-07c1-05ba757d8070.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f6adb2de-af25-f804-07c1-05ba757d8070.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetEnabled Method

RFmxSpecAnMXSemConfigurationSetOffsetEnabled Method

Sets whether to enable the offset segment for the spectral emission mask (SEM) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetEnabled(
	string selectorString,
	RFmxSpecAnMXSemOffsetEnabled value
)
```

```text
Public Function SetOffsetEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXSemOffsetEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetEnabled**
  - Specifies whether to enable the offset segment for the SEM measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f6ee90e4-1df9-d21b-319e-3836446b8c2a.htm language=enus -->
## TOPIC 00653: rfmxspecandotnet/html/f6ee90e4-1df9-d21b-319e-3836446b8c2a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f6ee90e4-1df9-d21b-319e-3836446b8c2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f6ee90e4-1df9-d21b-319e-3836446b8c2a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.SetPretriggerTime Method

RFmxSpecAnMXIQConfigurationSetPretriggerTime Method

Sets the pretrigger time, in seconds, for the I/Q measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPretriggerTime(
	string selectorString,
	double value
)
```

```text
Public Function SetPretriggerTime ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the pretrigger time, in seconds, for the I/Q measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQSetPretriggerTime() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f7030fac-7e69-c087-f604-38a7b2adbd9c.htm language=enus -->
## TOPIC 00654: rfmxspecandotnet/html/f7030fac-7e69-c087-f604-38a7b2adbd9c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f7030fac-7e69-c087-f604-38a7b2adbd9c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f7030fac-7e69-c087-f604-38a7b2adbd9c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.ConfigureSegmentMeasurementInterval Method

RFmxSpecAnMXPavtConfigurationConfigureSegmentMeasurementInterval Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSegmentMeasurementInterval(
	string selectorString,
	double segmentMeasurementOffset,
	double segmentMeasurementLength
)
```

```text
Public Function ConfigureSegmentMeasurementInterval ( 
	selectorString As String,
	segmentMeasurementOffset As Double,
	segmentMeasurementLength As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of segment number. Example:"segment0" You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **segmentMeasurementOffset Double**
  - Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid only when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.
- **segmentMeasurementLength Double**
  - Specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f7310ec0-c2ea-9db2-0528-6a56ad05b96c.htm language=enus -->
## TOPIC 00655: rfmxspecandotnet/html/f7310ec0-c2ea-9db2-0528-6a56ad05b96c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f7310ec0-c2ea-9db2-0528-6a56ad05b96c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f7310ec0-c2ea-9db2-0528-6a56ad05b96c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetAveragingType Method

RFmxSpecAnMXAcpConfigurationSetAveragingType Method

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxSpecAnMXAcpAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpAveragingType**
  - Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetAveragingType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f753e3cf-75ae-3e2f-4a62-1b4cda4d300b.htm language=enus -->
## TOPIC 00656: rfmxspecandotnet/html/f753e3cf-75ae-3e2f-4a62-1b4cda4d300b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f753e3cf-75ae-3e2f-4a62-1b4cda4d300b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f753e3cf-75ae-3e2f-4a62-1b4cda4d300b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetRbwFilterAutoBandwidth Method

RFmxSpecAnMXSpectrumConfigurationGetRbwFilterAutoBandwidth Method

Gets whether the resolution bandwidth (RBW) is computed by the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterAutoBandwidth(
	string selectorString,
	out RFmxSpecAnMXSpectrumRbwAutoBandwidth value
)
```

```text
Public Function GetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumRbwAutoBandwidth**
  - Upon return, indicates whether the RBW is computed by the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumGetRBWFilterAutoBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f75bad52-0400-b8ab-3a8b-943a642f618f.htm language=enus -->
## TOPIC 00657: rfmxspecandotnet/html/f75bad52-0400-b8ab-3a8b-943a642f618f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f75bad52-0400-b8ab-3a8b-943a642f618f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f75bad52-0400-b8ab-3a8b-943a642f618f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Spur Property

RFmxSpecAnMXSpur Property

Gets the RFmxSpecAnMXSpur instance that represents the Spur measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXSpur Spur { get; }
```

```text
Public ReadOnly Property Spur As RFmxSpecAnMXSpur
	Get
```

###### Property Value

RFmxSpecAnMXSpur

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f7a028a2-4658-1eb5-55ca-b3575570f18e.htm language=enus -->
## TOPIC 00658: rfmxspecandotnet/html/f7a028a2-4658-1eb5-55ca-b3575570f18e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f7a028a2-4658-1eb5-55ca-b3575570f18e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f7a028a2-4658-1eb5-55ca-b3575570f18e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemCarrierRbwFilterType Enumeration

RFmxSpecAnMXSemCarrierRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemCarrierRbwFilterType
```

```text
Public Enumeration RFmxSpecAnMXSemCarrierRbwFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | The RBW filter has a Gaussian response. |
| Flat | 2 | The RBW filter has a flat response. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f7a6f1ea-f7d7-3fcf-f386-6e6c2b54f21a.htm language=enus -->
## TOPIC 00659: rfmxspecandotnet/html/f7a6f1ea-f7d7-3fcf-f386-6e6c2b54f21a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f7a6f1ea-f7d7-3fcf-f386-6e6c2b54f21a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f7a6f1ea-f7d7-3fcf-f386-6e6c2b54f21a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntResults.GetMeanPhase Method

RFmxSpecAnMXFcntResultsGetMeanPhase Method

Gets the I/Q samples averaged over all acquisitions. The phase of the sum of these I/Q samples is returned. Only samples above the threshold are used.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanPhase(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanPhase ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the I/Q samples averaged over all acquisitions. The phase of the sum of these I/Q samples is returned. Only samples above the threshold are used.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetResultsMeanPhase() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f7c37270-8b19-249d-2fe3-5d27c2ba6e86.htm language=enus -->
## TOPIC 00660: rfmxspecandotnet/html/f7c37270-8b19-249d-2fe3-5d27c2ba6e86.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f7c37270-8b19-249d-2fe3-5d27c2ba6e86.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f7c37270-8b19-249d-2fe3-5d27c2ba6e86.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.GetThresholdType Method

RFmxSpecAnMXCcdfConfigurationGetThresholdType Method

Gets the reference for the power level used for thresholding.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetThresholdType(
	string selectorString,
	out RFmxSpecAnMXCcdfThresholdType value
)
```

```text
Public Function GetThresholdType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXCcdfThresholdType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXCcdfThresholdType**
  - Upon return, contains the reference for the power level used for thresholding.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFGetThresholdType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f7d4ebde-1c4f-a4c9-b56a-05d6aea8b821.htm language=enus -->
## TOPIC 00661: rfmxspecandotnet/html/f7d4ebde-1c4f-a4c9-b56a-05d6aea8b821.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f7d4ebde-1c4f-a4c9-b56a-05d6aea8b821.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f7d4ebde-1c4f-a4c9-b56a-05d6aea8b821.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants.PxieDStarBLine Field

RFmxSpecAnMXConstantsPxieDStarBLine Field

The signal is exported to the PXIe DStar B trigger line.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMXConstants Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f817fe02-557e-3eee-e6dd-b99e793ddbcd.htm language=enus -->
## TOPIC 00662: rfmxspecandotnet/html/f817fe02-557e-3eee-e6dd-b99e793ddbcd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f817fe02-557e-3eee-e6dd-b99e793ddbcd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f817fe02-557e-3eee-e6dd-b99e793ddbcd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.WaitForMeasurementComplete Method

RFmxSpecAnMXListWaitForMeasurementComplete Method

Waits for the specified number for seconds for all the measurements to complete.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f825fe30-53b2-b10e-4710-3e2a3b4a7327.htm language=enus -->
## TOPIC 00663: rfmxspecandotnet/html/f825fe30-53b2-b10e-4710-3e2a3b4a7327.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f825fe30-53b2-b10e-4710-3e2a3b4a7327.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f825fe30-53b2-b10e-4710-3e2a3b4a7327.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.ClearAllNamedResults Method

RFmxSpecAnMXClearAllNamedResults Method

Clears all results for the current signal instance.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

##### Remarks

This method maps to the RFmxSpecAn_ClearAllNamedResults() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f8465a0b-8a11-b354-dfe9-2a05db6f6f37.htm language=enus -->
## TOPIC 00664: rfmxspecandotnet/html/f8465a0b-8a11-b354-dfe9-2a05db6f6f37.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f8465a0b-8a11-b354-dfe9-2a05db6f6f37.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f8465a0b-8a11-b354-dfe9-2a05db6f6f37.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQDeleteRecordOnFetch Enumeration

RFmxSpecAnMXIQDeleteRecordOnFetch Enumeration

Specifies whether the measurement deletes the fetched record.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIQDeleteRecordOnFetch
```

```text
Public Enumeration RFmxSpecAnMXIQDeleteRecordOnFetch
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement does not delete the fetched record. |
| True | 1 | The measurement deletes the fetched record. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f86e658b-ac74-b9ba-9ddd-8222b3c08dde.htm language=enus -->
## TOPIC 00665: rfmxspecandotnet/html/f86e658b-ac74-b9ba-9ddd-8222b3c08dde.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f86e658b-ac74-b9ba-9ddd-8222b3c08dde.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f86e658b-ac74-b9ba-9ddd-8222b3c08dde.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.GetAveragingEnabled Method

RFmxSpecAnMXIdpdConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the IDPD measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxSpecAnMXIdpdAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIdpdAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIdpdAveragingEnabled**
  - Upon return, contains whether to enable averaging for the IDPD measurement.

###### Return Value

Int32

##### Remarks

IdpdAveragingEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f87243f6-d562-1f4d-0781-a7ce387e7906.htm language=enus -->
## TOPIC 00666: rfmxspecandotnet/html/f87243f6-d562-1f4d-0781-a7ce387e7906.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f87243f6-d562-1f4d-0781-a7ce387e7906.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f87243f6-d562-1f4d-0781-a7ce387e7906.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.GetDeleteRecordOnFetch Method

RFmxSpecAnMXIQConfigurationGetDeleteRecordOnFetch Method

Gets whether the measurement deletes the fetched record.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDeleteRecordOnFetch(
	string selectorString,
	out RFmxSpecAnMXIQDeleteRecordOnFetch value
)
```

```text
Public Function GetDeleteRecordOnFetch ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIQDeleteRecordOnFetch
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIQDeleteRecordOnFetch**
  - Upon return, contains whether the measurement deletes the fetched record.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQGetDeleteRecordOnFetch() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f875560d-7aa6-b547-4e18-def4c900bdfa.htm language=enus -->
## TOPIC 00667: rfmxspecandotnet/html/f875560d-7aa6-b547-4e18-def4c900bdfa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f875560d-7aa6-b547-4e18-def4c900bdfa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f875560d-7aa6-b547-4e18-def4c900bdfa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.SetHarmonicMeasurementInterval Method

RFmxSpecAnMXHarmConfigurationSetHarmonicMeasurementInterval Method

Sets the acquisition time, in seconds, for the harmonic.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetHarmonicMeasurementInterval(
	string selectorString,
	double value
)
```

```text
Public Function SetHarmonicMeasurementInterval ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the harmonic number. Example: "harmonic0". You can use the BuildHarmonicString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the acquisition time, in seconds, for the harmonic.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmSetHarmonicMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f88bfed1-41de-7d5c-5d41-1ff98ae5e52b.htm language=enus -->
## TOPIC 00668: rfmxspecandotnet/html/f88bfed1-41de-7d5c-5d41-1ff98ae5e52b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f88bfed1-41de-7d5c-5d41-1ff98ae5e52b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f88bfed1-41de-7d5c-5d41-1ff98ae5e52b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.ConfigureFft Method

RFmxSpecAnMXAcpConfigurationConfigureFft Method

Configures window and FFT to obtain a spectrum for the adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFft(
	string selectorString,
	RFmxSpecAnMXAcpFftWindow fftWindow,
	double fftPadding
)
```

```text
Public Function ConfigureFft ( 
	selectorString As String,
	fftWindow As RFmxSpecAnMXAcpFftWindow,
	fftPadding As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **fftWindow RFmxSpecAnMXAcpFftWindow**
  - Specifies the FFT window type to use to reduce spectral leakage.
- **fftPadding Double**
  - Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth of the device.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPCfgFFT() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f8950be2-460f-c4c6-55d6-1848388586f7.htm language=enus -->
## TOPIC 00669: rfmxspecandotnet/html/f8950be2-460f-c4c6-55d6-1848388586f7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f8950be2-460f-c4c6-55d6-1848388586f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f8950be2-460f-c4c6-55d6-1848388586f7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.ConfigureOffsetIntegrationBandwidth Method

RFmxSpecAnMXAcpConfigurationConfigureOffsetIntegrationBandwidth Method

Configures the frequency range, in hertz (Hz), over which the adjacent channel power (ACP) measurement integrates the offset channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetIntegrationBandwidth(
	string selectorString,
	double integrationBandwidth
)
```

```text
Public Function ConfigureOffsetIntegrationBandwidth ( 
	selectorString As String,
	integrationBandwidth As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **integrationBandwidth Double**
  - Specifies the frequency range, in Hz, over which the measurement integrates the offset channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPCfgOffsetIntegrationBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f8c79920-539d-8925-721d-41ae1d14688a.htm language=enus -->
## TOPIC 00670: rfmxspecandotnet/html/f8c79920-539d-8925-721d-41ae1d14688a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f8c79920-539d-8925-721d-41ae1d14688a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f8c79920-539d-8925-721d-41ae1d14688a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetCfrEnabled Method

RFmxSpecAnMXDpdApplyDpdSetCfrEnabled Method

Sets whether to enable the crest factor reduction (CFR) on the pre-distorted waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCfrEnabled(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdCfrEnabled value
)
```

```text
Public Function SetCfrEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdApplyDpdCfrEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdCfrEnabled**
  - Specifies whether to enable the crest factor reduction (CFR) on the pre-distorted waveform.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/f9f5381e-520a-4b29-2f65-5e1778c9749a.htm language=enus -->
## TOPIC 00671: rfmxspecandotnet/html/f9f5381e-520a-4b29-2f65-5e1778c9749a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/f9f5381e-520a-4b29-2f65-5e1778c9749a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/f9f5381e-520a-4b29-2f65-5e1778c9749a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetSpurRemovalPeakExcursion Method

RFmxSpecAnMXPhaseNoiseConfigurationGetSpurRemovalPeakExcursion Method

Gets the peak excursion to be used when spur detection is performed. Refer to the Marker topic for more information on peak excursion.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpurRemovalPeakExcursion(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpurRemovalPeakExcursion ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, the peak excursion to be used when spur detection is performed. Refer to the Phase Noise topic for more information on spur removal.

###### Return Value

Int32

##### Remarks

PhaseNoiseSpurRemovalPeakExcursion

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fa1c6324-6354-e805-7832-018a5f9338ca.htm language=enus -->
## TOPIC 00672: rfmxspecandotnet/html/fa1c6324-6354-e805-7832-018a5f9338ca.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fa1c6324-6354-e805-7832-018a5f9338ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fa1c6324-6354-e805-7832-018a5f9338ca.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetDetectorType Method

RFmxSpecAnMXChpConfigurationGetDetectorType Method

Gets the type of detector to be used.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectorType(
	string selectorString,
	out RFmxSpecAnMXChpDetectorType value
)
```

```text
Public Function GetDetectorType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpDetectorType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpDetectorType**
  - Upon return, contains the type of detector to be used.

###### Return Value

Int32

##### Remarks

ChpDetectorType

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fc1383d1-ae54-f4ee-654b-b03f350e9903.htm language=enus -->
## TOPIC 00673: rfmxspecandotnet/html/fc1383d1-ae54-f4ee-654b-b03f350e9903.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fc1383d1-ae54-f4ee-654b-b03f350e9903.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fc1383d1-ae54-f4ee-654b-b03f350e9903.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetWarning Method

RFmxSpecAnMXGetWarning Method

Retrieves and then clears the warning information for the session.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

This method maps to the RFmxSpecAn_GetError() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fc336e1f-c164-a1f3-eb95-6a849cc5648b.htm language=enus -->
## TOPIC 00674: rfmxspecandotnet/html/fc336e1f-c164-a1f3-eb95-6a849cc5648b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fc336e1f-c164-a1f3-eb95-6a849cc5648b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fc336e1f-c164-a1f3-eb95-6a849cc5648b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetDetectorType Method

RFmxSpecAnMXSpectrumConfigurationSetDetectorType Method

Sets the type of detector to be used.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDetectorType(
	string selectorString,
	RFmxSpecAnMXSpectrumDetectorType value
)
```

```text
Public Function SetDetectorType ( 
	selectorString As String,
	value As RFmxSpecAnMXSpectrumDetectorType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumDetectorType**
  - Specifies the type of detector to be used.

###### Return Value

Int32

##### Remarks

SpectrumDetectorType

None

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fc8ca51a-dabc-2f68-e1b1-46fddd07d707.htm language=enus -->
## TOPIC 00675: rfmxspecandotnet/html/fc8ca51a-dabc-2f68-e1b1-46fddd07d707.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fc8ca51a-dabc-2f68-e1b1-46fddd07d707.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fc8ca51a-dabc-2f68-e1b1-46fddd07d707.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.ConfigureAveraging Method

RFmxSpecAnMXHarmConfigurationConfigureAveraging Method

Configures averaging for the Harmonics measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxSpecAnMXHarmAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxSpecAnMXHarmAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxSpecAnMXHarmAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxSpecAnMXHarmAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxSpecAnMXHarmAveragingEnabled**
  - Specifies whether to enable averaging for the measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXHarmAveragingEnabled) method to True.
- **averagingType RFmxSpecAnMXHarmAveragingType**
  - Specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmCfgAveraging() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fcfc0885-4b2f-d0db-778b-9deab47a2900.htm language=enus -->
## TOPIC 00676: rfmxspecandotnet/html/fcfc0885-4b2f-d0db-778b-9deab47a2900.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fcfc0885-4b2f-d0db-778b-9deab47a2900.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fcfc0885-4b2f-d0db-778b-9deab47a2900.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFColdSourceMode Enumeration

RFmxSpecAnMXNFColdSourceMode Enumeration

Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFColdSourceMode
```

```text
Public Enumeration RFmxSpecAnMXNFColdSourceMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Measure | 0 | The noise figure (NF) measurement computes the noise characteristics of the DUT and compensates for the noise figure of the analyzer. |
| Calibrate | 1 | The NF measurement computes the noise characteristics of the analyzer. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fe2bd13f-8941-e2bd-7310-45a6162f782f.htm language=enus -->
## TOPIC 00677: rfmxspecandotnet/html/fe2bd13f-8941-e2bd-7310-45a6162f782f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fe2bd13f-8941-e2bd-7310-45a6162f782f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fe2bd13f-8941-e2bd-7310-45a6162f782f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetSweepTimeAuto Method

RFmxSpecAnMXChpConfigurationGetSweepTimeAuto Method

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
	out RFmxSpecAnMXChpSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpSweepTimeAuto**
  - Upon return, indicates whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetSweepTimeAuto() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fe35466b-a91d-f532-06e3-6314ee882390.htm language=enus -->
## TOPIC 00678: rfmxspecandotnet/html/fe35466b-a91d-f532-06e3-6314ee882390.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fe35466b-a91d-f532-06e3-6314ee882390.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fe35466b-a91d-f532-06e3-6314ee882390.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetEqualizerMode Method

RFmxSpecAnMXAmpmConfigurationSetEqualizerMode Method

Sets whether the measurement equalizes the channel.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEqualizerMode(
	string selectorString,
	RFmxSpecAnMXAmpmEqualizerMode value
)
```

```text
Public Function SetEqualizerMode ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmEqualizerMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmEqualizerMode**
  - Specifies whether the measurement equalizes the channel.

###### Return Value

Int32

##### Remarks

AmpmEqualizerMode

Off

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fe99e3c6-dac1-8410-8370-e5964ff7e64d.htm language=enus -->
## TOPIC 00679: rfmxspecandotnet/html/fe99e3c6-dac1-8410-8370-e5964ff7e64d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fe99e3c6-dac1-8410-8370-e5964ff7e64d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fe99e3c6-dac1-8410-8370-e5964ff7e64d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SetAttributeDoubleArray Method

RFmxSpecAnMXSetAttributeDoubleArray Method

Set the value of a double array attribute.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeDoubleArray(
	string selectorString,
	int attributeIdentifier,
	double[] value
)
```

```text
Public Function SetAttributeDoubleArray ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Double**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SetAttributeF64Array() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/ffc63056-2d56-af4e-c3d1-74583d8102f9.htm language=enus -->
## TOPIC 00680: rfmxspecandotnet/html/ffc63056-2d56-af4e-c3d1-74583d8102f9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/ffc63056-2d56-af4e-c3d1-74583d8102f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/ffc63056-2d56-af4e-c3d1-74583d8102f9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseResults.GetCarrierPower Method

RFmxSpecAnMXPhaseNoiseResultsGetCarrierPower Method

Gets the measured carrier power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the measured carrier power.

###### Return Value

Int32

##### Remarks

PhaseNoiseResultsCarrierPower

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/fff3f3b6-933a-4c0b-59e6-890ff19e40bf.htm language=enus -->
## TOPIC 00681: rfmxspecandotnet/html/fff3f3b6-933a-4c0b-59e6-890ff19e40bf.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/fff3f3b6-933a-4c0b-59e6-890ff19e40bf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/fff3f3b6-933a-4c0b-59e6-890ff19e40bf.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.GetOutputCompressionPoint Method

RFmxSpecAnMXAmpmResultsGetOutputCompressionPoint Method

AmpmCompressionPointGainReference

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOutputCompressionPoint(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetOutputCompressionPoint ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the value of theoretical output power at which device gain drops by the compression level, specified through RFmxSpecAnMXAmpmConfiguration.GetCompressionPointLevel Method , from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. this value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
