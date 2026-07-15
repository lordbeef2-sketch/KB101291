# NI DOCUMENT BUNDLE: rfmxspecan-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-dotnet-api-ref start=501 end=524 -->
<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemoffsetrbwfilterbandwidthdefinition.html language=enus -->
## TOPIC 00501: RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemoffsetrbwfilterbandwidthdefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemoffsetrbwfilterbandwidthdefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the resolution bandwidth (RBW). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinitionMembersNameValueDescriptionBandwidthDefinition3dB0Defines the RBW in terms of the 3dB bandwidth of the RBW filter.

### RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition Enumeration

Specifies whether the measurement computes the resolution bandwidth (RBW).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition

#### Members

| Name | Value | Description |
| --- | --- | --- |
| BandwidthDefinition3dB | 0 | Defines the RBW in terms of the 3dB bandwidth of the RBW filter. |
| BandwidthDefinitionBinWidth | 2 | Defines the RBW in terms of the bin width of the spectrum. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemreferencetype.html language=enus -->
## TOPIC 00502: RFmxSpecAnMXSemReferenceType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemreferencetype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemreferencetype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the power reference is the integrated power or the peak power in the closest carrier channel. The leftmost carrier is the carrier closest to all the lower (negative) offset segments. The rightmost carrier is the carrier closest to all the upper (positive) offset segments. SyntaxNam

### RFmxSpecAnMXSemReferenceType Enumeration

Specifies whether the power reference is the integrated power or the peak power in the closest carrier channel. The leftmost carrier is the carrier closest to all the lower (negative) offset segments. The rightmost carrier is the carrier closest to all the upper (positive) offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXSemReferenceType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Integration | 0 | The power reference is the integrated power of the closest carrier. |
| Peak | 1 | The power reference is the peak power of the closest carrier. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchabsolutemasktrace__string-double-ref.html language=enus -->
## TOPIC 00503: FetchAbsoluteMaskTrace(string, double, ref Spectrum< float >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchabsolutemasktrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchabsolutemasktrace__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute mask trace used for SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchAbsoluteMaskTrace(string selectorString, double timeout, ref Spectrum< float > absoluteMask)RemarksThis method maps to the RFmxSpecAn_SEMFetchAbsoluteMaskTrace() function in C.

### FetchAbsoluteMaskTrace(string, double, ref Spectrum< float >)

Fetches the absolute mask trace used for SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchAbsoluteMaskTrace(string selectorString, double timeout, ref Spectrum< float > absoluteMask)

#### Remarks

This method maps to the RFmxSpecAn_SEMFetchAbsoluteMaskTrace() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteMask | ref Spectrum< float > | Upon return, contains the absolute mask trace, in dBm or dBm/Hz, used for the channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchcompositemeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00504: FetchCompositeMeasurementStatus(string, double, out RFmxSpecAnMXSemCompositeMeasurementStatus)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchcompositemeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchcompositemeasurementstatus__string-double-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall SEM measurement status based on the measurement limits and the fail criteria that you set in the SetOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask) method for each offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchCompositeMeasureme

### FetchCompositeMeasurementStatus(string, double, out RFmxSpecAnMXSemCompositeMeasurementStatus)

Fetches the overall SEM measurement status based on the measurement limits and the fail criteria that you set in the [SetOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask)](nationalinstruments-rfmx-specanmx-rfmxspecanmxsemconfiguration-setoffsetlimitfailmask__string-rfmxspecanmxsemoffsetlimitfailmask.html) method for each offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchCompositeMeasurementStatus(string selectorString, double timeout, out RFmxSpecAnMXSemCompositeMeasurementStatus compositeMeasurementStatus)

#### Remarks

This method maps to the RFmxSpecAn_SEMFetchCompositeMeasurementStatus() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| compositeMeasurementStatus | out RFmxSpecAnMXSemCompositeMeasurementStatus | Indicates the overall measurement status based on the measurement limits and the fail criteria that you set in the RFmxSpecAnMXSemOffsetLimitFailMask method for each offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchfrequencyresolution__string-double-out.html language=enus -->
## TOPIC 00505: FetchFrequencyResolution(string, double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchfrequencyresolution__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchfrequencyresolution__string-double-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchFrequencyResolution(string selectorString, double timeout, out double frequencyResolution)RemarksThis method maps to the RFmxSpecAn_SEMFetc

### FetchFrequencyResolution(string, double, out double)

Fetches the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchFrequencyResolution(string selectorString, double timeout, out double frequencyResolution)

#### Remarks

This method maps to the RFmxSpecAn_SEMFetchFrequencyResolution() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete |
| frequencyResolution | out double | Upon return, contains the frequency bin spacing, in Hz, of the spectrum acquired by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00506: FetchLowerOffsetMargin(string, double, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement status and margin from the limit line measured in the lower offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchLowerOffsetMargin(string selectorString, double timeout, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus measurementStatus, out double

### FetchLowerOffsetMargin(string, double, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double)

Fetches the measurement status and margin from the limit line measured in the lower offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchLowerOffsetMargin(string selectorString, double timeout, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Remarks

This method maps to the RFmxSpecAn_SEMFetchLowerOffsetMargin() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxSpecAnMXSemLowerOffsetMeasurementStatus | Indicates the lower offset measurement status based on measurement limits and the fail criteria that you specify in the SetOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask) method. |
| margin | out double | Upon return, contains the margin, in dB, from the limit mask value that you set in the SetOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask) method. Margin is defined as the maximum difference between the spectrum and the limit mask. |
| marginFrequency | out double | Upon return, contains the frequency, in hertz (Hz), at which the margin occurred in the lower (negative) offset. |
| marginAbsolutePower | out double | Upon return, contains the power, in dBm or dBm/Hz, at which the margin occurred in the lower (negative) offset segment. The power is measured in dBm when you set the SetPowerUnits(string, RFmxSpecAnMXSemPowerUnits) method to dBm, and in dBm/Hz when you set the SetPowerUnits(string, RFmxSpecAnMXSemPowerUnits) method to dBmPerHertz. |
| marginRelativePower | out double | Upon return, contains the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00507: FetchUpperOffsetMarginArray(string, double, ref RFmxSpecAnMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement status and margin from the limit line measured in the upper offset segments. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxSpecAnMXSemUpperOffsetMeasurementStatus[] measurementStatus, re

### FetchUpperOffsetMarginArray(string, double, ref RFmxSpecAnMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Fetches the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxSpecAnMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Remarks

This method maps to the RFmxSpecAn_SEMFetchUpperOffsetMarginArray() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the methods waits until the measurement is complete. |
| measurementStatus | ref RFmxSpecAnMXSemUpperOffsetMeasurementStatus[] | Upon return, contains the array of upper offset measurement statuses based on measurement limits and the fail criteria that you specify in the SetOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask) method. |
| margin | ref double[] | Upon return, contains the array of margins, in dB, from the limit mask value that you set in the SetOffsetLimitFailMask(string, RFmxSpecAnMXSemOffsetLimitFailMask) method. Margin is defined as the maximum difference between the spectrum and the limit mask. |
| marginFrequency | ref double[] | Upon return, contains the array of frequencies, in hertz (Hz), at which the margin occurred in each upper (positive) offset. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of powers, in dBm or dBm/Hz, at which the margin occurred in each upper (positive) offset segment. The power is measured in dBm when you set the SetPowerUnits(string, RFmxSpecAnMXSemPowerUnits) method to dBm, and in dBm/Hz when you set the SetPowerUnits(string, RFmxSpecAnMXSemPowerUnits) method to dBmPerHertz. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers, in dB, at which the margin occurred in each upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00508: FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the upper offset segment power measurements. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchUpperOffsetPower(string selectorString, double timeout, out double totalAbsolutePower, out double totalRelativePower, out double peakAbsolutePower, out double peakFrequency, out dou

### FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

Fetches the upper offset segment power measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchUpperOffsetPower(string selectorString, double timeout, out double totalAbsolutePower, out double totalRelativePower, out double peakAbsolutePower, out double peakFrequency, out double peakRelativePower)

#### Remarks

This method maps to the RFmxSpecAn_SEMFetchUpperOffsetPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalAbsolutePower | out double | Upon return, contains the upper (positive) offset segment power measured. |
| totalRelativePower | out double | Upon return, contains the power in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |
| peakAbsolutePower | out double | Upon return, contains the peak power measured in the upper (positive) offset segment. The power is measured in dBm when you set the SetPowerUnits(string, RFmxSpecAnMXSemPowerUnits) method to dBm, and in dBm/Hz when you set the SetPowerUnits(string, RFmxSpecAnMXSemPowerUnits) method to dBmPerHertz. |
| peakFrequency | out double | Upon return, contains the frequency, in hertz (Hz), at which the peak power occurred in the offset segment. |
| peakRelativePower | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00509: GetLowerOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetmarginrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetMarginRelativePower(string selectorString, out double value)Remarks

### GetLowerOffsetMarginRelativePower(string, out double)

Gets the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetMarginRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00510: GetLowerOffsetMeasurementStatus(string, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetmeasurementstatus__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower offset measurement status based on measurement limits and the fail criteria. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus value)RemarksThis method maps to the RFmxSpe

### GetLowerOffsetMeasurementStatus(string, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus)

Gets the lower offset measurement status based on measurement limits and the fail criteria.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxSpecAnMXSemLowerOffsetMeasurementStatus value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetMeasurementStatus() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXSemLowerOffsetMeasurementStatus | Indicates the lower offset measurement status based on measurement limits and the fail criteria. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpeakabsolutepower__string-out.html language=enus -->
## TOPIC 00511: GetLowerOffsetPeakAbsolutePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpeakabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpeakabsolutepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the lower (negative) offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetPeakAbsolutePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetPeakAbsolutePower() function in

### GetLowerOffsetPeakAbsolutePower(string, out double)

Gets the peak power measured in the lower (negative) offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetPeakAbsolutePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetPeakAbsolutePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the lower (negative) offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpeakrelativepower__string-out.html language=enus -->
## TOPIC 00512: GetLowerOffsetPeakRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpeakrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpeakrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetPeakRelativePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMG

### GetLowerOffsetPeakRelativePower(string, out double)

Gets the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetPeakRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetPeakRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpowerreferencecarrier__string-out.html language=enus -->
## TOPIC 00513: GetLowerOffsetPowerReferenceCarrier(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpowerreferencecarrier__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetpowerreferencecarrier__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier index for measured power that was used as reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetPowerRe

### GetLowerOffsetPowerReferenceCarrier(string, out int)

Gets the carrier index for measured power that was used as reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetPowerReferenceCarrier(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetPowerReferenceCarrier() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out int | Upon return, contains the carrier index for measured power that was used as reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetstartfrequency__string-out.html language=enus -->
## TOPIC 00514: GetLowerOffsetStartFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetstartfrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetStartFrequency(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetResultsL

### GetLowerOffsetStartFrequency(string, out double)

Gets the start frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetStartFrequency(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetStartFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Specifies the start frequency, in Hz, of the offset segment relative to the closest configured carrier offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetstopfrequency__string-out.html language=enus -->
## TOPIC 00515: GetLowerOffsetStopFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsetstopfrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetStopFrequency(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetResultsLow

### GetLowerOffsetStopFrequency(string, out double)

Gets the stop frequency, in hertz (Hz), of the offset segment relative to the closest configured carrier offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetStopFrequency(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetStopFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Specifies the stop frequency, in Hz, of the offset segment relative to the closest configured carrier offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsettotalabsolutepower__string-out.html language=enus -->
## TOPIC 00516: GetLowerOffsetTotalAbsolutePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsettotalabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsettotalabsolutepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower (negative) offset segment power measured. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetTotalAbsolutePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetTotalAbsolutePower() function in C.Paramete

### GetLowerOffsetTotalAbsolutePower(string, out double)

Gets the lower (negative) offset segment power measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetTotalAbsolutePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetTotalAbsolutePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the lower (negative) offset segment power measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsettotalrelativepower__string-out.html language=enus -->
## TOPIC 00517: GetLowerOffsetTotalRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsettotalrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getloweroffsettotalrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetTotalRelativePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEM

### GetLowerOffsetTotalRelativePower(string, out double)

Gets the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetTotalRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsLowerOffsetTotalRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getupperoffsetpeakabsolutepower__string-out.html language=enus -->
## TOPIC 00518: GetUpperOffsetPeakAbsolutePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getupperoffsetpeakabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxsemresults-getupperoffsetpeakabsolutepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the upper (positive) offset segment. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUpperOffsetPeakAbsolutePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_SEMGetResultsUpperOffsetPeakAbsolutePower() function in

### GetUpperOffsetPeakAbsolutePower(string, out double)

Gets the peak power measured in the upper (positive) offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperOffsetPeakAbsolutePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_SEMGetResultsUpperOffsetPeakAbsolutePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the upper (positive) offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSemResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxspectrumaveragingtype.html language=enus -->
## TOPIC 00519: RFmxSpecAnMXSpectrumAveragingType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxspectrumaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxspectrumaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectrum measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXSpectrumAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averaged. RM

### RFmxSpecAnMXSpectrumAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spectrum measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXSpectrumAveragingType

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

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00520: SetRangeRbwFilterBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRangeRbwFilterBandwidth(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_SpurSetRangeRBWFilterBandw

### SetRangeRbwFilterBandwidth(string, double)

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter applied to the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRangeRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the range number. Example: "range0". You can use the BuildRangeString2(string, int) method to build the selector string. |
| value | double | Specifies the bandwidth, in Hz, of the RBW filter applied to the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSpurConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidthdefinition__string-rfmxspecanmxspurrbwfilterbandwidthdefinition.html language=enus -->
## TOPIC 00521: SetRangeRbwFilterBandwidthDefinition(string, RFmxSpecAnMXSpurRbwFilterBandwidthDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidthdefinition__string-rfmxspecanmxspurrbwfilterbandwidthdefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidthdefinition__string-rfmxspecanmxspurrbwfilterbandwidthdefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRangeRbwFilterBandwidthDefinition(string selectorString, RFmxSpecAnMXSpurRbwFilterBandwidthDefinition value)Remar

### SetRangeRbwFilterBandwidthDefinition(string, RFmxSpecAnMXSpurRbwFilterBandwidthDefinition)

Sets the bandwidth definition which you use to specify the value of the [SetRangeRbwFilterBandwidth(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerbwfilterbandwidth__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRangeRbwFilterBandwidthDefinition(string selectorString, RFmxSpecAnMXSpurRbwFilterBandwidthDefinition value)

#### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeRBWFilterBandwidthDefinition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the range number. Example: "range0". You can use the BuildRangeString2(string, int) method to build the selector string. |
| value | RFmxSpecAnMXSpurRbwFilterBandwidthDefinition | Specifies the bandwidth definition which you use to specify the value of the SetRangeRbwFilterBandwidth(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSpurConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerelativeattenuation__string-double.html language=enus -->
## TOPIC 00522: SetRangeRelativeAttenuation(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerelativeattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangerelativeattenuation__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation, in dB, relative to the value which you set in the SetExternalAttenuation(string, double) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpub

### SetRangeRelativeAttenuation(string, double)

Sets the attenuation, in dB, relative to the value which you set in the [SetExternalAttenuation(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmx-setexternalattenuation__string-double.html) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRangeRelativeAttenuation(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeRelativeAttenuation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the range number. Example: "range0". You can use the BuildRangeString2(string, int) method to build the selector string. |
| value | double | Specifies the attenuation, in dB, relative to the external attenuation which you set in the SetExternalAttenuation(string, double) method. Use the attenuation to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSpurConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangestartfrequency__string-double.html language=enus -->
## TOPIC 00523: SetRangeStartFrequency(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangestartfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangestartfrequency__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start frequency of the frequency range, in hertz (Hz), for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRangeStartFrequency(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_SpurSetRangeStartFrequency() function in C.Parameters

### SetRangeStartFrequency(string, double)

Sets the start frequency of the frequency range, in hertz (Hz), for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRangeStartFrequency(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_SpurSetRangeStartFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the range number. Example: "range0". You can use the BuildRangeString2(string, int) method to build the selector string. |
| value | double | Specifies the start of the frequency range, in Hz, for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXSpurConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangevbwfilterautobandwidth__string-rfmxspecanmxspurrangevbwfilterautobandwidth.html language=enus -->
## TOPIC 00524: SetRangeVbwFilterAutoBandwidth(string, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangevbwfilterautobandwidth__string-rfmxspecanmxspurrangevbwfilterautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxspurconfiguration-setrangevbwfilterautobandwidth__string-rfmxspecanmxspurrangevbwfilterautobandwidth.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRangeVbwFilterAutoBandwidth(string selectorString, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth value)RemarksThis method sets the val

### SetRangeVbwFilterAutoBandwidth(string, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth)

Sets whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRangeVbwFilterAutoBandwidth(string selectorString, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth value)

#### Remarks

This method sets the value of [SpurRangeVbwFilterAutoBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxspurrangevbwfilterautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the spurrange number. Example: "spurrange0". You can use the BuildRangeString(string, int) method to build the selector string. |
| value | RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth | Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXSpurConfiguration Class
