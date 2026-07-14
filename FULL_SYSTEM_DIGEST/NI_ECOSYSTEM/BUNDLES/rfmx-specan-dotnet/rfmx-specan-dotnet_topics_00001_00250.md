# NI DOCUMENT BUNDLE: rfmx-specan-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-dotnet start=1 end=250 -->
<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/030fd0a2-f55c-866c-20f2-1043c36de98f.htm language=enus -->
## TOPIC 00001: rfmxspecandotnet/html/030fd0a2-f55c-866c-20f2-1043c36de98f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/030fd0a2-f55c-866c-20f2-1043c36de98f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/030fd0a2-f55c-866c-20f2-1043c36de98f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.GetPeakReferencePowerGain Method

RFmxSpecAnMXAmpmResultsGetPeakReferencePowerGain Method

Gets the gain at the peak reference power. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakReferencePowerGain(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakReferencePowerGain ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Uopn return, contains the gain at the peak reference power. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0328cbc3-2c58-f433-e41f-7b6a2c6a7fa2.htm language=enus -->
## TOPIC 00002: rfmxspecandotnet/html/0328cbc3-2c58-f433-e41f-7b6a2c6a7fa2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0328cbc3-2c58-f433-e41f-7b6a2c6a7fa2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0328cbc3-2c58-f433-e41f-7b6a2c6a7fa2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQ Methods

RFmxSpecAnMXIQ Methods

The [RFmxSpecAnMXIQ](8ad7bff6-039c-caf6-b373-70e4d731dc74.htm) type exposes the following members.

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

RFmxSpecAnMXIQ Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/03e00558-9b63-97f8-d779-0a1f2c53074c.htm language=enus -->
## TOPIC 00003: rfmxspecandotnet/html/03e00558-9b63-97f8-d779-0a1f2c53074c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/03e00558-9b63-97f8-d779-0a1f2c53074c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/03e00558-9b63-97f8-d779-0a1f2c53074c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.ConfigureCompressionPoints Method

RFmxSpecAnMXAmpmConfigurationConfigureCompressionPoints Method

Configures the computation of compression points corresponding to the compression levels specified by RFmxSpecAnMXAmpmCompressionPointEnabled method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCompressionPoints(
	string selectorString,
	RFmxSpecAnMXAmpmCompressionPointEnabled compressionPointEnabled,
	double[] compressionLevel
)
```

```text
Public Function ConfigureCompressionPoints ( 
	selectorString As String,
	compressionPointEnabled As RFmxSpecAnMXAmpmCompressionPointEnabled,
	compressionLevel As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **compressionPointEnabled RFmxSpecAnMXAmpmCompressionPointEnabled**
  - Specifies the computation of compression points corresponding to the compression levels specified by RFmxSpecAnMXAmpmCompressionPointEnabled method.
- **compressionLevel Double**
  - Specifies the compression levels for which compression points are computed when RFmxSpecAnMXAmpmCompressionPointEnabled method is set to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/03e08b60-3ff9-851e-dca7-df4b7d5dfee3.htm language=enus -->
## TOPIC 00004: rfmxspecandotnet/html/03e08b60-3ff9-851e-dca7-df4b7d5dfee3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/03e08b60-3ff9-851e-dca7-df4b7d5dfee3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/03e08b60-3ff9-851e-dca7-df4b7d5dfee3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetCalibrationSetupId Method

RFmxSpecAnMXNFConfigurationSetCalibrationSetupId Method

Sets a unique string identifier with the hardware setup used to perform calibration for the NF measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCalibrationSetupId(
	string selectorString,
	string value
)
```

```text
Public Function SetCalibrationSetupId ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Associates a unique string identifier with the hardware setup used to perform calibration for the NF measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0483ea2f-28dc-c452-ef2d-6b7b0d8db06f.htm language=enus -->
## TOPIC 00005: rfmxspecandotnet/html/0483ea2f-28dc-c452-ef2d-6b7b0d8db06f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0483ea2f-28dc-c452-ef2d-6b7b0d8db06f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0483ea2f-28dc-c452-ef2d-6b7b0d8db06f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetMeasurementEnabled Method

RFmxSpecAnMXPhaseNoiseConfigurationSetMeasurementEnabled Method

Sets whether to enable the phase noise measurement.

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
  - Specifies whether to enable the phase noise measurement.

###### Return Value

Int32

##### Remarks

PhaseNoiseMeasurementEnabled

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/04e21332-4147-683b-634e-fb0c51b0a8cd.htm language=enus -->
## TOPIC 00006: rfmxspecandotnet/html/04e21332-4147-683b-634e-fb0c51b0a8cd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/04e21332-4147-683b-634e-fb0c51b0a8cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/04e21332-4147-683b-634e-fb0c51b0a8cd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFResults Methods

RFmxSpecAnMXNFResults Methods

The [RFmxSpecAnMXNFResults](064e8cc4-193b-f4e3-89aa-b55cef1fa95b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchAnalyzerNoiseFigure | Fetches the noise figure of the analyzer. |
|  | FetchColdSourcePower | Fetches the power measured by the analyzer when the cold source based noise figure (NF) measurement is performed. |
|  | FetchDutNoiseFigureAndGain | Fetches the DUT noise figure, noise temperature and gain results. |
|  | FetchYFactorPowers | Fetches the hot and cold powers measured when the Y-Factor based noise figure (NF) measurement is performed. |
|  | FetchYFactors | Returns the measurement Y-factor and calibration Y-factor values. |
|  | GetAnalyzerNoiseFigure | Gets an array of the noise figures of the analyzer measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. |
|  | GetCalibrationYFactor | Gets an array of the calibration Y-Factors measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
|  | GetColdSourcePower | Gets the power measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to Cold-source. |
|  | GetDutGain | Gets an array of the available gains of the DUT measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. |
|  | GetDutNoiseFigure | Gets an array of the noise figures of the DUT measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. |
|  | GetDutNoiseTemperature | Gets an array of the equivalent thermal noise temperatures of the DUT measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in kelvin. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementYFactor | Gets an array of the measurement Y-Factors measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetYFactorColdPower | Gets the array of powers measured at the frequencies specified by the SetFrequencyList(String, Double) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
|  | GetYFactorHotPower | Gets the array of powers measured at the frequencies specified by the SetFrequencyList(String, Double) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXNFResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0576c8b2-ea41-3ec4-b02b-8443aee82c9e.htm language=enus -->
## TOPIC 00007: rfmxspecandotnet/html/0576c8b2-ea41-3ec4-b02b-8443aee82c9e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0576c8b2-ea41-3ec4-b02b-8443aee82c9e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0576c8b2-ea41-3ec4-b02b-8443aee82c9e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetNoiseCalibrationAveragingCount Method

RFmxSpecAnMXChpConfigurationGetNoiseCalibrationAveragingCount Method

SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)

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
  - Upon return, contains the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False.

###### Return Value

Int32

##### Remarks

ChpNoiseCalibrationAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/05ba7d1a-e7a8-e773-519f-4a4727fa3a8f.htm language=enus -->
## TOPIC 00008: rfmxspecandotnet/html/05ba7d1a-e7a8-e773-519f-4a4727fa3a8f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/05ba7d1a-e7a8-e773-519f-4a4727fa3a8f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/05ba7d1a-e7a8-e773-519f-4a4727fa3a8f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarm Properties

RFmxSpecAnMXHarm Properties

The [RFmxSpecAnMXHarm](f53b592c-fcd1-7111-8878-66117df86174.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXHarmConfiguration instance that allows configuration of Harmonics measurement. |
|  | Results | Gets the RFmxSpecAnMXHarmResults instance that provides methods to retrieve Harmonics measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXHarm Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/05cea48e-82b3-b51b-3c29-324ed4c2e8b7.htm language=enus -->
## TOPIC 00009: rfmxspecandotnet/html/05cea48e-82b3-b51b-3c29-324ed4c2e8b7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/05cea48e-82b3-b51b-3c29-324ed4c2e8b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/05cea48e-82b3-b51b-3c29-324ed4c2e8b7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetDetectorPoints Method

RFmxSpecAnMXChpConfigurationGetDetectorPoints Method

Gets the number of trace points after the detector is applied.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectorPoints(
	string selectorString,
	out int value
)
```

```text
Public Function GetDetectorPoints ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of trace points after the detector is applied.

###### Return Value

Int32

##### Remarks

ChpDetectorPoints

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/06349d45-fc3d-48dc-1f2d-c35324361c73.htm language=enus -->
## TOPIC 00010: rfmxspecandotnet/html/06349d45-fc3d-48dc-1f2d-c35324361c73.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/06349d45-fc3d-48dc-1f2d-c35324361c73.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/06349d45-fc3d-48dc-1f2d-c35324361c73.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Dispose Method

RFmxSpecAnMXDispose Method

Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. This method does not do anything if it is called by using list step instance.

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

You can call this method safely more than once, even if the signal is already deleted.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0751aa0b-4dd7-6680-c79d-70870ddb0df8.htm language=enus -->
## TOPIC 00011: rfmxspecandotnet/html/0751aa0b-4dd7-6680-c79d-70870ddb0df8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0751aa0b-4dd7-6680-c79d-70870ddb0df8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0751aa0b-4dd7-6680-c79d-70870ddb0df8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetSpurRemovalEnabled Method

RFmxSpecAnMXPhaseNoiseConfigurationGetSpurRemovalEnabled Method

Gets whether to remove spurs from the log plot trace.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpurRemovalEnabled(
	string selectorString,
	out RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled value
)
```

```text
Public Function GetSpurRemovalEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled**
  - Upon return, contains whether to remove spurs from the log plot trace.

###### Return Value

Int32

##### Remarks

PhaseNoiseSpurRemovalEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/076bb520-ebb7-e34f-37b6-69831c1928af.htm language=enus -->
## TOPIC 00012: rfmxspecandotnet/html/076bb520-ebb7-e34f-37b6-69831c1928af.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/076bb520-ebb7-e34f-37b6-69831c1928af.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/076bb520-ebb7-e34f-37b6-69831c1928af.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMRbwFilterType Enumeration

RFmxSpecAnMXIMRbwFilterType Enumeration

Specifies the response of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIMRbwFilterType
```

```text
Public Enumeration RFmxSpecAnMXIMRbwFilterType
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/07a0996c-cf9a-10a7-509a-d34351feff7e.htm language=enus -->
## TOPIC 00013: rfmxspecandotnet/html/07a0996c-cf9a-10a7-509a-d34351feff7e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/07a0996c-cf9a-10a7-509a-d34351feff7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/07a0996c-cf9a-10a7-509a-d34351feff7e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntResults.FetchAllanDeviation Method

RFmxSpecAnMXFcntResultsFetchAllanDeviation Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAllanDeviation(
	string selectorString,
	double timeout,
	out double allanDeviation
)
```

```text
Public Function FetchAllanDeviation ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef allanDeviation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **allanDeviation Double**
  - Upon return, contains the two-sample deviation of the measured frequency.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXFcntResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/07a5a750-0bbf-02ed-28ed-95ea85c836c3.htm language=enus -->
## TOPIC 00014: rfmxspecandotnet/html/07a5a750-0bbf-02ed-28ed-95ea85c836c3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/07a5a750-0bbf-02ed-28ed-95ea85c836c3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/07a5a750-0bbf-02ed-28ed-95ea85c836c3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMResults.GetLowerOutputInterceptPower Method

RFmxSpecAnMXIMResultsGetLowerOutputInterceptPower Method

Gets the lower output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOutputInterceptPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOutputInterceptPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and ImIntermod number. Example: "ImIntermod0", "result::r1/ImIntermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the lower output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result.

###### Return Value

Int32

##### Remarks

IMResultsLowerOutputInterceptPower

##### See Also

###### Reference

RFmxSpecAnMXIMResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/083c3184-db93-10f3-bf92-c8eaed6de2b9.htm language=enus -->
## TOPIC 00015: rfmxspecandotnet/html/083c3184-db93-10f3-bf92-c8eaed6de2b9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/083c3184-db93-10f3-bf92-c8eaed6de2b9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/083c3184-db93-10f3-bf92-c8eaed6de2b9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.ClearNamedResult Method

RFmxSpecAnMXListClearNamedResult Method

selectorString

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0846b677-3159-6210-10cb-d9a785cf6245.htm language=enus -->
## TOPIC 00016: rfmxspecandotnet/html/0846b677-3159-6210-10cb-d9a785cf6245.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0846b677-3159-6210-10cb-d9a785cf6245.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0846b677-3159-6210-10cb-d9a785cf6245.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetCfrTargetPapr Method

RFmxSpecAnMXDpdApplyDpdGetCfrTargetPapr Method

DpdApplyDpdCfrEnabled

True

DpdApplyDpdCfrTargetPaprType

Custom

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrTargetPapr(
	string selectorString,
	out double value
)
```

```text
Public Function GetCfrTargetPapr ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the target PAPR when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrTargetPaprType method to Custom. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrTargetPapr

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/088989c8-769c-58af-940e-563e0caafa59.htm language=enus -->
## TOPIC 00017: rfmxspecandotnet/html/088989c8-769c-58af-940e-563e0caafa59.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/088989c8-769c-58af-940e-563e0caafa59.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/088989c8-769c-58af-940e-563e0caafa59.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.ConfigureFft Method

RFmxSpecAnMXObwConfigurationConfigureFft Method

Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFft(
	string selectorString,
	RFmxSpecAnMXObwFftWindow fftWindow,
	double fftPadding
)
```

```text
Public Function ConfigureFft ( 
	selectorString As String,
	fftWindow As RFmxSpecAnMXObwFftWindow,
	fftPadding As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **fftWindow RFmxSpecAnMXObwFftWindow**
  - Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types.
- **fftPadding Double**
  - Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWCfgFFT() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/096f66be-7df4-fa15-b039-93ad2c31022f.htm language=enus -->
## TOPIC 00018: rfmxspecandotnet/html/096f66be-7df4-fa15-b039-93ad2c31022f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/096f66be-7df4-fa15-b039-93ad2c31022f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/096f66be-7df4-fa15-b039-93ad2c31022f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.GetLowerOffsetFrequency Method

RFmxSpecAnMXAcpResultsGetLowerOffsetFrequency Method

Gets the center frequency of the lower offset channel relative to the center frequency of the closest carrier. The offset frequency has a negative value.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the center frequency of the lower offset channel relative to the center frequency of the closest carrier. The offset frequency has a negative value.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsLowerOffsetFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/098ed2b4-3c38-4cdb-42ba-a95a0501b493.htm language=enus -->
## TOPIC 00019: rfmxspecandotnet/html/098ed2b4-3c38-4cdb-42ba-a95a0501b493.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/098ed2b4-3c38-4cdb-42ba-a95a0501b493.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/098ed2b4-3c38-4cdb-42ba-a95a0501b493.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetPowerUnits Method

RFmxSpecAnMXObwConfigurationSetPowerUnits Method

Sets the units for the absolute power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPowerUnits(
	string selectorString,
	RFmxSpecAnMXObwPowerUnits value
)
```

```text
Public Function SetPowerUnits ( 
	selectorString As String,
	value As RFmxSpecAnMXObwPowerUnits
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwPowerUnits**
  - Specifies the units for the absolute power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetPowerUnits() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0995eda4-92e2-185e-7d0d-c2183a4bbf80.htm language=enus -->
## TOPIC 00020: rfmxspecandotnet/html/0995eda4-92e2-185e-7d0d-c2183a4bbf80.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0995eda4-92e2-185e-7d0d-c2183a4bbf80.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0995eda4-92e2-185e-7d0d-c2183a4bbf80.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumAnalysisInput Enumeration

RFmxSpecAnMXSpectrumAnalysisInput Enumeration

Specifies whether to analyze just the real I or Q component of the acquired IQ data, or analyze the complex IQ data.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumAnalysisInput
```

```text
Public Enumeration RFmxSpecAnMXSpectrumAnalysisInput
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| IQ | 0 | Measurement analyzes the acquired I+jQ data, resulting generally in a spectrum that is not symmetric around 0 Hz. Spectrum trace result contains both positive and negative frequencies. Since the RMS power of the complex envelope is 3.01 dB higher than that of its equivalent real RF signal, the spectrum trace result of the acquired I+jQ data is scaled by -3.01 dB. |
| IOnly | 1 | Measurement ignores the Q data from the acquired I+jQ data and analyzes I+j0, resulting in a spectrum that is symmetric around 0 Hz. Spectrum trace result contains positive frequencies only. Spectrum of I+j0 data is scaled by +3.01 dB to account for the power of the negative frequencies that are not returned in the spectrum trace. |
| QOnly | 2 | Measurement ignores the I data from the acquired I+jQ data and analyzes Q+j0, resulting in a spectrum that is symmetric around 0 Hz. Spectrum trace result contains positive frequencies only. Spectrum of Q+j0 data is scaled by +3.01 dB to account for the power of the negative frequencies that are not returned in the spectrum trace. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/09ec5f38-5529-59ca-9030-974d5c11bf66.htm language=enus -->
## TOPIC 00021: rfmxspecandotnet/html/09ec5f38-5529-59ca-9030-974d5c11bf66.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/09ec5f38-5529-59ca-9030-974d5c11bf66.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/09ec5f38-5529-59ca-9030-974d5c11bf66.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.ConfigureEqualizerCoefficients Method

RFmxSpecAnMXIdpdConfigurationConfigureEqualizerCoefficients Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureEqualizerCoefficients(
	string selectorString,
	double x0,
	double dx,
	ComplexSingle[] equalizerCoefficients
)
```

```text
Public Function ConfigureEqualizerCoefficients ( 
	selectorString As String,
	x0 As Double,
	dx As Double,
	equalizerCoefficients As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **x0 Double**
  - Always pass 0 to this parameter. Any other values are ignored.
- **dx Double**
  - Specifies the spacing between the coefficients.
- **equalizerCoefficients ComplexSingle**
  - Specifies the equalizer coefficients.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0ba60346-81d3-5e4d-e427-5672e4a4f9c0.htm language=enus -->
## TOPIC 00022: rfmxspecandotnet/html/0ba60346-81d3-5e4d-e427-5672e4a4f9c0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0ba60346-81d3-5e4d-e427-5672e4a4f9c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0ba60346-81d3-5e4d-e427-5672e4a4f9c0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.DeleteSignalConfiguration Method

RFmxSpecAnMXDeleteSignalConfiguration Method

Deletes the current instance of a signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

##### Remarks

This method maps to the RFmxSpecAn_DeleteSignalConfiguration() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0bfffa05-d038-117f-429d-d05f92a6eb67.htm language=enus -->
## TOPIC 00023: rfmxspecandotnet/html/0bfffa05-d038-117f-429d-d05f92a6eb67.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0bfffa05-d038-117f-429d-d05f92a6eb67.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0bfffa05-d038-117f-429d-d05f92a6eb67.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSem Class

RFmxSpecAnMXSem Class

Represents a spectral emission mask (SEM) measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXSem : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXSem
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXSem type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXSemConfiguration instance that allows configuration of spectral emission mask (SEM) measurement. |
|  | Results | Gets the RFmxSpecAnMXSemResults instance that provides methods to retrieve spectral emission mask (SEM) measurement results. |

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0c00f947-4497-bf68-d7ec-6c94f79f1f9b.htm language=enus -->
## TOPIC 00024: rfmxspecandotnet/html/0c00f947-4497-bf68-d7ec-6c94f79f1f9b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0c00f947-4497-bf68-d7ec-6c94f79f1f9b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0c00f947-4497-bf68-d7ec-6c94f79f1f9b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarm.Configuration Property

RFmxSpecAnMXHarmConfiguration Property

RFmxSpecAnMXHarmConfiguration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXHarmConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxSpecAnMXHarmConfiguration
	Get
```

###### Property Value

RFmxSpecAnMXHarmConfiguration

##### See Also

###### Reference

RFmxSpecAnMXHarm Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0d718b88-5c2b-cf7b-17fa-16ac5327be8e.htm language=enus -->
## TOPIC 00025: rfmxspecandotnet/html/0d718b88-5c2b-cf7b-17fa-16ac5327be8e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0d718b88-5c2b-cf7b-17fa-16ac5327be8e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0d718b88-5c2b-cf7b-17fa-16ac5327be8e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerFunctionType Enumeration

RFmxSpecAnMXMarkerFunctionType Enumeration

specifies the function type for the selected marker. The default value is Off.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXMarkerFunctionType
```

```text
Public Enumeration RFmxSpecAnMXMarkerFunctionType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Off | 0 | The marker function is disabled. |
| BandPower | 1 | Band Power is computed within the specified span. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0dd21e31-c00b-7c3d-c7a8-e60564e259e4.htm language=enus -->
## TOPIC 00026: rfmxspecandotnet/html/0dd21e31-c00b-7c3d-c7a8-e60564e259e4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0dd21e31-c00b-7c3d-c7a8-e60564e259e4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0dd21e31-c00b-7c3d-c7a8-e60564e259e4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.ConfigureNumberOfHarmonics Method

RFmxSpecAnMXHarmConfigurationConfigureNumberOfHarmonics Method

Configures the number of harmonics, including fundamental, to measure.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfHarmonics(
	string selectorString,
	int numberOfHarmonics
)
```

```text
Public Function ConfigureNumberOfHarmonics ( 
	selectorString As String,
	numberOfHarmonics As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **numberOfHarmonics Int32**
  - Specifies the number of harmonics, including fundamental, to measure.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmCfgNumberOfHarmonics() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0debc277-d35c-37d9-9b9c-38d662d1b533.htm language=enus -->
## TOPIC 00027: rfmxspecandotnet/html/0debc277-d35c-37d9-9b9c-38d662d1b533.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0debc277-d35c-37d9-9b9c-38d662d1b533.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0debc277-d35c-37d9-9b9c-38d662d1b533.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmConfiguration.SetNumberOfAnalysisThreads Method

RFmxSpecAnMXHarmConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for Harmonics measurement.

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
  - Specifies the maximum number of threads used for parallelism for Harmonics measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmSetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0e6240ab-e0d7-0ae0-ebab-d1e20a1af225.htm language=enus -->
## TOPIC 00028: rfmxspecandotnet/html/0e6240ab-e0d7-0ae0-ebab-d1e20a1af225.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0e6240ab-e0d7-0ae0-ebab-d1e20a1af225.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0e6240ab-e0d7-0ae0-ebab-d1e20a1af225.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMResults.GetUpperOutputInterceptPower Method

RFmxSpecAnMXIMResultsGetUpperOutputInterceptPower Method

Gets the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOutputInterceptPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOutputInterceptPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and ImIntermod number. Example: "ImIntermod0", "result::r1/ImIntermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result.

###### Return Value

Int32

##### Remarks

IMResultsUpperOutputInterceptPower

##### See Also

###### Reference

RFmxSpecAnMXIMResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0f2df3b9-94ce-81a4-2f1f-6ad89fe32b93.htm language=enus -->
## TOPIC 00029: rfmxspecandotnet/html/0f2df3b9-94ce-81a4-2f1f-6ad89fe32b93.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0f2df3b9-94ce-81a4-2f1f-6ad89fe32b93.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0f2df3b9-94ce-81a4-2f1f-6ad89fe32b93.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetCancellationFrequency Method

RFmxSpecAnMXPhaseNoiseConfigurationSetCancellationFrequency Method

Sets an array of frequency offsets where the reference phase noise has been measured.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCancellationFrequency(
	string selectorString,
	float[] value
)
```

```text
Public Function SetCancellationFrequency ( 
	selectorString As String,
	value As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Single**
  - Specifies an array of frequencies where the reference phase noise has been measured.

###### Return Value

Int32

##### Remarks

PhaseNoiseCancellationFrequency

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0f9071a2-8504-7963-a8f3-502a77630163.htm language=enus -->
## TOPIC 00030: rfmxspecandotnet/html/0f9071a2-8504-7963-a8f3-502a77630163.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0f9071a2-8504-7963-a8f3-502a77630163.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0f9071a2-8504-7963-a8f3-502a77630163.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.GetThresholdLevel Method

RFmxSpecAnMXFcntConfigurationGetThresholdLevel Method

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
  - Upon return, indicates either the relative or absolute threshold power level.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetThresholdLevel() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0fb931b7-7473-0fd9-a4f5-cf7222ac8d9a.htm language=enus -->
## TOPIC 00031: rfmxspecandotnet/html/0fb931b7-7473-0fd9-a4f5-cf7222ac8d9a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0fb931b7-7473-0fd9-a4f5-cf7222ac8d9a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0fb931b7-7473-0fd9-a4f5-cf7222ac8d9a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMeasurementSampleRate Method

RFmxSpecAnMXDpdConfigurationGetMeasurementSampleRate Method

Gets the acquisition sample rate, in samples per second (S/s).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementSampleRate(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeasurementSampleRate ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the acquisition sample rate, in S/s.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetMeasurementSampleRate() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0fce6446-24eb-fc57-e90d-c14cab90a094.htm language=enus -->
## TOPIC 00032: rfmxspecandotnet/html/0fce6446-24eb-fc57-e90d-c14cab90a094.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0fce6446-24eb-fc57-e90d-c14cab90a094.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0fce6446-24eb-fc57-e90d-c14cab90a094.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetRbwFilterBandwidthDefinition Method

RFmxSpecAnMXSemConfigurationGetOffsetRbwFilterBandwidthDefinition Method

SetOffsetRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRbwFilterBandwidthDefinition(
	string selectorString,
	out RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition value
)
```

```text
Public Function GetOffsetRbwFilterBandwidthDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition**
  - Upon return, contains the bandwidth definition which you use to specify the value of the SetOffsetRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetRBWFilterBandwidthDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/0fcf7b3e-8ab3-b60a-866b-bf86f9c628fc.htm language=enus -->
## TOPIC 00033: rfmxspecandotnet/html/0fcf7b3e-8ab3-b60a-866b-bf86f9c628fc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/0fcf7b3e-8ab3-b60a-866b-bf86f9c628fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/0fcf7b3e-8ab3-b60a-866b-bf86f9c628fc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetMeasurementEnabled Method

RFmxSpecAnMXNFConfigurationGetMeasurementEnabled Method

Enables the noise figure (NF) measurement.

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
  - Enables the noise figure (NF) measurement.

###### Return Value

Int32

##### Remarks

NFMeasurementEnabled

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/112a6c5f-fa90-50dd-f1c1-ef4a864f557c.htm language=enus -->
## TOPIC 00034: rfmxspecandotnet/html/112a6c5f-fa90-50dd-f1c1-ef4a864f557c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/112a6c5f-fa90-50dd-f1c1-ef4a864f557c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/112a6c5f-fa90-50dd-f1c1-ef4a864f557c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFResults.FetchYFactorPowers Method

RFmxSpecAnMXNFResultsFetchYFactorPowers Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchYFactorPowers(
	string selectorString,
	double timeout,
	ref double[] hotPower,
	ref double[] coldPower
)
```

```text
Public Function FetchYFactorPowers ( 
	selectorString As String,
	timeout As Double,
	ByRef hotPower As Double(),
	ByRef coldPower As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **hotPower Double**
  - Upon return, contains an array of powers measured at the frequencies specified by the SetFrequencyList(String, Double) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor.
- **coldPower Double**
  - Upon return, contains an array of powers measured at the frequencies specified by the SetFrequencyList(String, Double) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/127606a7-26ce-efcf-e7e0-24ef737d3816.htm language=enus -->
## TOPIC 00035: rfmxspecandotnet/html/127606a7-26ce-efcf-e7e0-24ef737d3816.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/127606a7-26ce-efcf-e7e0-24ef737d3816.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/127606a7-26ce-efcf-e7e0-24ef737d3816.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Chp Property

RFmxSpecAnMXChp Property

Gets the RFmxSpecAnMXChp instance that represents the CHP measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXChp Chp { get; }
```

```text
Public ReadOnly Property Chp As RFmxSpecAnMXChp
	Get
```

###### Property Value

RFmxSpecAnMXChp

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1287ff4f-7692-e60b-6fb1-7b831b10d9bb.htm language=enus -->
## TOPIC 00036: rfmxspecandotnet/html/1287ff4f-7692-e60b-6fb1-7b831b10d9bb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1287ff4f-7692-e60b-6fb1-7b831b10d9bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1287ff4f-7692-e60b-6fb1-7b831b10d9bb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPropertyId Enumeration

RFmxSpecAnMXPropertyId Enumeration

Specifies all the attribute identifiers.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXPropertyId
```

```text
Public Enumeration RFmxSpecAnMXPropertyId
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| CenterFrequency | 1,048,577 | Specifies the expected carrier frequency, in hertz (Hz), of the RF signal that needs to be acquires. The signal analyzer tunes to this frequency. |
| ReferenceLevel | 1,048,578 | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ExternalAttenuation | 1,048,579 | Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the RF signal analyzer. |
| TriggerType | 1,048,580 | Specifies the type of reference trigger to use for signal acquisition. |
| DigitalEdgeTriggerSource | 1,048,581 | Returns the source terminal for the digital-edge trigger. |
| DigitalEdgeTriggerEdge | 1,048,582 | Specifies whether the RF vector signal analyzer detects a or on the signal. |
| IQPowerEdgeTriggerSource | 1,048,583 | Specifies the channel from which the device monitors the trigger. |
| IQPowerEdgeTriggerLevel | 1,048,584 | Specifies the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxSpecAnMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxSpecAnMXIQPowerEdgeTriggerLevelType) method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. |
| IQPowerEdgeTriggerSlope | 1,048,585 | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
| TriggerDelay | 1,048,586 | Specifies the trigger delay time, in seconds. |
| TriggerMinimumQuietTimeMode | 1,048,587 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 1,048,588 | Specifies a time duration, in seconds, for which the signal must be quiet before the RF signal analyzer arms the I/Q Power Edge trigger. |
| AutoLevelInitialReferenceLevel | 1,048,589 | Specifies the initial reference level, in dBm, which the auto level function uses to estimate the peak power of the input signal. |
| LimitedConfigurationChange | 1,048,590 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| ListStepTimerOffset | 1,052,663 | Specifies the time offset from the start of the step for which the measurements are computed. This value is expressed in seconds. This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent. |
| NumberOfSteps | 1,052,664 | Specifies the number of active steps in a list. |
| ListStepTimerDuration | 1,052,665 | Specifies the duration of a given list step. This value is expressed in seconds. |
| ReferenceLevelHeadroom | 1,052,668 | Specifies the margin RFmx adds to the Reference Level method. |
| SelectedPorts | 1,052,669 | Specifies the instrument port to be configured to acquire a signal. |
| IQPowerEdgeTriggerLevelType | 1,052,671 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. |
| AcpMeasurementEnabled | 1,052,672 | Specifies whether to enable the adjacent channel power (ACP) measurement. |
| AcpNumberOfCarriers | 1,052,674 | Specifies the number of carriers. |
| AcpCarrierMode | 1,052,675 | Specifies whether to consider the carrier power as part of total carrier power measurement. |
| AcpCarrierFrequency | 1,052,676 | Specifies the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| AcpCarrierIntegrationBandwidth | 1,052,677 | Specifies the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| AcpCarrierRrcFilterEnabled | 1,052,678 | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power. |
| AcpCarrierRrcFilterAlpha | 1,052,679 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter on the carrier channel before measuring the carrier channel power. |
| AcpNumberOfOffsets | 1,052,680 | Specifies the number of offset channels. |
| AcpOffsetEnabled | 1,052,681 | Specifies whether to enable the offset channel for adjacent channel power (ACP) measurement. |
| AcpOffsetFrequency | 1,052,682 | Specifies the center frequency, in hertz (Hz), of the offset channel, relative to the center frequency of the closest carrier. The absolute value of the offset frequency, along with the sideband information, is considered to configure an offset channel. |
| AcpOffsetSideband | 1,052,683 | Specifies whether the offset segment is present on one side, or on both sides of the carriers. |
| AcpOffsetPowerReferenceCarrier | 1,052,684 | Specifies the carrier, for which the measured power is the power reference to measure offset channel relative power. |
| AcpOffsetPowerReferenceSpecific | 1,052,685 | Specifies the carrier index, for which the measured power is the power reference for the offset channel relative power. |
| AcpOffsetIntegrationBandwidth | 1,052,686 | Specifies the frequency range, in hertz (Hz), over which the measurement integrates the offset channel power. |
| AcpOffsetRelativeAttenuation | 1,052,687 | Specifies the attenuation, in dB, relative to the method. |
| AcpOffsetRrcFilterEnabled | 1,052,688 | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. |
| AcpOffsetRrcFilterAlpha | 1,052,689 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. |
| AcpMeasurementMethod | 1,052,690 | Specifies the method for performing the adjacent channel power (ACP) measurement. |
| AcpPowerUnits | 1,052,691 | Specifies the adjacent channel power (ACP) power units. |
| AcpNumberOfAnalysisThreads | 1,052,692 | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
| AcpAveragingCount | 1,052,693 | Specifies the number of acquisitions used for averaging. |
| AcpAveragingEnabled | 1,052,694 | Specifies whether averaging is enabled for the adjacent channel power (ACP) measurement. |
| AcpAveragingType | 1,052,696 | Specifies the averaging type for averaging multiple spectrum acquisitions. |
| AcpFftWindow | 1,052,697 | Specifies the FFT window type to use to reduce spectral leakage. |
| AcpFftPadding | 1,052,698 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. |
| AcpRbwFilterAutoBandwidth | 1,052,699 | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| AcpRbwFilterBandwidth | 1,052,700 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| AcpRbwFilterType | 1,052,701 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| AcpSweepTimeAuto | 1,052,702 | Specifies whether the measurement computes the sweep time. |
| AcpSweepTimeInterval | 1,052,703 | Specifies the sweep time, in seconds, when you set the SetSweepTimeAuto(String, RFmxSpecAnMXAcpSweepTimeAuto) method to False. |
| AcpNoiseCompensationEnabled | 1,052,704 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the RF signal analyzer. |
| AcpAllTracesEnabled | 1,052,705 | Specifies whether to enable the traces to be stored and retrieved after performing the adjacent channel power (ACP) measurement. |
| AcpResultsTotalCarrierPower | 1,052,706 | Returns the total integrated power of all the active carriers measured. |
| AcpResultsFrequencyResolution | 1,052,707 | Returns the frequency resolution, in hertz (Hz), of the spectrum acquired by the measurement. |
| AcpResultsCarrierFrequency | 1,052,708 | Returns the center frequency, in hertz (Hz). |
| AcpResultsCarrierIntegrationBandwidth | 1,052,709 | Returns the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| AcpResultsCarrierAbsolutePower | 1,052,710 | Returns the measured carrier power. |
| AcpResultsCarrierTotalRelativePower | 1,052,711 | Returns the carrier power, in dB, measured relative to the total carrier power. |
| AcpResultsLowerOffsetFrequencyReferenceCarrier | 1,052,712 | Returns the carrier index of the center frequency that was used as a reference to define the center frequency of the lower (negative) offset channel. Lower offset channels are channels that are to the left of the reference carrier when the offset frequency specified is a positive value. The reference carrier is the carrier that has an offset frequency closest to the lower offset channel. |
| AcpResultsLowerOffsetFrequency | 1,052,713 | Returns the center frequency of the lower offset channel relative to the center frequency of the closest carrier. The sign of offset frequency is negative. |
| AcpResultsLowerOffsetIntegrationBandwidth | 1,052,714 | Returns the integration bandwidth used to measure the power in the lower offset channel. |
| AcpResultsLowerOffsetPowerReferenceCarrier | 1,052,715 | Returns the carrier index of the measured power that was used as a reference to define the lower (negative) offset channel relative power. |
| AcpResultsLowerOffsetAbsolutePower | 1,052,716 | Returns the lower offset channel power. |
| AcpResultsLowerOffsetRelativePower | 1,052,717 | Returns the lower offset channel power, in dB, measured relative to the integrated power of the reference carrier. |
| AcpResultsUpperOffsetFrequencyReferenceCarrier | 1,052,718 | Returns the carrier index of the center frequency that was used as a reference to define the center frequency of the upper (positive) offset channel. Upper offset channels are channels that are to the right of the reference carrier. The reference carrier is the carrier that has an offset closest to the lower offset channel. |
| AcpResultsUpperOffsetFrequency | 1,052,719 | Returns the center frequency of the upper offset channel relative to the center frequency of the closest carrier. The sign of offset frequency is negative. |
| AcpResultsUpperOffsetIntegrationBandwidth | 1,052,720 | Returns the integration bandwidth used to measure the power in the upper offset channel. |
| AcpResultsUpperOffsetPowerReferenceCarrier | 1,052,721 | Returns the carrier index of the measured power that was used as a reference to define the upper (positive) offset channel relative power. |
| AcpResultsUpperOffsetAbsolutePower | 1,052,722 | Returns the upper offset channel power. |
| AcpResultsUpperOffsetRelativePower | 1,052,723 | Returns the upper offset channel power, in dB, measured relative to the integrated power of the reference carrier. |
| AcpIFOutputPowerOffsetAuto | 1,052,724 | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. |
| AcpNearIFOutputPowerOffset | 1,052,725 | Specifies the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. |
| AcpFarIFOutputPowerOffset | 1,052,726 | Specifies the offset, in dB, by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. |
| AcpOffsetFrequencyDefinition | 1,052,727 | Specifies the offset frequency definition for the ACP measurement. |
| AcpRbwFilterBandwidthDefinition | 1,052,728 | Specifies the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method. |
| AcpAmplitudeCorrectionType | 1,052,729 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| AcpSequentialFftSize | 1,052,730 | Specifies the FFT size when you set the SetMeasurementMethod(String, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| AcpFftOverlapMode | 1,052,731 | Specifies the overlap mode when you set the SetMeasurementMethod(String, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| AcpFftOverlap | 1,052,732 | Returns the overlap between the consecutive chunks as a percentage of the SetSequentialFftSize(String, Int32) method when you set SetMeasurementMethod(String, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| AcpMeasurementMode | 1,052,733 | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| AcpNoiseCompensationType | 1,052,734 | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| AcpNoiseCalibrationAveragingCount | 1,052,735 | Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) method to False. |
| AcpNoiseCalibrationAveragingAuto | 1,052,736 | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| AcpNoiseCalibrationMode | 1,052,737 | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| AcpDetectorType | 1,052,738 | Specifies the type of detector to be used. |
| AcpDetectorPoints | 1,052,739 | Specifies the number of trace points after the detector is applied. |
| CcdfMeasurementEnabled | 1,056,768 | Specifies whether to enable the complementary cumulative distribution function (CCDF) measurement. |
| CcdfMeasurementInterval | 1,056,770 | Specifies the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement. |
| CcdfNumberOfAnalysisThreads | 1,056,771 | Specifies the maximum number of threads used for parallelism for complementary cumulative distribution function (CCDF) measurement. |
| CcdfNumberOfRecords | 1,056,772 | Specifies the number of acquisitions used for the complementary cumulative distribution function (CCDF) measurement. |
| CcdfRbwFilterRrcAlpha | 1,056,774 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| CcdfRbwFilterBandwidth | 1,056,775 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| CcdfRbwFilterType | 1,056,776 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| CcdfThresholdEnabled | 1,056,777 | Specifies whether to enable thresholding of the acquired samples to be used for the complementary cumulative distribution function (CCDF) measurement. |
| CcdfThresholdLevel | 1,056,778 | Specifies either the relative or absolute threshold power level. |
| CcdfThresholdType | 1,056,779 | Specifies the reference for the power level used for thresholding. |
| CcdfAllTracesEnabled | 1,056,781 | Specifies whether to enable the traces to be stored and retrieved after performing the complementary cumulative distribution function (CCDF) measurement. |
| CcdfResultsMeanPower | 1,056,782 | Returns the average power, in dBm, of all the samples. |
| CcdfResultsMeanPowerPercentile | 1,056,783 | Returns the percentage of samples that have more power than the value returned by the GetMeanPower(String, Double) method. |
| CcdfResultsTenPercentPower | 1,056,784 | Returns the power, in dB, above the mean power, over which 10% of the total samples in the signal are present. |
| CcdfResultsOnePercentPower | 1,056,785 | Returns the power, in dB, above the mean power, over which 1% of the total samples in the signal are present. |
| CcdfResultsOneTenthPercentPower | 1,056,786 | Returns the power, in dB, above the mean power, over which 0.1% of the total samples in the signal are present. |
| CcdfResultsOneHundredthPercentPower | 1,056,787 | Returns the power, in dB, above the mean power, over which 0.01% of the total samples in the signal are present. |
| CcdfResultsOneThousandthPercentPower | 1,056,788 | Returns the power, in dB, above the mean power, over which 0.001% of the total samples in the signal are present. |
| CcdfResultsOneTenThousandthPercentPower | 1,056,789 | Returns the power, in dB, above the mean power, over which 0.0001% of the total samples in the signal are present. |
| CcdfResultsPeakPower | 1,056,790 | Returns the peak power of the acquired signal, relative to the GetMeanPower(String, Double) method. |
| CcdfResultsMeasuredSamplesCount | 1,056,791 | Returns the total number of samples measured. The total number of samples includes only the samples above the threshold, when you set the SetThresholdEnabled(String, RFmxSpecAnMXCcdfThresholdEnabled) to True. |
| ChpMeasurementEnabled | 1,060,864 | Specifies whether to enable the channel power (CHP) measurement. |
| ChpCarrierIntegrationBandwidth | 1,060,866 | Specifies the frequency range, in hertz (Hz), over which the measurement integrates the power. |
| ChpIntegrationBandwidth | 1,060,866 | Obsolete. Specifies the frequency range, in hertz (Hz), over which the measurement integrates the power. |
| ChpNumberOfAnalysisThreads | 1,060,867 | Specifies the maximum number of threads used for parallelism for channel power (CHP) measurement. |
| ChpSpan | 1,060,868 | Specifies the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |
| ChpAveragingCount | 1,060,870 | Specifies the number of acquisitions used for averaging. |
| ChpAveragingEnabled | 1,060,871 | Specifies whether to enable averaging for the channel power (CHP) measurement. |
| ChpAveragingType | 1,060,873 | Specifies the averaging type for averaging multiple spectrum acquisitions. |
| ChpFftWindow | 1,060,874 | Specifies the FFT window type used to reduce spectral leakage. |
| ChpFftPadding | 1,060,875 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. |
| ChpRbwFilterAutoBandwidth | 1,060,876 | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| ChpRbwFilterBandwidth | 1,060,877 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| ChpRbwFilterType | 1,060,878 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| ChpCarrierRrcFilterEnabled | 1,060,879 | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. |
| ChpRrcFilterEnabled | 1,060,879 | Obsolete. Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. |
| ChpCarrierRrcFilterAlpha | 1,060,880 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| ChpRrcFilterAlpha | 1,060,880 | Obsolete. Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| ChpSweepTimeAuto | 1,060,881 | Specifies whether the measurement computes the sweep time. |
| ChpSweepTimeInterval | 1,060,882 | Specifies the sweep time, in seconds. |
| ChpDetectorType | 1,060,883 | Specifies the type of detector to be used. |
| ChpAllTracesEnabled | 1,060,884 | Specifies whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. |
| ChpResultsCarrierAbsolutePower | 1,060,885 | Specifies the carrier power, in dBm, measured in the integration bandwidth that you specify in the SetCarrierIntegrationBandwidth(String, Double) method. |
| ChpResultsAverageChannelPower | 1,060,885 | Obsolete. Specifies the averaged channel power (CHP), in dBm, measured in the specified integration bandwidth. |
| ChpResultsCarrierPsd | 1,060,886 | Specifies the spectral density of the channel, in dBm/Hz. |
| ChpResultsAverageChannelPowerPsd | 1,060,886 | Obsolete. Specifies the spectral density of the averaged channel power (CHP), in dBm/Hz, in the specified integration bandwidth. |
| ChpResultsFrequencyResolution | 1,060,887 | Specifies the frequency resolution, in hertz (Hz), of the spectrum acquired by the measurement. |
| ChpNumberOfCarriers | 1,060,888 | Specifies the number of carriers. |
| ChpCarrierFrequency | 1,060,889 | Specifies the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| ChpResultsTotalCarrierPower | 1,060,890 | Specifies the total integrated carrier power of all carriers, in dBm. |
| ChpResultsCarrierFrequency | 1,060,891 | Specifies the center frequency, in hertz (Hz), of the carrier relative to the SetCenterFrequency(String, Double) method. |
| ChpResultsCarrierIntegrationBandwidth | 1,060,892 | Specifies the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| ChpResultsCarrierRelativePower | 1,060,893 | Specifies the carrier power, in dB, measured relative to the total carrier power of all carriers. |
| ChpRbwFilterBandwidthDefinition | 1,060,894 | Specifies the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method. |
| ChpAmplitudeCorrectionType | 1,060,895 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| ChpMeasurementMode | 1,060,896 | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| ChpNoiseCompensationEnabled | 1,060,897 | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(String, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(String, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| ChpNoiseCompensationType | 1,060,898 | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| ChpNoiseCalibrationAveragingCount | 1,060,899 | Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. |
| ChpNoiseCalibrationAveragingAuto | 1,060,900 | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| ChpNoiseCalibrationMode | 1,060,901 | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| ChpDetectorPoints | 1,060,902 | Specifies the number of trace points after the detector is applied. |
| FcntMeasurementEnabled | 1,064,960 | Specifies whether to enable the frequency count (Fcnt) measurement. |
| FcntMeasurementInterval | 1,064,962 | Specifies the acquisition time, in seconds, for the frequency count (Fcnt) measurement. |
| FcntNumberOfAnalysisThreads | 1,064,963 | Specifies the maximum number of threads used for parallelism for frequency count (Fcnt) measurement. |
| FcntAveragingCount | 1,064,965 | Specifies the number of acquisitions used for averaging. |
| FcntAveragingEnabled | 1,064,966 | Specifies whether to enable averaging for the frequency count (Fcnt) measurement. |
| FcntAveragingType | 1,064,968 | Specifies the averaging type for frequency count (Fcnt) measurement. |
| FcntRbwFilterRrcAlpha | 1,064,969 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| FcntRbwFilterBandwidth | 1,064,970 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| FcntRbwFilterType | 1,064,971 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| FcntThresholdEnabled | 1,064,972 | Specifies whether to enable thresholding of the acquired samples to be used for the frequency count (Fcnt) measurement. |
| FcntThresholdLevel | 1,064,973 | Specifies either the relative or absolute threshold power level. |
| FcntThresholdType | 1,064,974 | Specifies the reference for the power level used for thresholding. |
| FcntAllTracesEnabled | 1,064,976 | Specifies whether to enable the traces to be stored and retrieved after performing the frequency count (Fcnt) measurement. |
| FcntResultsAverageRelativeFrequency | 1,064,977 | Specifies the signal frequency relative to the RF center frequency. Only samples above the threshold are used when you set the method to . |
| FcntResultsMeanPhase | 1,064,978 | Specifies the I/Q samples averaged over all acquisitions. The phase of the sum of these I/Q samples is returned. Only samples above the threshold are used. |
| FcntResultsAverageAbsoluteFrequency | 1,064,979 | Specifies the instantaneous frequency of the samples averaged over all acquisitions. RFmxSpecAn returns the mean of these averaged frequency samples as the average mean frequency. |
| FcntResultsAllanDeviation | 1,064,980 | Returns the two-sample deviation of the measured frequency. |
| HarmMeasurementEnabled | 1,069,056 | Specifies whether to enable the Harmonics measurement. |
| HarmNumberOfAnalysisThreads | 1,069,058 | Specifies the maximum number of threads used for parallelism for Harmonics measurement. |
| HarmFundamentalRbwFilterAlpha | 1,069,059 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| HarmFundamentalRbwFilterBandwidth | 1,069,060 | Specifies the acquisition bandwidth of the fundamental. |
| HarmFundamentalRbwFilterType | 1,069,061 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| HarmFundamentalMeasurementInterval | 1,069,062 | Specifies the acquisition time, in seconds, for the Harmonics measurement. |
| HarmNumberOfHarmonics | 1,069,063 | Specifies the number of Harmonics, including fundamental, to measure. |
| HarmAutoSetupEnabled | 1,069,064 | Specifies whether to enable auto configuration of successive harmonics. |
| HarmHarmonicEnabled | 1,069,065 | Specifies whether to enable a particular harmonic for measurement. |
| HarmHarmonicOrder | 1,069,066 | Specifies the order of the harmonic. |
| HarmHarmonicMeasurementInterval | 1,069,067 | Specifies the acquisition time, in seconds, for the harmonic. |
| HarmAveragingCount | 1,069,068 | Specifies the number of acquisitions used for averaging. |
| HarmAveragingEnabled | 1,069,069 | Specifies whether to enable averaging for the Harmonics measurement. |
| HarmAveragingType | 1,069,071 | Specifies the averaging type for averaging multiple spectrum acquisitions. |
| HarmAllTracesEnabled | 1,069,072 | Specifies whether to enable the traces to be stored and retrieved after performing the Harmonics measurement. |
| HarmResultsFundamentalFrequency | 1,069,073 | Specifies the frequency, in hertz (Hz), used as the fundamental frequency. |
| HarmResultsAverageFundamentalPower | 1,069,074 | Specifies the average power, in dBm, measured at the fundamental frequency. |
| HarmResultsTotalHarmonicDistortion | 1,069,075 | Specifies the total harmonics distortion (THD) measured in percentage of the power in fundamental. |
| HarmResultsHarmonicFrequency | 1,069,076 | Specifies the frequency, in hertz (Hz), of the Harmonics specified by the selector string. |
| HarmResultsHarmonicRbw | 1,069,077 | Specifies the resolution bandwidth (RBW), in hertz (Hz), which is used by the harmonic measurement, for the harmonic specified by the selector string. |
| HarmResultsHarmonicAverageAbsolutePower | 1,069,078 | Specifies the average absolute power, in dBm, measured at the harmonic specified by the active channel string. |
| HarmResultsHarmonicAverageRelativePower | 1,069,079 | Specifies the average power, in dB, relative to the fundamental power measured at the harmonic specified by the selector string. |
| HarmHarmonicBandwidth | 1,069,080 | Specifies the resolution bandwidth, in hertz (Hz), for the harmonic. |
| HarmMeasurementMethod | 1,069,082 | Specifies the method used to perform the harmonics measurement. |
| HarmNoiseCompensationEnabled | 1,069,083 | Specifies whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. |
| ObwMeasurementEnabled | 1,073,152 | Specifies whether to enable occupied bandwidth (OBW) measurement. |
| ObwBandwidthPercentage | 1,073,154 | Specifies the percentage of the total power that is contained in the frequency range defined by the occupied bandwidth (OBW). |
| ObwNumberOfAnalysisThreads | 1,073,155 | Specifies the maximum number of threads used for parallelism for occupied bandwidth (OBW) measurement. |
| ObwSpan | 1,073,156 | Specifies the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |
| ObwAveragingCount | 1,073,158 | Specifies the number of acquisitions used for averaging. |
| ObwAveragingEnabled | 1,073,159 | Specifies whether to enable averaging for the occupied bandwidth (OBW) measurement. |
| ObwAveragingType | 1,073,161 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for occupied bandwidth (OBW) measurement. |
| ObwFftWindow | 1,073,162 | Specifies the FFT window type used to reduce spectral leakage. |
| ObwFftPadding | 1,073,163 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
| ObwRbwFilterAutoBandwidth | 1,073,164 | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| ObwRbwFilterBandwidth | 1,073,165 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| ObwRbwFilterType | 1,073,166 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| ObwSweepTimeAuto | 1,073,167 | Specifies whether the measurement computes the sweep time. |
| ObwSweepTimeInterval | 1,073,168 | Specifies the sweep time, in seconds. |
| ObwAllTracesEnabled | 1,073,170 | Specifies whether to enable the traces to be stored and retrieved after performing the occupied bandwidth (OBW). |
| ObwResultsOccupiedBandwidth | 1,073,171 | Specifies the bandwidth, in hertz (Hz), that occupies the percentage of the total power of the signal that you specify in the SetBandwidthPercentage(String, Double) method. |
| ObwResultsAveragePower | 1,073,172 | Specifies the total power, in dBm, measured in the averaged spectrum acquired by the occupied bandwidth (OBW) measurement. |
| ObwResultsStartFrequency | 1,073,173 | Specifies the start frequency, in hertz (Hz), of the occupied bandwidth (OBW). |
| ObwResultsStopFrequency | 1,073,174 | Specifies the stop frequency, in hertz (Hz), of the occupied bandwidth (OBW). |
| ObwResultsFrequencyResolution | 1,073,175 | Specifies the frequency resolution, in hertz (Hz), of the spectrum acquired by the occupied bandwidth (OBW) measurement. |
| ObwPowerUnits | 1,073,176 | Specifies the units for the absolute power. |
| ObwRbwFilterBandwidthDefinition | 1,073,177 | Specifies the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method. |
| ObwAmplitudeCorrectionType | 1,073,178 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| PavtMeasurementEnabled | 1,077,248 | Specifies whether to enable the Phase Amplitude Versus Time (PAVT) measurement. |
| PavtMeasurementLocationType | 1,077,250 | Specifies the location at which the segment is measured. |
| PavtNumberOfSegments | 1,077,251 | Specifies the number of segments to be measured. |
| PavtSegmentStartTime | 1,077,252 | Specifies the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(String, RFmxSpecAnMXPavtMeasurementLocationType) method to Time. |
| PavtMeasurementStartTime | 1,077,252 | Obsolete. Specifies the start of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(String, RFmxSpecAnMXPavtMeasurementLocationType) method to Time. |
| PavtMeasurementOffset | 1,077,253 | Specifies the time offset from the start of the segment for which the phase and amplitude values are computed. This value is expressed in seconds. |
| PavtMeasurementLength | 1,077,254 | Specifies the duration within the segment over which the phase and amplitude values are computed. This value is expressed in seconds. |
| PavtAllTracesEnabled | 1,077,255 | Specifies whether to enable the traces to be stored and retrieved after performing the PAVT measurement. |
| PavtResultsMeanRelativePhase | 1,077,258 | Returns the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. |
| PavtResultsMeanRelativeAmplitude | 1,077,259 | Returns the mean amplitude of the segment relative to the first segment of the measurement. This value is expressed in dB. |
| PavtFrequencyOffsetCorrectionEnabled | 1,077,260 | Specifies whether to enable frequency offset correction for the measurement. |
| PavtMeasurementBandwidth | 1,077,261 | Specifies the bandwidth over which the signal is measured. This value is expressed in Hz. |
| PavtResultsMeanAbsoluteAmplitude | 1,077,262 | Returns the mean absolute amplitude of the segment. This value is expressed in dBm. |
| PavtResultsMeanAbsolutePhase | 1,077,263 | Returns the mean absolute phase of the segment. This value is expressed in degrees. |
| PavtSegmentType | 1,077,264 | Specifies the type of segment. |
| PavtSegmentMeasurementOffset | 1,077,265 | Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable. |
| PavtSegmentMeasurementLength | 1,077,266 | Specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable. |
| PavtPhaseUnwrapEnabled | 1,077,267 | Specifies whether the phase measurement results are unwrapped or wrapped. |
| PavtResultsFrequencyErrorMean | 1,077,268 | Returns the mean frequency error of the segment. This value is expressed in Hz |
| PavtMeasurementIntervalMode | 1,077,269 | Specifies the mode of configuring the measurement interval. |
| PavtFrequencyTrackingEnabled | 1,077,270 | Specifies whether to enable frequency offset correction per segment for the measurement. While you set this property to True, ensure that the PavtFrequencyOffsetCorrectionEnabled attribute is set to True and the PavtSegmentType attribute is set to PhaseAndAmplitude. |
| SemMeasurementEnabled | 1,081,344 | Specifies whether to enable spectral emission mask (SEM) measurement. |
| SemNumberOfCarriers | 1,081,346 | Specifies the number of carriers. |
| SemCarrierEnabled | 1,081,347 | Specifies whether to consider the carrier power as part of total carrier power measurement. |
| SemCarrierFrequency | 1,081,348 | Specifies the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| SemCarrierIntegrationBandwidth | 1,081,349 | Specifies the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| SemCarrierRbwFilterAutoBandwidth | 1,081,350 | Specifies whether the measurement computes the resolution bandwidth (RBW) of the carrier. |
| SemCarrierRbwFilterBandwidth | 1,081,351 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal. |
| SemCarrierRbwFilterType | 1,081,352 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| SemCarrierRrcFilterEnabled | 1,081,353 | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel after measuring the carrier channel power. |
| SemCarrierRrcFilterAlpha | 1,081,354 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| SemNumberOfOffsets | 1,081,355 | Specifies the number of offset segment configurations. |
| SemOffsetBandwidthIntegral | 1,081,356 | Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). |
| SemOffsetLimitFailMask | 1,081,357 | Specifies the criteria to determine the measurement fail status. |
| SemOffsetRelativeAttenuation | 1,081,358 | Specifies the attenuation, in dB, relative to the SetExternalAttenuation(String, Double) method. Use this value to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
| SemOffsetAbsoluteLimitMode | 1,081,359 | Specifies whether the absolute limit mask is a flat line or is a line with a slope. |
| SemOffsetAbsoluteLimitStart | 1,081,360 | Specifies the absolute power limit, in dBm, corresponding to the beginning of the offset segment. |
| SemOffsetAbsoluteLimitStop | 1,081,361 | Specifies the absolute power limit, in dBm, corresponding to the end of the offset segment. |
| SemOffsetEnabled | 1,081,362 | Specifies whether to enable the offset segment for the spectral emission mask (SEM) measurement. |
| SemOffsetSideband | 1,081,363 | Specifies whether the offset segment is present on one side, or on both sides of the carriers. |
| SemOffsetStartFrequency | 1,081,364 | Specifies the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. |
| SemOffsetStopFrequency | 1,081,365 | Specifies the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. |
| SemOffsetRbwFilterAutoBandwidth | 1,081,366 | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| SemOffsetRbwFilterBandwidth | 1,081,367 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment. |
| SemOffsetRbwFilterType | 1,081,368 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| SemOffsetRelativeLimitMode | 1,081,369 | Specifies whether the relative limit mask is a flat line or a line with a slope. |
| SemOffsetRelativeLimitStart | 1,081,370 | Specifies the relative power limit, in dB, corresponding to the beginning of the offset segment. |
| SemOffsetRelativeLimitStop | 1,081,371 | Specifies the relative power limit, in dB, corresponding to the end of the offset segment. |
| SemPowerUnits | 1,081,372 | Specifies the power units. |
| SemNumberOfAnalysisThreads | 1,081,373 | Specifies the maximum number of threads used for parallelism for spectral emission mask (SEM) measurement. |
| SemAveragingCount | 1,081,374 | Specifies the number of acquisitions used for averaging. |
| SemAveragingEnabled | 1,081,375 | Specifies whether to enable averaging for the spectral emission mask (SEM) measurement. |
| SemAveragingType | 1,081,377 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectral emission mask (SEM) measurement. |
| SemFftWindow | 1,081,378 | Specifies the FFT window type used to reduce spectral leakage. |
| SemFftPadding | 1,081,379 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This value is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
| SemReferenceType | 1,081,380 | Specifies whether the power reference is the integrated power or the peak power in the closest carrier channel. The least carrier offset is the carrier closest to all the lower (negative) offset segments. The highest carrier offset is the carrier closest to all the upper (positive) offsets segments. |
| SemSweepTimeAuto | 1,081,381 | Specifies whether the measurement computes the sweep time. |
| SemSweepTimeInterval | 1,081,382 | Specifies the sweep time, in seconds. |
| SemAllTracesEnabled | 1,081,383 | Specifies whether to enable the traces to be stored and retrieved after performing the spectral emission mask (SEM) measurement. |
| SemResultsTotalCarrierPower | 1,081,384 | Returns the total integrated power of all the active carriers measured. |
| SemResultsCompositeMeasurementStatus | 1,081,385 | Returns the overall measurement status based on the measurement limits and the fail criteria. |
| SemResultsFrequencyResolution | 1,081,386 | Returns the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement. |
| SemResultsCarrierFrequency | 1,081,387 | Returns the center frequency, in hertz (Hz), of the carrier. |
| SemResultsCarrierIntegrationBandwidth | 1,081,388 | Returns the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| SemResultsCarrierAbsolutePower | 1,081,389 | Returns the carrier power. |
| SemResultsCarrierTotalRelativePower | 1,081,390 | Returns the carrier power, in dB, relative to the total carrier power of all enabled carriers. |
| SemResultsCarrierPeakAbsolutePower | 1,081,391 | Returns the peak power in the carrier channel. |
| SemResultsCarrierPeakFrequency | 1,081,392 | Returns the frequency, in hertz (Hz), at which the peak power occurred in the carrier channel. |
| SemResultsLowerOffsetStartFrequency | 1,081,393 | Returns the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. |
| SemResultsLowerOffsetStopFrequency | 1,081,394 | Returns the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. |
| SemResultsLowerOffsetPowerReferenceCarrier | 1,081,395 | Returns the carrier index for measured power that was used as reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. |
| SemResultsLowerOffsetTotalAbsolutePower | 1,081,396 | Returns the lower (negative) offset segment power measured. |
| SemResultsLowerOffsetTotalRelativePower | 1,081,397 | Returns the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |
| SemResultsLowerOffsetPeakAbsolutePower | 1,081,398 | Returns the peak power measured in the lower (negative) offset segment. |
| SemResultsLowerOffsetPeakRelativePower | 1,081,399 | Returns the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |
| SemResultsLowerOffsetPeakFrequency | 1,081,400 | Returns the frequency, in hertz (Hz), at which the peak power occurred in the offset segment. |
| SemResultsLowerOffsetMargin | 1,081,401 | Returns the margin, in dB, from the limit mask. |
| SemResultsLowerOffsetMarginAbsolutePower | 1,081,402 | Returns the power, at which the margin occurred in the lower (negative) offset segment. |
| SemResultsLowerOffsetMarginRelativePower | 1,081,403 | Returns the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |
| SemResultsLowerOffsetMarginFrequency | 1,081,404 | Returns the frequency, in hertz (Hz), at which the margin occurred in the lower (negative) offset segment. |
| SemResultsLowerOffsetMeasurementStatus | 1,081,405 | Returns the lower offset measurement status based on measurement limits and the fail criteria. |
| SemResultsUpperOffsetStartFrequency | 1,081,406 | Returns the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. |
| SemResultsUpperOffsetStopFrequency | 1,081,407 | Returns the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. |
| SemResultsUpperOffsetPowerReferenceCarrier | 1,081,408 | Returns the carrier index for measured power that was used as reference to define the upper (positive) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. |
| SemResultsUpperOffsetTotalAbsolutePower | 1,081,409 | Returns the upper (positive) offset segment power. |
| SemResultsUpperOffsetTotalRelativePower | 1,081,410 | Returns the power in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |
| SemResultsUpperOffsetPeakAbsolutePower | 1,081,411 | Returns the peak power measured in the upper (positive) offset segment. |
| SemResultsUpperOffsetPeakRelativePower | 1,081,412 | Returns the peak power in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |
| SemResultsUpperOffsetPeakFrequency | 1,081,413 | Returns the frequency, in hertz (Hz), at which the peak power occurred in the offset segment. |
| SemResultsUpperOffsetMargin | 1,081,414 | Returns the margin, in dB, from the limit mask. |
| SemResultsUpperOffsetMarginAbsolutePower | 1,081,415 | Returns the power, in dB, at which the margin occurred in the upper (positive) offset segment. |
| SemResultsUpperOffsetMarginRelativePower | 1,081,416 | Returns the power, in dB, at which the margin occurred in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |
| SemResultsUpperOffsetMarginFrequency | 1,081,417 | Returns the frequency, in hertz (Hz), at which the margin occurred in the upper (positive) offset. |
| SemResultsUpperOffsetMeasurementStatus | 1,081,418 | Returns the upper offset measurement status based on measurement limits and the fail criteria. |
| SemCarrierChannelBandwidth | 1,081,419 | Specifies the channel bandwidth, in hertz (Hz), of the carrier. |
| SemOffsetFrequencyDefinition | 1,081,420 | Specifies the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels. |
| SemOffsetRbwFilterBandwidthDefinition | 1,081,421 | Specifies the bandwidth definition which you use to specify the value of the SetOffsetRbwFilterBandwidth(String, Double) method. |
| SemCarrierRbwFilterBandwidthDefinition | 1,081,422 | Specifies the bandwidth definition which you use to specify the value of the SetCarrierRbwFilterBandwidth(String, Double) method. |
| SemAmplitudeCorrectionType | 1,081,423 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| SpectrumMeasurementEnabled | 1,085,440 | Specifies whether to enable Spectrum measurement. |
| SpectrumNumberOfAnalysisThreads | 1,085,442 | Specifies the maximum number of threads used for parallelism for Spectrum measurement. |
| SpectrumSpan | 1,085,443 | Specifies the frequency range, in hertz (Hz), around the center frequency to be acquired for the measurement. |
| SpectrumAveragingCount | 1,085,445 | Specifies the number of acquisitions used for averaging. |
| SpectrumAveragingEnabled | 1,085,446 | Specifies whether to enable averaging for the Spectrum measurement. |
| SpectrumAveragingType | 1,085,448 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for Spectrum measurement. |
| SpectrumFftWindow | 1,085,449 | Specifies the FFT window type used to reduce spectral leakage. |
| SpectrumFftPadding | 1,085,450 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
| SpectrumRbwFilterAutoBandwidth | 1,085,451 | Specifies whether the resolution bandwidth (RBW) is computed by the measurement. |
| SpectrumRbwFilterBandwidth | 1,085,452 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal. |
| SpectrumRbwFilterType | 1,085,453 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| SpectrumSweepTimeAuto | 1,085,454 | Specifies whether the measurement computes the sweep time. |
| SpectrumSweepTimeInterval | 1,085,455 | Specifies the sweep time, in seconds. |
| SpectrumNoiseCompensationEnabled | 1,085,456 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| SpectrumResultsPeakAmplitude | 1,085,458 | Specifies the peak amplitude, in dBm, of the averaged spectrum. |
| SpectrumResultsPeakFrequency | 1,085,459 | Specifies the frequency, in hertz (Hz), at the peak amplitude of the averaged spectrum. |
| SpectrumResultsFrequencyResolution | 1,085,460 | Specifies the frequency resolution, in hertz (Hz), of the spectrum acquired by the measurement. |
| SpectrumPowerUnits | 1,085,461 | Specifies the units for the absolute power. |
| SpectrumRbwFilterBandwidthDefinition | 1,085,462 | Specifies the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method. |
| SpectrumAmplitudeCorrectionType | 1,085,463 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| SpectrumDetectorType | 1,085,464 | Specifies the type of detector to be used. |
| SpectrumDetectorPoints | 1,085,465 | Specifies the number of trace points after the detector is applied. |
| SpectrumVbwFilterAutoBandwidth | 1,085,466 | Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |
| SpectrumVbwFilterBandwidth | 1,085,467 | Specifies the video bandwidth (VBW) in Hz when you set the SetVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth) method to False. |
| SpectrumVbwFilterVbwToRbwRatio | 1,085,468 | Specifies the VBW to RBW Ratio when you set the SetVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth) method to True . |
| SpectrumMeasurementMode | 1,085,470 | Specifies whether the measurement calibrates the noise floor of analyzer or performs the spectrum measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SpectrumNoiseCompensationType | 1,085,471 | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| SpectrumNoiseCalibrationAveragingCount | 1,085,472 | Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(String, RFmxSpecAnMXSpectrumNoiseCalibrationAveragingAuto) method to False. |
| SpectrumNoiseCalibrationAveragingAuto | 1,085,473 | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| SpectrumNoiseCalibrationMode | 1,085,474 | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SpectrumAnalysisInput | 1,085,475 | Specifies whether to analyze just the real I or Q component of the acquired IQ data, or analyze the complex IQ data. |
| SpectrumFftOverlapMode | 1,085,476 | Specifies the overlap mode when you set the SpectrumMeasurementMethod method to SequentialFft. |
| SpectrumFftOverlap | 1,085,477 | Specifies the samples to overlap between the consecutive chunks as a percentage of the SpectrumSequentialFftSize method when you set the SpectrumMeasurementMethod method to SequentialFft and the SpectrumFftOverlapMode method to UserDefined. This value is expressed as a percentage. |
| SpectrumFftOverlapType | 1,085,478 | Specifies the overlap type when you set the SpectrumMeasurementMethod method to SequentialFft. |
| SpectrumMeasurementMethod | 1,085,479 | Specifies the method for performing the Spectrum measurement. |
| SpectrumSequentialFftSize | 1,085,480 | Specifies the FFT size when you set the SpectrumMeasurementMethod method to SequentialFft. If the method SpectrumRbwFilterAutoBandwidth is False, FFT Size is auto computed based on the configured SpectrumRbwFilterBandwidth |
| SpurMeasurementEnabled | 1,089,536 | Specifies whether to enable spurious emission (Spur) measurement. |
| SpurNumberOfAnalysisThreads | 1,089,539 | Specifies the maximum number of threads used for parallelism for spurious emission (Spur) measurement. |
| SpurNumberOfRanges | 1,089,540 | Specifies the number of range configurations. |
| SpurRangeEnabled | 1,089,541 | Specifies whether to measure the spurious emissions in the frequency range. |
| SpurRangeRelativeAttenuation | 1,089,542 | Specifies the attenuation, in dB, relative to the value of the SetExternalAttenuation(String, Double) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
| SpurRangeNumberOfSpursToReport | 1,089,543 | Specifies the number of spurious emissions (Spur) that the measurement should report in the frequency range. |
| SpurRangeStartFrequency | 1,089,544 | Specifies the start frequency of the frequency range, in hertz (Hz), for the measurement. |
| SpurRangeStopFrequency | 1,089,545 | Specifies the stop frequency of the frequency range, in hertz (Hz), for the measurement. |
| SpurAveragingCount | 1,089,546 | Specifies the number of acquisitions used for averaging. |
| SpurAveragingEnabled | 1,089,547 | Specifies whether to enable averaging for the spurious emission (Spur) measurement. |
| SpurAveragingType | 1,089,549 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spurious emission (Spur) measurement. |
| SpurFftWindow | 1,089,551 | Specifies the FFT window type used to reduce spectral leakage. |
| SpurRangeAbsoluteLimitMode | 1,089,552 | Specifies whether the absolute limit threshold is a flat line or a line with a slope. |
| SpurRangeAbsoluteLimitStart | 1,089,553 | Specifies the absolute power limit, in dBm, corresponding to the beginning of the frequency range. |
| SpurRangeAbsoluteLimitStop | 1,089,554 | Specifies the absolute power limit, in dBm, corresponding to the end of the frequency range. |
| SpurRangeRbwFilterAutoBandwidth | 1,089,555 | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| SpurRangeRbwFilterBandwidth | 1,089,556 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal. |
| SpurRangeRbwFilterType | 1,089,557 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| SpurRangeSweepTimeAuto | 1,089,558 | Specifies whether the measurement computes the sweep time. |
| SpurRangeSweepTimeInterval | 1,089,559 | Specifies the sweep time, in seconds. |
| SpurAllTracesEnabled | 1,089,560 | Specifies whether to enable the traces to be stored and retrieved after performing the spurious emissions (Spur) measurement. |
| SpurResultsMeasurementStatus | 1,089,561 | Returns the overall measurement status. |
| SpurResultsRangeSpurFrequency | 1,089,562 | Returns the frequency, in hertz (Hz), of the detected spurious emission (Spur). |
| SpurResultsRangeSpurAmplitude | 1,089,563 | Returns the power, in dBm, of the detected spurious emission (Spur). |
| SpurResultsRangeSpurAbsoluteLimit | 1,089,564 | Returns the threshold, in dBm, used to calculate the margin of the detected spurious emission (Spur). |
| SpurResultsRangeSpurMargin | 1,089,565 | Returns the difference between the amplitude and the absolute limit of the detected spurious emission (Spur). |
| SpurResultsRangeMeasurementStatus | 1,089,566 | Returns the measurement status for the frequency range. |
| SpurResultsRangeSpurNumberOfDetectedSpurs | 1,089,567 | Specifies the number of detected spurious emissions (Spur) in the specified frequency range. |
| SpurTraceRangeIndex | 1,089,568 | Specifies the index of the range used to store and retrieve spurious emission (Spur) traces. |
| SpurRangePeakThreshold | 1,089,569 | Specifies the threshold level, in dBm, above which the measurement detects spurs in the range that you specify using the SetRangeStartFrequency(String, Double) and SetRangeStopFrequency(String, Double) methods. |
| SpurRangePeakExcursion | 1,089,570 | Specifies the peak excursion value, in dB, used to find the spurs in the spectrum. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered a spur. |
| SpurRangeRbwFilterBandwidthDefinition | 1,089,571 | Specifies the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(String, Double) method. |
| SpurAmplitudeCorrectionType | 1,089,572 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| SpurRangeDetectorType | 1,089,573 | Specifies the type of detector to be used. Use "range(n)" as the selector string to configure or read this method. |
| SpurRangeDetectorPoints | 1,089,574 | Specifies the number of range points after the detector is applied. Use "range(n)" as the selector string to configure or read this method. |
| SpurRangeVbwFilterAutoBandwidth | 1,089,575 | Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |
| SpurRangeVbwFilterBandwidth | 1,089,576 | Specifies the video bandwidth (VBW) in Hz when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to False. |
| SpurRangeVbwFilterVbwToRbwRatio | 1,089,577 | Specifies the VBW to RBW Ratio when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to True. |
| TxpMeasurementEnabled | 1,093,632 | Specifies whether to enable transmit power (TXP) measurement. |
| TxpMeasurementInterval | 1,093,634 | Specifies the acquisition time, in seconds, for the transmit power (TXP) measurement. |
| TxpNumberOfAnalysisThreads | 1,093,635 | Specifies the maximum number of threads used for parallelism for transmit power (TXP) measurement. |
| TxpAveragingCount | 1,093,637 | Specifies the number of acquisitions used for averaging. |
| TxpAveragingEnabled | 1,093,638 | Specifies whether to enable averaging for the transmit power (TXP) measurement. |
| TxpAveragingType | 1,093,640 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for transmit power (TXP) measurement. |
| TxpRbwFilterAlpha | 1,093,641 | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| TxpRbwFilterBandwidth | 1,093,642 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| TxpRbwFilterType | 1,093,643 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| TxpThresholdEnabled | 1,093,644 | Specifies whether to enable thresholding of the acquired samples to be used for the transmit power (TXP) measurement. |
| TxpThresholdLevel | 1,093,645 | Specifies the relative or absolute threshold power level. |
| TxpThresholdType | 1,093,646 | Specifies the reference for the power level that is used as the threshold. |
| TxpAllTracesEnabled | 1,093,648 | Specifies whether to enable the traces to be stored and retrieved after performing the transmit power (TXP) measurement. |
| TxpResultsAverageMeanPower | 1,093,649 | Specifies the mean power, in dBm, of the signal. |
| TxpResultsPeakToAverageRatio | 1,093,650 | Specifies the ratio of the peak power of the signal to the mean power. |
| TxpResultsMaximumPower | 1,093,651 | Specifies the maximum power, in dBm, of the averaged power trace. |
| TxpResultsMinimumPower | 1,093,652 | Specifies the minimum power, in dBm, of the averaged power trace. |
| TxpVbwFilterAutoBandwidth | 1,093,655 | Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |
| TxpVbwFilterBandwidth | 1,093,656 | Specifies the video bandwidth when you set the SetVbwFilterAutoBandwidth(String, RFmxSpecAnMXTxpVbwFilterAutoBandwidth) method to False. |
| TxpVbwFilterVbwToRbwRatio | 1,093,657 | Specifies the VBW to RBW Ratio when you set the SetVbwFilterAutoBandwidth(String, RFmxSpecAnMXTxpVbwFilterAutoBandwidth) method to True. |
| ResultFetchTimeout | 1,097,728 | Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
| AmpmMeasurementEnabled | 1,105,920 | Specifies whether to enable the AMPM measurement. |
| AmpmAMToAMCurveFitOrder | 1,105,922 | Specifies the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test. |
| AmpmAMToAMCurveFitType | 1,105,923 | Specifies the cost-function for polynomial approximation of the AM-to-AM characteristic of the device under test. |
| AmpmAMToPMCurveFitOrder | 1,105,924 | Specifies the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test. |
| AmpmAMToPMCurveFitType | 1,105,925 | Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic. |
| AmpmAveragingEnabled | 1,105,926 | Specifies whether to enable averaging for the AMPM measurement. |
| AmpmAveragingCount | 1,105,927 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXAmpmAveragingEnabled) method to True. |
| AmpmMeasurementInterval | 1,105,929 | Specifies the acquisition time, in seconds, for the AMPM measurement. |
| AmpmSignalType | 1,105,930 | Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. |
| AmpmMeasurementSampleRateMode | 1,105,931 | Specifies whether the acquisition sample rate is based on the reference waveform. |
| AmpmMeasurementSampleRate | 1,105,932 | Specifies the acquisition sample rate, in hertz (Hz), when you set the SetMeasurementSampleRateMode(String, RFmxSpecAnMXAmpmMeasurementSampleRateMode) method to User. |
| AmpmThresholdEnabled | 1,105,933 | Specifies whether to enable thresholding of the acquired samples to be used for the AMPM measurement |
| AmpmThresholdType | 1,105,934 | Specifies the reference for the power level used for thresholding. |
| AmpmThresholdLevel | 1,105,935 | Specifies either the relative or absolute threshold power level based on the GetThresholdType(String, RFmxSpecAnMXAmpmThresholdType) method. |
| AmpmDutAverageInputPower | 1,105,936 | Specifies the average power, in dBm, of the signal at the input port of the device under test. |
| AmpmAllTracesEnabled | 1,105,937 | Specifies whether to enable the traces to be stored and retrieved after performing the AMPM measurement. |
| AmpmNumberOfAnalysisThreads | 1,105,938 | Specifies the maximum number of threads used for parallelism for AMPM measurement. |
| AmpmResultsAMToAMCurveFitCoefficients | 1,105,940 | Returns the coefficients of the polynomial that approximates the measured AM-to-AM characteristic of the device under test. |
| AmpmResultsAMToPMCurveFitCoefficients | 1,105,941 | Returns the coefficients of the polynomial that approximates the measured AM-to-PM characteristic of the device under test. |
| AmpmResultsMeanLinearGain | 1,105,942 | Returns the average linear gain, in dB, of the device under test, computed by rejecting signal samples suffering gain compression. |
| AmpmResultsMeanPhaseError | 1,105,943 | Returns the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test. |
| AmpmResultsMeanRmsEvm | 1,105,944 | Returns the ratio, as a percentage, of l2 norm of difference between the normalized reference and acquired waveforms, to the L2 norm of the normalized reference waveform. |
| AmpmResultsAMToAMCurveFitResidual | 1,105,945 | Returns the approximation error, in dB, in the polynomial approximation of the measured AM-to-AM characteristic of the device under test. |
| AmpmResultsAMToPMCurveFitResidual | 1,105,946 | Returns the approximation error, in degrees, in the polynomial approximation of the measured AM-to-PM characteristic of the device under test. |
| AmpmResultsGainErrorRange | 1,105,947 | Returns the peak-to-peak deviation, in dB, in the gain of the device under test. |
| AmpmResultsPhaseErrorRange | 1,105,948 | Returns the peak-to-peak deviation, in degrees, in the phase distortion of the acquired signal relative to the reference waveform caused by the device under test. |
| AmpmResults1dBCompressionPoint | 1,105,949 | Returns the theoretical output power, in dBm, at which gain of the device under test drops by 1 dB from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. This function returns NaN when the AM-to-AM charecteristics of the device under test are flat. |
| AmpmFrequencyOffsetCorrectionEnabled | 1,105,953 | Enables frequency offset correction for the measurement.When Frequency Offset Correction Enabled is True, the measurement computes and corrects any frequency offset between the reference and the acquired waveforms.When Frequency Offset Correction Enabled is False, frequency offset correction is not performed. |
| AmpmMaximumTimingError | 1,105,954 | Specifies the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds. |
| AmpmReferencePowerType | 1,105,955 | Specifies the reference power used for AM to AM and AM to PM traces. |
| AmpmCompressionPointEnabled | 1,105,956 | Specifies computation of compression points corresponding to the compression levels specified by RFmxSpecAnMXAmpmCompressionPointEnabled method. |
| AmpmCompressionPointLevel | 1,105,957 | Specifies the compression levels for which compression points are computed when you set the RFmxSpecAnMXAmpmCompressionPointEnabled method to True. |
| AmpmResultsInputCompressionPoint | 1,105,958 | Returns the theoretical input power at which device gain drops by the compression level, specified through RFmxSpecAnMXAmpmConfiguration.GetCompressionPointLevel Method , from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. this value is expressed in dBm. |
| AmpmResultsOutputCompressionPoint | 1,105,959 | Returns the theoretical output power at which device gain drops by the compression level, specified through RFmxSpecAnMXAmpmConfiguration.GetCompressionPointLevel Method , from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. this value is expressed in dBm. |
| DpdApplyDpdUserLookupTableInputPower | 1,105,960 | Specifies the input power array, in dBm, for the predistortion lookup table when you set the DPD Apply DPD User DPD Model to Lookup Table |
| AmpmIQOriginOffsetCorrectionEnabled | 1,105,961 | Specifies whether to enable the IQ origin offset correction for the measurement. |
| AmpmSynchronizationMethod | 1,105,962 | Specifies the method used for synchronization of acquired waveform with reference waveform. |
| AmpmAutoCarrierDetectionEnabled | 1,105,963 | Specifies if auto detection of carrier offset and carrier bandwidth is enabled. |
| AmpmNumberOfCarriers | 1,105,964 | Specifies the number of carriers in the reference waveform when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. |
| AmpmCarrierOffset | 1,105,965 | Specifies the carrier offset when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
| AmpmCarrierBandwidth | 1,105,966 | Specifies the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
| AmpmEqualizerMode | 1,105,967 | Specifies whether the measurement equalizes the channel. |
| AmpmEqualizerFilterLength | 1,105,968 | Specifies the length of the equalizer filter. The measurement maintains the filter length as an odd number by incrementing any even numbered value by one. |
| AmpmAMToAMEnabled | 1,105,969 | Specifies whether to enable the results that rely on the AM to AM characteristics. |
| AmpmAMToPMEnabled | 1,105,970 | Specifies whether to enable the results that rely on AM to PM characteristics. |
| AmpmEvmEnabled | 1,105,971 | Specifies whether to enable the GetMeanRmsEvm(String, Double) method. |
| AmpmCompressionPointGainReference | 1,105,972 | Specifies the gain reference for compression point calculation. |
| AmpmCompressionPointGainReferencePower | 1,105,973 | Specifies the reference power corresponding to the gain reference to be used for compression point calculation when you set the SetCompressionPointGainReference(String, RFmxSpecAnMXAmpmCompressionPointGainReference) method to ReferencePower. The reference power can be configured as either input or output power based on the value of the SetReferencePowerType(String, RFmxSpecAnMXAmpmReferencePowerType) method. This value is expressed in dBm. |
| AmpmCompressionPointUserGain | 1,105,974 | Specifies the gain to be used as the gain reference for compression point calculation when you set the AmpmCompressionPointGainReference attribute to User Defined. This value is expressed in dB. |
| AmpmResultsCompressionPointGainReference | 1,105,975 | Returns the gain reference used for compression point calculation. This value is expressed in dB. |
| AmpmResultsPeakReferencePower | 1,105,976 | Returns the peak reference power. This value is expressed in dBm. |
| AmpmResultsPeakReferencePowerGain | 1,105,977 | Returns the gain at the peak reference power. This value is expressed in dB. |
| DpdMeasurementEnabled | 1,110,016 | Specifies whether to enable the DPD measurement. |
| DpdMeasurementSampleRateMode | 1,110,018 | Specifies the acquisition sample rate configuration mode. |
| DpdMeasurementSampleRate | 1,110,019 | Specifies the acquisition sample rate, in hertz (Hz), when you set the SetMeasurementSampleRateMode(String, RFmxSpecAnMXDpdMeasurementSampleRateMode) method to User. |
| DpdMeasurementInterval | 1,110,020 | Specifies the acquisition time, in seconds, for the DPD measurement. |
| DpdSignalType | 1,110,021 | Specifies whether the reference waveform is a modulated signal or a combination of tones |
| DpdDutAverageInputPower | 1,110,023 | Specifies the average power of the signal at the input port of the device under test. |
| DpdModel | 1,110,024 | Specifies the DPD model used by the DPD measurement. |
| DpdLookupTableAMToAMCurveFitOrder | 1,110,025 | Specifies the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
| DpdLookupTableAMToAMCurveFitType | 1,110,026 | Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
| DpdLookupTableAMToPMCurveFitOrder | 1,110,027 | Specifies the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
| DpdLookupTableAMToPMCurveFitType | 1,110,028 | Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
| DpdLookupTableThresholdEnabled | 1,110,029 | Specifies whether to enable thresholding of the acquired samples to be used for the DPD measurement when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
| DpdLookupTableThresholdType | 1,110,030 | Specifies the reference for the power level used for thresholding. |
| DpdLookupTableThresholdLevel | 1,110,031 | Specifies either the relative or absolute threshold power level based on the GetLookupTableThresholdType(String, RFmxSpecAnMXDpdLookupTableThresholdType) method. |
| DpdLookupTableStepSize | 1,110,032 | Specifies the step size, in dB, of the input power levels in the predistortion lookup table when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
| DpdMemoryPolynomialOrder | 1,110,033 | Specifies the order of the digital predistortion (DPD) polynomial when you set the DPD Model to Memory Polynomial |
| DpdMemoryPolynomialMemoryDepth | 1,110,034 | Specifies the memory depth of the digital predistortion (DPD) polynomial when you set the DPD Model to Memory Polynomial |
| DpdMemoryPolynomialLeadOrder | 1,110,035 | Specifies the lead order cross term of the digital predistortion (DPD) polynomial when you set the DPD Model to Generalized Memory Polynomial |
| DpdMemoryPolynomialLagOrder | 1,110,036 | Specifies the lag order cross term of the digital predistortion (DPD) polynomial when you set the DPD Model to Generalized Memory Polynomial |
| DpdMemoryPolynomialLeadMemoryDepth | 1,110,037 | Specifies the lead memory depth cross term of the digital predistortion (DPD) polynomial when you set the DPD Model to Generalized Memory Polynomial |
| DpdMemoryPolynomialLagMemoryDepth | 1,110,038 | Specifies the lag memory depth cross term of the digital predistortion (DPD) polynomial when you set the DPD Model to Generalized Memory Polynomial |
| DpdMemoryPolynomialMaximumLead | 1,110,039 | Specifies the maximum lead stagger cross term of the digital predistortion (DPD) polynomial when you set the DPD Model to Generalized Memory Polynomial |
| DpdMemoryPolynomialMaximumLag | 1,110,040 | Specifies the maximum lag stagger cross term of the digital predistortion (DPD) polynomial when you set the DPD Model to Generalized Memory Polynomial |
| DpdIterativeDpdEnabled | 1,110,042 | Specifies whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture |
| DpdAveragingEnabled | 1,110,044 | Specifies whether to enable averaging for the digital predistortion (DPD) measurement. |
| DpdAveragingCount | 1,110,045 | Specifies the number of acquisitions used for averaging when you set the DPD Averaging Enabled to True |
| DpdAllTracesEnabled | 1,110,047 | Specifies whether to enable the traces to be stored and retrieved after performing the digital predistortion (DPD) measurement. |
| DpdNumberOfAnalysisThreads | 1,110,048 | Specifies the maximum number of threads used for parallelism for the digital predistortion (DPD) measurement |
| DpdApplyDpdConfigurationInput | 1,110,049 | Specifies whether to use the configuration used by the DPD measurement for applying the digital predistortion (DPD). |
| DpdApplyDpdLookupTableCorrectionType | 1,110,050 | Specifies the predistortion type when you set the DPD Model to Lookup Table |
| DpdApplyDpdHeadroomMode | 1,110,051 | Obsolete. Specifies whether to compute and apply the headroom of the predistorted waveform or to apply the value specified using DPD Apply DPD Headroom on the predistorted waveform. |
| DpdApplyDpdHeadroom | 1,110,052 | Obsolete. Specifies the headroom, in dB, applied to the predistorted waveform when you set the DPD Apply DPD Headroom Mode to Manual |
| DpdApplyDpdUserDutAverageInputPower | 1,110,053 | Specifies the average input power for the device under test, in dBm, that was used to compute the DPD Apply DPD User DPD Polynomial or the DPD Apply DPD User LUT Complex Gain when you set the DPD Apply DPD Config Input to User |
| DpdApplyDpdUserDpdModel | 1,110,054 | Specifies the DPD model for applying digital predistortion (DPD) when you set the DPD Apply DPD Config Input to User |
| DpdApplyDpdUserMeasurementSampleRate | 1,110,055 | Specifies the acquisition sample rate, in hertz (Hz), that was used to compute the DPD Apply DPD User DPD Polynomial or DPD Apply DPD User LUT Complex Gain when you set the DPD Apply DPD Config Input to User |
| DpdApplyDpdUserMemoryPolynomialOrder | 1,110,058 | Specifies the order of the DPD polynomial when you set the DPD Apply DPD User DPD Model to Memory Polynomial |
| DpdApplyDpdUserMemoryPolynomialMemoryDepth | 1,110,059 | Specifies the memory depth of the DPD polynomial when you set the DPD Apply DPD User DPD Model to Memory Polynomial |
| DpdApplyDpdUserMemoryPolynomialLeadOrder | 1,110,060 | Specifies the lead order cross term of the digital predistortion (DPD) polynomial when you set the DPD Apply DPD User DPD Model to Generalized Memory Polynomial |
| DpdApplyDpdUserMemoryPolynomialLagOrder | 1,110,061 | Specifies the lag order cross term of the digital predistortion (DPD) polynomial when you set the DPD Apply DPD User DPD Model to Generalized Memory Polynomial |
| DpdApplyDpdUserMemoryPolynomialLeadMemoryDepth | 1,110,062 | Specifies the lead memory depth cross term of the digital predistortion (DPD) polynomial when you set the DPD Apply DPD User DPD Model to Generalized Memory Polynomial |
| DpdApplyDpdUserMemoryPolynomialLagMemoryDepth | 1,110,063 | Specifies the lag memory depth cross term of the digital predistortion (DPD) polynomial when you set the DPD Apply DPD User DPD Model to Memory Polynomial or Generalized Memory Polynomial and set the DPD Apply DPD Config Input to User. |
| DpdApplyDpdUserMemoryPolynomialMaximumLead | 1,110,064 | Specifies the maximum lead stagger cross term of the digital predistortion (DPD) polynomial when you set the DPD Apply DPD User DPD Model to Memory Polynomial or Generalized Memory Polynomial and set the DPD Apply DPD Config Input to User. |
| DpdApplyDpdUserMemoryPolynomialMaximumLag | 1,110,065 | Specifies the maximum lag stagger cross term of the digital predistortion (DPD) polynomial when you set the DPD Apply DPD User DPD Model to Memory Polynomial or Generalized Memory Polynomial and set the DPD Apply DPD Config Input to User. |
| DpdResultsAverageGain | 1,110,067 | Specifies the average gain, in dB, of the device under test. |
| DpdApplyDpdMemoryModelCorrectionType | 1,110,070 | Specifies the predistortion type when DPD Model is Memory Polynomial or Generalized Memory Polynomial. |
| DpdTargetGainType | 1,110,071 | Specifies the gain expected from the DUT after applying DPD on the input waveform. |
| DpdLookupTableType | 1,110,072 | Specifies the type of the DPD lookup table (LUT). |
| DpdFrequencyOffsetCorrectionEnabled | 1,110,073 | Specifies whether to enable frequency offset correction for the DPD measurement. |
| DpdMaximumTimingError | 1,110,074 | Specifies the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds. |
| DpdNmseEnabled | 1,110,075 | Specifies whether to enable the normalized mean-squared error (NMSE) computation. |
| DpdPreDpdCfrEnabled | 1,110,076 | Specifies whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning. |
| DpdPreDpdCfrMaximumIterations | 1,110,077 | Specifies the maximum number of iterations required to converge waveform PAPR to target PAPR, when you set the DpdPreDpdCfrEnabled method to True. |
| DpdPreDpdCfrMethod | 1,110,078 | Specifies the method used to perform crest factor reduction (CFR) when you set the DpdPreDpdCfrEnabled method to True. Refer to DPD concept topic for more information about CFR methods. |
| DpdApplyDpdUserLookupTableType | 1,110,080 | Specifies the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method to User. |
| DpdPreDpdCfrTargetPapr | 1,110,081 | Specifies the target peak-to-average power ratio when you set the DpdPreDpdCfrEnabled method to True. This value is expressed in dB. |
| DpdPreDpdCfrWindowType | 1,110,082 | Specifies the window type to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to PeakWindowing. |
| DpdPreDpdCfrWindowLength | 1,110,083 | Specifies the maximum window length to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to PeakWindowing. |
| DpdPreDpdCfrShapingFactor | 1,110,084 | Specifies the shaping factor to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to Sigmoid. Refer to the DPD concept topic for more information about shaping factor. |
| DpdPreDpdCfrShapingThreshold | 1,110,085 | Specifies the shaping threshold to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to the DPD concept topic for more information about shaping threshold. |
| DpdApplyDpdCfrEnabled | 1,110,086 | Specifies whether to enable the crest factor reduction (CFR) on the pre-distorted waveform. |
| DpdApplyDpdCfrMethod | 1,110,087 | Specifies the method used to perform the crest factor reduction (CFR) when you set the DpdApplyDpdCfrEnabled method to True. |
| DpdApplyDpdCfrMaximumIterations | 1,110,088 | Specifies the maximum number of iterations to converge a waveform PAPR to target PAPR when you set the DpdApplyDpdCfrEnabled method to True. |
| DpdApplyDpdCfrTargetPaprType | 1,110,089 | Specifies the target PAPR type when you set the DpdApplyDpdCfrEnabled method to True. |
| DpdSynchronizationMethod | 1,110,090 | Specifies the method used for synchronization of the acquired waveform with the reference waveform. |
| DpdAutoCarrierDetectionEnabled | 1,110,091 | Specifies if auto detection of carrier offset and carrier bandwidth is enabled. |
| DpdNumberOfCarriers | 1,110,092 | Specifies the number of carriers in the reference waveform when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. |
| DpdCarrierOffset | 1,110,093 | Specifies the carrier offset when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
| DpdCarrierBandwidth | 1,110,094 | Specifies the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |
| DpdMemoryPolynomialOrderType | 1,110,095 | Configures the type of terms of the DPD polynomial when you set RFmxSpecAnMXDpdModel to MemoryPolynomial or GeneralizedMemoryPolynomial. |
| DpdMemoryPolynomialLeadOrderType | 1,110,096 | Configures the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |
| DpdMemoryPolynomialLagOrderType | 1,110,097 | Configures the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |
| DpdApplyDpdCfrTargetPapr | 1,110,106 | Specifies the target PAPR when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrTargetPaprType method to Custom. This value is expressed in dB. |
| DpdApplyDpdCfrWindowType | 1,110,107 | Specifies the window type to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |
| DpdApplyDpdCfrWindowLength | 1,110,108 | Specifies the maximum window length to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |
| DpdApplyDpdCfrShapingFactor | 1,110,109 | Specifies the shaping factor to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. Refer to DPD concept topic for more information about shaping factor. |
| DpdApplyDpdCfrShapingThreshold | 1,110,110 | Specifies the shaping threshold to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. |
| DpdResultsNmse | 1,110,111 | Returns the normalized mean-squared DPD modeling error when you set the SetNmseEnabled(String, RFmxSpecAnMXDpdNmseEnabled) method to True. This value is expressed in dB. |
| DpdPreDpdCfrFilterEnabled | 1,110,112 | Specifies whether to enable the filtering operation when you set the DpdApplyDpdCfrEnabled method to True. Refer to DPD concept topic for more information about filtering. |
| DpdPreDpdCfrNumberOfCarriers | 1,110,114 | Specifies the number of carriers in the input waveform when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. |
| DpdPreDpdCarrierOffset | 1,110,115 | Specifies the carrier offset relative to the center of the complex baseband equivalent of the RF signal when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz. |
| DpdPreDpdCarrierBandwidth | 1,110,116 | Specifies the carrier bandwidth when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz. |
| DpdIQOriginOffsetCorrectionEnabled | 1,110,117 | Specifies whether to enable the IQ origin offset correction for the measurement. |
| IQMeasurementEnabled | 1,110,272 | Specifies whether to enable the IQ measurement. |
| IQSampleRate | 1,110,274 | Specifies the I/Q sample rate. |
| IQNumberOfRecords | 1,110,275 | Specifies the number of records to acquire. |
| IQAcquisitionTime | 1,110,276 | Specifies the I/Q acquisition time. |
| IQPretriggerTime | 1,110,277 | Specifies the I/Q pretrigger time. |
| IQBandwidthAuto | 1,110,280 | Specifies whether the measurement computes the minimum acquisition bandwidth. |
| IQBandwidth | 1,110,281 | Specifies the minimum acquisition bandwidth, in hertz (Hz), when you set the SetBandwidthAuto(String, RFmxSpecAnMXIQBandwidthAuto) method to False. |
| IQDeleteRecordOnFetch | 1,110,282 | Specifies whether the measurement deletes the fetched record. |
| IMMeasurementEnabled | 1,114,112 | Specifies whether to enable the IM measurement. |
| IMFrequencyDefinition | 1,114,114 | Specifies whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. |
| IMFundamentalLowerToneFrequency | 1,114,115 | Specifies the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |
| IMFundamentalUpperToneFrequency | 1,114,116 | Specifies the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |
| IMAutoIntermodsSetupEnabled | 1,114,117 | Specifies whether the measurement computes the intermod frequencies or uses user-specified frequencies. |
| IMMaximumIntermodOrder | 1,114,118 | Specifies the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order. |
| IMNumberOfIntermods | 1,114,119 | Specifies the number of intermods to measure when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to False. |
| IMIntermodEnabled | 1,114,120 | Specifies whether to enable an intermod for the IM measurement. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
| IMIntermodOrder | 1,114,121 | Specifies the order of the intermod. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
| IMIntermodSide | 1,114,122 | Specifies whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
| IMLowerIntermodFrequency | 1,114,123 | Specifies the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
| IMUpperIntermodFrequency | 1,114,124 | Specifies the frequency of the upper intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
| IMMeasurementMethod | 1,114,125 | Specifies the method used to perform the IM measurement. |
| IMRbwFilterAutoBandwidth | 1,114,126 | Specifies whether the measurement computes the RBW. |
| IMRbwFilterBandwidth | 1,114,127 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxSpecAnMXIMRbwFilterAutoBandwidth) method to False. This value is expressed in Hz. |
| IMRbwFilterType | 1,114,128 | Specifies the response of the digital RBW filter. |
| IMSweepTimeAuto | 1,114,129 | Specifies whether the measurement computes the sweep time. |
| IMSweepTimeInterval | 1,114,130 | Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxSpecAnMXIMSweepTimeAuto) method to False. This value is expressed in seconds. |
| IMAveragingEnabled | 1,114,131 | Specifies whether to enable averaging for the IM measurement. |
| IMAveragingCount | 1,114,132 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXIMAveragingEnabled) method to True. |
| IMAveragingType | 1,114,134 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. |
| IMFftWindow | 1,114,135 | Specifies the FFT window type to use to reduce spectral leakage. |
| IMFftPadding | 1,114,136 | Specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. |
| IMIFOutputPowerOffsetAuto | 1,114,137 | Specifies whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. |
| IMNearIFOutputPowerOffset | 1,114,138 | Specifies the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |
| IMFarIFOutputPowerOffset | 1,114,139 | Specifies the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |
| IMAllTracesEnabled | 1,114,140 | Specifies whether to enable the traces to be stored and retrieved after performing the IM measurement. |
| IMNumberOfAnalysisThreads | 1,114,141 | Specifies the maximum number of threads used for parallelism for the IM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| IMResultsFundamentalLowerTonePower | 1,114,143 | Returns the peak power measured around the lower tone frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the lower tone frequency. |
| IMResultsFundamentalUpperTonePower | 1,114,145 | Returns the peak power measured around the upper tone frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the upper tone frequency. |
| IMResultsIntermodOrder | 1,114,146 | Returns the order of the intermod. |
| IMResultsLowerIntermodPower | 1,114,148 | Returns the peak power measured around the lower intermod frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the lower intermod frequency. |
| IMResultsUpperIntermodPower | 1,114,150 | Returns the peak power measured around the upper intermod frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the upper intermod frequency. |
| IMResultsLowerOutputInterceptPower | 1,114,151 | Returns the lower output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. |
| IMResultsUpperOutputInterceptPower | 1,114,152 | Returns the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. |
| IMResultsWorstCaseOutputInterceptPower | 1,114,153 | Returns the worst case output intercept power which is equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm. |
| IMLocalPeakSearchEnabled | 1,114,154 | Specifies whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. |
| IMAmplitudeCorrectionType | 1,114,155 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| IMResultsLowerIntermodRelativePower | 1,114,160 | Returns the relative peak power measured around the lower intermod frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBc. When you set the IM Local Peak Search Enabled method to False, the measurement returns the relative power at the lower intermod frequency. |
| IMResultsUpperIntermodRelativePower | 1,114,161 | Returns the relative peak power measured around the upper intermod frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBc. When you set the IM Local Peak Search Enabled method to False, the measurement returns the relative power at the upper intermod frequency. |
| IMResultsWorstCaseIntermodAbsolutePower | 1,114,162 | Returns the worst case intermod power that is equal to the maximum of the values of both the IM Results Upper Intermod Power and IM Results Lower Intermod Power results. This value is expressed in dBm. |
| IMResultsWorstCaseIntermodRelativePower | 1,114,163 | Returns the worst case intermod relative power that is equal to the maximum of the values of both the IM Results Upper Intermod Relative Power and IM Results Lower Intermod Relative Power results. This value is expressed in dBc. |
| NFMeasurementEnabled | 1,179,649 | Enables the noise figure (NF) measurement. |
| NFFrequencyList | 1,179,652 | Specifies the list of frequencies at which the noise figure (NF) of the DUT is computed. This value is expressed in Hz. |
| NFMeasurementBandwidth | 1,179,653 | Specifies the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz. |
| NFMeasurementInterval | 1,179,654 | Specifies the duration for which the signals are acquired at each frequency which you specify in the SetFrequencyList(String, Double) method. This value is expressed in seconds. |
| NFAveragingEnabled | 1,179,655 | Specifies whether to enable averaging for the noise figure (NF) measurement. |
| NFAveragingCount | 1,179,656 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXNFAveragingEnabled) method to True. |
| NFMeasurementMethod | 1,179,657 | Specifies the measurement method used to perform the noise figure (NF) measurement. |
| NFYFactorMode | 1,179,658 | Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFYFactorNoiseSourceEnr | 1,179,660 | Specifies the array of effective noise ratio (ENR) values of the noise source as a function of the frequency. This value is expressed in dB. The corresponding frequencies are specified by the SetYFactorNoiseSourceEnrFrequency(String, Double) method. This method is used only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFYFactorNoiseSourceEnrFrequency | 1,179,661 | Specifies an array of frequencies corresponding to the effective noise ratio (ENR) values specified by the SetYFactorNoiseSourceEnr(String, Double) method. This value is expressed in Hz. |
| NFYFactorNoiseSourceColdTemperature | 1,179,662 | Specifies the calibrated cold noise temperature of the noise source used in the Y-Factor method. This value is expressed in kelvin. |
| NFYFactorNoiseSourceOffTemperature | 1,179,663 | Specifies the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin. |
| NFYFactorNoiseSourceSettlingTime | 1,179,664 | Specifies the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This value is expressed in seconds. |
| NFDutInputLossCompensationEnabled | 1,179,665 | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the noise source and the input port of the DUT, excluding the losses that are common to calibration and the measurement steps for the Y-Factor method, which are specified by the SetYFactorNoiseSourceLoss(String, Double) method. |
| NFDutInputLoss | 1,179,666 | Specifies an array of the the ohmic losses between the noise source and the input port of the DUT, as a function of the frequency. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the SetDutInputLossCompensationEnabled(String, RFmxSpecAnMXNFDutInputLossCompensationEnabled) method to True. You must exclude any loss which is inherent to the noise source and is common between the calibration and measurement steps, and configure the loss using the SetYFactorNoiseSourceLoss(String, Double) method. Specify the frequencies at which the losses were measured using the SetDutInputLossFrequency(String, Double) method. |
| NFDutInputLossFrequency | 1,179,667 | Specifies an array of frequencies corresponding to the value of the SetDutInputLoss(String, Double) method. This value is expressed in Hz. |
| NFDutInputLossTemperature | 1,179,668 | Specifies the physical temperature of the ohmic loss elements considered in the SetDutInputLoss(String, Double) method. This value is expressed in kelvin. |
| NFDutOutputLossCompensationEnabled | 1,179,669 | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. |
| NFDutOutputLoss | 1,179,670 | Specifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the SetDutOutputLossCompensationEnabled(String, RFmxSpecAnMXNFDutOutputLossCompensationEnabled) method to True. Specify the array of frequencies at which the losses were measured using the SetDutOutputLossFrequency(String, Double) method. |
| NFDutOutputLossFrequency | 1,179,671 | Specifies the array of frequencies corresponding to the value of the SetDutOutputLoss(String, Double) method. This value is expressed in Hz. |
| NFDutOutputLossTemperature | 1,179,672 | Specifies the physical temperature of the ohmic loss elements specified by the SetDutOutputLoss(String, Double) method. This value is expressed in kelvin. |
| NFYFactorNoiseSourceLossCompensationEnabled | 1,179,673 | Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. |
| NFYFactorNoiseSourceLoss | 1,179,674 | Specifies an array of the ohmic losses inherent to the noise source used in the Y-Factor method. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the SetYFactorNoiseSourceLossCompensationEnabled(String, RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled) method to True. |
| NFYFactorNoiseSourceLossFrequency | 1,179,675 | Specifies the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the SetYFactorNoiseSourceLoss(String, Double) method. This value is expressed in Hz. |
| NFYFactorNoiseSourceLossTemperature | 1,179,676 | Specifies the physical temperature of the ohmic loss elements specified in the SetYFactorNoiseSourceLoss(String, Double) method. This value is expressed in kelvin. |
| NFCalibrationLossCompensationEnabled | 1,179,677 | Specifies whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the SetYFactorNoiseSourceLoss(String, Double) method. |
| NFCalibrationLoss | 1,179,678 | Specifies the array of ohmic losses between the noise source and input port of the analyzer during calibration, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the SetCalibrationLossCompensationEnabled(String, RFmxSpecAnMXNFCalibrationLossCompensationEnabled) method to True. You must exclude any loss specified by the SetYFactorNoiseSourceLoss(String, Double) method. This method specifies the frequencies at which the SetCalibrationLossFrequency(String, Double) method measures the losses. |
| NFCalibrationLossFrequency | 1,179,679 | Specifies an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. THis value is expressed in Hz. This method is applicable only when you set the SetYFactorMode(String, RFmxSpecAnMXNFYFactorMode) method to Calibrate and set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor, or when you set the SetColdSourceMode(String, RFmxSpecAnMXNFColdSourceMode) method to Calibrate and set the NF Meas Method method to ColdSource. |
| NFCalibrationLossTemperature | 1,179,680 | Specifies the physical temperature of the ohmic loss elements specified by the SetCalibrationLoss(String, Double) method. This value is expressed in kelvin. |
| NFNumberOfAnalysisThreads | 1,179,681 | Specifies the maximum number of threads used for parallelism for the noise figure (NF) measurement. |
| NFResultsDutNoiseFigure | 1,179,682 | Returns an array of the noise figures of the DUT measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. |
| NFResultsDutNoiseTemperature | 1,179,683 | Returns an array of the equivalent thermal noise temperatures of the DUT measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in kelvin. |
| NFResultsDutGain | 1,179,684 | Returns an array of the available gains of the DUT measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. |
| NFResultsAnalyzerNoiseFigure | 1,179,685 | Returns an array of the noise figures of the analyzer measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. |
| NFResultsMeasurementYFactor | 1,179,686 | Returns an array of the measurement Y-Factors measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFResultsCalibrationYFactor | 1,179,687 | Returns an array of the calibration Y-Factors measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dB. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFResultsYFactorHotPower | 1,179,688 | Returns the array of powers measured at the frequencies specified by the SetFrequencyList(String, Double) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFResultsYFactorColdPower | 1,179,689 | Returns the array of powers measured at the frequencies specified by the SetFrequencyList(String, Double) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFResultsColdSourcePower | 1,179,690 | Returns the power measured at the frequencies specified by the SetFrequencyList(String, Double) method. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to Cold-source. |
| NFColdSourceMode | 1,179,691 | Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method. |
| NFColdSourceInputTerminationVswr | 1,179,692 | Specifies an array of voltage standing wave ratios (VSWR) as a function of frequency of the microwave termination used as the noise source in cold source method. The corresponding array of frequencies is specified by the SetColdSourceInputTerminationVswrFrequency(String, Double) method. |
| NFColdSourceInputTerminationVswrFrequency | 1,179,693 | Specifies an array of frequencies corresponding to the voltage standing wave ratios (VSWR) of the microwave termination used in the cold source method as specified by the SetColdSourceInputTerminationVswr(String, Double) method. This value is expressed in Hz. |
| NFColdSourceInputTerminationTemperature | 1,179,694 | Specifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin. |
| NFColdSourceDutS21 | 1,179,695 | Specifies an array of the gains of the DUT as a function of freqency, when the output port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the SetColdSourceDutSParametersFrequency(String, Double) method. |
| NFColdSourceDutS12 | 1,179,696 | Specifies an array of the input-isolations of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the SetColdSourceDutSParametersFrequency(String, Double) method. |
| NFColdSourceDutS11 | 1,179,697 | Specifies an array of the input-reflections of the DUT as a function of frequency, when the output port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. |
| NFColdSourceDutS22 | 1,179,698 | Specifies an array of the output-reflections of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the SetColdSourceDutSParametersFrequency(String, Double) method. |
| NFColdSourceDutSParametersFrequency | 1,179,699 | Specifies an array of frequencies corresponding to the s-parameters of the DUT specified by the SetColdSourceDutS21(String, Double), SetColdSourceDutS12(String, Double), SetColdSourceDutS11(String, Double), and SetColdSourceDutS22(String, Double) properties. This value is expressed in Hz. |
| NFCalibrationSetupId | 1,179,700 | Specifies a unique string identifier with the hardware setup used to perform calibration for the NF measurement. |
| NFExternalPreampPresent | 1,179,701 | Specifies whether an external preamplifier is present in the signal path. |
| NFExternalPreampFrequency | 1,179,702 | Specifies the array of frequencies corresponding to the value of the SetExternalPreampGain(String, Double) method. |
| NFExternalPreampGain | 1,179,703 | Specifies the gain of the external preamplifier as a function of frequency. |
| NFDeviceTemperatureTolerance | 1,179,705 | Specifies the tolerance for device temperature beyond which the calibration data is considered invalid. This value is expressed in Celsius. |
| NFDutType | 1,179,706 | Specifies the type of DUT. |
| NFFrequencyConverterLOFrequency | 1,179,708 | Specifies the fixed LO frequency of the DUT when you set the SetDutType(String, RFmxSpecAnMXNFDutType) method to either Downconverter or Upconverter. This value is expressed in Hz. |
| NFFrequencyConverterFrequencyContext | 1,179,710 | Specifies the context of the NF Frequency List method. |
| NFFrequencyConverterSideband | 1,179,711 | Specifies the sideband when you set the SetDutType(String, RFmxSpecAnMXNFDutType) method to either Downconverter or Upconverter, and the SetFrequencyConverterFrequencyContext(String, RFmxSpecAnMXNFFrequencyConverterFrequencyContext) method to IF. |
| NFFrequencyConverterImageRejection | 1,179,712 | Specifies the gain ratio of the DUT at the image frequency to that at the RF frequency. This value is expressed in dB. Refer to NF concept help for more details. |
| NFYFactorNoiseSourceType | 1,179,713 | Specifies the noise source type for performing the noise figure (NF) measurement when you set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| NFYFactorNoiseSourceRFSignalGeneratorPort | 1,179,714 | Specifies the vector signal generator port to be configured to generate a noise signal when you set the SetYFactorNoiseSourceType(String, RFmxSpecAnMXNFYFactorNoiseSourceType) method to RFSignalGenerator. |
| PhaseNoiseMeasurementEnabled | 1,245,184 | Specifies whether to enable the phase noise measurement. |
| PhaseNoiseRangeDefinition | 1,245,186 | Specifies how the measurement computes offset subranges. |
| PhaseNoiseStartFrequency | 1,245,187 | Specifies the start offset frequency for the specified subrange when you set the PhaseNoise Range Definition method to Auto. |
| PhaseNoiseStopFrequency | 1,245,188 | Specifies the stop frequency of the offset frequency range when you set the PhaseNoise Range Definition method to Auto. |
| PhaseNoiseRbwPercentage | 1,245,189 | Specifies the RBW as a percentage of the start frequency of each subrange when you set the PhaseNoise Range Definition method to Auto. |
| PhaseNoiseAveragingMultiplier | 1,245,190 | Specifies the factor by which you increase the averaging count for each range. This setting applies to both Auto and Manual range definitions. |
| PhaseNoiseFftWindow | 1,245,191 | Specifies the FFT window to use. |
| PhaseNoiseNumberOfRanges | 1,245,192 | Specifies the number of manual ranges. |
| PhaseNoiseRangeStartFrequency | 1,245,193 | Specifies the start frequency for the specified subrange when you set the PhaseNoise Range Definition method to Manual. |
| PhaseNoiseRangeStopFrequency | 1,245,194 | Specifies the stop frequency of the offset frequency range when you set the PhaseNoise Range Definition method to Manual. |
| PhaseNoiseRangeRbwPercentage | 1,245,195 | Specifies the RBW as a percentage of the PhaseNoise Range Start Freq method of the specified subrange when you set the PhaseNoise Range Definition method to Manual. |
| PhaseNoiseRangeAveragingCount | 1,245,196 | Specifies the averaging count for the specified range. |
| PhaseNoiseSmoothingType | 1,245,197 | Specifies the smoothing type used to smoothen the log plot trace. |
| PhaseNoiseSmoothingPercentage | 1,245,198 | Specifies the number of trace points to use in the moving average filter as a percentage of total number of points in the log plot trace. |
| PhaseNoiseSpotNoiseFrequencyList | 1,245,199 | Specifies an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. |
| PhaseNoiseIntegratedNoiseRangeDefinition | 1,245,200 | Specifies the frequency range for integrated noise measurements. |
| PhaseNoiseIntegratedNoiseStartFrequency | 1,245,201 | Specifies an array of the start frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom. |
| PhaseNoiseIntegratedNoiseStopFrequency | 1,245,202 | Specifies an array of the stop frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom. |
| PhaseNoiseAllTracesEnabled | 1,245,203 | Specifies whether to enable the traces to be stored and retrieved after performing the Phase Noise measurement. |
| PhaseNoiseResultsCarrierPower | 1,245,205 | Returns the measured carrier power. |
| PhaseNoiseResultsCarrierFrequency | 1,245,206 | Returns the measured carrier frequency. |
| PhaseNoiseResultsSpotPhaseNoise | 1,245,207 | Returns the phase noise corresponding to the PhaseNoise Spot Noise Frequency List method by using the smoothed log plot trace. |
| PhaseNoiseResultsIntegratedPhaseNoise | 1,245,208 | Returns the integrated phase noise. |
| PhaseNoiseResultsResidualPMInRadian | 1,245,209 | Returns the residual PM in radians. |
| PhaseNoiseResultsResidualPMInDegree | 1,245,210 | Returns the residual PM in degrees. |
| PhaseNoiseResultsResidualFM | 1,245,211 | Returns the residual FM in Hz. |
| PhaseNoiseResultsJitter | 1,245,212 | Returns the jitter in seconds. |
| PhaseNoiseSpurRemovalEnabled | 1,245,213 | Specifies whether to remove spurs from the log plot trace. |
| PhaseNoiseSpurRemovalPeakExcursion | 1,245,214 | Specifies the peak excursion to be used when spur detection is performed. Refer to the Phase Noise topic for more information on spur removal |
| PhaseNoiseCancellationEnabled | 1,245,215 | Specifies whether to enable or disable the phase noise cancellation. Refer to the Phase Noise topic for more information on phase noise cancellation. |
| PhaseNoiseCancellationThreshold | 1,245,216 | Specifies the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed. |
| PhaseNoiseCancellationFrequency | 1,245,217 | Specifies an array of frequencies where the reference phase noise has been measured. |
| PhaseNoiseCancellationReferencePhaseNoise | 1,245,218 | Specifies an array of reference phase noise at the frequencies specified by the Phase Noise Cancellation Frequency method. |
| IdpdMeasurementEnabled | 1,310,720 | Specifies whether to enable IDPD measurement. |
| IdpdEqualizerMode | 1,310,722 | Specifies whether to enable equalization. |
| IdpdEqualizerFilterLength | 1,310,723 | Specifies the length of the equalizer filter to be trained. |
| IdpdMeasurementSampleRateMode | 1,310,724 | Specifies acquisition sample rate configuration mode. |
| IdpdMeasurementSampleRate | 1,310,725 | Specifies the acquisition sample rate, in S/s, when you set the SetMeasurementSampleRateMode(String, RFmxSpecAnMXIdpdMeasurementSampleRateMode) is User. |
| IdpdSignalType | 1,310,726 | Specifies the type of reference waveform. |
| IdpdReferenceWaveformIdleDurationPresent | 1,310,731 | Specifies whether the reference waveform contains idle duration or dead time. |
| IdpdDutAverageInputPower | 1,310,732 | Specifies the initial (first itertion) average power of the signal at the input port of the device under test. |
| IdpdAveragingEnabled | 1,310,735 | Specifies whether to enable averaging for the IDPD measurement. |
| IdpdAveragingCount | 1,310,736 | Specifies the number of acquisitions used for averaging when Averaging Enabled is TRUE. |
| IdpdEvmEnabled | 1,310,739 | Specifies whether to enable EVM computation. |
| IdpdEvmUnit | 1,310,740 | Specifies the units of the EVM results. |
| IdpdImpairmentEstimationStart | 1,310,741 | Specifies the start time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| IdpdImpairmentEstimationStop | 1,310,742 | Specifies the stop time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| IdpdSynchronizationEstimationStart | 1,310,743 | Specifies the start time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| IdpdSynchronizationEstimationStop | 1,310,744 | Specifies the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| IdpdGainExpansion | 1,310,745 | Specifies the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB. |
| IdpdPowerLinearityTradeoff | 1,310,747 | Specifies the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage. |
| IdpdResultsGain | 1,310,749 | Returns the gain of the device under test. This value is expressed in dB. |
| IdpdResultsMeanRmsEvm | 1,310,750 | Returns the ratio of L2 norm of difference between the normalized reference and acquired waveforms, to the L2 norm of the normalized reference waveform. This value is expressed either as a percentage or in dB depending on the configured SetEvmUnit(String, RFmxSpecAnMXIdpdEvmUnit), |
| IdpdAllTracesEnabled | 1,310,751 | Specifies whether to enable the traces to be stored and retrieved after performing the IDPD measurement. |
| IdpdNumberofAnalysisThreads | 1,310,753 | Specifies the maximum number of threads used for parallelism for the IDPD measurement. |
| IdpdTargetGain | 1,310,759 | Specifies the Target gain when the configured pre-distorted waveform is non-empty. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/12b1984f-235a-9830-4287-8f94f9225bc8.htm language=enus -->
## TOPIC 00037: rfmxspecandotnet/html/12b1984f-235a-9830-4287-8f94f9225bc8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/12b1984f-235a-9830-4287-8f94f9225bc8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/12b1984f-235a-9830-4287-8f94f9225bc8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.ConfigureThreshold Method

RFmxSpecAnMXFcntConfigurationConfigureThreshold Method

Configures the threshold level for the samples that need to be considered for the frequency count (Fcnt) measurement. Enable the threshold when analyzing burst signals or signals with dead time.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureThreshold(
	string selectorString,
	RFmxSpecAnMXFcntThresholdEnabled thresholdEnabled,
	double thresholdLevel,
	RFmxSpecAnMXFcntThresholdType thresholdType
)
```

```text
Public Function ConfigureThreshold ( 
	selectorString As String,
	thresholdEnabled As RFmxSpecAnMXFcntThresholdEnabled,
	thresholdLevel As Double,
	thresholdType As RFmxSpecAnMXFcntThresholdType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **thresholdEnabled RFmxSpecAnMXFcntThresholdEnabled**
  - Specifies whether to enable thresholding of the acquired samples to be used for the measurement.
- **thresholdLevel Double**
  - Specifies either the relative or absolute threshold power level based on the value of the SetThresholdEnabled(String, RFmxSpecAnMXFcntThresholdEnabled) method.
- **thresholdType RFmxSpecAnMXFcntThresholdType**
  - Specifies the reference for the power level used for thresholding.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntCfgThreshold() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/12bda071-2eab-93fa-d8fe-dfeaa3c045f2.htm language=enus -->
## TOPIC 00038: rfmxspecandotnet/html/12bda071-2eab-93fa-d8fe-dfeaa3c045f2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/12bda071-2eab-93fa-d8fe-dfeaa3c045f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/12bda071-2eab-93fa-d8fe-dfeaa3c045f2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetNumberOfAnalysisThreads Method

RFmxSpecAnMXChpConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for channel power (CHP) measurement.

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
  - Specifies the maximum number of threads used for parallelism for CHP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/12c4a761-3bff-d193-267c-8c84a0995dd6.htm language=enus -->
## TOPIC 00039: rfmxspecandotnet/html/12c4a761-3bff-d193-267c-8c84a0995dd6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/12c4a761-3bff-d193-267c-8c84a0995dd6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/12c4a761-3bff-d193-267c-8c84a0995dd6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetOffsetEnabled Method

RFmxSpecAnMXAcpConfigurationSetOffsetEnabled Method

Sets whether to enable the offset channel for adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetEnabled(
	string selectorString,
	RFmxSpecAnMXAcpOffsetEnabled value
)
```

```text
Public Function SetOffsetEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpOffsetEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXAcpOffsetEnabled**
  - Specifies whether to enable the offset channel for ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetOffsetEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/12f5a4bb-18de-e6c2-cb24-9f474f188da4.htm language=enus -->
## TOPIC 00040: rfmxspecandotnet/html/12f5a4bb-18de-e6c2-cb24-9f474f188da4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/12f5a4bb-18de-e6c2-cb24-9f474f188da4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/12f5a4bb-18de-e6c2-cb24-9f474f188da4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetFftPadding Method

RFmxSpecAnMXSemConfigurationGetFftPadding Method

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

This method maps to the RFmxSpecAn_SEMGetFFTPadding() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/137969f6-1b5a-a988-cba6-a0eb9dd16e5c.htm language=enus -->
## TOPIC 00041: rfmxspecandotnet/html/137969f6-1b5a-a988-cba6-a0eb9dd16e5c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/137969f6-1b5a-a988-cba6-a0eb9dd16e5c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/137969f6-1b5a-a988-cba6-a0eb9dd16e5c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMeasurementSampleRateMode Method

RFmxSpecAnMXDpdConfigurationSetMeasurementSampleRateMode Method

Sets the acquisition sample rate configuration mode.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementSampleRateMode(
	string selectorString,
	RFmxSpecAnMXDpdMeasurementSampleRateMode value
)
```

```text
Public Function SetMeasurementSampleRateMode ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdMeasurementSampleRateMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdMeasurementSampleRateMode**
  - Contains the acquisition sample rate configuration mode.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetMeasurementSampleRateMode() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/137e1238-b2e7-a994-edd7-3f88464a53af.htm language=enus -->
## TOPIC 00042: rfmxspecandotnet/html/137e1238-b2e7-a994-edd7-3f88464a53af.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/137e1238-b2e7-a994-edd7-3f88464a53af.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/137e1238-b2e7-a994-edd7-3f88464a53af.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd Methods

RFmxSpecAnMXDpdApplyDpd Methods

The [RFmxSpecAnMXDpdApplyDpd](709778f0-caa8-5b7c-ee33-401ecc5e15b4.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ApplyDigitalPredistortion | Scales the input waveform to DUT average input power and then predistorts using the DPD polynomial or the lookup table. To scale the waveform correctly, specify if the idle duration is present in the waveform. |
|  | ApplyDpd | Obsolete. Scales the input waveform to DUT Average Input Power and then predistorts the waveform using the DPD polynomial or the lookup table. |
|  | ConfigureConfigurationInput | Configures the source of measurement settings for applying DPD. |
|  | ConfigureHeadroom | Obsolete. Configures the headroom, in dB, for the predistorted waveform. |
|  | ConfigureLookupTableCorrectionType | Configures the predistortion type when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable. |
|  | ConfigureMemoryModelCorrectionType | Configures the predistortion type when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | ConfigureUserDpdPolynomial | Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | ConfigureUserLookupTable | Configures the predistortion lookup table when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to LookupTable. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchPreCfrPapr | Fetches the PAPR of the pre-distorted waveform before CFR is applied to it. |
|  | GetApplyDpdUserLookupTableType | Gets the DPD Lookup Table (LUT) type. |
|  | GetCfrEnabled | Gets whether to enable the crest factor reduction (CFR) on the pre-distorted waveform. |
|  | GetCfrMaximumIterations | Gets the maximum number of iterations to converge a waveform PAPR to target PAPR when you set the DpdApplyDpdCfrEnabled method to True. |
|  | GetCfrMethod | Gets the method used to perform the crest factor reduction (CFR) when you set the DpdApplyDpdCfrEnabled method to True. |
|  | GetCfrShapingFactor | Gets the shaping factor to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. Refer to DPD concept topic for more information about shaping factor. |
|  | GetCfrShapingThreshold | Gets the shaping threshold to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. |
|  | GetCfrTargetPapr | Gets the target PAPR when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrTargetPaprType method to Custom. This value is expressed in dB. |
|  | GetCfrTargetPaprType | Gets the target PAPR type when you set the DpdApplyDpdCfrEnabled method to True. |
|  | GetCfrWindowLength | Gets the maximum window length to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |
|  | GetCfrWindowType | Gets the window type to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |
|  | GetConfigurationInput | Gets whether to use the configuration used by the DPD measurement for applying DPD. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetHeadroom | Obsolete. Gets the headroom, in dB, to apply to the predistorted waveform. |
|  | GetHeadroomMode | Obsolete. Gets whether to compute and apply the headroom of the predistorted waveform or to apply the value that you specify using the SetHeadroom(String, Double) method on the predistorted waveform. |
|  | GetLookupTableCorrectionType | Gets the predistortion type. |
|  | GetMemoryModelCorrectionType | Gets the predistortion type when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetUserDpdModel | Gets the DPD model used to apply DPD. |
|  | GetUserDutAverageInputPower | Gets the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain. |
|  | GetUserLookupTableInputPower | Gets the input power array, in dBm, for the predistortion lookup table. |
|  | GetUserMeasurementSampleRate | Gets the acquisition sample rate, in hertz (Hz), used to compute the DPD User DPD Polynomial or DPD User LUT Complex Gain. |
|  | GetUserMemoryPolynomialLagMemoryDepth | Gets the lead memory depth cross term of the DPD polynomial. |
|  | GetUserMemoryPolynomialLagOrder | Gets the lag order cross term of the DPD polynomial. |
|  | GetUserMemoryPolynomialLeadMemoryDepth | Gets the lead memory depth cross term of the DPD polynomial. |
|  | GetUserMemoryPolynomialLeadOrder | Gets the lead order cross term of the DPD polynomial.. |
|  | GetUserMemoryPolynomialMaximumLag | Gets the maximum lag stagger cross term of the DPD polynomial. |
|  | GetUserMemoryPolynomialMaximumLead | Gets the maximum lead stagger cross term of the DPD polynomial. |
|  | GetUserMemoryPolynomialMemoryDepth | Gets the memory depth of the DPD polynomial. |
|  | GetUserMemoryPolynomialOrder | Gets the order of the DPD polynomial. |
|  | SetApplyDpdUserLookupTableType | Sets the DPD Lookup Table (LUT) type. |
|  | SetCfrEnabled | Sets whether to enable the crest factor reduction (CFR) on the pre-distorted waveform. |
|  | SetCfrMaximumIterations | Sets the maximum number of iterations to converge a waveform PAPR to target PAPR when you set the DpdApplyDpdCfrEnabled method to True. |
|  | SetCfrMethod | Sets the method used to perform the crest factor reduction (CFR) when you set the DpdApplyDpdCfrEnabled method to True. |
|  | SetCfrShapingFactor | Sets the shaping factor to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. Refer to DPD concept topic for more information about shaping factor. |
|  | SetCfrShapingThreshold | Sets the shaping threshold to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. |
|  | SetCfrTargetPapr | Sets the target PAPR when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrTargetPaprType method to Custom. This value is expressed in dB. |
|  | SetCfrTargetPaprType | Sets the target PAPR type when you set the DpdApplyDpdCfrEnabled method to True. |
|  | SetCfrWindowLength | Sets the maximum window length to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |
|  | SetCfrWindowType | Sets the window type to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |
|  | SetConfigurationInput | Sets whether to use the configuration used by the DPD measurement for applying DPD. |
|  | SetHeadroom | Obsolete. Sets the headroom, in dB, to apply to the predistorted waveform when you set the SetHeadroomMode(String, RFmxSpecAnMXDpdApplyDpdHeadroomMode) method to Manual. |
|  | SetHeadroomMode | Obsolete. Sets whether to compute and apply the headroom of the predistorted waveform, or to apply the value that you specify using the SetHeadroom(String, Double) method, on the predistorted waveform. |
|  | SetLookupTableCorrectionType | Sets the predistortion type when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to LookupTable. |
|  | SetMemoryModelCorrectionType | Sets the predistortion type when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
|  | SetUserDpdModel | Sets the DPD model used to apply DPD when you set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserDutAverageInputPower | Sets the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain when you set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserLookupTableInputPower | Sets the input power array, in dBm, for the predistortion lookup table when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to LookupTable. |
|  | SetUserMeasurementSampleRate | Gets the acquisition sample rate, in hertz (Hz), used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain when you set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserMemoryPolynomialLagMemoryDepth | Sets the lead memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set RFmxSpecAnMXDpdApplyDpdConfigurationInput to User. |
|  | SetUserMemoryPolynomialLagOrder | Sets the lag order cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserMemoryPolynomialLeadMemoryDepth | Sets the lead memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserMemoryPolynomialLeadOrder | Gets the lead order cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserMemoryPolynomialMaximumLag | Sets the maximum lag stagger cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserMemoryPolynomialMaximumLead | Sets the maximum lead stagger cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |
|  | SetUserMemoryPolynomialMemoryDepth | Sets the memory depth of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set RFmxSpecAnMXDpdApplyDpdConfigurationInput to User. |
|  | SetUserMemoryPolynomialOrder | Sets the order of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set RFmxSpecAnMXDpdApplyDpdConfigurationInput to User. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/13df57b6-c16c-05c0-7ab2-dcedb3310a05.htm language=enus -->
## TOPIC 00043: rfmxspecandotnet/html/13df57b6-c16c-05c0-7ab2-dcedb3310a05.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/13df57b6-c16c-05c0-7ab2-dcedb3310a05.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/13df57b6-c16c-05c0-7ab2-dcedb3310a05.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFFrequencyConverterSideband Enumeration

RFmxSpecAnMXNFFrequencyConverterSideband Enumeration

SetDutType(String, RFmxSpecAnMXNFDutType)

Downconverter

Upconverter

SetFrequencyConverterFrequencyContext(String, RFmxSpecAnMXNFFrequencyConverterFrequencyContext)

IF

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXNFFrequencyConverterSideband
```

```text
Public Enumeration RFmxSpecAnMXNFFrequencyConverterSideband
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Lsb | 0 | When the frequency context is IF, out of the two possible input frequencies that gets translated to IF, the lower is treated as the RF (signal) frequency while the higher is treated as the image frequency. |
| Usb | 1 | When the frequency context is IF, out of the two possible input frequencies that gets translated to IF, the lower is treated as the image frequency while the higher is treated as the RF (signal) frequency. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/13e73bf6-0bee-eb2e-7351-4c0e64576453.htm language=enus -->
## TOPIC 00044: rfmxspecandotnet/html/13e73bf6-0bee-eb2e-7351-4c0e64576453.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/13e73bf6-0bee-eb2e-7351-4c0e64576453.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/13e73bf6-0bee-eb2e-7351-4c0e64576453.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.SetVbwFilterAutoBandwidth Method

RFmxSpecAnMXTxpConfigurationSetVbwFilterAutoBandwidth Method

Sets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetVbwFilterAutoBandwidth(
	string selectorString,
	RFmxSpecAnMXTxpVbwFilterAutoBandwidth value
)
```

```text
Public Function SetVbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxSpecAnMXTxpVbwFilterAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXTxpVbwFilterAutoBandwidth**
  - Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

###### Return Value

Int32

##### Remarks

TxpVbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/143a0a24-e9d6-a00e-d200-6dc6d13d3212.htm language=enus -->
## TOPIC 00045: rfmxspecandotnet/html/143a0a24-e9d6-a00e-d200-6dc6d13d3212.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/143a0a24-e9d6-a00e-d200-6dc6d13d3212.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/143a0a24-e9d6-a00e-d200-6dc6d13d3212.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetCalibrationLoss Method

RFmxSpecAnMXNFConfigurationSetCalibrationLoss Method

SetCalibrationLossCompensationEnabled(String, RFmxSpecAnMXNFCalibrationLossCompensationEnabled)

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCalibrationLoss(
	string selectorString,
	double[] value
)
```

```text
Public Function SetCalibrationLoss ( 
	selectorString As String,
	value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the array of ohmic losses between the noise source and input port of the analyzer during calibration, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the SetCalibrationLossCompensationEnabled(String, RFmxSpecAnMXNFCalibrationLossCompensationEnabled) method to True. You must exclude any loss specified by the SetYFactorNoiseSourceLoss(String, Double) method. This method specifies the frequencies at which the SetCalibrationLossFrequency(String, Double) method measures the losses.

###### Return Value

Int32

##### Remarks

NFCalibrationLoss

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/145fd8bf-e437-5260-e2eb-20da9d208b08.htm language=enus -->
## TOPIC 00046: rfmxspecandotnet/html/145fd8bf-e437-5260-e2eb-20da9d208b08.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/145fd8bf-e437-5260-e2eb-20da9d208b08.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/145fd8bf-e437-5260-e2eb-20da9d208b08.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.GetRbwFilterBandwidth Method

RFmxSpecAnMXCcdfConfigurationGetRbwFilterBandwidth Method

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

This method maps to the RFmxSpecAn_CCDFGetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1479a4f6-c419-e4d1-6bfe-a459664fb6ed.htm language=enus -->
## TOPIC 00047: rfmxspecandotnet/html/1479a4f6-c419-e4d1-6bfe-a459664fb6ed.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1479a4f6-c419-e4d1-6bfe-a459664fb6ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1479a4f6-c419-e4d1-6bfe-a459664fb6ed.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetOffsetFrequency Method

RFmxSpecAnMXAcpConfigurationSetOffsetFrequency Method

SetOffsetFrequencyDefinition(String, RFmxSpecAnMXAcpOffsetFrequencyDefinition)

SetOffsetSideband(String, RFmxSpecAnMXAcpOffsetSideband)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the center or edge frequency, in hertz (Hz), of the offset channel, relative to the center frequency of the closest carrier as determined by the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXAcpOffsetFrequencyDefinition) method. The sign of offset frequency is ignored and the SetOffsetSideband(String, RFmxSpecAnMXAcpOffsetSideband) method determines whether the upper, lower, or both offsets are measured.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetOffsetFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/148c0e87-180b-9205-6d78-972e110b4f9e.htm language=enus -->
## TOPIC 00048: rfmxspecandotnet/html/148c0e87-180b-9205-6d78-972e110b4f9e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/148c0e87-180b-9205-6d78-972e110b4f9e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/148c0e87-180b-9205-6d78-972e110b4f9e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetNumberOfAnalysisThreads Method

RFmxSpecAnMXAmpmConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for AMPM measurement.

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
  - Upon return, contains the maximum number of threads used for parallelism in the AMPM measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetNumberOfAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/14c8d43e-fae0-3216-951d-7ff315be0e6a.htm language=enus -->
## TOPIC 00049: rfmxspecandotnet/html/14c8d43e-fae0-3216-951d-7ff315be0e6a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/14c8d43e-fae0-3216-951d-7ff315be0e6a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/14c8d43e-fae0-3216-951d-7ff315be0e6a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.SetRbwFilterRrcAlpha Method

RFmxSpecAnMXCcdfConfigurationSetRbwFilterRrcAlpha Method

Sets the roll-off factor for the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterRrcAlpha(
	string selectorString,
	double value
)
```

```text
Public Function SetRbwFilterRrcAlpha ( 
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

This method maps to the RFmxSpecAn_CCDFSetRBWFilterRRCAlpha() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/14cb5008-15d5-f90d-bfdd-3e10dabb3564.htm language=enus -->
## TOPIC 00050: rfmxspecandotnet/html/14cb5008-15d5-f90d-bfdd-3e10dabb3564.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/14cb5008-15d5-f90d-bfdd-3e10dabb3564.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/14cb5008-15d5-f90d-bfdd-3e10dabb3564.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SetTriggerMinimumQuietTimeMode Method

RFmxSpecAnMXSetTriggerMinimumQuietTimeMode Method

Sets whether the measurement computes the minimum quiet time used for triggering.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerMinimumQuietTimeMode(
	string selectorString,
	RFmxSpecAnMXTriggerMinimumQuietTimeMode value
)
```

```text
Public Function SetTriggerMinimumQuietTimeMode ( 
	selectorString As String,
	value As RFmxSpecAnMXTriggerMinimumQuietTimeMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXTriggerMinimumQuietTimeMode**
  - Specifies whether the measurement computes the minimum quiet time used for triggering.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SetTriggerMinimumQuietTimeMode() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/14d31bae-096c-6bc0-8137-e1d70186f5cd.htm language=enus -->
## TOPIC 00051: rfmxspecandotnet/html/14d31bae-096c-6bc0-8137-e1d70186f5cd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/14d31bae-096c-6bc0-8137-e1d70186f5cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/14d31bae-096c-6bc0-8137-e1d70186f5cd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.GetMeasurementEnabled Method

RFmxSpecAnMXFcntConfigurationGetMeasurementEnabled Method

Gets whether to enable the frequency count (Fcnt) measurement.

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
  - if Fcnt measurement is enabled; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntGetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/14f59ff6-ef68-dd8f-5360-0153ab2630b1.htm language=enus -->
## TOPIC 00052: rfmxspecandotnet/html/14f59ff6-ef68-dd8f-5360-0153ab2630b1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/14f59ff6-ef68-dd8f-5360-0153ab2630b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/14f59ff6-ef68-dd8f-5360-0153ab2630b1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetIntegratedNoiseStopFrequency Method

RFmxSpecAnMXPhaseNoiseConfigurationGetIntegratedNoiseStopFrequency Method

Gets an array of the stop frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIntegratedNoiseStopFrequency(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetIntegratedNoiseStopFrequency ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains an array of the stop frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom.

###### Return Value

Int32

##### Remarks

PhaseNoiseIntegratedNoiseStopFrequency

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/14fb98fb-7912-d6c4-6c13-c4a5ee5d8f1b.htm language=enus -->
## TOPIC 00053: rfmxspecandotnet/html/14fb98fb-7912-d6c4-6c13-c4a5ee5d8f1b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/14fb98fb-7912-d6c4-6c13-c4a5ee5d8f1b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/14fb98fb-7912-d6c4-6c13-c4a5ee5d8f1b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetFrequencyOffsetCorrectionEnabled Method

RFmxSpecAnMXAmpmConfigurationSetFrequencyOffsetCorrectionEnabled Method

Sets the frequency offset correction for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFrequencyOffsetCorrectionEnabled(
	string selectorString,
	RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled value
)
```

```text
Public Function SetFrequencyOffsetCorrectionEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled**
  - Spcifies whether to enable frequency offset correction for the measurement.

###### Return Value

Int32

##### Remarks

AmpmFrequencyOffsetCorrectionEnabled

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15031477-d5a0-0dcf-990b-20d5ae0bb7b6.htm language=enus -->
## TOPIC 00054: rfmxspecandotnet/html/15031477-d5a0-0dcf-990b-20d5ae0bb7b6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15031477-d5a0-0dcf-990b-20d5ae0bb7b6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15031477-d5a0-0dcf-990b-20d5ae0bb7b6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemPowerUnits Enumeration

RFmxSpecAnMXSemPowerUnits Enumeration

Specifies the units for the absolute power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemPowerUnits
```

```text
Public Enumeration RFmxSpecAnMXSemPowerUnits
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| dBm | 0 | The absolute powers are reported in dBm. |
| dBmPerHertz | 1 | The absolute powers are reported in dBm/Hz. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15186e01-b810-59bd-f4da-2fc6edd63061.htm language=enus -->
## TOPIC 00055: rfmxspecandotnet/html/15186e01-b810-59bd-f4da-2fc6edd63061.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15186e01-b810-59bd-f4da-2fc6edd63061.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15186e01-b810-59bd-f4da-2fc6edd63061.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeSweepTimeInterval Method

RFmxSpecAnMXSpurConfigurationSetRangeSweepTimeInterval Method

SetRangeSweepTimeAuto(String, RFmxSpecAnMXSpurSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeSweepTimeInterval(
	string selectorString,
	double value
)
```

```text
Public Function SetRangeSweepTimeInterval ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the sweep time, in seconds, when you set the SetRangeSweepTimeAuto(String, RFmxSpecAnMXSpurSweepTimeAuto) method to False.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeSweepTimeInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/151f6655-9999-21ef-5998-efca8d44f78c.htm language=enus -->
## TOPIC 00056: rfmxspecandotnet/html/151f6655-9999-21ef-5998-efca8d44f78c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/151f6655-9999-21ef-5998-efca8d44f78c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/151f6655-9999-21ef-5998-efca8d44f78c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetCfrTargetPaprType Method

RFmxSpecAnMXDpdApplyDpdSetCfrTargetPaprType Method

DpdApplyDpdCfrEnabled

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCfrTargetPaprType(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType value
)
```

```text
Public Function SetCfrTargetPaprType ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType**
  - Specifies the target PAPR type when you set the DpdApplyDpdCfrEnabled method to True.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrTargetPaprType

InputPapr

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/155f2054-d51f-ffb3-4a01-10d3601211b6.htm language=enus -->
## TOPIC 00057: rfmxspecandotnet/html/155f2054-d51f-ffb3-4a01-10d3601211b6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/155f2054-d51f-ffb3-4a01-10d3601211b6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/155f2054-d51f-ffb3-4a01-10d3601211b6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpd Class

RFmxSpecAnMXDpd Class

Represents a DPD measurement.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXDpd : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXDpd
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXDpd type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ApplyDpd | Gets the RFmxSpecAnMXDpdApplyDpd instance that provides methods to apply DPD measurements. |
|  | Configuration | Gets the RFmxSpecAnMXDpdConfiguration instance that allows configuration of DPD measurement. |
|  | PreDpd | Gets the RFmxSpecAnMXDpdPreDpd instance that provides methods to apply DPD measurements. |
|  | Results | Gets the RFmxSpecAnMXDpdResults instance that provides methods to retrieve the DPD measurement results. |

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15860836-42fe-a1c6-430e-38456f1ec66e.htm language=enus -->
## TOPIC 00058: rfmxspecandotnet/html/15860836-42fe-a1c6-430e-38456f1ec66e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15860836-42fe-a1c6-430e-38456f1ec66e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15860836-42fe-a1c6-430e-38456f1ec66e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.GetSampleRate Method

RFmxSpecAnMXIQConfigurationGetSampleRate Method

Gets the acquisition sample rate, in samples per second (S/s).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSampleRate(
	string selectorString,
	out double value
)
```

```text
Public Function GetSampleRate ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the acquisition sample rate, in S/s.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQGetSampleRate() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15ab886e-f11d-1cc9-f908-f7c71afc2022.htm language=enus -->
## TOPIC 00059: rfmxspecandotnet/html/15ab886e-f11d-1cc9-f908-f7c71afc2022.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15ab886e-f11d-1cc9-f908-f7c71afc2022.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15ab886e-f11d-1cc9-f908-f7c71afc2022.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpFftWindow Enumeration

RFmxSpecAnMXChpFftWindow Enumeration

Specifies the FFT window type used to reduce spectral leakage.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpFftWindow
```

```text
Public Enumeration RFmxSpecAnMXChpFftWindow
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
| BlackmanHarris | 6 | Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. |
| KaiserBessel | 7 | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15c42218-4caf-946f-ba6a-253e9b335589.htm language=enus -->
## TOPIC 00060: rfmxspecandotnet/html/15c42218-4caf-946f-ba6a-253e9b335589.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15c42218-4caf-946f-ba6a-253e9b335589.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15c42218-4caf-946f-ba6a-253e9b335589.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.FetchOffsetMeasurementArray Method

RFmxSpecAnMXAcpResultsFetchOffsetMeasurementArray Method

SetCarrierMode(String, RFmxSpecAnMXAcpCarrierMode)

Passive

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchOffsetMeasurementArray(
	string selectorString,
	double timeout,
	ref double[] lowerRelativePower,
	ref double[] upperRelativePower,
	ref double[] lowerAbsolutePower,
	ref double[] upperAbsolutePower
)
```

```text
Public Function FetchOffsetMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef lowerRelativePower As Double(),
	ByRef upperRelativePower As Double(),
	ByRef lowerAbsolutePower As Double(),
	ByRef upperAbsolutePower As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete.
- **lowerRelativePower Double**
  - Upon return, contains the array of lower offset channel powers, in dB, measured relative to the integrated power of the ACP Results Lower Offset Pwr Ref Carrier.
- **upperRelativePower Double**
  - Upon return, contains the array of upper offset channel powers, in dB, measured relative to the integrated power of the ACP Results Upper Offset Pwr Ref Carrier.
- **lowerAbsolutePower Double**
  - Upon return, contains the array of lower offset channel powers.
- **upperAbsolutePower Double**
  - Upon return, contains the array of upper offset channel powers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPFetchOffsetMeasurementArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15dbbfec-c80b-906e-e813-0183cae786ea.htm language=enus -->
## TOPIC 00061: rfmxspecandotnet/html/15dbbfec-c80b-906e-e813-0183cae786ea.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15dbbfec-c80b-906e-e813-0183cae786ea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15dbbfec-c80b-906e-e813-0183cae786ea.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.ConfigureLookupTableAMToAMCurveFit Method

RFmxSpecAnMXDpdConfigurationConfigureLookupTableAMToAMCurveFit Method

SetModel(String, RFmxSpecAnMXDpdModel)

LookupTable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureLookupTableAMToAMCurveFit(
	string selectorString,
	int amToAMCurveFitOrder,
	RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType amToAMCurveFitType
)
```

```text
Public Function ConfigureLookupTableAMToAMCurveFit ( 
	selectorString As String,
	amToAMCurveFitOrder As Integer,
	amToAMCurveFitType As RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **amToAMCurveFitOrder Int32**
  - Specifies the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test when you set RFmxSpecAnMXDpdModel to LookupTable.
- **amToAMCurveFitType RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType**
  - Specifies the cost-function for polynomial approximation of the AM-to-AM characteristic of the device under test when you set RFmxSpecAnMXDpdModel to LookupTable.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgLookupTableAMToAMCurveFit() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15dc6159-0b57-a1a1-870c-59e770ab5780.htm language=enus -->
## TOPIC 00062: rfmxspecandotnet/html/15dc6159-0b57-a1a1-870c-59e770ab5780.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15dc6159-0b57-a1a1-870c-59e770ab5780.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15dc6159-0b57-a1a1-870c-59e770ab5780.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcnt Methods

RFmxSpecAnMXFcnt Methods

The [RFmxSpecAnMXFcnt](d68d4936-2223-ddae-8786-86d298098e9a.htm) type exposes the following members.

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

RFmxSpecAnMXFcnt Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/15dde3ce-17a1-7d28-f33a-708ed1b06685.htm language=enus -->
## TOPIC 00063: rfmxspecandotnet/html/15dde3ce-17a1-7d28-f33a-708ed1b06685.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/15dde3ce-17a1-7d28-f33a-708ed1b06685.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/15dde3ce-17a1-7d28-f33a-708ed1b06685.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetFftWindow Method

RFmxSpecAnMXChpConfigurationGetFftWindow Method

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
	out RFmxSpecAnMXChpFftWindow value
)
```

```text
Public Function GetFftWindow ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpFftWindow
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpFftWindow**
  - Upon return, contains the FFT window type used to reduce spectral leakage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPGetFFTWindow() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/16047825-a0b3-f03f-412c-f6447391df0c.htm language=enus -->
## TOPIC 00064: rfmxspecandotnet/html/16047825-a0b3-f03f-412c-f6447391df0c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/16047825-a0b3-f03f-412c-f6447391df0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/16047825-a0b3-f03f-412c-f6447391df0c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumResults Class

RFmxSpecAnMXSpectrumResults Class

Provides methods to fetch and read the Spectrum measurement results.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXSpectrumResults : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXSpectrumResults
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXSpectrumResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchMeasurement | Fetches the peak amplitude and frequency at which the peak occurred in the spectrum. |
|  | FetchPowerTrace | Fetches the power trace for the Spectrum measurement. |
|  | FetchSpectrum | Fetches the spectrum used for the Spectrum measurement. |
|  | GetFrequencyResolution | Gets the frequency resolution, in hertz (Hz), of the spectrum acquired by the measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetPeakAmplitude | Gets the peak amplitude, in dBm, of the averaged spectrum. |
|  | GetPeakFrequency | Gets the frequency, in hertz (Hz), at the peak amplitude of the averaged spectrum. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | Read | Gets the hardware for acquisition, performs measurement on acquired data, and returns Spectrum measurement results. |
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/160cbc96-1f0f-81b3-8d56-f5ec11b475cb.htm language=enus -->
## TOPIC 00065: rfmxspecandotnet/html/160cbc96-1f0f-81b3-8d56-f5ec11b475cb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/160cbc96-1f0f-81b3-8d56-f5ec11b475cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/160cbc96-1f0f-81b3-8d56-f5ec11b475cb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetTraceRangeIndex Method

RFmxSpecAnMXSpurConfigurationSetTraceRangeIndex Method

Sets the index of the range used to store and retrieve spurious emission (Spur) traces. This method is not used if you set the spur all traces enabled to FALSE. When you set this method to -1, the measurement stores and retrieves traces for all enabled ranges.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTraceRangeIndex(
	string selectorString,
	int value
)
```

```text
Public Function SetTraceRangeIndex ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the index of the range used to store and retrieve Spur traces. This method is not used if you set the spur all traces enabled to FALSE. When you set this method to -1, the measurement stores and retrieves traces for all enabled ranges.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetTraceRangeIndex() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1634541f-2139-b3bd-4362-3961b1e32efc.htm language=enus -->
## TOPIC 00066: rfmxspecandotnet/html/1634541f-2139-b3bd-4362-3961b1e32efc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1634541f-2139-b3bd-4362-3961b1e32efc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1634541f-2139-b3bd-4362-3961b1e32efc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.SetRbwFilterBandwidth Method

RFmxSpecAnMXTxpConfigurationSetRbwFilterBandwidth Method

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

This method maps to the RFmxSpecAn_TXPSetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/164460be-42f5-7f1b-3e75-c7691eb10736.htm language=enus -->
## TOPIC 00067: rfmxspecandotnet/html/164460be-42f5-7f1b-3e75-c7691eb10736.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/164460be-42f5-7f1b-3e75-c7691eb10736.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/164460be-42f5-7f1b-3e75-c7691eb10736.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.FetchRangeSpectrumTrace Method

RFmxSpecAnMXSpurResultsFetchRangeSpectrumTrace Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRangeSpectrumTrace(
	string selectorString,
	double timeout,
	ref Spectrum<float> rangeSpectrum
)
```

```text
Public Function FetchRangeSpectrumTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef rangeSpectrum As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and range number. Example: "range0", "result::r1/range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **timeout Double**
  - specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **rangeSpectrum SpectrumSingle**
  - Specifies the spectrum of the range.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurFetchRangeSpectrumTrace() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/164d86b6-4f62-6833-423e-8170fc5e3724.htm language=enus -->
## TOPIC 00068: rfmxspecandotnet/html/164d86b6-4f62-6833-423e-8170fc5e3724.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/164d86b6-4f62-6833-423e-8170fc5e3724.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/164d86b6-4f62-6833-423e-8170fc5e3724.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetCarrierEnabled Method

RFmxSpecAnMXSemConfigurationSetCarrierEnabled Method

Sets whether to consider the carrier power as part of total carrier power measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCarrierEnabled(
	string selectorString,
	RFmxSpecAnMXSemCarrierEnabled value
)
```

```text
Public Function SetCarrierEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXSemCarrierEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemCarrierEnabled**
  - Specifies whether to consider the carrier power as part of total carrier power measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetCarrierEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/167bbfc5-ef0e-8230-c6ed-250b726e68c9.htm language=enus -->
## TOPIC 00069: rfmxspecandotnet/html/167bbfc5-ef0e-8230-c6ed-250b726e68c9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/167bbfc5-ef0e-8230-c6ed-250b726e68c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/167bbfc5-ef0e-8230-c6ed-250b726e68c9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetCfrWindowType Method

RFmxSpecAnMXDpdApplyDpdGetCfrWindowType Method

DpdApplyDpdCfrEnabled

True

DpdApplyDpdCfrMethod

PeakWindowing

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCfrWindowType(
	string selectorString,
	out RFmxSpecAnMXDpdApplyDpdCfrWindowType value
)
```

```text
Public Function GetCfrWindowType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdApplyDpdCfrWindowType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdCfrWindowType**
  - Upon return, contains the window type to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrWindowType

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/16c55153-bbc2-ec87-d1e5-86e84170de00.htm language=enus -->
## TOPIC 00070: rfmxspecandotnet/html/16c55153-bbc2-ec87-d1e5-86e84170de00.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/16c55153-bbc2-ec87-d1e5-86e84170de00.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/16c55153-bbc2-ec87-d1e5-86e84170de00.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.GetPretriggerTime Method

RFmxSpecAnMXIQConfigurationGetPretriggerTime Method

Gets the pretrigger time, in seconds, for the I/Q measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPretriggerTime(
	string selectorString,
	out double value
)
```

```text
Public Function GetPretriggerTime ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the pretrigger time, in seconds, for the I/Q measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQGetPretriggerTime() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1729859a-ef67-48b9-d069-f9baf8087310.htm language=enus -->
## TOPIC 00071: rfmxspecandotnet/html/1729859a-ef67-48b9-d069-f9baf8087310.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1729859a-ef67-48b9-d069-f9baf8087310.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1729859a-ef67-48b9-d069-f9baf8087310.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmSynchronizationMethod Enumeration

RFmxSpecAnMXAmpmSynchronizationMethod Enumeration

Specifies the method used for synchronization of acquired waveform with reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAmpmSynchronizationMethod
```

```text
Public Enumeration RFmxSpecAnMXAmpmSynchronizationMethod
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Direct | 1 | Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when the measurement sampling rate is high. |
| AliasProtected | 2 | Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when the measurement sampling rate is low. Refer to AMPM concept help for more information. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1734bb8a-fa15-4aeb-6c17-8a113a5bc03f.htm language=enus -->
## TOPIC 00072: rfmxspecandotnet/html/1734bb8a-fa15-4aeb-6c17-8a113a5bc03f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1734bb8a-fa15-4aeb-6c17-8a113a5bc03f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1734bb8a-fa15-4aeb-6c17-8a113a5bc03f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpm Properties

RFmxSpecAnMXAmpm Properties

The [RFmxSpecAnMXAmpm](194e942d-3c77-43a1-c589-34b5ca02da20.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXAmpmConfiguration instance that allows configuration of AMPM measurement. |
|  | Results | Gets the RFmxSpecAnMXAmpmResults instance that provides methods to retrieve AMPM measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXAmpm Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/173997cb-a6b4-df7b-8cbb-a40672af17db.htm language=enus -->
## TOPIC 00073: rfmxspecandotnet/html/173997cb-a6b4-df7b-8cbb-a40672af17db.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/173997cb-a6b4-df7b-8cbb-a40672af17db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/173997cb-a6b4-df7b-8cbb-a40672af17db.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpMeasurementMethod Enumeration

RFmxSpecAnMXAcpMeasurementMethod Enumeration

Specifies the method for performing the adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpMeasurementMethod
```

```text
Public Enumeration RFmxSpecAnMXAcpMeasurementMethod
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this value when measurement speed is desirable over higher dynamic range. |
| DynamicRange | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Supported Devices: PXIe-5665, PXIe-5668 |
| SequentialFft | 2 | The ACP measurement acquires I/Q samples specified for a duration by the ACP Sweep Time method. These samples are divided into smaller chunks. The size of each chunk is defined by the SetSequentialFftSize(String, Int32) method. The overlap between the chunks is defined by the ACP FFT Overlap Mode method. FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. Sequential FFT method should be used for the following scenarios. While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following methods have limited support when you set the RFmxSpecAnMXAcpConfiguration.ConfigureMeasurementMethod method to SequentialFft.The RFmxSpecAnMXAcpConfiguration.SetRbwFilterAutoBandwidth method will only support True value. The RFmxSpecAnMXAcpConfiguration.SetRbwFilterType method will only support FftBased value. The RFmxSpecAnMXAcpConfiguration.SetSweepTimeAuto method will only support False value. The RFmxSpecAnMXAcpConfiguration.SetAveragingCount method will only support a value greater than or equal to 1. The RFmxSpecAnMXAcpConfiguration.SetNumberOfAnalysisThreads method will only support a value of 1. The RFmxSpecAnMXAcpConfiguration.SetAmplitudeCorrectionType Method will only support a value of RFCenterFrequency. The RFmxSpecAnMXAcpConfiguration.SetOffsetRelativeAttenuation Method will only support 0. Note For multi-span FFT, the averaging count should be 1. |
| Note |  |  |
| For multi-span FFT, the averaging count should be 1. |  |  |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1744ba6c-5c52-4b4d-d40d-b7563e5c7a5a.htm language=enus -->
## TOPIC 00074: rfmxspecandotnet/html/1744ba6c-5c52-4b4d-d40d-b7563e5c7a5a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1744ba6c-5c52-4b4d-d40d-b7563e5c7a5a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1744ba6c-5c52-4b4d-d40d-b7563e5c7a5a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SignalConfigurationType Property

RFmxSpecAnMXSignalConfigurationType Property

Type

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1b19eb08-b053-21af-4ed7-d6ed5f98109b.htm language=enus -->
## TOPIC 00075: rfmxspecandotnet/html/1b19eb08-b053-21af-4ed7-d6ed5f98109b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1b19eb08-b053-21af-4ed7-d6ed5f98109b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1b19eb08-b053-21af-4ed7-d6ed5f98109b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeDetectorPoints Method

RFmxSpecAnMXSpurConfigurationSetRangeDetectorPoints Method

Sets the number of range points after the detector is applied. Use "range(n)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeDetectorPoints(
	string selectorString,
	int value
)
```

```text
Public Function SetRangeDetectorPoints ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the spurrange number. Example: "spurrange0". You can use the BuildRangeString(String, Int32) method to build the selector string.
- **value Int32**
  - Specifies the number of range points after the detector is applied. Use "range(n)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

SpurRangeDetectorPoints

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1b499e5c-964a-f6b2-73cb-a01f016f8af8.htm language=enus -->
## TOPIC 00076: rfmxspecandotnet/html/1b499e5c-964a-f6b2-73cb-a01f016f8af8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1b499e5c-964a-f6b2-73cb-a01f016f8af8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1b499e5c-964a-f6b2-73cb-a01f016f8af8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetRbwFilterType Method

RFmxSpecAnMXObwConfigurationSetRbwFilterType Method

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
	RFmxSpecAnMXObwRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxSpecAnMXObwRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetRBWFilterType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1be57f11-c262-5940-cea8-4b9f488ac6f8.htm language=enus -->
## TOPIC 00077: rfmxspecandotnet/html/1be57f11-c262-5940-cea8-4b9f488ac6f8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1be57f11-c262-5940-cea8-4b9f488ac6f8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1be57f11-c262-5940-cea8-4b9f488ac6f8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdResults.FetchEqualizerCoefficients Method

RFmxSpecAnMXIdpdResultsFetchEqualizerCoefficients Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchEqualizerCoefficients(
	string selectorString,
	double timeout,
	ref ComplexWaveform<ComplexSingle> equalizerCoefficients
)
```

```text
Public Function FetchEqualizerCoefficients ( 
	selectorString As String,
	timeout As Double,
	ByRef equalizerCoefficients As ComplexWaveform(Of ComplexSingle)
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **equalizerCoefficients ComplexWaveformComplexSingle**
  - Upon return, contains the equalizer coefficients.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIdpdResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1c2c1a9d-1ad6-ef22-f467-d4baf7fbeefc.htm language=enus -->
## TOPIC 00078: rfmxspecandotnet/html/1c2c1a9d-1ad6-ef22-f467-d4baf7fbeefc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1c2c1a9d-1ad6-ef22-f467-d4baf7fbeefc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1c2c1a9d-1ad6-ef22-f467-d4baf7fbeefc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpm.Configuration Property

RFmxSpecAnMXAmpmConfiguration Property

RFmxSpecAnMXAmpmConfiguration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXAmpmConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxSpecAnMXAmpmConfiguration
	Get
```

###### Property Value

RFmxSpecAnMXAmpmConfiguration

##### See Also

###### Reference

RFmxSpecAnMXAmpm Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1cb75432-d2f2-2bc7-cbd0-ac5534588d4b.htm language=enus -->
## TOPIC 00079: rfmxspecandotnet/html/1cb75432-d2f2-2bc7-cbd0-ac5534588d4b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1cb75432-d2f2-2bc7-cbd0-ac5534588d4b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1cb75432-d2f2-2bc7-cbd0-ac5534588d4b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.FetchAllSpurs Method

RFmxSpecAnMXSpurResultsFetchAllSpurs Method

Fetches all the spurs across all ranges.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAllSpurs(
	string selectorString,
	double timeout,
	ref double[] spurFrequency,
	ref double[] spurAmplitude,
	ref double[] spurMargin,
	ref double[] spurAbsoluteLimit,
	ref int[] spurRangeIndex
)
```

```text
Public Function FetchAllSpurs ( 
	selectorString As String,
	timeout As Double,
	ByRef spurFrequency As Double(),
	ByRef spurAmplitude As Double(),
	ByRef spurMargin As Double(),
	ByRef spurAbsoluteLimit As Double(),
	ByRef spurRangeIndex As Integer()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the signal name and result name. Example: "signal::sig1", "result::r1" "signal::sig1/result::r1". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **spurFrequency Double**
  - Upon return, contains the array of frequencies, in hertz (Hz), of all detected spurs across all ranges.
- **spurAmplitude Double**
  - Upon return, contains the array of powers, in dBm, of all detected spurs across all ranges.
- **spurMargin Double**
  - Upon return, contains the array of differences between the spur amplitude and the absolute limit at the spur frequency.
- **spurAbsoluteLimit Double**
  - Upon return, contains the array of thresholds, in dBm, used to calculate the margin of the detected spurs.
- **spurRangeIndex Int32**
  - Upon return, contains the array containing range indices corresponding to the detected spurs.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurFetchAllSpurs() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1dd08092-e3ad-6f76-f62f-32c621a63b5b.htm language=enus -->
## TOPIC 00080: rfmxspecandotnet/html/1dd08092-e3ad-6f76-f62f-32c621a63b5b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1dd08092-e3ad-6f76-f62f-32c621a63b5b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1dd08092-e3ad-6f76-f62f-32c621a63b5b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.GetPhaseErrorRange Method

RFmxSpecAnMXAmpmResultsGetPhaseErrorRange Method

Gets the peak-to-peak deviation, in degrees, in the phase distortion of the acquired signal relative to the reference waveform caused by the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhaseErrorRange(
	string selectorString,
	out double value
)
```

```text
Public Function GetPhaseErrorRange ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the peak-to-peak deviation, in degrees, in the phase distortion of the acquired signal relative to the reference waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetResultsPhaseErrorRange() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1dde40b3-41bf-13f7-6ef1-597363f0066c.htm language=enus -->
## TOPIC 00081: rfmxspecandotnet/html/1dde40b3-41bf-13f7-6ef1-597363f0066c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1dde40b3-41bf-13f7-6ef1-597363f0066c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1dde40b3-41bf-13f7-6ef1-597363f0066c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurFftWindow Enumeration

RFmxSpecAnMXSpurFftWindow Enumeration

Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpurFftWindow
```

```text
Public Enumeration RFmxSpecAnMXSpurFftWindow
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1de1ab57-72e1-b03b-72c7-b079ea1b77de.htm language=enus -->
## TOPIC 00082: rfmxspecandotnet/html/1de1ab57-72e1-b03b-72c7-b079ea1b77de.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1de1ab57-72e1-b03b-72c7-b079ea1b77de.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1de1ab57-72e1-b03b-72c7-b079ea1b77de.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMemoryPolynomialMaximumLag Method

RFmxSpecAnMXDpdConfigurationGetMemoryPolynomialMaximumLag Method

Gets the maximum lag stagger cross term of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMemoryPolynomialMaximumLag(
	string selectorString,
	out int value
)
```

```text
Public Function GetMemoryPolynomialMaximumLag ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the maximum lag stagger cross term of the DPD polynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetMemoryPolynomialMaximumLag() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1defd334-ad91-6618-9646-09d15a3d9e92.htm language=enus -->
## TOPIC 00083: rfmxspecandotnet/html/1defd334-ad91-6618-9646-09d15a3d9e92.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1defd334-ad91-6618-9646-09d15a3d9e92.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1defd334-ad91-6618-9646-09d15a3d9e92.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurRangeStatus Enumeration

RFmxSpecAnMXSpurRangeStatus Enumeration

Indicates the measurement status for the frequency range.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpurRangeStatus
```

```text
Public Enumeration RFmxSpecAnMXSpurRangeStatus
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Fail | 0 | Indicates that a detected spur in the range is greater than the value of the GetRangeSpurAbsoluteLimit(String, Double) method. |
| Pass | 1 | Indicates that all detected spurs in the range are lower than the value of the GetRangeSpurAbsoluteLimit(String, Double) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1e257e12-dd85-5594-2b1b-3e933ccd0332.htm language=enus -->
## TOPIC 00084: rfmxspecandotnet/html/1e257e12-dd85-5594-2b1b-3e933ccd0332.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1e257e12-dd85-5594-2b1b-3e933ccd0332.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1e257e12-dd85-5594-2b1b-3e933ccd0332.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.SetAveragingCount Method

RFmxSpecAnMXTxpConfigurationSetAveragingCount Method

Sets the number of acquisitions used for averaging.

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
  - Specifies the number of acquisitions used for averaging.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPSetAveragingCount() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1ec22483-bf68-1f6a-85a7-9016da35b0c2.htm language=enus -->
## TOPIC 00085: rfmxspecandotnet/html/1ec22483-bf68-1f6a-85a7-9016da35b0c2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1ec22483-bf68-1f6a-85a7-9016da35b0c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1ec22483-bf68-1f6a-85a7-9016da35b0c2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdLookupTableThresholdEnabled Enumeration

RFmxSpecAnMXDpdLookupTableThresholdEnabled Enumeration

SetModel(String, RFmxSpecAnMXDpdModel)

LookupTable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdLookupTableThresholdEnabled
```

```text
Public Enumeration RFmxSpecAnMXDpdLookupTableThresholdEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | All samples are considered for the DPD measurement. |
| True | 1 | Samples above the threshold level specified are considered for the DPD measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/1faf51f5-5a2d-e616-9d82-e83fa719d4a7.htm language=enus -->
## TOPIC 00086: rfmxspecandotnet/html/1faf51f5-5a2d-e616-9d82-e83fa719d4a7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/1faf51f5-5a2d-e616-9d82-e83fa719d4a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/1faf51f5-5a2d-e616-9d82-e83fa719d4a7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetEqualizerMode Method

RFmxSpecAnMXAmpmConfigurationGetEqualizerMode Method

Gets whether the measurement equalizes the channel.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEqualizerMode(
	string selectorString,
	out RFmxSpecAnMXAmpmEqualizerMode value
)
```

```text
Public Function GetEqualizerMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmEqualizerMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmEqualizerMode**
  - Upon return, contains whether the measurement equalizes the channel.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2034a8a2-6c9d-8f06-6728-6b0905443de0.htm language=enus -->
## TOPIC 00087: rfmxspecandotnet/html/2034a8a2-6c9d-8f06-6728-6b0905443de0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2034a8a2-6c9d-8f06-6728-6b0905443de0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2034a8a2-6c9d-8f06-6728-6b0905443de0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMemoryPolynomialLagOrderType Method

RFmxSpecAnMXDpdConfigurationGetMemoryPolynomialLagOrderType Method

RFmxSpecAnMXDpdModel

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMemoryPolynomialLagOrderType(
	string selectorString,
	out RFmxSpecAnMXDpdMemoryPolynomialLagOrderType value
)
```

```text
Public Function GetMemoryPolynomialLagOrderType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdMemoryPolynomialLagOrderType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdMemoryPolynomialLagOrderType**
  - Upon return, contains the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/20412a1d-57eb-65ea-3bcc-e0d819189e16.htm language=enus -->
## TOPIC 00088: rfmxspecandotnet/html/20412a1d-57eb-65ea-3bcc-e0d819189e16.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/20412a1d-57eb-65ea-3bcc-e0d819189e16.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/20412a1d-57eb-65ea-3bcc-e0d819189e16.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetMeasurementInterval Method

RFmxSpecAnMXAmpmConfigurationSetMeasurementInterval Method

Sets the duration, in seconds, of the reference waveform considered for the AMPM measurement. When the reference waveform contains an idle duration, the AMPM measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

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
  - Contains the duration, in seconds, of the reference waveform considered for the AMPM measurement. When the reference waveform contains an idle duration, the AMPM measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMSetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/206add10-4e35-5be1-c02e-c4f1b2a1d701.htm language=enus -->
## TOPIC 00089: rfmxspecandotnet/html/206add10-4e35-5be1-c02e-c4f1b2a1d701.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/206add10-4e35-5be1-c02e-c4f1b2a1d701.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/206add10-4e35-5be1-c02e-c4f1b2a1d701.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetLowerIntermodFrequency Method

RFmxSpecAnMXIMConfigurationGetLowerIntermodFrequency Method

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerIntermodFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerIntermodFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True.

###### Return Value

Int32

##### Remarks

IMLowerIntermodFrequency

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2089a284-8d6d-9a60-ced1-91ab4131e1c7.htm language=enus -->
## TOPIC 00090: rfmxspecandotnet/html/2089a284-8d6d-9a60-ced1-91ab4131e1c7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2089a284-8d6d-9a60-ced1-91ab4131e1c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2089a284-8d6d-9a60-ced1-91ab4131e1c7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration Methods

RFmxSpecAnMXIMConfiguration Methods

The [RFmxSpecAnMXIMConfiguration](6167d7ed-eab3-0e01-51d2-cf0d74da919f.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAutoIntermodsSetup | Configures whether the measurement computes the intermod frequencies or uses manually specified frequencies. |
|  | ConfigureAveraging | Configures averaging for the IM measurement. |
|  | ConfigureFft | Configures the window and FFT to obtain a spectrum for the IM measurement. |
|  | ConfigureFrequencyDefinition | Configures whether you can specify the tones and intermod frequencies as either relative to the RF center frequency or as absolute frequencies. |
|  | ConfigureFundamentalTones | Configures the upper and lower frequencies in a two-tone input signal. |
|  | ConfigureIntermod | Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to False. Use "intermod(n)" as the selector string to configure this method. |
|  | ConfigureIntermodArray | Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to False. |
|  | ConfigureMeasurementMethod | Configures the method for performing the IM measurement. |
|  | ConfigureNumberOfIntermods | Configures the number of intermods to measure when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to False. |
|  | ConfigureRbwFilter | Configures the RBW filter. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the IM measurement. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAutoIntermodsSetupEnabled | Gets whether the measurement computes the intermod frequencies or uses user-specified frequencies. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXIMAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the IM measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. |
|  | GetFarIFOutputPowerOffset | Gets the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |
|  | GetFftPadding | Gets the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. |
|  | GetFftWindow | Gets the FFT window type to use to reduce spectral leakage. |
|  | GetFrequencyDefinition | Gets whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. |
|  | GetFundamentalLowerToneFrequency | Gets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |
|  | GetFundamentalUpperToneFrequency | Gets the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIFOutputPowerOffsetAuto | Gets whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. |
|  | GetIntermodEnabled | Gets whether to enable an intermod for the IM measurement. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | GetIntermodOrder | Gets the order of the intermod. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | GetIntermodSide | Gets whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | GetLocalPeakSearchEnabled | Gets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. |
|  | GetLowerIntermodFrequency | Gets the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | GetMaximumIntermodOrder | Gets the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order. |
|  | GetMeasurementEnabled | Gets whether to enable the IM measurement. |
|  | GetMeasurementMethod | Gets the method used to perform the IM measurement. |
|  | GetNearIFOutputPowerOffset | Gets the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the IM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetNumberOfIntermods | Gets the number of intermods to measure when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to False. |
|  | GetRbwFilterAutoBandwidth | Gets whether the measurement computes the RBW. |
|  | GetRbwFilterBandwidth | Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxSpecAnMXIMRbwFilterAutoBandwidth) method to False. This value is expressed in Hz. |
|  | GetRbwFilterType | Gets the response of the digital RBW filter. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxSpecAnMXIMSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | GetUpperIntermodFrequency | Gets the frequency of the upper intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the IM measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAutoIntermodsSetupEnabled | Sets whether the measurement computes the intermod frequencies or uses user-specified frequencies. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXIMAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the IM measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. |
|  | SetFarIFOutputPowerOffset | Sets the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |
|  | SetFftPadding | Sets the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. |
|  | SetFftWindow | Sets the FFT window type to use to reduce spectral leakage. |
|  | SetFrequencyDefinition | Sets whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. |
|  | SetFundamentalLowerToneFrequency | Sets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |
|  | SetFundamentalUpperToneFrequency | Sets the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |
|  | SetIFOutputPowerOffsetAuto | Sets whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. |
|  | SetIntermodEnabled | Sets whether to enable an intermod for the IM measurement. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | SetIntermodOrder | Sets the order of the intermod. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | SetIntermodSide | Sets whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | SetLocalPeakSearchEnabled | Sets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. |
|  | SetLowerIntermodFrequency | Sets the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | SetMaximumIntermodOrder | Sets the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order. |
|  | SetMeasurementEnabled | Sets whether to enable the IM measurement. |
|  | SetMeasurementMethod | Sets the method used to perform the IM measurement. |
|  | SetNearIFOutputPowerOffset | Sets the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(String, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the IM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetNumberOfIntermods | Sets the number of intermods to measure when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to False. |
|  | SetRbwFilterAutoBandwidth | Sets whether the measurement computes the RBW. |
|  | SetRbwFilterBandwidth | Sets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxSpecAnMXIMRbwFilterAutoBandwidth) method to False. This value is expressed in Hz. |
|  | SetRbwFilterType | Sets the response of the digital RBW filter. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxSpecAnMXIMSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | SetUpperIntermodFrequency | Sets the frequency of the upper intermodulation product. This value is expressed in Hz. This method is not used when you set the GetAutoIntermodsSetupEnabled(String, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) method to True. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2092366d-2650-a1be-df47-67c13d8dea2c.htm language=enus -->
## TOPIC 00091: rfmxspecandotnet/html/2092366d-2650-a1be-df47-67c13d8dea2c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2092366d-2650-a1be-df47-67c13d8dea2c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2092366d-2650-a1be-df47-67c13d8dea2c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.GetRbwFilterBandwidthDefinition Method

RFmxSpecAnMXObwConfigurationGetRbwFilterBandwidthDefinition Method

SetRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterBandwidthDefinition(
	string selectorString,
	out RFmxSpecAnMXObwRbwFilterBandwidthDefinition value
)
```

```text
Public Function GetRbwFilterBandwidthDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXObwRbwFilterBandwidthDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwRbwFilterBandwidthDefinition**
  - Upon return, contains the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWGetRBWFilterBandwidthDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/26f98015-c26d-07e5-84f9-e74cb2e52fa4.htm language=enus -->
## TOPIC 00092: rfmxspecandotnet/html/26f98015-c26d-07e5-84f9-e74cb2e52fa4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/26f98015-c26d-07e5-84f9-e74cb2e52fa4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/26f98015-c26d-07e5-84f9-e74cb2e52fa4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetApplyDpdUserLookupTableType Method

RFmxSpecAnMXDpdApplyDpdGetApplyDpdUserLookupTableType Method

Gets the DPD Lookup Table (LUT) type.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetApplyDpdUserLookupTableType(
	string selectorString,
	out RFmxSpecAnMXDpdApplyDpdUserLookupTableType value
)
```

```text
Public Function GetApplyDpdUserLookupTableType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdApplyDpdUserLookupTableType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdUserLookupTableType**
  - Upon return, contains the the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method to User.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2b703b4c-8863-7fbe-63f3-17ec6f2be468.htm language=enus -->
## TOPIC 00093: rfmxspecandotnet/html/2b703b4c-8863-7fbe-63f3-17ec6f2be468.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2b703b4c-8863-7fbe-63f3-17ec6f2be468.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2b703b4c-8863-7fbe-63f3-17ec6f2be468.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerConfiguration.ConfigureBandSpan Method

RFmxSpecAnMXMarkerConfigurationConfigureBandSpan Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureBandSpan(
	string selectorString,
	double span
)
```

```text
Public Function ConfigureBandSpan ( 
	selectorString As String,
	span As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of marker number. Example:"marker0" You can use the RFmxSpecAn_BuildMarkerString2 method to build the selector string.
- **span Double**
  - Specifies the width of the span for the selected marker. This method selects the trace data within the specified span to perform specified marker method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXMarkerConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2c1e450e-b3ba-4bd3-4dae-bf154fdc8cde.htm language=enus -->
## TOPIC 00094: rfmxspecandotnet/html/2c1e450e-b3ba-4bd3-4dae-bf154fdc8cde.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2c1e450e-b3ba-4bd3-4dae-bf154fdc8cde.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2c1e450e-b3ba-4bd3-4dae-bf154fdc8cde.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.GetRbwFilterBandwidth Method

RFmxSpecAnMXTxpConfigurationGetRbwFilterBandwidth Method

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

This method maps to the RFmxSpecAn_TXPGetRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2c31faf1-1ccd-ebca-c8ef-2cfdcc8f78f6.htm language=enus -->
## TOPIC 00095: rfmxspecandotnet/html/2c31faf1-1ccd-ebca-c8ef-2cfdcc8f78f6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2c31faf1-1ccd-ebca-c8ef-2cfdcc8f78f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2c31faf1-1ccd-ebca-c8ef-2cfdcc8f78f6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.SetEqualizerFilterLength Method

RFmxSpecAnMXIdpdConfigurationSetEqualizerFilterLength Method

Sets the length of the equalizer filter to be trained.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEqualizerFilterLength(
	string selectorString,
	int value
)
```

```text
Public Function SetEqualizerFilterLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the length of the equalizer filter to be trained.

###### Return Value

Int32

##### Remarks

IdpdEqualizerFilterLength

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2c35ddbe-65dd-0738-b446-d918f647d222.htm language=enus -->
## TOPIC 00096: rfmxspecandotnet/html/2c35ddbe-65dd-0738-b446-d918f647d222.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2c35ddbe-65dd-0738-b446-d918f647d222.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2c35ddbe-65dd-0738-b446-d918f647d222.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetUserMemoryPolynomialLagMemoryDepth Method

RFmxSpecAnMXDpdApplyDpdSetUserMemoryPolynomialLagMemoryDepth Method

SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel)

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
public int SetUserMemoryPolynomialLagMemoryDepth(
	string selectorString,
	int value
)
```

```text
Public Function SetUserMemoryPolynomialLagMemoryDepth ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Contains the lead memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set RFmxSpecAnMXDpdApplyDpdConfigurationInput to User.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDUserMemoryPolynomialLagMemoryDepth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2c8a6ca4-aa23-d2ac-bcda-112931cc891c.htm language=enus -->
## TOPIC 00097: rfmxspecandotnet/html/2c8a6ca4-aa23-d2ac-bcda-112931cc891c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2c8a6ca4-aa23-d2ac-bcda-112931cc891c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2c8a6ca4-aa23-d2ac-bcda-112931cc891c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.GetMeasurementInterval Method

RFmxSpecAnMXTxpConfigurationGetMeasurementInterval Method

Gets the acquisition time, in seconds, for the transmit power (TXP) measurement.

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
  - Upon return, contains the acquisition time, in seconds, for the TXP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPGetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2cc99af0-6d8f-09d5-1014-470f817caeff.htm language=enus -->
## TOPIC 00098: rfmxspecandotnet/html/2cc99af0-6d8f-09d5-1014-470f817caeff.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2cc99af0-6d8f-09d5-1014-470f817caeff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2cc99af0-6d8f-09d5-1014-470f817caeff.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.ConfigureAveraging Method

RFmxSpecAnMXFcntConfigurationConfigureAveraging Method

Configures averaging for the frequency count (Fcnt) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxSpecAnMXFcntAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxSpecAnMXFcntAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxSpecAnMXFcntAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxSpecAnMXFcntAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxSpecAnMXFcntAveragingEnabled**
  - Specifies whether to enable averaging for the Fcnt measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging.
- **averagingType RFmxSpecAnMXFcntAveragingType**
  - Specifies the averaging type for averaging multiple acquisitions.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntCfgAveraging() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2ccc57ae-dba4-488f-ac91-6820099ee3ad.htm language=enus -->
## TOPIC 00099: rfmxspecandotnet/html/2ccc57ae-dba4-488f-ac91-6820099ee3ad.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2ccc57ae-dba4-488f-ac91-6820099ee3ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2ccc57ae-dba4-488f-ac91-6820099ee3ad.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMemoryPolynomialMaximumLead Method

RFmxSpecAnMXDpdConfigurationSetMemoryPolynomialMaximumLead Method

SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel)

MemoryPolynomial

GeneralizedMemoryPolynomial

SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput)

User

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMemoryPolynomialMaximumLead(
	string selectorString,
	int value
)
```

```text
Public Function SetMemoryPolynomialMaximumLead ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the maximum lead stagger cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial, and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialMaximumLead() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2e0af98e-fc09-f3f3-fcef-e9d93d7f3b8b.htm language=enus -->
## TOPIC 00100: rfmxspecandotnet/html/2e0af98e-fc09-f3f3-fcef-e9d93d7f3b8b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2e0af98e-fc09-f3f3-fcef-e9d93d7f3b8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2e0af98e-fc09-f3f3-fcef-e9d93d7f3b8b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetNumberOfAnalysisThreads Method

RFmxSpecAnMXDpdConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the DPD measurement.

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
  - Contains the maximum number of threads used for parallelism for the DPD measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetNumberofAnalysisThreads() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/2fd5d25c-e8b5-04c9-48fe-91f58802ca53.htm language=enus -->
## TOPIC 00101: rfmxspecandotnet/html/2fd5d25c-e8b5-04c9-48fe-91f58802ca53.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/2fd5d25c-e8b5-04c9-48fe-91f58802ca53.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/2fd5d25c-e8b5-04c9-48fe-91f58802ca53.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrum.Results Property

RFmxSpecAnMXSpectrumResults Property

RFmxSpecAnMXSpectrumResults

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXSpectrumResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxSpecAnMXSpectrumResults
	Get
```

###### Property Value

RFmxSpecAnMXSpectrumResults

##### See Also

###### Reference

RFmxSpecAnMXSpectrum Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3145a1b3-16f4-4f59-63df-7227e2ae26e2.htm language=enus -->
## TOPIC 00102: rfmxspecandotnet/html/3145a1b3-16f4-4f59-63df-7227e2ae26e2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3145a1b3-16f4-4f59-63df-7227e2ae26e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3145a1b3-16f4-4f59-63df-7227e2ae26e2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetSweepTimeAuto Method

RFmxSpecAnMXIMConfigurationGetSweepTimeAuto Method

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
	out RFmxSpecAnMXIMSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIMSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIMSweepTimeAuto**
  - Upon return, contains whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

IMSweepTimeAuto

True

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/31ab2ab3-700b-ec60-6cb8-0e3f13f1d67e.htm language=enus -->
## TOPIC 00103: rfmxspecandotnet/html/31ab2ab3-700b-ec60-6cb8-0e3f13f1d67e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/31ab2ab3-700b-ec60-6cb8-0e3f13f1d67e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/31ab2ab3-700b-ec60-6cb8-0e3f13f1d67e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.SetMeasurementIntervalMode Method

RFmxSpecAnMXPavtConfigurationSetMeasurementIntervalMode Method

Sets the mode of configuring the measurement interval.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementIntervalMode(
	string selectorString,
	RFmxSpecAnMXPavtMeasurementIntervalMode value
)
```

```text
Public Function SetMeasurementIntervalMode ( 
	selectorString As String,
	value As RFmxSpecAnMXPavtMeasurementIntervalMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPavtMeasurementIntervalMode**
  - Specifies the mode of configuring the measurement interval.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3372587b-0153-daec-f251-df8dc4567ba1.htm language=enus -->
## TOPIC 00104: rfmxspecandotnet/html/3372587b-0153-daec-f251-df8dc4567ba1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3372587b-0153-daec-f251-df8dc4567ba1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3372587b-0153-daec-f251-df8dc4567ba1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSem.Configuration Property

RFmxSpecAnMXSemConfiguration Property

RFmxSpecAnMXSemConfiguration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXSemConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxSpecAnMXSemConfiguration
	Get
```

###### Property Value

RFmxSpecAnMXSemConfiguration

##### See Also

###### Reference

RFmxSpecAnMXSem Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/346565b2-c74f-7d17-c081-d7262689c7f9.htm language=enus -->
## TOPIC 00105: rfmxspecandotnet/html/346565b2-c74f-7d17-c081-d7262689c7f9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/346565b2-c74f-7d17-c081-d7262689c7f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/346565b2-c74f-7d17-c081-d7262689c7f9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.Commit Method

RFmxSpecAnMXListCommit Method

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
  - Pass an empty string. The list name that is passed when creating the list is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/34cba55a-2ba8-44a7-30ae-a163941b87a4.htm language=enus -->
## TOPIC 00106: rfmxspecandotnet/html/34cba55a-2ba8-44a7-30ae-a163941b87a4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/34cba55a-2ba8-44a7-30ae-a163941b87a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/34cba55a-2ba8-44a7-30ae-a163941b87a4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetCarrierTotalRelativePower Method

RFmxSpecAnMXSemResultsGetCarrierTotalRelativePower Method

Gets the carrier power, in dB, relative to the total carrier power of all enabled carriers.

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
  - Upon return, contains the carrier power, in dB, relative to the total carrier power of all enabled carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsCarrierTotalRelativePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/34e17b0f-10f5-912b-d01b-13d236986b58.htm language=enus -->
## TOPIC 00107: rfmxspecandotnet/html/34e17b0f-10f5-912b-d01b-13d236986b58.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/34e17b0f-10f5-912b-d01b-13d236986b58.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/34e17b0f-10f5-912b-d01b-13d236986b58.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetUserMemoryPolynomialMaximumLag Method

RFmxSpecAnMXDpdApplyDpdGetUserMemoryPolynomialMaximumLag Method

Gets the maximum lag stagger cross term of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUserMemoryPolynomialMaximumLag(
	string selectorString,
	out int value
)
```

```text
Public Function GetUserMemoryPolynomialMaximumLag ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the maximum lag stagger cross term of the DPD polynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserMemoryPolynomialMaximumLag() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/351acaaf-a674-270a-b8de-69bfc863a21e.htm language=enus -->
## TOPIC 00108: rfmxspecandotnet/html/351acaaf-a674-270a-b8de-69bfc863a21e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/351acaaf-a674-270a-b8de-69bfc863a21e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/351acaaf-a674-270a-b8de-69bfc863a21e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition Enumeration

RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition Enumeration

Specifies the frequency range for integrated noise measurements.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition
```

```text
Public Enumeration RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | Integrated noise measurement is not computed. |
| Measurement | 1 | The complete log plot frequency range, considered as a single range, is used for computing integrated measurements. |
| Custom | 2 | The measurement range(s) specified by PhaseNoise Integrated Noise Start Freq method and the PhaseNoise Integrated Noise Stop Freq method is used for computing integrated measurements. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/35d22cf7-d73a-eedf-774f-65b4ec77601a.htm language=enus -->
## TOPIC 00109: rfmxspecandotnet/html/35d22cf7-d73a-eedf-774f-65b4ec77601a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/35d22cf7-d73a-eedf-774f-65b4ec77601a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/35d22cf7-d73a-eedf-774f-65b4ec77601a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetMeasurementInterval Method

RFmxSpecAnMXAmpmConfigurationGetMeasurementInterval Method

Gets the duration, in seconds, of the reference waveform considered for the AMPM measurement. When the reference waveform contains an idle duration, the AMPM measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

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
  - Upon return, contains the duration, in seconds, of the reference waveform considered for the AMPM measurement. When the reference waveform contains an idle duration, the AMPM measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/38242fa4-c66c-f832-6d0f-0908be135be1.htm language=enus -->
## TOPIC 00110: rfmxspecandotnet/html/38242fa4-c66c-f832-6d0f-0908be135be1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/38242fa4-c66c-f832-6d0f-0908be135be1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/38242fa4-c66c-f832-6d0f-0908be135be1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetRangeRbwFilterBandwidthDefinition Method

RFmxSpecAnMXSpurConfigurationGetRangeRbwFilterBandwidthDefinition Method

SetRangeRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeRbwFilterBandwidthDefinition(
	string selectorString,
	out RFmxSpecAnMXSpurRbwFilterBandwidthDefinition value
)
```

```text
Public Function GetRangeRbwFilterBandwidthDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpurRbwFilterBandwidthDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSpurRbwFilterBandwidthDefinition**
  - Upon return, contains the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetRangeRBWFilterBandwidthDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/38399bed-0032-5b49-4056-a4948c60626e.htm language=enus -->
## TOPIC 00111: rfmxspecandotnet/html/38399bed-0032-5b49-4056-a4948c60626e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/38399bed-0032-5b49-4056-a4948c60626e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/38399bed-0032-5b49-4056-a4948c60626e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetColdSourceInputTerminationVswrFrequency Method

RFmxSpecAnMXNFConfigurationGetColdSourceInputTerminationVswrFrequency Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetColdSourceInputTerminationVswrFrequency(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetColdSourceInputTerminationVswrFrequency ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains an array of frequencies corresponding to the voltage standing wave ratios (VSWR) of the microwave termination used in the cold source method as specified by the SetColdSourceInputTerminationVswr(String, Double) method. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

NFColdSourceInputTerminationVswrFrequency

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3840341a-f002-80d2-7f47-f5144fa3aa6f.htm language=enus -->
## TOPIC 00112: rfmxspecandotnet/html/3840341a-f002-80d2-7f47-f5144fa3aa6f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3840341a-f002-80d2-7f47-f5144fa3aa6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3840341a-f002-80d2-7f47-f5144fa3aa6f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemUpperOffsetMeasurementStatus Enumeration

RFmxSpecAnMXSemUpperOffsetMeasurementStatus Enumeration

SetOffsetLimitFailMask(String, RFmxSpecAnMXSemOffsetLimitFailMask)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemUpperOffsetMeasurementStatus
```

```text
Public Enumeration RFmxSpecAnMXSemUpperOffsetMeasurementStatus
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d424c76-e5ee-b70c-98e5-d12775aed208.htm language=enus -->
## TOPIC 00113: rfmxspecandotnet/html/3d424c76-e5ee-b70c-98e5-d12775aed208.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d424c76-e5ee-b70c-98e5-d12775aed208.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d424c76-e5ee-b70c-98e5-d12775aed208.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureCarrierRbwFilter Method

RFmxSpecAnMXSemConfigurationConfigureCarrierRbwFilter Method

Configures the resolution bandwidth (RBW) filter of the carrier signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierRbwFilter(
	string selectorString,
	RFmxSpecAnMXSemCarrierRbwAutoBandwidth rbwAuto,
	double rbw,
	RFmxSpecAnMXSemCarrierRbwFilterType rbwFilterType
)
```

```text
Public Function ConfigureCarrierRbwFilter ( 
	selectorString As String,
	rbwAuto As RFmxSpecAnMXSemCarrierRbwAutoBandwidth,
	rbw As Double,
	rbwFilterType As RFmxSpecAnMXSemCarrierRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **rbwAuto RFmxSpecAnMXSemCarrierRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW of the carrier. Refer to the SEM topic for more details on RBW.
- **rbw Double**
  - Specifies the bandwidth, in Hz, of the RBW filter used to sweep the acquired carrier signal, when you set the SetCarrierRbwFilterAutoBandwidth(String, RFmxSpecAnMXSemCarrierRbwAutoBandwidth) method to False.
- **rbwFilterType RFmxSpecAnMXSemCarrierRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierRBWFilter() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d528970-9907-b7d5-ac12-312ea98ffba9.htm language=enus -->
## TOPIC 00114: rfmxspecandotnet/html/3d528970-9907-b7d5-ac12-312ea98ffba9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d528970-9907-b7d5-ac12-312ea98ffba9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d528970-9907-b7d5-ac12-312ea98ffba9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.GetCarrierIntegrationBandwidth Method

RFmxSpecAnMXSemResultsGetCarrierIntegrationBandwidth Method

Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

- **selectorString String**
  - Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency range, in hertz (Hz), over which the measurement integrates the carrier power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsCarrierIntegrationBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d54b8cd-a8db-37e6-6b1d-1682177cf0bb.htm language=enus -->
## TOPIC 00115: rfmxspecandotnet/html/3d54b8cd-a8db-37e6-6b1d-1682177cf0bb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d54b8cd-a8db-37e6-6b1d-1682177cf0bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d54b8cd-a8db-37e6-6b1d-1682177cf0bb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetAMToPMCurveFitType Method

RFmxSpecAnMXAmpmConfigurationSetAMToPMCurveFitType Method

Sets the polynomial approximation cost-function of the device under test AM-to-PM characteristic.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAMToPMCurveFitType(
	string selectorString,
	RFmxSpecAnMXAmpmAMToPMCurveFitType value
)
```

```text
Public Function SetAMToPMCurveFitType ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmAMToPMCurveFitType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmAMToPMCurveFitType**
  - Contains the polynomial approximation cost-function of the device under test AM-to-PM characteristic.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMSetAMToPMCurveFitType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d582814-a7d7-4d02-5101-42c48eb927ba.htm language=enus -->
## TOPIC 00116: rfmxspecandotnet/html/3d582814-a7d7-4d02-5101-42c48eb927ba.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d582814-a7d7-4d02-5101-42c48eb927ba.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d582814-a7d7-4d02-5101-42c48eb927ba.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpAmplitudeCorrectionType Enumeration

RFmxSpecAnMXChpAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpAmplitudeCorrectionType
```

```text
Public Enumeration RFmxSpecAnMXChpAmplitudeCorrectionType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d5b23c2-16dc-8ec3-41da-a15b42a2f993.htm language=enus -->
## TOPIC 00117: rfmxspecandotnet/html/3d5b23c2-16dc-8ec3-41da-a15b42a2f993.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d5b23c2-16dc-8ec3-41da-a15b42a2f993.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d5b23c2-16dc-8ec3-41da-a15b42a2f993.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpNoiseCalibrationMode Enumeration

RFmxSpecAnMXAcpNoiseCalibrationMode Enumeration

Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpNoiseCalibrationMode
```

```text
Public Enumeration RFmxSpecAnMXAcpNoiseCalibrationMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Manual | 0 | When you set the SetMeasurementMode(String, RFmxSpecAnMXAcpMeasurementMode) method to RFMXSPECAN_VAL_ACP_MEASUREMENT_MODE_NOISE_CALIBRATE, you can initiate instrument noise calibration for the ACP measurement manually. When you set the ACP Meas Mode method to Measure, you can initiate the ACP measurement manually. |
| Auto | 1 | When you set the SetNoiseCompensationEnabled(String, RFmxSpecAnMXAcpNoiseCompensationEnabled) to True, RFmx sets the Input Isolation Enabled method to Enabled and calibrates the instrument noise in the current state of the instrument. RFmx then resets the Input Isolation Enabled method and performs the ACP measurement, including compensation for noise of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set the SetNoiseCompensationEnabled(String, RFmxSpecAnMXAcpNoiseCompensationEnabled) method to False, RFmx does not calibrate instrument noise and only performs the ACP measurement without compensating for noise of the instrument. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d5c50ab-afd5-119f-ebe4-ab50e99e5c84.htm language=enus -->
## TOPIC 00118: rfmxspecandotnet/html/3d5c50ab-afd5-119f-ebe4-ab50e99e5c84.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d5c50ab-afd5-119f-ebe4-ab50e99e5c84.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d5c50ab-afd5-119f-ebe4-ab50e99e5c84.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMemoryPolynomialLagOrder Method

RFmxSpecAnMXDpdConfigurationSetMemoryPolynomialLagOrder Method

SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel)

MemoryPolynomial

GeneralizedMemoryPolynomial

SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput)

User

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMemoryPolynomialLagOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetMemoryPolynomialLagOrder ( 
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

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialLagOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d5fb356-0ce9-6940-7b57-2dad37974c4b.htm language=enus -->
## TOPIC 00119: rfmxspecandotnet/html/3d5fb356-0ce9-6940-7b57-2dad37974c4b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d5fb356-0ce9-6940-7b57-2dad37974c4b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d5fb356-0ce9-6940-7b57-2dad37974c4b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetUserMemoryPolynomialMaximumLead Method

RFmxSpecAnMXDpdApplyDpdGetUserMemoryPolynomialMaximumLead Method

Gets the maximum lead stagger cross term of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUserMemoryPolynomialMaximumLead(
	string selectorString,
	out int value
)
```

```text
Public Function GetUserMemoryPolynomialMaximumLead ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the maximum lead stagger cross term of the DPD polynomial.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserMemoryPolynomialMaximumLead() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3d628eff-a954-7e4c-b02d-6029005c9861.htm language=enus -->
## TOPIC 00120: rfmxspecandotnet/html/3d628eff-a954-7e4c-b02d-6029005c9861.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3d628eff-a954-7e4c-b02d-6029005c9861.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3d628eff-a954-7e4c-b02d-6029005c9861.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoise Properties

RFmxSpecAnMXPhaseNoise Properties

The [RFmxSpecAnMXPhaseNoise](be357805-baca-5dcb-f9fc-aef55bf04f5e.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxSpecAnMXPhaseNoiseConfiguration instance that provides methods to configure the PhaseNoise measurement |
|  | Results | Gets the RFmxSpecAnMXPhaseNoiseResults instance that provides methods to fetch and read the PhaseNoise measurement results. |

Top

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoise Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3dbb2b15-4e6f-2566-e7fe-91f681364f98.htm language=enus -->
## TOPIC 00121: rfmxspecandotnet/html/3dbb2b15-4e6f-2566-e7fe-91f681364f98.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3dbb2b15-4e6f-2566-e7fe-91f681364f98.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3dbb2b15-4e6f-2566-e7fe-91f681364f98.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.FetchRangeStatus Method

RFmxSpecAnMXSpurResultsFetchRangeStatus Method

Fetches the range status for spurious emission (Spur) measurements.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchRangeStatus(
	string selectorString,
	double timeout,
	out RFmxSpecAnMXSpurRangeStatus rangeStatus,
	out int detectedSpurs
)
```

```text
Public Function FetchRangeStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef rangeStatus As RFmxSpecAnMXSpurRangeStatus,
	<OutAttribute> ByRef detectedSpurs As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and range number. Example: "range0", "result::r1/range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **rangeStatus RFmxSpecAnMXSpurRangeStatus**
  - Indicates the measurement status for the frequency range.
- **detectedSpurs Int32**
  - Returns the number of detected Spurs in the specified frequency range.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurFetchRangeStatus() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3e5a7826-0db6-b159-1481-d289a4663dc0.htm language=enus -->
## TOPIC 00122: rfmxspecandotnet/html/3e5a7826-0db6-b159-1481-d289a4663dc0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3e5a7826-0db6-b159-1481-d289a4663dc0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3e5a7826-0db6-b159-1481-d289a4663dc0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.BuildIntermodString Method

RFmxSpecAnMXBuildIntermodString Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildIntermodString(
	string selectorString,
	int intermodNumber
)
```

```text
Public Shared Function BuildIntermodString ( 
	selectorString As String,
	intermodNumber As Integer
) As String
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **intermodNumber Int32**
  - Specifies the intermod number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3e769c21-b0ae-571c-0106-034e92c0fa5c.htm language=enus -->
## TOPIC 00123: rfmxspecandotnet/html/3e769c21-b0ae-571c-0106-034e92c0fa5c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3e769c21-b0ae-571c-0106-034e92c0fa5c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3e769c21-b0ae-571c-0106-034e92c0fa5c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetCarrierBandwidth Method

RFmxSpecAnMXDpdConfigurationGetCarrierBandwidth Method

SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled)

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
  - Upon return, contains the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

DpdCarrierBandwidth

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3ec82f7d-b4c2-3a92-665e-6aef50a50bde.htm language=enus -->
## TOPIC 00124: rfmxspecandotnet/html/3ec82f7d-b4c2-3a92-665e-6aef50a50bde.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3ec82f7d-b4c2-3a92-665e-6aef50a50bde.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3ec82f7d-b4c2-3a92-665e-6aef50a50bde.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.ConfigureRangeSweepTimeArray Method

RFmxSpecAnMXSpurConfigurationConfigureRangeSweepTimeArray Method

SetRangeSweepTimeAuto(String, RFmxSpecAnMXSpurSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRangeSweepTimeArray(
	string selectorString,
	RFmxSpecAnMXSpurSweepTimeAuto[] sweepTimeAuto,
	double[] sweepTimeInterval
)
```

```text
Public Function ConfigureRangeSweepTimeArray ( 
	selectorString As String,
	sweepTimeAuto As RFmxSpecAnMXSpurSweepTimeAuto(),
	sweepTimeInterval As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sweepTimeAuto RFmxSpecAnMXSpurSweepTimeAuto**
  - Specifies whether the measurement computes the sweep time.
- **sweepTimeInterval Double**
  - Specifies the array of sweep times, in seconds, when you set the SetRangeSweepTimeAuto(String, RFmxSpecAnMXSpurSweepTimeAuto) to False.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurCfgRangeSweepTimeArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f035eb8-2dfa-be09-fc5d-9879384a0577.htm language=enus -->
## TOPIC 00125: rfmxspecandotnet/html/3f035eb8-2dfa-be09-fc5d-9879384a0577.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f035eb8-2dfa-be09-fc5d-9879384a0577.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f035eb8-2dfa-be09-fc5d-9879384a0577.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemOffsetRbwFilterType Enumeration

RFmxSpecAnMXSemOffsetRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemOffsetRbwFilterType
```

```text
Public Enumeration RFmxSpecAnMXSemOffsetRbwFilterType
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f092f0e-5928-9ca8-50e2-cc58bc4b8873.htm language=enus -->
## TOPIC 00126: rfmxspecandotnet/html/3f092f0e-5928-9ca8-50e2-cc58bc4b8873.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f092f0e-5928-9ca8-50e2-cc58bc4b8873.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f092f0e-5928-9ca8-50e2-cc58bc4b8873.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.GetRbwFilterType Method

RFmxSpecAnMXIMConfigurationGetRbwFilterType Method

Gets the response of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterType(
	string selectorString,
	out RFmxSpecAnMXIMRbwFilterType value
)
```

```text
Public Function GetRbwFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIMRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIMRbwFilterType**
  - Upon return, contains the response of the digital RBW filter.

###### Return Value

Int32

##### Remarks

IMRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f1e879a-7f2e-32f0-7ee3-fd33d9ef6ac0.htm language=enus -->
## TOPIC 00127: rfmxspecandotnet/html/3f1e879a-7f2e-32f0-7ee3-fd33d9ef6ac0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f1e879a-7f2e-32f0-7ee3-fd33d9ef6ac0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f1e879a-7f2e-32f0-7ee3-fd33d9ef6ac0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMeasurementEnabled Method

RFmxSpecAnMXDpdConfigurationGetMeasurementEnabled Method

Gets whether to enable DPD measurements.

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
  - if the DPD measurement is enabled; otherwise, .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f46a97a-5ebf-8ac8-0ddd-ebd8491a7e83.htm language=enus -->
## TOPIC 00128: rfmxspecandotnet/html/3f46a97a-5ebf-8ac8-0ddd-ebd8491a7e83.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f46a97a-5ebf-8ac8-0ddd-ebd8491a7e83.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f46a97a-5ebf-8ac8-0ddd-ebd8491a7e83.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.IM Property

RFmxSpecAnMXIM Property

RFmxSpecAnMXIM

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXIM IM { get; }
```

```text
Public ReadOnly Property IM As RFmxSpecAnMXIM
	Get
```

###### Property Value

RFmxSpecAnMXIM

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f473e54-bcfe-5d12-bc04-b58013946d7d.htm language=enus -->
## TOPIC 00129: rfmxspecandotnet/html/3f473e54-bcfe-5d12-bc04-b58013946d7d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f473e54-bcfe-5d12-bc04-b58013946d7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f473e54-bcfe-5d12-bc04-b58013946d7d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetNumberOfRanges Method

RFmxSpecAnMXSpurConfigurationGetNumberOfRanges Method

Gets the number of range configurations.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfRanges(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfRanges ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of range configurations.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetNumberOfRanges() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f4a8511-63b4-d42b-be45-3bd3993c44bc.htm language=enus -->
## TOPIC 00130: rfmxspecandotnet/html/3f4a8511-63b4-d42b-be45-3bd3993c44bc.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f4a8511-63b4-d42b-be45-3bd3993c44bc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f4a8511-63b4-d42b-be45-3bd3993c44bc.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpAveragingType Enumeration

RFmxSpecAnMXTxpAveragingType Enumeration

Specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXTxpAveragingType
```

```text
Public Enumeration RFmxSpecAnMXTxpAveragingType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power trace is averaged in a logarithm scale. |
| Scalar | 2 | The square root of the power trace is averaged. |
| Maximum | 3 | The peak power in the power trace at each sample instance is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the power trace at each sample instance is retained from one acquisition to the next. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f606e01-7b38-a0b1-ce83-ec11328a82a4.htm language=enus -->
## TOPIC 00131: rfmxspecandotnet/html/3f606e01-7b38-a0b1-ce83-ec11328a82a4.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f606e01-7b38-a0b1-ce83-ec11328a82a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f606e01-7b38-a0b1-ce83-ec11328a82a4.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdSignalType Enumeration

RFmxSpecAnMXDpdSignalType Enumeration

Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXDpdSignalType
```

```text
Public Enumeration RFmxSpecAnMXDpdSignalType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Modulated | 0 | The reference waveform is a cellular or connectivity standard signal. |
| Tones | 1 | The reference waveform is a continuous signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f711b87-808d-1132-8b0a-a8c6738065b1.htm language=enus -->
## TOPIC 00132: rfmxspecandotnet/html/3f711b87-808d-1132-8b0a-a8c6738065b1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f711b87-808d-1132-8b0a-a8c6738065b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f711b87-808d-1132-8b0a-a8c6738065b1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.ConfigureSegmentTypeArray Method

RFmxSpecAnMXPavtConfigurationConfigureSegmentTypeArray Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSegmentTypeArray(
	string selectorString,
	RFmxSpecAnMXPavtSegmentType[] segmentType
)
```

```text
Public Function ConfigureSegmentTypeArray ( 
	selectorString As String,
	segmentType As RFmxSpecAnMXPavtSegmentType()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **segmentType RFmxSpecAnMXPavtSegmentType**
  - Specifies the type of segment.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3f9b5089-b894-ead1-f368-11c34298c23f.htm language=enus -->
## TOPIC 00133: rfmxspecandotnet/html/3f9b5089-b894-ead1-f368-11c34298c23f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3f9b5089-b894-ead1-f368-11c34298c23f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3f9b5089-b894-ead1-f368-11c34298c23f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.Dpd Property

RFmxSpecAnMXDpd Property

Gets the RFmxSpecAnMXDpd instance that represents the DPD measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXDpd Dpd { get; }
```

```text
Public ReadOnly Property Dpd As RFmxSpecAnMXDpd
	Get
```

###### Property Value

RFmxSpecAnMXDpd

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3fa14a03-a316-f0bb-09cd-4644d758caa7.htm language=enus -->
## TOPIC 00134: rfmxspecandotnet/html/3fa14a03-a316-f0bb-09cd-4644d758caa7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3fa14a03-a316-f0bb-09cd-4644d758caa7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3fa14a03-a316-f0bb-09cd-4644d758caa7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetDetectorPoints Method

RFmxSpecAnMXAcpConfigurationSetDetectorPoints Method

Sets the number of trace points after the detector is applied.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDetectorPoints(
	string selectorString,
	int value
)
```

```text
Public Function SetDetectorPoints ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of trace points after the detector is applied.

###### Return Value

Int32

##### Remarks

AcpDetectorPoints

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3fb4a639-52e4-e98c-0591-a7b534f4d1b3.htm language=enus -->
## TOPIC 00135: rfmxspecandotnet/html/3fb4a639-52e4-e98c-0591-a7b534f4d1b3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3fb4a639-52e4-e98c-0591-a7b534f4d1b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3fb4a639-52e4-e98c-0591-a7b534f4d1b3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetUserDpdModel Method

RFmxSpecAnMXDpdApplyDpdGetUserDpdModel Method

Gets the DPD model used to apply DPD.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUserDpdModel(
	string selectorString,
	out RFmxSpecAnMXDpdApplyDpdUserDpdModel value
)
```

```text
Public Function GetUserDpdModel ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdApplyDpdUserDpdModel
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdUserDpdModel**
  - Upon return, contains the DPD model used to apply DPD.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserDPDModel() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3fc6f432-34c8-ae40-ee3f-20ea94d57e71.htm language=enus -->
## TOPIC 00136: rfmxspecandotnet/html/3fc6f432-34c8-ae40-ee3f-20ea94d57e71.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3fc6f432-34c8-ae40-ee3f-20ea94d57e71.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3fc6f432-34c8-ae40-ee3f-20ea94d57e71.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetAveragingMultiplier Method

RFmxSpecAnMXPhaseNoiseConfigurationGetAveragingMultiplier Method

Gets the factor by which you increase the averaging count for each range. This setting applies to both Auto and Manual range definitions.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingMultiplier(
	string selectorString,
	out int value
)
```

```text
Public Function GetAveragingMultiplier ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the factor by which you increase the averaging count for each range.

###### Return Value

Int32

##### Remarks

PhaseNoiseAveragingMultiplier

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/3fd14890-8d96-8343-68c7-625ff60dfff3.htm language=enus -->
## TOPIC 00137: rfmxspecandotnet/html/3fd14890-8d96-8343-68c7-625ff60dfff3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/3fd14890-8d96-8343-68c7-625ff60dfff3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/3fd14890-8d96-8343-68c7-625ff60dfff3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetUserDpdModel Method

RFmxSpecAnMXDpdApplyDpdSetUserDpdModel Method

SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput)

User

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUserDpdModel(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdUserDpdModel value
)
```

```text
Public Function SetUserDpdModel ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdApplyDpdUserDpdModel
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdUserDpdModel**
  - Contains a value that indicates the DPD model used to apply DPD when you set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDUserDPDModel() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/400ea52c-1c7d-1700-1d7f-85bd3d9a94aa.htm language=enus -->
## TOPIC 00138: rfmxspecandotnet/html/400ea52c-1c7d-1700-1d7f-85bd3d9a94aa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/400ea52c-1c7d-1700-1d7f-85bd3d9a94aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/400ea52c-1c7d-1700-1d7f-85bd3d9a94aa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.GetVbwFilterVbwToRbwRatio Method

RFmxSpecAnMXTxpConfigurationGetVbwFilterVbwToRbwRatio Method

SetVbwFilterAutoBandwidth(String, RFmxSpecAnMXTxpVbwFilterAutoBandwidth)

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetVbwFilterVbwToRbwRatio(
	string selectorString,
	out double value
)
```

```text
Public Function GetVbwFilterVbwToRbwRatio ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the VBW to RBW Ratio when you set the SetVbwFilterAutoBandwidth(String, RFmxSpecAnMXTxpVbwFilterAutoBandwidth) method to True.

###### Return Value

Int32

##### Remarks

TxpVbwFilterVbwToRbwRatio

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/40472318-4f82-ff33-72bc-ce09de55a1c7.htm language=enus -->
## TOPIC 00139: rfmxspecandotnet/html/40472318-4f82-ff33-72bc-ce09de55a1c7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/40472318-4f82-ff33-72bc-ce09de55a1c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/40472318-4f82-ff33-72bc-ce09de55a1c7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.SetCfrMaximumIterations Method

RFmxSpecAnMXDpdPreDpdSetCfrMaximumIterations Method

DpdPreDpdCfrEnabled

True

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCfrMaximumIterations(
	string selectorString,
	int value
)
```

```text
Public Function SetCfrMaximumIterations ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the maximum number of iterations required to converge waveform PAPR to target PAPR, when you set the DpdPreDpdCfrEnabled method to True.

###### Return Value

Int32

##### Remarks

DpdPreDpdCfrMaximumIterations

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/40863042-b725-a8a3-4e47-c8318a9eb941.htm language=enus -->
## TOPIC 00140: rfmxspecandotnet/html/40863042-b725-a8a3-4e47-c8318a9eb941.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/40863042-b725-a8a3-4e47-c8318a9eb941.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/40863042-b725-a8a3-4e47-c8318a9eb941.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerResults.FetchFunctionValue Method

RFmxSpecAnMXMarkerResultsFetchFunctionValue Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFunctionValue(
	string selectorString,
	out double functionValue
)
```

```text
Public Function FetchFunctionValue ( 
	selectorString As String,
	<OutAttribute> ByRef functionValue As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and marker number. Example:"marker0""result::r1/marker0" You can use the RFmxSpecAn_BuildMarkerString2 method to build the selector string.
- **functionValue Double**
  - Upon return, contains the value of the selected marker method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXMarkerResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/408ff53b-2f7c-7d4f-6bf2-402304c2b3e2.htm language=enus -->
## TOPIC 00141: rfmxspecandotnet/html/408ff53b-2f7c-7d4f-6bf2-402304c2b3e2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/408ff53b-2f7c-7d4f-6bf2-402304c2b3e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/408ff53b-2f7c-7d4f-6bf2-402304c2b3e2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerType Enumeration

RFmxSpecAnMXMarkerType Enumeration

Configures the marker type.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXMarkerType
```

```text
Public Enumeration RFmxSpecAnMXMarkerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Off | 0 | The marker is disabled. |
| Normal | 1 | The marker is enabled as a normal marker. |
| Delta | 3 | The marker is enabled as a delta marker. |
| Fixed | 4 |  |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/40a1850e-4ece-3067-2a5b-f297c9c29df6.htm language=enus -->
## TOPIC 00142: rfmxspecandotnet/html/40a1850e-4ece-3067-2a5b-f297c9c29df6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/40a1850e-4ece-3067-2a5b-f297c9c29df6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/40a1850e-4ece-3067-2a5b-f297c9c29df6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMResults.GetFundamentalLowerTonePower Method

RFmxSpecAnMXIMResultsGetFundamentalLowerTonePower Method

SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled)

True

False

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFundamentalLowerTonePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetFundamentalLowerTonePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(String)Â method to build the selectorString.
- **value Double**
  - Upon return, contains the peak power measured around the lower tone frequency when you set the SetLocalPeakSearchEnabled(String, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the lower tone frequency.

###### Return Value

Int32

##### Remarks

IMResultsFundamentalLowerTonePower

##### See Also

###### Reference

RFmxSpecAnMXIMResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/40af59c0-e2f3-10a8-3eef-b6d003d65e10.htm language=enus -->
## TOPIC 00143: rfmxspecandotnet/html/40af59c0-e2f3-10a8-3eef-b6d003d65e10.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/40af59c0-e2f3-10a8-3eef-b6d003d65e10.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/40af59c0-e2f3-10a8-3eef-b6d003d65e10.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetDutAverageInputPower Method

RFmxSpecAnMXAmpmConfigurationGetDutAverageInputPower Method

Gets the average power, in dBm, of the signal at the input port of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDutAverageInputPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetDutAverageInputPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the average power, in dBm, of the signal at the input port of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetDUTAverageInputPower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/40b77928-645f-1e39-4ccd-b6af30830090.htm language=enus -->
## TOPIC 00144: rfmxspecandotnet/html/40b77928-645f-1e39-4ccd-b6af30830090.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/40b77928-645f-1e39-4ccd-b6af30830090.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/40b77928-645f-1e39-4ccd-b6af30830090.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.GetCfrShapingThreshold Method

RFmxSpecAnMXDpdPreDpdGetCfrShapingThreshold Method

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
  - Upon return, contains the shaping threshold to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to the DPD concept topic for more information about shaping threshold.

###### Return Value

Int32

##### Remarks

DpdPreDpdCfrShapingThreshold

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/40cea40b-3108-43a5-8e81-f4c4d0bb2452.htm language=enus -->
## TOPIC 00145: rfmxspecandotnet/html/40cea40b-3108-43a5-8e81-f4c4d0bb2452.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/40cea40b-3108-43a5-8e81-f4c4d0bb2452.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/40cea40b-3108-43a5-8e81-f4c4d0bb2452.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetRangeAveragingCount Method

RFmxSpecAnMXPhaseNoiseConfigurationGetRangeAveragingCount Method

Gets the averaging count for the specified range.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeAveragingCount(
	string selectorString,
	out int value
)
```

```text
Public Function GetRangeAveragingCount ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the phasenoiserange number. Example: "phasenoiserange0". You can use the BuildRangeString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the averaging count for the specified range.

###### Return Value

Int32

##### Remarks

PhaseNoiseRangeAveragingCount

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4188e8e8-2b82-f088-0db2-cfd25a987bd8.htm language=enus -->
## TOPIC 00146: rfmxspecandotnet/html/4188e8e8-2b82-f088-0db2-cfd25a987bd8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4188e8e8-2b82-f088-0db2-cfd25a987bd8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4188e8e8-2b82-f088-0db2-cfd25a987bd8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetOffsetSideband Method

RFmxSpecAnMXAcpConfigurationGetOffsetSideband Method

Gets whether the offset segment is present on one side, or on both sides of the carriers.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetSideband(
	string selectorString,
	out RFmxSpecAnMXAcpOffsetSideband value
)
```

```text
Public Function GetOffsetSideband ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpOffsetSideband
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXAcpOffsetSideband**
  - Upon return, indicates whether the offset segment is present on one side, or on both sides of the carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetSideband() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4190e750-3197-37d8-efb6-733be005b589.htm language=enus -->
## TOPIC 00147: rfmxspecandotnet/html/4190e750-3197-37d8-efb6-733be005b589.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4190e750-3197-37d8-efb6-733be005b589.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4190e750-3197-37d8-efb6-733be005b589.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition Enumeration

RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition Enumeration

SetCarrierRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition
```

```text
Public Enumeration RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| BandwidthDefinition3dB | 0 | Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the SetCarrierRbwFilterType(String, RFmxSpecAnMXSemCarrierRbwFilterType) method to FftBased, RBW is the 3dB bandwidth of the window specified by the SetFftWindow(String, RFmxSpecAnMXSemFftWindow). |
| BandwidthDefinitionBinWidth | 2 | Defines the RBW in terms of the spectrum bin width computed using FFT when you set the SetCarrierRbwFilterType(String, RFmxSpecAnMXSemCarrierRbwFilterType) method to FftBased. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/41a9178f-f14b-bff4-4a7f-fdd991277dbf.htm language=enus -->
## TOPIC 00148: rfmxspecandotnet/html/41a9178f-f14b-bff4-4a7f-fdd991277dbf.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/41a9178f-f14b-bff4-4a7f-fdd991277dbf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/41a9178f-f14b-bff4-4a7f-fdd991277dbf.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.BuildSegmentString Method

RFmxSpecAnMXBuildSegmentString Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildSegmentString(
	string selectorString,
	int segmentNumber
)
```

```text
Public Shared Function BuildSegmentString ( 
	selectorString As String,
	segmentNumber As Integer
) As String
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **segmentNumber Int32**
  - Specifies the segment number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/41ae2c9a-d27a-198a-8f49-8bbe931f422f.htm language=enus -->
## TOPIC 00149: rfmxspecandotnet/html/41ae2c9a-d27a-198a-8f49-8bbe931f422f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/41ae2c9a-d27a-198a-8f49-8bbe931f422f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/41ae2c9a-d27a-198a-8f49-8bbe931f422f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetYFactorNoiseSourceLossFrequency Method

RFmxSpecAnMXNFConfigurationGetYFactorNoiseSourceLossFrequency Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetYFactorNoiseSourceLossFrequency(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetYFactorNoiseSourceLossFrequency ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the SetYFactorNoiseSourceLoss(String, Double) method. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

NFYFactorNoiseSourceLossFrequency

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/41d85077-0577-c453-5a98-1de1a86917fa.htm language=enus -->
## TOPIC 00150: rfmxspecandotnet/html/41d85077-0577-c453-5a98-1de1a86917fa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/41d85077-0577-c453-5a98-1de1a86917fa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/41d85077-0577-c453-5a98-1de1a86917fa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXList.DeleteList Method

RFmxSpecAnMXListDeleteList Method

Deletes the current instance of a list.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

##### Remarks

This method maps to the RFmxSpecAn_DeleteList() function in C.

##### See Also

###### Reference

RFmxSpecAnMXList Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4201d4e6-edc0-59fd-6146-3258382dbaa7.htm language=enus -->
## TOPIC 00151: rfmxspecandotnet/html/4201d4e6-edc0-59fd-6146-3258382dbaa7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4201d4e6-edc0-59fd-6146-3258382dbaa7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4201d4e6-edc0-59fd-6146-3258382dbaa7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetPowerUnits Method

RFmxSpecAnMXAcpConfigurationGetPowerUnits Method

Gets the adjacent channel power (ACP) power units.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPowerUnits(
	string selectorString,
	out RFmxSpecAnMXAcpPowerUnits value
)
```

```text
Public Function GetPowerUnits ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpPowerUnits
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpPowerUnits**
  - Upon return, contains the ACP power units.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetPowerUnits() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/428a1ca4-7af4-a8ae-18b2-d29d381d72b3.htm language=enus -->
## TOPIC 00152: rfmxspecandotnet/html/428a1ca4-7af4-a8ae-18b2-d29d381d72b3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/428a1ca4-7af4-a8ae-18b2-d29d381d72b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/428a1ca4-7af4-a8ae-18b2-d29d381d72b3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.ConfigureColdSourceInputTermination Method

RFmxSpecAnMXNFConfigurationConfigureColdSourceInputTermination Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureColdSourceInputTermination(
	string selectorString,
	double[] terminationVswr,
	double[] terminationVswrFrequency,
	double terminationTemperature
)
```

```text
Public Function ConfigureColdSourceInputTermination ( 
	selectorString As String,
	terminationVswr As Double(),
	terminationVswrFrequency As Double(),
	terminationTemperature As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **terminationVswr Double**
  - Specifies an array of voltage standing wave ratios (VSWR) as a method of frequency of the microwave termination used as the noise source in cold source method. The corresponding array of frequencies is specified by the terminationVSWRFrequency parameter. In most cases, the exact VSWR of the microwave termination may not be known. Hence, NI recommends that you set this parameter to an empty array, in which case the noise figure (NF) measurement assumes that the VSWR of the microwave termination is unity for all frequencies.
- **terminationVswrFrequency Double**
  - Specifies an array of frequencies corresponding to the VSWRs of the microwave termination used in the cold source method as specified by the terminationVSWR parameter. This value is expressed in Hz.
- **terminationTemperature Double**
  - Specifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/42d87fae-8c1b-9c3c-c77f-25f08f8a41fd.htm language=enus -->
## TOPIC 00153: rfmxspecandotnet/html/42d87fae-8c1b-9c3c-c77f-25f08f8a41fd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/42d87fae-8c1b-9c3c-c77f-25f08f8a41fd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/42d87fae-8c1b-9c3c-c77f-25f08f8a41fd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.GetAutoLevelInitialReferenceLevel Method

RFmxSpecAnMXGetAutoLevelInitialReferenceLevel Method

Gets the initial reference level, in dBm, which the auto level function uses to estimate the peak power of the input signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the initial reference level, in dBm, which the auto level function uses to estimate the peak power of the input signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_GetAutoLevelInitialReferenceLevel() function in C.

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/42e6f0c9-cedc-a1d8-efb4-520d91d5401b.htm language=enus -->
## TOPIC 00154: rfmxspecandotnet/html/42e6f0c9-cedc-a1d8-efb4-520d91d5401b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/42e6f0c9-cedc-a1d8-efb4-520d91d5401b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/42e6f0c9-cedc-a1d8-efb4-520d91d5401b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetCarrierRrcFilterEnabled Method

RFmxSpecAnMXSemConfigurationSetCarrierRrcFilterEnabled Method

Sets whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel after measuring the carrier channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCarrierRrcFilterEnabled(
	string selectorString,
	RFmxSpecAnMXSemCarrierRrcFilterEnabled value
)
```

```text
Public Function SetCarrierRrcFilterEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXSemCarrierRrcFilterEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemCarrierRrcFilterEnabled**
  - Specifies whether to apply the RRC filter on the acquired carrier channel after measuring the carrier channel power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetCarrierRRCFilterEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/430011d7-3f78-52de-b9cf-6e1c7f6728f0.htm language=enus -->
## TOPIC 00155: rfmxspecandotnet/html/430011d7-3f78-52de-b9cf-6e1c7f6728f0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/430011d7-3f78-52de-b9cf-6e1c7f6728f0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/430011d7-3f78-52de-b9cf-6e1c7f6728f0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNF.Configuration Property

RFmxSpecAnMXNFConfiguration Property

RFmxSpecAnMXNFConfiguration

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXNFConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxSpecAnMXNFConfiguration
	Get
```

###### Property Value

RFmxSpecAnMXNFConfiguration

##### See Also

###### Reference

RFmxSpecAnMXNF Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/431c6931-1246-e58b-aa83-7f6d03a9be80.htm language=enus -->
## TOPIC 00156: rfmxspecandotnet/html/431c6931-1246-e58b-aa83-7f6d03a9be80.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/431c6931-1246-e58b-aa83-7f6d03a9be80.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/431c6931-1246-e58b-aa83-7f6d03a9be80.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetFrequencyList Method

RFmxSpecAnMXNFConfigurationGetFrequencyList Method

Gets the list of frequencies at which the noise figure (NF) of the DUT is computed. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyList(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetFrequencyList ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the list of frequencies at which the noise figure (NF) of the DUT is computed. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

NFFrequencyList

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/433259c0-4259-4141-a53d-90a4912899b6.htm language=enus -->
## TOPIC 00157: rfmxspecandotnet/html/433259c0-4259-4141-a53d-90a4912899b6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/433259c0-4259-4141-a53d-90a4912899b6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/433259c0-4259-4141-a53d-90a4912899b6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.ConfigureSweepTime Method

RFmxSpecAnMXObwConfigurationConfigureSweepTime Method

Configures the sweep time.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSweepTime(
	string selectorString,
	RFmxSpecAnMXObwSweepTimeAuto sweepTimeAuto,
	double sweepTimeInterval
)
```

```text
Public Function ConfigureSweepTime ( 
	selectorString As String,
	sweepTimeAuto As RFmxSpecAnMXObwSweepTimeAuto,
	sweepTimeInterval As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sweepTimeAuto RFmxSpecAnMXObwSweepTimeAuto**
  - Specifies whether the measurement computes the sweep time.
- **sweepTimeInterval Double**
  - Specifies the sweep time, in seconds, when you set the SetSweepTimeAuto(String, RFmxSpecAnMXObwSweepTimeAuto) method to False.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWCfgSweepTime() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/433697e5-10f8-bda9-5451-1fe0d48d47fa.htm language=enus -->
## TOPIC 00158: rfmxspecandotnet/html/433697e5-10f8-bda9-5451-1fe0d48d47fa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/433697e5-10f8-bda9-5451-1fe0d48d47fa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/433697e5-10f8-bda9-5451-1fe0d48d47fa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetIntegratedNoiseStopFrequency Method

RFmxSpecAnMXPhaseNoiseConfigurationSetIntegratedNoiseStopFrequency Method

Sets an array of the stop offset frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIntegratedNoiseStopFrequency(
	string selectorString,
	double[] value
)
```

```text
Public Function SetIntegratedNoiseStopFrequency ( 
	selectorString As String,
	value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies an array of the stop frequencies for integrated noise measurement when you set the PhaseNoise Integrated Noise Range Definition method to Custom.

###### Return Value

Int32

##### Remarks

PhaseNoiseIntegratedNoiseStopFrequency

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/436e16a3-cad3-8fc1-4011-e6fa3b8b8b50.htm language=enus -->
## TOPIC 00159: rfmxspecandotnet/html/436e16a3-cad3-8fc1-4011-e6fa3b8b8b50.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/436e16a3-cad3-8fc1-4011-e6fa3b8b8b50.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/436e16a3-cad3-8fc1-4011-e6fa3b8b8b50.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureOffsetRelativeAttenuation Method

RFmxSpecAnMXSemConfigurationConfigureOffsetRelativeAttenuation Method

Configures the attenuation, in dB, relative to the external attenuation. Use this method to compensate for variations in external attenuation when the offset channels are spread wide in frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetRelativeAttenuation(
	string selectorString,
	double relativeAttenuation
)
```

```text
Public Function ConfigureOffsetRelativeAttenuation ( 
	selectorString As String,
	relativeAttenuation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **relativeAttenuation Double**
  - Specifies the attenuation, in dB, relative to the external attenuation.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetRelativeAttenuation() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/438b2aa1-5fe8-d1de-a1b3-22b61be86dc1.htm language=enus -->
## TOPIC 00160: rfmxspecandotnet/html/438b2aa1-5fe8-d1de-a1b3-22b61be86dc1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/438b2aa1-5fe8-d1de-a1b3-22b61be86dc1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/438b2aa1-5fe8-d1de-a1b3-22b61be86dc1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurResults.GetRangeSpurAbsoluteLimit Method

RFmxSpecAnMXSpurResultsGetRangeSpurAbsoluteLimit Method

Gets the threshold, in dBm, used to calculate the margin of the detected spurious emission (Spur).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRangeSpurAbsoluteLimit(
	string selectorString,
	out double value
)
```

```text
Public Function GetRangeSpurAbsoluteLimit ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name, range number and spur number. Example: "range0/spur0","result::r1/range0/spur0". You can use the BuildSpurString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the threshold, in dBm, used to calculate the margin of the detected Spur.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetResultsRangeAbsoluteLimit() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/43be2f95-2d74-50a4-3a3b-88c38b90e170.htm language=enus -->
## TOPIC 00161: rfmxspecandotnet/html/43be2f95-2d74-50a4-3a3b-88c38b90e170.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/43be2f95-2d74-50a4-3a3b-88c38b90e170.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/43be2f95-2d74-50a4-3a3b-88c38b90e170.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.GetRbwPercentage Method

RFmxSpecAnMXPhaseNoiseConfigurationGetRbwPercentage Method

Gets the RBW as a percentage of the start frequency of each subrange when you set the Phase Noise Range Definition property to Auto.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwPercentage(
	string selectorString,
	out double value
)
```

```text
Public Function GetRbwPercentage ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the RBW as a percentage of the start frequency of each subrange when you set the PhaseNoise Range Definition method to Auto.

###### Return Value

Int32

##### Remarks

PhaseNoiseRbwPercentage

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/43d7dcbf-b05a-2567-20da-16c9bc774048.htm language=enus -->
## TOPIC 00162: rfmxspecandotnet/html/43d7dcbf-b05a-2567-20da-16c9bc774048.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/43d7dcbf-b05a-2567-20da-16c9bc774048.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/43d7dcbf-b05a-2567-20da-16c9bc774048.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.SetMeasurementSampleRate Method

RFmxSpecAnMXIdpdConfigurationSetMeasurementSampleRate Method

SetMeasurementSampleRateMode(String, RFmxSpecAnMXIdpdMeasurementSampleRateMode)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementSampleRate(
	string selectorString,
	double value
)
```

```text
Public Function SetMeasurementSampleRate ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the acquisition sample rate, in S/s, when you set the SetMeasurementSampleRateMode(String, RFmxSpecAnMXIdpdMeasurementSampleRateMode) is User.

###### Return Value

Int32

##### Remarks

IdpdMeasurementSampleRate

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/43d86e03-375a-5909-75c4-d19eadf4f543.htm language=enus -->
## TOPIC 00163: rfmxspecandotnet/html/43d86e03-375a-5909-75c4-d19eadf4f543.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/43d86e03-375a-5909-75c4-d19eadf4f543.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/43d86e03-375a-5909-75c4-d19eadf4f543.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntConfiguration.SetAveragingType Method

RFmxSpecAnMXFcntConfigurationSetAveragingType Method

Sets the averaging type for frequency count (Fcnt) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxSpecAnMXFcntAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxSpecAnMXFcntAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXFcntAveragingType**
  - Specifies the averaging type for Fcnt measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntSetAveragingType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44105700-ec17-5970-c0c1-67cd21aa8609.htm language=enus -->
## TOPIC 00164: rfmxspecandotnet/html/44105700-ec17-5970-c0c1-67cd21aa8609.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44105700-ec17-5970-c0c1-67cd21aa8609.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44105700-ec17-5970-c0c1-67cd21aa8609.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth Enumeration

RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth Enumeration

Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth
```

```text
Public Enumeration RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Specify the video bandwidth in the Spectrum VBW method. The SetVbwFilterVbwToRbwRatio(String, Double) method is disregarded in this mode. |
| True | 1 | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the SetVbwFilterVbwToRbwRatio(String, Double) method and the Spectrum RBW method. The value of the Spectrum VBW method is disregarded in this mode. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4419d86b-0e65-f743-e2ba-c16a24d356fb.htm language=enus -->
## TOPIC 00165: rfmxspecandotnet/html/4419d86b-0e65-f743-e2ba-c16a24d356fb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4419d86b-0e65-f743-e2ba-c16a24d356fb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4419d86b-0e65-f743-e2ba-c16a24d356fb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetColdSourceDutS22 Method

RFmxSpecAnMXNFConfigurationGetColdSourceDutS22 Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetColdSourceDutS22(
	string selectorString,
	ref double[] value
)
```

```text
Public Function GetColdSourceDutS22 ( 
	selectorString As String,
	ByRef value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains an array of the output-reflections of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the SetColdSourceDutSParametersFrequency(String, Double) method.

###### Return Value

Int32

##### Remarks

NFColdSourceDutS22

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/442c8264-edae-2570-dbc3-b4c5461091b0.htm language=enus -->
## TOPIC 00166: rfmxspecandotnet/html/442c8264-edae-2570-dbc3-b4c5461091b0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/442c8264-edae-2570-dbc3-b4c5461091b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/442c8264-edae-2570-dbc3-b4c5461091b0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetMeasurementEnabled Method

RFmxSpecAnMXSpurConfigurationGetMeasurementEnabled Method

Gets whether to enable spurious emission (Spur) measurement.

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
  - if Spur measurement is enabled; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurGetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/443b2c91-a8b3-0463-b8a4-7add8f18391b.htm language=enus -->
## TOPIC 00167: rfmxspecandotnet/html/443b2c91-a8b3-0463-b8a4-7add8f18391b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/443b2c91-a8b3-0463-b8a4-7add8f18391b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/443b2c91-a8b3-0463-b8a4-7add8f18391b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerResults Class

RFmxSpecAnMXMarkerResults Class

Provides methods to fetch and read the Marker measurement results.

##### Inheritance Hierarchy

RFmxSpecAnMXSubObject

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxSpecAnMXMarkerResults : RFmxSpecAnMXSubObject
```

```text
Public NotInheritable Class RFmxSpecAnMXMarkerResults
	Inherits RFmxSpecAnMXSubObject
```

The RFmxSpecAnMXMarkerResults type exposes the following members.

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

##### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/444a3a68-2c3c-4e00-09a6-205a19a05264.htm language=enus -->
## TOPIC 00168: rfmxspecandotnet/html/444a3a68-2c3c-4e00-09a6-205a19a05264.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/444a3a68-2c3c-4e00-09a6-205a19a05264.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/444a3a68-2c3c-4e00-09a6-205a19a05264.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.ConfigureBandwidth Method

RFmxSpecAnMXIQConfigurationConfigureBandwidth Method

Configures the bandwidth, in hertz (Hz), for the I/Q measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureBandwidth(
	string selectorString,
	RFmxSpecAnMXIQBandwidthAuto bandwidthAuto,
	double bandwidth
)
```

```text
Public Function ConfigureBandwidth ( 
	selectorString As String,
	bandwidthAuto As RFmxSpecAnMXIQBandwidthAuto,
	bandwidth As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **bandwidthAuto RFmxSpecAnMXIQBandwidthAuto**
  - Specifies whether the measurement computes the minimum acquisition bandwidth.
- **bandwidth Double**
  - Specifies the minimum acquisition bandwidth, in hertz (Hz), when you set the bandwidthAuto parameter to False.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQCfgBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44505d08-b426-e61b-7181-a97b1109883e.htm language=enus -->
## TOPIC 00169: rfmxspecandotnet/html/44505d08-b426-e61b-7181-a97b1109883e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44505d08-b426-e61b-7181-a97b1109883e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44505d08-b426-e61b-7181-a97b1109883e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetAveragingEnabled Method

RFmxSpecAnMXAmpmConfigurationGetAveragingEnabled Method

Gets whether averaging is enabled for the AMPM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxSpecAnMXAmpmAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmAveragingEnabled**
  - Upon return, contains a value that indicates whether averaging is enabled for the AMPM measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44755d2e-5547-08f7-6c2a-9d9fcc2c5f8c.htm language=enus -->
## TOPIC 00170: rfmxspecandotnet/html/44755d2e-5547-08f7-6c2a-9d9fcc2c5f8c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44755d2e-5547-08f7-6c2a-9d9fcc2c5f8c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44755d2e-5547-08f7-6c2a-9d9fcc2c5f8c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.SetSegmentMeasurementOffset Method

RFmxSpecAnMXPavtConfigurationSetSegmentMeasurementOffset Method

SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode)

Variable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentMeasurementOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetSegmentMeasurementOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.

###### Return Value

Int32

##### Remarks

PavtSegmentMeasurementOffset

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44a7bb75-87a5-a112-778f-511db61aa527.htm language=enus -->
## TOPIC 00171: rfmxspecandotnet/html/44a7bb75-87a5-a112-778f-511db61aa527.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44a7bb75-87a5-a112-778f-511db61aa527.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44a7bb75-87a5-a112-778f-511db61aa527.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpResults.GetPeakToAverageRatio Method

RFmxSpecAnMXTxpResultsGetPeakToAverageRatio Method

Gets the ratio of the peak power of the signal to the mean power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakToAverageRatio(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakToAverageRatio ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the ratio of the peak power of the signal to the mean power.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPGetResultsPeaktoAverageRatio() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44a8bc42-8584-6c09-3d3a-cf381bbd35ce.htm language=enus -->
## TOPIC 00172: rfmxspecandotnet/html/44a8bc42-8584-6c09-3d3a-cf381bbd35ce.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44a8bc42-8584-6c09-3d3a-cf381bbd35ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44a8bc42-8584-6c09-3d3a-cf381bbd35ce.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetLookupTableThresholdEnabled Method

RFmxSpecAnMXDpdConfigurationGetLookupTableThresholdEnabled Method

Gets whether to enable thresholding of the acquired samples to be used for the DPD measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLookupTableThresholdEnabled(
	string selectorString,
	out RFmxSpecAnMXDpdLookupTableThresholdEnabled value
)
```

```text
Public Function GetLookupTableThresholdEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdLookupTableThresholdEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdLookupTableThresholdEnabled**
  - Upon return, contains a value that indicates whether to enable thresholding of the acquired samples to be used for the DPD measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableThresholdEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44ad8341-2fd6-f9b1-07f8-86a06d17f907.htm language=enus -->
## TOPIC 00173: rfmxspecandotnet/html/44ad8341-2fd6-f9b1-07f8-86a06d17f907.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44ad8341-2fd6-f9b1-07f8-86a06d17f907.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44ad8341-2fd6-f9b1-07f8-86a06d17f907.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.GetYFactorNoiseSourceSettlingTime Method

RFmxSpecAnMXNFConfigurationGetYFactorNoiseSourceSettlingTime Method

Gets the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetYFactorNoiseSourceSettlingTime(
	string selectorString,
	out double value
)
```

```text
Public Function GetYFactorNoiseSourceSettlingTime ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

NFYFactorNoiseSourceSettlingTime

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/44e199e4-6061-e6f5-2aa5-feec8dd75d77.htm language=enus -->
## TOPIC 00174: rfmxspecandotnet/html/44e199e4-6061-e6f5-2aa5-feec8dd75d77.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/44e199e4-6061-e6f5-2aa5-feec8dd75d77.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/44e199e4-6061-e6f5-2aa5-feec8dd75d77.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetRbwFilterType Method

RFmxSpecAnMXSemConfigurationSetOffsetRbwFilterType Method

Sets the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetRbwFilterType(
	string selectorString,
	RFmxSpecAnMXSemOffsetRbwFilterType value
)
```

```text
Public Function SetOffsetRbwFilterType ( 
	selectorString As String,
	value As RFmxSpecAnMXSemOffsetRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetRBWFilterType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/450c278d-0087-3365-5615-c47c68c8ccf0.htm language=enus -->
## TOPIC 00175: rfmxspecandotnet/html/450c278d-0087-3365-5615-c47c68c8ccf0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/450c278d-0087-3365-5615-c47c68c8ccf0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/450c278d-0087-3365-5615-c47c68c8ccf0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetNumberOfCarriers Method

RFmxSpecAnMXAcpConfigurationGetNumberOfCarriers Method

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
  - Upon return, contains the number of carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPGetNumberOfCarriers() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/46bf3cea-fc33-c12d-ac7b-82c6ddafb1f3.htm language=enus -->
## TOPIC 00176: rfmxspecandotnet/html/46bf3cea-fc33-c12d-ac7b-82c6ddafb1f3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/46bf3cea-fc33-c12d-ac7b-82c6ddafb1f3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/46bf3cea-fc33-c12d-ac7b-82c6ddafb1f3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.FetchCompressionPoints Method

RFmxSpecAnMXAmpmResultsFetchCompressionPoints Method

Fetches the compression points.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCompressionPoints(
	string selectorString,
	double timeout,
	ref double[] inputCompressionPoint,
	ref double[] outputCompressionPoint
)
```

```text
Public Function FetchCompressionPoints ( 
	selectorString As String,
	timeout As Double,
	ByRef inputCompressionPoint As Double(),
	ByRef outputCompressionPoint As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **inputCompressionPoint Double**
  - Returns the theoretical input power, in dBm, at which device gain drops by the compression level, specified through AMPM Compression Point Level (dB) property, from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute.
- **outputCompressionPoint Double**
  - Returns the theoretical output power, in dBm, at which device gain drops by the compression level, specified through AMPM Compression Point Level (dB) property, from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/481d6642-1204-ccbc-1fda-b494cb0be508.htm language=enus -->
## TOPIC 00177: rfmxspecandotnet/html/481d6642-1204-ccbc-1fda-b494cb0be508.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/481d6642-1204-ccbc-1fda-b494cb0be508.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/481d6642-1204-ccbc-1fda-b494cb0be508.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetMeasurementMethod Method

RFmxSpecAnMXSpectrumConfigurationSetMeasurementMethod Method

Sets the method for performing the Spectrum measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementMethod(
	string selectorString,
	RFmxSpecAnMXSpectrumMeasurementMethod value
)
```

```text
Public Function SetMeasurementMethod ( 
	selectorString As String,
	value As RFmxSpecAnMXSpectrumMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumMeasurementMethod**
  - Specifies the method for performing the Spectrum measurement.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/48e59a9a-9090-3cfd-bdb4-48e42fe65ee0.htm language=enus -->
## TOPIC 00178: rfmxspecandotnet/html/48e59a9a-9090-3cfd-bdb4-48e42fe65ee0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/48e59a9a-9090-3cfd-bdb4-48e42fe65ee0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/48e59a9a-9090-3cfd-bdb4-48e42fe65ee0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetCarrierBandwidth Method

RFmxSpecAnMXDpdConfigurationSetCarrierBandwidth Method

SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled)

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
  - Specifies the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

DpdCarrierBandwidth

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/490c2127-abb9-e4ac-26c8-c72cc1dafdcf.htm language=enus -->
## TOPIC 00179: rfmxspecandotnet/html/490c2127-abb9-e4ac-26c8-c72cc1dafdcf.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/490c2127-abb9-e4ac-26c8-c72cc1dafdcf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/490c2127-abb9-e4ac-26c8-c72cc1dafdcf.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.GetMeasurementMode Method

RFmxSpecAnMXChpConfigurationGetMeasurementMode Method

Gets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementMode(
	string selectorString,
	out RFmxSpecAnMXChpMeasurementMode value
)
```

```text
Public Function GetMeasurementMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXChpMeasurementMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpMeasurementMode**
  - Upon return, contains whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

###### Return Value

Int32

##### Remarks

ChpMeasurementMode

Measure

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/490db4f1-282c-c71c-b5e5-80730133cbc7.htm language=enus -->
## TOPIC 00180: rfmxspecandotnet/html/490db4f1-282c-c71c-b5e5-80730133cbc7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/490db4f1-282c-c71c-b5e5-80730133cbc7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/490db4f1-282c-c71c-b5e5-80730133cbc7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.ConfigureThreshold Method

RFmxSpecAnMXAmpmConfigurationConfigureThreshold Method

Configures the threshold level for the samples that need to be considered for the AMPM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureThreshold(
	string selectorString,
	RFmxSpecAnMXAmpmThresholdEnabled thresholdEnabled,
	double thresholdLevel,
	RFmxSpecAnMXAmpmThresholdType thresholdType
)
```

```text
Public Function ConfigureThreshold ( 
	selectorString As String,
	thresholdEnabled As RFmxSpecAnMXAmpmThresholdEnabled,
	thresholdLevel As Double,
	thresholdType As RFmxSpecAnMXAmpmThresholdType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **thresholdEnabled RFmxSpecAnMXAmpmThresholdEnabled**
  - Specifies whether to enable thresholding of the acquired samples to be used for the measurement.
- **thresholdLevel Double**
  - Specifies either the relative or absolute threshold power level based on the value of the thresholdType parameter.
- **thresholdType RFmxSpecAnMXAmpmThresholdType**
  - Specifies the reference for the power level used for thresholding.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMCfgThreshold() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/49e017d6-eb27-a319-3a58-51688520958c.htm language=enus -->
## TOPIC 00181: rfmxspecandotnet/html/49e017d6-eb27-a319-3a58-51688520958c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/49e017d6-eb27-a319-3a58-51688520958c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/49e017d6-eb27-a319-3a58-51688520958c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetMeasurementSampleRateMode Method

RFmxSpecAnMXAmpmConfigurationGetMeasurementSampleRateMode Method

Gets whether the acquisition sample rate is based on the reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementSampleRateMode(
	string selectorString,
	out RFmxSpecAnMXAmpmMeasurementSampleRateMode value
)
```

```text
Public Function GetMeasurementSampleRateMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmMeasurementSampleRateMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmMeasurementSampleRateMode**
  - Upon return, contains a value that indicates whether the acquisition sample rate is based on the reference waveform.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetMeasurementSampleRateMode() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4a35b190-3578-296e-caec-16942ac7dbe3.htm language=enus -->
## TOPIC 00182: rfmxspecandotnet/html/4a35b190-3578-296e-caec-16942ac7dbe3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4a35b190-3578-296e-caec-16942ac7dbe3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4a35b190-3578-296e-caec-16942ac7dbe3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetCarrierRrcFilterAlpha Method

RFmxSpecAnMXChpConfigurationSetCarrierRrcFilterAlpha Method

Sets the roll-off factor for the root-raised-cosine (RRC) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCarrierRrcFilterAlpha(
	string selectorString,
	double value
)
```

```text
Public Function SetCarrierRrcFilterAlpha ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the roll-off factor for the RRC filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetCarrierRRCFilterAlpha() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4a5ccbce-2146-ab74-cb1d-a73ea6c37a2b.htm language=enus -->
## TOPIC 00183: rfmxspecandotnet/html/4a5ccbce-2146-ab74-cb1d-a73ea6c37a2b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4a5ccbce-2146-ab74-cb1d-a73ea6c37a2b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4a5ccbce-2146-ab74-cb1d-a73ea6c37a2b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.SetListStepTimerOffset Method

RFmxSpecAnMXSetListStepTimerOffset Method

SetDigitalEdgeTriggerSource(String, String)

TimerEvent

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetListStepTimerOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetListStepTimerOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the time offset from the start of the step for which the measurements are computed. This value is expressed in seconds. This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent.

###### Return Value

Int32

##### Remarks

ListStepTimerOffset

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4a73333f-fc58-5f1e-12a5-4e1912c8b669.htm language=enus -->
## TOPIC 00184: rfmxspecandotnet/html/4a73333f-fc58-5f1e-12a5-4e1912c8b669.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4a73333f-fc58-5f1e-12a5-4e1912c8b669.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4a73333f-fc58-5f1e-12a5-4e1912c8b669.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetCfrWindowLength Method

RFmxSpecAnMXDpdApplyDpdSetCfrWindowLength Method

DpdApplyDpdCfrEnabled

True

DpdApplyDpdCfrMethod

PeakWindowing

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCfrWindowLength(
	string selectorString,
	int value
)
```

```text
Public Function SetCfrWindowLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the maximum window length to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing.

###### Return Value

Int32

##### Remarks

DpdApplyDpdCfrWindowLength

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4ae78eff-011e-071e-6870-db61d5739857.htm language=enus -->
## TOPIC 00185: rfmxspecandotnet/html/4ae78eff-011e-071e-6870-db61d5739857.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4ae78eff-011e-071e-6870-db61d5739857.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4ae78eff-011e-071e-6870-db61d5739857.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.GetNumberOfRecords Method

RFmxSpecAnMXIQConfigurationGetNumberOfRecords Method

Gets the the number of records to acquire.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfRecords(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfRecords ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of records to acquire.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQGetNumberOfRecords() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4b2ef065-2d14-1f57-2d34-6364a3687012.htm language=enus -->
## TOPIC 00186: rfmxspecandotnet/html/4b2ef065-2d14-1f57-2d34-6364a3687012.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4b2ef065-2d14-1f57-2d34-6364a3687012.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4b2ef065-2d14-1f57-2d34-6364a3687012.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMX.BuildRangeSpurString Method

RFmxSpecAnMXBuildRangeSpurString Method

**Note: This API is now obsolete.**

Creates the selector string for use with Spurious emissions (Spur) measurement results or fetch methods.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("Use BuildRangeString2 followed by BuildSpurString2 instead.")]
public static string BuildRangeSpurString(
	string resultName,
	int rangeNumber,
	int spurNumber
)
```

```text
<ObsoleteAttribute("Use BuildRangeString2 followed by BuildSpurString2 instead.")>
Public Shared Function BuildRangeSpurString ( 
	resultName As String,
	rangeNumber As Integer,
	spurNumber As Integer
) As String
```

###### Parameters

- **resultName String**
  - Specifies the name of the result. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. An empty string refers to the default result instance.
- **rangeNumber Int32**
  - Specifies the range number.
- **spurNumber Int32**
  - Specifies the Spur number.

###### Return Value

String

##### See Also

###### Reference

RFmxSpecAnMX Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4b411210-8fbc-f465-3543-6ae877bc0e0c.htm language=enus -->
## TOPIC 00187: rfmxspecandotnet/html/4b411210-8fbc-f465-3543-6ae877bc0e0c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4b411210-8fbc-f465-3543-6ae877bc0e0c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4b411210-8fbc-f465-3543-6ae877bc0e0c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetBandwidthIntegral Method

RFmxSpecAnMXSemConfigurationSetOffsetBandwidthIntegral Method

Sets the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW).

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetBandwidthIntegral(
	string selectorString,
	int value
)
```

```text
Public Function SetOffsetBandwidthIntegral ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value Int32**
  - Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetBandwidthIntegral() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4c98bb4c-eeb5-7c12-e025-40ada4fd2dbe.htm language=enus -->
## TOPIC 00188: rfmxspecandotnet/html/4c98bb4c-eeb5-7c12-e025-40ada4fd2dbe.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4c98bb4c-eeb5-7c12-e025-40ada4fd2dbe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4c98bb4c-eeb5-7c12-e025-40ada4fd2dbe.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetYFactorNoiseSourceLossCompensationEnabled Method

RFmxSpecAnMXNFConfigurationSetYFactorNoiseSourceLossCompensationEnabled Method

Sets whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetYFactorNoiseSourceLossCompensationEnabled(
	string selectorString,
	RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled value
)
```

```text
Public Function SetYFactorNoiseSourceLossCompensationEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled**
  - Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps.

###### Return Value

Int32

##### Remarks

NFYFactorNoiseSourceLossCompensationEnabled

False

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4d07a1f5-b5ba-b237-7540-d2481974751b.htm language=enus -->
## TOPIC 00189: rfmxspecandotnet/html/4d07a1f5-b5ba-b237-7540-d2481974751b.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4d07a1f5-b5ba-b237-7540-d2481974751b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4d07a1f5-b5ba-b237-7540-d2481974751b.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetAutoCarrierDetectionEnabled Method

RFmxSpecAnMXAmpmConfigurationGetAutoCarrierDetectionEnabled Method

Gets if auto detection of carrier offset and carrier bandwidth is enabled.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoCarrierDetectionEnabled(
	string selectorString,
	out RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled value
)
```

```text
Public Function GetAutoCarrierDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled**
  - Upon return, contains if auto detection of carrier offset and carrier bandwidth is enabled.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4d418573-df79-cf75-72f6-a29e4db10f65.htm language=enus -->
## TOPIC 00190: rfmxspecandotnet/html/4d418573-df79-cf75-72f6-a29e4db10f65.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4d418573-df79-cf75-72f6-a29e4db10f65.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4d418573-df79-cf75-72f6-a29e4db10f65.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemResults.FetchCarrierMeasurement Method

RFmxSpecAnMXSemResultsFetchCarrierMeasurement Method

Fetches the carrier power measurement.

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
	out double peakAbsolutePower,
	out double peakFrequency,
	out double totalRelativePower
)
```

```text
Public Function FetchCarrierMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef absolutePower As Double,
	<OutAttribute> ByRef peakAbsolutePower As Double,
	<OutAttribute> ByRef peakFrequency As Double,
	<OutAttribute> ByRef totalRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absolutePower Double**
  - Upon return, contains the carrier power. The power is measured in dBm when you set the RFmxSpecAnMXSemPowerUnits method to dBm, and in dBm/Hz when you set the RFmxSpecAnMXSemPowerUnits method to dBmPerHertz.
- **peakAbsolutePower Double**
  - Upon return, contains the peak power in the carrier channel. The power is measured in dBm when you set the RFmxSpecAnMXSemPowerUnits method to dBm, and in dBm/Hz when you set the RFmxSpecAnMXSemPowerUnits method to dBmPerHertz.
- **peakFrequency Double**
  - Upon return, contains the frequency, in hertz (Hz), at which the peak power occurs in the carrier channel.
- **totalRelativePower Double**
  - Upon return, contains the carrier power, in dB, relative to the total carrier power of all enabled carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMFetchCarrierMeasurement() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4d537349-0e02-6313-643c-e20b97e5956a.htm language=enus -->
## TOPIC 00191: rfmxspecandotnet/html/4d537349-0e02-6313-643c-e20b97e5956a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4d537349-0e02-6313-643c-e20b97e5956a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4d537349-0e02-6313-643c-e20b97e5956a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmResults.Read Method

RFmxSpecAnMXHarmResultsRead Method

Configures hardware for acquisition, performs measurement on acquired data, and returns Harmonics measurement results.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int Read(
	string selectorString,
	double timeout,
	out double totalHarmonicDistortion,
	out double averageFundamentalPower
)
```

```text
Public Function Read ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef totalHarmonicDistortion As Double,
	<OutAttribute> ByRef averageFundamentalPower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **totalHarmonicDistortion Double**
  - Upon return, contains the total harmonics distortion (THD), measured as a percentage of the power in the fundamental signal. THD calculation involves only the harmonics that are enabled.
- **averageFundamentalPower Double**
  - Upon return, contains the average power, in dBm, measured at the fundamental frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmRead() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4e34907a-aad6-936c-afec-fc42b33af895.htm language=enus -->
## TOPIC 00192: rfmxspecandotnet/html/4e34907a-aad6-936c-afec-fc42b33af895.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4e34907a-aad6-936c-afec-fc42b33af895.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4e34907a-aad6-936c-afec-fc42b33af895.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.SetSpan Method

RFmxSpecAnMXSpectrumConfigurationSetSpan Method

Sets the frequency range, in hertz (Hz), around the center frequency to be acquired for the measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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
  - Specifies the frequency range, in hertz (Hz), around the center frequency to be acquired for the measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpectrumSetSpan() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4eceb68e-554b-418e-67e1-1b1b82ba7f48.htm language=enus -->
## TOPIC 00193: rfmxspecandotnet/html/4eceb68e-554b-418e-67e1-1b1b82ba7f48.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4eceb68e-554b-418e-67e1-1b1b82ba7f48.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4eceb68e-554b-418e-67e1-1b1b82ba7f48.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.ConfigureThreshold Method

RFmxSpecAnMXTxpConfigurationConfigureThreshold Method

Configures the threshold level for the samples that need to be considered for the transmit power (TXP) measurement. Enable the threshold when analyzing burst signals or signals with dead time.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureThreshold(
	string selectorString,
	RFmxSpecAnMXTxpThresholdEnabled thresholdEnabled,
	double thresholdLevel,
	RFmxSpecAnMXTxpThresholdType thresholdType
)
```

```text
Public Function ConfigureThreshold ( 
	selectorString As String,
	thresholdEnabled As RFmxSpecAnMXTxpThresholdEnabled,
	thresholdLevel As Double,
	thresholdType As RFmxSpecAnMXTxpThresholdType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **thresholdEnabled RFmxSpecAnMXTxpThresholdEnabled**
  - Specifies whether to enable thresholding of the acquired samples to be used for the measurement.
- **thresholdLevel Double**
  - Specifies either the relative or absolute threshold power level based on the value of the SetThresholdType(String, RFmxSpecAnMXTxpThresholdType) method.
- **thresholdType RFmxSpecAnMXTxpThresholdType**
  - Specifies the reference for the power level used for thresholding.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_TXPCfgThreshold() function in C.

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4edfd7c1-5329-b237-e20a-3447eed534c8.htm language=enus -->
## TOPIC 00194: rfmxspecandotnet/html/4edfd7c1-5329-b237-e20a-3447eed534c8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4edfd7c1-5329-b237-e20a-3447eed534c8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4edfd7c1-5329-b237-e20a-3447eed534c8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpResults.Read Method

RFmxSpecAnMXAcpResultsRead Method

Configures hardware for acquisition, performs measurement on acquired data, and returns the adjacent channel power (ACP) measurement results.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int Read(
	string selectorString,
	double timeout,
	out double carrierAbsolutePower,
	out double offsetCh0LowerRelativePower,
	out double offsetCh0UpperRelativePower,
	out double offsetCh1LowerRelativePower,
	out double offsetCh1UpperRelativePower
)
```

```text
Public Function Read ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef carrierAbsolutePower As Double,
	<OutAttribute> ByRef offsetCh0LowerRelativePower As Double,
	<OutAttribute> ByRef offsetCh0UpperRelativePower As Double,
	<OutAttribute> ByRef offsetCh1LowerRelativePower As Double,
	<OutAttribute> ByRef offsetCh1UpperRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement
- **carrierAbsolutePower Double**
  - Upon return, contains the power measured in carrier 0. The carrier power is reported in dBm or dBm/Hz based on the value of the ACP Power Units
- **offsetCh0LowerRelativePower Double**
  - Upon return, contains the power measured in offset 0 in the negative band, relative to the power measured in the reference carrier specified using GetLowerOffsetPowerReferenceCarrier(String, Int32).
- **offsetCh0UpperRelativePower Double**
  - Upon return, contains the power measured in offset 0 in the positive band, relative to the power measured in the reference carrier specified using GetUpperOffsetPowerReferenceCarrier(String, Int32).
- **offsetCh1LowerRelativePower Double**
  - Upon return, contains the power measured in offset 1 in the negative band, relative to the power measured in the reference carrier specified using GetLowerOffsetPowerReferenceCarrier(String, Int32).
- **offsetCh1UpperRelativePower Double**
  - Upon return, contains the power measured in offset 1 in the positive band, relative to the power measured in the reference carrier specified using GetUpperOffsetPowerReferenceCarrier(String, Int32).

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPRead() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/4f2225dc-3b8a-8bab-150b-0c28c8c55434.htm language=enus -->
## TOPIC 00195: rfmxspecandotnet/html/4f2225dc-3b8a-8bab-150b-0c28c8c55434.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/4f2225dc-3b8a-8bab-150b-0c28c8c55434.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/4f2225dc-3b8a-8bab-150b-0c28c8c55434.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.SetAveragingEnabled Method

RFmxSpecAnMXAcpConfigurationSetAveragingEnabled Method

Sets whether to enable averaging of the spectrum for the adjacent channel power (ACP) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxSpecAnMXAcpAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAcpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpAveragingEnabled**
  - Specifies whether to enable averaging of the spectrum for the ACP measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPSetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/510a67ed-59d8-8a91-576f-dfd8b442a50c.htm language=enus -->
## TOPIC 00196: rfmxspecandotnet/html/510a67ed-59d8-8a91-576f-dfd8b442a50c.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/510a67ed-59d8-8a91-576f-dfd8b442a50c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/510a67ed-59d8-8a91-576f-dfd8b442a50c.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetEqualizerFilterLength Method

RFmxSpecAnMXAmpmConfigurationSetEqualizerFilterLength Method

Sets the length of the equalizer filter. The measurement maintains the filter length as an odd number by incrementing any even numbered value by one.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEqualizerFilterLength(
	string selectorString,
	int value
)
```

```text
Public Function SetEqualizerFilterLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the length of the equalizer filter. The measurement maintains the filter length as an odd number by incrementing any even numbered value by one.

###### Return Value

Int32

##### Remarks

AmpmEqualizerFilterLength

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/51322e12-bbdc-cca2-3036-c6d9b5a2376d.htm language=enus -->
## TOPIC 00197: rfmxspecandotnet/html/51322e12-bbdc-cca2-3036-c6d9b5a2376d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/51322e12-bbdc-cca2-3036-c6d9b5a2376d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/51322e12-bbdc-cca2-3036-c6d9b5a2376d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavt Methods

RFmxSpecAnMXPavt Methods

The [RFmxSpecAnMXPavt](a2479acb-bf7f-9979-88bd-25653175c095.htm) type exposes the following members.

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

RFmxSpecAnMXPavt Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/52dd165d-62d6-e38f-0c26-bbc9bf27fa38.htm language=enus -->
## TOPIC 00198: rfmxspecandotnet/html/52dd165d-62d6-e38f-0c26-bbc9bf27fa38.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/52dd165d-62d6-e38f-0c26-bbc9bf27fa38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/52dd165d-62d6-e38f-0c26-bbc9bf27fa38.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.SetOffsetSideband Method

RFmxSpecAnMXSemConfigurationSetOffsetSideband Method

Sets whether the offset segment is present on one side, or on both sides of the carriers.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetSideband(
	string selectorString,
	RFmxSpecAnMXSemOffsetSideband value
)
```

```text
Public Function SetOffsetSideband ( 
	selectorString As String,
	value As RFmxSpecAnMXSemOffsetSideband
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetSideband**
  - Specifies whether the offset segment is present on one side, or on both sides of the carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMSetOffsetSideband() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/534274d1-4764-41ee-28d2-9b0300083caa.htm language=enus -->
## TOPIC 00199: rfmxspecandotnet/html/534274d1-4764-41ee-28d2-9b0300083caa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/534274d1-4764-41ee-28d2-9b0300083caa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/534274d1-4764-41ee-28d2-9b0300083caa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseConfiguration.SetIntegratedNoiseRangeDefinition Method

RFmxSpecAnMXPhaseNoiseConfigurationSetIntegratedNoiseRangeDefinition Method

Sets the frequency range for integrated noise measurements.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIntegratedNoiseRangeDefinition(
	string selectorString,
	RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition value
)
```

```text
Public Function SetIntegratedNoiseRangeDefinition ( 
	selectorString As String,
	value As RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition**
  - Specifies the frequency range for integrated noise measurements.

###### Return Value

Int32

##### Remarks

PhaseNoiseIntegratedNoiseRangeDefinition

Measurement

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5458f7bf-8a2b-2cbf-45df-a18d0449dc4a.htm language=enus -->
## TOPIC 00200: rfmxspecandotnet/html/5458f7bf-8a2b-2cbf-45df-a18d0449dc4a.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5458f7bf-8a2b-2cbf-45df-a18d0449dc4a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5458f7bf-8a2b-2cbf-45df-a18d0449dc4a.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMemoryPolynomialOrder Method

RFmxSpecAnMXDpdConfigurationGetMemoryPolynomialOrder Method

Gets the order of the DPD polynomial.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMemoryPolynomialOrder(
	string selectorString,
	out int value
)
```

```text
Public Function GetMemoryPolynomialOrder ( 
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

This method maps to the RFmxSpecAn_DPDGetMemoryPolynomialOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5467aa3f-3133-3952-69bc-d98812a08bc8.htm language=enus -->
## TOPIC 00201: rfmxspecandotnet/html/5467aa3f-3133-3952-69bc-d98812a08bc8.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5467aa3f-3133-3952-69bc-d98812a08bc8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5467aa3f-3133-3952-69bc-d98812a08bc8.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.GetMemoryPolynomialLeadOrderType Method

RFmxSpecAnMXDpdConfigurationGetMemoryPolynomialLeadOrderType Method

RFmxSpecAnMXDpdModel

GeneralizedMemoryPolynomial

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMemoryPolynomialLeadOrderType(
	string selectorString,
	out RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType value
)
```

```text
Public Function GetMemoryPolynomialLeadOrderType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType**
  - Upon return, contains the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5467ad56-cbbd-851f-a3df-63fa4136be56.htm language=enus -->
## TOPIC 00202: rfmxspecandotnet/html/5467ad56-cbbd-851f-a3df-63fa4136be56.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5467ad56-cbbd-851f-a3df-63fa4136be56.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5467ad56-cbbd-851f-a3df-63fa4136be56.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.SetMeasurementEnabled Method

RFmxSpecAnMXDpdConfigurationSetMeasurementEnabled Method

Sets whether to enable the DPD measurement.

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
  - if the DPD measurement is enabled; otherwise .

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetMeasurementEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/54996cfe-1dfd-99ab-62d8-2e4be8724a12.htm language=enus -->
## TOPIC 00203: rfmxspecandotnet/html/54996cfe-1dfd-99ab-62d8-2e4be8724a12.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/54996cfe-1dfd-99ab-62d8-2e4be8724a12.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/54996cfe-1dfd-99ab-62d8-2e4be8724a12.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmResults.GetHarmonicAverageAbsolutePower Method

RFmxSpecAnMXHarmResultsGetHarmonicAverageAbsolutePower Method

Gets the average absolute power, in dBm, measured at the harmonic specified by the selector string.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetHarmonicAverageAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetHarmonicAverageAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and harmonic number. Example: "harmonic0", "result::r1/harmonic0". You can use the BuildHarmonicString2(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the average absolute power, in dBm, measured at the harmonic specified by the selector string.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmGetResultsHarmonicAverageAbsolutePower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/54f00ad1-b4e0-f396-8c4b-9614a1709ff3.htm language=enus -->
## TOPIC 00204: rfmxspecandotnet/html/54f00ad1-b4e0-f396-8c4b-9614a1709ff3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/54f00ad1-b4e0-f396-8c4b-9614a1709ff3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/54f00ad1-b4e0-f396-8c4b-9614a1709ff3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXCcdfConfiguration.GetMeasurementInterval Method

RFmxSpecAnMXCcdfConfigurationGetMeasurementInterval Method

Gets the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement.

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
  - Upon return, contains the acquisition time, in seconds, for the CCDF measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CCDFGetMeasurementInterval() function in C.

##### See Also

###### Reference

RFmxSpecAnMXCcdfConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/54f59383-a08a-86fa-331b-4b6ae89d2392.htm language=enus -->
## TOPIC 00205: rfmxspecandotnet/html/54f59383-a08a-86fa-331b-4b6ae89d2392.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/54f59383-a08a-86fa-331b-4b6ae89d2392.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/54f59383-a08a-86fa-331b-4b6ae89d2392.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetCalibrationLossFrequency Method

RFmxSpecAnMXNFConfigurationSetCalibrationLossFrequency Method

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
public int SetCalibrationLossFrequency(
	string selectorString,
	double[] value
)
```

```text
Public Function SetCalibrationLossFrequency ( 
	selectorString As String,
	value As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. THis value is expressed in Hz. This method is applicable only when you set the SetYFactorMode(String, RFmxSpecAnMXNFYFactorMode) method to Calibrate and set the SetMeasurementMethod(String, RFmxSpecAnMXNFMeasurementMethod) method to YFactor, or when you set the SetColdSourceMode(String, RFmxSpecAnMXNFColdSourceMode) method to Calibrate and set the NF Meas Method method to ColdSource.

###### Return Value

Int32

##### Remarks

NFCalibrationLossFrequency

##### See Also

###### Reference

RFmxSpecAnMXNFConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/54ff1f05-947d-ef4e-44df-0fe1ad330086.htm language=enus -->
## TOPIC 00206: rfmxspecandotnet/html/54ff1f05-947d-ef4e-44df-0fe1ad330086.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/54ff1f05-947d-ef4e-44df-0fe1ad330086.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/54ff1f05-947d-ef4e-44df-0fe1ad330086.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdConfiguration.ConfigureLookupTableStepSize Method

RFmxSpecAnMXDpdConfigurationConfigureLookupTableStepSize Method

SetModel(String, RFmxSpecAnMXDpdModel)

LookupTable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureLookupTableStepSize(
	string selectorString,
	double stepSize
)
```

```text
Public Function ConfigureLookupTableStepSize ( 
	selectorString As String,
	stepSize As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **stepSize Double**
  - Specifies the step size, in dB, of the input power levels in the predistortion lookup table when you set the SetModel(String, RFmxSpecAnMXDpdModel) method to LookupTable.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgLookupTableStepSize() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/55389aff-7418-f7a6-4edb-f088e0d2f580.htm language=enus -->
## TOPIC 00207: rfmxspecandotnet/html/55389aff-7418-f7a6-4edb-f088e0d2f580.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/55389aff-7418-f7a6-4edb-f088e0d2f580.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/55389aff-7418-f7a6-4edb-f088e0d2f580.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXNFConfiguration.SetDutType Method

RFmxSpecAnMXNFConfigurationSetDutType Method

Sets the type of DUT.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDutType(
	string selectorString,
	RFmxSpecAnMXNFDutType value
)
```

```text
Public Function SetDutType ( 
	selectorString As String,
	value As RFmxSpecAnMXNFDutType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXNFDutType**
  - Specifies the type of DUT.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/55580ccc-977d-54bc-5d0e-297ecba9f5b7.htm language=enus -->
## TOPIC 00208: rfmxspecandotnet/html/55580ccc-977d-54bc-5d0e-297ecba9f5b7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/55580ccc-977d-54bc-5d0e-297ecba9f5b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/55580ccc-977d-54bc-5d0e-297ecba9f5b7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration Methods

RFmxSpecAnMXSemConfiguration Methods

The [RFmxSpecAnMXSemConfiguration](b04b0407-0259-5fde-e05d-fd4f84119852.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the spectral emission mask (SEM) measurement. |
|  | ConfigureCarrierChannelBandwidth | Configures the channel bandwidth, in hertz (Hz), of the carrier. |
|  | ConfigureCarrierEnabled | Configures whether to consider the carrier power as part of total carrier power measurement. |
|  | ConfigureCarrierFrequency | Configures the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency |
|  | ConfigureCarrierIntegrationBandwidth | Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power. |
|  | ConfigureCarrierRbwFilter | Configures the resolution bandwidth (RBW) filter of the carrier signal. |
|  | ConfigureCarrierRrcFilter | Configures the root raised cosine (RRC) channel filter to apply on the acquired carrier channel before measuring the channel power. RRC alpha is the filter roll off. |
|  | ConfigureFft | Configures window and FFT to obtain a spectrum for the spectral emission mask (SEM) measurement. |
|  | ConfigureNumberOfCarriers | Configures the number of carriers for the spectral emission mask (SEM) measurement. |
|  | ConfigureNumberOfOffsets | Configures the number of offset segments for the spectral emission mask (SEM) measurement. |
|  | ConfigureOffsetAbsoluteLimit | Configures the absolute limit mode and specifies the absolute power limits corresponding to the beginning and end of the offset segment. |
|  | ConfigureOffsetAbsoluteLimitArray | Configures the absolute limit mode and specifies the absolute power limits corresponding to the beginning and end of the offset segment. |
|  | ConfigureOffsetBandwidthIntegral | Configures the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). If you set this method to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW. |
|  | ConfigureOffsetFrequency | Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers. |
|  | ConfigureOffsetFrequencyArray | Configures the offset frequency start and stop values, and specifies whether the offset segment is present on one side, or on both sides of the carriers. |
|  | ConfigureOffsetFrequencyDefinition | Configures the offset frequency definition for the SEM measurement. |
|  | ConfigureOffsetLimitFailMask | Configures the criteria to determine the measurement fail status. |
|  | ConfigureOffsetRbwFilter | Configures the resolution bandwidth (RBW) filter of the offset segment. |
|  | ConfigureOffsetRbwFilterArray | Configures the resolution bandwidth (RBW) filter of the offset segment. |
|  | ConfigureOffsetRelativeAttenuation | Configures the attenuation, in dB, relative to the external attenuation. Use this method to compensate for variations in external attenuation when the offset channels are spread wide in frequency. |
|  | ConfigureOffsetRelativeAttenuationArray | Configures the attenuation, in dB, relative to the external attenuation. Use this method to compensate for the variations in external attenuation when offset channels are spread wide in frequency. |
|  | ConfigureOffsetRelativeLimit | Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. |
|  | ConfigureOffsetRelativeLimitArray | Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. |
|  | ConfigurePowerUnits | Configures the units for the absolute power. |
|  | ConfigureReferenceType | Configures whether the power reference is the integrated power or the peak power in the closest carrier channel. The leftmost carrier is the carrier closest to all the lower (negative) offset segments. The rightmost carrier offset is the carrier closest to all the upper (positive) offset segments. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets if the traces to be stored and retrieved after performing the spectral emission mask (SEM) measurement are enabled. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging. |
|  | GetAveragingEnabled | Gets whether averaging for the spectral emission mask (SEM) measurement is enabled. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectral emission mask (SEM) measurement. |
|  | GetCarrierChannelBandwidth | Gets the channel bandwidth, in hertz (Hz), of the carrier. The channel bandwidth is used to calculate the values of the SetOffsetStartFrequency(String, Double) and SetOffsetStopFrequency(String, Double) methods when you set the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method to CarrierEdgeToMeasurementBandwidthCenter or CarrierEdgeToMeasurementBandwidthEdge. |
|  | GetCarrierEnabled | Gets whether the carrier power is considered as part of total carrier power measurement. |
|  | GetCarrierFrequency | Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
|  | GetCarrierIntegrationBandwidth | Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power. |
|  | GetCarrierRbwFilterAutoBandwidth | Gets whether the measurement computes the resolution bandwidth (RBW) of the carrier. |
|  | GetCarrierRbwFilterBandwidth | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal. |
|  | GetCarrierRbwFilterBandwidthDefinition | Gets the bandwidth definition which you use to specify the value of the SetCarrierRbwFilterBandwidth(String, Double) method. |
|  | GetCarrierRbwFilterType | Gets the shape of the digital resolution bandwidth (RBW) filter. |
|  | GetCarrierRrcFilterAlpha | Gets the roll-off factor for the root-raised-cosine (RRC) filter. |
|  | GetCarrierRrcFilterEnabled | Gets whether the root-raised-cosine (RRC) filter is applied on the acquired carrier channel after measuring the carrier channel power. |
|  | GetFftPadding | Gets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
|  | GetFftWindow | Gets the FFT window type used to reduce spectral leakage. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable spectral emission mask (SEM) measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for spectral emission mask (SEM) measurement. |
|  | GetNumberOfCarriers | Gets the number of carriers. |
|  | GetNumberOfOffsets | Gets the number of offset segment configurations. |
|  | GetOffsetAbsoluteLimitMode | Gets whether the absolute limit mask is a flat line or is a line with a slope. |
|  | GetOffsetAbsoluteLimitStart | Gets the absolute power limit, in dBm, corresponding to the beginning of the offset segment. |
|  | GetOffsetAbsoluteLimitStop | Gets the absolute power limit, in dBm, corresponding to the end of the offset segment. |
|  | GetOffsetBandwidthIntegral | Gets the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). |
|  | GetOffsetEnabled | Gets whether the offset segment for the spectral emission mask (SEM) measurement is enabled. |
|  | GetOffsetFrequencyDefinition | Gets the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels. |
|  | GetOffsetLimitFailMask | Gets the criteria to determine the measurement fail status. |
|  | GetOffsetRbwFilterAutoBandwidth | Gets whether the measurement computes the resolution bandwidth (RBW). |
|  | GetOffsetRbwFilterBandwidth | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment. |
|  | GetOffsetRbwFilterBandwidthDefinition | Gets the bandwidth definition which you use to specify the value of the SetOffsetRbwFilterBandwidth(String, Double) method. |
|  | GetOffsetRbwFilterType | Gets the shape of the digital resolution bandwidth (RBW) filter. |
|  | GetOffsetRelativeAttenuation | Gets the attenuation, in dB, relative to the SetExternalAttenuation(String, Double) method. Use this method to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
|  | GetOffsetRelativeLimitMode | Gets whether the relative limit mask is a flat line or a line with a slope. |
|  | GetOffsetRelativeLimitStart | Gets the relative power limit, in dB, corresponding to the beginning of the offset segment. |
|  | GetOffsetRelativeLimitStop | Gets the relative power limit, in dB, corresponding to the end of the offset segment. |
|  | GetOffsetSideband | Gets whether the offset segment is present on one side, or on both sides of the carriers. |
|  | GetOffsetStartFrequency | Gets the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method. |
|  | GetOffsetStopFrequency | Gets the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method. |
|  | GetPowerUnits | Gets the power units. |
|  | GetReferenceType | Gets whether the power reference is the integrated power or the peak power in the closest carrier channel. The least carrier offset is the carrier closest to all the lower (negative) offset segments. The highest carrier offset is the carrier closest to all the upper (positive) offsets segments. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time, in seconds. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the spectral emission mask (SEM) measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the RFmxSpecAnMXSemAveragingEnabled method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the spectral emission mask (SEM) measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectral emission mask (SEM) measurement. |
|  | SetCarrierChannelBandwidth | Sets the channel bandwidth, in hertz (Hz), of the carrier. The channel bandwidth is used to calculate the values of the SetOffsetStartFrequency(String, Double) and SetOffsetStopFrequency(String, Double) methods when you set the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method to CarrierEdgeToMeasurementBandwidthCenter or CarrierEdgeToMeasurementBandwidthEdge. |
|  | SetCarrierEnabled | Sets whether to consider the carrier power as part of total carrier power measurement. |
|  | SetCarrierFrequency | Sets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
|  | SetCarrierIntegrationBandwidth | Sets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
|  | SetCarrierRbwFilterAutoBandwidth | Sets whether the measurement computes the resolution bandwidth (RBW) of the carrier. |
|  | SetCarrierRbwFilterBandwidth | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal. |
|  | SetCarrierRbwFilterBandwidthDefinition | Sets the bandwidth definition which you use to specify the value of the SetCarrierRbwFilterBandwidth(String, Double) method. |
|  | SetCarrierRbwFilterType | Sets the shape of the digital resolution bandwidth (RBW) filter. |
|  | SetCarrierRrcFilterAlpha | Sets the roll-off factor for the root-raised-cosine (RRC) filter. |
|  | SetCarrierRrcFilterEnabled | Sets whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel after measuring the carrier channel power. |
|  | SetFftPadding | Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
|  | SetFftWindow | Sets the FFT window type used to reduce spectral leakage. |
|  | SetMeasurementEnabled | Sets whether to enable spectral emission mask (SEM) measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for spectral emission mask (SEM) measurement. |
|  | SetNumberOfCarriers | Sets the number of carriers. |
|  | SetNumberOfOffsets | Sets the number of offset segment configurations. |
|  | SetOffsetAbsoluteLimitMode | Sets whether the absolute limit mask is a flat line or is a line with a slope. |
|  | SetOffsetAbsoluteLimitStart | Sets the absolute power limit, in dBm, corresponding to the beginning of the offset segment. This power limit is also set as the absolute power limit for the offset segment when you set the SetOffsetAbsoluteLimitMode(String, RFmxSpecAnMXSemOffsetAbsoluteLimitMode) method to Couple. |
|  | SetOffsetAbsoluteLimitStop | Sets the absolute power limit, in dBm, corresponding to the end of the offset segment. This power limit is also set as the absolute power limit for the offset segment when you set the SetOffsetAbsoluteLimitMode(String, RFmxSpecAnMXSemOffsetAbsoluteLimitMode) method to Couple. |
|  | SetOffsetBandwidthIntegral | Sets the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). |
|  | SetOffsetEnabled | Sets whether to enable the offset segment for the spectral emission mask (SEM) measurement. |
|  | SetOffsetFrequencyDefinition | Sets the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels. |
|  | SetOffsetLimitFailMask | Sets the criteria to determine the measurement fail status. |
|  | SetOffsetRbwFilterAutoBandwidth | Sets whether the measurement computes the resolution bandwidth (RBW). |
|  | SetOffsetRbwFilterBandwidth | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment. |
|  | SetOffsetRbwFilterBandwidthDefinition | Sets the bandwidth definition which you use to specify the value of the SetOffsetRbwFilterBandwidth(String, Double) method. |
|  | SetOffsetRbwFilterType | Sets the shape of the digital resolution bandwidth (RBW) filter. |
|  | SetOffsetRelativeAttenuation | Sets the attenuation, in dB, relative to the SetExternalAttenuation(String, Double) method. Use this method to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
|  | SetOffsetRelativeLimitMode | Sets whether the relative limit mask is a flat line or a line with a slope. |
|  | SetOffsetRelativeLimitStart | Sets the relative power limit, in dB, corresponding to the beginning of the offset segment. This power limit is also set as the relative power limit for the offset segment when you set the SetOffsetRelativeLimitMode(String, RFmxSpecAnMXSemOffsetRelativeLimitMode) method to Couple. |
|  | SetOffsetRelativeLimitStop | Sets the relative power limit, in dB, corresponding to the end of the offset segment. This method is ignored if you set the SetOffsetRelativeLimitMode(String, RFmxSpecAnMXSemOffsetRelativeLimitMode) method to Couple. |
|  | SetOffsetSideband | Sets whether the offset segment is present on one side, or on both sides of the carriers. |
|  | SetOffsetStartFrequency | Sets the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method. |
|  | SetOffsetStopFrequency | Sets the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the ConfigureOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method. |
|  | SetPowerUnits | Sets the power units. |
|  | SetReferenceType | Sets whether the power reference is the integrated power or the peak power in the closest carrier channel. The least carrier offset is the carrier closest to all the lower (negative) offset segments. The highest carrier offset is the carrier closest to all the upper (positive) offsets segments. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time, in seconds, when you set the SetSweepTimeAuto(String, RFmxSpecAnMXSemSweepTimeAuto) method to False. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/561a1516-c8ad-4655-bbc0-a5ce26137444.htm language=enus -->
## TOPIC 00209: rfmxspecandotnet/html/561a1516-c8ad-4655-bbc0-a5ce26137444.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/561a1516-c8ad-4655-bbc0-a5ce26137444.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/561a1516-c8ad-4655-bbc0-a5ce26137444.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetNumberOfCarriers Method

RFmxSpecAnMXAmpmConfigurationSetNumberOfCarriers Method

SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled)

False

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
  - Specifies the number of carriers in the reference waveform when you set the SetAutoCarrierDetectionEnabled(String, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False.

###### Return Value

Int32

##### Remarks

AmpmNumberOfCarriers

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/562ee14f-6213-853a-a257-21e93f789d28.htm language=enus -->
## TOPIC 00210: rfmxspecandotnet/html/562ee14f-6213-853a-a257-21e93f789d28.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/562ee14f-6213-853a-a257-21e93f789d28.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/562ee14f-6213-853a-a257-21e93f789d28.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXConstants.PxiTriggerLine1 Field

RFmxSpecAnMXConstantsPxiTriggerLine1 Field

The signal is exported to the PXI trigger line 1.

Namespace:

NationalInstruments.RFmx.SpecAnMX

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

RFmxSpecAnMXConstants Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5645874d-4645-6db4-a65a-e1a4caec9afe.htm language=enus -->
## TOPIC 00211: rfmxspecandotnet/html/5645874d-4645-6db4-a65a-e1a4caec9afe.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5645874d-4645-6db4-a65a-e1a4caec9afe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5645874d-4645-6db4-a65a-e1a4caec9afe.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIQConfiguration.GetAcquisitionTime Method

RFmxSpecAnMXIQConfigurationGetAcquisitionTime Method

Gets the acquisition time, in seconds, for the I/Q measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAcquisitionTime(
	string selectorString,
	out double value
)
```

```text
Public Function GetAcquisitionTime ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the acquisition time, in seconds, for the I/Q measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_IQGetAcquisitionTime() function in C.

##### See Also

###### Reference

RFmxSpecAnMXIQConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/578412ef-0527-d446-4083-caede43b88f0.htm language=enus -->
## TOPIC 00212: rfmxspecandotnet/html/578412ef-0527-d446-4083-caede43b88f0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/578412ef-0527-d446-4083-caede43b88f0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/578412ef-0527-d446-4083-caede43b88f0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.GetAMToPMCurveFitOrder Method

RFmxSpecAnMXAmpmConfigurationGetAMToPMCurveFitOrder Method

Gets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAMToPMCurveFitOrder(
	string selectorString,
	out int value
)
```

```text
Public Function GetAMToPMCurveFitOrder ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetAMToPMCurveFitOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/57b4b250-76d3-0967-6adb-6027af367de0.htm language=enus -->
## TOPIC 00213: rfmxspecandotnet/html/57b4b250-76d3-0967-6adb-6027af367de0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/57b4b250-76d3-0967-6adb-6027af367de0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/57b4b250-76d3-0967-6adb-6027af367de0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetFftWindow Method

RFmxSpecAnMXSpurConfigurationSetFftWindow Method

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
	RFmxSpecAnMXSpurFftWindow value
)
```

```text
Public Function SetFftWindow ( 
	selectorString As String,
	value As RFmxSpecAnMXSpurFftWindow
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpurFftWindow**
  - Specifies the FFT window type used to reduce spectral leakage.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetFFTWindow() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5898a793-30bb-f82a-edb3-b047e2f331c2.htm language=enus -->
## TOPIC 00214: rfmxspecandotnet/html/5898a793-30bb-f82a-edb3-b047e2f331c2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5898a793-30bb-f82a-edb3-b047e2f331c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5898a793-30bb-f82a-edb3-b047e2f331c2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpNoiseCalibrationMode Enumeration

RFmxSpecAnMXChpNoiseCalibrationMode Enumeration

Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXChpNoiseCalibrationMode
```

```text
Public Enumeration RFmxSpecAnMXChpNoiseCalibrationMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Manual | 0 | When you set the SetMeasurementMode(String, RFmxSpecAnMXChpMeasurementMode) method to RFMXSPECAN_VAL_CHP_MEASUREMENT_MODE_NOISE_CALIBRATE, you can initiate instrument noise calibration for the CHP measurement manually. When you set the CHP Meas Mode method to Measure, you can initiate the CHP measurement manually. |
| Auto | 1 | When you set the SetNoiseCompensationEnabled(String, RFmxSpecAnMXChpNoiseCompensationEnabled) method to True, RFmx sets Input Isolation Enabled to Enabled and calibrates the intrument noise in the current state of the instrument. RFmx then resets the Input Isolation Enabled method and performs the CHP measurement, including compensation for noise of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set the CHP Noise Comp Enabled method to False, RFmx does not calibrate instrument noise and performs only the CHP measurement without compensating for the noise contribution of the instrument. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/58b60847-7b3e-6e24-5024-856c65ca92af.htm language=enus -->
## TOPIC 00215: rfmxspecandotnet/html/58b60847-7b3e-6e24-5024-856c65ca92af.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/58b60847-7b3e-6e24-5024-856c65ca92af.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/58b60847-7b3e-6e24-5024-856c65ca92af.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.ConfigureConfigurationInput Method

RFmxSpecAnMXDpdApplyDpdConfigureConfigurationInput Method

Configures the source of measurement settings for applying DPD.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureConfigurationInput(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdConfigurationInput configurationInput
)
```

```text
Public Function ConfigureConfigurationInput ( 
	selectorString As String,
	configurationInput As RFmxSpecAnMXDpdApplyDpdConfigurationInput
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **configurationInput RFmxSpecAnMXDpdApplyDpdConfigurationInput**
  - Specifies the mode of configuring parameters for applying the DPD.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDCfgApplyDPDConfigurationInput() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/58c6eb91-2ee9-dc7b-6918-9319ba0dd203.htm language=enus -->
## TOPIC 00216: rfmxspecandotnet/html/58c6eb91-2ee9-dc7b-6918-9319ba0dd203.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/58c6eb91-2ee9-dc7b-6918-9319ba0dd203.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/58c6eb91-2ee9-dc7b-6918-9319ba0dd203.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.SetAveragingEnabled Method

RFmxSpecAnMXObwConfigurationSetAveragingEnabled Method

Sets whether to enable averaging for the occupied bandwidth (OBW) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxSpecAnMXObwAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXObwAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwAveragingEnabled**
  - Specifies whether to enable averaging for the OBW measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWSetAveragingEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/592f9ad5-9ac0-cff1-6ba1-8499e9703d6f.htm language=enus -->
## TOPIC 00217: rfmxspecandotnet/html/592f9ad5-9ac0-cff1-6ba1-8499e9703d6f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/592f9ad5-9ac0-cff1-6ba1-8499e9703d6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/592f9ad5-9ac0-cff1-6ba1-8499e9703d6f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.GetAmplitudeCorrectionType Method

RFmxSpecAnMXSpurConfigurationGetAmplitudeCorrectionType Method

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeCorrectionType(
	string selectorString,
	out RFmxSpecAnMXSpurAmplitudeCorrectionType value
)
```

```text
Public Function GetAmplitudeCorrectionType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpurAmplitudeCorrectionType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpurAmplitudeCorrectionType**
  - Upon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

###### Return Value

Int32

##### Remarks

SpurAmplitudeCorrectionType

RFCenterFrequency

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5a459009-14f7-1f43-3529-69870a55b117.htm language=enus -->
## TOPIC 00218: rfmxspecandotnet/html/5a459009-14f7-1f43-3529-69870a55b117.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5a459009-14f7-1f43-3529-69870a55b117.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5a459009-14f7-1f43-3529-69870a55b117.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.ConfigureOffsetFrequencyArray Method

RFmxSpecAnMXSemConfigurationConfigureOffsetFrequencyArray Method

Configures the offset frequency start and stop values, and specifies whether the offset segment is present on one side, or on both sides of the carriers.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetFrequencyArray(
	string selectorString,
	double[] offsetStartFrequency,
	double[] offsetStopFrequency,
	RFmxSpecAnMXSemOffsetEnabled[] offsetEnabled,
	RFmxSpecAnMXSemOffsetSideband[] offsetSideband
)
```

```text
Public Function ConfigureOffsetFrequencyArray ( 
	selectorString As String,
	offsetStartFrequency As Double(),
	offsetStopFrequency As Double(),
	offsetEnabled As RFmxSpecAnMXSemOffsetEnabled(),
	offsetSideband As RFmxSpecAnMXSemOffsetSideband()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetStartFrequency Double**
  - Specifies the array of start frequencies, in hertz (Hz), of each offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method.
- **offsetStopFrequency Double**
  - Specifies the array of stop frequencies, in Hz, of each offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the SetOffsetFrequencyDefinition(String, RFmxSpecAnMXSemOffsetFrequencyDefinition) method.
- **offsetEnabled RFmxSpecAnMXSemOffsetEnabled**
  - Specifies whether to enable the offset segment for the SEM measurement.
- **offsetSideband RFmxSpecAnMXSemOffsetSideband**
  - Specifies whether the offset segment is present on one side, or on both sides of the carriers.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetFrequencyArray() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5a47e934-e15c-8d17-b8a1-253b848f78aa.htm language=enus -->
## TOPIC 00219: rfmxspecandotnet/html/5a47e934-e15c-8d17-b8a1-253b848f78aa.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5a47e934-e15c-8d17-b8a1-253b848f78aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5a47e934-e15c-8d17-b8a1-253b848f78aa.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration.SetRangeRbwFilterBandwidth Method

RFmxSpecAnMXSpurConfigurationSetRangeRbwFilterBandwidth Method

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRangeRbwFilterBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetRangeRbwFilterBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the range number. Example: "range0". You can use the BuildRangeString2(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the bandwidth, in Hz, of the RBW filter applied to the acquired signal.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeRBWFilterBandwidth() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5aabadc4-4921-3739-fc95-b0628a501518.htm language=enus -->
## TOPIC 00220: rfmxspecandotnet/html/5aabadc4-4921-3739-fc95-b0628a501518.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5aabadc4-4921-3739-fc95-b0628a501518.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5aabadc4-4921-3739-fc95-b0628a501518.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcp.Results Property

RFmxSpecAnMXAcpResults Property

Gets the RFmxSpecAnMXAcpResults instance that provides methods to retrieve ACP measurement results.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxSpecAnMXAcpResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxSpecAnMXAcpResults
	Get
```

###### Property Value

RFmxSpecAnMXAcpResults

##### See Also

###### Reference

RFmxSpecAnMXAcp Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5de3a195-5889-9d38-6b91-820110024cf3.htm language=enus -->
## TOPIC 00221: rfmxspecandotnet/html/5de3a195-5889-9d38-6b91-820110024cf3.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5de3a195-5889-9d38-6b91-820110024cf3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5de3a195-5889-9d38-6b91-820110024cf3.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXMarkerConfiguration.ConfigureFunctionType Method

RFmxSpecAnMXMarkerConfigurationConfigureFunctionType Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureFunctionType(
	string selectorString,
	RFmxSpecAnMXMarkerFunctionType functionType
)
```

```text
Public Function ConfigureFunctionType ( 
	selectorString As String,
	functionType As RFmxSpecAnMXMarkerFunctionType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of marker number. Example:"marker0" You can use the RFmxSpecAn_BuildMarkerString2 method to build the selector string.
- **functionType RFmxSpecAnMXMarkerFunctionType**
  - specifies the function type for the selected marker. The default value is Off.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXMarkerConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5ee9a740-dfb0-5e68-8603-527ccc3958ce.htm language=enus -->
## TOPIC 00222: rfmxspecandotnet/html/5ee9a740-dfb0-5e68-8603-527ccc3958ce.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5ee9a740-dfb0-5e68-8603-527ccc3958ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5ee9a740-dfb0-5e68-8603-527ccc3958ce.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwConfiguration.GetRbwFilterType Method

RFmxSpecAnMXObwConfigurationGetRbwFilterType Method

Gets the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterType(
	string selectorString,
	out RFmxSpecAnMXObwRbwFilterType value
)
```

```text
Public Function GetRbwFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXObwRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXObwRbwFilterType**
  - Upon return, contains the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_OBWGetRBWFilterType() function in C.

##### See Also

###### Reference

RFmxSpecAnMXObwConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5ef37b4c-fb59-68bf-0ce8-7fcb4ad0d6c9.htm language=enus -->
## TOPIC 00223: rfmxspecandotnet/html/5ef37b4c-fb59-68bf-0ce8-7fcb4ad0d6c9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5ef37b4c-fb59-68bf-0ce8-7fcb4ad0d6c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5ef37b4c-fb59-68bf-0ce8-7fcb4ad0d6c9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdResults.FetchProcessedReferenceWaveform Method

RFmxSpecAnMXIdpdResultsFetchProcessedReferenceWaveform Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchProcessedReferenceWaveform(
	string selectorString,
	double timeout,
	ref ComplexWaveform<ComplexSingle> processedReferenceWaveform
)
```

```text
Public Function FetchProcessedReferenceWaveform ( 
	selectorString As String,
	timeout As Double,
	ByRef processedReferenceWaveform As ComplexWaveform(Of ComplexSingle)
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **processedReferenceWaveform ComplexWaveformComplexSingle**
  - Upon return, contains the segment of the reference waveform used to perform the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIdpdResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5f030e89-f370-4beb-1ae6-f201a5117ac9.htm language=enus -->
## TOPIC 00224: rfmxspecandotnet/html/5f030e89-f370-4beb-1ae6-f201a5117ac9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5f030e89-f370-4beb-1ae6-f201a5117ac9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5f030e89-f370-4beb-1ae6-f201a5117ac9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXObwRbwFilterType Enumeration

RFmxSpecAnMXObwRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXObwRbwFilterType
```

```text
Public Enumeration RFmxSpecAnMXObwRbwFilterType
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5f18eed7-f5ce-7f11-9799-5be4fdbb7a40.htm language=enus -->
## TOPIC 00225: rfmxspecandotnet/html/5f18eed7-f5ce-7f11-9799-5be4fdbb7a40.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5f18eed7-f5ce-7f11-9799-5be4fdbb7a40.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5f18eed7-f5ce-7f11-9799-5be4fdbb7a40.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdPreDpd.GetCarrierOffset Method

RFmxSpecAnMXDpdPreDpdGetCarrierOffset Method

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
public int GetCarrierOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the carrier offset relative to the center of the complex baseband equivalent of the RF signal when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

DpdPreDpdCarrierOffset

##### See Also

###### Reference

RFmxSpecAnMXDpdPreDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/5f93c990-cf45-3379-3cb7-ac4a7edcffec.htm language=enus -->
## TOPIC 00226: rfmxspecandotnet/html/5f93c990-cf45-3379-3cb7-ac4a7edcffec.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/5f93c990-cf45-3379-3cb7-ac4a7edcffec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/5f93c990-cf45-3379-3cb7-ac4a7edcffec.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpOffsetRrcFilterEnabled Enumeration

RFmxSpecAnMXAcpOffsetRrcFilterEnabled Enumeration

Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpOffsetRrcFilterEnabled
```

```text
Public Enumeration RFmxSpecAnMXAcpOffsetRrcFilterEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The channel power of the acquired offset channel is measured directly. |
| True | 1 | The measurement applies the RRC filter on the acquired offset channel before measuring the offset channel power. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/60731f0c-fb5e-f423-7d56-64f39ffed13f.htm language=enus -->
## TOPIC 00227: rfmxspecandotnet/html/60731f0c-fb5e-f423-7d56-64f39ffed13f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/60731f0c-fb5e-f423-7d56-64f39ffed13f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/60731f0c-fb5e-f423-7d56-64f39ffed13f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumFftOverlapMode Enumeration

RFmxSpecAnMXSpectrumFftOverlapMode Enumeration

SpectrumMeasurementMethod

SequentialFft

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXSpectrumFftOverlapMode
```

```text
Public Enumeration RFmxSpecAnMXSpectrumFftOverlapMode
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the overlap between the chunks. |
| Automatic | 1 | Measurement sets the overlap based on the value you have set for the SpectrumFftWindow method. When you set the Spectrum FFT Window method to any value other than None, the number of overlapped samples between consecutive chunks is set to 50% of the value of the SpectrumSequentialFftSize method. When you set the Spectrum FFT Window method to None, the chunks are not overlapped and the overlap is set to 0%. |
| UserDefined | 2 | Measurement uses the overlap that you specify in the Spectrum FFT Overlap (%) method. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/60d8c52e-7d82-f3cc-3602-0e1b77829591.htm language=enus -->
## TOPIC 00228: rfmxspecandotnet/html/60d8c52e-7d82-f3cc-3602-0e1b77829591.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/60d8c52e-7d82-f3cc-3602-0e1b77829591.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/60d8c52e-7d82-f3cc-3602-0e1b77829591.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpRbwFilterType Enumeration

RFmxSpecAnMXAcpRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXAcpRbwFilterType
```

```text
Public Enumeration RFmxSpecAnMXAcpRbwFilterType
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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/61086feb-7440-7049-c425-ebc323320dd7.htm language=enus -->
## TOPIC 00229: rfmxspecandotnet/html/61086feb-7440-7049-c425-ebc323320dd7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/61086feb-7440-7049-c425-ebc323320dd7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/61086feb-7440-7049-c425-ebc323320dd7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXExtension.GetSpecAnList Method

RFmxSpecAnMXExtensionGetSpecAnList Method

Creates a new SpecAn list if it doesn't exist; otherwise, it returns the
 existing SpecAn list.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxSpecAnMXList GetSpecAnList(
	this RFmxInstrMX instrSession,
	string listName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetSpecAnList ( 
	instrSession As RFmxInstrMX,
	listName As String
) As RFmxSpecAnMXList
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an instr session.
- **listName String**
  - Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::list1" "list1" .

###### Return Value

RFmxSpecAnMXList

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxSpecAnMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/618f61bc-d8da-9ac6-2811-4d6c37ec7ffd.htm language=enus -->
## TOPIC 00230: rfmxspecandotnet/html/618f61bc-d8da-9ac6-2811-4d6c37ec7ffd.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/618f61bc-d8da-9ac6-2811-4d6c37ec7ffd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/618f61bc-d8da-9ac6-2811-4d6c37ec7ffd.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPhaseNoiseResults.FetchSpotNoise Method

RFmxSpecAnMXPhaseNoiseResultsFetchSpotNoise Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSpotNoise(
	string selectorString,
	double timeout,
	ref double[] spotPhaseNoise
)
```

```text
Public Function FetchSpotNoise ( 
	selectorString As String,
	timeout As Double,
	ByRef spotPhaseNoise As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **spotPhaseNoise Double**
  - Upon return, contains the phase noise corresponding to the value of the PhaseNoise Spot Noise Freq List method, by using the smoothed log plot trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXPhaseNoiseResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/61a1baeb-19db-3c46-522d-3bcc86bdda3e.htm language=enus -->
## TOPIC 00231: rfmxspecandotnet/html/61a1baeb-19db-3c46-522d-3bcc86bdda3e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/61a1baeb-19db-3c46-522d-3bcc86bdda3e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/61a1baeb-19db-3c46-522d-3bcc86bdda3e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetApplyDpdUserLookupTableType Method

RFmxSpecAnMXDpdApplyDpdSetApplyDpdUserLookupTableType Method

Sets the DPD Lookup Table (LUT) type.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetApplyDpdUserLookupTableType(
	string selectorString,
	RFmxSpecAnMXDpdApplyDpdUserLookupTableType value
)
```

```text
Public Function SetApplyDpdUserLookupTableType ( 
	selectorString As String,
	value As RFmxSpecAnMXDpdApplyDpdUserLookupTableType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdUserLookupTableType**
  - Specifies the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method to User.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/61f8b366-c61b-e885-043f-adf35a1ba1a7.htm language=enus -->
## TOPIC 00232: rfmxspecandotnet/html/61f8b366-c61b-e885-043f-adf35a1ba1a7.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/61f8b366-c61b-e885-043f-adf35a1ba1a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/61f8b366-c61b-e885-043f-adf35a1ba1a7.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmResults.GetGainErrorRange Method

RFmxSpecAnMXAmpmResultsGetGainErrorRange Method

Gets the peak-to-peak deviation of the gain, in dB, of the device under test.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetGainErrorRange(
	string selectorString,
	out double value
)
```

```text
Public Function GetGainErrorRange ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the peak-to-peak deviation of the gain, in dB, of the device under test.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMGetResultsGainErrorRange() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/640d5068-836d-10fc-77da-7ae1e07c6d15.htm language=enus -->
## TOPIC 00233: rfmxspecandotnet/html/640d5068-836d-10fc-77da-7ae1e07c6d15.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/640d5068-836d-10fc-77da-7ae1e07c6d15.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/640d5068-836d-10fc-77da-7ae1e07c6d15.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSemConfiguration.GetOffsetFrequencyDefinition Method

RFmxSpecAnMXSemConfigurationGetOffsetFrequencyDefinition Method

Gets the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetFrequencyDefinition(
	string selectorString,
	out RFmxSpecAnMXSemOffsetFrequencyDefinition value
)
```

```text
Public Function GetOffsetFrequencyDefinition ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSemOffsetFrequencyDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(String, Int32) method to build the selector string.
- **value RFmxSpecAnMXSemOffsetFrequencyDefinition**
  - Upon return, gets the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_SEMGetOffsetFrequencyDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXSemConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/641c3cc7-0c49-55f9-f931-9067ce441a8e.htm language=enus -->
## TOPIC 00234: rfmxspecandotnet/html/641c3cc7-0c49-55f9-f931-9067ce441a8e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/641c3cc7-0c49-55f9-f931-9067ce441a8e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/641c3cc7-0c49-55f9-f931-9067ce441a8e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAmpmConfiguration.SetThresholdEnabled Method

RFmxSpecAnMXAmpmConfigurationSetThresholdEnabled Method

Sets whether to enable thresholding of the acquired samples used for the AMPM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetThresholdEnabled(
	string selectorString,
	RFmxSpecAnMXAmpmThresholdEnabled value
)
```

```text
Public Function SetThresholdEnabled ( 
	selectorString As String,
	value As RFmxSpecAnMXAmpmThresholdEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAmpmThresholdEnabled**
  - Contains a value that indicates whether to enable thresholding of the acquired samples used for the AMPM measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_AMPMSetThresholdEnabled() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAmpmConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/642b085c-7269-9f8a-ca4b-7b0275471105.htm language=enus -->
## TOPIC 00235: rfmxspecandotnet/html/642b085c-7269-9f8a-ca4b-7b0275471105.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/642b085c-7269-9f8a-ca4b-7b0275471105.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/642b085c-7269-9f8a-ca4b-7b0275471105.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.GetNoiseCompensationType Method

RFmxSpecAnMXAcpConfigurationGetNoiseCompensationType Method

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
	out RFmxSpecAnMXAcpNoiseCompensationType value
)
```

```text
Public Function GetNoiseCompensationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXAcpNoiseCompensationType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXAcpNoiseCompensationType**
  - Upon return, contains the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

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

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/64951c4b-4719-53a9-6a7a-96d545ae8970.htm language=enus -->
## TOPIC 00236: rfmxspecandotnet/html/64951c4b-4719-53a9-6a7a-96d545ae8970.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/64951c4b-4719-53a9-6a7a-96d545ae8970.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/64951c4b-4719-53a9-6a7a-96d545ae8970.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXTxpConfiguration.ConfigureVbwFilter Method

RFmxSpecAnMXTxpConfigurationConfigureVbwFilter Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureVbwFilter(
	string selectorString,
	RFmxSpecAnMXTxpVbwFilterAutoBandwidth vbwAuto,
	double vbw,
	double vbwToRbwRatio
)
```

```text
Public Function ConfigureVbwFilter ( 
	selectorString As String,
	vbwAuto As RFmxSpecAnMXTxpVbwFilterAutoBandwidth,
	vbw As Double,
	vbwToRbwRatio As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **vbwAuto RFmxSpecAnMXTxpVbwFilterAutoBandwidth**
  - Specifies whether the VBW is expressed directly or computed based on VBW to RBW ratio. This value is expressed in Hz.
- **vbw Double**
  - Specifies the video bandwidth when you set the VBWAuto parameter False. This value is expressed in Hz.
- **vbwToRbwRatio Double**
  - Specifies the VBW to RBW Ratio when you set the VBWAuto parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXTxpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/649dda59-bd48-6c1d-1306-3b42e924c29f.htm language=enus -->
## TOPIC 00237: rfmxspecandotnet/html/649dda59-bd48-6c1d-1306-3b42e924c29f.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/649dda59-bd48-6c1d-1306-3b42e924c29f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/649dda59-bd48-6c1d-1306-3b42e924c29f.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpConfiguration.SetRbwFilterBandwidthDefinition Method

RFmxSpecAnMXChpConfigurationSetRbwFilterBandwidthDefinition Method

SetRbwFilterBandwidth(String, Double)

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterBandwidthDefinition(
	string selectorString,
	RFmxSpecAnMXChpRbwFilterBandwidthDefinition value
)
```

```text
Public Function SetRbwFilterBandwidthDefinition ( 
	selectorString As String,
	value As RFmxSpecAnMXChpRbwFilterBandwidthDefinition
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXChpRbwFilterBandwidthDefinition**
  - Specifies the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(String, Double) method.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPSetRBWFilterBandwidthDefinition() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/64d7194e-7f3a-33a7-39bc-521adfb376e9.htm language=enus -->
## TOPIC 00238: rfmxspecandotnet/html/64d7194e-7f3a-33a7-39bc-521adfb376e9.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/64d7194e-7f3a-33a7-39bc-521adfb376e9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/64d7194e-7f3a-33a7-39bc-521adfb376e9.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMAveragingEnabled Enumeration

RFmxSpecAnMXIMAveragingEnabled Enumeration

Specifies whether to enable averaging for the IM measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxSpecAnMXIMAveragingEnabled
```

```text
Public Enumeration RFmxSpecAnMXIMAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The IM measurement uses the SetAveragingCount(String, Int32) method as the number of acquisitions over which the IM measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/65a28dee-74a7-5f27-456b-4326891c6996.htm language=enus -->
## TOPIC 00239: rfmxspecandotnet/html/65a28dee-74a7-5f27-456b-4326891c6996.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/65a28dee-74a7-5f27-456b-4326891c6996.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/65a28dee-74a7-5f27-456b-4326891c6996.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIMConfiguration.ConfigureAveraging Method

RFmxSpecAnMXIMConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxSpecAnMXIMAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxSpecAnMXIMAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxSpecAnMXIMAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxSpecAnMXIMAveragingType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled RFmxSpecAnMXIMAveragingEnabled**
  - Specifies whether to enable averaging for the measurement.
- **averagingCount Int32**
  - Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.
- **averagingType RFmxSpecAnMXIMAveragingType**
  - Specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types.

###### Return Value

Int32

##### See Also

###### Reference

RFmxSpecAnMXIMConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/65c76757-de42-d7cf-67d8-cda2aad74a09.htm language=enus -->
## TOPIC 00240: rfmxspecandotnet/html/65c76757-de42-d7cf-67d8-cda2aad74a09.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/65c76757-de42-d7cf-67d8-cda2aad74a09.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/65c76757-de42-d7cf-67d8-cda2aad74a09.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.GetConfigurationInput Method

RFmxSpecAnMXDpdApplyDpdGetConfigurationInput Method

Gets whether to use the configuration used by the DPD measurement for applying DPD.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetConfigurationInput(
	string selectorString,
	out RFmxSpecAnMXDpdApplyDpdConfigurationInput value
)
```

```text
Public Function GetConfigurationInput ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXDpdApplyDpdConfigurationInput
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXDpdApplyDpdConfigurationInput**
  - Upon return, contains a value that indicates whether to use the configuration used by the DPD measurement, for applying DPD.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDConfigurationInput() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/66cbeda2-770a-add9-6038-dcaaf46ed286.htm language=enus -->
## TOPIC 00241: rfmxspecandotnet/html/66cbeda2-770a-add9-6038-dcaaf46ed286.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/66cbeda2-770a-add9-6038-dcaaf46ed286.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/66cbeda2-770a-add9-6038-dcaaf46ed286.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpurConfiguration Methods

RFmxSpecAnMXSpurConfiguration Methods

The [RFmxSpecAnMXSpurConfiguration](636953d3-ea42-c054-d286-bd22b264a5de.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the spurious emission (Spur) measurement. |
|  | ConfigureFftWindowType | Configures the FFT window to obtain a spectrum for the spurious emission (Spur) measurement. |
|  | ConfigureNumberOfRanges | Configures the number of ranges. |
|  | ConfigureRangeAbsoluteLimit | Configures the absolute power limits corresponding to the beginning and end of the frequency range. |
|  | ConfigureRangeAbsoluteLimitArray | Configures the absolute power limits corresponding to the beginning and end of the frequency range and specifies whether the absolute limit threshold is a flat line or a line with a slope. |
|  | ConfigureRangeDetector | Configures the detector settings including detector type and the number of points to be detected. Use "range(n)" as the selector string to configure this method. |
|  | ConfigureRangeDetectorArray | Configures an array of the detector settings including detector type and the number of points to be detected. |
|  | ConfigureRangeFrequency | Configures the frequency start and stop values of the range. |
|  | ConfigureRangeFrequencyArray | Configures the frequency start and stop values and specifies whether to enable measurement of the spurious emissions (Spur) in the frequency range. |
|  | ConfigureRangeNumberOfSpursToReport | Configures the number of Spurs that the measurement should report in the frequency range. |
|  | ConfigureRangeNumberOfSpursToReportArray | Configures the array of number of Spurs that the measurement should report in the frequency range. |
|  | ConfigureRangePeakCriteria | Configures the peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur). |
|  | ConfigureRangePeakCriteriaArray | Configures arrays of peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur). |
|  | ConfigureRangeRbwArray | Configures the resolution bandwidth (RBW) filter. |
|  | ConfigureRangeRbwFilter | Configures the resolution bandwidth (RBW) filter. |
|  | ConfigureRangeRelativeAttenuation | Configures the attenuation, in dB, relative to the external attenuation. Use this method to compensate for variations in external attenuation when the offset channels are spread wide in frequency. |
|  | ConfigureRangeRelativeAttenuationArray | Configures an array of attenuation values, in dB, relative to the value of the GetExternalAttenuation(String, Double) method. Use this method to compensate for the variations in external attenuation when offset channels are spread wide in frequency. |
|  | ConfigureRangeSweepTime | Configures the sweep time. |
|  | ConfigureRangeSweepTimeArray | Configures the array of sweep times, in seconds, when you set the SetRangeSweepTimeAuto(String, RFmxSpecAnMXSpurSweepTimeAuto) to False. |
|  | ConfigureRangeVbwFilter | Configures the video bandwidth (VBW) settings including VBW Auto, VBW, and VBW to RBW ratio for the specified range.Use "range(n)" as the selector string to configure this method. |
|  | ConfigureRangeVbwFilterArray | Configures an array of the VBW settings, including VBW Auto, VBW, and VBW to RBW ratio for the specified range. |
|  | ConfigureTraceRangeIndex | Configures the index of the range used to store and retrieve spurious emission (Spur) traces. When you set this method to -1, the measurement stores and retrieves traces for all enabled ranges. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether the traces to be stored and retrieved after performing the spurious emissions (Spur) measurement are enabled. |
|  | GetAmplitudeCorrectionType | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging. |
|  | GetAveragingEnabled | Gets whether averaging for the spurious emission (Spur) measurement is enabled. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spurious emission (Spur) measurement. |
|  | GetFftWindow | Gets the FFT window type used to reduce spectral leakage. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable spurious emission (Spur) measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for spurious emission (Spur) measurement. |
|  | GetNumberOfRanges | Gets the number of range configurations. |
|  | GetRangeAbsoluteLimitMode | Gets whether the absolute limit threshold is a flat line or a line with a slope. |
|  | GetRangeAbsoluteLimitStart | Gets the absolute power limit, in dBm, corresponding to the beginning of the frequency range. |
|  | GetRangeAbsoluteLimitStop | Gets the absolute power limit, in dBm, corresponding to the end of the frequency range. |
|  | GetRangeDetectorPoints | Gets the number of range points after the detector is applied. Use "range(n)" as the selector string to configure or read this method. |
|  | GetRangeDetectorType | Gets the type of detector to be used. Use "range(n)" as the selector string to configure or read this method. |
|  | GetRangeEnabled | Gets whether the spurious emissions are measured in the frequency range. |
|  | GetRangeNumberOfSpursToReport | Gets the number of spurious emissions (Spur) that the measurement should report in the frequency range. |
|  | GetRangePeakExcursion | Gets the peak excursion value for finding the spurs on trace. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered as a spur. |
|  | GetRangePeakThreshold | Gets the threshold level, in dBm, above which the measurement detects spurs in the range that you specify using the SetRangeStartFrequency(String, Double) and SetRangeStopFrequency(String, Double) methods. |
|  | GetRangeRbwFilterAutoBandwidth | Gets whether the measurement computes the resolution bandwidth (RBW). |
|  | GetRangeRbwFilterBandwidth | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal. |
|  | GetRangeRbwFilterBandwidthDefinition | Gets the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(String, Double) method. |
|  | GetRangeRbwFilterType | Gets the shape of the digital resolution bandwidth (RBW) filter. |
|  | GetRangeRelativeAttenuation | Gets the attenuation, in dB, relative to the value of the SetExternalAttenuation(String, Double) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
|  | GetRangeStartFrequency | Gets the start frequency of the frequency range, in hertz (Hz), for the measurement. |
|  | GetRangeStopFrequency | Gets the stop frequency of the frequency range, in hertz (Hz), for the measurement. |
|  | GetRangeSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetRangeSweepTimeInterval | Gets the sweep time, in seconds. |
|  | GetRangeVbwFilterAutoBandwidth | Gets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |
|  | GetRangeVbwFilterBandwidth | Gets the video bandwidth (VBW) in Hz when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to False. |
|  | GetRangeVbwFilterVbwToRbwRatio | Gets the VBW to RBW Ratio when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to True. |
|  | GetTraceRangeIndex | Gets the index of the range used to store and retrieve spurious emission (Spur) traces. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the spurious emissions (Spur) measurement. |
|  | SetAmplitudeCorrectionType | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxSpecAnMXSpurAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the spurious emission (Spur) measurement. |
|  | SetAveragingType | Sets averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spurious emission (Spur) measurement. |
|  | SetFftWindow | Sets the FFT window type used to reduce spectral leakage. |
|  | SetMeasurementEnabled | Sets whether to enable spurious emission (Spur) measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for spurious emission (Spur) measurement. |
|  | SetNumberOfRanges | Sets the number of range configurations. |
|  | SetRangeAbsoluteLimitMode | Sets whether the absolute limit threshold is a flat line or a line with a slope. |
|  | SetRangeAbsoluteLimitStart | Sets the absolute power limit, in dBm, corresponding to the beginning of the frequency range. This power limit is also set as the absolute power limit for the range when you set the SetRangeAbsoluteLimitMode(String, RFmxSpecAnMXSpurAbsoluteLimitMode) to Couple. |
|  | SetRangeAbsoluteLimitStop | Sets the absolute power limit, in dBm, corresponding to the end of the frequency range. This method is ignored when you set the SetRangeAbsoluteLimitMode(String, RFmxSpecAnMXSpurAbsoluteLimitMode) to Couple. |
|  | SetRangeDetectorPoints | Sets the number of range points after the detector is applied. Use "range(n)" as the selector string to configure or read this method. |
|  | SetRangeDetectorType | Sets the type of detector to be used. Use "range(n)" as the selector string to configure or read this method. |
|  | SetRangeEnabled | Sets whether to measure the spurious emissions (Spur) in the frequency range. |
|  | SetRangeNumberOfSpursToReport | Sets the number of spurious emissions (Spur) that the measurement must report in the frequency range. |
|  | SetRangePeakExcursion | Sets the peak excursion value for finding the spurs on the trace. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered as a spur. |
|  | SetRangePeakThreshold | Sets the threshold level, in dBm, above which the measurement detects spurs in the range that you specify using the SetRangeStartFrequency(String, Double) and SetRangeStopFrequency(String, Double) methods. |
|  | SetRangeRbwFilterAutoBandwidth | Sets whether the measurement computes the resolution bandwidth (RBW). |
|  | SetRangeRbwFilterBandwidth | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal. |
|  | SetRangeRbwFilterBandwidthDefinition | Sets the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(String, Double) method. |
|  | SetRangeRbwFilterType | Sets the shape of the digital resolution bandwidth (RBW) filter. |
|  | SetRangeRelativeAttenuation | Sets the attenuation, in dB, relative to the value which you set in the SetExternalAttenuation(String, Double) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
|  | SetRangeStartFrequency | Sets the start frequency of the frequency range, in hertz (Hz), for the measurement. |
|  | SetRangeStopFrequency | Sets the stop frequency of the frequency range, in hertz (Hz), for the measurement. |
|  | SetRangeSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetRangeSweepTimeInterval | Sets the sweep time, in seconds, when you set the SetRangeSweepTimeAuto(String, RFmxSpecAnMXSpurSweepTimeAuto) method to False. |
|  | SetRangeVbwFilterAutoBandwidth | Sets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |
|  | SetRangeVbwFilterBandwidth | Sets the video bandwidth (VBW) in Hz when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to False. |
|  | SetRangeVbwFilterVbwToRbwRatio | Sets the VBW to RBW Ratio when you set the SetRangeVbwFilterAutoBandwidth(String, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) method to True. |
|  | SetTraceRangeIndex | Sets the index of the range used to store and retrieve spurious emission (Spur) traces. This method is not used if you set the spur all traces enabled to FALSE. When you set this method to -1, the measurement stores and retrieves traces for all enabled ranges. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxSpecAnMXSpurConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/66eede61-61f4-18dc-1f63-7ba47b4531cb.htm language=enus -->
## TOPIC 00242: rfmxspecandotnet/html/66eede61-61f4-18dc-1f63-7ba47b4531cb.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/66eede61-61f4-18dc-1f63-7ba47b4531cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/66eede61-61f4-18dc-1f63-7ba47b4531cb.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXSpectrumConfiguration.GetAmplitudeCorrectionType Method

RFmxSpecAnMXSpectrumConfigurationGetAmplitudeCorrectionType Method

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAmplitudeCorrectionType(
	string selectorString,
	out RFmxSpecAnMXSpectrumAmplitudeCorrectionType value
)
```

```text
Public Function GetAmplitudeCorrectionType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXSpectrumAmplitudeCorrectionType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXSpectrumAmplitudeCorrectionType**
  - Upon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

###### Return Value

Int32

##### Remarks

SpectrumAmplitudeCorrectionType

RFCenterFrequency

##### See Also

###### Reference

RFmxSpecAnMXSpectrumConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/670dc278-684f-286b-80fd-1a3a9c0d27d2.htm language=enus -->
## TOPIC 00243: rfmxspecandotnet/html/670dc278-684f-286b-80fd-1a3a9c0d27d2.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/670dc278-684f-286b-80fd-1a3a9c0d27d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/670dc278-684f-286b-80fd-1a3a9c0d27d2.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.SetSynchronizationEstimationStop Method

RFmxSpecAnMXIdpdConfigurationSetSynchronizationEstimationStop Method

Sets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSynchronizationEstimationStop(
	string selectorString,
	double value
)
```

```text
Public Function SetSynchronizationEstimationStop ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

IdpdSynchronizationEstimationStop

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6741c83a-acb6-6969-6788-cc4eea8bb2d0.htm language=enus -->
## TOPIC 00244: rfmxspecandotnet/html/6741c83a-acb6-6969-6788-cc4eea8bb2d0.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6741c83a-acb6-6969-6788-cc4eea8bb2d0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6741c83a-acb6-6969-6788-cc4eea8bb2d0.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXChpResults.FetchTotalCarrierPower Method

RFmxSpecAnMXChpResultsFetchTotalCarrierPower Method

Fetches the total integrated carrier power.

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
  - Upon return, contains the total integrated power of all carriers, in dBm.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_CHPFetchTotalCarrierPower() function in C.

##### See Also

###### Reference

RFmxSpecAnMXChpResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/67f512de-c916-9a99-3f01-a8d83c2640d6.htm language=enus -->
## TOPIC 00245: rfmxspecandotnet/html/67f512de-c916-9a99-3f01-a8d83c2640d6.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/67f512de-c916-9a99-3f01-a8d83c2640d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/67f512de-c916-9a99-3f01-a8d83c2640d6.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXAcpConfiguration.ConfigureCarrierAndOffsets Method

RFmxSpecAnMXAcpConfigurationConfigureCarrierAndOffsets Method

Configures a carrier channel with offset channels on both sides of the carrier as specified by the number of offsets. The offset channels are separated by +/- (n*channel) spacing from the center of the carrier. Power is measured over the integration bandwidth for each channel.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierAndOffsets(
	string selectorString,
	double integrationBandwidth,
	int numberOfOffsets,
	double channelSpacing
)
```

```text
Public Function ConfigureCarrierAndOffsets ( 
	selectorString As String,
	integrationBandwidth As Double,
	numberOfOffsets As Integer,
	channelSpacing As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **integrationBandwidth Double**
  - Specifies the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power.
- **numberOfOffsets Int32**
  - Specifies the number of offset channels.
- **channelSpacing Double**
  - Specifies the spacing between offset channels.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_ACPCfgCarrierAndOffsets() function in C.

##### See Also

###### Reference

RFmxSpecAnMXAcpConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/68025d21-2766-531f-a7aa-e830c69c1d7d.htm language=enus -->
## TOPIC 00246: rfmxspecandotnet/html/68025d21-2766-531f-a7aa-e830c69c1d7d.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/68025d21-2766-531f-a7aa-e830c69c1d7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/68025d21-2766-531f-a7aa-e830c69c1d7d.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXIdpdConfiguration.GetSignalType Method

RFmxSpecAnMXIdpdConfigurationGetSignalType Method

Gets the type of reference waveform.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSignalType(
	string selectorString,
	out RFmxSpecAnMXIdpdSignalType value
)
```

```text
Public Function GetSignalType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxSpecAnMXIdpdSignalType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxSpecAnMXIdpdSignalType**
  - Upon return, contains the type of reference waveform.

###### Return Value

Int32

##### Remarks

IdpdSignalType

Modulated

##### See Also

###### Reference

RFmxSpecAnMXIdpdConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/68261e3d-c534-ceba-0b3d-7edb0664b11e.htm language=enus -->
## TOPIC 00247: rfmxspecandotnet/html/68261e3d-c534-ceba-0b3d-7edb0664b11e.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/68261e3d-c534-ceba-0b3d-7edb0664b11e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/68261e3d-c534-ceba-0b3d-7edb0664b11e.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXDpdApplyDpd.SetUserMemoryPolynomialLeadOrder Method

RFmxSpecAnMXDpdApplyDpdSetUserMemoryPolynomialLeadOrder Method

SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel)

GeneralizedMemoryPolynomial

SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput)

User

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUserMemoryPolynomialLeadOrder(
	string selectorString,
	int value
)
```

```text
Public Function SetUserMemoryPolynomialLeadOrder ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Contains the lead order cross term of the DPD polynomial when you set the SetUserDpdModel(String, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(String, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDUserMemoryPolynomialLeadOrder() function in C.

##### See Also

###### Reference

RFmxSpecAnMXDpdApplyDpd Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/68d0b019-0891-a016-72e5-6d8cf2b43991.htm language=enus -->
## TOPIC 00248: rfmxspecandotnet/html/68d0b019-0891-a016-72e5-6d8cf2b43991.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/68d0b019-0891-a016-72e5-6d8cf2b43991.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/68d0b019-0891-a016-72e5-6d8cf2b43991.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXHarmResults.GetFundamentalFrequency Method

RFmxSpecAnMXHarmResultsGetFundamentalFrequency Method

Gets the frequency, in hertz (Hz), used as the fundamental frequency.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFundamentalFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetFundamentalFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency, in Hz, used as the fundamental frequency.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_HarmGetResultsFundamentalFrequency() function in C.

##### See Also

###### Reference

RFmxSpecAnMXHarmResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/68d5329b-3e26-281a-ab21-daac405dde41.htm language=enus -->
## TOPIC 00249: rfmxspecandotnet/html/68d5329b-3e26-281a-ab21-daac405dde41.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/68d5329b-3e26-281a-ab21-daac405dde41.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/68d5329b-3e26-281a-ab21-daac405dde41.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXPavtConfiguration.SetSegmentMeasurementLength Method

RFmxSpecAnMXPavtConfigurationSetSegmentMeasurementLength Method

SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode)

Variable

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentMeasurementLength(
	string selectorString,
	double value
)
```

```text
Public Function SetSegmentMeasurementLength ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(String, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable.

###### Return Value

Int32

##### Remarks

PavtSegmentMeasurementLength

##### See Also

###### Reference

RFmxSpecAnMXPavtConfiguration Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-specan-dotnet path=rfmxspecandotnet/html/6952cb37-b847-84e0-82a1-ee934f004cf1.htm language=enus -->
## TOPIC 00250: rfmxspecandotnet/html/6952cb37-b847-84e0-82a1-ee934f004cf1.htm

- bundle_id: `rfmx-specan-dotnet`
- source_path: `rfmxspecandotnet/html/6952cb37-b847-84e0-82a1-ee934f004cf1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-dotnet/raw/resource/enus/rfmxspecandotnet/html/6952cb37-b847-84e0-82a1-ee934f004cf1.htm
- document_id: `rfmx-specan-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxSpecAnMXFcntResults.FetchMeasurement Method

RFmxSpecAnMXFcntResultsFetchMeasurement Method

Fetches the frequency and phase measured using the frequency count (Fcnt) measurement.

Namespace:

NationalInstruments.RFmx.SpecAnMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurement(
	string selectorString,
	double timeout,
	out double averageRelativeFrequency,
	out double averageAbsoluteFrequency,
	out double meanPhase
)
```

```text
Public Function FetchMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef averageRelativeFrequency As Double,
	<OutAttribute> ByRef averageAbsoluteFrequency As Double,
	<OutAttribute> ByRef meanPhase As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(String) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **averageRelativeFrequency Double**
  - Upon return, contains the signal frequency relative to the RF center frequency. Only samples above the threshold are used when you set the RFmxSpecAnMXFcntThresholdEnabled to True.
- **averageAbsoluteFrequency Double**
  - Upon return, contains the RF signal frequency.
- **meanPhase Double**
  - Upon return, contains the net phase of the vector sum of the I/Q samples used for frequency measurement.

###### Return Value

Int32

##### Remarks

This method maps to the RFmxSpecAn_FCntFetchMeasurement() function in C.

##### See Also

###### Reference

RFmxSpecAnMXFcntResults Class

NationalInstruments.RFmx.SpecAnMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
