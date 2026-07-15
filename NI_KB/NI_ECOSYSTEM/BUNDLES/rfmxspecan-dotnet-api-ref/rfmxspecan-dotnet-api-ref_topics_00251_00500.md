# NI DOCUMENT BUNDLE: rfmxspecan-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-dotnet-api-ref start=251 end=500 -->
<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00251: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_FCntSetAllTracesEnabled()

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the traces to be stored and retrieved after performing the Fcnt measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00252: SetAveragingCount(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXFcntAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxSpecAnMXFcntAveragingEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingenabled__string-rfmxspecanmxfcntaveragingenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetAveragingCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXFcntAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingenabled__string-rfmxspecanmxfcntaveragingenabled.html language=enus -->
## TOPIC 00253: SetAveragingEnabled(string, RFmxSpecAnMXFcntAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingenabled__string-rfmxspecanmxfcntaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setaveragingenabled__string-rfmxspecanmxfcntaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingEnabled(string selectorString, RFmxSpecAnMXFcntAveragingEnabled value)RemarksThis method maps to the RFmxSpecAn_FCntSetAveragingEnabled() function in

### SetAveragingEnabled(string, RFmxSpecAnMXFcntAveragingEnabled)

Sets whether to enable averaging for the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingEnabled(string selectorString, RFmxSpecAnMXFcntAveragingEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXFcntAveragingEnabled | Specifies whether to enable averaging for the Fcnt measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00254: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_FCntSetMeasurementEnabled() function in C.ParametersNameTypeDescriptionselecto

### SetMeasurementEnabled(string, bool)

Sets whether to enable the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the Fcnt measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00255: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_FCntSetNumberOfAnalysisThreads() function

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for Fcnt measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setrbwfiltertype__string-rfmxspecanmxfcntrbwfiltertype.html language=enus -->
## TOPIC 00256: SetRbwFilterType(string, RFmxSpecAnMXFcntRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setrbwfiltertype__string-rfmxspecanmxfcntrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setrbwfiltertype__string-rfmxspecanmxfcntrbwfiltertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital resolution bandwidth (RBW) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterType(string selectorString, RFmxSpecAnMXFcntRbwFilterType value)RemarksThis method maps to the RFmxSpecAn_FCntSetRBWFilterType() function in C.ParametersNameTypeD

### SetRbwFilterType(string, RFmxSpecAnMXFcntRbwFilterType)

Sets the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterType(string selectorString, RFmxSpecAnMXFcntRbwFilterType value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetRBWFilterType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXFcntRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setthresholdlevel__string-double.html language=enus -->
## TOPIC 00257: SetThresholdLevel(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setthresholdlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setthresholdlevel__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets either the relative or absolute threshold power level based on the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXFcntConfiguration.GetThresholdType(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXFcntThresholdType@) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetTh

### SetThresholdLevel(string, double)

Sets either the relative or absolute threshold power level based on the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXFcntConfiguration.GetThresholdType(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXFcntThresholdType@) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetThresholdLevel(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetThresholdLevel() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies either the relative or absolute threshold power level based on the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXFcntConfiguration.GetThresholdType(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXFcntThresholdType@) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setthresholdtype__string-rfmxspecanmxfcntthresholdtype.html language=enus -->
## TOPIC 00258: SetThresholdType(string, RFmxSpecAnMXFcntThresholdType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setthresholdtype__string-rfmxspecanmxfcntthresholdtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-setthresholdtype__string-rfmxspecanmxfcntthresholdtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference for the power level used for thresholding. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetThresholdType(string selectorString, RFmxSpecAnMXFcntThresholdType value)RemarksThis method maps to the RFmxSpecAn_FCntSetThresholdType() function in C.ParametersNameTypeDesc

### SetThresholdType(string, RFmxSpecAnMXFcntThresholdType)

Sets the reference for the power level used for thresholding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetThresholdType(string selectorString, RFmxSpecAnMXFcntThresholdType value)

#### Remarks

This method maps to the RFmxSpecAn_FCntSetThresholdType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXFcntThresholdType | Specifies the reference for the power level used for thresholding. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults-fetchfrequencytrace__string-double-ref.html language=enus -->
## TOPIC 00259: FetchFrequencyTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults-fetchfrequencytrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults-fetchfrequencytrace__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency trace for frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchFrequencyTrace(string selectorString, double timeout, ref AnalogWaveform< float > frequencyTrace)RemarksThis method maps to the RFmxSpecAn_FCntFetchFrequencyTrace() f

### FetchFrequencyTrace(string, double, ref AnalogWaveform< float >)

Fetches the frequency trace for frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchFrequencyTrace(string selectorString, double timeout, ref AnalogWaveform< float > frequencyTrace)

#### Remarks

This method maps to the RFmxSpecAn_FCntFetchFrequencyTrace() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| frequencyTrace | ref AnalogWaveform< float > | Upon return, contains the frequency trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults-getallandeviation__string-out.html language=enus -->
## TOPIC 00260: GetAllanDeviation(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults-getallandeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults-getallandeviation__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the two-sample deviation of the measured frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllanDeviation(string selectorString, out double value)RemarksThis method gets the value of FcntResultsAllanDeviation attribute.ParametersNameTypeDescriptionselectorStringstringSp

### GetAllanDeviation(string, out double)

Gets the two-sample deviation of the measured frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllanDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [FcntResultsAllanDeviation](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(string)Â method to build the selectorString. |
| value | out double | Upon return, contains the two-sample deviation of the measured frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXFcntResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntthresholdenabled.html language=enus -->
## TOPIC 00261: RFmxSpecAnMXFcntThresholdEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntthresholdenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntthresholdenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable thresholding of the acquired samples to be used for the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXFcntThresholdEnabledMembersNameValueDescriptionFalse0All samples are considered for the Fcnt measurement.

### RFmxSpecAnMXFcntThresholdEnabled Enumeration

Specifies whether to enable thresholding of the acquired samples to be used for the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXFcntThresholdEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | All samples are considered for the Fcnt measurement. |
| True | 1 | The samples above the threshold level specified in the SetThresholdLevel(string, double) method are considered for the Fcnt measurement. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmaveragingtype.html language=enus -->
## TOPIC 00262: RFmxSpecAnMXHarmAveragingType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for the Harmonics measurement. The averaged power trace is used for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXHarmAveragingTypeMembersNameValueDescriptionRms0The power trace is linearly averaged. RMS averaging reduces sign

### RFmxSpecAnMXHarmAveragingType Enumeration

Specifies the averaging type for the Harmonics measurement. The averaged power trace is used for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXHarmAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power trace is averaged in a logarithm scale. |
| Scalar | 2 | The square root of the power trace is averaged. |
| Maximum | 3 | The maximum instantaneous power in the power trace is retained from one acquisition to the next. |
| Minimum | 4 | The minimum instantaneous power in the power trace is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configureaveraging__string-rfmxspecanmxharmaveragingenabled-int-rfmxspecanmxharmaveragingtype.html language=enus -->
## TOPIC 00263: ConfigureAveraging(string, RFmxSpecAnMXHarmAveragingEnabled, int, RFmxSpecAnMXHarmAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configureaveraging__string-rfmxspecanmxharmaveragingenabled-int-rfmxspecanmxharmaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configureaveraging__string-rfmxspecanmxharmaveragingenabled-int-rfmxspecanmxharmaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the Harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureAveraging(string selectorString, RFmxSpecAnMXHarmAveragingEnabled averagingEnabled, int averagingCount, RFmxSpecAnMXHarmAveragingType averagingType)RemarksThis method maps to the

### ConfigureAveraging(string, RFmxSpecAnMXHarmAveragingEnabled, int, RFmxSpecAnMXHarmAveragingType)

Configures averaging for the Harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureAveraging(string selectorString, RFmxSpecAnMXHarmAveragingEnabled averagingEnabled, int averagingCount, RFmxSpecAnMXHarmAveragingType averagingType)

#### Remarks

This method maps to the RFmxSpecAn_HarmCfgAveraging() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxSpecAnMXHarmAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled) method to True. |
| averagingType | RFmxSpecAnMXHarmAveragingType | Specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configurefundamentalmeasurementinterval__string-double.html language=enus -->
## TOPIC 00264: ConfigureFundamentalMeasurementInterval(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configurefundamentalmeasurementinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configurefundamentalmeasurementinterval__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the acquisition time, in seconds, for acquiring the fundamental signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFundamentalMeasurementInterval(string selectorString, double measurementInterval)RemarksThis method maps to the RFmxSpecAn_HarmCfgFundamentalMeasur

### ConfigureFundamentalMeasurementInterval(string, double)

Configures the acquisition time, in seconds, for acquiring the fundamental signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFundamentalMeasurementInterval(string selectorString, double measurementInterval)

#### Remarks

This method maps to the RFmxSpecAn_HarmCfgFundamentalMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the acquisition time, in seconds, for acquiring the fundamental signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configurefundamentalrbw__string-double-rfmxspecanmxharmrbwfiltertype-double.html language=enus -->
## TOPIC 00265: ConfigureFundamentalRbw(string, double, RFmxSpecAnMXHarmRbwFilterType, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configurefundamentalrbw__string-double-rfmxspecanmxharmrbwfiltertype-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-configurefundamentalrbw__string-double-rfmxspecanmxharmrbwfiltertype-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter to be applied on the acquired signal. The bandwidth of the filter specified is used to measure the fundamental signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFundamentalRbw(string selectorString, double rbw, RFmxSpecAnMX

### ConfigureFundamentalRbw(string, double, RFmxSpecAnMXHarmRbwFilterType, double)

Configures the resolution bandwidth (RBW) filter to be applied on the acquired signal. The bandwidth of the filter specified is used to measure the fundamental signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFundamentalRbw(string selectorString, double rbw, RFmxSpecAnMXHarmRbwFilterType rbwFilterType, double rrcAlpha)

#### Remarks

This method maps to the RFmxSpecAn_HarmCfgFundamentalRBW() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbw | double | Specifies the bandwidth, in hertz (Hz), of the RBW filter used to acquire the fundamental signal. |
| rbwFilterType | RFmxSpecAnMXHarmRbwFilterType | Specifies the shape of the digital RBW filter. |
| rrcAlpha | double | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00266: GetAveragingEnabled(string, out RFmxSpecAnMXHarmAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether averaging for the Harmonics measurement is enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXHarmAveragingEnabled value)RemarksThis method maps to the RFmxSpecAn_HarmGetAveragingEnabled() function in C.Parame

### GetAveragingEnabled(string, out RFmxSpecAnMXHarmAveragingEnabled)

Gets whether averaging for the Harmonics measurement is enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXHarmAveragingEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXHarmAveragingEnabled | Upon return, indicates whether averaging for the Harmonics measurement is enabled. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalmeasurementinterval__string-out.html language=enus -->
## TOPIC 00267: GetFundamentalMeasurementInterval(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalmeasurementinterval__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition time, in seconds, for the Harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFundamentalMeasurementInterval(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_HarmGetFundamentalMeasurementInterval() function in C

### GetFundamentalMeasurementInterval(string, out double)

Gets the acquisition time, in seconds, for the Harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFundamentalMeasurementInterval(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetFundamentalMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the acquisition time, in seconds, for the Harmonics measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00268: GetFundamentalRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalrbwfilterbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition bandwidth of the fundamental. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFundamentalRbwFilterBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_HarmGetFundamentalRBWFilterBandwidth() function in C.ParametersNameTypeDe

### GetFundamentalRbwFilterBandwidth(string, out double)

Gets the acquisition bandwidth of the fundamental.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFundamentalRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetFundamentalRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the acquisition bandwidth of the fundamental. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalrbwfiltertype__string-out.html language=enus -->
## TOPIC 00269: GetFundamentalRbwFilterType(string, out RFmxSpecAnMXHarmRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getfundamentalrbwfiltertype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital resolution bandwidth (RBW) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFundamentalRbwFilterType(string selectorString, out RFmxSpecAnMXHarmRbwFilterType value)RemarksThis method maps to the RFmxSpecAn_HarmGetFundamentalRBWFilterType() functio

### GetFundamentalRbwFilterType(string, out RFmxSpecAnMXHarmRbwFilterType)

Gets the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFundamentalRbwFilterType(string selectorString, out RFmxSpecAnMXHarmRbwFilterType value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetFundamentalRBWFilterType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXHarmRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getharmonicenabled__string-out.html language=enus -->
## TOPIC 00270: GetHarmonicEnabled(string, out RFmxSpecAnMXHarmHarmonicEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getharmonicenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getharmonicenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether a particular harmonic for measurement is enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetHarmonicEnabled(string selectorString, out RFmxSpecAnMXHarmHarmonicEnabled value)RemarksThis method maps to the RFmxSpecAn_HarmGetHarmonicEnabled() function in C.ParametersN

### GetHarmonicEnabled(string, out RFmxSpecAnMXHarmHarmonicEnabled)

Gets whether a particular harmonic for measurement is enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetHarmonicEnabled(string selectorString, out RFmxSpecAnMXHarmHarmonicEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetHarmonicEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the harmonic number. Example: "harmonic0". You can use the BuildHarmonicString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXHarmHarmonicEnabled | Upon return, indicates whether a particular harmonic for measurement is enabled. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00271: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether Harmonics measurement is enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_HarmGetMeasurementEnabled() function in C.ParametersNameTypeDescriptionselectorStringstrin

### GetMeasurementEnabled(string, out bool)

Gets whether Harmonics measurement is enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if Harmonics measurement is enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getmeasurementmethod__string-out.html language=enus -->
## TOPIC 00272: GetMeasurementMethod(string, out RFmxSpecAnMXHarmMeasurementMethod)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getmeasurementmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getmeasurementmethod__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method used to perform the harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementMethod(string selectorString, out RFmxSpecAnMXHarmMeasurementMethod value)RemarksThis method gets the value of HarmMeasurementMethod attribute.The default value is Ti

### GetMeasurementMethod(string, out RFmxSpecAnMXHarmMeasurementMethod)

Gets the method used to perform the harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementMethod(string selectorString, out RFmxSpecAnMXHarmMeasurementMethod value)

#### Remarks

This method gets the value of [HarmMeasurementMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [TimeDomain](nationalinstruments-rfmx-specanmx-rfmxspecanmxharmmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXHarmMeasurementMethod | Upon return, contains the method used to perform the harmonics measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnoisecompensationenabled__string-out.html language=enus -->
## TOPIC 00273: GetNoiseCompensationEnabled(string, out RFmxSpecAnMXHarmNoiseCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnoisecompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnoisecompensationenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNoiseCompensationEnabled(string selectorString, out RFmxSpecAnMXHarmNoiseCompensationEnabled value)RemarksThis method ge

### GetNoiseCompensationEnabled(string, out RFmxSpecAnMXHarmNoiseCompensationEnabled)

Gets whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCompensationEnabled(string selectorString, out RFmxSpecAnMXHarmNoiseCompensationEnabled value)

#### Remarks

This method gets the value of [HarmNoiseCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxharmnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXHarmNoiseCompensationEnabled | Upon return, contains whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00274: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for Harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_HarmGetNumberOfAnalysisThreads() function in C.Par

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for Harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for Harmonics measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnumberofharmonics__string-out.html language=enus -->
## TOPIC 00275: GetNumberOfHarmonics(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnumberofharmonics__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-getnumberofharmonics__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of harmonics, including fundamental, to measure. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNumberOfHarmonics(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_HarmGetNumberOfHarmonics() function in C.ParametersNameTypeDescriptionsele

### GetNumberOfHarmonics(string, out int)

Gets the number of harmonics, including fundamental, to measure.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfHarmonics(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetNumberOfHarmonics() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of harmonics, including fundamental, to measure. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00276: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the Harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_HarmSetAllTracesEnabled() function in

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the Harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_HarmSetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the traces to be stored and retrieved after performing the Harmonics measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00277: SetAveragingCount(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingenabled__string-rfmxspecanmxharmaveragingenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxharmaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_HarmSetAveragingCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingenabled__string-rfmxspecanmxharmaveragingenabled.html language=enus -->
## TOPIC 00278: SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingenabled__string-rfmxspecanmxharmaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setaveragingenabled__string-rfmxspecanmxharmaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the Harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingEnabled(string selectorString, RFmxSpecAnMXHarmAveragingEnabled value)RemarksThis method maps to the RFmxSpecAn_HarmSetAveragingEnabled() function in C.ParametersN

### SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled)

Sets whether to enable averaging for the Harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingEnabled(string selectorString, RFmxSpecAnMXHarmAveragingEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_HarmSetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXHarmAveragingEnabled | Specifies whether to enable averaging for the Harmonics measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setnumberofharmonics__string-int.html language=enus -->
## TOPIC 00279: SetNumberOfHarmonics(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setnumberofharmonics__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setnumberofharmonics__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of Harmonics, including fundamental, to measure. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfHarmonics(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_HarmSetNumberOfHarmonics() function in C.ParametersNameTypeDescriptionselector

### SetNumberOfHarmonics(string, int)

Sets the number of Harmonics, including fundamental, to measure.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfHarmonics(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_HarmSetNumberOfHarmonics() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of Harmonics, including fundamental, to measure. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration.html language=enus -->
## TOPIC 00280: RFmxSpecAnMXHarmConfiguration Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the Harmonics measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXHarmConfiguration : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny

### RFmxSpecAnMXHarmConfiguration Class

Provides methods to configure the Harmonics measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXHarmConfiguration : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAutoHarmonics(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) | Configures auto configuration of successive harmonics. |
| ConfigureAveraging(string, RFmxSpecAnMXHarmAveragingEnabled, int, RFmxSpecAnMXHarmAveragingType) | Configures averaging for the Harmonics measurement. |
| ConfigureFundamentalMeasurementInterval(string, double) | Configures the acquisition time, in seconds, for acquiring the fundamental signal. |
| ConfigureFundamentalRbw(string, double, RFmxSpecAnMXHarmRbwFilterType, double) | Configures the resolution bandwidth (RBW) filter to be applied on the acquired signal. The bandwidth of the filter specified is used to measure the fundamental signal. |
| ConfigureHarmonic(string, int, double, RFmxSpecAnMXHarmHarmonicEnabled, double) | Configures the harmonic frequency, acquisition bandwidth, and acquisition time for the harmonic, when you set the SetAutoSetupEnabled(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) method to False. |
| ConfigureHarmonicArray(string, int[], double[], RFmxSpecAnMXHarmHarmonicEnabled[], double[]) | Configures the harmonic frequency, acquisition bandwidth, and acquisition time for the harmonic, when you set the SetAutoSetupEnabled(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) method to False. |
| ConfigureNumberOfHarmonics(string, int) | Configures the number of harmonics, including fundamental, to measure. |
| GetAllTracesEnabled(string, out bool) | Gets whether the traces to be stored and retrieved after performing the Harmonics measurement are enabled. |
| GetAutoSetupEnabled(string, out RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) | Gets whether auto configuration of successive harmonics is enabled. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging. |
| GetAveragingEnabled(string, out RFmxSpecAnMXHarmAveragingEnabled) | Gets whether averaging for the Harmonics measurement is enabled. |
| GetAveragingType(string, out RFmxSpecAnMXHarmAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. |
| GetFundamentalMeasurementInterval(string, out double) | Gets the acquisition time, in seconds, for the Harmonics measurement. |
| GetFundamentalRbwFilterAlpha(string, out double) | Gets the roll-off factor for the root-raised-cosine (RRC) filter. |
| GetFundamentalRbwFilterBandwidth(string, out double) | Gets the acquisition bandwidth of the fundamental. |
| GetFundamentalRbwFilterType(string, out RFmxSpecAnMXHarmRbwFilterType) | Gets the shape of the digital resolution bandwidth (RBW) filter. |
| GetHarmonicBandwidth(string, out double) | Gets the resolution bandwidth, in hertz (Hz), for the harmonic. |
| GetHarmonicEnabled(string, out RFmxSpecAnMXHarmHarmonicEnabled) | Gets whether a particular harmonic for measurement is enabled. |
| GetHarmonicMeasurementInterval(string, out double) | Gets the acquisition time, in seconds, for the harmonic. |
| GetHarmonicOrder(string, out int) | Gets the order of the harmonic. |
| GetMeasurementEnabled(string, out bool) | Gets whether Harmonics measurement is enabled. |
| GetMeasurementMethod(string, out RFmxSpecAnMXHarmMeasurementMethod) | Gets the method used to perform the harmonics measurement. |
| GetNoiseCompensationEnabled(string, out RFmxSpecAnMXHarmNoiseCompensationEnabled) | Gets whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for Harmonics measurement. |
| GetNumberOfHarmonics(string, out int) | Gets the number of harmonics, including fundamental, to measure. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the Harmonics measurement. |
| SetAutoSetupEnabled(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) | Sets whether to enable auto configuration of successive harmonics. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxSpecAnMXHarmAveragingEnabled) | Sets whether to enable averaging for the Harmonics measurement. |
| SetAveragingType(string, RFmxSpecAnMXHarmAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for Harmonics measurement. |
| SetFundamentalMeasurementInterval(string, double) | Sets the acquisition time, in seconds, for the Harmonics measurement. |
| SetFundamentalRbwFilterAlpha(string, double) | Sets the roll-off factor for the root-raised-cosine (RRC) filter. |
| SetFundamentalRbwFilterBandwidth(string, double) | Sets the resolution bandwidth (RBW) filter to be applied on the acquired signal. The bandwidth of the filter specified is applicable for fundamental signal. |
| SetFundamentalRbwFilterType(string, RFmxSpecAnMXHarmRbwFilterType) | Sets the shape of the digital resolution bandwidth (RBW) filter. |
| SetHarmonicBandwidth(string, double) | Sets the resolution bandwidth, in hertz (Hz), for the harmonic. The value set by this method is not used if you set the SetAutoSetupEnabled(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) method to True. |
| SetHarmonicEnabled(string, RFmxSpecAnMXHarmHarmonicEnabled) | Sets whether to enable a particular harmonic for measurement. Only the enabled Harmonics are used to measure the total harmonic distortion (THD). |
| SetHarmonicMeasurementInterval(string, double) | Sets the acquisition time, in seconds, for the harmonic. |
| SetHarmonicOrder(string, int) | Sets the order of the harmonic. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the Harmonics measurement. |
| SetMeasurementMethod(string, RFmxSpecAnMXHarmMeasurementMethod) | Sets the method used to perform the harmonics measurement. |
| SetNoiseCompensationEnabled(string, RFmxSpecAnMXHarmNoiseCompensationEnabled) | Sets whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for Harmonics measurement. |
| SetNumberOfHarmonics(string, int) | Sets the number of Harmonics, including fundamental, to measure. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmharmonicenabled.html language=enus -->
## TOPIC 00281: RFmxSpecAnMXHarmHarmonicEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmharmonicenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmharmonicenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable a particular harmonic for measurement. Only the enabled Harmonics are used to measure the total harmonic distortion (THD). This enum is not used if you set the SetAutoSetupEnabled(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) to True. SyntaxNamespace: NationalInstrum

### RFmxSpecAnMXHarmHarmonicEnabled Enumeration

Specifies whether to enable a particular harmonic for measurement. Only the enabled Harmonics are used to measure the total harmonic distortion (THD). This enum is not used if you set the [SetAutoSetupEnabled(string, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxharmconfiguration-setautosetupenabled__string-rfmxspecanmxharmautoharmonicssetupenabled.html) to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxharmautoharmonicssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXHarmHarmonicEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the harmonic for measurement. |
| True | 1 | Enables the harmonic for measurement. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmmeasurementmethod.html language=enus -->
## TOPIC 00282: RFmxSpecAnMXHarmMeasurementMethod Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmmeasurementmethod.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to perform the harmonics measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXHarmMeasurementMethodMembersNameValueDescriptionTimeDomain0The harmonics measurement acquires the signal using the same signal analyzer setting across frequency b

### RFmxSpecAnMXHarmMeasurementMethod Enumeration

Specifies the method used to perform the harmonics measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXHarmMeasurementMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TimeDomain | 0 | The harmonics measurement acquires the signal using the same signal analyzer setting across frequency bands. Use this method when the measurement speed is desirable over higher dynamic range. |
| DynamicRange | 2 | The harmonics measurement acquires the signal using the hardware-specific features, such as the IF filter and IF gain, for different frequency bands. Use this method to get the best dynamic range. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmnoisecompensationenabled.html language=enus -->
## TOPIC 00283: RFmxSpecAnMXHarmNoiseCompensationEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmnoisecompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXHarmNoiseCompensationEnabledMembersNameValueDescriptionFalse0Disables compensation of the average harmoni

### RFmxSpecAnMXHarmNoiseCompensationEnabled Enumeration

Specifies whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXHarmNoiseCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables compensation of the average harmonic powers for the noise floor of the signal analyzer. |
| True | 1 | Enables compensation of the average harmonic powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the harmonics measurement and cached for future use. If the signal analyzer or measurement parameters change, noise floors are measured again. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-fetchharmonicmeasurement__string-double-out-out-out-out.html language=enus -->
## TOPIC 00284: FetchHarmonicMeasurement(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-fetchharmonicmeasurement__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-fetchharmonicmeasurement__string-double-out-out-out-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power measured at the harmonic frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchHarmonicMeasurement(string selectorString, double timeout, out double averageRelativePower, out double averageAbsolutePower, out double rbw, out double frequency)RemarksThis method

### FetchHarmonicMeasurement(string, double, out double, out double, out double, out double)

Fetches the power measured at the harmonic frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchHarmonicMeasurement(string selectorString, double timeout, out double averageRelativePower, out double averageAbsolutePower, out double rbw, out double frequency)

#### Remarks

This method maps to the RFmxSpecAn_HarmFetchHarmonicMeasurement() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and harmonic number. Example: "harmonic0", "result::r1/harmonic0". You can use the BuildHarmonicString2(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| averageRelativePower | out double | Upon return, contains the average power, in dB, relative to the fundamental power measured at the harmonic. |
| averageAbsolutePower | out double | Upon return, contains the average absolute power, in dBm, measured at the harmonic. |
| rbw | out double | Upon return, contains the resolution bandwidth (RBW), in hertz (Hz), which is used by the harmonic measurement, for the harmonic. |
| frequency | out double | Upon return, contains the RF frequency, in Hz, of the harmonic. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-fetchharmonicmeasurementarray__string-double-ref-ref-ref-ref.html language=enus -->
## TOPIC 00285: FetchHarmonicMeasurementArray(string, double, ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-fetchharmonicmeasurementarray__string-double-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-fetchharmonicmeasurementarray__string-double-ref-ref-ref-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power measured at the harmonic frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchHarmonicMeasurementArray(string selectorString, double timeout, ref double[] averageRelativePower, ref double[] averageAbsolutePower, ref double[] rbw, ref double[] frequency)Remar

### FetchHarmonicMeasurementArray(string, double, ref double[], ref double[], ref double[], ref double[])

Fetches the power measured at the harmonic frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchHarmonicMeasurementArray(string selectorString, double timeout, ref double[] averageRelativePower, ref double[] averageAbsolutePower, ref double[] rbw, ref double[] frequency)

#### Remarks

This method maps to the RFmxSpecAn_HarmFetchHarmonicMeasurementArray() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| averageRelativePower | ref double[] | Upon return, contains the array of average power, in dB, relative to the fundamental power measured at the harmonic. |
| averageAbsolutePower | ref double[] | Upon return, contains the array of average absolute power, in dBm, measured at the harmonic. |
| rbw | ref double[] | Upon return, contains the array of resolution bandwidth (RBW), in hertz (Hz), which is used by the harmonic measurement, for the harmonic. |
| frequency | ref double[] | Upon return, contains the array of RF frequency, in Hz, of the harmonic. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-getharmonicaveragerelativepower__string-out.html language=enus -->
## TOPIC 00286: GetHarmonicAverageRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-getharmonicaveragerelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-getharmonicaveragerelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power, in dB, relative to the fundamental power measured at the harmonic specified by the selector string. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetHarmonicAverageRelativePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_H

### GetHarmonicAverageRelativePower(string, out double)

Gets the average power, in dB, relative to the fundamental power measured at the harmonic specified by the selector string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetHarmonicAverageRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetResultsHarmonicAverageRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and harmonic number. Example: "harmonic0", "result::r1/harmonic0". You can use the BuildHarmonicString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power, in dB, relative to the fundamental power measured at the harmonic specified by the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-getharmonicrbw__string-out.html language=enus -->
## TOPIC 00287: GetHarmonicRbw(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-getharmonicrbw__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxharmresults-getharmonicrbw__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resolution bandwidth (RBW), in hertz (Hz), which is used by the Harmonics measurement, for the harmonic specified by the selector string. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetHarmonicRbw(string selectorString, out double value)RemarksThis method maps to the RFmxSp

### GetHarmonicRbw(string, out double)

Gets the resolution bandwidth (RBW), in hertz (Hz), which is used by the Harmonics measurement, for the harmonic specified by the selector string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetHarmonicRbw(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_HarmGetResultsHarmonicRBW() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and harmonic number. Example: "harmonic0", "result::r1/harmonic0". You can use the BuildHarmonicString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the RBW, in Hz, which is used by the Harmonics measurement, for the harmonic specified by the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXHarmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdaveragingenabled.html language=enus -->
## TOPIC 00288: RFmxSpecAnMXIdpdAveragingEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the IDPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIdpdAveragingEnabledMembersNameValueDescriptionFalse0The number of acquisitions is 1. True1the measurement uses Averaging Count for the number of acquisitions ove

### RFmxSpecAnMXIdpdAveragingEnabled Enumeration

Specifies whether to enable averaging for the IDPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIdpdAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The number of acquisitions is 1. |
| True | 1 | the measurement uses Averaging Count for the number of acquisitions over which the measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00289: GetAveragingCount(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when Averaging Enabled is TRUE. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of IdpdAveragingCount attribute.The default value is 10.ParametersN

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when Averaging Enabled is TRUE.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [IdpdAveragingCount](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when Averaging Enabled is TRUE. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getreferencewaveformidledurationpresent__string-out.html language=enus -->
## TOPIC 00290: GetReferenceWaveformIdleDurationPresent(string, out RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getreferencewaveformidledurationpresent__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getreferencewaveformidledurationpresent__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the reference waveform contains idle duration or dead time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetReferenceWaveformIdleDurationPresent(string selectorString, out RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent value)RemarksThis method gets the value of Idp

### GetReferenceWaveformIdleDurationPresent(string, out RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent)

Gets whether the reference waveform contains idle duration or dead time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetReferenceWaveformIdleDurationPresent(string selectorString, out RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent value)

#### Remarks

This method gets the value of [IdpdReferenceWaveformIdleDurationPresent](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdreferencewaveformidledurationpresent.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent | Upon return, contains whether the reference waveform contains idle duration or dead time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getsynchronizationestimationstop__string-out.html language=enus -->
## TOPIC 00291: GetSynchronizationEstimationStop(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getsynchronizationestimationstop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-getsynchronizationestimationstop__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSynchronizationEstimationStop(string selectorString, out double value)RemarksThis method

### GetSynchronizationEstimationStop(string, out double)

Gets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSynchronizationEstimationStop(string selectorString, out double value)

#### Remarks

This method gets the value of [IdpdSynchronizationEstimationStop](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-gettargetgain__string-out.html language=enus -->
## TOPIC 00292: GetTargetGain(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-gettargetgain__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-gettargetgain__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Target gain when the configured pre-distorted waveform is non-empty. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetTargetGain(string selectorString, out double value)RemarksThis method gets the value of IdpdTargetGain attribute.The default value is 20.ParametersNameTypeDes

### GetTargetGain(string, out double)

Gets the Target gain when the configured pre-distorted waveform is non-empty.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetTargetGain(string selectorString, out double value)

#### Remarks

This method gets the value of [IdpdTargetGain](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the Target gain when the configured pre-distorted waveform is non-empty. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setequalizerfilterlength__string-int.html language=enus -->
## TOPIC 00293: SetEqualizerFilterLength(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setequalizerfilterlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setequalizerfilterlength__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length of the equalizer filter to be trained. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetEqualizerFilterLength(string selectorString, int value)RemarksThis method sets the value of IdpdEqualizerFilterLength attribute.The default value is 101.Valid values are 1 to 4096,

### SetEqualizerFilterLength(string, int)

Sets the length of the equalizer filter to be trained.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetEqualizerFilterLength(string selectorString, int value)

#### Remarks

This method sets the value of [IdpdEqualizerFilterLength](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 101.Valid values are 1 to 4096, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the length of the equalizer filter to be trained. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setevmenabled__string-rfmxspecanmxidpdevmenabled.html language=enus -->
## TOPIC 00294: SetEvmEnabled(string, RFmxSpecAnMXIdpdEvmEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setevmenabled__string-rfmxspecanmxidpdevmenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setevmenabled__string-rfmxspecanmxidpdevmenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable EVM computation. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetEvmEnabled(string selectorString, RFmxSpecAnMXIdpdEvmEnabled value)RemarksThis method sets the value of IdpdEvmEnabled attribute.The default value is False.ParametersNameTypeDescriptionselectorStr

### SetEvmEnabled(string, RFmxSpecAnMXIdpdEvmEnabled)

Sets whether to enable EVM computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetEvmEnabled(string selectorString, RFmxSpecAnMXIdpdEvmEnabled value)

#### Remarks

This method sets the value of [IdpdEvmEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdevmenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIdpdEvmEnabled | Specifies whether to enable EVM computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setgainexpansion__string-double.html language=enus -->
## TOPIC 00295: SetGainExpansion(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setgainexpansion__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setgainexpansion__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetGainExpansion(string selectorString, double value)RemarksIdpdTargetGainThis method sets the value of IdpdGainExpan

### SetGainExpansion(string, double)

Sets the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetGainExpansion(string selectorString, double value)

#### Remarks

IdpdTargetGain

This method sets the value of [IdpdGainExpansion](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 6.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxidpdmeasurementsampleratemode.html language=enus -->
## TOPIC 00296: SetMeasurementSampleRateMode(string, RFmxSpecAnMXIdpdMeasurementSampleRateMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxidpdmeasurementsampleratemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxidpdmeasurementsampleratemode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets acquisition sample rate configuration mode. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementSampleRateMode(string selectorString, RFmxSpecAnMXIdpdMeasurementSampleRateMode value)RemarksThis method sets the value of IdpdMeasurementSampleRateMode attribute.The default v

### SetMeasurementSampleRateMode(string, RFmxSpecAnMXIdpdMeasurementSampleRateMode)

Sets acquisition sample rate configuration mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementSampleRateMode(string selectorString, RFmxSpecAnMXIdpdMeasurementSampleRateMode value)

#### Remarks

This method sets the value of [IdpdMeasurementSampleRateMode](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [ReferenceWaveform](nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdmeasurementsampleratemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIdpdMeasurementSampleRateMode | Specifies acquisition sample rate configuration mode. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00297: SetNumberofAnalysisThreads(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the IDPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberofAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of IdpdNumberofAnalysisThreads attribute.The default value is 1

### SetNumberofAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the IDPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberofAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [IdpdNumberofAnalysisThreads](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the IDPD measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setpowerlinearitytradeoff__string-double.html language=enus -->
## TOPIC 00298: SetPowerLinearityTradeoff(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setpowerlinearitytradeoff__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setpowerlinearitytradeoff__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetPowerLinearityTradeoff(string selectorString, double value)RemarksThis method sets the va

### SetPowerLinearityTradeoff(string, double)

Sets the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetPowerLinearityTradeoff(string selectorString, double value)

#### Remarks

This method sets the value of [IdpdPowerLinearityTradeoff](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 50.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setreferencewaveformidledurationpresent__string-rfmxspecanmxidpdreferencewaveformidledurationpresent.html language=enus -->
## TOPIC 00299: SetReferenceWaveformIdleDurationPresent(string, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setreferencewaveformidledurationpresent__string-rfmxspecanmxidpdreferencewaveformidledurationpresent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setreferencewaveformidledurationpresent__string-rfmxspecanmxidpdreferencewaveformidledurationpresent.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the reference waveform contains idle duration or dead time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetReferenceWaveformIdleDurationPresent(string selectorString, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent value)RemarksThis method sets the value of IdpdRef

### SetReferenceWaveformIdleDurationPresent(string, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent)

Sets whether the reference waveform contains idle duration or dead time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetReferenceWaveformIdleDurationPresent(string selectorString, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent value)

#### Remarks

This method sets the value of [IdpdReferenceWaveformIdleDurationPresent](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdreferencewaveformidledurationpresent.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent | Specifies whether the reference waveform contains idle duration or dead time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setsignaltype__string-rfmxspecanmxidpdsignaltype.html language=enus -->
## TOPIC 00300: SetSignalType(string, RFmxSpecAnMXIdpdSignalType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setsignaltype__string-rfmxspecanmxidpdsignaltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setsignaltype__string-rfmxspecanmxidpdsignaltype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of reference waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSignalType(string selectorString, RFmxSpecAnMXIdpdSignalType value)RemarksThis method sets the value of IdpdSignalType attribute.The default value is Modulated.ParametersNameTypeDescriptionselectorSt

### SetSignalType(string, RFmxSpecAnMXIdpdSignalType)

Sets the type of reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSignalType(string selectorString, RFmxSpecAnMXIdpdSignalType value)

#### Remarks

This method sets the value of [IdpdSignalType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Modulated](nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdsignaltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIdpdSignalType | Specifies the type of reference waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setsynchronizationestimationstop__string-double.html language=enus -->
## TOPIC 00301: SetSynchronizationEstimationStop(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setsynchronizationestimationstop__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setsynchronizationestimationstop__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSynchronizationEstimationStop(string selectorString, double value)RemarksThis method sets

### SetSynchronizationEstimationStop(string, double)

Sets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSynchronizationEstimationStop(string selectorString, double value)

#### Remarks

This method sets the value of [IdpdSynchronizationEstimationStop](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-settargetgain__string-double.html language=enus -->
## TOPIC 00302: SetTargetGain(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-settargetgain__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-settargetgain__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Target gain when the configured pre-distorted waveform is non-empty. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetTargetGain(string selectorString, double value)RemarksThis method sets the value of IdpdTargetGain attribute.The default value is 20.ParametersNameTypeDescrip

### SetTargetGain(string, double)

Sets the Target gain when the configured pre-distorted waveform is non-empty.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetTargetGain(string selectorString, double value)

#### Remarks

This method sets the value of [IdpdTargetGain](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the Target gain when the configured pre-distorted waveform is non-empty. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration.html language=enus -->
## TOPIC 00303: RFmxSpecAnMXIdpdConfiguration Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the IDPD measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXIdpdConfiguration : RFmxSpecAnMXSubObjectMethodsNameDescriptionConfigureEqualizerCoefficients(string, double, double, ComplexSingle[])Config

### RFmxSpecAnMXIdpdConfiguration Class

Provides methods to configure the IDPD measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXIdpdConfiguration : RFmxSpecAnMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureEqualizerCoefficients(string, double, double, ComplexSingle[]) | Configures the equalizer coefficients for the IDPD measurement. |
| ConfigurePredistortedWaveform(string, ComplexWaveform< ComplexSingle >, double) | Configures the predistorted waveform for the IDPD measurement. |
| ConfigureReferenceWaveform(string, ComplexWaveform< ComplexSingle >, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent, RFmxSpecAnMXIdpdSignalType) | Configures the reference waveform for the IDPD measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the IDPD measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when Averaging Enabled is TRUE. |
| GetAveragingEnabled(string, out RFmxSpecAnMXIdpdAveragingEnabled) | Gets whether to enable averaging for the IDPD measurement. |
| GetDutAverageInputPower(string, out double) | Gets the initial (first itertion) average power of the signal at the input port of the device under test. |
| GetEqualizerFilterLength(string, out int) | Gets the length of the equalizer filter to be trained. |
| GetEqualizerMode(string, out RFmxSpecAnMXIdpdEqualizerMode) | Gets whether to enable equalization. |
| GetEvmEnabled(string, out RFmxSpecAnMXIdpdEvmEnabled) | Gets whether to enable EVM computation. |
| GetEvmUnit(string, out RFmxSpecAnMXIdpdEvmUnit) | Gets the units of the EVM results. |
| GetGainExpansion(string, out double) | Gets the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB. |
| GetImpairmentEstimationStart(string, out double) | Gets the start time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| GetImpairmentEstimationStop(string, out double) | Gets the stop time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable IDPD measurement. |
| GetMeasurementSampleRate(string, out double) | Gets the acquisition sample rate, in S/s, when you set the SetMeasurementSampleRateMode(string, RFmxSpecAnMXIdpdMeasurementSampleRateMode) is User. Users should read back the actual sample rate used by the measurement. Actual sample rate may differ from requested sample rate in order to ensure a waveform is phase continuous. |
| GetMeasurementSampleRateMode(string, out RFmxSpecAnMXIdpdMeasurementSampleRateMode) | Gets acquisition sample rate configuration mode. |
| GetNumberofAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the IDPD measurement. |
| GetPowerLinearityTradeoff(string, out double) | Gets the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage. |
| GetReferenceWaveformIdleDurationPresent(string, out RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent) | Gets whether the reference waveform contains idle duration or dead time. |
| GetSignalType(string, out RFmxSpecAnMXIdpdSignalType) | Gets the type of reference waveform. |
| GetSynchronizationEstimationStart(string, out double) | Gets the start time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| GetSynchronizationEstimationStop(string, out double) | Gets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| GetTargetGain(string, out double) | Gets the Target gain when the configured pre-distorted waveform is non-empty. |
| LoadReferenceWaveformFromTdmsFile(string, string, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent, RFmxSpecAnMXIdpdSignalType, int) |  |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the IDPD measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when Averaging Enabled is TRUE. |
| SetAveragingEnabled(string, RFmxSpecAnMXIdpdAveragingEnabled) | Sets whether to enable averaging for the IDPD measurement. |
| SetDutAverageInputPower(string, double) | Sets the initial (first itertion) average power of the signal at the input port of the device under test. |
| SetEqualizerFilterLength(string, int) | Sets the length of the equalizer filter to be trained. |
| SetEqualizerMode(string, RFmxSpecAnMXIdpdEqualizerMode) | Sets whether to enable equalization. |
| SetEvmEnabled(string, RFmxSpecAnMXIdpdEvmEnabled) | Sets whether to enable EVM computation. |
| SetEvmUnit(string, RFmxSpecAnMXIdpdEvmUnit) | Sets the units of the EVM results. |
| SetGainExpansion(string, double) | Sets the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB. |
| SetImpairmentEstimationStart(string, double) | Sets the start time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| SetImpairmentEstimationStop(string, double) | Sets the stop time of the impairment estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable IDPD measurement. |
| SetMeasurementSampleRate(string, double) | Sets the acquisition sample rate, in S/s, when you set the SetMeasurementSampleRateMode(string, RFmxSpecAnMXIdpdMeasurementSampleRateMode) is User. Users should read back the actual sample rate used by the measurement. Actual sample rate may differ from requested sample rate in order to ensure a waveform is phase continuous. |
| SetMeasurementSampleRateMode(string, RFmxSpecAnMXIdpdMeasurementSampleRateMode) | Sets acquisition sample rate configuration mode. |
| SetNumberofAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the IDPD measurement. |
| SetPowerLinearityTradeoff(string, double) | Sets the gain tradeoff factor x such that target gain= x *Gain_at_max Power+ (1-x)*Gain_at_max_Linearity. This value is expressed as a percentage. |
| SetReferenceWaveformIdleDurationPresent(string, RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent) | Sets whether the reference waveform contains idle duration or dead time. |
| SetSignalType(string, RFmxSpecAnMXIdpdSignalType) | Sets the type of reference waveform. |
| SetSynchronizationEstimationStart(string, double) | Sets the start time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| SetSynchronizationEstimationStop(string, double) | Sets the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. |
| SetTargetGain(string, double) | Sets the Target gain when the configured pre-distorted waveform is non-empty. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdequalizermode.html language=enus -->
## TOPIC 00304: RFmxSpecAnMXIdpdEqualizerMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdequalizermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdequalizermode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable equalization. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIdpdEqualizerModeMembersNameValueDescriptionOff0Equalization filter is not applied. Train1Train Equalization filter. The filter length is obtained from the IDPD Equalizer Filter Length

### RFmxSpecAnMXIdpdEqualizerMode Enumeration

Specifies whether to enable equalization.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIdpdEqualizerMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | Equalization filter is not applied. |
| Train | 1 | Train Equalization filter. The filter length is obtained from the IDPD Equalizer Filter Length method. |
| Hold | 2 | The NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIdpdConfiguration.ConfigureEqualizerCoefficients(string,double,double,NationalInstruments.ComplexSingle[]) function specifies the filter that acts as the equalization filter. This filter is applied prior to calculating the predistorted waveform. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdevmenabled.html language=enus -->
## TOPIC 00305: RFmxSpecAnMXIdpdEvmEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdevmenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdevmenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable EVM computation. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIdpdEvmEnabledMembersNameValueDescriptionFalse0Disables EVM computation. NaN is returned for Mean RMS EVM. True1Enables EVM computation.

### RFmxSpecAnMXIdpdEvmEnabled Enumeration

Specifies whether to enable EVM computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIdpdEvmEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables EVM computation. NaN is returned for Mean RMS EVM. |
| True | 1 | Enables EVM computation. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdmeasurementsampleratemode.html language=enus -->
## TOPIC 00306: RFmxSpecAnMXIdpdMeasurementSampleRateMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdmeasurementsampleratemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdmeasurementsampleratemode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies acquisition sample rate configuration mode. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIdpdMeasurementSampleRateModeMembersNameValueDescriptionUser0Acquisition sample rate is defined by the IDPD Meas Sample Rate (S/s) method. ReferenceWaveform1Acquisition sam

### RFmxSpecAnMXIdpdMeasurementSampleRateMode Enumeration

Specifies acquisition sample rate configuration mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIdpdMeasurementSampleRateMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| User | 0 | Acquisition sample rate is defined by the IDPD Meas Sample Rate (S/s) method. |
| ReferenceWaveform | 1 | Acquisition sample rate is set to match the sample rate of the reference waveform. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdreferencewaveformidledurationpresent.html language=enus -->
## TOPIC 00307: RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdreferencewaveformidledurationpresent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdreferencewaveformidledurationpresent.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference waveform contains idle duration or dead time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresentMembersNameValueDescriptionFalse0Reference waveform has no idle duration. True1Reference waveform contains i

### RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent Enumeration

Specifies whether the reference waveform contains idle duration or dead time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIdpdReferenceWaveformIdleDurationPresent

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Reference waveform has no idle duration. |
| True | 1 | Reference waveform contains idle duration. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchequalizercoefficients__string-double-ref.html language=enus -->
## TOPIC 00308: FetchEqualizerCoefficients(string, double, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchequalizercoefficients__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchequalizercoefficients__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the trained equalizer coefficients.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchEqualizerCoefficients(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > equalizerCoefficients)ParametersNameTypeDescriptionselectorStringstringPass an empty string.

### FetchEqualizerCoefficients(string, double, ref ComplexWaveform< ComplexSingle >)

Fetches the trained equalizer coefficients.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchEqualizerCoefficients(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > equalizerCoefficients)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| equalizerCoefficients | ref ComplexWaveform< ComplexSingle > | Upon return, contains the equalizer coefficients. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchpredistortedwaveform__string-double-ref-out-out-out.html language=enus -->
## TOPIC 00309: FetchPredistortedWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out double, out double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchpredistortedwaveform__string-double-ref-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchpredistortedwaveform__string-double-ref-out-out-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the predistorted waveform output after the IDPD measurement.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchPredistortedWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > predistortedWaveform, out double papr, out double powerOffset, out do

### FetchPredistortedWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out double, out double, out double)

Fetches the predistorted waveform output after the IDPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchPredistortedWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > predistortedWaveform, out double papr, out double powerOffset, out double gain)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| predistortedWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the predistorted waveform output after the measurement. |
| papr | out double | Upon return, contains the peak-to-average power ratio of the waveform obtained after applying digital predistortion. This value is expressed in dB. |
| powerOffset | out double | Upon return, contains the change in the average power in the waveform due to applying digital predistortion. This value is expressed in dB. |
| gain | out double | Upon return, contains the gain of the device under test. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchprocessedmeanacquiredwaveform__string-double-ref.html language=enus -->
## TOPIC 00310: FetchProcessedMeanAcquiredWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchprocessedmeanacquiredwaveform__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchprocessedmeanacquiredwaveform__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchProcessedMeanAcquiredWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > pr

### FetchProcessedMeanAcquiredWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchProcessedMeanAcquiredWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > processedMeanAcquiredWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| processedMeanAcquiredWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchprocessedreferencewaveform__string-double-ref.html language=enus -->
## TOPIC 00311: FetchProcessedReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchprocessedreferencewaveform__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-fetchprocessedreferencewaveform__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform used to perform the IDPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchProcessedReferenceWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > processedReferenceWaveform)ParametersNameTypeDescriptionselect

### FetchProcessedReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

Fetches the reference waveform used to perform the IDPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchProcessedReferenceWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > processedReferenceWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| processedReferenceWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the segment of the reference waveform used to perform the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getequalizerreferencewaveform__string-ref-out.html language=enus -->
## TOPIC 00312: GetEqualizerReferenceWaveform(string, ref ComplexWaveform< ComplexSingle >, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getequalizerreferencewaveform__string-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getequalizerreferencewaveform__string-ref-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the equalizer reference waveform used to perform the IDPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetEqualizerReferenceWaveform(string selectorString, ref ComplexWaveform< ComplexSingle > equalizerReferenceWaveform, out double papr)ParametersNameTypeDescription

### GetEqualizerReferenceWaveform(string, ref ComplexWaveform< ComplexSingle >, out double)

Gets the equalizer reference waveform used to perform the IDPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetEqualizerReferenceWaveform(string selectorString, ref ComplexWaveform< ComplexSingle > equalizerReferenceWaveform, out double papr)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| equalizerReferenceWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the equalizer reference waveform used to perform the measurement. |
| papr | out double | Upon return, containss the peak-to-average power ratio of the waveform obtained after applying digital predistortion. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getgain__string-out.html language=enus -->
## TOPIC 00313: GetGain(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getgain__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getgain__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the gain of the device under test. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetGain(string selectorString, out double value)RemarksThis method gets the value of IdpdResultsGain attribute.ParametersNameTypeDescriptionselectorStringstringSpecifie

### GetGain(string, out double)

Gets the gain of the device under test. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetGain(string selectorString, out double value)

#### Remarks

This method gets the value of [IdpdResultsGain](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the gain of the device under test. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getmeanrmsevm__string-out.html language=enus -->
## TOPIC 00314: GetMeanRmsEvm(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getmeanrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults-getmeanrmsevm__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ratio of L2 norm of difference between the normalized reference and acquired waveforms, to the L2 norm of the normalized reference waveform. This value is expressed either as a percentage or in dB depending on the configured SetEvmUnit(string, RFmxSpecAnMXIdpdEvmUnit),. SyntaxNamespace: Nat

### GetMeanRmsEvm(string, out double)

Gets the ratio of L2 norm of difference between the normalized reference and acquired waveforms, to the L2 norm of the normalized reference waveform. This value is expressed either as a percentage or in dB depending on the configured [SetEvmUnit(string, RFmxSpecAnMXIdpdEvmUnit)](nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdconfiguration-setevmunit__string-rfmxspecanmxidpdevmunit.html),.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanRmsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [IdpdResultsMeanRmsEvm](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the ratio of L2 norm of difference between the normalized reference and acquired waveforms, to the L2 norm of the normalized reference waveform. This value is expressed either as a percentage or in dB depending on the configured SetEvmUnit(string, RFmxSpecAnMXIdpdEvmUnit), |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIdpdResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults.html language=enus -->
## TOPIC 00315: RFmxSpecAnMXIdpdResults Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdresults.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the IDPD measurement results. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXIdpdResults : RFmxSpecAnMXSubObjectMethodsNameDescriptionFetchEqualizerCoefficients(string, double, ref ComplexWaveform< Comple

### RFmxSpecAnMXIdpdResults Class

Provides methods to fetch and read the IDPD measurement results.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXIdpdResults : RFmxSpecAnMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchEqualizerCoefficients(string, double, ref ComplexWaveform< ComplexSingle >) | Fetches the trained equalizer coefficients. |
| FetchPredistortedWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out double, out double, out double) | Fetches the predistorted waveform output after the IDPD measurement. |
| FetchProcessedMeanAcquiredWaveform(string, double, ref ComplexWaveform< ComplexSingle >) | Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement. |
| FetchProcessedReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >) | Fetches the reference waveform used to perform the IDPD measurement. |
| GetEqualizerReferenceWaveform(string, ref ComplexWaveform< ComplexSingle >, out double) | Gets the equalizer reference waveform used to perform the IDPD measurement. |
| GetGain(string, out double) | Gets the gain of the device under test. This value is expressed in dB. |
| GetMeanRmsEvm(string, out double) | Gets the ratio of L2 norm of difference between the normalized reference and acquired waveforms, to the L2 norm of the normalized reference waveform. This value is expressed either as a percentage or in dB depending on the configured SetEvmUnit(string, RFmxSpecAnMXIdpdEvmUnit),. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdsignaltype.html language=enus -->
## TOPIC 00316: RFmxSpecAnMXIdpdSignalType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdsignaltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxidpdsignaltype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of reference waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIdpdSignalTypeMembersNameValueDescriptionModulated0Specifies the reference waveform is a banded signal like cellular or connectivity standard signals. Tones1Specifies the reference wav

### RFmxSpecAnMXIdpdSignalType Enumeration

Specifies the type of reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIdpdSignalType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Modulated | 0 | Specifies the reference waveform is a banded signal like cellular or connectivity standard signals. |
| Tones | 1 | Specifies the reference waveform is a continuous signal comprising of one or more tones. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxim-configuration.html language=enus -->
## TOPIC 00317: Configuration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxim-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxim-configuration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXIMConfiguration instance that provides methods to configure the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXIMConfiguration Configuration { get; }

### Configuration

Gets the [RFmxSpecAnMXIMConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration.html) instance that provides methods to configure the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXIMConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration.html) Configuration { get; }

Parent topic:

RFmxSpecAnMXIM Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxim-results.html language=enus -->
## TOPIC 00318: Results

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxim-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxim-results.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXIMResults instance that provides methods to fetch and read the IM measurement results. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXIMResults Results { get; }

### Results

Gets the [RFmxSpecAnMXIMResults](nationalinstruments-rfmx-specanmx-rfmxspecanmximresults.html) instance that provides methods to fetch and read the IM measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXIMResults](nationalinstruments-rfmx-specanmx-rfmxspecanmximresults.html) Results { get; }

Parent topic:

RFmxSpecAnMXIM Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxim.html language=enus -->
## TOPIC 00319: RFmxSpecAnMXIM Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxim.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxim.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the IM measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXIM : RFmxSpecAnMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxSpecAnMXIMConfiguration instance that provides methods to configure the IM measureme

### RFmxSpecAnMXIM Class

Represents the IM measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXIM : RFmxSpecAnMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxSpecAnMXIMConfiguration instance that provides methods to configure the IM measurement. |
| Results | Gets the RFmxSpecAnMXIMResults instance that provides methods to fetch and read the IM measurement results. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximamplitudecorrectiontype.html language=enus -->
## TOPIC 00320: RFmxSpecAnMXIMAmplitudeCorrectionType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximamplitudecorrectiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace:

### RFmxSpecAnMXIMAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIMAmplitudeCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An Individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html language=enus -->
## TOPIC 00321: RFmxSpecAnMXIMAutoIntermodsSetupEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the intermod frequencies or uses user-specified frequencies. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIMAutoIntermodsSetupEnabledMembersNameValueDescriptionFalse0The measurement uses the values that you specify for the SetLo

### RFmxSpecAnMXIMAutoIntermodsSetupEnabled Enumeration

Specifies whether the measurement computes the intermod frequencies or uses user-specified frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIMAutoIntermodsSetupEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the values that you specify for the SetLowerIntermodFrequency(string, double) and SetUpperIntermodFrequency(string, double) properties. |
| True | 1 | The measurement computes the intermod frequencies. The maximum number of intermods that you can measure is based on the value of the SetMaximumIntermodOrder(string, int) method. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html language=enus -->
## TOPIC 00322: RFmxSpecAnMXIMAveragingEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIMAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The IM measurement uses the SetAveragingCount(string,

### RFmxSpecAnMXIMAveragingEnabled Enumeration

Specifies whether to enable averaging for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIMAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The IM measurement uses the SetAveragingCount(string, int) method as the number of acquisitions over which the IM measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingtype.html language=enus -->
## TOPIC 00323: RFmxSpecAnMXIMAveragingType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIMAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averaged. RMS averag

### RFmxSpecAnMXIMAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIMAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureautointermodssetup__string-rfmxspecanmximautointermodssetupenabled-int.html language=enus -->
## TOPIC 00324: ConfigureAutoIntermodsSetup(string, RFmxSpecAnMXIMAutoIntermodsSetupEnabled, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureautointermodssetup__string-rfmxspecanmximautointermodssetupenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureautointermodssetup__string-rfmxspecanmximautointermodssetupenabled-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the measurement computes the intermod frequencies or uses manually specified frequencies. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureAutoIntermodsSetup(string selectorString, RFmxSpecAnMXIMAutoIntermodsSetupEnabled autoIntermodsSetupEnabled, int maximumI

### ConfigureAutoIntermodsSetup(string, RFmxSpecAnMXIMAutoIntermodsSetupEnabled, int)

Configures whether the measurement computes the intermod frequencies or uses manually specified frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureAutoIntermodsSetup(string selectorString, RFmxSpecAnMXIMAutoIntermodsSetupEnabled autoIntermodsSetupEnabled, int maximumIntermodOrder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| autoIntermodsSetupEnabled | RFmxSpecAnMXIMAutoIntermodsSetupEnabled | Specifies whether the measurement computes the intermod frequencies or uses manually specified frequencies. |
| maximumIntermodOrder | int | Specifies the order up to which the RFmx driver measures odd order intermodulation products when you set the autoIntermodsSetupEnabled parameter to True. The lower and upper intermodulation products are measured for each order. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureaveraging__string-rfmxspecanmximaveragingenabled-int-rfmxspecanmximaveragingtype.html language=enus -->
## TOPIC 00325: ConfigureAveraging(string, RFmxSpecAnMXIMAveragingEnabled, int, RFmxSpecAnMXIMAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureaveraging__string-rfmxspecanmximaveragingenabled-int-rfmxspecanmximaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureaveraging__string-rfmxspecanmximaveragingenabled-int-rfmxspecanmximaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the IM measurement.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureAveraging(string selectorString, RFmxSpecAnMXIMAveragingEnabled averagingEnabled, int averagingCount, RFmxSpecAnMXIMAveragingType averagingType)ParametersNameTypeDescriptionselectorStrin

### ConfigureAveraging(string, RFmxSpecAnMXIMAveragingEnabled, int, RFmxSpecAnMXIMAveragingType)

Configures averaging for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureAveraging(string selectorString, RFmxSpecAnMXIMAveragingEnabled averagingEnabled, int averagingCount, RFmxSpecAnMXIMAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxSpecAnMXIMAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxSpecAnMXIMAveragingType | Specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefft__string-rfmxspecanmximfftwindow-double.html language=enus -->
## TOPIC 00326: ConfigureFft(string, RFmxSpecAnMXIMFftWindow, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefft__string-rfmxspecanmximfftwindow-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefft__string-rfmxspecanmximfftwindow-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the window and FFT to obtain a spectrum for the IM measurement.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFft(string selectorString, RFmxSpecAnMXIMFftWindow fftWindow, double fftPadding)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The s

### ConfigureFft(string, RFmxSpecAnMXIMFftWindow, double)

Configures the window and FFT to obtain a spectrum for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFft(string selectorString, RFmxSpecAnMXIMFftWindow fftWindow, double fftPadding)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| fftWindow | RFmxSpecAnMXIMFftWindow | Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectral Measurements> topic for more information about FFT window types. |
| fftPadding | double | Specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefrequencydefinition__string-rfmxspecanmximfrequencydefinition.html language=enus -->
## TOPIC 00327: ConfigureFrequencyDefinition(string, RFmxSpecAnMXIMFrequencyDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefrequencydefinition__string-rfmxspecanmximfrequencydefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefrequencydefinition__string-rfmxspecanmximfrequencydefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether you can specify the tones and intermod frequencies as either relative to the RF center frequency or as absolute frequencies.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFrequencyDefinition(string selectorString, RFmxSpecAnMXIMFrequencyDefinition frequencyD

### ConfigureFrequencyDefinition(string, RFmxSpecAnMXIMFrequencyDefinition)

Configures whether you can specify the tones and intermod frequencies as either relative to the RF center frequency or as absolute frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFrequencyDefinition(string selectorString, RFmxSpecAnMXIMFrequencyDefinition frequencyDefinition)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| frequencyDefinition | RFmxSpecAnMXIMFrequencyDefinition | Specifies whether you can specify the tones and intermod frequencies as either relative to the RF center frequency or as absolute frequencies. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefundamentaltones__string-double-double.html language=enus -->
## TOPIC 00328: ConfigureFundamentalTones(string, double, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefundamentaltones__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurefundamentaltones__string-double-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the upper and lower frequencies in a two-tone input signal.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFundamentalTones(string selectorString, double lowerToneFrequency, double upperToneFrequency)ParametersNameTypeDescriptionselectorStringstringPass an empty stri

### ConfigureFundamentalTones(string, double, double)

Configures the upper and lower frequencies in a two-tone input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFundamentalTones(string selectorString, double lowerToneFrequency, double upperToneFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| lowerToneFrequency | double | Specifies the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |
| upperToneFrequency | double | Specifies the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureintermod__string-int-double-double-rfmxspecanmximintermodside-rfmxspecanmximintermodenabled.html language=enus -->
## TOPIC 00329: ConfigureIntermod(string, int, double, double, RFmxSpecAnMXIMIntermodSide, RFmxSpecAnMXIMIntermodEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureintermod__string-int-double-double-rfmxspecanmximintermodside-rfmxspecanmximintermodenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configureintermod__string-int-double-double-rfmxspecanmximintermodside-rfmxspecanmximintermodenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method t

### ConfigureIntermod(string, int, double, double, RFmxSpecAnMXIMIntermodSide, RFmxSpecAnMXIMIntermodEnabled)

Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html). 
 Use "intermod(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureIntermod(string selectorString, int intermodOrder, double lowerIntermodFrequency, double upperIntermodFrequency, RFmxSpecAnMXIMIntermodSide intermodSide, RFmxSpecAnMXIMIntermodEnabled intermodEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of intermod number. Example:"intermod0" You can use the BuildIntermodString(string, int) method to build the selector string. |
| intermodOrder | int | Specifies the order of the intermod. |
| lowerIntermodFrequency | double | Specifies the frequency of the lower intermodulation product. This value is expressed in Hz. |
| upperIntermodFrequency | double | Specifies the frequency of the upper intermodulation product. This value is expressed in Hz. |
| intermodSide | RFmxSpecAnMXIMIntermodSide | Specifies whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. |
| intermodEnabled | RFmxSpecAnMXIMIntermodEnabled | Specifies whether to enable an intermod for the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configuremeasurementmethod__string-rfmxspecanmximmeasurementmethod.html language=enus -->
## TOPIC 00330: ConfigureMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configuremeasurementmethod__string-rfmxspecanmximmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configuremeasurementmethod__string-rfmxspecanmximmeasurementmethod.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureMeasurementMethod(string selectorString, RFmxSpecAnMXIMMeasurementMethod measurementMethod)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal

### ConfigureMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)

Configures the method for performing the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureMeasurementMethod(string selectorString, RFmxSpecAnMXIMMeasurementMethod measurementMethod)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementMethod | RFmxSpecAnMXIMMeasurementMethod | Specifies the method for performing the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurenumberofintermods__string-int.html language=enus -->
## TOPIC 00331: ConfigureNumberOfIntermods(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurenumberofintermods__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurenumberofintermods__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of intermods to measure when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to False.SyntaxNamespace: NationalInstruments.RFmx.SpecA

### ConfigureNumberOfIntermods(string, int)

Configures the number of intermods to measure when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureNumberOfIntermods(string selectorString, int numberOfIntermods)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfIntermods | int | Specifies the number of intermods to measure when you set the IM Auto Intermods Setup Enabled method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurerbwfilter__string-rfmxspecanmximrbwfilterautobandwidth-double-rfmxspecanmximrbwfiltertype.html language=enus -->
## TOPIC 00332: ConfigureRbwFilter(string, RFmxSpecAnMXIMRbwFilterAutoBandwidth, double, RFmxSpecAnMXIMRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurerbwfilter__string-rfmxspecanmximrbwfilterautobandwidth-double-rfmxspecanmximrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configurerbwfilter__string-rfmxspecanmximrbwfilterautobandwidth-double-rfmxspecanmximrbwfiltertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureRbwFilter(string selectorString, RFmxSpecAnMXIMRbwFilterAutoBandwidth rbwAuto, double rbw, RFmxSpecAnMXIMRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an empty string.

### ConfigureRbwFilter(string, RFmxSpecAnMXIMRbwFilterAutoBandwidth, double, RFmxSpecAnMXIMRbwFilterType)

Configures the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureRbwFilter(string selectorString, RFmxSpecAnMXIMRbwFilterAutoBandwidth rbwAuto, double rbw, RFmxSpecAnMXIMRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxSpecAnMXIMRbwFilterAutoBandwidth | Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Measurements topic for more details on RBW and sweep time. |
| rbw | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxSpecAnMXIMRbwFilterType | Specifies the response of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configuresweeptime__string-rfmxspecanmximsweeptimeauto-double.html language=enus -->
## TOPIC 00333: ConfigureSweepTime(string, RFmxSpecAnMXIMSweepTimeAuto, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configuresweeptime__string-rfmxspecanmximsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-configuresweeptime__string-rfmxspecanmximsweeptimeauto-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSweepTime(string selectorString, RFmxSpecAnMXIMSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed w

### ConfigureSweepTime(string, RFmxSpecAnMXIMSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSweepTime(string selectorString, RFmxSpecAnMXIMSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxSpecAnMXIMSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time, in seconds, when you set the sweepTimeAuto parameter to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00334: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of IMAllTracesEnabled attribute.The default value

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [IMAllTracesEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00335: GetAmplitudeCorrectionType(string, out RFmxSpecAnMXIMAmplitudeCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Natio

### GetAmplitudeCorrectionType(string, out RFmxSpecAnMXIMAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxSpecAnMXIMAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [IMAmplitudeCorrectionType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmximamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getautointermodssetupenabled__string-out.html language=enus -->
## TOPIC 00336: GetAutoIntermodsSetupEnabled(string, out RFmxSpecAnMXIMAutoIntermodsSetupEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getautointermodssetupenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getautointermodssetupenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the intermod frequencies or uses user-specified frequencies. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAutoIntermodsSetupEnabled(string selectorString, out RFmxSpecAnMXIMAutoIntermodsSetupEnabled value)RemarksThis method gets the value of I

### GetAutoIntermodsSetupEnabled(string, out RFmxSpecAnMXIMAutoIntermodsSetupEnabled)

Gets whether the measurement computes the intermod frequencies or uses user-specified frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAutoIntermodsSetupEnabled(string selectorString, out RFmxSpecAnMXIMAutoIntermodsSetupEnabled value)

#### Remarks

This method gets the value of [IMAutoIntermodsSetupEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMAutoIntermodsSetupEnabled | Upon return, contains whether the measurement computes the intermod frequencies or uses user-specified frequencies. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00337: GetAveragingCount(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of IMA

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingenabled__string-rfmxspecanmximaveragingenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [IMAveragingCount](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00338: GetAveragingEnabled(string, out RFmxSpecAnMXIMAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXIMAveragingEnabled value)RemarksThis method gets the value of IMAveragingEnabled attribute.The default value is False.Param

### GetAveragingEnabled(string, out RFmxSpecAnMXIMAveragingEnabled)

Gets whether to enable averaging for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXIMAveragingEnabled value)

#### Remarks

This method gets the value of [IMAveragingEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMAveragingEnabled | Upon return, contains whether to enable averaging for the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00339: GetAveragingType(string, out RFmxSpecAnMXIMAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingType(string selectorString, out RFmxSpecAnMXIMAveragingType value)RemarksThis method gets the value of

### GetAveragingType(string, out RFmxSpecAnMXIMAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingType(string selectorString, out RFmxSpecAnMXIMAveragingType value)

#### Remarks

This method gets the value of [IMAveragingType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfarifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00340: GetFarIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfarifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfarifoutputpoweroffset__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMetho

### GetFarIFOutputPowerOffset(string, out double)

Gets the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setmeasurementmethod__string-rfmxspecanmximmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-specanmx-rfmxspecanmximmeasurementmethod.html) and the [SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setifoutputpoweroffsetauto__string-rfmxspecanmximifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFarIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [IMFarIFOutputPowerOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 20 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfftpadding__string-out.html language=enus -->
## TOPIC 00341: GetFftPadding(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfftpadding__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfftpadding__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. SyntaxNamespace: NationalInstruments.

### GetFftPadding(string, out double)

Gets the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: *FFT size* = *waveform size* * *padding* This method is used only when the acquisition span is less than the device instantaneous bandwidth.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFftPadding(string selectorString, out double value)

#### Remarks

This method gets the value of [IMFftPadding](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is -1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfftwindow__string-out.html language=enus -->
## TOPIC 00342: GetFftWindow(string, out RFmxSpecAnMXIMFftWindow)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfftwindow__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfftwindow__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT window type to use to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFftWindow(string selectorString, out RFmxSpecAnMXIMFftWindow value)RemarksThis method gets the value of IMFftWindow attribute.The default value is FlatTop.ParametersNameTypeDes

### GetFftWindow(string, out RFmxSpecAnMXIMFftWindow)

Gets the FFT window type to use to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFftWindow(string selectorString, out RFmxSpecAnMXIMFftWindow value)

#### Remarks

This method gets the value of [IMFftWindow](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [FlatTop](nationalinstruments-rfmx-specanmx-rfmxspecanmximfftwindow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMFftWindow | Upon return, contains the FFT window type to use to reduce spectral leakage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfrequencydefinition__string-out.html language=enus -->
## TOPIC 00343: GetFrequencyDefinition(string, out RFmxSpecAnMXIMFrequencyDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfrequencydefinition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfrequencydefinition__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFrequencyDefinition(string selectorString, out RFmxSpecAnMXIMFrequencyDefinition value)RemarksThis method gets the val

### GetFrequencyDefinition(string, out RFmxSpecAnMXIMFrequencyDefinition)

Gets whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFrequencyDefinition(string selectorString, out RFmxSpecAnMXIMFrequencyDefinition value)

#### Remarks

This method gets the value of [IMFrequencyDefinition](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-specanmx-rfmxspecanmximfrequencydefinition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMFrequencyDefinition | Upon return, contains whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfundamentallowertonefrequency__string-out.html language=enus -->
## TOPIC 00344: GetFundamentalLowerToneFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfundamentallowertonefrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfundamentallowertonefrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFundamentalLowerToneFrequency(string selectorString, out double value)RemarksThis method gets the value of

### GetFundamentalLowerToneFrequency(string, out double)

Gets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFundamentalLowerToneFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [IMFundamentalLowerToneFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is -1 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfundamentaluppertonefrequency__string-out.html language=enus -->
## TOPIC 00345: GetFundamentalUpperToneFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfundamentaluppertonefrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getfundamentaluppertonefrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFundamentalUpperToneFrequency(string selectorString, out double value)RemarksThis method gets the value o

### GetFundamentalUpperToneFrequency(string, out double)

Gets the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFundamentalUpperToneFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [IMFundamentalUpperToneFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getifoutputpoweroffsetauto__string-out.html language=enus -->
## TOPIC 00346: GetIFOutputPowerOffsetAuto(string, out RFmxSpecAnMXIMIFOutputPowerOffsetAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getifoutputpoweroffsetauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getifoutputpoweroffsetauto__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. SyntaxNamespace: NationalInstrum

### GetIFOutputPowerOffsetAuto(string, out RFmxSpecAnMXIMIFOutputPowerOffsetAuto)

Gets whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the [SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setmeasurementmethod__string-rfmxspecanmximmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-specanmx-rfmxspecanmximmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIFOutputPowerOffsetAuto(string selectorString, out RFmxSpecAnMXIMIFOutputPowerOffsetAuto value)

#### Remarks

This method gets the value of [IMIFOutputPowerOffsetAuto](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximifoutputpoweroffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMIFOutputPowerOffsetAuto | Upon return, contains whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodenabled__string-out.html language=enus -->
## TOPIC 00347: GetIntermodEnabled(string, out RFmxSpecAnMXIMIntermodEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable an intermod for the IM measurement. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. SyntaxName

### GetIntermodEnabled(string, out RFmxSpecAnMXIMIntermodEnabled)

Gets whether to enable an intermod for the IM measurement. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximintermodenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIntermodEnabled(string selectorString, out RFmxSpecAnMXIMIntermodEnabled value)

#### Remarks

This method gets the value of [IMIntermodEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximintermodenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXIMIntermodEnabled | Upon return, contains whether to enable an intermod for the IM measurement. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodorder__string-out.html language=enus -->
## TOPIC 00348: GetIntermodOrder(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodorder__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodorder__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the order of the intermod. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. SyntaxNamespace: NationalInstruments.

### GetIntermodOrder(string, out int)

Gets the order of the intermod. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIntermodOrder(string selectorString, out int value)

#### Remarks

This method gets the value of [IMIntermodOrder](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 3.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the order of the intermod. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodside__string-out.html language=enus -->
## TOPIC 00349: GetIntermodSide(string, out RFmxSpecAnMXIMIntermodSide)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodside__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getintermodside__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecA

### GetIntermodSide(string, out RFmxSpecAnMXIMIntermodSide)

Gets whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIntermodSide(string selectorString, out RFmxSpecAnMXIMIntermodSide value)

#### Remarks

This method gets the value of [IMIntermodSide](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Both](nationalinstruments-rfmx-specanmx-rfmxspecanmximintermodside.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXIMIntermodSide | Upon return, contains whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getlocalpeaksearchenabled__string-out.html language=enus -->
## TOPIC 00350: GetLocalPeakSearchEnabled(string, out RFmxSpecAnMXIMLocalPeakSearchEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getlocalpeaksearchenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getlocalpeaksearchenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLocalPeakSearchEnabled(string selectorString, out RFmxSpecAnMXIMLocalPeakSearchEnabled value)RemarksThis method g

### GetLocalPeakSearchEnabled(string, out RFmxSpecAnMXIMLocalPeakSearchEnabled)

Gets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLocalPeakSearchEnabled(string selectorString, out RFmxSpecAnMXIMLocalPeakSearchEnabled value)

#### Remarks

This method gets the value of [IMLocalPeakSearchEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximlocalpeaksearchenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMLocalPeakSearchEnabled | Upon return, contains whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getlowerintermodfrequency__string-out.html language=enus -->
## TOPIC 00351: GetLowerIntermodFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getlowerintermodfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getlowerintermodfrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled

### GetLowerIntermodFrequency(string, out double)

Gets the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerIntermodFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [IMLowerIntermodFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is -3 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency of the lower intermodulation product. This value is expressed in Hz. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmaximumintermodorder__string-out.html language=enus -->
## TOPIC 00352: GetMaximumIntermodOrder(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmaximumintermodorder__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmaximumintermodorder__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMaximumInterm

### GetMaximumIntermodOrder(string, out int)

Gets the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMaximumIntermodOrder(string selectorString, out int value)

#### Remarks

This method gets the value of [IMMaximumIntermodOrder](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 3.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled method to True. The lower and upper intermodulation products are measured for each order. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00353: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of IMMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStri

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [IMMeasurementEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmeasurementmethod__string-out.html language=enus -->
## TOPIC 00354: GetMeasurementMethod(string, out RFmxSpecAnMXIMMeasurementMethod)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmeasurementmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getmeasurementmethod__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method used to perform the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementMethod(string selectorString, out RFmxSpecAnMXIMMeasurementMethod value)RemarksThis method gets the value of IMMeasurementMethod attribute.The default value is Normal.Parame

### GetMeasurementMethod(string, out RFmxSpecAnMXIMMeasurementMethod)

Gets the method used to perform the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementMethod(string selectorString, out RFmxSpecAnMXIMMeasurementMethod value)

#### Remarks

This method gets the value of [IMMeasurementMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Normal](nationalinstruments-rfmx-specanmx-rfmxspecanmximmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMMeasurementMethod | Upon return, contains the method used to perform the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnearifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00355: GetNearIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnearifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnearifoutputpoweroffset__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to

### GetNearIFOutputPowerOffset(string, out double)

Gets the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setmeasurementmethod__string-rfmxspecanmximmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-specanmx-rfmxspecanmximmeasurementmethod.html) and the [SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setifoutputpoweroffsetauto__string-rfmxspecanmximifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNearIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [IMNearIFOutputPowerOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset by which to adjust the IF output power level for the intermods near the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00356: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the IM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the IM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [IMNumberOfAnalysisThreads](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the IM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnumberofintermods__string-out.html language=enus -->
## TOPIC 00357: GetNumberOfIntermods(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnumberofintermods__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getnumberofintermods__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of intermods to measure when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to False. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpu

### GetNumberOfIntermods(string, out int)

Gets the number of intermods to measure when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfIntermods(string selectorString, out int value)

#### Remarks

This method gets the value of [IMNumberOfIntermods](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of intermods to measure when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00358: GetRbwFilterAutoBandwidth(string, out RFmxSpecAnMXIMRbwFilterAutoBandwidth)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfilterautobandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterAutoBandwidth(string selectorString, out RFmxSpecAnMXIMRbwFilterAutoBandwidth value)RemarksThis method gets the value of IMRbwFilterAutoBandwidth attribute.The default value is Tru

### GetRbwFilterAutoBandwidth(string, out RFmxSpecAnMXIMRbwFilterAutoBandwidth)

Gets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterAutoBandwidth(string selectorString, out RFmxSpecAnMXIMRbwFilterAutoBandwidth value)

#### Remarks

This method gets the value of [IMRbwFilterAutoBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximrbwfilterautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMRbwFilterAutoBandwidth | Upon return, contains whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00359: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXIMRbwFilterAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterBandwidth(string s

### GetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXIMRbwFilterAutoBandwidth)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmximrbwfilterautobandwidth.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximrbwfilterautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [IMRbwFilterBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXIMRbwFilterAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00360: GetRbwFilterType(string, out RFmxSpecAnMXIMRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the response of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterType(string selectorString, out RFmxSpecAnMXIMRbwFilterType value)RemarksThis method gets the value of IMRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDescr

### GetRbwFilterType(string, out RFmxSpecAnMXIMRbwFilterType)

Gets the response of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterType(string selectorString, out RFmxSpecAnMXIMRbwFilterType value)

#### Remarks

This method gets the value of [IMRbwFilterType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-specanmx-rfmxspecanmximrbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMRbwFilterType | Upon return, contains the response of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00361: GetSweepTimeAuto(string, out RFmxSpecAnMXIMSweepTimeAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSweepTimeAuto(string selectorString, out RFmxSpecAnMXIMSweepTimeAuto value)RemarksThis method gets the value of IMSweepTimeAuto attribute.The default value is True.ParametersNameType

### GetSweepTimeAuto(string, out RFmxSpecAnMXIMSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxSpecAnMXIMSweepTimeAuto value)

#### Remarks

This method gets the value of [IMSweepTimeAuto](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXIMSweepTimeAuto | Upon return, contains whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00362: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxSpecAnMXIMSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method gets the value

### GetSweepTimeInterval(string, out double)

Gets the sweep time when you set the [SetSweepTimeAuto(string, RFmxSpecAnMXIMSweepTimeAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setsweeptimeauto__string-rfmxspecanmximsweeptimeauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [IMSweepTimeInterval](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time when you set the SetSweepTimeAuto(string, RFmxSpecAnMXIMSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getupperintermodfrequency__string-out.html language=enus -->
## TOPIC 00363: GetUpperIntermodFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getupperintermodfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-getupperintermodfrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of the upper intermodulation product. This value is expressed in Hz. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled

### GetUpperIntermodFrequency(string, out double)

Gets the frequency of the upper intermodulation product. This value is expressed in Hz. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximautointermodssetupenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperIntermodFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [IMUpperIntermodFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 3 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency of the upper intermodulation product. This value is expressed in Hz. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00364: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of IMAllTracesEnabled attribute.The default value is

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [IMAllTracesEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setamplitudecorrectiontype__string-rfmxspecanmximamplitudecorrectiontype.html language=enus -->
## TOPIC 00365: SetAmplitudeCorrectionType(string, RFmxSpecAnMXIMAmplitudeCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setamplitudecorrectiontype__string-rfmxspecanmximamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setamplitudecorrectiontype__string-rfmxspecanmximamplitudecorrectiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Natio

### SetAmplitudeCorrectionType(string, RFmxSpecAnMXIMAmplitudeCorrectionType)

Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxSpecAnMXIMAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [IMAmplitudeCorrectionType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmximamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setautointermodssetupenabled__string-rfmxspecanmximautointermodssetupenabled.html language=enus -->
## TOPIC 00366: SetAutoIntermodsSetupEnabled(string, RFmxSpecAnMXIMAutoIntermodsSetupEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setautointermodssetupenabled__string-rfmxspecanmximautointermodssetupenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setautointermodssetupenabled__string-rfmxspecanmximautointermodssetupenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the intermod frequencies or uses user-specified frequencies. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAutoIntermodsSetupEnabled(string selectorString, RFmxSpecAnMXIMAutoIntermodsSetupEnabled value)ParametersNameTypeDescriptionselectorStrin

### SetAutoIntermodsSetupEnabled(string, RFmxSpecAnMXIMAutoIntermodsSetupEnabled)

Sets whether the measurement computes the intermod frequencies or uses user-specified frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAutoIntermodsSetupEnabled(string selectorString, RFmxSpecAnMXIMAutoIntermodsSetupEnabled value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMAutoIntermodsSetupEnabled | Specifies whether the measurement computes the intermod frequencies or uses user-specified frequencies. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00367: SetAveragingCount(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of IMAvera

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingenabled__string-rfmxspecanmximaveragingenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [IMAveragingCount](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingenabled__string-rfmxspecanmximaveragingenabled.html language=enus -->
## TOPIC 00368: SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingenabled__string-rfmxspecanmximaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingenabled__string-rfmxspecanmximaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingEnabled(string selectorString, RFmxSpecAnMXIMAveragingEnabled value)RemarksThis method sets the value of IMAveragingEnabled attribute.The default value is False.Parameter

### SetAveragingEnabled(string, RFmxSpecAnMXIMAveragingEnabled)

Sets whether to enable averaging for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingEnabled(string selectorString, RFmxSpecAnMXIMAveragingEnabled value)

#### Remarks

This method sets the value of [IMAveragingEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMAveragingEnabled | Specifies whether to enable averaging for the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingtype__string-rfmxspecanmximaveragingtype.html language=enus -->
## TOPIC 00369: SetAveragingType(string, RFmxSpecAnMXIMAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingtype__string-rfmxspecanmximaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setaveragingtype__string-rfmxspecanmximaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingType(string selectorString, RFmxSpecAnMXIMAveragingType value)RemarksThis method sets the value of IMAv

### SetAveragingType(string, RFmxSpecAnMXIMAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingType(string selectorString, RFmxSpecAnMXIMAveragingType value)

#### Remarks

This method sets the value of [IMAveragingType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-specanmx-rfmxspecanmximaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the IM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfarifoutputpoweroffset__string-double.html language=enus -->
## TOPIC 00370: SetFarIFOutputPowerOffset(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfarifoutputpoweroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfarifoutputpoweroffset__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMetho

### SetFarIFOutputPowerOffset(string, double)

Sets the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setmeasurementmethod__string-rfmxspecanmximmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-specanmx-rfmxspecanmximmeasurementmethod.html) and the [SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setifoutputpoweroffsetauto__string-rfmxspecanmximifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmximifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFarIFOutputPowerOffset(string selectorString, double value)

#### Remarks

This method sets the value of [IMFarIFOutputPowerOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 20 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the offset by which to adjust the IF output power level for the intermods that are far from the carrier channel to improve the dynamic range of the signal analyzer. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange and the SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfftpadding__string-double.html language=enus -->
## TOPIC 00371: SetFftPadding(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfftpadding__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfftpadding__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. SyntaxNamespace: NationalInstruments.

### SetFftPadding(string, double)

Sets the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: *FFT size* = *waveform size* * *padding* This method is used only when the acquisition span is less than the device instantaneous bandwidth.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFftPadding(string selectorString, double value)

#### Remarks

This method sets the value of [IMFftPadding](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is -1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding This method is used only when the acquisition span is less than the device instantaneous bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfftwindow__string-rfmxspecanmximfftwindow.html language=enus -->
## TOPIC 00372: SetFftWindow(string, RFmxSpecAnMXIMFftWindow)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfftwindow__string-rfmxspecanmximfftwindow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfftwindow__string-rfmxspecanmximfftwindow.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the FFT window type to use to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetFftWindow(string selectorString, RFmxSpecAnMXIMFftWindow value)RemarksThis method sets the value of IMFftWindow attribute.The default value is FlatTop.ParametersNameTypeDescrip

### SetFftWindow(string, RFmxSpecAnMXIMFftWindow)

Sets the FFT window type to use to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFftWindow(string selectorString, RFmxSpecAnMXIMFftWindow value)

#### Remarks

This method sets the value of [IMFftWindow](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [FlatTop](nationalinstruments-rfmx-specanmx-rfmxspecanmximfftwindow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMFftWindow | Specifies the FFT window type to use to reduce spectral leakage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfrequencydefinition__string-rfmxspecanmximfrequencydefinition.html language=enus -->
## TOPIC 00373: SetFrequencyDefinition(string, RFmxSpecAnMXIMFrequencyDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfrequencydefinition__string-rfmxspecanmximfrequencydefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfrequencydefinition__string-rfmxspecanmximfrequencydefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetFrequencyDefinition(string selectorString, RFmxSpecAnMXIMFrequencyDefinition value)RemarksThis method sets the value o

### SetFrequencyDefinition(string, RFmxSpecAnMXIMFrequencyDefinition)

Sets whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFrequencyDefinition(string selectorString, RFmxSpecAnMXIMFrequencyDefinition value)

#### Remarks

This method sets the value of [IMFrequencyDefinition](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-specanmx-rfmxspecanmximfrequencydefinition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMFrequencyDefinition | Specifies whether the tones and intermod frequencies are relative to the RF center frequency, or are absolute frequencies. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfundamentallowertonefrequency__string-double.html language=enus -->
## TOPIC 00374: SetFundamentalLowerToneFrequency(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfundamentallowertonefrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfundamentallowertonefrequency__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetFundamentalLowerToneFrequency(string selectorString, double value)RemarksThis method sets the value of IMF

### SetFundamentalLowerToneFrequency(string, double)

Sets the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFundamentalLowerToneFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [IMFundamentalLowerToneFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is -1 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfundamentaluppertonefrequency__string-double.html language=enus -->
## TOPIC 00375: SetFundamentalUpperToneFrequency(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfundamentaluppertonefrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setfundamentaluppertonefrequency__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetFundamentalUpperToneFrequency(string selectorString, double value)RemarksThis method sets the value of IM

### SetFundamentalUpperToneFrequency(string, double)

Sets the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFundamentalUpperToneFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [IMFundamentalUpperToneFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setifoutputpoweroffsetauto__string-rfmxspecanmximifoutputpoweroffsetauto.html language=enus -->
## TOPIC 00376: SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setifoutputpoweroffsetauto__string-rfmxspecanmximifoutputpoweroffsetauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setifoutputpoweroffsetauto__string-rfmxspecanmximifoutputpoweroffsetauto.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. SyntaxNamespace: NationalInstrum

### SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXIMIFOutputPowerOffsetAuto)

Sets whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the [SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setmeasurementmethod__string-rfmxspecanmximmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-specanmx-rfmxspecanmximmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetIFOutputPowerOffsetAuto(string selectorString, RFmxSpecAnMXIMIFOutputPowerOffsetAuto value)

#### Remarks

This method sets the value of [IMIFOutputPowerOffsetAuto](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximifoutputpoweroffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMIFOutputPowerOffsetAuto | Specifies whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This method is used only if you set the SetMeasurementMethod(string, RFmxSpecAnMXIMMeasurementMethod) method to DynamicRange. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setintermodenabled__string-rfmxspecanmximintermodenabled.html language=enus -->
## TOPIC 00377: SetIntermodEnabled(string, RFmxSpecAnMXIMIntermodEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setintermodenabled__string-rfmxspecanmximintermodenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setintermodenabled__string-rfmxspecanmximintermodenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable an intermod for the IM measurement. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. SyntaxName

### SetIntermodEnabled(string, RFmxSpecAnMXIMIntermodEnabled)

Sets whether to enable an intermod for the IM measurement. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximintermodenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetIntermodEnabled(string selectorString, RFmxSpecAnMXIMIntermodEnabled value)

#### Remarks

This method sets the value of [IMIntermodEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximintermodenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the imintermod number. Example: "imintermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | RFmxSpecAnMXIMIntermodEnabled | Specifies whether to enable an intermod for the IM measurement. This method is not used when you set the NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMConfiguration.GetAutoIntermodsSetupEnabled(string,NationalInstruments.RFmx.SpecAnMX.RFmxSpecAnMXIMAutoIntermodsSetupEnabled@) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setlocalpeaksearchenabled__string-rfmxspecanmximlocalpeaksearchenabled.html language=enus -->
## TOPIC 00378: SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setlocalpeaksearchenabled__string-rfmxspecanmximlocalpeaksearchenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximconfiguration-setlocalpeaksearchenabled__string-rfmxspecanmximlocalpeaksearchenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetLocalPeakSearchEnabled(string selectorString, RFmxSpecAnMXIMLocalPeakSearchEnabled value)RemarksThis method sets

### SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled)

Sets whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetLocalPeakSearchEnabled(string selectorString, RFmxSpecAnMXIMLocalPeakSearchEnabled value)

#### Remarks

This method sets the value of [IMLocalPeakSearchEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmximlocalpeaksearchenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXIMLocalPeakSearchEnabled | Specifies whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getupperoutputinterceptpower__string-out.html language=enus -->
## TOPIC 00379: GetUpperOutputInterceptPower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getupperoutputinterceptpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getupperoutputinterceptpower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUpperOutputInterceptPower(string selectorString, out double value)RemarksThis method gets the value of

### GetUpperOutputInterceptPower(string, out double)

Gets the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperOutputInterceptPower(string selectorString, out double value)

#### Remarks

This method gets the value of [IMResultsUpperOutputInterceptPower](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and ImIntermod number. Example: "ImIntermod0", "result::r1/ImIntermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getworstcaseintermodrelativepower__string-out.html language=enus -->
## TOPIC 00380: GetWorstCaseIntermodRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getworstcaseintermodrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getworstcaseintermodrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the worst case intermod relative power that is equal to the maximum of the values of both the IM Results Upper Intermod Relative Power and IM Results Lower Intermod Relative Power results. This value is expressed in dBc. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetWorstCaseI

### GetWorstCaseIntermodRelativePower(string, out double)

Gets the worst case intermod relative power that is equal to the maximum of the values of both the IM Results Upper Intermod Relative Power and IM Results Lower Intermod Relative Power results. This value is expressed in dBc.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetWorstCaseIntermodRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [IMResultsWorstCaseIntermodRelativePower](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and ImIntermod number. Example: "ImIntermod0", "result::r1/ImIntermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the worst case intermod relative power that is equal to the maximum of the values of both the IM Results Upper Intermod Relative Power and IM Results Lower Intermod Relative Power results. This value is expressed in dBc. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getworstcaseoutputinterceptpower__string-out.html language=enus -->
## TOPIC 00381: GetWorstCaseOutputInterceptPower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getworstcaseoutputinterceptpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximresults-getworstcaseoutputinterceptpower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the worst case output intercept power which is equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetWorstCaseOutputIn

### GetWorstCaseOutputInterceptPower(string, out double)

Gets the worst case output intercept power which is equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetWorstCaseOutputInterceptPower(string selectorString, out double value)

#### Remarks

This method gets the value of [IMResultsWorstCaseOutputInterceptPower](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and ImIntermod number. Example: "ImIntermod0", "result::r1/ImIntermod0". You can use the BuildIntermodString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the worst case output intercept power which is equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXIMResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmximresults.html language=enus -->
## TOPIC 00382: RFmxSpecAnMXIMResults Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmximresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmximresults.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the IM measurement results. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXIMResults : RFmxSpecAnMXSubObjectMethodsNameDescriptionFetchFundamentalMeasurement(string, double, out double, out double)Fetches

### RFmxSpecAnMXIMResults Class

Provides methods to fetch and read the IM measurement results.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXIMResults : RFmxSpecAnMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchFundamentalMeasurement(string, double, out double, out double) | Fetches the peak powers of the two fundamental tones. |
| FetchInterceptPower(string, double, out int, out double, out double, out double) | Fetches the output intercept powers for the intermod. Use "intermod(n)" as the selector string to read results from this method. |
| FetchInterceptPowerArray(string, double, ref int[], ref double[], ref double[], ref double[]) | Fetches the output intercept powers for the intermod. |
| FetchIntermodMeasurement(string, double, out int, out double, out double) | Fetches the peak powers of the lower and upper intermods. Use "intermod(n)" as the selector string to read results from this method. |
| FetchIntermodMeasurementArray(string, double, ref int[], ref double[], ref double[]) | Fetches an array of peak powers of the lower and upper intermods. |
| FetchSpectrum(string, double, int, ref Spectrum< float >) | Fetches the spectrum trace in IM measurement corresponding to the specified spectrumIndex. |
| GetFundamentalLowerTonePower(string, out double) | Gets the peak power measured around the lower tone frequency when you set the SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the lower tone frequency. |
| GetFundamentalUpperTonePower(string, out double) | Gets the peak power measured around the upper tone frequency when you set the SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the upper tone frequency. |
| GetIntermodOrder(string, out int) | Gets the order of the intermod. |
| GetLowerIntermodPower(string, out double) | Gets the peak power measured around the lower intermod frequency when you set the SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the lower intermod frequency. |
| GetLowerIntermodRelativePower(string, out double) | Gets the relative peak power measured around the lower intermod frequency when you set the SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBc. When you set the IM Local Peak Search Enabled method to False, the measurement returns the relative power at the lower intermod frequency. |
| GetLowerOutputInterceptPower(string, out double) | Gets the lower output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. |
| GetUpperIntermodPower(string, out double) | Gets the peak power measured around the upper intermod frequency when you set the SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled method to False, the measurement returns the power at the upper intermod frequency. |
| GetUpperIntermodRelativePower(string, out double) | Gets the relative peak power measured around the upper intermod frequency when you set the SetLocalPeakSearchEnabled(string, RFmxSpecAnMXIMLocalPeakSearchEnabled) method to True. This value is expressed in dBc. When you set the IM Local Peak Search Enabled method to False, the measurement returns the relative power at the upper intermod frequency. |
| GetUpperOutputInterceptPower(string, out double) | Gets the upper output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. |
| GetWorstCaseIntermodAbsolutePower(string, out double) | Gets the worst case intermod power that is equal to the maximum of the values of both the IM Results Upper Intermod Power and IM Results Lower Intermod Power results. This value is expressed in dBm. |
| GetWorstCaseIntermodRelativePower(string, out double) | Gets the worst case intermod relative power that is equal to the maximum of the values of both the IM Results Upper Intermod Relative Power and IM Results Lower Intermod Relative Power results. This value is expressed in dBc. |
| GetWorstCaseOutputInterceptPower(string, out double) | Gets the worst case output intercept power which is equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiq-configuration.html language=enus -->
## TOPIC 00383: Configuration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiq-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiq-configuration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXIQConfiguration instance that enables configuration of I/Q measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXIQConfiguration Configuration { get; }RemarksReturns an object of type RFmxSpecAnMXIQConfiguration.

### Configuration

Gets the [RFmxSpecAnMXIQConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration.html) instance that enables configuration of I/Q measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXIQConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration.html) Configuration { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXIQConfiguration.

Parent topic:

RFmxSpecAnMXIQ Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiq-results.html language=enus -->
## TOPIC 00384: Results

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiq-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiq-results.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXIQResults instance that provides methods to retrieve I/Q measurement results. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXIQResults Results { get; }RemarksReturns an object of type RFmxSpecAnMXIQResults.

### Results

Gets the [RFmxSpecAnMXIQResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults.html) instance that provides methods to retrieve I/Q measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXIQResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults.html) Results { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXIQResults.

Parent topic:

RFmxSpecAnMXIQ Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiq.html language=enus -->
## TOPIC 00385: RFmxSpecAnMXIQ Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiq.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiq.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an I/Q measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXIQ : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny public static members of this type are th

### RFmxSpecAnMXIQ Class

Represents an I/Q measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXIQ : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxSpecAnMXIQConfiguration instance that enables configuration of I/Q measurement. |
| Results | Gets the RFmxSpecAnMXIQResults instance that provides methods to retrieve I/Q measurement results. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-configureacquisition__string-double-int-double-double.html language=enus -->
## TOPIC 00386: ConfigureAcquisition(string, double, int, double, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-configureacquisition__string-double-int-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-configureacquisition__string-double-int-double-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the acquisition settings for the I/Q measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureAcquisition(string selectorString, double sampleRate, int numberOfRecords, double acquisitionTime, double pretriggerTime)RemarksThis method maps to the RFmxSpecAn_IQCfgA

### ConfigureAcquisition(string, double, int, double, double)

Configures the acquisition settings for the I/Q measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureAcquisition(string selectorString, double sampleRate, int numberOfRecords, double acquisitionTime, double pretriggerTime)

#### Remarks

This method maps to the RFmxSpecAn_IQCfgAcquisition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sampleRate | double | Specifies the acquisition sample rate, in samples per second (S/s). |
| numberOfRecords | int | Specifies the number of records to acquire. |
| acquisitionTime | double | Specifies the acquisition time, in seconds, for the I/Q measurement. |
| pretriggerTime | double | Specifies the pretrigger time, in seconds, for the I/Q measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXIQConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00387: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the I/Q measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_IQSetMeasurementEnabled() function in C.ParametersNameTypeDescriptionselectorStringstringPass an

### SetMeasurementEnabled(string, bool)

Sets whether to enable the I/Q measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_IQSetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the I/Q measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXIQConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-setsamplerate__string-double.html language=enus -->
## TOPIC 00388: SetSampleRate(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-setsamplerate__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqconfiguration-setsamplerate__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition sample rate, in samples per second (S/s). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSampleRate(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_IQSetSampleRate() function in C.ParametersNameTypeDescriptionselectorStringstringPas

### SetSampleRate(string, double)

Sets the acquisition sample rate, in samples per second (S/s).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSampleRate(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_IQSetSampleRate() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the acquisition sample rate, in S/s. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXIQConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqdeleterecordonfetch.html language=enus -->
## TOPIC 00389: RFmxSpecAnMXIQDeleteRecordOnFetch Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqdeleterecordonfetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqdeleterecordonfetch.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement deletes the fetched record. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIQDeleteRecordOnFetchMembersNameValueDescriptionFalse0The measurement does not delete the fetched record. True1The measurement deletes the fetched record.

### RFmxSpecAnMXIQDeleteRecordOnFetch Enumeration

Specifies whether the measurement deletes the fetched record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIQDeleteRecordOnFetch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement does not delete the fetched record. |
| True | 1 | The measurement deletes the fetched record. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00390: RFmxSpecAnMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFmx.SpecAnMX.RFmxSpecAnMX.SetIQPowerEdgeTriggerLevel method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXIQPowerEdgeTriggerLevelTypeMembersNameValueDescriptionRelative0IQ Power EdgeLevel is relative to the value of the RFmxSpecAnMX.Confi

### RFmxSpecAnMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the RFmx.SpecAnMX.RFmxSpecAnMX.SetIQPowerEdgeTriggerLevel method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | IQ Power EdgeLevel is relative to the value of the RFmxSpecAnMX.ConfigureReferenceLevel method. |
| Absolute | 1 | The IQ Power Edge Level specifies the absolute power. This value is expressed in units specified by the value of the RFmxSpecAnMX.ConfigureReferenceLevelUnits method. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00391: RFmxSpecAnMXIQPowerEdgeTriggerSlope Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqpoweredgetriggerslope.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This enum is used only when you set the Trigger Type to IQPowerEdge. SyntaxNamespace: N

### RFmxSpecAnMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This enum is used only when you set the Trigger Type to [IQPowerEdge](nationalinstruments-rfmx-specanmx-rfmxspecanmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXIQPowerEdgeTriggerSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults-fetchdata__string-double-int-long-ref.html language=enus -->
## TOPIC 00392: FetchData(string, double, int, long, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults-fetchdata__string-double-int-long-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults-fetchdata__string-double-int-long-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from a single record in an acquisition. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchData(string selectorString, double timeout, int recordToFetch, long samplesToRead, ref ComplexWaveform< ComplexSingle > data)RemarksThis method maps to the RFmxSpecAn_IQFetchDat

### FetchData(string, double, int, long, ref ComplexWaveform< ComplexSingle >)

Fetches I/Q data from a single record in an acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchData(string selectorString, double timeout, int recordToFetch, long samplesToRead, ref ComplexWaveform< ComplexSingle > data)

#### Remarks

This method maps to the RFmxSpecAn_IQFetchData() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| recordToFetch | int | Specifies the record to retrieve. Record numbers are zero-based. |
| samplesToRead | long | Specifies the number of samples to fetch. A value of -1 specifies that RFmx fetches all samples. |
| data | ref ComplexWaveform< ComplexSingle > | Returns the data acquired by the I/Q measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXIQResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults.html language=enus -->
## TOPIC 00393: RFmxSpecAnMXIQResults Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxiqresults.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch the I/Q measurement results. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXIQResults : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny public sta

### RFmxSpecAnMXIQResults Class

Provides methods to fetch the I/Q measurement results.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXIQResults : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| FetchData(string, double, int, long, ref ComplexWaveform< ComplexSingle >) | Fetches I/Q data from a single record in an acquisition. |
| GetRecordsDone(string, out int) | Fetches the number of records that RFmx has acquired. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlimitedconfigurationchange.html language=enus -->
## TOPIC 00394: RFmxSpecAnMXLimitedConfigurationChange Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlimitedconfigurationchange.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXLimitedConfigurationChangeMembersNameValueDescriptionDisabled0This is the normal mode of RFmx operation. All configuration c

### RFmxSpecAnMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXLimitedConfigurationChange

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| NoChange | 1 | Signal configuration and RFmxInstr configuration are locked after the first Commit or Initiate of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency | 2 | Signal configuration, other than center frequency, external attenuation, and RFmxInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter, only the Center Frequency and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| ReferenceLevel | 3 | Signal configuration, other than the reference level and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only the SetReferenceLevel(string, double) method value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the SetIQPowerEdgeTriggerLevelType(string, RFmxSpecAnMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| FrequencyAndReferenceLevel | 4 | Signal configuration, other than center frequency, reference level, external attenuation, and RFInstr configuration, is locked after the first Commit or Initiate of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| SelectedPortsFrequencyAndReferenceLevel | 5 | Signal configuration, other than Selected Ports, Center frequency, Reference level, External attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-abortmeasurements__string.html language=enus -->
## TOPIC 00395: AbortMeasurements(string)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-abortmeasurements__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-abortmeasurements__string.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with list instance, which were previously initiated by the Initiate or measurement read methods. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int AbortMeasurements(string selectorString)RemarksCalling this method is optional, unless you want

### AbortMeasurements(string)

Stops acquisition and measurements associated with list instance, which were previously initiated by the Initiate or measurement read methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int AbortMeasurements(string selectorString)

#### Remarks

Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-commit__string.html language=enus -->
## TOPIC 00396: Commit(string)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-commit__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-commit__string.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this method is optional. RFmxSpecAn commits settings to the hardware when you call the RFmxInstrMX Initiate or any of the measurement Read methods. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int Commit(string selectorString)ParametersNameTypeDe

### Commit(string)

Commits settings to the hardware. Calling this method is optional. RFmxSpecAn commits settings to the hardware when you call the RFmxInstrMX Initiate or any of the measurement Read methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int Commit(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-createliststep.html language=enus -->
## TOPIC 00397: CreateListStep()

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-createliststep.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-createliststep.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new list step instance in a list. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMX CreateListStep()ReturnsReturns the status code of this method. The status code either indicates success or describes an error or warning condition.

### CreateListStep()

Creates a new list step instance in a list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMX](nationalinstruments-rfmx-specanmx-rfmxspecanmx.html) CreateListStep()

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-isdisposed.html language=enus -->
## TOPIC 00398: IsDisposed

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-isdisposed.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the list has been disposed. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic bool IsDisposed { get; }Remarkstrue if the list is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the list has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public bool IsDisposed { get; }

#### Remarks

true if the list is disposed; otherwise, false.

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-listname.html language=enus -->
## TOPIC 00399: ListName

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-listname.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-listname.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list name. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic string ListName { get; }RemarksReturns a string representing the list name

### ListName

Gets the list name.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public string ListName { get; }

#### Remarks

Returns a string representing the list name

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-listtype.html language=enus -->
## TOPIC 00400: ListType

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-listtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-listtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxSpecAnMXList. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic Type ListType { get; }RemarksReturns the type of list object.

### ListType

Gets the Type object for RFmxSpecAnMXList.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public Type ListType { get; }

#### Remarks

Returns the type of list object.

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-setnumberofsteps__string-int.html language=enus -->
## TOPIC 00401: SetNumberOfSteps(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-setnumberofsteps__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxlist-setnumberofsteps__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets number of list step instances in a list. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfSteps(string selectorString, int value)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The list name that is passed when creating the list is used.valueintSpec

### SetNumberOfSteps(string, int)

Sets number of list step instances in a list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfSteps(string selectorString, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |
| value | int | Specifies the number of list step instances in a list. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXList Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarker.html language=enus -->
## TOPIC 00402: RFmxSpecAnMXMarker Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarker.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarker.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Marker measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXMarker : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny public static members of this type

### RFmxSpecAnMXMarker Class

Represents a Marker measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXMarker : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxSpecAnMXMarkerConfiguration instance that allows configuration of Marker measurement. |
| Results | Gets the RFmxSpecAnMXMarkerResults instance that provides methods to retrieve Marker measurement results. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurebandspan__string-double.html language=enus -->
## TOPIC 00403: ConfigureBandSpan(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurebandspan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurebandspan__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band span of the selected marker. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureBandSpan(string selectorString, double span)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector str

### ConfigureBandSpan(string, double)

Configures the band span of the selected marker. 
Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureBandSpan(string selectorString, double span)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example:"marker0" You can use the RFmxSpecAn_BuildMarkerString2 method to build the selector string. |
| span | double | Specifies the width of the span for the selected marker. This method selects the trace data within the specified span to perform specified marker method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurefunctiontype__string-rfmxspecanmxmarkerfunctiontype.html language=enus -->
## TOPIC 00404: ConfigureFunctionType(string, RFmxSpecAnMXMarkerFunctionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurefunctiontype__string-rfmxspecanmxmarkerfunctiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurefunctiontype__string-rfmxspecanmxmarkerfunctiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker method type. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFunctionType(string selectorString, RFmxSpecAnMXMarkerFunctionType functionType)ParametersNameTypeDescriptionselectorStringstringSp

### ConfigureFunctionType(string, RFmxSpecAnMXMarkerFunctionType)

Configures the marker method type. 
Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFunctionType(string selectorString, RFmxSpecAnMXMarkerFunctionType functionType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example:"marker0" You can use the RFmxSpecAn_BuildMarkerString2 method to build the selector string. |
| functionType | RFmxSpecAnMXMarkerFunctionType | specifies the function type for the selected marker. The default value is Off. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurenumberofmarkers__string-int.html language=enus -->
## TOPIC 00405: ConfigureNumberOfMarkers(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurenumberofmarkers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurenumberofmarkers__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of markers. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureNumberOfMarkers(string selectorString, int numberOfMarkers)RemarksThis method maps to the RFmxSpecAn_MarkerCfgNumberOfMarkers() function in C.ParametersNameTypeDescriptionselectorStringstringPass

### ConfigureNumberOfMarkers(string, int)

Configures the number of markers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureNumberOfMarkers(string selectorString, int numberOfMarkers)

#### Remarks

This method maps to the RFmxSpecAn_MarkerCfgNumberOfMarkers() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfMarkers | int | Specifies the number of markers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurepeakexcursion__string-rfmxspecanmxmarkerpeakexcursionenabled-double.html language=enus -->
## TOPIC 00406: ConfigurePeakExcursion(string, RFmxSpecAnMXMarkerPeakExcursionEnabled, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurepeakexcursion__string-rfmxspecanmxmarkerpeakexcursionenabled-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurepeakexcursion__string-rfmxspecanmxmarkerpeakexcursionenabled-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak excursion. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigurePeakExcursion(string selectorString, RFmxSpecAnMXMarkerPeakExcursionEnabled peakExcursionEnabled, double peakExcursion)RemarksThis method maps to the RFmxSpecAn_MarkerCfgPeakExcursion() function in C

### ConfigurePeakExcursion(string, RFmxSpecAnMXMarkerPeakExcursionEnabled, double)

Configures the peak excursion.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigurePeakExcursion(string selectorString, RFmxSpecAnMXMarkerPeakExcursionEnabled peakExcursionEnabled, double peakExcursion)

#### Remarks

This method maps to the RFmxSpecAn_MarkerCfgPeakExcursion() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| peakExcursionEnabled | RFmxSpecAnMXMarkerPeakExcursionEnabled | Specifies whether to enable the peak excursion check for the trace while finding the peaks. |
| peakExcursion | double | Specifies the peak excursion value for finding the peaks on trace when you set the peakExcursionEnabled parameter to True. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered a peak. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurereferencemarker__string-int.html language=enus -->
## TOPIC 00407: ConfigureReferenceMarker(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurereferencemarker__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurereferencemarker__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker to be used as reference marker when you set the RFmxSpecAnMXMarkerType to Delta. The value set by this method is not used when you set the RFmxSpecAnMXMarkerType to Normal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureReferenceMarker(string selectorStri

### ConfigureReferenceMarker(string, int)

Configures the marker to be used as reference marker when you set the [RFmxSpecAnMXMarkerType](nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertype.html) to [Delta](nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertype.html). The value set by this method is not used when you set the [RFmxSpecAnMXMarkerType](nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertype.html) to [Normal](nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureReferenceMarker(string selectorString, int referenceMarker)

#### Remarks

This method maps to the RFmxSpecAn_MarkerCfgReferenceMarker() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the marker number. Example: "marker0". You can use the BuildMarkerString2(string, int) method to build the selector string. |
| referenceMarker | int | Specifies the marker to be used as reference marker when you set the RFmxSpecAnMXMarkerType to Delta. The value set by this method is not used when you set the RFmxSpecAnMXMarkerType to Normal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurethreshold__string-rfmxspecanmxmarkerthresholdenabled-double.html language=enus -->
## TOPIC 00408: ConfigureThreshold(string, RFmxSpecAnMXMarkerThresholdEnabled, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurethreshold__string-rfmxspecanmxmarkerthresholdenabled-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configurethreshold__string-rfmxspecanmxmarkerthresholdenabled-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the threshold to use for peak search. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureThreshold(string selectorString, RFmxSpecAnMXMarkerThresholdEnabled thresholdEnabled, double threshold)RemarksThis method maps to the RFmxSpecAn_MarkerCfgThreshold() function in C.P

### ConfigureThreshold(string, RFmxSpecAnMXMarkerThresholdEnabled, double)

Configures the threshold to use for peak search.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureThreshold(string selectorString, RFmxSpecAnMXMarkerThresholdEnabled thresholdEnabled, double threshold)

#### Remarks

This method maps to the RFmxSpecAn_MarkerCfgThreshold() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| thresholdEnabled | RFmxSpecAnMXMarkerThresholdEnabled | Specifies whether to enable the threshold for the trace while finding the peaks. |
| threshold | double | Specifies the threshold for finding the peaks on the trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configuretype__string-rfmxspecanmxmarkertype.html language=enus -->
## TOPIC 00409: ConfigureType(string, RFmxSpecAnMXMarkerType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configuretype__string-rfmxspecanmxmarkertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerconfiguration-configuretype__string-rfmxspecanmxmarkertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker type. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureType(string selectorString, RFmxSpecAnMXMarkerType markerType)RemarksThis method maps to the RFmxSpecAn_MarkerCfgType() function in C.ParametersNameTypeDescriptionselectorStringstringSpecifies the marke

### ConfigureType(string, RFmxSpecAnMXMarkerType)

Configures the marker type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureType(string selectorString, RFmxSpecAnMXMarkerType markerType)

#### Remarks

This method maps to the RFmxSpecAn_MarkerCfgType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the marker number. Example: "marker0". You can use the BuildMarkerString2(string, int) method to build the selector string. |
| markerType | RFmxSpecAnMXMarkerType | Specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerpeakexcursionenabled.html language=enus -->
## TOPIC 00410: RFmxSpecAnMXMarkerPeakExcursionEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerpeakexcursionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerpeakexcursionenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the peak excursion check for the trace while finding the peaks. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXMarkerPeakExcursionEnabledMembersNameValueDescriptionFalse0Disables the peak excursion check while finding the peaks on trace. True1En

### RFmxSpecAnMXMarkerPeakExcursionEnabled Enumeration

Specifies whether to enable the peak excursion check for the trace while finding the peaks.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXMarkerPeakExcursionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the peak excursion check while finding the peaks on trace. |
| True | 1 | Enables the peak excursion check while finding the peaks on trace. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerresults-nextpeak__string-rfmxspecanmxmarkernextpeak-out.html language=enus -->
## TOPIC 00411: NextPeak(string, RFmxSpecAnMXMarkerNextPeak, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerresults-nextpeak__string-rfmxspecanmxmarkernextpeak-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkerresults-nextpeak__string-rfmxspecanmxmarkernextpeak-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the marker to the next highest, next left, or next right peak above the threshold on the configured trace. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int NextPeak(string selectorString, RFmxSpecAnMXMarkerNextPeak nextPeak, out bool nextPeakFound)RemarksThis method maps to the RFm

### NextPeak(string, RFmxSpecAnMXMarkerNextPeak, out bool)

Moves the marker to the next highest, next left, or next right peak above the threshold on the configured trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int NextPeak(string selectorString, RFmxSpecAnMXMarkerNextPeak nextPeak, out bool nextPeakFound)

#### Remarks

This method maps to the RFmxSpecAn_MarkerNextPeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and marker number. Example: "marker0", "result::r1/marker0". You can use the BuildMarkerString2(string, int) method to build the selector string. |
| nextPeak | RFmxSpecAnMXMarkerNextPeak | Specifies the next peak on the trace. |
| nextPeakFound | out bool | Upon return, indicates whether the next peak has been found on the trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXMarkerResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertrace.html language=enus -->
## TOPIC 00412: RFmxSpecAnMXMarkerTrace Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxmarkertrace.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement trace to be used by the marker. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXMarkerTraceMembersNameValueDescriptionAcpSpectrum0The marker uses the ACP spectrum trace. CcdfGaussianProbabilitiesTrace1The marker uses the CCDF Gaussian probabilitie

### RFmxSpecAnMXMarkerTrace Enumeration

Configures the measurement trace to be used by the marker.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXMarkerTrace

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AcpSpectrum | 0 | The marker uses the ACP spectrum trace. |
| CcdfGaussianProbabilitiesTrace | 1 | The marker uses the CCDF Gaussian probabilities trace. |
| CcdfProbabilitiesTrace | 2 | The marker uses the CCDF probabilities trace. |
| ChpSpectrum | 3 | The marker uses the CHP spectrum trace. |
| FcntPowerTrace | 4 | The marker uses the frequency count (Fcnt) power trace. |
| ObwSpectrum | 5 | The marker uses the OBW spectrum trace. |
| SemSpectrum | 6 | The marker uses the SEM spectrum trace. |
| Spectrum | 7 | The marker uses the Spectrum trace. |
| TxpPowerTrace | 8 | The marker uses the TXP power trace. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnf.html language=enus -->
## TOPIC 00413: RFmxSpecAnMXNF Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnf.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the NF measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXNF : RFmxSpecAnMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxSpecAnMXNFConfiguration instance that provides methods to configure the NF measureme

### RFmxSpecAnMXNF Class

Represents the NF measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXNF : RFmxSpecAnMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxSpecAnMXNFConfiguration instance that provides methods to configure the NF measurement. |
| Results | Gets the RFmxSpecAnMXNFResults instance that provides methods to fetch and read the NF measurement results. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfaveragingenabled.html language=enus -->
## TOPIC 00414: RFmxSpecAnMXNFAveragingEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the noise figure (NF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXNFAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The NF measurement uses the value of th

### RFmxSpecAnMXNFAveragingEnabled Enumeration

Specifies whether to enable averaging for the noise figure (NF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The NF measurement uses the value of the SetAveragingCount(string, int) method as the number of acquisitions for each frequency which you specify in the SetFrequencyList(string, double[]) method, over which the NF measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationdatavalid.html language=enus -->
## TOPIC 00415: RFmxSpecAnMXNFCalibrationDataValid Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationdatavalid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationdatavalid.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the calibration data is valid for the configuration specified by the signal name in the selectorString parameter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXNFCalibrationDataValidMembersNameValueDescriptionFalse0Calibration data is not present for one o

### RFmxSpecAnMXNFCalibrationDataValid Enumeration

Returns whether the calibration data is valid for the configuration specified by the signal name in the selectorString parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFCalibrationDataValid

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Calibration data is not present for one or more frequency points in the list or the difference between the current device temperature and the temperature at which calibration was performed exceeds the tolerance specified by the NFDeviceTemperatureTolerance method. |
| True | 1 | Calibration data is present for all of the frequencies in the list. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationlosscompensationenabled.html language=enus -->
## TOPIC 00416: RFmxSpecAnMXNFCalibrationLossCompensationEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationlosscompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationlosscompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the SetYFactorNoiseSourceLoss(string, double[]) method. SyntaxNamespace: National

### RFmxSpecAnMXNFCalibrationLossCompensationEnabled Enumeration

Specifies whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the [SetYFactorNoiseSourceLoss(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceloss__string-double_arr1.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFCalibrationLossCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The NF measurement ignores the ohmic losses. |
| True | 1 | The NF measurement accounts for the ohmic losses. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcoldsourcemode.html language=enus -->
## TOPIC 00417: RFmxSpecAnMXNFColdSourceMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcoldsourcemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcoldsourcemode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXNFColdSourceModeMembersNameValueDescriptionMeasure0The no

### RFmxSpecAnMXNFColdSourceMode Enumeration

Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFColdSourceMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Measure | 0 | The noise figure (NF) measurement computes the noise characteristics of the DUT and compensates for the noise figure of the analyzer. |
| Calibrate | 1 | The NF measurement computes the noise characteristics of the analyzer. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureaveraging__string-rfmxspecanmxnfaveragingenabled-int.html language=enus -->
## TOPIC 00418: ConfigureAveraging(string, RFmxSpecAnMXNFAveragingEnabled, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureaveraging__string-rfmxspecanmxnfaveragingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureaveraging__string-rfmxspecanmxnfaveragingenabled-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the noise figure (NF) measurement.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureAveraging(string selectorString, RFmxSpecAnMXNFAveragingEnabled averagingEnabled, int averagingCount)ParametersNameTypeDescriptionselectorStringstringPass an empty string.

### ConfigureAveraging(string, RFmxSpecAnMXNFAveragingEnabled, int)

Configures averaging for the noise figure (NF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureAveraging(string selectorString, RFmxSpecAnMXNFAveragingEnabled averagingEnabled, int averagingCount)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxSpecAnMXNFAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configurecoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html language=enus -->
## TOPIC 00419: ConfigureColdSourceMode(string, RFmxSpecAnMXNFColdSourceMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configurecoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configurecoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the cold source based noise figure (NF) measurement to perform the calibration step or the measurement step.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureColdSourceMode(string selectorString, RFmxSpecAnMXNFColdSourceMode coldSourceMode)ParametersNameTypeDescription

### ConfigureColdSourceMode(string, RFmxSpecAnMXNFColdSourceMode)

Configures the cold source based noise figure (NF) measurement to perform the calibration step or the measurement step.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureColdSourceMode(string selectorString, RFmxSpecAnMXNFColdSourceMode coldSourceMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| coldSourceMode | RFmxSpecAnMXNFColdSourceMode | Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configurefrequencyliststartstopstep__string-double-double-double.html language=enus -->
## TOPIC 00420: ConfigureFrequencyListStartStopStep(string, double, double, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configurefrequencyliststartstopstep__string-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configurefrequencyliststartstopstep__string-double-double-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list of frequencies at which to perform the noise figure (NF) measurement. The start frequency and stop frequency points are inclusive in the frequency list.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFrequencyListStartStopStep(string selectorString, double s

### ConfigureFrequencyListStartStopStep(string, double, double, double)

Configures the list of frequencies at which to perform the noise figure (NF) measurement. The start frequency and stop frequency points are inclusive in the frequency list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFrequencyListStartStopStep(string selectorString, double startFrequency, double stopFrequency, double stepSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| startFrequency | double | Specifies the lowest frequency at which to perform the NF measurement. This value is expressed in Hz. |
| stopFrequency | double | Specifies the highest frequency at which to perform the NF measurement. This value is expressed in Hz. |
| stepSize | double | Specifies the spacing between adjacent frequency points in the list of frequencies at which to perform the NF measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configuremeasurementbandwidth__string-double.html language=enus -->
## TOPIC 00421: ConfigureMeasurementBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configuremeasurementbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configuremeasurementbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the effective noise-bandwidth in which power measurements are performed in the noise figure (NF) measurement.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureMeasurementBandwidth(string selectorString, double measurementBandwidth)ParametersNameTypeDescriptionselectorS

### ConfigureMeasurementBandwidth(string, double)

Configures the effective noise-bandwidth in which power measurements are performed in the noise figure (NF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureMeasurementBandwidth(string selectorString, double measurementBandwidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementBandwidth | double | Specifies the effective noise-bandwidth in which power measurements are performed for the NF measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configuremeasurementinterval__string-double.html language=enus -->
## TOPIC 00422: ConfigureMeasurementInterval(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configuremeasurementinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configuremeasurementinterval__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the duration for which the signals are acquired at each frequency to perform the noise figure (NF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureMeasurementInterval(string selectorString, double measurementInterval)ParametersNameTypeDescriptionselector

### ConfigureMeasurementInterval(string, double)

Configures the duration for which the signals are acquired at each frequency to perform the noise figure (NF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureMeasurementInterval(string selectorString, double measurementInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the duration for which signals are aquired at each frequency which you specify in the SetFrequencyList(string, double[]) method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureyfactormode__string-rfmxspecanmxnfyfactormode.html language=enus -->
## TOPIC 00423: ConfigureYFactorMode(string, RFmxSpecAnMXNFYFactorMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureyfactormode__string-rfmxspecanmxnfyfactormode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureyfactormode__string-rfmxspecanmxnfyfactormode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Y-Factor based noise figure (NF) measurement to perform the calibration step or the measurement step.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureYFactorMode(string selectorString, RFmxSpecAnMXNFYFactorMode yFactorMode)ParametersNameTypeDescriptionselectorStri

### ConfigureYFactorMode(string, RFmxSpecAnMXNFYFactorMode)

Configures the Y-Factor based noise figure (NF) measurement to perform the calibration step or the measurement step.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureYFactorMode(string selectorString, RFmxSpecAnMXNFYFactorMode yFactorMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| yFactorMode | RFmxSpecAnMXNFYFactorMode | Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureyfactornoisesourcesettlingtime__string-double.html language=enus -->
## TOPIC 00424: ConfigureYFactorNoiseSourceSettlingTime(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureyfactornoisesourcesettlingtime__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-configureyfactornoisesourcesettlingtime__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the time required for the acquisition to wait till the noise source used in the Y-Factor method settles to hot or cold state when the noise source is powered on or off.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureYFactorNoiseSourceSettlingTime(string selectorStrin

### ConfigureYFactorNoiseSourceSettlingTime(string, double)

Configures the time required for the acquisition to wait till the noise source used in the Y-Factor method settles to hot or cold state when the noise source is powered on or off.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureYFactorNoiseSourceSettlingTime(string selectorString, double settlingTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| settlingTime | double | Specifies the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is enabled or disabled. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcalibrationlossfrequency__string-ref.html language=enus -->
## TOPIC 00425: GetCalibrationLossFrequency(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcalibrationlossfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcalibrationlossfrequency__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. THis value is expressed in Hz. This method is applicable only when you set the SetYFactorMode(string, RFmxSpecAnMXNFYFactorMode) method to Calibrate and set the SetMeasurementMethod(

### GetCalibrationLossFrequency(string, ref double[])

Gets an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. THis value is expressed in Hz. This method is applicable only when you set the [SetYFactorMode(string, RFmxSpecAnMXNFYFactorMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactormode__string-rfmxspecanmxnfyfactormode.html) method to [Calibrate](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactormode.html) and set the [SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setmeasurementmethod__string-rfmxspecanmxnfmeasurementmethod.html) method to [YFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfmeasurementmethod.html), or when you set the [SetColdSourceMode(string, RFmxSpecAnMXNFColdSourceMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html) method to [Calibrate](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactormode.html) and set the NF Meas Method method to [ColdSource](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCalibrationLossFrequency(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFCalibrationLossFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is an empty array.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref double[] | Upon return, contains an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. THis value is expressed in Hz. This method is applicable only when you set the SetYFactorMode(string, RFmxSpecAnMXNFYFactorMode) method to Calibrate and set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor, or when you set the SetColdSourceMode(string, RFmxSpecAnMXNFColdSourceMode) method to Calibrate and set the NF Meas Method method to ColdSource. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcoldsourceduts22__string-ref.html language=enus -->
## TOPIC 00426: GetColdSourceDutS22(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcoldsourceduts22__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcoldsourceduts22__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of the output-reflections of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the SetColdSourceDutSParametersFr

### GetColdSourceDutS22(string, ref double[])

Gets an array of the output-reflections of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the [SetColdSourceDutSParametersFrequency(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcoldsourcedutsparametersfrequency__string-double_arr1.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetColdSourceDutS22(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFColdSourceDutS22](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is an empty array.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref double[] | Upon return, contains an array of the output-reflections of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the SetColdSourceDutSParametersFrequency(string, double[]) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcoldsourceinputterminationvswrfrequency__string-ref.html language=enus -->
## TOPIC 00427: GetColdSourceInputTerminationVswrFrequency(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcoldsourceinputterminationvswrfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getcoldsourceinputterminationvswrfrequency__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of frequencies corresponding to the voltage standing wave ratios (VSWR) of the microwave termination used in the cold source method as specified by the SetColdSourceInputTerminationVswr(string, double[]) method. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.S

### GetColdSourceInputTerminationVswrFrequency(string, ref double[])

Gets an array of frequencies corresponding to the voltage standing wave ratios (VSWR) of the microwave termination used in the cold source method as specified by the [SetColdSourceInputTerminationVswr(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcoldsourceinputterminationvswr__string-double_arr1.html) method. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetColdSourceInputTerminationVswrFrequency(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFColdSourceInputTerminationVswrFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is an empty array.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref double[] | Upon return, contains an array of frequencies corresponding to the voltage standing wave ratios (VSWR) of the microwave termination used in the cold source method as specified by the SetColdSourceInputTerminationVswr(string, double[]) method. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getdutoutputloss__string-ref.html language=enus -->
## TOPIC 00428: GetDutOutputLoss(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getdutoutputloss__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getdutoutputloss__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the SetDutOutputLossCompensationEnabled(string, RFmxSpecAnMXNF

### GetDutOutputLoss(string, ref double[])

Gets the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the [SetDutOutputLossCompensationEnabled(string, RFmxSpecAnMXNFDutOutputLossCompensationEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosscompensationenabled__string-rfmxspecanmxnfdutoutputlosscompensationenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutoutputlosscompensationenabled.html). Specify the array of frequencies at which the losses were measured using the [SetDutOutputLossFrequency(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlossfrequency__string-double_arr1.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDutOutputLoss(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFDutOutputLoss](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is an empty array.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref double[] | Upon return, contains the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the SetDutOutputLossCompensationEnabled(string, RFmxSpecAnMXNFDutOutputLossCompensationEnabled) method to True. Specify the array of frequencies at which the losses were measured using the SetDutOutputLossFrequency(string, double[]) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getdutoutputlosscompensationenabled__string-out.html language=enus -->
## TOPIC 00429: GetDutOutputLossCompensationEnabled(string, out RFmxSpecAnMXNFDutOutputLossCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getdutoutputlosscompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getdutoutputlosscompensationenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetDutOutputLossCompensationEnabled(string selectorString, out RFmxSpecAnMXNFDutOutputLossCompe

### GetDutOutputLossCompensationEnabled(string, out RFmxSpecAnMXNFDutOutputLossCompensationEnabled)

Gets whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDutOutputLossCompensationEnabled(string selectorString, out RFmxSpecAnMXNFDutOutputLossCompensationEnabled value)

#### Remarks

This method gets the value of [NFDutOutputLossCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutoutputlosscompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXNFDutOutputLossCompensationEnabled | Upon return, contains whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getmeasurementbandwidth__string-out.html language=enus -->
## TOPIC 00430: GetMeasurementBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getmeasurementbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getmeasurementbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementBandwidth(string selectorString, out double value)RemarksThis method gets the

### GetMeasurementBandwidth(string, out double)

Gets the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [NFMeasurementBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 100 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getmeasurementinterval__string-out.html language=enus -->
## TOPIC 00431: GetMeasurementInterval(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getmeasurementinterval__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration for which the signals are acquired at each frequency which you specify in the SetFrequencyList(string, double[]) method. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementInterval(string selectorString, out double value)R

### GetMeasurementInterval(string, out double)

Gets the duration for which the signals are acquired at each frequency which you specify in the [SetFrequencyList(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencylist__string-double_arr1.html) method. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [NFMeasurementInterval](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1 ms.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the duration for which the signals are acquired at each frequency which you specify in the SetFrequencyList(string, double[]) method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelosscompensationenabled__string-out.html language=enus -->
## TOPIC 00432: GetYFactorNoiseSourceLossCompensationEnabled(string, out RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelosscompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelosscompensationenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetYFactorNoiseSourceLossCompensationEnabled(string se

### GetYFactorNoiseSourceLossCompensationEnabled(string, out RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled)

Gets whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetYFactorNoiseSourceLossCompensationEnabled(string selectorString, out RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled value)

#### Remarks

This method gets the value of [NFYFactorNoiseSourceLossCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactornoisesourcelosscompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled | Upon return, contains whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelossfrequency__string-ref.html language=enus -->
## TOPIC 00433: GetYFactorNoiseSourceLossFrequency(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelossfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelossfrequency__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the SetYFactorNoiseSourceLoss(string, double[]) method. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetYFactorNoiseSourceLossFreq

### GetYFactorNoiseSourceLossFrequency(string, ref double[])

Gets the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the [SetYFactorNoiseSourceLoss(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceloss__string-double_arr1.html) method. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetYFactorNoiseSourceLossFrequency(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFYFactorNoiseSourceLossFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is an empty array.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref double[] | Upon return, contains the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the SetYFactorNoiseSourceLoss(string, double[]) method. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelosstemperature__string-out.html language=enus -->
## TOPIC 00434: GetYFactorNoiseSourceLossTemperature(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelosstemperature__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcelosstemperature__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the physical temperature of the ohmic loss elements specified in the SetYFactorNoiseSourceLoss(string, double[]) method. This value is expressed in kelvin. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetYFactorNoiseSourceLossTemperature(string selectorString, out double value)R

### GetYFactorNoiseSourceLossTemperature(string, out double)

Gets the physical temperature of the ohmic loss elements specified in the [SetYFactorNoiseSourceLoss(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceloss__string-double_arr1.html) method. This value is expressed in kelvin.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetYFactorNoiseSourceLossTemperature(string selectorString, out double value)

#### Remarks

This method gets the value of [NFYFactorNoiseSourceLossTemperature](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 297.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the physical temperature of the ohmic loss elements specified in the SetYFactorNoiseSourceLoss(string, double[]) method. This value is expressed in kelvin. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcesettlingtime__string-out.html language=enus -->
## TOPIC 00435: GetYFactorNoiseSourceSettlingTime(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcesettlingtime__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-getyfactornoisesourcesettlingtime__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetYFactorNoiseSourceSettlingTime(string selectorStr

### GetYFactorNoiseSourceSettlingTime(string, out double)

Gets the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetYFactorNoiseSourceSettlingTime(string selectorString, out double value)

#### Remarks

This method gets the value of [NFYFactorNoiseSourceSettlingTime](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-recommendreferencelevel__string-double-double-out.html language=enus -->
## TOPIC 00436: RecommendReferenceLevel(string, double, double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-recommendreferencelevel__string-double-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-recommendreferencelevel__string-double-double-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer methods. You must not set Mixer Level, Mixer Level Offset, IF Output Power Level Offset, and IF Filter Bandwidth methods in order to obtain an appropr

### RecommendReferenceLevel(string, double, double, out double)

Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer methods. You must not set Mixer Level, Mixer Level Offset, IF Output Power Level Offset, and IF Filter Bandwidth methods in order to obtain an appropriate recommended reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int RecommendReferenceLevel(string selectorString, double dutMaxGain, double dutMaxNoiseFigure, out double referenceLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| dutMaxGain | double | Upon return, contains the expected maximum gain from the DUT. This value is expressed in dB. |
| dutMaxNoiseFigure | double | Upon return, contains the expected maximum noise figure of the DUT. This value is expressed in dB. |
| referenceLevel | out double | Upon return, contains the recommended reference level for the NF measurement. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00437: SetAveragingCount(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXNFAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of NFAvera

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxSpecAnMXNFAveragingEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setaveragingenabled__string-rfmxspecanmxnfaveragingenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [NFAveragingCount](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXNFAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcalibrationlosscompensationenabled__string-rfmxspecanmxnfcalibrationlosscompensationenabled.html language=enus -->
## TOPIC 00438: SetCalibrationLossCompensationEnabled(string, RFmxSpecAnMXNFCalibrationLossCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcalibrationlosscompensationenabled__string-rfmxspecanmxnfcalibrationlosscompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcalibrationlosscompensationenabled__string-rfmxspecanmxnfcalibrationlosscompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the SetYFactorNoiseSourceLoss(string, double[]) method. SyntaxNamespace: NationalInstr

### SetCalibrationLossCompensationEnabled(string, RFmxSpecAnMXNFCalibrationLossCompensationEnabled)

Sets whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the [SetYFactorNoiseSourceLoss(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceloss__string-double_arr1.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCalibrationLossCompensationEnabled(string selectorString, RFmxSpecAnMXNFCalibrationLossCompensationEnabled value)

#### Remarks

This method sets the value of [NFCalibrationLossCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcalibrationlosscompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXNFCalibrationLossCompensationEnabled | Specifies whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the SetYFactorNoiseSourceLoss(string, double[]) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html language=enus -->
## TOPIC 00439: SetColdSourceMode(string, RFmxSpecAnMXNFColdSourceMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setcoldsourcemode__string-rfmxspecanmxnfcoldsourcemode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetColdSourceMode(string selectorString, RFmxSpecAnMXNFColdSourceMode value

### SetColdSourceMode(string, RFmxSpecAnMXNFColdSourceMode)

Sets whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetColdSourceMode(string selectorString, RFmxSpecAnMXNFColdSourceMode value)

#### Remarks

This method sets the value of [NFColdSourceMode](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Measure](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfcoldsourcemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXNFColdSourceMode | Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutinputlosscompensationenabled__string-rfmxspecanmxnfdutinputlosscompensationenabled.html language=enus -->
## TOPIC 00440: SetDutInputLossCompensationEnabled(string, RFmxSpecAnMXNFDutInputLossCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutinputlosscompensationenabled__string-rfmxspecanmxnfdutinputlosscompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutinputlosscompensationenabled__string-rfmxspecanmxnfdutinputlosscompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the noise figure (NF) measurement accounts for ohmic losses between the noise source and the input port of the DUT, excluding the losses that are common to calibration and the measurement steps for the Y-Factor method, which are specified by the SetYFactorNoiseSourceLoss(string, double[

### SetDutInputLossCompensationEnabled(string, RFmxSpecAnMXNFDutInputLossCompensationEnabled)

Sets whether the noise figure (NF) measurement accounts for ohmic losses between the noise source and the input port of the DUT, excluding the losses that are common to calibration and the measurement steps for the Y-Factor method, which are specified by the [SetYFactorNoiseSourceLoss(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceloss__string-double_arr1.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetDutInputLossCompensationEnabled(string selectorString, RFmxSpecAnMXNFDutInputLossCompensationEnabled value)

#### Remarks

This method sets the value of [NFDutInputLossCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutinputlosscompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXNFDutInputLossCompensationEnabled | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the noise source and the input port of the DUT, excluding the losses that are common to calibration and the measurement steps for the Y-Factor method, which are specified by the SetYFactorNoiseSourceLoss(string, double[]) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosscompensationenabled__string-rfmxspecanmxnfdutoutputlosscompensationenabled.html language=enus -->
## TOPIC 00441: SetDutOutputLossCompensationEnabled(string, RFmxSpecAnMXNFDutOutputLossCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosscompensationenabled__string-rfmxspecanmxnfdutoutputlosscompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosscompensationenabled__string-rfmxspecanmxnfdutoutputlosscompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetDutOutputLossCompensationEnabled(string selectorString, RFmxSpecAnMXNFDutOutputLossCompensat

### SetDutOutputLossCompensationEnabled(string, RFmxSpecAnMXNFDutOutputLossCompensationEnabled)

Sets whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetDutOutputLossCompensationEnabled(string selectorString, RFmxSpecAnMXNFDutOutputLossCompensationEnabled value)

#### Remarks

This method sets the value of [NFDutOutputLossCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutoutputlosscompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXNFDutOutputLossCompensationEnabled | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosstemperature__string-double.html language=enus -->
## TOPIC 00442: SetDutOutputLossTemperature(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosstemperature__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputlosstemperature__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the physical temperature of the ohmic loss elements specified by the SetDutOutputLoss(string, double[]) method. This value is expressed in kelvin. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetDutOutputLossTemperature(string selectorString, double value)RemarksThis method sets

### SetDutOutputLossTemperature(string, double)

Sets the physical temperature of the ohmic loss elements specified by the [SetDutOutputLoss(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setdutoutputloss__string-double_arr1.html) method. This value is expressed in kelvin.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetDutOutputLossTemperature(string selectorString, double value)

#### Remarks

This method sets the value of [NFDutOutputLossTemperature](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 297.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the physical temperature of the ohmic loss elements specified by the SetDutOutputLoss(string, double[]) method. This value is expressed in kelvin. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setduttype__string-rfmxspecanmxnfduttype.html language=enus -->
## TOPIC 00443: SetDutType(string, RFmxSpecAnMXNFDutType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setduttype__string-rfmxspecanmxnfduttype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setduttype__string-rfmxspecanmxnfduttype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of DUT. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetDutType(string selectorString, RFmxSpecAnMXNFDutType value)RemarksThis method sets the value of NFDutType attribute.The default value is Amplifier.ParametersNameTypeDescriptionselectorStringstringPass an empty stri

### SetDutType(string, RFmxSpecAnMXNFDutType)

Sets the type of DUT.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetDutType(string selectorString, RFmxSpecAnMXNFDutType value)

#### Remarks

This method sets the value of [NFDutType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Amplifier](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfduttype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXNFDutType | Specifies the type of DUT. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencyconvertersideband__string-rfmxspecanmxnffrequencyconvertersideband.html language=enus -->
## TOPIC 00444: SetFrequencyConverterSideband(string, RFmxSpecAnMXNFFrequencyConverterSideband)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencyconvertersideband__string-rfmxspecanmxnffrequencyconvertersideband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencyconvertersideband__string-rfmxspecanmxnffrequencyconvertersideband.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sideband when you set the SetDutType(string, RFmxSpecAnMXNFDutType) method to either Downconverter or Upconverter, and the SetFrequencyConverterFrequencyContext(string, RFmxSpecAnMXNFFrequencyConverterFrequencyContext) method to IF. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic i

### SetFrequencyConverterSideband(string, RFmxSpecAnMXNFFrequencyConverterSideband)

Sets the sideband when you set the [SetDutType(string, RFmxSpecAnMXNFDutType)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setduttype__string-rfmxspecanmxnfduttype.html) method to either [Downconverter](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfduttype.html) or [Upconverter](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfduttype.html), and the [SetFrequencyConverterFrequencyContext(string, RFmxSpecAnMXNFFrequencyConverterFrequencyContext)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencyconverterfrequencycontext__string-rfmxspecanmxnffrequencyconverterfrequencycontext.html) method to [IF](nationalinstruments-rfmx-specanmx-rfmxspecanmxnffrequencyconverterfrequencycontext.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFrequencyConverterSideband(string selectorString, RFmxSpecAnMXNFFrequencyConverterSideband value)

#### Remarks

This method sets the value of [NFFrequencyConverterSideband](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Lsb](nationalinstruments-rfmx-specanmx-rfmxspecanmxnffrequencyconvertersideband.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXNFFrequencyConverterSideband | Specifies the sideband when you set the SetDutType(string, RFmxSpecAnMXNFDutType) method to either Downconverter or Upconverter, and the SetFrequencyConverterFrequencyContext(string, RFmxSpecAnMXNFFrequencyConverterFrequencyContext) method to IF. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceofftemperature__string-double.html language=enus -->
## TOPIC 00445: SetYFactorNoiseSourceOffTemperature(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceofftemperature__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setyfactornoisesourceofftemperature__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetYFactorNoiseSourceOffTemperature(string selectorString, double value)RemarksThis metho

### SetYFactorNoiseSourceOffTemperature(string, double)

Sets the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetYFactorNoiseSourceOffTemperature(string selectorString, double value)

#### Remarks

This method sets the value of [NFYFactorNoiseSourceOffTemperature](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 297.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutoutputlosscompensationenabled.html language=enus -->
## TOPIC 00446: RFmxSpecAnMXNFDutOutputLossCompensationEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutoutputlosscompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfdutoutputlosscompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXNFDutOutputLossCompensationEnabledMembersNameValueDescriptionFalse0The NF mea

### RFmxSpecAnMXNFDutOutputLossCompensationEnabled Enumeration

Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFDutOutputLossCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The NF measurement ignores ohmic losses. |
| True | 1 | The NF measurement accounts for the ohmic losses. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfexternalpreamppresent.html language=enus -->
## TOPIC 00447: RFmxSpecAnMXNFExternalPreampPresent Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfexternalpreamppresent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfexternalpreamppresent.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether an external preamplifier is present in the signal path. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXNFExternalPreampPresentMembersNameValueDescriptionFalse0No external preamplifier present in the signal path. True1An external preamplifier present in th

### RFmxSpecAnMXNFExternalPreampPresent Enumeration

Specifies whether an external preamplifier is present in the signal path.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFExternalPreampPresent

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | No external preamplifier present in the signal path. |
| True | 1 | An external preamplifier present in the signal path. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-fetchyfactorpowers__string-double-ref-ref.html language=enus -->
## TOPIC 00448: FetchYFactorPowers(string, double, ref double[], ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-fetchyfactorpowers__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-fetchyfactorpowers__string-double-ref-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the hot and cold powers measured when the Y-Factor based noise figure (NF) measurement is performed.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchYFactorPowers(string selectorString, double timeout, ref double[] hotPower, ref double[] coldPower)ParametersNameTypeDescripti

### FetchYFactorPowers(string, double, ref double[], ref double[])

Fetches the hot and cold powers measured when the Y-Factor based noise figure (NF) measurement is performed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchYFactorPowers(string selectorString, double timeout, ref double[] hotPower, ref double[] coldPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| hotPower | ref double[] | Upon return, contains an array of powers measured at the frequencies specified by the SetFrequencyList(string, double[]) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| coldPower | ref double[] | Upon return, contains an array of powers measured at the frequencies specified by the SetFrequencyList(string, double[]) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-fetchyfactors__string-double-ref-ref.html language=enus -->
## TOPIC 00449: FetchYFactors(string, double, ref double[], ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-fetchyfactors__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-fetchyfactors__string-double-ref-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement Y-factor and calibration Y-factor values.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchYFactors(string selectorString, double timeout, ref double[] measurementYFactor, ref double[] calibrationYFactor)ParametersNameTypeDescriptionselectorStringstringSpecifi

### FetchYFactors(string, double, ref double[], ref double[])

Returns the measurement Y-factor and calibration Y-factor values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchYFactors(string selectorString, double timeout, ref double[] measurementYFactor, ref double[] calibrationYFactor)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementYFactor | ref double[] | Upon return, contains the array of measurement Y-Factor values measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dB. This method returns a valid result only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |
| calibrationYFactor | ref double[] | Upon return, contains the array of calibration Y-Factor values measured at the frequencies specified by the NF Freq List method. This value is expressed in dB. This method returns a valid result only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getcalibrationyfactor__string-ref.html language=enus -->
## TOPIC 00450: GetCalibrationYFactor(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getcalibrationyfactor__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getcalibrationyfactor__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of the calibration Y-Factors measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dB. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. SyntaxNa

### GetCalibrationYFactor(string, ref double[])

Gets an array of the calibration Y-Factors measured at the frequencies specified by the [SetFrequencyList(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencylist__string-double_arr1.html) method. This value is expressed in dB. A valid result is returned only when you set the [SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setmeasurementmethod__string-rfmxspecanmxnfmeasurementmethod.html) method to [YFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCalibrationYFactor(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFResultsCalibrationYFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(string)Â method to build the selectorString. |
| value | ref double[] | Upon return, contains an array of the calibration Y-Factors measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dB. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getcoldsourcepower__string-ref.html language=enus -->
## TOPIC 00451: GetColdSourcePower(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getcoldsourcepower__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getcoldsourcepower__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to Cold-source. SyntaxNamespace: NationalInstru

### GetColdSourcePower(string, ref double[])

Gets the power measured at the frequencies specified by the [SetFrequencyList(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencylist__string-double_arr1.html) method. This value is expressed in dBm. A valid result is returned only when you set the [SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setmeasurementmethod__string-rfmxspecanmxnfmeasurementmethod.html) method to Cold-source.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetColdSourcePower(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFResultsColdSourcePower](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(string)Â method to build the selectorString. |
| value | ref double[] | Upon return, contains the power measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to Cold-source. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getdutnoisefigure__string-ref.html language=enus -->
## TOPIC 00452: GetDutNoiseFigure(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getdutnoisefigure__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getdutnoisefigure__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of the noise figures of the DUT measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetDutNoiseFigure(string selectorString, ref double[] value)RemarksThis me

### GetDutNoiseFigure(string, ref double[])

Gets an array of the noise figures of the DUT measured at the frequencies specified by the [SetFrequencyList(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencylist__string-double_arr1.html) method. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDutNoiseFigure(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFResultsDutNoiseFigure](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(string)Â method to build the selectorString. |
| value | ref double[] | Upon return, contains an array of the noise figures of the DUT measured at the frequencies specified by the SetFrequencyList(string, double[]) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getyfactorcoldpower__string-ref.html language=enus -->
## TOPIC 00453: GetYFactorColdPower(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getyfactorcoldpower__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getyfactorcoldpower__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of powers measured at the frequencies specified by the SetFrequencyList(string, double[]) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to

### GetYFactorColdPower(string, ref double[])

Gets the array of powers measured at the frequencies specified by the [SetFrequencyList(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencylist__string-double_arr1.html) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the [SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setmeasurementmethod__string-rfmxspecanmxnfmeasurementmethod.html) method to [YFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetYFactorColdPower(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFResultsYFactorColdPower](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(string)Â method to build the selectorString. |
| value | ref double[] | Upon return, contains the array of powers measured at the frequencies specified by the SetFrequencyList(string, double[]) method, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getyfactorhotpower__string-ref.html language=enus -->
## TOPIC 00454: GetYFactorHotPower(string, ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getyfactorhotpower__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfresults-getyfactorhotpower__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of powers measured at the frequencies specified by the SetFrequencyList(string, double[]) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to

### GetYFactorHotPower(string, ref double[])

Gets the array of powers measured at the frequencies specified by the [SetFrequencyList(string, double[])](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setfrequencylist__string-double_arr1.html) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the [SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setmeasurementmethod__string-rfmxspecanmxnfmeasurementmethod.html) method to [YFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetYFactorHotPower(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [NFResultsYFactorHotPower](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use theÂ BuildResultString(string)Â method to build the selectorString. |
| value | ref double[] | Upon return, contains the array of powers measured at the frequencies specified by the SetFrequencyList(string, double[]) method, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXNFResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactormode.html language=enus -->
## TOPIC 00455: RFmxSpecAnMXNFYFactorMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactormode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactormode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod) method to YFactor. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum

### RFmxSpecAnMXNFYFactorMode Enumeration

Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the [SetMeasurementMethod(string, RFmxSpecAnMXNFMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfconfiguration-setmeasurementmethod__string-rfmxspecanmxnfmeasurementmethod.html) method to [YFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxnfmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFYFactorMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Measure | 0 | The noise figure (NF) measurement computes the noise characteristics of the DUT, compensating for the noise figure of the analyzer. |
| Calibrate | 1 | The NF measurement computes the noise characteristics of the analyzer. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactornoisesourcelosscompensationenabled.html language=enus -->
## TOPIC 00456: RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactornoisesourcelosscompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxnfyfactornoisesourcelosscompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXNFYFactorNoiseSourceLossCompensation

### RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled Enumeration

Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Ohmic losses are ignored. |
| True | 1 | Ohmic losses are accounted for in the NF measurement. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configureaveraging__string-rfmxspecanmxobwaveragingenabled-int-rfmxspecanmxobwaveragingtype.html language=enus -->
## TOPIC 00457: ConfigureAveraging(string, RFmxSpecAnMXObwAveragingEnabled, int, RFmxSpecAnMXObwAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configureaveraging__string-rfmxspecanmxobwaveragingenabled-int-rfmxspecanmxobwaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configureaveraging__string-rfmxspecanmxobwaveragingenabled-int-rfmxspecanmxobwaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the occupied bandwidth (OBW) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureAveraging(string selectorString, RFmxSpecAnMXObwAveragingEnabled averagingEnabled, int averagingCount, RFmxSpecAnMXObwAveragingType averagingType)RemarksThis metho

### ConfigureAveraging(string, RFmxSpecAnMXObwAveragingEnabled, int, RFmxSpecAnMXObwAveragingType)

Configures averaging for the occupied bandwidth (OBW) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureAveraging(string selectorString, RFmxSpecAnMXObwAveragingEnabled averagingEnabled, int averagingCount, RFmxSpecAnMXObwAveragingType averagingType)

#### Remarks

This method maps to the RFmxSpecAn_OBWCfgAveraging() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxSpecAnMXObwAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXObwAveragingEnabled) method to True. |
| averagingType | RFmxSpecAnMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configurefft__string-rfmxspecanmxobwfftwindow-double.html language=enus -->
## TOPIC 00458: ConfigureFft(string, RFmxSpecAnMXObwFftWindow, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configurefft__string-rfmxspecanmxobwfftwindow-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configurefft__string-rfmxspecanmxobwfftwindow-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureFft(string selectorString, RFmxSpecAnMXObwFftWindow fftWindow, double fftPadding)RemarksThis method maps to the RFmxSpecAn_OBWCfgFFT() fu

### ConfigureFft(string, RFmxSpecAnMXObwFftWindow, double)

Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureFft(string selectorString, RFmxSpecAnMXObwFftWindow fftWindow, double fftPadding)

#### Remarks

This method maps to the RFmxSpecAn_OBWCfgFFT() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| fftWindow | RFmxSpecAnMXObwFftWindow | Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types. |
| fftPadding | double | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configurespan__string-double.html language=enus -->
## TOPIC 00459: ConfigureSpan(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configurespan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-configurespan__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSpan(string selectorString, double span)RemarksThis method maps to the RFmxSpecAn_OBWCfgSpan() function in C.ParametersNam

### ConfigureSpan(string, double)

Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSpan(string selectorString, double span)

#### Remarks

This method maps to the RFmxSpecAn_OBWCfgSpan() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| span | double | Specifies the frequency range, in Hz, around the center frequency, to acquire for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00460: GetAmplitudeCorrectionType(string, out RFmxSpecAnMXObwAmplitudeCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxobwconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Natio

### GetAmplitudeCorrectionType(string, out RFmxSpecAnMXObwAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxSpecAnMXObwAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [ObwAmplitudeCorrectionType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxobwamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXObwAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuremeasurementintervalmode__string-rfmxspecanmxpavtmeasurementintervalmode.html language=enus -->
## TOPIC 00461: ConfigureMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuremeasurementintervalmode__string-rfmxspecanmxpavtmeasurementintervalmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuremeasurementintervalmode__string-rfmxspecanmxpavtmeasurementintervalmode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement interval mode.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureMeasurementIntervalMode(string selectorString, RFmxSpecAnMXPavtMeasurementIntervalMode measurementIntervalMode)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The sig

### ConfigureMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode)

Configures the measurement interval mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureMeasurementIntervalMode(string selectorString, RFmxSpecAnMXPavtMeasurementIntervalMode measurementIntervalMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementIntervalMode | RFmxSpecAnMXPavtMeasurementIntervalMode | Specifies the mode of configuring the measurement interval. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuresegmentstarttimestep__string-int-double-double.html language=enus -->
## TOPIC 00462: ConfigureSegmentStartTimeStep(string, int, double, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuresegmentstarttimestep__string-int-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuresegmentstarttimestep__string-int-double-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list of the segment start times based on segment0StartTime and segmentInterval. This method is used when the segments to be measured have equal duration.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSegmentStartTimeStep(string selectorString, int numberOfSegmen

### ConfigureSegmentStartTimeStep(string, int, double, double)

Configures the list of the segment start times based on *segment0StartTime* and *segmentInterval*. This method is used when the segments to be measured have equal duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSegmentStartTimeStep(string selectorString, int numberOfSegments, double segment0StartTime, double segmentInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfSegments | int | Specifies the number of segments to be measured. |
| segment0StartTime | double | Specifies the start time for segment0. This value is expressed in seconds. |
| segmentInterval | double | Specifies the difference in the start times between consecutive segments. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuresegmenttype__string-rfmxspecanmxpavtsegmenttype.html language=enus -->
## TOPIC 00463: ConfigureSegmentType(string, RFmxSpecAnMXPavtSegmentType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuresegmenttype__string-rfmxspecanmxpavtsegmenttype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-configuresegmenttype__string-rfmxspecanmxpavtsegmenttype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the segment type.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSegmentType(string selectorString, RFmxSpecAnMXPavtSegmentType segmentType)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of segment number. Example: "segment0"

### ConfigureSegmentType(string, RFmxSpecAnMXPavtSegmentType)

Configures the segment type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSegmentType(string selectorString, RFmxSpecAnMXPavtSegmentType segmentType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of segment number. Example:"segment0" You can use the BuildSegmentString(string, int) method to build the selector string. |
| segmentType | RFmxSpecAnMXPavtSegmentType | Specifies the type of segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getfrequencyoffsetcorrectionenabled__string-out.html language=enus -->
## TOPIC 00464: GetFrequencyOffsetCorrectionEnabled(string, out RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getfrequencyoffsetcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getfrequencyoffsetcorrectionenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable frequency offset correction for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFrequencyOffsetCorrectionEnabled(string selectorString, out RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled value)RemarksThis method gets the value of PavtFrequenc

### GetFrequencyOffsetCorrectionEnabled(string, out RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled)

Gets whether to enable frequency offset correction for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFrequencyOffsetCorrectionEnabled(string selectorString, out RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled value)

#### Remarks

This method gets the value of [PavtFrequencyOffsetCorrectionEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtfrequencyoffsetcorrectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled | Upon return, contains whether to enable frequency offset correction for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getfrequencytrackingenabled__string-out.html language=enus -->
## TOPIC 00465: GetFrequencyTrackingEnabled(string, out RFmxSpecAnMXPavtFrequencyTrackingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getfrequencytrackingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getfrequencytrackingenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable frequency offset correction per segment for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFrequencyTrackingEnabled(string selectorString, out RFmxSpecAnMXPavtFrequencyTrackingEnabled value)RemarksThis method gets the value of PavtFrequencyTra

### GetFrequencyTrackingEnabled(string, out RFmxSpecAnMXPavtFrequencyTrackingEnabled)

Gets whether to enable frequency offset correction per segment for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFrequencyTrackingEnabled(string selectorString, out RFmxSpecAnMXPavtFrequencyTrackingEnabled value)

#### Remarks

This method gets the value of [PavtFrequencyTrackingEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtfrequencytrackingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXPavtFrequencyTrackingEnabled | Upon return, contains whether to enable frequency offset correction for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getmeasurementbandwidth__string-out.html language=enus -->
## TOPIC 00466: GetMeasurementBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getmeasurementbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getmeasurementbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth over which the signal is measured. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementBandwidth(string selectorString, out double value)RemarksThis method gets the value of PavtMeasurementBandwidth attribute.The default value

### GetMeasurementBandwidth(string, out double)

Gets the bandwidth over which the signal is measured. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PavtMeasurementBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth over which the signal is measured. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentmeasurementlength__string-out.html language=enus -->
## TOPIC 00467: GetSegmentMeasurementLength(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentmeasurementlength__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable. Synta

### GetSegmentMeasurementLength(string, out double)

Gets the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the [SetMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementintervalmode__string-rfmxspecanmxpavtmeasurementintervalmode.html) method to [Variable](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtmeasurementintervalmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSegmentMeasurementLength(string selectorString, out double value)

#### Remarks

This method gets the value of [PavtSegmentMeasurementLength](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1 millisecond.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This method is valid when you set the SetMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentmeasurementoffset__string-out.html language=enus -->
## TOPIC 00468: GetSegmentMeasurementOffset(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentmeasurementoffset__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the SetMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode) method

### GetSegmentMeasurementOffset(string, out double)

Gets the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the [SetMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementintervalmode__string-rfmxspecanmxpavtmeasurementintervalmode.html) method to [Variable](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtmeasurementintervalmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSegmentMeasurementOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [PavtSegmentMeasurementOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the SetMeasurementIntervalMode(string, RFmxSpecAnMXPavtMeasurementIntervalMode) method to Variable. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentstarttime__string-out.html language=enus -->
## TOPIC 00469: GetSegmentStartTime(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentstarttime__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmentstarttime__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(string, RFmxSpecAnMXPavtMeasurementLocationType) method to Time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSegmentSta

### GetSegmentStartTime(string, out double)

Gets the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the [SetMeasurementLocationType(string, RFmxSpecAnMXPavtMeasurementLocationType)](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementlocationtype__string-rfmxspecanmxpavtmeasurementlocationtype.html) method to [Time](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtmeasurementlocationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSegmentStartTime(string selectorString, out double value)

#### Remarks

This method gets the value of [PavtSegmentStartTime](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(string, RFmxSpecAnMXPavtMeasurementLocationType) method to Time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmenttype__string-out.html language=enus -->
## TOPIC 00470: GetSegmentType(string, out RFmxSpecAnMXPavtSegmentType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmenttype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-getsegmenttype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSegmentType(string selectorString, out RFmxSpecAnMXPavtSegmentType value)RemarksThis method gets the value of PavtSegmentType attribute.The default value is PhaseAndAmplitude.ParametersNameTypeDescriptionselect

### GetSegmentType(string, out RFmxSpecAnMXPavtSegmentType)

Gets the type of segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSegmentType(string selectorString, out RFmxSpecAnMXPavtSegmentType value)

#### Remarks

This method gets the value of [PavtSegmentType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [PhaseAndAmplitude](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtsegmenttype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXPavtSegmentType | Upon return, contains the type of segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementbandwidth__string-double.html language=enus -->
## TOPIC 00471: SetMeasurementBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth over which the signal is measured. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementBandwidth(string selectorString, double value)RemarksThis method sets the value of PavtMeasurementBandwidth attribute.The default value is 1

### SetMeasurementBandwidth(string, double)

Sets the bandwidth over which the signal is measured. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [PavtMeasurementBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth over which the signal is measured. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setphaseunwrapenabled__string-rfmxspecanmxpavtphaseunwrapenabled.html language=enus -->
## TOPIC 00472: SetPhaseUnwrapEnabled(string, RFmxSpecAnMXPavtPhaseUnwrapEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setphaseunwrapenabled__string-rfmxspecanmxpavtphaseunwrapenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setphaseunwrapenabled__string-rfmxspecanmxpavtphaseunwrapenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the phase measurement results are unwrapped or wrapped. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetPhaseUnwrapEnabled(string selectorString, RFmxSpecAnMXPavtPhaseUnwrapEnabled value)RemarksThis method sets the value of PavtPhaseUnwrapEnabled attribute.The default va

### SetPhaseUnwrapEnabled(string, RFmxSpecAnMXPavtPhaseUnwrapEnabled)

Sets whether the phase measurement results are unwrapped or wrapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetPhaseUnwrapEnabled(string selectorString, RFmxSpecAnMXPavtPhaseUnwrapEnabled value)

#### Remarks

This method sets the value of [PavtPhaseUnwrapEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtphaseunwrapenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXPavtPhaseUnwrapEnabled | Specifies whether the phase measurement results are unwrapped or wrapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setsegmentstarttime__string-double.html language=enus -->
## TOPIC 00473: SetSegmentStartTime(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setsegmentstarttime__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setsegmentstarttime__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(string, RFmxSpecAnMXPavtMeasurementLocationType) method to Time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSegmentSta

### SetSegmentStartTime(string, double)

Sets the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the [SetMeasurementLocationType(string, RFmxSpecAnMXPavtMeasurementLocationType)](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setmeasurementlocationtype__string-rfmxspecanmxpavtmeasurementlocationtype.html) method to [Time](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtmeasurementlocationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSegmentStartTime(string selectorString, double value)

#### Remarks

This method sets the value of [PavtSegmentStartTime](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the start time of measurement of the segments. This value is expressed in seconds. You can use this method only when you set the SetMeasurementLocationType(string, RFmxSpecAnMXPavtMeasurementLocationType) method to Time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setsegmenttype__string-rfmxspecanmxpavtsegmenttype.html language=enus -->
## TOPIC 00474: SetSegmentType(string, RFmxSpecAnMXPavtSegmentType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setsegmenttype__string-rfmxspecanmxpavtsegmenttype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtconfiguration-setsegmenttype__string-rfmxspecanmxpavtsegmenttype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSegmentType(string selectorString, RFmxSpecAnMXPavtSegmentType value)RemarksThis method sets the value of PavtSegmentType attribute.The default value is PhaseAndAmplitude.ParametersNameTypeDescriptionselectorSt

### SetSegmentType(string, RFmxSpecAnMXPavtSegmentType)

Sets the type of segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSegmentType(string selectorString, RFmxSpecAnMXPavtSegmentType value)

#### Remarks

This method sets the value of [PavtSegmentType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [PhaseAndAmplitude](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtsegmenttype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | RFmxSpecAnMXPavtSegmentType | Specifies the type of segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtphaseunwrapenabled.html language=enus -->
## TOPIC 00475: RFmxSpecAnMXPavtPhaseUnwrapEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtphaseunwrapenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtphaseunwrapenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the phase measurement results are unwrapped or wrapped. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXPavtPhaseUnwrapEnabledMembersNameValueDescriptionFalse0Phase measurement results are wrapped within +/-180 degrees. True1Phase measurement results are u

### RFmxSpecAnMXPavtPhaseUnwrapEnabled Enumeration

Specifies whether the phase measurement results are unwrapped or wrapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXPavtPhaseUnwrapEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Phase measurement results are wrapped within +/-180 degrees. |
| True | 1 | Phase measurement results are unwrapped. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtresults-getmeanabsolutephase__string-out.html language=enus -->
## TOPIC 00476: GetMeanAbsolutePhase(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtresults-getmeanabsolutephase__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtresults-getmeanabsolutephase__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean absolute phase of the segment. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeanAbsolutePhase(string selectorString, out double value)RemarksThis method gets the value of PavtResultsMeanAbsolutePhase attribute.ParametersNameTypeDes

### GetMeanAbsolutePhase(string, out double)

Gets the mean absolute phase of the segment. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanAbsolutePhase(string selectorString, out double value)

#### Remarks

This method gets the value of [PavtResultsMeanAbsolutePhase](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and PavtSegment number. Example: "segment0", "result::r1/segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean absolute phase of the segment. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtresults-getmeanrelativephase__string-out.html language=enus -->
## TOPIC 00477: GetMeanRelativePhase(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtresults-getmeanrelativephase__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxpavtresults-getmeanrelativephase__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeanRelativePhase(string selectorString, out double value)RemarksThis method gets the value of PavtResultsMeanRelat

### GetMeanRelativePhase(string, out double)

Gets the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanRelativePhase(string selectorString, out double value)

#### Remarks

This method gets the value of [PavtResultsMeanRelativePhase](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and PavtSegment number. Example: "segment0", "result::r1/segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPavtResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationfrequency__string-ref.html language=enus -->
## TOPIC 00478: GetCancellationFrequency(string, ref float[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationfrequency__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of frequency offsets where the reference phase noise has been measured. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCancellationFrequency(string selectorString, ref float[] value)RemarksThis method gets the value of PhaseNoiseCancellationFrequency attribute.Paramete

### GetCancellationFrequency(string, ref float[])

Gets an array of frequency offsets where the reference phase noise has been measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCancellationFrequency(string selectorString, ref float[] value)

#### Remarks

This method gets the value of [PhaseNoiseCancellationFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref float[] | Upon return, contains an array of frequencies where the reference phase noise has been measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPhaseNoiseConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationreferencephasenoise__string-ref.html language=enus -->
## TOPIC 00479: GetCancellationReferencePhaseNoise(string, ref float[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationreferencephasenoise__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationreferencephasenoise__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of reference phase noise at the frequency offsets. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCancellationReferencePhaseNoise(string selectorString, ref float[] value)RemarksThis method gets the value of PhaseNoiseCancellationReferencePhaseNoise attribute.Parameter

### GetCancellationReferencePhaseNoise(string, ref float[])

Gets an array of reference phase noise at the frequency offsets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCancellationReferencePhaseNoise(string selectorString, ref float[] value)

#### Remarks

This method gets the value of [PhaseNoiseCancellationReferencePhaseNoise](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref float[] | Upon return, contains an array of reference phase noise at the frequencies specified by the Phase Noise Cancellation Frequency method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPhaseNoiseConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationthreshold__string-out.html language=enus -->
## TOPIC 00480: GetCancellationThreshold(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationthreshold__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoiseconfiguration-getcancellationthreshold__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCancellationThreshold(string selectorString, out double value)RemarksThis method gets the value of PhaseNois

### GetCancellationThreshold(string, out double)

Gets the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCancellationThreshold(string selectorString, out double value)

#### Remarks

This method gets the value of [PhaseNoiseCancellationThreshold](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.01.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXPhaseNoiseConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsem-configuration.html language=enus -->
## TOPIC 00481: Configuration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsem-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsem-configuration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXSemConfiguration instance that allows configuration of spectral emission mask (SEM) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXSemConfiguration Configuration { get; }RemarksReturns an object of type RFmxSpecAnMXSemConfiguration

### Configuration

Gets the [RFmxSpecAnMXSemConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration.html) instance that allows configuration of spectral emission mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXSemConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration.html) Configuration { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXSemConfiguration

Parent topic:

RFmxSpecAnMXSem Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemaveragingtype.html language=enus -->
## TOPIC 00482: RFmxSpecAnMXSemAveragingType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectral emission mask (SEM) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXSemAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linear

### RFmxSpecAnMXSemAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectral emission mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXSemAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithm scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierenabled__string-rfmxspecanmxsemcarrierenabled.html language=enus -->
## TOPIC 00483: ConfigureCarrierEnabled(string, RFmxSpecAnMXSemCarrierEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierenabled__string-rfmxspecanmxsemcarrierenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierenabled__string-rfmxspecanmxsemcarrierenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to consider the carrier power as part of total carrier power measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureCarrierEnabled(string selectorString, RFmxSpecAnMXSemCarrierEnabled carrierEnabled)RemarksThis method maps to the RFmxSpecAn_SEMCfgCarrie

### ConfigureCarrierEnabled(string, RFmxSpecAnMXSemCarrierEnabled)

Configures whether to consider the carrier power as part of total carrier power measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureCarrierEnabled(string selectorString, RFmxSpecAnMXSemCarrierEnabled carrierEnabled)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| carrierEnabled | RFmxSpecAnMXSemCarrierEnabled | Specifies whether to consider the carrier power as part of total carrier power measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierfrequency__string-double.html language=enus -->
## TOPIC 00484: ConfigureCarrierFrequency(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierfrequency__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureCarrierFrequency(string selectorString, double carrierFrequency)RemarksThis method maps to the RFmxSpecAn_SEMCfgCarrierFrequency(

### ConfigureCarrierFrequency(string, double)

Configures the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureCarrierFrequency(string selectorString, double carrierFrequency)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| carrierFrequency | double | Specifies the center frequency, in Hz, of the carrier, relative to the RF center frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierintegrationbandwidth__string-double.html language=enus -->
## TOPIC 00485: ConfigureCarrierIntegrationBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierintegrationbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurecarrierintegrationbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureCarrierIntegrationBandwidth(string selectorString, double integrationBandwidth)RemarksThis method maps to the RFmxSpec

### ConfigureCarrierIntegrationBandwidth(string, double)

Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureCarrierIntegrationBandwidth(string selectorString, double integrationBandwidth)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgCarrierIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| integrationBandwidth | double | Specifies the frequency range, in Hz, over which the measurement integrates the carrier channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetfrequency__string-double-double-rfmxspecanmxsemoffsetenabled-rfmxspecanmxsemoffsetsideband.html language=enus -->
## TOPIC 00486: ConfigureOffsetFrequency(string, double, double, RFmxSpecAnMXSemOffsetEnabled, RFmxSpecAnMXSemOffsetSideband)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetfrequency__string-double-double-rfmxspecanmxsemoffsetenabled-rfmxspecanmxsemoffsetsideband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetfrequency__string-double-double-rfmxspecanmxsemoffsetenabled-rfmxspecanmxsemoffsetsideband.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureOffsetFrequency(string selectorString, double offsetStartFrequency, double of

### ConfigureOffsetFrequency(string, double, double, RFmxSpecAnMXSemOffsetEnabled, RFmxSpecAnMXSemOffsetSideband)

Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureOffsetFrequency(string selectorString, double offsetStartFrequency, double offsetStopFrequency, RFmxSpecAnMXSemOffsetEnabled offsetEnabled, RFmxSpecAnMXSemOffsetSideband offsetSideband)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| offsetStartFrequency | double | Specifies the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the SetOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefinition) method. |
| offsetStopFrequency | double | Specifies the stop frequency, in Hz, of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the SetOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefinition) method. |
| offsetEnabled | RFmxSpecAnMXSemOffsetEnabled | Specifies whether to enable the offset segment for the SEM measurement. |
| offsetSideband | RFmxSpecAnMXSemOffsetSideband | Specifies whether the offset segment is present on one side, or on both sides of the carriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetfrequencydefinition__string-rfmxspecanmxsemoffsetfrequencydefinition.html language=enus -->
## TOPIC 00487: ConfigureOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetfrequencydefinition__string-rfmxspecanmxsemoffsetfrequencydefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetfrequencydefinition__string-rfmxspecanmxsemoffsetfrequencydefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset frequency definition for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureOffsetFrequencyDefinition(string selectorString, RFmxSpecAnMXSemOffsetFrequencyDefinition offsetFrequencyDefinition)RemarksThis method maps to the RFmxSpecAn_SEMC

### ConfigureOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefinition)

Configures the offset frequency definition for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureOffsetFrequencyDefinition(string selectorString, RFmxSpecAnMXSemOffsetFrequencyDefinition offsetFrequencyDefinition)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetFrequencyDefinition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| offsetFrequencyDefinition | RFmxSpecAnMXSemOffsetFrequencyDefinition | Specifies the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetlimitfailmask__string-rfmxspecanmxsemoffsetlimitfailmask.html language=enus -->
## TOPIC 00488: ConfigureOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetlimitfailmask__string-rfmxspecanmxsemoffsetlimitfailmask.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetlimitfailmask__string-rfmxspecanmxsemoffsetlimitfailmask.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the criteria to determine the measurement fail status. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureOffsetLimitFailMask(string selectorString, RFmxSpecAnMXSemOffsetLimitFailMask limitFailMask)RemarksThis method maps to the RFmxSpecAn_SEMCfgOffsetLimitFailMask() fu

### ConfigureOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask)

Configures the criteria to determine the measurement fail status.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureOffsetLimitFailMask(string selectorString, RFmxSpecAnMXSemOffsetLimitFailMask limitFailMask)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetLimitFailMask() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| limitFailMask | RFmxSpecAnMXSemOffsetLimitFailMask | Specifies the criteria to determine the measurement fail status. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrbwfilter__string-rfmxspecanmxsemoffsetrbwautobandwidth-double-rfmxspecanmxsemoffsetrbwfiltertype.html language=enus -->
## TOPIC 00489: ConfigureOffsetRbwFilter(string, RFmxSpecAnMXSemOffsetRbwAutoBandwidth, double, RFmxSpecAnMXSemOffsetRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrbwfilter__string-rfmxspecanmxsemoffsetrbwautobandwidth-double-rfmxspecanmxsemoffsetrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrbwfilter__string-rfmxspecanmxsemoffsetrbwautobandwidth-double-rfmxspecanmxsemoffsetrbwfiltertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter of the offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureOffsetRbwFilter(string selectorString, RFmxSpecAnMXSemOffsetRbwAutoBandwidth rbwAuto, double rbw, RFmxSpecAnMXSemOffsetRbwFilterType rbwFilterType)RemarksThis

### ConfigureOffsetRbwFilter(string, RFmxSpecAnMXSemOffsetRbwAutoBandwidth, double, RFmxSpecAnMXSemOffsetRbwFilterType)

Configures the resolution bandwidth (RBW) filter of the offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureOffsetRbwFilter(string selectorString, RFmxSpecAnMXSemOffsetRbwAutoBandwidth rbwAuto, double rbw, RFmxSpecAnMXSemOffsetRbwFilterType rbwFilterType)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetRBWFilter() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| rbwAuto | RFmxSpecAnMXSemOffsetRbwAutoBandwidth | Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the SEM topic for more details on RBW and sweep time. |
| rbw | double | Specifies the bandwidth, in hertz (Hz), of the RBW filter used to sweep the acquired offset segment, when you set the rbwAuto parameter to False. |
| rbwFilterType | RFmxSpecAnMXSemOffsetRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrelativeattenuation__string-double.html language=enus -->
## TOPIC 00490: ConfigureOffsetRelativeAttenuation(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrelativeattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrelativeattenuation__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the attenuation, in dB, relative to the external attenuation. Use this method to compensate for variations in external attenuation when the offset channels are spread wide in frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureOffsetRelativeAttenuation(string

### ConfigureOffsetRelativeAttenuation(string, double)

Configures the attenuation, in dB, relative to the external attenuation. Use this method to compensate for variations in external attenuation when the offset channels are spread wide in frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureOffsetRelativeAttenuation(string selectorString, double relativeAttenuation)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetRelativeAttenuation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| relativeAttenuation | double | Specifies the attenuation, in dB, relative to the external attenuation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrelativelimit__string-rfmxspecanmxsemoffsetrelativelimitmode-double-double.html language=enus -->
## TOPIC 00491: ConfigureOffsetRelativeLimit(string, RFmxSpecAnMXSemOffsetRelativeLimitMode, double, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrelativelimit__string-rfmxspecanmxsemoffsetrelativelimitmode-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configureoffsetrelativelimit__string-rfmxspecanmxsemoffsetrelativelimitmode-double-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureOffsetRelativeLimit(string selectorString, RFmxSpecAnMXSemOffsetRelativeLimitMode relativeLim

### ConfigureOffsetRelativeLimit(string, RFmxSpecAnMXSemOffsetRelativeLimitMode, double, double)

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureOffsetRelativeLimit(string selectorString, RFmxSpecAnMXSemOffsetRelativeLimitMode relativeLimitMode, double relativeLimitStart, double relativeLimitStop)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgOffsetRelativeLimit() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| relativeLimitMode | RFmxSpecAnMXSemOffsetRelativeLimitMode | Specifies whether the relative limit mask is a flat line or a line with a slope. |
| relativeLimitStart | double | Specifies the relative power limit, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the relativeLimitMode parameter to Couple. |
| relativeLimitStop | double | Specifies the relative power limit, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the relativeLimitMode parameter to Couple. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurepowerunits__string-rfmxspecanmxsempowerunits.html language=enus -->
## TOPIC 00492: ConfigurePowerUnits(string, RFmxSpecAnMXSemPowerUnits)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurepowerunits__string-rfmxspecanmxsempowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurepowerunits__string-rfmxspecanmxsempowerunits.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the units for the absolute power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigurePowerUnits(string selectorString, RFmxSpecAnMXSemPowerUnits powerUnits)RemarksThis method maps to the RFmxSpecAn_SEMCfgPowerUnits() function in C.ParametersNameTypeDescriptionselectorSt

### ConfigurePowerUnits(string, RFmxSpecAnMXSemPowerUnits)

Configures the units for the absolute power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigurePowerUnits(string selectorString, RFmxSpecAnMXSemPowerUnits powerUnits)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgPowerUnits() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| powerUnits | RFmxSpecAnMXSemPowerUnits | Specifies the units for the absolute power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurereferencetype__string-rfmxspecanmxsemreferencetype.html language=enus -->
## TOPIC 00493: ConfigureReferenceType(string, RFmxSpecAnMXSemReferenceType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurereferencetype__string-rfmxspecanmxsemreferencetype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configurereferencetype__string-rfmxspecanmxsemreferencetype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the power reference is the integrated power or the peak power in the closest carrier channel. The leftmost carrier is the carrier closest to all the lower (negative) offset segments. The rightmost carrier offset is the carrier closest to all the upper (positive) offset segments. S

### ConfigureReferenceType(string, RFmxSpecAnMXSemReferenceType)

Configures whether the power reference is the integrated power or the peak power in the closest carrier channel. The leftmost carrier is the carrier closest to all the lower (negative) offset segments. The rightmost carrier offset is the carrier closest to all the upper (positive) offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureReferenceType(string selectorString, RFmxSpecAnMXSemReferenceType referenceType)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgReferenceType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceType | RFmxSpecAnMXSemReferenceType | Specifies whether the power reference is the integrated power or the peak power in the closest carrier channel. The leftmost carrier is the carrier closest to all the lower (negative) offset segments. The rightmost carrier offset is the carrier closest to all the upper (positive) offset segments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configuresweeptime__string-rfmxspecanmxsemsweeptimeauto-double.html language=enus -->
## TOPIC 00494: ConfigureSweepTime(string, RFmxSpecAnMXSemSweepTimeAuto, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configuresweeptime__string-rfmxspecanmxsemsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-configuresweeptime__string-rfmxspecanmxsemsweeptimeauto-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSweepTime(string selectorString, RFmxSpecAnMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)RemarksThis method maps to the RFmxSpecAn_SEMCfgSweepTime() function in C.ParametersNameTypeDescripti

### ConfigureSweepTime(string, RFmxSpecAnMXSemSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSweepTime(string selectorString, RFmxSpecAnMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Remarks

This method maps to the RFmxSpecAn_SEMCfgSweepTime() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxSpecAnMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXSemSweepTimeAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00495: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets if the traces to be stored and retrieved after performing the spectral emission mask (SEM) measurement are enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_SEMGetAllTracesEna

### GetAllTracesEnabled(string, out bool)

Gets if the traces to be stored and retrieved after performing the spectral emission mask (SEM) measurement are enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if traces to be stored and retrieved after performing the SEM measurement are enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierchannelbandwidth__string-out.html language=enus -->
## TOPIC 00496: GetCarrierChannelBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierchannelbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierchannelbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel bandwidth, in hertz (Hz), of the carrier. The channel bandwidth is used to calculate the values of the SetOffsetStartFrequency(string, double) and SetOffsetStopFrequency(string, double) methods when you set the SetOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefin

### GetCarrierChannelBandwidth(string, out double)

Gets the channel bandwidth, in hertz (Hz), of the carrier. The channel bandwidth is used to calculate the values of the [SetOffsetStartFrequency(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-setoffsetstartfrequency__string-double.html) and [SetOffsetStopFrequency(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-setoffsetstopfrequency__string-double.html) methods when you set the [SetOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefinition)](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-setoffsetfrequencydefinition__string-rfmxspecanmxsemoffsetfrequencydefinition.html) method to [CarrierEdgeToMeasurementBandwidthCenter](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemoffsetfrequencydefinition.html) or [CarrierEdgeToMeasurementBandwidthEdge](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemoffsetfrequencydefinition.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierChannelBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierChannelBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the channel bandwidth, in hertz (Hz), of the carrier. The channel bandwidth is used to calculate the values of the SetOffsetStartFrequency(string, double) and SetOffsetStopFrequency(string, double) methods when you set the SetOffsetFrequencyDefinition(string, RFmxSpecAnMXSemOffsetFrequencyDefinition) method to CarrierEdgeToMeasurementBandwidthCenter or CarrierEdgeToMeasurementBandwidthEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00497: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetCarrierIntegra

### GetCarrierIntegrationBandwidth(string, out double)

Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency range, in Hz, over which the measurement integrates the carrier channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00498: GetCarrierRbwFilterAutoBandwidth(string, out RFmxSpecAnMXSemCarrierRbwAutoBandwidth)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterautobandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the resolution bandwidth (RBW) of the carrier. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierRbwFilterAutoBandwidth(string selectorString, out RFmxSpecAnMXSemCarrierRbwAutoBandwidth value)RemarksThis method maps to the RFmxSpecAn_SEMGetC

### GetCarrierRbwFilterAutoBandwidth(string, out RFmxSpecAnMXSemCarrierRbwAutoBandwidth)

Gets whether the measurement computes the resolution bandwidth (RBW) of the carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierRbwFilterAutoBandwidth(string selectorString, out RFmxSpecAnMXSemCarrierRbwAutoBandwidth value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierRBWFilterAutoBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXSemCarrierRbwAutoBandwidth | Upon return, indicates whether the measurement computes the RBW of the carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00499: GetCarrierRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierRbwFilterBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetCar

### GetCarrierRbwFilterBandwidth(string, out double)

Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the bandwidth, in Hz, of the RBW filter used to sweep the acquired carrier signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterbandwidthdefinition__string-out.html language=enus -->
## TOPIC 00500: GetCarrierRbwFilterBandwidthDefinition(string, out RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterbandwidthdefinition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-getcarrierrbwfilterbandwidthdefinition__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth definition which you use to specify the value of the SetCarrierRbwFilterBandwidth(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierRbwFilterBandwidthDefinition(string selectorString, out RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefiniti

### GetCarrierRbwFilterBandwidthDefinition(string, out RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition)

Gets the bandwidth definition which you use to specify the value of the [SetCarrierRbwFilterBandwidth(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-setcarrierrbwfilterbandwidth__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierRbwFilterBandwidthDefinition(string selectorString, out RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetCarrierRBWFilterBandwidthDefinition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition | Specifies the bandwidth definition which you use to specify the value of the SetCarrierRbwFilterBandwidth(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemConfiguration Class
